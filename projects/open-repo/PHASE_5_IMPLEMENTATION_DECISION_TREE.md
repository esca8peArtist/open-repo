---
title: "Phase 5 Implementation Decision Tree — Candidate Prioritization, Integration Order, Go-Live Checklist"
project: open-repo
phase: 5
status: awaiting-user-decision
date: 2026-05-19
decision_needed_by: "2026-05-22"
---

# Phase 5 Implementation Decision Tree
## Which Candidate First, Integration Order, Success Criteria, Go-Live Checklist

**Decision date**: 2026-05-19  
**Decision needed by**: 2026-05-22 to begin implementation within the May 19–June 5 window  
**Phase 4 baseline**: 255 tests passing, federation stack complete, ZimWriter and OPDSGenerator scaffolds at 100%

---

## Which Candidate Should Be Prioritized First

### Mandatory First: Candidate 1 (ZimWriter)

There is no realistic path where Candidate 2 (OPDS) is implemented before Candidate 1 (ZimWriter). This is not a preference — it is a structural dependency:

`OPDSEntry.from_zim_export()` requires `ZimExport` ORM rows with a `cdn_url` populated. Those rows only exist after ZimWriter has produced valid ZIM output, uploaded it to CDN, and written the result to the `zim_exports` table. Without Candidate 1, the OPDS catalog has nothing to catalog.

The decision tree branches only after Candidate 1 is approved:

```
User decision required:

  ┌─ Q1: Approve Candidate 1 (ZimWriter)? ──────────────────────────────────────────────────┐
  │                                                                                          │
  │  YES (expected)                          NO (unusual)                                    │
  │    │                                       → Phase 5 does not start                      │
  │    ▼                                       → All downstream work is blocked               │
  │  Candidate 1 begins immediately                                                           │
  │  ETA: merged by May 28                                                                   │
  │    │                                                                                     │
  │    ▼                                                                                     │
  ├─ Q2: Add Candidate 2 (OPDS) to Phase 5? ───────────────────────────────────────────────┐│
  │                                                                                         ││
  │  YES — discoverability matters         NO — direct URL download is sufficient          ││
  │    │                                     → Skip OPDS; Phase 5 = ZimWriter only         ││
  │    ▼                                     → Revisit in Phase 6                          ││
  │  Candidate 2 begins in parallel                                                         ││
  │  (separate branch, must not merge                                                       ││
  │  before Candidate 1 lands)                                                              ││
  │  ETA: merged by June 5                                                                  ││
  │    │                                                                                     ││
  │    ▼                                                                                     ││
  └─ Phase 5 complete: offline ZIM + OPDS catalog ◄────────────────────────────────────────┘│
                                                                                             │
  └─────────────────────────────────────────────────────────────────────────────────────────┘
```

### Recommended Execution Path

**Path A (Recommended)**: Candidate 1 immediately, Candidate 2 in parallel on a separate branch, merge Candidate 2 after Candidate 1 lands.

- Candidate 1 feature branch: `feature/zimwriter-libzim-integration`
- Candidate 2 feature branch: `feature/opds-feedgen-migration` (starts when Candidate 1 is ~50% complete)
- Candidate 1 merges first; Candidate 2 rebases and merges second

**Path B**: Candidate 1 only, defer Candidate 2 to Phase 6. Appropriate if the direct CDN download URL is sufficient for Phase 5 users and Kiwix in-app discovery is not a priority right now.

---

## Effort vs. Benefit Tradeoff

| Candidate | Effort | User-facing benefit | Mission alignment |
|-----------|--------|--------------------|--------------------|
| **1: ZimWriter** | 8-11 hours | Offline access for users without reliable internet — field workers, disaster zones, off-grid installations; anyone with a phone and Kiwix can read the full knowledge base | Core mission deliverable. Nothing else matters if users cannot access the content offline. |
| **2: OPDS feedgen** | 8-11 hours (after C1) | Kiwix users discover open-repo from within the app's library browser with one-click install, without needing to know the CDN URL | Discovery polish. Direct URL download already works after Candidate 1 lands. OPDS enables library/institutional partnerships that rely on OPDS catalog standards. |

**Tradeoff summary**: Candidate 1 delivers the core value proposition. Candidate 2 improves how users find and acquire that value. Both are worth doing; the question is whether Phase 5 should deliver both or just the first.

