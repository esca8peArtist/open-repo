# Phase 5.1 MVP Activation Checklist

**Document status**: Item 32 pre-staging, May 22 10:30 UTC | Confidence: High | Timeline: June 1–15 post-merge

## Pre-Merge Verification (User Approval Expected June 1–3)

### Code Quality Gates

- [ ] **Test pass rate**: Feature branch shows 51/51 ZIM integration tests passing (100%)
  - Command: `cd projects/open-repo && uv run pytest tests/integration/ -v --tb=short 2>&1 | tail -20`
  - Acceptance: All 51 tests PASS, 0 FAIL, 0 SKIP

- [ ] **Code coverage**: ZimWriter module coverage ≥90%
  - Command: `cd projects/open-repo && uv run pytest tests/integration/ --cov=src/zim_writer --cov-report=term-missing | grep -E "TOTAL|zim_writer"`
  - Acceptance: TOTAL coverage ≥90%; no critical paths <80%

- [ ] **Linting**: No new ruff violations in `src/zim_writer.py` vs master
  - Command: `cd projects/open-repo && uv run ruff check src/zim_writer.py --select=E,F,W --show-source`
  - Acceptance: 0 errors or warnings

- [ ] **Type checking**: mypy clean on zim_writer module
  - Command: `cd projects/open-repo && uv run mypy src/zim_writer.py --strict`
  - Acceptance: 0 errors

### Documentation Completeness

- [ ] **Feature branch README**: Updated with ZimWriter feature description + usage example
  - File: `projects/open-repo/PHASE_5.1_FEATURE_DESCRIPTION.md` exists with:
    - Libzim 3.9.0 integration overview
    - Use case: offline library export
    - Example: `python scripts/export_to_zim.py --domain medical --output medical.zim`

- [ ] **Migration script documented**: `alembic/versions/003_zim_exports_table.py` includes docstring explaining schema
  - Acceptance: Docstring ≥50 words, describes all 28 columns, references ZIM spec

- [ ] **Known limitations documented**: `PHASE_5.1_KNOWN_LIMITATIONS.md` exists with:
  - Libzim version compatibility matrix (tested: 3.9.0; known working: 3.8.0+)
  - Export time baseline (small: <1s, medium: 10–30s, large: >60s)
  - Unsupported features (dynamic content, real-time updates)

---

## Merge Workflow (June 1–5)

### Pre-Merge Rebase (if needed)

- [ ] **Check master for new commits**: `cd projects/open-repo && git log master --oneline --since=2026-05-18 | head -10`
  - If ≥3 new commits on master since feature branch last updated (2026-05-21): rebase required

- [ ] **Rebase feature branch** (if new commits exist):
  ```bash
  cd projects/open-repo
  git checkout feature/zimwriter-libzim-activation
  git rebase master
  # Verify no conflicts; if conflicts: resolve manually, test again
  uv run pytest tests/integration/ -q
  ```
  - Acceptance: Rebase succeeds with 0 conflicts; all tests still pass

- [ ] **Force-push to feature branch** (if rebased):
  ```bash
  git push origin feature/zimwriter-libzim-activation --force-with-lease
  ```
  - Acceptance: Push succeeds; GitHub shows "1 commit ahead of master, 0 commits behind"

### Merge to Master

- [ ] **Verify branch protection rules**: GitHub pull request requires 1 approval (user provides)
  - User action: Review feature branch PR comments + approve merge

- [ ] **Merge via GitHub UI** (squash or regular, per project convention):
  ```bash
  # If squashing: 1 new commit on master
  # If regular merge: feature branch commits + 1 merge commit
  # Either acceptable; verify: git log master --oneline | head -5
  ```
  - Acceptance: Commit(s) appear on master; feature branch is merged

- [ ] **Delete feature branch** after merge:
  ```bash
  git branch -d feature/zimwriter-libzim-activation
  ```
  - Acceptance: Branch deleted locally and on GitHub

---

## Post-Merge Validation (June 5–10)

### Database Migration Testing

- [ ] **Fresh database migration**: Start from empty state; verify migration 003 creates ZIM export table
  ```bash
  cd projects/open-repo
  rm -f sqlite.db  # Start fresh
  uv run alembic upgrade head
  sqlite3 sqlite.db ".schema zim_exports"
  ```
  - Acceptance: Output shows zim_exports table with 28 columns (id, domain, title, description, export_date, zim_filename, byte_size, entry_count, media_count, compression_ratio, index_present, search_enabled, auto_tags, created_at, updated_at, ... [see migration spec])

- [ ] **Backward compatibility**: Master without migration 003 can still run; migration runs cleanly without errors
  - Acceptance: No migration errors in alembic log; no foreign key constraint violations

