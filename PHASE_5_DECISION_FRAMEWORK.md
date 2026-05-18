# Phase 5 Decision Framework: Candidate Evaluation & Prioritization Guide

**Status**: Framework Ready (User Decision Required)  
**Date**: 2026-05-18  
**Purpose**: Help user decide between Phase 5 candidates (ZimWriter, OPDS, README) and determine implementation sequence  

---

## Executive Summary: Three Paths Forward

Phase 4 PR #1 (Federation) is merged, backend is stable with 194 tests passing. Phase 5 opens three distinct directions, each valuable but solving different problems:

| Candidate | Delivers | Hours | Blocks | Best For |
|-----------|----------|-------|--------|----------|
| **Candidate 1: ZimWriter** | Offline archive export to Kiwix | 4–6 | Nothing (core path) | Users in low-bandwidth regions |
| **Candidate 2: OPDS** | Discovery mechanism in Kiwix app | 3–4 | Needs Candidate 1 | Discoverability; UX improvement |
| **Candidate 3: README** | Documentation + security fixes | 2–3 | Nothing (independent) | Community onboarding; security |

**Recommended sequence**: 3 → 1 → 2 (low risk to high impact)  
**Alternative (aggressive)**: Start 3 + 1 in parallel once 3 lands  

---

## Candidate Deep-Dive: What You're Choosing Between

### Candidate 1: ZimWriter libzim Integration

**What it does**: Activates the offline export pipeline. Users get valid ZIM archives they can read in Kiwix.

**Technical scope**:
- Replace stub `_stub_write_placeholder()` calls with `libzim.Creator` calls (Python wrapper)
- Wire `add_article()` and `add_image_resource()` to the libzim API
- Enable Xapian full-text indexing (built into ZIM format)
- Uncomment `zimcheck` validation that confirms archive integrity
- Update 6 lines in `pyproject.toml` to add `libzim>=3.2,<4.0`

**Why it matters**:
- **Unlocks Phase 5 core value**: Users can download open-repo offline—critical for low-bandwidth, field, and disaster scenarios
- **All downstream work depends on it**: OPDS catalogs need real ZIM output; CDN upload needs real ZIM; weekly exports need real ZIM
- **No integration debt**: The scaffold is 100% complete. This is purely filling in placeholders
- **Completely independent**: Does not depend on PR #1 review or any other PR; can be developed right now

**Implementation difficulty**: LOW
- Every integration point already has a TODO comment
- 84 export pipeline tests already exist and cover the public interface
- The stubs are comprehensive enough that implementation is a "fill-in" exercise, not a design exercise
- Expected to take 4–6 hours for an experienced Python dev

**Risk profile**: MINIMAL
- No schema migrations
- No breaking API changes
- No cross-service dependencies
- Tests are already written; just need to swap stubs → real code

**User experience after**:
```
User downloads 100 MB open-repo.zim → Opens in Kiwix → 
Full-text searchable offline library of all domains
```

**What users in your target audience gain**:
- Farmers in rural areas → planting guides offline during growing season
- Disaster responders → medical/emergency procedures without internet
- Offline researchers → complete knowledge base on USB stick
- Raspberry Pi installations → self-contained knowledge nodes

---

### Candidate 2: OPDS Catalog feedgen Migration

**What it does**: Enables discovery inside Kiwix apps. Users see open-repo content in the Kiwix app store and can download directly from there.

**Technical scope**:
- Replace raw `xml.etree` XML construction with `feedgen` library for cleaner Atom/RSS handling
- Implement `OPDSEntry.from_zim_export()` factory (currently a TODO)
- Add missing OPDS 1.2 elements: `dc:language`, `dc:issued`, `opensearch`, version history
- Add OPDS search endpoint integration
- Update 19 existing OPDS tests (most should pass unchanged after refactor)

**Why it matters**:
- **Solves discoverability problem**: Right now, users need a direct URL to find open-repo archives. With OPDS, they browse within Kiwix app
- **Standard interop**: OPDS 1.2 is the standard for ebook/content catalogs. Full compliance means Kiwix app will recognize and surface your archives
- **Competitive feature**: Kiwix has many content sources; OPDS catalog ensures yours shows up prominently

**Implementation difficulty**: MEDIUM
- Feedgen library is simpler than raw XML, but requires understanding Atom/OPDS standards
- The factory method `from_zim_export()` needs to understand ZIM export records (only available after Candidate 1)
- 19 tests provide good coverage; most will pass with minor assertion updates

**Dependency**: Requires Candidate 1 to complete first
- OPDS catalog needs to populate from real ZIM export records
- Can be developed in parallel with Candidate 1 if you have extra bandwidth, but should not be merged first

**Risk profile**: MEDIUM
- OPDS standard has some gotchas (namespace handling, element ordering)
- Feedgen library is actively maintained but smaller community than xml.etree
- If OPDS catalog doesn't validate, Kiwix app may silently ignore it (hard to debug)

