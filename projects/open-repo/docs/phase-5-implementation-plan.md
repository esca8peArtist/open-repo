---
title: "Phase 5: Implementation Plan"
project: open-repo
phase: 5
status: active-planning
date: 2026-04-28
author: research-agent
confidence: high
tags: [implementation, planning, timeline, dependencies, risks, phase-5]
---

# Phase 5: Offline Export — Implementation Plan

Phase 5 delivers open-repo's offline distribution capability: users can download the knowledge
library as a self-contained ZIM file and read it with Kiwix on any device, with or without internet
access. This document is the implementation plan for the engineering team: scope, dependency tree,
effort estimates, integration checkpoints with Phase 4, known risks, success criteria, and
post-launch maintenance.

**Current status** (as of 2026-04-28): Preliminary phase in progress. Phase 4 PR #1 is in review.
All foundational infrastructure (module stubs, test harness, documentation, CDN configuration) is
being prepared now so that full implementation can begin the day PR #1 merges.

---

## 1. High-Level Scope

Phase 5 builds four things:

**1. ZIM Export Pipeline**: A Python background job that queries the open-repo database, renders
content items as self-contained HTML, and packages them into a ZIM file using python-libzim. Output
is validated with `zimcheck` and uploaded to Cloudflare R2.

**2. OPDS Catalog Endpoint**: A FastAPI endpoint at `/opds/v2/root.xml` that exposes available ZIM
files as an OPDS Atom feed, enabling Kiwix's in-app library browser to discover and download
open-repo exports.

**3. Export API**: REST endpoints for triggering export jobs, checking job status, listing available
exports, and downloading ZIM files. Supports the three export variants: Full, Domain-Specific, and
Reference.

**4. User Documentation**: Step-by-step guides for downloading and using open-repo offline on
Kiwix Android, Kiwix desktop (Windows/macOS/Linux), and institutional kiwix-serve deployments.

---

## 2. Dependency Tree

Components must be built in this order. Items at the same level can be built in parallel.

```
Level 0 (Prerequisites — must be complete before Phase 5 starts):
  [Phase 4 PR #1 merged]
  [python-libzim added to pyproject.toml]
  [feedgen added to pyproject.toml]
  [boto3/cloudflare SDK added to pyproject.toml]
  [Cloudflare R2 bucket provisioned]

Level 1 (Can start now — preliminary work):
  [ZimMetadata + ZimEntry + ZimWriter stub classes]
  [OPDSGenerator stub class]
  [ExportConfig + ExportScope models]
  [zim_exports DB schema migration]
  [CDN deployment configuration templates]
  [Test harness with mock data]

Level 2 (Requires Phase 4 data model):
  [ContentItem query layer for export]
  [HTML template for ZIM articles]
  [is_local field migration on ContentItem]
  [Export scope filtering (LOCAL_ONLY vs FEDERATED)]

Level 3 (Requires Level 1 + Level 2):
  [ZimWriter full implementation]
  [ExportJob background task]
  [zimcheck subprocess validation]
  [SHA-256 checksum computation]
  [R2 upload integration]

Level 4 (Requires Level 3):
  [Export API endpoints (POST /api/exports, GET /api/exports/{job_id})]
  [OPDS catalog endpoint (/opds/v2/root.xml)]
  [Retention policy implementation]
  [Scheduled export jobs (APScheduler/Celery Beat)]

Level 5 (Requires Level 4):
  [User documentation (3 platforms)]
  [OPDS catalog submission to openzim/zim-requests]
  [End-to-end production validation]
  [Performance benchmarks]
```

---

## 3. Effort Estimates

### Preliminary Phase (now — parallel with PR #1 review): 10-14 days

| Component | Effort | Status |
|---|---|---|
| Kiwix Integration Guide (`docs/phase-5-kiwix-integration-guide.md`) | 0.5 day | Complete |
| Export Strategy Document (`docs/phase-5-export-strategy.md`) | 0.5 day | Complete |
| ZimWriter stub module (`src/export/zim_writer.py`) | 1.5 days | Complete |
| OPDSGenerator stub module (`src/export/opds_generator.py`) | 1.5 days | Complete |
| CDN deployment config template (`infrastructure/cdn-deployment.yaml`) | 1 day | Complete |
| Integration test harness (`tests/integration/test_export_pipeline.py`) | 2 days | Complete |
| Implementation plan (this document) | 0.5 day | Complete |
| **Preliminary total** | **7.5 days** | **Complete** |

### Full Implementation Phase (after PR #1 merges): 14-23 days

Based on the Session 546 estimate (15-23 days core) plus Phase 5 production architecture additions
(9-14 days per `phase-5-offline-export-architecture.md`), filtered to MVP scope:

| Component | Estimate |
|---|---|
| ContentItem query layer + HTML template rendering | 3-5 days |
| ZimWriter full implementation (with python-libzim) | 3-5 days |
| Export background job (Celery/APScheduler) + DB schema | 2-3 days |
| R2 upload integration + retention policy | 1-2 days |
| Export API endpoints (create, status, list, download) | 2-3 days |
| OPDS catalog endpoint (feedgen-based, FastAPI) | 1-2 days |
| Scheduled exports (cron config) | 0.5-1 day |
| User documentation (3 platforms) | 1-2 days |
| CI/CD integration (zimcheck in pipeline) | 0.5-1 day |
| End-to-end testing and production validation | 2-3 days |
| **Full implementation total** | **16-27 days** |