At 8-11 hours each, doing both in the May 19–June 5 window (16-22 hours total available) is feasible with consistent execution. The constraint is the sequencing dependency: Candidate 2 cannot merge first.

---

## Interdependencies

### Can They Be Done in Parallel?

**Development**: Yes, on separate branches. Candidate 2 development can begin once `OPDSEntry.from_zim_export()` is written against a mock `ZimExport` object (no real DB row needed for the factory method itself or for feed generation tests).

**Merge order**: No — Candidate 2 must not merge to main before Candidate 1. The `zim_exports` table does not exist until Candidate 1's Alembic migration runs.

**Practical sequence for maximum speed**:

```
Day 1-2:  Candidate 1 development starts
          Add libzim dependency, add ArticleItem class, replace stub

Day 2-3:  Candidate 1 tests run — 84 existing + 8 new tests pass
          While tests run: Candidate 2 development starts on separate branch
          Write OPDSEntry.from_zim_export() with mock ZimExport

Day 3-4:  Candidate 1 zimcheck integration test, manual Kiwix test
          Candidate 2: write feedgen generate methods, OPDS unit tests

Day 4-5:  Candidate 1 PR created and reviewed
          Candidate 2: integration test with kiwix-serve

Day 5-6:  Candidate 1 merges to main
          Candidate 2: rebase on main, run final tests

Day 6-7:  Candidate 2 merges to main
          Phase 5 complete
```

---

## Phase 6 Implications

### How Each Candidate Shapes Future Architecture

**If Candidate 1 (ZimWriter) is the only Phase 5 deliverable**:
- Phase 6 must include OPDS as its first item (library/institutional users need catalog discovery)
- Phase 6 CDN and distribution work (IPFS, BitTorrent) can proceed without OPDS
- Phase 6 scheduled export automation can proceed without OPDS

**If both Candidate 1 and Candidate 2 complete in Phase 5**:
- Phase 6 can focus on distribution expansion: IPFS integration, CDN retention automation, scheduled export cron
- Phase 6 can focus on content: multi-language ZIM, domain sub-feeds, image-inclusive exports
- Phase 6 can focus on federation: distributed sync, peer-to-peer node sync (Wave 5.2 activation)

**If neither completes** (not a realistic outcome given scaffold state):
- Phase 5 has not delivered. All downstream Phase 6 distribution work is blocked.