**User experience after**:
```
User opens Kiwix Android/Desktop → Sees "open-repo" in content directory → 
Clicks "Download" → Gets your archive → Reads offline
```

**What users in your target audience gain**:
- Easier discovery (no URL needed)
- Confidence that archive is legitimate (signed in app store)
- One-click install from within Kiwix
- Updates available through Kiwix's normal content refresh

---

### Candidate 3: README Accuracy Pass & Security Fix

**What it does**: Updates public-facing documentation to match Phase 4 reality and fixes a security issue in the developer quickstart.

**Technical scope**:
- Update README status line: "Phase 2 Complete" → "Phase 4 Complete (Federation)"
- Correct test count: 35 → 194
- Fix `--host 0.0.0.0` to `--host 127.0.0.1` (security rule violation)
- Update project structure diagram to show actual directories
- Document Phase 5 goals and federation endpoints
- Update `API.md` version and endpoint list

**Why it matters**:
- **Security fix**: The `0.0.0.0` binding in the quickstart violates the project's absolute security rules. A developer following the README would expose the API to network attack
- **Community friction**: Anyone reading the repo right now sees Phase 2 documentation for a Phase 4 project. This deters contributors and suggests the project is abandoned
- **Professional presentation**: A public repository's README is the first thing potential contributors see

**Implementation difficulty**: MINIMAL (2–3 hours, mostly editing)
- No code changes
- No test changes
- No dependencies to update
- Can be merged independently

**Dependency**: None
- Can be developed and merged right now, no waiting for other PRs
- Will be just as valuable after Candidates 1 & 2 ship

**Risk profile**: NONE
- Pure documentation, no code risk
- Security fix is a straight substitution
- Can be reviewed and merged in isolation

**User experience after**:
```
Developer finds open-repo on GitHub → Reads Phase 4 status → 
Understands project scope → Runs correct quickstart (127.0.0.1) → 
Starts contributing with correct context
```

**What users in your target audience gain**:
- Contributors: Clear project status and correct setup instructions
- All users: Security fix (no network exposure from default dev config)
- Maintainers: Reduced support friction from confused developers

---

## Implementation Timeline & Dependencies

### Sequential Path (Low Risk, 2 weeks)
```
Week 1:
  Mon–Tue (2–3h): Candidate 3 PR — README/docs update
  → Merge immediately, zero dependencies

  Wed–Thu (4–6h): Candidate 1 branch — ZimWriter libzim integration
  → Develop alongside Candidate 3, merge after 3 lands

Week 2:
  Fri (3–4h): Candidate 2 branch — OPDS feedgen migration
  → Merge last, depends on Candidate 1
```

### Aggressive Path (Medium Risk, 10 days)
```
Day 1: Candidate 3 PR opens → Code review & merge (same day)
Day 1–3: Candidate 1 + Candidate 2 develop in parallel
Day 3–4: Candidate 1 merges (no blockers for 2)
Day 4–5: Candidate 2 merges (has all dependencies)
```

### Conservative Path (Zero Risk, 3 weeks)
```
Finish Candidate 3 → Monitor for issues (1 week) → 
Start Candidate 1 → Monitor (1 week) → 
Start Candidate 2 (no rush, high confidence)
```

---

## Decision Matrix: What to Prioritize

### If you want **Maximum user impact** immediately:
→ **Candidate 1 (ZimWriter) first**
- Enables the core feature (offline access)
- Everything else depends on it
- Unblocks Candidate 2 and future features

### If you want **Fastest morale win** (most complete):
→ **Candidate 3 (README) first**
- Mergeable in 1 day, zero risk
- Fixes a live security issue
- Improves community perception immediately
- Then move to Candidate 1

### If you have **limited time / bandwidth**:
→ **Candidate 3 alone** (2–3 hours, standalone value)
- Security fix is worth doing regardless
- Candidate 1 is next when you have a free week

### If you want **all three** eventually:
→ **Sequential: 3 → 1 → 2** (9–13 hours over 2 weeks)
- Recommended approach
- Low risk, all three deliver independently
- Natural flow: docs → core → polish

---

## Risk Assessment by Candidate

### Candidate 1: ZimWriter (MEDIUM risk → LOW risk)

**Risks**:
- libzim Python wrapper is actively maintained but smaller ecosystem than some alternatives
- Xapian indexing can be tricky if content HTML isn't well-formed
- zimcheck validation sometimes catches edge cases not caught by tests

**Mitigation**:
- Start with a small content set (10 items) to test the full export pipeline
- Run zimcheck locally before shipping
- Have a rollback plan: tests are comprehensive; stubs can be restored in 30 seconds if needed

**Outcome if it fails**:
- You find bugs, fix them, move on. The scaffold is so complete that debugging is straightforward
- Worst case: you skip Candidate 1 and focus on Candidate 2 or 3