**Total Phase 5 effort (preliminary + full)**: 24-35 days.

The wide range reflects:
- Unknown complexity of HTML template adaptation for offline context (self-contained CSS)
- Whether APScheduler or Celery Beat is already present from Phase 4
- Complexity of OPDS catalog submission and Kiwix catalog testing

---

## 4. Integration Checkpoints with Phase 4

### Checkpoint 1: PR #1 Merge (blocking)

The full implementation phase cannot start until Phase 4 PR #1 is merged. This provides:
- `ContentItem` model with `domain` and `is_local` fields
- `FederationPartner` model and federation state management
- ActivityPub endpoints (not directly used by Phase 5, but part of the merged codebase)
- Alembic migration history that Phase 5 migrations must extend

**Action at merge**: Run `uv run pytest` to confirm all existing tests pass. Then begin Level 2
work (ContentItem query layer).

### Checkpoint 2: API Contract Validation (day 3 of full implementation)

Before building the HTML rendering layer, validate the actual `ContentItem` content structure
against the assumptions in `ZimWriter.add_article()` stubs. Check:
- Does `content_jsonld` contain `language` field? (assumed: `{"language": ["en"]}`)
- Does `content_jsonld` contain `steps` for procedures? (assumed: `[{stepNumber, title, body}]`)
- What is the actual domain vocabulary? (assumed from models.py: any string, not enum-constrained)

Resolve any schema mismatches before building the full HTML template.

### Checkpoint 3: First ZIM Passes zimcheck (day 8 of full implementation)

Generate a 10-50 item ZIM file from real data. Run `zimcheck output.zim`. This is the first
integration milestone. All Phase 5 subsequent work assumes this checkpoint passes.

**Known zimcheck failure modes to watch for**:
- Missing `Illustration_48x48` (prepare 48x48 PNG before this checkpoint)
- Non-UTF-8 characters in metadata fields (sanitize all string inputs)
- Articles with no `get_title()` return (every item must have a non-empty title)
- Broken internal links (ZIM path references must be URL-encoded correctly)

### Checkpoint 4: First Production Export Deployed (day 15-18 of full implementation)

A full export ZIM is generated, validated, uploaded to R2, and accessible at the public URL.
The OPDS endpoint returns a valid catalog entry for this export. Manual test: download the ZIM
in Kiwix Android and browse content.

### Checkpoint 5: OPDS Catalog Submission (post-launch)

After Phase 5 is stable and the first 2-3 production exports have been generated and manually
validated in Kiwix apps, submit to the official Kiwix catalog via openzim/zim-requests.

---

## 5. Known Risks and Mitigations

| Risk | Probability | Impact | Mitigation |
|---|---|---|---|
| python-libzim version conflict with existing dependencies | Low | Medium | Pin `libzim>=3.2,<4.0`. Test in clean venv before adding to pyproject.toml. |
| ZIM file size exceeds CDN free tier (>10 GB) | Low (Phase 5 MVP) | Low | At MVP scale (<100 MB per export), no risk. Monitor R2 storage; alert at 8 GB. |
| OPDS XML namespace errors causing Kiwix rejection | Medium | Medium | Validate OPDS XML with feedgen's built-in linting. Test catalog against kiwix-serve in CI. |
| Android Kiwix Play Store restrictions on user-downloaded ZIMs | Medium | Low | Document F-Droid Kiwix path. Provide in-app OPDS catalog as primary UX. |
| HTML template produces external dependencies (CDN CSS/JS) | Medium | High | CI test: parse exported HTML with BeautifulSoup, fail if `src` or `href` starts with `http`. |
| ContentItem `content_jsonld` schema more complex than assumed | Medium | Medium | Checkpoint 2 (API contract validation) catches this before HTML template work. |
| zimcheck rejects export for non-obvious reason | Low | Medium | Run zimcheck in CI with `--verbose`. Test known-good minimal ZIM first. |
| Celery/APScheduler not present in Phase 4 codebase | Medium | Low | Use FastAPI BackgroundTasks for MVP; migrate to Celery if needed for scheduling reliability. |
| UUID instability across export runs | Low | Medium | Store UUID in `zim_exports` table. Pass to Creator explicitly (see architecture doc). |
| Federated content missing attribution metadata | Low | High | Fail export job if any federated item lacks `source_url`. Unit test this path. |

---

## 6. Success Criteria for Full Phase 5 Completion

Phase 5 is complete when all of the following are true:

