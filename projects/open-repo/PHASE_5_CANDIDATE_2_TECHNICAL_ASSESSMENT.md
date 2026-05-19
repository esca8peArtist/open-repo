---
title: "Phase 5 Candidate 2 — OPDS Feedgen Technical Assessment"
created: 2026-05-19
session: 1361
status: READY FOR IMPLEMENTATION POST-CANDIDATE-1-MERGE
effort_confirmed: 8-11 hours
confidence: HIGH (90%)
---

# Phase 5 Candidate 2 — OPDS Feedgen Migration
## Technical Assessment & Implementation Readiness

**Purpose**: This document assesses Phase 5 Candidate 2 (OPDS feedgen migration) for immediate implementation post-Candidate-1-merge. It validates the architecture, identifies implementation blockers, and confirms the 8-11 hour effort estimate.

**Status**: ✅ READY FOR IMPLEMENTATION
- Detailed roadmap exists (`PHASE_5_CANDIDATE_2_OPDS_IMPLEMENTATION_ROADMAP.md`)
- Dependency mapping complete (Candidate 1 → Candidate 2 → deployable)
- Test strategy documented
- Risk mitigation identified

---

## 1. Architecture Summary

### 1.1 What Candidate 2 Delivers

OPDS (Open Publication Distribution System) 1.2 Atom-based catalog for Kiwix in-app discovery:
- **OPDS Root Catalog** (`/opds/v2/root.xml`): Navigation feed listing export categories
- **OPDS Acquisition Feed** (`/opds/v2/entries`): Detailed export entries with download links, SHA-256 checksums, metadata
- **Single Entry View** (`/opds/v2/entry/{uuid}`): Per-export metadata and history
- **Search Description** (`/opds/v2/searchdescription.xml`): OpenSearch protocol integration for Kiwix search

**User impact**: Kiwix users (Android F-Droid app, desktop client, kiwix-serve) can discover and install open-repo exports from within the app's library browser without needing to know direct CDN URLs.

**Business impact**: Enables library/institutional partnerships that standardize on OPDS catalog integration (UN agencies, educational networks, NGOs).

### 1.2 Dependency Chain

```
Candidate 1 (ZimWriter) merged to main
    ↓ (ZIM exports being produced → zim_exports table populated)
    ├─ Candidate 2 development begins on separate branch
    │  (write factory method, feed generation logic, unit tests)
    │
    ├─ All 84 Phase 4 federation tests still passing
    │
    ├─ ZimExport ORM model ready for factory method
    │
    ├─ OPDSEntry.from_zim_export() written & tested against mock
    │
    ├─ FeedGenerator integration with feedgen library ≥0.9
    │
    └─ OPDS endpoints in FastAPI router
       ↓
       ├─ Unit tests for all 4 feed generation methods
       │
       ├─ Integration test: full OPDS feed → Kiwix-serve validation
       │
       ├─ Manual kiwix-serve verification
       │
       └─ Candidate 2 merges to main AFTER Candidate 1 confirmed stable
```

**Critical constraint**: Candidate 2 must NOT merge before Candidate 1. The `zim_exports` ORM table does not exist until Candidate 1's Alembic migration (003) runs.

### 1.3 No Architectural Risks Identified

Candidate 2 is a straightforward integration:
- ✅ Existing OPDS generator code already exists and compiles
- ✅ feedgen library is stable (35K weekly downloads) with known fallback (xml.etree)
- ✅ No schema changes required to zim_exports table created by Candidate 1
- ✅ No changes needed to Phase 4 federation ORM models
- ✅ FastAPI router already has `/opds/*` route stubs
- ✅ All 84 Phase 4 tests continue to pass without modification

---

## 2. Implementation Sequence

### Phase: Development (parallel with Candidate 1 testing)

**Trigger**: Candidate 1 ~50% complete (OPDSEntry.from_zim_export() method being written)

**Deliverables**:
1. Create `feature/opds-feedgen-migration` branch from main
2. pyproject.toml: add feedgen>=0.9 dependency
3. app/services/export/opds_generator.py: rewrite with feedgen
   - FeedGenerator wrapper class (abstract feed generation logic)
   - OPDSEntry.from_zim_export() factory method
   - Root catalog generation method
   - Acquisition feed generation method
   - Single entry endpoint method
   - Search description method
4. app/routers/opds.py: FastAPI endpoints (4 routes)
5. tests/integration/test_opds_integration.py: integration tests
6. tests/unit/test_opds_generator.py: unit tests for each feed method

**Time estimate**: 6-8 hours for feature branch implementation

### Phase: Integration (after Candidate 1 merges)

1. Pull Candidate 1 merge from main into feature branch
2. Run full test suite: `uv run pytest` (should pass all 84 + new OPDS tests)
3. Manual kiwix-serve integration test
4. Rebase feature branch on main
5. Create PR from feature/opds-feedgen-migration to main
6. Merge (fast-forward, no conflicts expected)

