---
title: "Phase 5.3 Versioning Strategy — Collaborative ZIM Library Management"
project: open-repo
phase: "5.3 design"
status: design-proposal
created: 2026-05-22
author: General Research Agent
depends_on:
  - PHASE_5_ARCHITECTURE.md
  - PHASE_5.2_IMPLEMENTATION_ROADMAP.md
  - FEDERATION_ARCHITECTURE.md
deadline: 2026-05-30
tags: [versioning, collaboration, zim, semantic-versioning, merge-conflict, attribution, community]
---

# Phase 5.3 Versioning Strategy
## Collaborative ZIM Library Management Without Merge Chaos

---

## Executive Summary

Phase 5.1–5.2 treats ZIM files as periodically regenerated snapshots: a pipeline runs weekly, overwrites the previous export, and the CDN serves the latest version. This works when there is one authoritative publisher. It breaks when multiple community libraries want to contribute adaptations — a translation into Haitian Creole, a medical protocol revision by a field physician, an agricultural guide updated for a specific soil type.

Without a versioning strategy, the first contributor to push their changes wins. The second contributor's work is silently discarded. This is the "last write wins" failure mode that destroys collaborative knowledge work.

This document designs a versioning system that enables:
- Multiple community libraries to maintain **domain-authoritative versions** of ZIM content
- Community contributors to propose **patches and corrections** without overwriting the canonical version
- Multiple **language forks** of the same ZIM to evolve independently and merge selectively
- A complete **audit trail** of who changed what, when, and why
- A **conflict resolution process** that is meaningful to non-developers

The design draws on three proven versioning models: Git's object-DAG model (for structural integrity), Wikipedia's revision history (for accessibility to non-developers), and semantic versioning (for consumer clarity about compatibility).

---

## 1. The Versioning Problem in Community Libraries

### 1.1 Why ZIM Files Are Hard to Version

ZIM files are binary archives. Unlike Markdown source files or database records, they are not human-editable and they cannot be merged with standard text diff tools. A ZIM file is the output of a build pipeline that processes structured source content into a compressed, indexed binary format.

This creates a versioning challenge: the natural unit of work for a content contributor is at the article level (editing one procedure, correcting one drug dosage, translating one seed species guide), but the natural unit of distribution is at the ZIM file level (a 50 MB binary containing 3,000 articles).

The versioning strategy must bridge this gap: track changes at the article level, but distribute at the ZIM file level.

### 1.2 Personas and Their Version Needs

**The domain maintainer** (example: a medical librarian at a clinic cooperative) wants to:
- Accept or reject proposed changes to medical articles before they appear in the published ZIM
- Maintain a stable "current" version that their clinics depend on
- Roll back to a previous version if an error is discovered after publication

**The contributor** (example: a field physician reviewing drug dosing tables) wants to:
- Propose a specific correction without affecting other articles
- Know when their proposal was reviewed and whether it was accepted
- Understand why a proposal was rejected

**The translator** (example: a NGO localizing the seed preservation guide for West African farming conditions) wants to:
- Maintain a French/Wolof fork of the seed guide
- Receive upstream updates from the English canonical version when new species are added
- Merge selectively: adopt new species articles, but keep their localized farming instructions for existing species

**The library operator** (example: a school network administrator) wants to:
- Know which version of each ZIM is currently deployed
- Know when a new version is available and what changed
- Roll out updates on a schedule that works for their connection constraints

### 1.3 What Must Not Happen

- A contributor's correction must not silently overwrite another contributor's concurrent correction
- A translator's localized content must not be silently overwritten when the canonical English version is updated
- A library operator must not discover that the ZIM they deployed last week has been silently replaced with a different version (same filename, different content)
- Domain expertise must not be bypassed: a non-medical contributor must not be able to publish a drug dosing table change without medical review

---

## 2. Content Versioning Model

### 2.1 Two-Level Versioning

The system tracks versions at two levels simultaneously:

**Article-level versioning**: Every individual article (one drug monograph, one water procedure, one seed species guide) has its own version history. This is the granular editing layer, analogous to Wikipedia's per-page revision history.

**ZIM-bundle versioning**: Each ZIM file is a snapshot of a specific set of article versions, assembled into a distributable archive. This is the consumer-facing layer, analogous to a software release.