**Functional**:
- [ ] `POST /api/exports` triggers a background export job and returns a job ID
- [ ] Full export ZIM (`open-repo_en_nopic_YYYY-MM.zim`) passes `zimcheck` with zero warnings
- [ ] Domain-specific exports work for at least 3 domains
- [ ] Exported ZIM opens in Kiwix Android (F-Droid variant) and all articles are readable
- [ ] Exported ZIM opens in Kiwix desktop (Linux) and full-text search returns relevant results
- [ ] kiwix-serve can serve the ZIM from Docker; articles accessible via browser
- [ ] OPDS endpoint at `/opds/v2/root.xml` returns valid Atom XML accepted by feedgen validator
- [ ] SHA-256 checksum sidecar file published alongside each ZIM export

**Infrastructure**:
- [ ] Cloudflare R2 bucket provisioned with correct CORS and cache headers
- [ ] Scheduled export job runs weekly without manual intervention
- [ ] Retention policy deletes superseded exports older than 30 days
- [ ] Monthly storage cost is under $5

**Quality**:
- [ ] All new code has ≥90% test coverage
- [ ] Integration test harness passes with zero external network calls
- [ ] No external HTTP references in exported ZIM HTML (CI enforced)
- [ ] Accessibility: all images have alt text, heading hierarchy is correct

**Distribution**:
- [ ] Public download URL documented in open-repo's README
- [ ] User guide covers Android, desktop, and kiwix-serve deployment
- [ ] OPDS catalog submission made to openzim/zim-requests (even if not yet accepted)

**Storage target**: Total ZIM storage < 500 MB per month at Phase 5 MVP scale (<$0.01/month).
**Cost ceiling**: Total monthly cost (storage + bandwidth) < $20/month.

---

## 7. Post-Launch Maintenance Plan

### 7.1 Update Frequency

- `nopic` full export: weekly (Sunday 02:00 UTC, automated)
- `all` full export: monthly (1st of month, 03:00 UTC, automated)
- Domain exports: weekly, automated
- Reference exports: manual, triggered by major milestones

Review cadence: Monthly review of export sizes, zimcheck results, and CDN costs. If any metric
exceeds threshold, investigate before the next scheduled export.

### 7.2 Version Retention

Follow the policy defined in `phase-5-export-strategy.md` section 5:
- Keep current + previous month + 30-day safety window
- Reference exports kept permanently
- Auto-deletion runs as part of each export job

### 7.3 Cost Monitoring

Monitor Cloudflare R2 dashboard for:
- Storage (alert at 500 GB — not expected in Phase 5 but alerting is cheap)
- Class A + B operations (alert if monthly cost exceeds $5)

If cost exceeds $10/month: investigate traffic patterns, consider switching heavy-traffic exports to
Backblaze B2 + Cloudflare CDN (Bandwidth Alliance zero-egress configuration).

### 7.4 Kiwix Catalog Maintenance

After catalog submission to openzim/zim-requests:
- Monitor the `openzim/libzim` and `openzim/zim-tools` release notes for breaking changes
- Run `zimcheck` against new libzim versions before deploying updates
- Update `libzim` dependency pin when minor versions are released and verified

### 7.5 Content Growth Scaling

At current Phase 5 MVP scale (500-1,000 items), ZIM generation completes in minutes. At 10,000
items (Phase 5 growth), expect 30-60 minutes for a full export. At 100,000 items, the export job
will need to be optimized:
- Stream items from the DB in batches (avoid loading all into memory)
- Run `zimcheck` on a sampled subset, not the entire file (for CI speed; full check remains in
  production pipeline)
- Consider per-domain parallel export jobs

These are Phase 5.1+ concerns. The `ZimWriter` class stub is designed to accept a stream
interface, making this optimization straightforward when needed.

---

## 8. Files Created in Preliminary Phase

All preliminary phase deliverables are committed to `master` in the open-repo project directory.
They are designed to be self-consistent: the test harness and module stubs will work immediately
after `uv pip install libzim feedgen` even before Phase 4 merges.

| File | Purpose |
|---|---|
| `docs/phase-5-kiwix-integration-guide.md` | Hands-on integration reference for engineers |
| `docs/phase-5-export-strategy.md` | Export variants, scoping rules, retention policy |
| `docs/phase-5-implementation-plan.md` | This document |
| `backend/app/services/export/zim_writer.py` | ZimWriter stub with full interfaces |
| `backend/app/services/export/opds_generator.py` | OPDSGenerator stub |
| `backend/app/services/export/__init__.py` | Package init |
| `infrastructure/cdn-deployment.yaml` | R2 + B2 CDN configuration templates |
| `backend/tests/integration/test_export_pipeline.py` | Integration test harness |

---

## Sources

- [Phase 5 Kiwix Architecture](../phase-5-kiwix-architecture.md)
- [Phase 5 Offline Export Architecture](../phase-5-offline-export-architecture.md)
- [Phase 4 Design](../PHASE_4_DESIGN.md)
- [python-libzim ReadTheDocs](https://python-libzim.readthedocs.io/)
- [feedgen documentation](https://feedgen.kiesow.be/)
- [openZIM Zimfarm](https://github.com/openzim/zimfarm)
- [Cloudflare R2 documentation](https://developers.cloudflare.com/r2/)
- [openzim/zim-requests](https://github.com/openzim/zim-requests)