- [ ] **Data integrity**: Existing domain data is unaffected by migration
  ```bash
  # After migration, query existing domains
  sqlite3 sqlite.db "SELECT COUNT(*) FROM domains;" # Should match pre-migration count
  ```
  - Acceptance: Domain count unchanged

### ZIM Export Output Validation

- [ ] **Export small dataset** (Medical domain, single section, <100 entries):
  ```bash
  cd projects/open-repo
  uv run python scripts/export_to_zim.py --domain medical --output test_small.zim
  ls -lh test_small.zim  # Should be <5 MB
  file test_small.zim  # Should identify as "Zim archive data"
  ```
  - Acceptance: File created, size <5 MB, MIME type is Zim archive

- [ ] **ZIM validity check**: libzim can read the exported file
  ```bash
  cd projects/open-repo
  uv run python -c "from libzim.reader import Archive; a = Archive('test_small.zim'); print(f'Entries: {a.entry_count}')"
  ```
  - Acceptance: Output shows entry count >0; no errors reading archive

- [ ] **Export medium dataset** (Water domain, 3 sections, 500+ entries):
  ```bash
  cd projects/open-repo
  time uv run python scripts/export_to_zim.py --domain water --output test_medium.zim
  ls -lh test_medium.zim  # Should be 15–50 MB
  ```
  - Acceptance: File created in <30 seconds; size 15–50 MB; valid archive

- [ ] **Export performance baseline**:
  - Small (1 section, <100 entries): <1 second expected
  - Medium (3 sections, 500+ entries): 10–30 seconds expected
  - Large (10+ sections, 2000+ entries): 60–120 seconds expected
  - If actual time exceeds expectation by >50%: investigate before production deployment

### Content Validation

- [ ] **Metadata exported correctly**: Title, description, domain, author info present in ZIM metadata
  ```bash
  cd projects/open-repo
  uv run python -c "from libzim.reader import Archive; a = Archive('test_medium.zim'); m = a.metadata; print(f'Title: {m.title}, Description: {m.description}')"
  ```
  - Acceptance: Metadata fields populated (non-empty strings)

- [ ] **Media assets exported**: Images, PDFs, referenced files are included in ZIM
  - Acceptance: `libzim.reader.Archive.entry_count` includes media; spot-check by opening ZIM in Kiwix desktop viewer (verify images display)

- [ ] **Search index functional**: ZIM includes search capability
  ```bash
  cd projects/open-repo
  uv run python -c "from libzim.reader import Archive; a = Archive('test_medium.zim'); print(f'Full-text search: {a.has_fulltext_index}')"
  ```
  - Acceptance: `has_fulltext_index` is True

---

## Deployment Sequence (June 10–15)

### Staging Environment Validation

- [ ] **Deploy to staging server** (test instance separate from production):
  ```bash
  cd projects/open-repo
  git checkout master
  git pull origin master
  # Deploy to staging environment (specific procedure per infrastructure)
  # E.g., Docker: docker build -f Dockerfile.staging -t open-repo:staging . && docker run -d open-repo:staging
  ```
  - Acceptance: Staging deployment succeeds; no startup errors in logs

- [ ] **Smoke test**: API endpoint responds to basic request
  ```bash
  curl http://staging.open-repo.local/api/health
  # Expected: {"status":"ok","version":"5.1"}
  ```
  - Acceptance: HTTP 200 response with ok status

- [ ] **Export via staging API**:
  ```bash
  curl -X POST http://staging.open-repo.local/api/export \
    -H "Content-Type: application/json" \
    -d '{"domain":"medical","format":"zim"}' \
    -o staging_export.zim
  ```
  - Acceptance: HTTP 200; valid ZIM file returned

- [ ] **Load testing** (optional, for production confidence):
  - Parallel exports (3–5 concurrent requests) should succeed without hanging
  - Acceptance: All requests complete in <60 seconds total; no 503 Service Unavailable errors

### Rollback Procedure (Before Production Deployment)

Document and test rollback before going live:

- [ ] **Rollback to master (pre-Phase-5.1 commit)**: 
  ```bash
  # Identify last commit before Phase 5.1 merge (e.g., abc123def)
  git log master --oneline --grep="Merge" | grep zimwriter | head -1
  git revert <merge-commit-hash>  # Creates a new commit that undoes the merge
  git push origin master
  ```
  - Acceptance: Rollback commit appears on master; system reverts to Phase 5.0 state

- [ ] **Data recovery from rollback**: If ZIM exports table was created, ensure it doesn't break Phase 5.0
  - Acceptance: Phase 5.0 code (without ZimWriter) runs without errors even with zim_exports table present (unused)
  - Alternative: Drop zim_exports table if code compatibility required
    ```bash
    alembic downgrade 002  # Undo migration 003
    ```

### Production Deployment (June 15)