**Architecture implications of OPDS for Phase 6**:
- Once OPDS is live, Phase 6 must maintain backward compatibility with the catalog URL structure (`/opds/v2/root.xml`, `/opds/v2/entries`)
- Version history in the OPDS catalog enables Phase 6's retention policy automation: when a ZIM export is deleted, it must also be removed from the OPDS version history entries
- OPDS enables Phase 6 library partnerships (Kiwix Library project, Internet Archive's Open Library) because they require OPDS catalogs for automated content indexing

---

## Recommended Execution Order with Rationale

1. **Candidate 1 (ZimWriter) — Start immediately, merge by May 28**

   Rationale: It is the structural prerequisite for everything downstream. The scaffold is 100% complete. The risk profile is the lowest of any Phase 5 item. The user impact is the highest (offline access for the mission's most underserved users). 84 tests already cover the public interface; the implementation is a fill-in exercise, not a design exercise.

2. **Candidate 2 (OPDS) — Start in parallel on Day 2-3, merge by June 5**

   Rationale: Development can run in parallel to maximize the window. The merge dependency on Candidate 1 introduces a 1-2 day delay between merges, not a 2-week delay. OPDS enables in-app discovery and positions the project for library partnerships in Phase 6. The feedgen risk is well-contained (xml.etree fallback always available).

---

## Shared Go-Live Checklist

This checklist applies to both candidates. A candidate is not go-live ready until all items in its section and all shared items are checked.

### Shared Pre-Deployment Steps

```
[ ] Phase 4 PR #1 is merged to main (255 tests passing, federation stack live)
[ ] zim_exports Alembic migration applied: alembic upgrade head
[ ] Cloudflare R2 bucket created with public read access
[ ] R2 credentials added to environment: R2_ACCOUNT_ID, R2_ACCESS_KEY_ID,
    R2_SECRET_ACCESS_KEY, R2_BUCKET_NAME
[ ] boto3 upload test passes: python -c "import boto3; s3 = boto3.client(...); s3.put_object(...)"
[ ] zimcheck installed on CI and deployment: apt-get install zim-tools
[ ] Kiwix Android (F-Droid) installed on test device
[ ] Kiwix Desktop installed on test machine (Linux or macOS)
```

### Candidate 1 (ZimWriter) Go-Live Gate

```
[ ] uv run pytest tests/ -k "zim" -v — all 84 + 8 new tests pass (92 total)
[ ] zimcheck passes on a real 50-article export:
      zimcheck /tmp/test_export.zim → exit code 0
[ ] ZIM file is non-stub: first 4 bytes are ZIM magic header (not "STUB")
[ ] Xapian index populated: search for known keyword returns >= 1 result
[ ] ZIM opens in Kiwix Android (F-Droid): articles display, no broken layout
[ ] ZIM opens in Kiwix Desktop: full-text search functional
[ ] ZIM opens in kiwix-serve: GET localhost:8080/A/agriculture returns article HTML
[ ] SHA-256 sidecar valid: sha256sum -c *.sha256 passes
[ ] zim_exports DB row created: SELECT * FROM zim_exports WHERE status='available'
[ ] CDN URL is publicly accessible: curl -I https://exports.example.org/zim/...zim → 200
[ ] Export generation time: < 60 seconds for nopic variant on test data
[ ] _stub_write_placeholder() method removed from zim_writer.py
[ ] README updated: Phase 5 status, new test count, offline access instructions
```

### Candidate 2 (OPDS) Go-Live Gate

```
[ ] Candidate 1 gate fully complete (all items above checked)
[ ] zim_exports has at least one row with status='available' and cdn_url set
[ ] OPDSEntry.from_zim_export() tested with real DB row (not mock)
[ ] uv run pytest tests/unit/test_opds_generator.py -v — all 23 tests pass
[ ] GET /opds/v2/root.xml → 200, Content-Type: application/atom+xml
[ ] GET /opds/v2/entries → 200, contains at least one <entry> with acquisition link
[ ] OPDSGenerator.validate_opds_xml(feed_bytes) → empty list (no errors)
[ ] Kiwix Android (F-Droid): Add library URL → shows open-repo archives → Install button works
[ ] Kiwix Desktop: Add library URL → shows open-repo archives → Install button works
[ ] GET /opds/v2/searchdescription.xml → well-formed XML
[ ] OPDS catalog auto-regenerates after new ZimWriter export completes
[ ] Version history visible in Kiwix when ≥2 exports exist for same flavour
[ ] DC elements present: <dc:language> and <dc:issued> in each acquisition entry
```

---

## Rollback Procedures

### Rolling Back Candidate 1 (ZimWriter)

The libzim integration is additive — it replaces stub behavior with real behavior. Rolling back means re-introducing the stub, which is a git revert.

```bash
# Rollback: revert to stub behavior in 30 seconds
git revert <candidate-1-merge-commit-hash>
# This re-introduces _stub_write_placeholder() and removes the Creator calls
# The 84 existing tests will pass again on the stub
# The zim_exports table can remain; rows with status='available' will be stale
# but no data is lost
```

**Fallback (less drastic)**: If only the real export is broken but the stub was working, add `if not _LIBZIM_AVAILABLE: _stub_write_placeholder()` back to `create_zim()`. This leaves libzim installed but falls back to stub behavior for the current run.

### Rolling Back Candidate 2 (OPDS feedgen)

The feedgen migration is a code quality change, not a data change. The xml.etree implementation was never removed — only the active code path changed.

```bash
# Rollback: set _FEEDGEN_AVAILABLE = False at the top of opds_generator.py
# This switches generate_root_catalog() and generate_acquisition_feed() to the
# etree fallback path in one line, without reverting any ORM or schema changes

# OR: full git revert:
git revert <candidate-2-merge-commit-hash>
# OPDSEntry.from_zim_export() is also reverted; catalog will not auto-populate
# but existing GET /opds/v2/entries still serves (from stored XML if cached)
```

---

## Success Criteria

### How to Know Phase 5 Is Working

**Candidate 1 success** (offline access delivered):

| Criterion | Target | How to verify |
|-----------|--------|--------------|
| ZIM export generation | Completes in < 60s for nopic, < 300s for all | `zim_exports.generation_duration_seconds` |
| zimcheck validation | 100% pass rate on automated exports | `zim_exports.zimcheck_passed = TRUE` |
| Offline read on Android | Articles display and search works | Manual test on Kiwix F-Droid |
| Offline read on Desktop | Same | Manual test on Kiwix Desktop |
| File size | nopic < 100 MB at 500 items | `zim_exports.file_size_bytes` |
| CDN availability | ZIM file accessible via HTTPS | `curl -I {cdn_url}` returns 200 |
| Search quality | 10 test keywords each return >= 1 relevant result | Automated integration test |

**Candidate 2 success** (discoverability delivered):

| Criterion | Target | How to verify |
|-----------|--------|--------------|
| Kiwix catalog discovery | OPDS URL shows archives in Kiwix library browser | Manual test on Kiwix Android |
| Feed validity | 0 errors from validate_opds_xml() | Automated after each regeneration |
| Acquisition link works | "Install" in Kiwix starts download of correct ZIM | Manual test |
| Feed response time | < 200ms for catalog endpoint | API response time monitoring |
| DC element presence | dc:language and dc:issued present in each entry | test_opds_dc_language_element_present |

**Phase 5 complete** (both candidates merged, both checklists checked):

- A user in a low-bandwidth region can type the OPDS URL into Kiwix Android, see the open-repo library, tap "Install", download the ZIM over a spotty connection, and read all content offline.
- Alternatively, they can download the ZIM directly from the CDN URL and open it in Kiwix.
- A librarian running kiwix-serve for an institution can add the OPDS URL to their library catalog and serve it to all patrons on their LAN without internet access.

---

## Monitoring Dashboards

### What to Watch After Go-Live

**Metric collection** (add to `GET /api/exports/health`):

```json
{
  "phase_5_status": {
    "zimwriter": {
      "last_successful_export_at": "2026-05-19T02:03:14Z",
      "current_exports": [
        {
          "name": "open-repo_en_nopic",
          "period": "2026-05",
          "status": "available",
          "article_count": 487,
          "file_size_mb": 22.4,
          "zimcheck_passed": true,
          "cdn_url": "https://exports.example.org/zim/open-repo_en_nopic_2026-05.zim"
        }
      ],
      "failed_exports_7d": 0,
      "avg_generation_seconds_7d": 34.2
    },
    "opds": {
      "catalog_url": "https://node.example.org/opds/v2/root.xml",
      "entry_count": 6,
      "last_regenerated_at": "2026-05-19T02:04:22Z",
      "validation_errors": [],
      "feed_size_bytes": 3421
    }
  }
}
```

**Weekly sanity checks** (manual, 10 minutes):
1. Download the latest ZIM from the CDN URL, open in Kiwix, search for a known keyword
2. Open Kiwix Android, add OPDS URL, confirm library shows current month's archives
3. Check `zim_exports` table: no rows stuck in `status='generating'` for > 2 hours
4. Check `zim_exports.zimcheck_passed`: all recent rows should be `TRUE`

**Alert conditions** (add to monitoring):
- Any `zim_exports` row with `status='generating'` for > 90 minutes: export job may be hung
- Any `zim_exports` row with `zimcheck_passed=FALSE`: broken export was uploaded to CDN
- `GET /opds/v2/root.xml` returns non-200: OPDS endpoint is down
- CDN URL returns 404 for a `zim_exports` row with `status='available'`: upload may have failed silently

---

## Appendix: Phase 5 Scope Reminder

**Explicitly in scope for Phase 5 (both candidates)**:
- Export local content items (`is_local=True`) only — no federated content in Phase 5
- Text-only (nopic) variant as primary export; image-inclusive as secondary
- English language only (`language='eng'`)
- Cloudflare R2 as CDN
- Weekly automated exports (APScheduler cron)

**Explicitly out of scope for Phase 5** (documented to prevent scope creep):
- Multi-language ZIM files (Phase 5.1)
- IPFS/CAR file generation (Wave 5.2)
- BitTorrent seeding (Phase 5.1 supplement)
- Federated content inclusion in exports (each node exports only its own items)
- Mobile PWA wrapping kiwix-serve (Phase 5 stretch goal)
- Incremental/differential exports (Phase 5.1)
- Signed manifests (GPG) for artifact verification (Phase 5.1)

---

*Document generated: 2026-05-19*  
*Depends on: `PHASE_5_CANDIDATE_1_ZIMWRITER_IMPLEMENTATION_ROADMAP.md`, `PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md`*