---

### Candidate 2: OPDS (MEDIUM risk)

**Risks**:
- OPDS 1.2 spec has namespace subtleties; if not done exactly right, Kiwix ignores your catalog silently
- Feedgen library is smaller community; less Stack Overflow help
- `OPDSEntry.from_zim_export()` requires understanding ZIM export record schema (depends on Candidate 1)

**Mitigation**:
- Test against Kiwix Android emulator and Desktop (both free)
- OPDS spec examples exist; copy the pattern
- If feedgen proves problematic, fallback to raw xml.etree (known to work, just verbose)

**Outcome if it fails**:
- Kiwix app doesn't discover your catalog, but users can still access via direct URL
- Not a blocker; Candidate 1 (ZimWriter) already works independently

---

### Candidate 3: README (ZERO risk)

**Risks**: None. It's documentation.

**Mitigation**: N/A

**Outcome if it fails**: Worst case: typo in README. Fix and re-merge. No code impact.

---

## Community & User Value Comparison

### Value to Low-Bandwidth Communities
1. **ZimWriter** (Candidate 1): ⭐⭐⭐⭐⭐ — Direct access to full offline library
2. **OPDS** (Candidate 2): ⭐⭐ — Indirect (better discoverability, but needs ZimWriter first)
3. **README** (Candidate 3): ⭐ — No direct benefit, but enables contributors

### Value to Contributors
1. **README** (Candidate 3): ⭐⭐⭐⭐⭐ — Clear status, correct setup, professional presentation
2. **ZimWriter** (Candidate 1): ⭐⭐⭐ — Cool feature to work on next
3. **OPDS** (Candidate 2): ⭐⭐ — Interesting but depends on other work

### Value to Project Completeness
1. **ZimWriter** (Candidate 1): ⭐⭐⭐⭐⭐ — Core Phase 5 feature
2. **OPDS** (Candidate 2): ⭐⭐⭐⭐ — Polishes the feature
3. **README** (Candidate 3): ⭐⭐⭐ — Foundation for growth

---

## What Happens If You Choose Each Path

### Path A: All Three (Recommended)
**Timeline**: 2 weeks  
**Effort**: 9–13 hours  
**Outcome**: Phase 5 infrastructure complete. Users have:
- Valid offline archives (ZimWriter)
- In-app discoverability (OPDS)
- Clear contributor onboarding (README)
- Zero tech debt

**Follow-up work**: CDN upload, scheduled exports, IPFS integration (Phase 5 Wave 2)

---

### Path B: ZimWriter Only (Candidate 1)
**Timeline**: 1 week  
**Effort**: 4–6 hours  
**Outcome**: Core Phase 5 feature complete. Users have offline archives.
- Missing: In-app discoverability (OPDS), professional documentation

**Follow-up work**: Candidate 2 + 3 next; then CDN/scheduling

---

### Path C: README + ZimWriter (Smart Default)
**Timeline**: 1.5 weeks  
**Effort**: 6–9 hours  
**Outcome**: Foundation for growth + core feature complete.
- Missing: Polish (OPDS)

**Follow-up work**: Candidate 2 when you have spare bandwidth; then CDN/scheduling

---

### Path D: README Only (Conservative)
**Timeline**: 1 day  
**Effort**: 2–3 hours  
**Outcome**: Security fix + community clarity.
- Missing: Core Phase 5 feature (ZimWriter)

**Best if**: You want one quick win before committing to larger work

---

## Recommendation

**For maximum impact with low risk**: Start with **Path C (Candidate 3 + 1)**

1. **Candidate 3** (README): 2–3 hours, mergeable today, fixes security issue
2. **Candidate 1** (ZimWriter): 4–6 hours, core Phase 5 feature, enables everything else
3. **Candidate 2** (OPDS): 3–4 hours, one month later when you have bandwidth

This sequence:
- Fixes an immediate security issue
- Delivers the core Phase 5 feature
- Gives you a clean, professional public-facing repository
- Leaves OPDS polish for later (still valuable, but not blocking)

**Effort to get a working offline export**: 6–9 hours over 1.5 weeks  
**Barrier to contribution/adoption**: Cleared (good docs, secure quickstart)  
**Path to Phase 5 complete**: Clear (CDN + scheduling are straightforward once ZimWriter works)

---

## Next Steps (User Input Required)

Choose one:

1. **Path A**: "Do all three in order 3 → 1 → 2 over 2 weeks"
2. **Path B**: "Just do Candidate 1 (ZimWriter) for now"
3. **Path C**: "Do Candidate 3 + 1 (my recommended default)"
4. **Path D**: "Just README for now, plan ZimWriter later"
5. **Custom**: "Different priority order / candidates"

Once you decide, I'll create execution checklists for each phase.