- [ ] **Deploy to production**:
  ```bash
  cd projects/open-repo
  git checkout master
  git pull origin master
  # Production deployment procedure (Blue-Green, Canary, etc. per your infrastructure)
  ```
  - Acceptance: Deployment succeeds; no startup errors

- [ ] **Smoke test on production**:
  ```bash
  curl https://api.open-repo.local/api/health
  ```
  - Acceptance: HTTP 200; ok status

- [ ] **Monitor logs for errors**:
  - First 5 minutes: No 500 errors in application logs
  - First 30 minutes: No ERROR level entries related to ZimWriter or zim_exports table
  - Acceptance: Clean logs; alert if any issues appear

- [ ] **First production export**:
  ```bash
  curl -X POST https://api.open-repo.local/api/export \
    -H "Content-Type: application/json" \
    -d '{"domain":"medical","format":"zim"}' \
    -o prod_export.zim
  ```
  - Acceptance: HTTP 200; valid ZIM file returned; export completes in <30 seconds

---

## Phase 5.2 Kickoff Gates (June 15+)

Before starting Phase 5.2 (Medical/Water/Seed/Food/Botanical content implementation), verify:

- [ ] **Phase 5.1 stability**: No production errors for 3+ days post-deployment (June 15–18)
  - Acceptance: Error rate <0.1%; no incident reports

- [ ] **Export performance meets baseline**: Real production workload matches expected timelines
  - Acceptance: Small/medium exports complete in <30s; large exports in <2m

- [ ] **User feedback**: No critical bugs reported by stakeholders (medical domain users, if internal stakeholders exist)
  - Acceptance: 0 P0/P1 bug reports; ≤2 P2 issues (non-blocking)

- [ ] **Phase 5.2 content sourcing confirmed**: Medical domain content files are ready (exists in `projects/open-repo/content/medical/`)
  - Acceptance: ≥10 source files present; validated against ZIM schema

- [ ] **Author/editor capacity confirmed**: Content writing team is assigned and ready June 15–July 15
  - Acceptance: 40+ hours/week availability confirmed for medical domain completion

**If all gates PASS**: Proceed to Phase 5.2 implementation (Medical domain) starting June 16

**If gates FAIL**: 
- P0 bugs: Emergency fix; delay Phase 5.2 by 1 week
- P1 bugs: Fix; delay Phase 5.2 by 3–5 days
- P2 bugs: Log for Phase 5.3; proceed with Phase 5.2 on schedule
- Capacity unavailable: Defer Phase 5.2 to July 1; replan June 15–30 for hotfixes

---

## Resource Estimates

| Task | Hours | Owner | Overlap |
|------|-------|-------|---------|
| Pre-merge verification | 4 | QA/reviewer | None |
| Merge workflow + rebase (if needed) | 2 | Developer | Merge day |
| Post-merge validation (database + export) | 6 | QA | June 5–10 |
| Staging deployment + smoke tests | 3 | DevOps | June 10–12 |
| Production deployment | 2 | DevOps | June 15 |
| Monitoring + first 24h support | 4 | DevOps/on-call | June 15–16 |
| **Total estimated effort** | **21 hours** | Mixed | 15-calendar-day window |

**Timeline**: June 1 (code review) → June 3 (merge) → June 5–10 (testing) → June 12 (staging) → June 15 (production)

---

## Risk Register

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|-----------|
| Libzim version incompatibility on production | Low (3.9.0 is stable) | High (export fails) | Pre-staging validation includes version check; maintain fallback to 3.8.0 in requirements |
| ZIM file corruption on export (incomplete metadata) | Low (libzim handles this) | High (archive unreadable) | Unit tests validate all 28 metadata fields; staging test creates readable archive |
| Export performance slower than baseline (>2x) | Medium (large exports may be slower in prod) | Medium (user experience) | Baseline measured in June 5–10; if >2x slower, investigate disk I/O; possible optimization in Phase 5.2 |
| Database migration breaks existing domains | Low (migration is append-only) | High (downtime) | Test migration on copy of master DB; rollback procedure documented; alembic downgrade tested |
| No user capacity for Phase 5.2 (June 15+) | Medium | Medium (schedule slip) | Gate: Confirm capacity by June 10; if unavailable, defer Phase 5.2 to July 1 |

---

## Success Criteria

✅ Phase 5.1 activation is successful if:
1. All 51 integration tests pass on master (post-merge)
2. Export performance meets baseline (small <1s, medium <30s, large <2m)
3. Production deployment succeeds with 0 P0 errors in first 24h
4. User can export a domain to ZIM format and open in Kiwix viewer
5. Phase 5.2 kickoff gates are all PASS by June 15

🔴 If any gate fails: Document failure; trigger rollback (revert merge) if P0 critical; else fix and retry Phase 5.1 validation within 3 days.