The relationship is explicit: ZIM version `1.3.0` of the medical ZIM is defined by a manifest listing which article version was included for each of its 500 articles. To reproduce ZIM `1.3.0` exactly, you need those specific article versions plus the build pipeline at that point in time.

### 2.2 Semantic Versioning for ZIM Bundles

Each ZIM bundle uses semantic versioning: `MAJOR.MINOR.PATCH`.

| Version component | Increment when | Examples |
|---|---|---|
| MAJOR | A fundamental change in the ZIM's structure, scope, or trust model. Consumers may need to update their workflows. | Switching from Imperial to metric measurements; removing a deprecated domain; a breaking change in article URL scheme |
| MINOR | New articles added, existing articles substantially revised, new language or domain coverage. Content is expanded or improved. | Adding 50 new seed species; updating drug dosages from WHO 2024 guidelines; adding French translations |
| PATCH | Corrections to existing articles that do not change their structure or scope. Typo fixes, citation corrections, formatting improvements. | Fixing a mispelled plant name; correcting a processing time that was transcribed incorrectly; updating a broken link |

**Why this matters for consumers**: A library operator running a low-bandwidth connection can confidently update PATCH versions (small deltas, low risk). MINOR updates require a review step. MAJOR updates may require the operator to communicate changes to their community.

The version appears in the ZIM filename and metadata:
```
open-repo_en_medical_2026-05_v1.3.2.zim
```

### 2.3 Article Version Identity