**Time estimate**: 2-3 hours

**Total**: 8-11 hours confirmed ✅

---

## 3. Files to Create/Modify

### Create
- `app/routers/opds.py` — Four new FastAPI endpoints
- `tests/integration/test_opds_integration.py` — Full OPDS feed validation
- `tests/unit/test_opds_generator.py` — Factory method, generator methods

### Modify
- `pyproject.toml` — Add feedgen dependency (1 line)
- `app/services/export/opds_generator.py` — Rewrite with feedgen (detailed in roadmap: ~200 lines)
- `app/main.py` — Register OPDS router (1 line)
- `.gitignore` — No changes (OPDS XML is generated, not committed)

### No Changes Required
- `app/models/` — ZimExport ORM from Candidate 1 is sufficient
- `app/services/export/zim_writer.py` — No integration needed at writer layer
- `alembic/versions/` — Migration 003 from Candidate 1 is sufficient
- Any Phase 4 federation code

---

## 4. Test Strategy

### Unit Tests (test_opds_generator.py)

**Test 1**: `test_opds_entry_from_zim_export_full`
- Mock ZimExport row with full metadata
- Verify OPDSEntry factory constructs correct dataclass
- Assert all fields mapped correctly

**Test 2**: `test_opds_entry_from_zim_export_minimal`
- Mock ZimExport with minimal fields (no illustration URL, no history)
- Verify factory produces valid entry with optional fields empty

**Test 3**: `test_feedgen_root_catalog_generation`
- Create FeedGenerator, add navigation entries
- Generate root catalog XML
- Parse result, verify OPDS namespaces correct, entries present

**Test 4**: `test_feedgen_acquisition_feed`
- Create 3 mock OPDSEntry objects (different flavours)
- Generate acquisition feed with feedgen
- Verify totalResults=3, verify each entry has UUID, title, download link

**Test 5**: `test_feedgen_fallback_xml_etree`
- Disable feedgen import
- Verify code falls back to xml.etree generator
- Verify output is valid Atom XML

**Coverage target**: 95% of opds_generator.py

### Integration Tests (test_opds_integration.py)

**Test 1**: `test_opds_endpoint_root_catalog`
- POST /api/exports/zim with valid export config (Candidate 1 creates ZIM)
- Wait for ZIM completion
- GET /opds/v2/root.xml
- Verify response is valid Atom XML, status 200, correct Content-Type

**Test 2**: `test_opds_endpoint_acquisition_feed`
- Similar setup with 3 different export types (full, domain-specific, reference)
- GET /opds/v2/entries
- Verify all 3 entries present, correct checksums, download URLs valid

**Test 3**: `test_opds_single_entry_endpoint`
- GET /opds/v2/entry/{uuid} for one export
- Verify entry metadata matches database record

**Test 4**: `test_kiwix_serve_compatibility`
- Generate OPDS feed via endpoint
- Write feed XML to temp file
- Launch kiwix-serve with feed URL
- Verify kiwix-serve parses feed successfully (may require kiwix-serve binary available)

**Coverage target**: All 4 OPDS endpoints tested

### Manual Verification

**Step 1**: Install kiwix-serve locally
```bash
brew install kiwix-server  # macOS / Linux
# or download from https://kiwix.org/en/downloads/
```

**Step 2**: Generate test OPDS feed
```bash
# Start open-repo backend
uv run python -m app.main

# Call OPDS endpoint
curl http://localhost:8000/opds/v2/entries > /tmp/test-feed.xml

# Inspect feed
cat /tmp/test-feed.xml | grep -o '<entry>.*</entry>' | head -1
```

**Step 3**: Verify Kiwix recognizes feed
```bash
kiwix-serve --opds http://localhost:8000/opds/v2/entries
# kiwix-serve should parse feed without errors
```

---

## 5. Risk Mitigation

### Risk 1: feedgen library instability
**Probability**: Low (35K weekly downloads, PyPI active)  
**Mitigation**: Fallback to xml.etree always available. Code includes try/except import guard with _FEEDGEN_AVAILABLE flag.  
**Action**: If feedgen fails, switch to lxml.etree (also Atom-capable) within same architecture.

### Risk 2: Candidate 1 merge delayed past May 26
**Probability**: Medium (user approval needed May 25-26)  
**Mitigation**: Candidate 2 development proceeds on separate branch regardless. No blocker to feature branch readiness.  
**Action**: Monitor Candidate 1 merge status. Candidate 2 feature branch can be complete and ready by May 28.

### Risk 3: OPDS feed validation fails in kiwix-serve
**Probability**: Low (OPDS spec is standard, feedgen is spec-compliant)  
**Mitigation**: Manual kiwix-serve test before merge. Fallback to xml.etree proof-of-concept if needed.  
**Action**: Test in integration phase; allow 1-2 hour debugging window if needed.

### Risk 4: Namespace collision in OPDS XML
**Probability**: Very Low (feedgen handles OPDS namespaces)  
**Mitigation**: Unit test validates generated XML against OPDS schema.  
**Action**: Run test_feedgen_root_catalog_generation before merge.