Each article version is identified by:
1. A **content hash** (SHA-256 of the article's canonical content): proves the content is unchanged from when it was reviewed
2. A **version number** (integer sequence per article): enables ordering without timestamps
3. A **parent hash**: the content hash of the article version this one was derived from. Enables a DAG (directed acyclic graph) of article lineage, analogous to Git commits.

```json
{
  "article_id": "medical:drug-amoxicillin",
  "version_number": 7,
  "content_hash": "sha256:4a5f3c...",
  "parent_hash": "sha256:2b8e1a...",
  "authored_by": "LIBID-5mfFqPJmzGGHGjHx...",
  "authored_at": "2026-05-20T10:23:00Z",
  "change_summary": "Updated adult dosing from WHO 2024 guidelines; added pediatric weight-based table",
  "review_status": "approved",
  "reviewed_by": "LIBID-KpBJNzHQnERQ4...",
  "domain_authority": "medical"
}
```

The `parent_hash` chain enables reconstruction of the full edit history for any article and detection of branching (two edits both claiming the same parent — the definition of a merge conflict).

---

## 3. Collaborative Editing Workflows

### 3.1 The Contribution Pipeline (Pull Request Equivalent)

A contributor who wants to improve an article follows this workflow, regardless of whether they are a developer:

**Step 1: Fork.** The contributor's library fetches the current article content from the canonical source library. The fork is recorded: the contributor's copy explicitly states "derived from version 7 of article `medical:drug-amoxicillin` from Library `LIBID-5mfFqP...`".

**Step 2: Edit.** The contributor makes changes. The editing interface (discussed in section 3.4) records each change at the article level. Changes are saved locally in the contributor's library node and are not published yet.

**Step 3: Propose.** The contributor submits a **Change Proposal** to the domain authority. A Change Proposal is a signed document containing:
- The original article version (parent hash)
- The proposed new content (full text or structured diff)
- A human-readable summary of what changed and why
- Any supporting references (citations, guideline updates)
- The contributor's Library ID and reputation context (how many prior contributions, how many were accepted)

**Step 4: Review.** The domain authority reviews the proposal. For medical content, this means a qualified reviewer examines the proposed change against source guidelines. For seed data, this might mean a cross-check against the GRIN database. For translations, this means a speaker of the target language reviews for accuracy and cultural appropriateness.

The review produces one of three outcomes:
- **Accept**: The proposal is merged into the canonical article as a new version. The contributor is credited in the attribution chain.
- **Accept with modifications**: The reviewer accepts the change but adds corrections. Both the original contributor and the reviewer are credited.
- **Reject with explanation**: The proposal is declined with a written rationale. The contributor's Library ID and the explanation are both logged. The contributor can revise and resubmit.

**Step 5: Publish.** Once enough article changes have accumulated (or on the weekly schedule), the domain authority runs the ZIM build pipeline, generating a new ZIM version that incorporates all accepted changes. The new ZIM is signed, manifested, and published via the federation protocol.

### 3.2 Branching: Language and Regional Forks

When a community localizes ZIM content — translating to a different language, adapting procedures for a specific regional context, or creating a variant for a particular deployment (a school curriculum vs. a clinic reference) — they create a **branch**.

A branch is a named fork of the canonical ZIM with its own version sequence:
```
open-repo_fr_medical_2026-05_v1.0.0.zim   # French branch
open-repo_en-us-appalachian_seed_v1.2.0.zim  # Regional US variant
```

Branches are first-class entities in the versioning system. They have their own maintainers, their own version sequences, and their own publishing schedules. A branch maintainer is not required to stay in sync with the canonical version — divergence is a legitimate and expected state.

However, branches can optionally declare an **upstream tracking relationship** with the canonical version. A tracking branch:
- Receives notifications when new articles or article versions are published in the canonical
- Has tooling to identify which upstream changes have been incorporated and which have not
- Can perform **selective merges**: pull specific new articles from the canonical while preserving local adaptations of existing articles

This is analogous to how Wikipedia language editions work: the French Wikipedia is not a translation of the English Wikipedia — it is an independent encyclopedia that happens to cover many of the same topics. Some articles are translated from English; others are written independently in French; others cover French-specific topics not present in English at all.

### 3.3 Merge Conflict Resolution

A merge conflict occurs when two parties have independently modified the same article. This can happen when:
- Two contributors both propose changes to the same article concurrently
- A branch maintainer's local adaptation of an article conflicts with a canonical update to the same article
- Two libraries merge their collections and discover they have different versions of the same article

The resolution strategy depends on the type of conflict:

**Type 1: Minor concurrent edits (non-overlapping changes)**
If Contributor A edited paragraphs 1 and 3, and Contributor B edited paragraph 2 of the same article, and the changes do not interact logically, a three-way merge can combine both edits automatically. The merged version lists both contributors. The domain authority reviews and approves the merged result before publication.

**Type 2: Overlapping edits (same content, different choices)**
If Contributor A changed a drug dosage to "500 mg" and Contributor B independently changed it to "400 mg", there is no automatic resolution. The domain authority must decide. The resolution protocol:
1. Both proposed values are presented to the reviewer side by side
2. The reviewer's decision is recorded with a rationale
3. The losing proposal is preserved in the history (not deleted) with a note explaining the decision
4. Both contributors receive notification of the resolution

**Type 3: Branch divergence (localized content vs. upstream update)**
A French branch has adapted an article significantly for French medical practice. The English canonical version of the same article has been substantially revised. The branch maintainer receives a notification with a diff showing what changed in the canonical. They decide:
- **Accept upstream entirely**: Replace the French article with a translation of the new English version
- **Accept specific changes**: Pull specific revisions from the English version (updated drug dosing tables) while retaining French-specific content
- **Reject upstream**: Keep the French version as-is and mark the upstream change as "reviewed and not adopted"

The third option is legitimate — a localized version may intentionally diverge from the canonical for valid reasons. The important thing is that the divergence is explicit and documented, not accidental.

**Domain specialist authority**: For safety-critical domains (medical, food safety), the domain authority has final say over conflict resolution in the canonical version. Community voting may inform the decision but does not override it. A medical reviewer who determines that a proposed change to a drug dosage is incorrect can reject it regardless of community sentiment. This reflects the same authority structure used in Wikipedia's featured article review process: community input is valued, but expert review is required for certain content.

### 3.3.1 Why CRDTs Are Not the Right Model Here

Conflict-Free Replicated Data Types (CRDTs) are often proposed for offline collaborative editing because they enable automatic merge without conflicts. The key property of a CRDT is that any two replicas, having received the same set of operations in any order, converge to the same state deterministically — no manual merge required.

For general-purpose collaborative text editing (Apple Notes sync, Google Docs offline mode), CRDTs are the correct choice. They are inappropriate for open-repo content for three reasons:

**1. Semantic validity is not derivable from merge operations.** A CRDT text merge of two edits to a drug dosage table would produce a syntactically valid result, but the dosage it contains might be neither of the two proposed values — it could be a malformed combination. For safety-critical content, "the algorithm produced a deterministic merged state" is not a sufficient review standard. A human reviewer must evaluate the merged content regardless.

**2. Domain authority intentionally introduces asymmetry.** CRDTs model all participants as equal peers. Open-repo's authority model is deliberately hierarchical: the domain authority's version of safety-critical fields is canonical, not one of two equal alternatives. Any merge strategy that treats a field physician's proposed dosage change as automatically mergeable with the WHO guideline is architecturally wrong for this domain.

**3. The editing unit is the entire article, not individual characters.** CRDTs work at the character or operation level. Articles in open-repo are semantic units (a drug monograph, a seed species guide) where the meaningful conflict unit is the entire field (dosage, storage temperature, toxicity classification) — not individual characters. The parent-hash chain model already captures this granularity correctly.

The right CRDT insight to carry forward: the **append-only audit log** (section 5.2) uses a hash-chained append structure that shares the tamper-evidence property of state-based CRDTs, without imposing automatic merge semantics. Operation-based CRDTs are useful inspiration for the delta manifest format in `DIFFERENTIAL_SYNC_PROTOCOL.md` (operations rather than full state transfers), but not for content conflict resolution itself.

### 3.4 Editing Interface Considerations for Non-Developers

The versioning system described above is technically sound but requires a usable interface for librarians who are not software developers. The current Phase 5.1–5.2 pipeline is developer-facing. Phase 5.3 needs a lightweight editing interface.

The minimum viable editing interface is not a web application — it is a structured template. Article content is maintained in structured JSON or YAML files with clear field definitions. A librarian with a text editor can:
- Open the article file, read the current content, and modify specific fields
- Fill in the `change_summary` field explaining what they changed
- Run a simple validation script that checks the required fields are present
- Submit the changed file as a Change Proposal via email or a web form

For communities with low technical literacy, the interface shifts to pre-formatted templates in the language of the community, with instructions for how to fill in corrections and who to send them to. The domain authority's maintainer receives these proposals and enters them into the system.

This is lower-tech than a GitHub pull request, but it is appropriate for the target deployment context. A clinic in rural Uganda cannot be expected to use Git. They can be expected to fill out a correction form.

---

## 4. Integration with Phase 5 Domain Structure

### 4.1 How Each Domain Handles Versioning

**Medical Reference** (highest stakes, strictest review)
- Domain authority: designated medical reviewer (established in Phase 5.2 Wave 0)
- Version gate: all MINOR and MAJOR version changes require medical review sign-off before the new ZIM is published
- PATCH-only releases can be published on a 48-hour review cycle
- Article types with mandatory review: drug monographs (any change), dosing tables (any change), procedure protocols (any change)
- Article types with lighter review: editorials, background context, resource lists

**Water Systems**
- Domain authority: cooperative of library maintainers, majority approval for changes
- Version gate: safety-critical parameters (acceptable turbidity, disinfection times, chemical concentrations) require two independent approvals
- Non-safety content (historical context, equipment descriptions) requires one approval

**Seed Preservation**
- Domain authority: distributed — different libraries may be authoritative for different species or regions
- GRIN accession data is treated as authoritative source; any change to GRIN-sourced fields requires a GRIN citation
- Regional adaptations (planting schedules, storage conditions) are tracked as branch content, not canonical

**Food Preservation**
- Domain authority: USDA guidelines are the final arbiter for processing times and safety parameters
- No change to processing times or safety thresholds without a USDA edition citation
- Structural changes (adding new food types, new jar sizes) require the USDA data to support the addition

**Botanical Knowledge**
- Domain authority: split by edibility/toxicity classification vs. general botanical information
- Safety-critical classifications (edible, poisonous, toxic look-alike) require two approvals and mandatory source citations
- Evidence levels (A/B/C) for medicinal claims are set conservatively and require explicit upgrade citations

### 4.2 Multi-Language Versioning Example

The seed preservation guide exists in English (canonical) and is being adapted into French and Swahili by two different library cooperatives. Each language version has its own version sequence:

```
open-repo_en_seed-preservation_v1.3.0.zim   # English canonical
open-repo_fr_seed-preservation_v1.1.0.zim   # French fork (tracks English 1.1)
open-repo_sw_seed-preservation_v1.0.0.zim   # Swahili fork (initial translation)
```

When the English canonical releases v1.4.0 (adding 80 new species from East Africa), both the French and Swahili fork maintainers receive an update notification. The Swahili maintainers may choose to fast-track these articles (they are directly relevant to their community). The French maintainers review each new article and translate those relevant to French-speaking African contexts.

The key invariant: both forks remain valid independently-versioned ZIM files. A library can deploy the Swahili fork without any reference to the English canonical. The tracking relationship is a convenience for fork maintainers, not a dependency.

### 4.3 Version Compatibility in the ZIM Catalog

The OPDS catalog (Phase 5.1) and signed manifest (Phase 5.3 FEDERATION_ARCHITECTURE) both include version information. A library operator can:
- See which version of each domain ZIM they are running
- See what version is available from trusted peers
- See a summary of what changed between their current version and the latest available
- Choose to update or stay on the current version

The OPDS entry for a ZIM includes:
```xml
<entry>
  <title>Seed Preservation Guide — English v1.3.0</title>
  <id>urn:open-repo:seed-preservation:eng:1.3.0</id>
  <updated>2026-05-01T00:00:00Z</updated>
  <summary>Added 120 heritage grain varieties. Updated storage temperature ranges from new GRIN data.</summary>
  <open-repo:version>1.3.0</open-repo:version>
  <open-repo:previous-version>1.2.0</open-repo:previous-version>
  <open-repo:delta-available>true</open-repo:delta-available>
  <link rel="acquisition" href="...seed-preservation_v1.3.0.zim"/>
  <link rel="related" title="delta from 1.2.0" href="...seed-preservation_v1.2.0-to-v1.3.0.zimdiff"/>
</entry>
```

---

## 5. Attribution and Audit Trails

### 5.1 Attribution Model

Every article version records the chain of attribution from its original creation:

```json
{
  "attribution": [
    {
      "library_id": "LIBID-originating-library",
      "role": "author",
      "article_version": 1,
      "timestamp": "2026-01-15T00:00:00Z"
    },
    {
      "library_id": "LIBID-fr-translation-cooperative",
      "role": "translator",
      "article_version": 2,
      "timestamp": "2026-03-20T00:00:00Z"
    },
    {
      "library_id": "LIBID-medical-reviewer",
      "role": "reviewer",
      "article_version": 2,
      "timestamp": "2026-03-22T00:00:00Z"
    }
  ]
}
```

The attribution chain is preserved in the ZIM article metadata (visible in the rendered HTML's footer) and in the article version record. Attribution is:
- **Permanent**: once credited, a contributor cannot be removed from the chain
- **Granular**: credited at the article level, not the ZIM level
- **Role-differentiated**: authorship, translation, review, and data-sourcing are distinct roles

Attribution in the ZIM article footer renders as plain text (no JavaScript required for offline reading):
```
Originally authored by: Appalachian Seed and Skills Library
Translated to French by: West Africa Library Cooperative
Medical review: Rural Health Cooperative, Dr. M. Diallo
Last updated: May 2026
```

### 5.2 Immutable Audit Log

All version events — proposals, approvals, rejections, merges, and key rotation events — are appended to a local immutable audit log. The log uses hash chaining (each entry contains the SHA-256 hash of the previous entry) to make tampering detectable.

```json
{
  "entry_id": 1247,
  "prev_hash": "sha256:4f3c8a...",
  "event_type": "change_proposal_rejected",
  "article_id": "medical:drug-amoxicillin",
  "proposal_hash": "sha256:b2e9f1...",
  "actor_library_id": "LIBID-contributor-X",
  "reviewer_library_id": "LIBID-medical-authority",
  "reason": "Proposed dosage exceeds WHO maximum for pediatric patients under 20 kg",
  "timestamp": "2026-05-18T14:33:00Z",
  "entry_hash": "sha256:9d7a4c..."
}
```

The audit log is **not federated** (it contains information that may be sensitive, such as rejected proposals and the reasons for rejection). However, a library can choose to share aggregate audit statistics with trusted peers: "we have reviewed 47 proposals this month; 38 accepted, 9 rejected."

The hash-chained log enables detection of retroactive tampering: if any entry in the log is modified, all subsequent entry hashes will no longer match. This is the same tamper-evidence mechanism used in certificate transparency logs and blockchain systems, without requiring a blockchain.

### 5.3 License Compatibility

Content in the open-repo ZIM ecosystem uses open licenses. The versioning system must track license provenance to ensure that content combining materials from multiple sources remains license-compatible.

Each article version includes:
- `license`: SPDX identifier (e.g., `CC-BY-SA-4.0`, `CC0-1.0`, `public-domain`)
- `source_citations`: list of source documents with their licenses
- `license_note`: any special permissions or restrictions

The ZIM build pipeline validates license compatibility before assembling articles into a ZIM bundle. It rejects combinations that would create license incompatibilities (e.g., including a CC-BY-NC article in a bundle with a Creative Commons license that permits commercial use).

---

## 6. Design Trade-offs

| Trade-off | Choice Made | Alternative Rejected | Reason |
|---|---|---|---|
| **Git for source control vs. custom version model** | Custom article-level versioning | Git repository for ZIM source | Git requires developer tooling; custom model can be simplified for non-technical contributors |
| **Automatic three-way merge vs. always-manual review** | Automatic for non-overlapping; manual for overlapping | Always manual | Non-overlapping changes have no meaningful conflict; manual review for those adds only process friction |
| **Domain authority veto vs. community voting** | Domain authority has final say on safety-critical content | Pure community voting | Medical and food safety content can cause harm if incorrect; expertise must be in the authority structure |
| **Granular article versioning vs. whole-ZIM versioning** | Both (articles track at article level; ZIM has semantic version) | ZIM-only versioning | Whole-ZIM versioning cannot represent partial updates or selective merges |
| **Attribution by individual vs. by library** | By Library ID (institution-level) | By individual user | Individual users may leave organizations; Library IDs are stable institutional identifiers |
| **Open contribution vs. invitation-only** | Open proposal (anyone can propose); gated acceptance | Fully open commit | Prevents content pollution; maintains quality without blocking participation |

---

## 7. Implementation Notes

### 7.1 Minimal Database Schema

The versioning system requires these new tables (beyond the Phase 5.1 export pipeline):

```
article_versions
  - article_id (text, namespaced: domain:slug)
  - version_number (integer)
  - content_hash (text, SHA-256)
  - parent_hash (text, nullable for version 1)
  - authored_by (text, Library ID)
  - authored_at (timestamp)
  - change_summary (text)
  - review_status (enum: proposed, approved, rejected)
  - reviewed_by (text, Library ID, nullable)
  - domain_authority (text, domain name)

change_proposals
  - proposal_id (UUID)
  - article_id (text)
  - base_version_hash (text)
  - proposed_content_hash (text)
  - proposed_by (text, Library ID)
  - proposed_at (timestamp)
  - proposal_summary (text)
  - status (enum: pending, accepted, accepted-modified, rejected)
  - resolution_note (text, nullable)
  - resolved_by (text, Library ID, nullable)
  - resolved_at (timestamp, nullable)

zim_bundle_manifests
  - zim_name (text)
  - version (text, semantic version)
  - articles (JSON array of {article_id, version_number, content_hash})
  - built_at (timestamp)
  - built_by (text, Library ID)
  - cid (text, IPFS CID)
  - sha256 (text)

audit_log
  - entry_id (integer, auto-increment)
  - prev_hash (text)
  - event_type (text)
  - payload (JSON)
  - timestamp (timestamp)
  - entry_hash (text)
```

### 7.2 ZIM Build Reproducibility

For a ZIM version to be reproducible from its manifest, the build pipeline must be deterministic: the same set of article versions must always produce the same ZIM file (and therefore the same CID). This requires:

- Deterministic article ordering in the ZIM (alphabetical by article path)
- Deterministic HTML rendering (no timestamps or session IDs in the rendered HTML)
- Pinned build tool versions (specific libzim version)
- Reproducible compression (same Zstandard compression level and seed)

Reproducible builds are important for trust: a community library that receives a ZIM and its manifest should be able to verify that the ZIM was actually built from the claimed article versions by building it themselves from the source articles and comparing CIDs.

### 7.3 Cross-reference to Differential Sync

The versioning system integrates with the differential sync protocol (`DIFFERENTIAL_SYNC_PROTOCOL.md`) at the ZIM bundle level. When a new PATCH or MINOR version of a ZIM is published, the export pipeline also generates a delta patch from the previous version to the new version. This delta patch is referenced in the OPDS catalog entry and manifest, enabling bandwidth-efficient updates.

### 7.4 Phase 5.2 to Phase 5.3 Activation Sequence

The versioning system described here activates incrementally, keyed to Phase 5.2 milestones. Nothing in this document requires Phase 5.2 to be complete before Phase 5.3 versioning infrastructure begins.

**Activates when Phase 5.2 Wave 0 completes (domain content sourcing)**:
- `article_versions` and `zim_bundle_manifests` tables can be created — they don't require domain ZIM content to exist yet
- Domain authority assignments (which library is authoritative for medical, water, seed) can be established
- The `change_proposals` workflow can accept its first test submissions even on stub content

**Activates when Phase 5.2 Wave 1 completes (first ZIM exports)**:
- Semantic versioning begins: the first ZIM export is `v1.0.0`
- Attribution metadata (section 5.1) can be embedded in the ZIM's article HTML footers from the first export
- Delta manifest generation activates (the first delta will be from empty → v1.0.0, establishing the baseline)

**Activates when Phase 5.2 Wave 2 completes (all 5 domains in production)**:
- Multi-language branch tracking can begin (the English canonical is established)
- The public version catalog (OPDS with version fields, section 4.3) is fully populated
- PATCH/MINOR/MAJOR version semantics become operationally meaningful because the content is stable enough for community contributors to propose changes

**Remains in Phase 5.3 scope regardless of Phase 5.2 timing**:
- The contribution pipeline (fork → edit → propose → review → publish) requires a web-based editing interface that is Phase 5.3 new work, not Phase 5.2 work
- Key rotation procedures (section 3.4 of FEDERATION_ARCHITECTURE.md) are tested after library identity is established in Phase 5.3a
- The immutable audit log hash-chain bootstrap requires a Phase 5.3a implementation decision on the chain anchoring mechanism (a genesis entry signed by the domain authority's key)

---

## Sources

- [MediaWiki Revision Table — Manual:revision table](https://www.mediawiki.org/wiki/Manual:Revision_table)
- [Help:Edit conflict — MediaWiki](https://www.mediawiki.org/wiki/Help:Edit_conflict)
- [Help:Merge history — MediaWiki](https://www.mediawiki.org/wiki/Help:Merge_history)
- [Wikipedia:History merging — Wikipedia](https://en.wikipedia.org/wiki/Wikipedia:History_merging)
- [Git Delta Compression Technical Deep Dive — LinkedIn](https://www.linkedin.com/pulse/gits-delta-compression-algorithm-technical-deep-dive-maheshwari)
- [Git Object Database and Pack Files — Geek Workbench](https://geekworkbench.com/blog/technical/git-object-database-pack-files/)
- [Offline-First Mobile Architecture — JAIGS 2025](https://www.researchgate.net/publication/393910615_Offline-First_Mobile_Architecture_Enhancing_Usability_and_Resilience_in_Mobile_Systems)
- [Offline sync and conflict resolution patterns — Sachith Dassanayake (2026)](https://www.sachith.co.uk/offline-sync-conflict-resolution-patterns-architecture-trade%E2%80%91offs-practical-guide-feb-19-2026/)
- [Conflict-Free Replicated Data Types (CRDTs) — arXiv survey (Shapiro et al.)](https://arxiv.org/pdf/1805.06358)
- [CRDT Implementation Guide — Velt (October 2025)](https://velt.dev/blog/crdt-implementation-guide-conflict-free-apps)
- [Approaches to CRDTs — ACM Computing Surveys (2024)](https://dl.acm.org/doi/full/10.1145/3695249)
- [TypeScript CRDT Toolkits for Offline-First Apps — Medium](https://medium.com/@2nick2patel2/typescript-crdt-toolkits-for-offline-first-apps-conflict-free-sync-without-tears-df456c7a169b)
- [Kiwix/ZIM incremental updates — MediaWiki](https://www.mediawiki.org/wiki/Kiwix/ZIM_incremental_updates)
- [Scuttlebutt Protocol Guide — SSBC (append-only feed model)](https://ssbc.github.io/scuttlebutt-protocol-guide/)
- [Phase 5 Architecture — open-repo project](./PHASE_5_ARCHITECTURE.md)
- [Phase 5.2 Implementation Roadmap — open-repo project](./PHASE_5.2_IMPLEMENTATION_ROADMAP.md)
- [Federation Architecture — open-repo project](./FEDERATION_ARCHITECTURE.md)