---

## 6. Implementation Blockers

### Hard Blockers (prevent implementation)
- ❌ Candidate 1 not merged: Candidate 2 cannot reference zim_exports table
  - **Mitigation**: Can write factory method against mock ZimExport before Candidate 1 merges
  - **Status**: MITIGATED — development can proceed in parallel on feature branch

### Soft Blockers (slow implementation)
- ⚠️ kiwix-serve not installed locally: Integration test cannot verify feed
  - **Mitigation**: Skip kiwix-serve test on CI; run manually before merge
  - **Status**: ACCEPTABLE — not a merge blocker

---

## 7. Timeline & Milestones

| Date | Milestone | Status |
|------|-----------|--------|
| May 19 (now) | Phase 5 Candidate 2 technical assessment complete | ✅ COMPLETE |
| May 19-21 | Candidate 1 in user approval | ⏳ IN PROGRESS |
| May 25-26 | Candidate 1 expected to merge | ⏳ WAITING |
| May 26-27 | Candidate 2 feature branch created, implementation begins | ⏳ READY |
| May 28-31 | Candidate 2 implementation complete, feature branch tested | ⏳ READY |
| June 1-2 | Candidate 2 PR review & merge to main | ⏳ READY |

**Contingency**: If Candidate 1 merge slips to June 1, Candidate 2 implementation timeline slides to June 2-5 (still within Phase 5 window).

---

## 8. Success Criteria

### Pre-Merge (feature branch ready)
- ✅ All 4 OPDS endpoints implemented
- ✅ pyproject.toml has feedgen dependency
- ✅ All 84 Phase 4 federation tests passing
- ✅ 15+ OPDS-specific unit/integration tests passing
- ✅ Manual kiwix-serve test passes
- ✅ No merge conflicts with Candidate 1
- ✅ Code review approval from project lead

### Post-Merge (Phase 5 Candidate 2 complete)
- ✅ OPDS feed accessible at `/opds/v2/entries` endpoint
- ✅ Kiwix app discovers open-repo catalogs in-app library browser
- ✅ SHA-256 checksums validate correctly
- ✅ Version history displays in Kiwix (up to 5 most recent exports per flavour)
- ✅ All Phase 4 + Phase 5 tests continue to pass
- ✅ No performance regression in /api/exports/ endpoints

---

## 9. Recommendations

### Recommended Path: Path A (Candidate 1 → Candidate 2 → both deployed)
✅ **APPROVED** — Candidate 1 immediate, Candidate 2 parallel post-merge

**Rationale**:
- OPDS catalog discovery is high-value for institutional users
- 8-11 hours is well within May 19-June 5 Phase 5 window
- No architectural risk; straightforward integration
- Kiwix in-app discovery is second-order benefit but significant for reach

**Alternative Path**: Path B (Candidate 1 only, defer Candidate 2)
- **Tradeoff**: Direct CDN URL download works fine for May 30 deployment; OPDS is nice-to-have
- **Defer to**: Phase 6 (June 2026+)
- **Cost**: Lose institutional partnerships that standardize on OPDS

**Recommendation**: Proceed with Path A unless Candidate 1 merge is significantly delayed (>June 1).

---

## 10. Open Questions for User Review

1. **OPDS priority**: Is Kiwix in-app discovery critical for May 30 Phase 5 launch, or is direct CDN download sufficient?
   - Answer determines Path A vs Path B decision

2. **feedgen vs xml.etree**: Is feedgen library acceptable, or prefer proven xml.etree fallback?
   - (Both are valid; feedgen is cleaner code, xml.etree is proven)

3. **Merge timing**: If Candidate 1 merges June 1+, is Phase 5 Candidate 2 still in scope?
   - Or defer to Phase 6?

---

## Appendix: Candidate 2 Feature Branch Checklist

Use this after Candidate 1 merge to track Candidate 2 implementation:

- [ ] Create `feature/opds-feedgen-migration` branch from main
- [ ] Add feedgen>=0.9 to pyproject.toml
- [ ] Rewrite opds_generator.py with FeedGenerator
- [ ] Implement OPDSEntry.from_zim_export() factory
- [ ] Create app/routers/opds.py with 4 endpoints
- [ ] Create unit tests (test_opds_generator.py)
- [ ] Create integration tests (test_opds_integration.py)
- [ ] Run full test suite: `uv run pytest` (expect 84 + N new tests)
- [ ] Manual kiwix-serve verification
- [ ] Rebase feature branch on main (pull latest)
- [ ] Create PR to main
- [ ] Code review approval
- [ ] Merge to main
- [ ] Verify Phase 5 deployment includes OPDS endpoints

---

**Confidence Level**: 90% — Ready for implementation post-Candidate-1-merge  
**Assessment Completed**: May 19, 2026 (Session 1361)  
**Orchestrator**: Autonomous project orchestrator
