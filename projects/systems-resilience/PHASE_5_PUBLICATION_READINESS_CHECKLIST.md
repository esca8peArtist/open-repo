---
title: "Phase 5 Wave 1+2 Publication Readiness Checklist"
project: systems-resilience
phase: 5
waves: "1 and 2"
purpose: "Platform-agnostic go/no-go gate for June 9 publication of five Wave 1+2 production documents. Works identically for Nextcloud+Matrix (Option A) and Discourse (Option B). Run June 5 morning for verification pass; run again June 8 for final go/no-go confirmation."
status: READY-FOR-USE — run June 5 morning, final run June 8
publication_target: 2026-06-09 13:00 UTC
go_no_go_deadline: 2026-06-08 18:00 UTC
created: 2026-06-04
version: 2.0
replaces: WAVE_1_PUBLICATION_READINESS_CHECKLIST.md (June 1 version)
cross_references:
  - JUNE_5_15_PHASE_5_PUBLICATION_AND_WAVE_2_RECRUITMENT_TIMELINE.md
  - WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md
  - PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP.md
  - PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md
  - PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md
  - WAVE_1_PUBLICATION_READINESS_CHECKLIST.md
---

# Phase 5 Wave 1+2 Publication Readiness Checklist
## Platform-Agnostic Go / No-Go Gate — June 9, 2026

---

## Executive Summary

**Three key points:**
1. Five production-ready documents (45,380 words, zero placeholder markers as of June 1 verification) plus the integrated corpus are cleared for publication. The only remaining pre-publication actions are operational: frontmatter status standardization, frontmatter stripping for platform upload, and PDF export. All are completable in under 2 hours.
2. This checklist runs twice: a verification pass on June 5 morning (90 minutes) and a final go/no-go confirmation on June 8 (30 minutes). June 9 is publication day.
3. Platform-specific publication steps are clearly marked [NEXTCLOUD+MATRIX ONLY] and [DISCOURSE ONLY]. All content validation, asset preparation, and quality gates are identical for both platforms.

**Timeline:** June 5 verification pass → June 6-8 platform deployment and asset prep → June 8 go/no-go → June 9 13:00 UTC publication

**Owner:** Orchestrator (project lead)

**Success criteria:** All five documents live on chosen platform by June 9 18:00 UTC, announcement email sent, post-publication verification complete by June 9 22:00 UTC.

---

## The Five Publication Candidates

This checklist covers the five Wave 1+2 production documents plus the integrated corpus. These are the actual publication assets — not the phase-3 community-scale domain research files (01-05), which are source material retained in the repo.

| # | Document Title | File Path | Word Count | Citations | June 1 Status |
|---|----------------|-----------|-----------|-----------|---------------|
| 1 | Distributed Microgrids as Community Resilience Infrastructure | `phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md` | 8,304 | verified | READY |
| 2 | Community Implementation Playbook — Tier 3 Coordination Framework | `phase-5-wave-2-community-implementation-playbook.md` | 8,619 | verified | READY |
| 3 | Conflict Resolution and Governance Framework | `phase-5-wave-2-conflict-resolution-framework.md` | 8,596 | verified | READY |
| 4 | Psychological Support and Trauma Recovery | `phase-5-wave-2-psychological-support-guide.md` | 9,163 | verified | READY with advisory |
| 5 | Veterinary Care in Crisis Contexts | `phase-5-wave-2-veterinary-care-guide.md` | 10,698 | verified | READY with advisory |
| 6 | Integrated Corpus (all five, unified) | `PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md` | 45,380 | unified | READY |

**Prior verification result (June 1, 2026)**: Zero placeholder markers across all five source documents. Four documents have frontmatter `status` field reading "production-draft" (requires update to "PRODUCTION-READY" before publication — see Section 1.3). The microgrids document reads "COMPLETE" — also requires standardization. All content cleared; only frontmatter formatting outstanding.

---

## SECTION 1: Content Readiness

### 1.1 Document Presence Verification

Run from the repository root on June 5 morning:

```bash
# Verify all five source documents and the integrated corpus are present
ls -la projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md
ls -la projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md
ls -la projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md
ls -la projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md
ls -la projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md
ls -la projects/systems-resilience/PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md
```

```bash
# Verify word counts match expected (within 2% is acceptable — wc -w counts differ slightly from manual counts)
wc -w projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md
wc -w projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md
wc -w projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md
wc -w projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md
wc -w projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md
wc -w projects/systems-resilience/PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md
```

**Expected word count range per document** (from June 1 verification):

| Document | Expected (June 1) | Acceptable Range |
|----------|------------------|------------------|
| Microgrids | 8,304 | 8,100–8,500 |
| Community Implementation Playbook | 8,619 | 8,400–8,800 |
| Conflict Resolution | 8,596 | 8,400–8,800 |
| Psychological Support | 9,163 | 8,900–9,400 |
| Veterinary Care | 10,698 | 10,400–11,000 |
| Integrated Corpus | 45,380 | 44,800–46,000 |

- [ ] All six files confirmed present
- [ ] Word counts within acceptable range for all five source documents
- [ ] Integrated corpus word count within acceptable range
- [ ] If any count is significantly below range: check for accidental file truncation; do not proceed until resolved

### 1.2 Placeholder Marker Scan

The June 1 verification found zero placeholder markers. This is a quick re-confirmation, not a full review.

```bash
# Scan for common placeholder markers in all five source documents
grep -rn "\[fill\]\|\[TODO\]\|\[TBD\]\|\[PLACEHOLDER\]\|\[NEEDS\]\|\[IN PROGRESS\]\|\[CITATION NEEDED\]\|FILL_IN\|INSERT_HERE" \
  projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md \
  projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md \
  projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md \
  projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md \
  projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md
```

**Expected result**: No output (zero matches). Any output is a HOLD — identify each instance and either complete the missing content or remove the marker with a note.

- [ ] Placeholder scan returns zero results
- [ ] If any marker found: document file and line number; resolve before June 8 go/no-go

### 1.3 Frontmatter Status Standardization

All four of these frontmatter updates were identified June 1 and should be completed before the June 5 verification pass. Verify they have been done:

```bash
# Check frontmatter status field in each document
grep "^status:" projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md
grep "^status:" projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md
grep "^status:" projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md
grep "^status:" projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md
grep "^status:" projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md
grep "^status:" projects/systems-resilience/PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md
```

**Required values**: All five source documents should show `status: PRODUCTION-READY`. Integrated corpus should show `status: PRODUCTION-READY` or `status: INTEGRATED` (both acceptable).

If any document still shows `status: production-draft`, `status: COMPLETE`, or `status: draft`, update in place:

```bash
# Example fix for a document still showing production-draft
sed -i 's/^status: production-draft/status: PRODUCTION-READY/' \
  projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md
# Repeat for each affected document; then commit the changes
git add projects/systems-resilience/phase-5*.md projects/systems-resilience/PHASE_5_WAVE_1_2*.md
git commit -m "chore(phase5): standardize frontmatter status to PRODUCTION-READY pre-publication"
```

- [ ] Microgrids: `status: PRODUCTION-READY` confirmed
- [ ] Community Implementation Playbook: `status: PRODUCTION-READY` confirmed
- [ ] Conflict Resolution: `status: PRODUCTION-READY` confirmed
- [ ] Psychological Support: `status: PRODUCTION-READY` confirmed
- [ ] Veterinary Care: `status: PRODUCTION-READY` confirmed
- [ ] Integrated Corpus: `status: PRODUCTION-READY` or `status: INTEGRATED` confirmed

### 1.4 Advisory Checks (Non-Blocking)

Two documents carry advisories from the June 1 review. These are not blockers for June 9 publication but should be tracked.

**Psychological Support and Trauma Recovery**: Contains clinical guidance (Psychological First Aid protocols, suicide warning signs, direct inquiry language drawn from SAMHSA Field Guide). Advisory: external peer review by a disaster mental health practitioner or licensed therapist before publication strengthens harm-reduction posture. If no reviewer has been sourced by June 8, publish on schedule and note in the publication announcement that clinical protocols reference SAMHSA and Red Cross guidelines; local practitioners should adapt to jurisdiction-specific standards.

- [ ] External clinical review of Psychological Support completed (if achievable by June 8) — OR —
- [ ] Publish without external review, include SAMHSA/Red Cross sourcing note in announcement (fallback)

**Veterinary Care in Crisis Contexts**: Contains specific triage protocols and clinical guidance for farm animals. Advisory: veterinary practitioner review (RVT or DVM) before June 9 publication. Same logic applies: publish on schedule if no reviewer available; note in the announcement that protocols reference peer-reviewed veterinary literature and should be adapted to local conditions.

- [ ] External veterinary review of Veterinary Care completed (if achievable by June 8) — OR —
- [ ] Publish without external review, include professional practice advisory in document (fallback)

---

## SECTION 2: Technical Readiness — Platform-Agnostic Checks

### 2.1 Markdown Rendering Validation

Both platforms render GitHub-Flavored Markdown (GFM). Validate rendering quality before upload.

**Quick validation method** (5 minutes per document, 25 minutes total):

Open each file in a GFM renderer. Accepted options: GitHub.com file preview, VS Code Markdown Preview (Ctrl+Shift+V), or `pandoc input.md -o /tmp/test.html && open /tmp/test.html`. Check for:
- Tables render as formatted tables (not raw pipe characters)
- Headings display at the correct level; no orphan `##` without a preceding `#`
- Code blocks have opening and closing triple-backtick fences; no runaway blocks
- Numbered and bulleted lists display correctly; no broken nesting
- No visible YAML frontmatter in the rendered output (frontmatter should be hidden or absent)

- [ ] Microgrids: renders clean
- [ ] Community Implementation Playbook: renders clean
- [ ] Conflict Resolution: renders clean
- [ ] Psychological Support: renders clean
- [ ] Veterinary Care: renders clean
- [ ] Integrated Corpus: renders clean (spot-check Table of Contents anchors and first 3 sections minimum)

**Known formatting complexity**: The integrated corpus at 45,380 words has a large Table of Contents with section anchors. If TOC anchors fail to resolve in a browser-rendered view, the issue is likely heading text mismatches (e.g., special characters in anchor IDs). Fix before upload by manually verifying each TOC entry links to an existing heading.

### 2.2 Image and Embedded Media Audit

All five source documents are text-only research synthesis. No external images should be present.

```bash
# Scan for image references
grep -n "!\[" \
  projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md \
  projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md \
  projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md \
  projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md \
  projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md
```

**Expected result**: No output. If an image reference is found: verify the image file exists at the referenced path. If the image file is not present, remove the image reference from the document (do not publish broken image links). If the image is present: confirm it has descriptive alt text (not empty `![]()`).

- [ ] Image scan returns zero results — OR — all found image references have valid paths and descriptive alt text

### 2.3 Frontmatter Handling by Platform

YAML frontmatter is present in all five documents. Both Nextcloud and Discourse display raw frontmatter as visible text if not stripped — unacceptable for reader-facing publication.

Before uploading to either platform, produce frontmatter-stripped copies of all five documents:

```bash
# Creates stripped copies in /tmp/phase5-pub/
# Preserves originals with frontmatter in the repo
mkdir -p /tmp/phase5-pub

for f in \
  "projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md" \
  "projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md" \
  "projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md" \
  "projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md" \
  "projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md" \
  "projects/systems-resilience/PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md"; do
  # Strip YAML frontmatter block (content between first two --- delimiters)
  awk 'BEGIN{found=0; n=0} /^---/{n++; if(n==2){found=1}; next} found{print}' "$f" \
    > "/tmp/phase5-pub/$(basename $f)"
done
```

After running, spot-check two files in `/tmp/phase5-pub/`: open in a text editor and confirm the first line is a Markdown heading (`# Title`), not a YAML key. If frontmatter is still visible, the awk script may need adjustment (some files use `---\n` as a section separator inside the document — confirm the pattern strips only the leading block).

**Platform-specific note on frontmatter handling**:

[NEXTCLOUD+MATRIX ONLY]: Nextcloud Text editor displays frontmatter as a visible block unless the `metadata` plugin is installed. Use stripped copies for upload. Keep originals in the repo.

[DISCOURSE ONLY]: Discourse renders frontmatter as raw text at the top of the post body. Always use stripped copies for Discourse topic creation.

- [ ] Frontmatter-stripped copies produced in `/tmp/phase5-pub/`
- [ ] Spot-check confirms each stripped file starts with a Markdown heading, not a YAML block

### 2.4 Access Control Pre-Verification

Before uploading content, verify that access permissions on the chosen platform are configured as intended. This step is done June 6-8 during platform deployment, but confirm here before publication day.

**Public read / private write model** (recommended for Phase 5 publication):
- Anonymous visitors can read all published documents
- Only registered authors can post or edit content
- Platform admin can manage user accounts

**Restricted read model** (alternative — appropriate if content is pre-release or for vetted community only):
- Only registered users can read
- Invited authors only

Confirm the model chosen and that the platform is configured correctly. Verifying access control prevents the embarrassing failure mode of publishing content that is only visible to the admin.

[NEXTCLOUD+MATRIX ONLY]: In Nextcloud, go to the `Phase5-Wave1-Published` folder → Share → confirm "Share link" is active with "Allow download" enabled. Test in an anonymous browser tab (incognito or different browser): navigate to the share link and confirm all five documents are visible and downloadable without login.

[DISCOURSE ONLY]: Log out of Discourse. Navigate to the "Phase 5 Wave 1 — Published Research" category. Confirm: topics are visible to anonymous visitors (or appropriate trust level), topic body renders correctly, no login wall appears before topic text is shown.

- [ ] Access control model confirmed and documented (public-read or restricted-read)
- [ ] Anonymous access test passed (or: restricted-read confirmed and invitation list is ready)

### 2.5 Platform Search Functionality

Both platforms have search. Verify search is operational before publication day — a broken search index is not a publication blocker but should be documented.

[NEXTCLOUD+MATRIX ONLY]: Navigate to Nextcloud admin panel → Apps → confirm `fulltextsearch` app status. If disabled: files are still accessible by name; full-text search will not work until FTS is configured. Document this as a known gap. Minimum acceptable: Nextcloud file names include domain keywords (e.g., "conflict-resolution" is findable via filename search even without FTS).

[DISCOURSE ONLY]: Discourse natively indexes post bodies within 10 minutes of posting. Search is functional by default. Test: create a test topic with the word "governance" in the body; search for "governance"; confirm the topic appears. Delete the test topic before publication.

- [ ] Search tested and confirmed functional — OR — search gap documented with workaround noted

---

## SECTION 3: Asset Inventory

### 3.1 PDF Export

PDFs serve as the platform-independent fallback distribution format. Generate before June 9.

```bash
# Requires pandoc and weasyprint (or another PDF backend)
# If weasyprint is not installed: pip install weasyprint OR use wkhtmltopdf as alternative

mkdir -p /tmp/phase5-pub/pdf

for f in /tmp/phase5-pub/*.md; do
  name=$(basename "$f" .md)
  pandoc "$f" \
    --from markdown \
    --to pdf \
    --pdf-engine=weasyprint \
    -o "/tmp/phase5-pub/pdf/${name}.pdf"
  echo "Generated: ${name}.pdf"
done
```

**If pandoc PDF generation is unavailable** (weasyprint or equivalent not installed):
- Push stripped copies to a GitHub repository branch
- Use GitHub UI to render each file
- Use browser print-to-PDF on the GitHub rendered view
- This produces acceptable PDFs at approximately 30–50 pages per document

**PDF quality spot-check** (2 minutes per PDF):
- Opens without error
- Title is visible on page 1
- Tables are not broken across pages catastrophically (some wrapping is acceptable)
- No massive blank sections or truncated content

**Expected PDF sizes**: Each document approximately 35–55 pages at standard margins. Integrated corpus approximately 175 pages. Total PDF bundle estimated at 350–400 pages.

- [ ] PDFs generated for all 5 source documents
- [ ] Integrated corpus PDF generated
- [ ] Spot-check: each PDF opens, title visible, no critical formatting failure
- [ ] If bundle exceeds 20 MB: compress with `gs -sDEVICE=pdfwrite -dNOPAUSE -dQUIET -dBATCH -r150 input.pdf -sOutputFile=output-compressed.pdf`

### 3.2 Metadata Sidecar

A machine-readable metadata file makes the corpus discoverable by external tools (Zotero, institutional repositories, content aggregators). Prepare before publication.

**Create as `/tmp/phase5-pub/phase5-wave1-2-metadata.csv`**:

```csv
title,file,phase,wave,created,word_count,status,domains,advisory
"Distributed Microgrids as Community Resilience Infrastructure","PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md",5,2,"2026-05-18",8304,"PRODUCTION-READY","energy;infrastructure;community-resilience",""
"Community Implementation Playbook — Tier 3 Coordination Framework","phase-5-wave-2-community-implementation-playbook.md",5,2,"2026-05-18",8619,"PRODUCTION-READY","governance;coordination;community-scale",""
"Conflict Resolution and Governance Framework","phase-5-wave-2-conflict-resolution-framework.md",5,2,"2026-05-18",8596,"PRODUCTION-READY","conflict-resolution;governance;facilitation",""
"Psychological Support and Trauma Recovery","phase-5-wave-2-psychological-support-guide.md",5,2,"2026-05-18",9163,"PRODUCTION-READY","psychological-support;trauma;PFA","Clinical protocols reference SAMHSA Field Guide — local adaptation advised"
"Veterinary Care in Crisis Contexts","phase-5-wave-2-veterinary-care-guide.md",5,2,"2026-05-18",10698,"PRODUCTION-READY","veterinary;livestock;crisis-medicine","Triage protocols for farm animals — professional veterinary adaptation advised"
"Integrated Corpus — Phase 5 Wave 1+2","PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md",5,"1+2","2026-06-01",45380,"PRODUCTION-READY","all-domains","Unified publication asset"
```

- [ ] Metadata sidecar created (or confirmed from prior session)
- [ ] CSV opens correctly in a spreadsheet application (no encoding errors)

### 3.3 Announcement Assets

Minimal set required for June 9 publication announcement:

**Item 1 — Founding coalition announcement email**: Template is in `WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md`, Part 1, coalition announcement template. Fill in the platform URL (generated during June 6-8 deployment) before sending.

**Item 2 — Platform URL**: Generated when the chosen platform is deployed (June 6-8). This must be confirmed before June 9 morning. Leave a placeholder here and fill in before the go/no-go call:

```
Platform URL (fill in after June 6-8 deployment):
  Nextcloud: https://100.70.184.84/nextcloud/s/[share-link-id]
  Discourse: https://[discourse-domain]/c/phase-5-published/
```

**Item 3 — One-sentence descriptions for social posts / announcement body**:

| Document | One-sentence description |
|----------|--------------------------|
| Microgrids | How communities of 100–1,000 people can deploy and govern distributed energy infrastructure that continues functioning when the grid fails. |
| Community Implementation Playbook | A step-by-step coordination framework for building Tier 3 community resilience structures, from initial assessment to full operational capacity. |
| Conflict Resolution | Decision-making, mediation, and dispute resolution protocols for communities managing shared resources under stress. |
| Psychological Support | Community-level Psychological First Aid frameworks and trauma recovery protocols for sustained crisis contexts. |
| Veterinary Care | Triage protocols, preventive care frameworks, and community-scale livestock and small-animal care for contexts without veterinary access. |

- [ ] Announcement email drafted and ready to send (platform URL is the only remaining blank)
- [ ] One-sentence descriptions confirmed usable for announcement
- [ ] All announcement assets saved to a staging location accessible on June 9 morning

---

## SECTION 4: Content Quality Gates

### 4.1 Spell Check

The June 1 editorial review confirmed zero blocking grammar or spelling errors. This is a light re-check pass to catch anything introduced in subsequent edits.

```bash
# Run aspell against each source document (pipe through tr to handle markdown)
for f in \
  "projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md" \
  "projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md" \
  "projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md" \
  "projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md" \
  "projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md"; do
  echo "=== $(basename $f) ==="
  aspell list --mode=markdown < "$f" | sort -u | head -40
done
```

Review the output for genuine misspellings (not proper nouns, technical terms, or Zone 5-specific vocabulary). Expect 0–8 genuine errors per document. Common false positives: "LoRa", "WeasyPrint", "Mjolnir", "PFA", "RVT", "DVM", "SAMHSA", "Meshtastic".

- [ ] Spell check run on all 5 source documents
- [ ] 0–8 genuine errors per document: fix inline (15 minutes total); proceed
- [ ] 9+ genuine errors in any single file: review output carefully; fix systematic issues before publication

### 4.2 Citation URL Validation

A 20% sample of citation URLs validated on June 5. This takes approximately 30–40 minutes.

**Method**:
```bash
# Extract all URLs from each document
for f in \
  "projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md" \
  "projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md" \
  "projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md" \
  "projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md" \
  "projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md"; do
  echo "=== $(basename $f) ==="
  grep -oP 'https?://[^\s)"]+' "$f" | sort -u
done
```

From each document's URL list, test every 5th URL (20% sample): open in a browser, confirm HTTP 200 or valid redirect, page title matches citation context, content is not paywalled.

**Prior context**: `PHASE_5_SOURCE_URL_VERIFICATION.md` (June 1) tested 10% of integrated corpus URLs with 90% working rate. The five Wave 1+2 source documents use the same citation pool. Expected rate on 20% sample: 87–93% working.

**Thresholds**:

| Working Rate | Decision |
|-------------|----------|
| 90%+ | GO — proceed without action |
| 80–89% | HOLD — investigate failed URLs; if all failures share a single domain (e.g., one news site with paywall changes), document and proceed |
| Below 80% | DEFER — systematic citation quality issue; run full verification before publishing |

- [ ] 20% URL sample tested per document
- [ ] Working rate documented per document: Microgrids ___%, Playbook ___%, Conflict ___%, Psych Support ___%, Vet Care ____%
- [ ] Any failed URLs documented with document name and section

### 4.3 Heading Hierarchy and Accessibility

All five documents follow a consistent GFM heading structure. Verify no heading level is skipped (e.g., no H4 under an H2 without an intervening H3).

```bash
# Extract heading structure from each document
for f in \
  "projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md" \
  "projects/systems-resilience/phase-5-wave-2-community-implementation-playbook.md" \
  "projects/systems-resilience/phase-5-wave-2-conflict-resolution-framework.md" \
  "projects/systems-resilience/phase-5-wave-2-psychological-support-guide.md" \
  "projects/systems-resilience/phase-5-wave-2-veterinary-care-guide.md"; do
  echo "=== $(basename $f) heading structure ==="
  grep -n "^#" "$f" | head -30
done
```

Visual scan: confirm H1 exists (document title), H2 sections follow, H3 subsections under H2s, no H4 without H3 parent.

Also check for link text quality (no bare "click here"):
```bash
grep -n "click here\|read more\|learn more\|here\](" \
  projects/systems-resilience/phase-5-wave-2-*.md \
  projects/systems-resilience/phase-5/wave-2/PHASE_5_WAVE_2_MICROGRIDS_RESEARCH_OUTLINE.md
```

- [ ] Heading hierarchy confirmed clean in all 5 documents (no skipped levels)
- [ ] No "click here" or empty link text found — OR — any found instances updated to descriptive text

---

## SECTION 5: Go / No-Go Decision Framework

### Decision Grid (Complete by June 8 18:00 UTC)

Work through Sections 1–4 before calling the Go/No-Go. Then apply the grid:

| Condition | Decision | Action |
|-----------|----------|--------|
| All sections PASS, all assets ready, platform deployed and accessible | **GO** | Proceed to June 9 publication (13:00–18:00 UTC) |
| 1–2 minor items outstanding (frontmatter not yet standardized, one broken cross-link, PDFs not generated) — total fix time under 2 hours | **HOLD** | Fix by June 9 09:00 UTC; publish June 9 afternoon window unchanged |
| Platform deployment incomplete as of June 8 EOD | **HOLD** | Activate GitHub Pages fallback immediately (`PHASE_5_GITHUB_PAGES_STAGING.md`); publish to GitHub Pages June 9; migrate to chosen platform when deployment completes (can be June 10–12 without disrupting Wave 2) |
| 3+ documents need content revision OR citation link rate below 80% in any document | **DEFER** | Push publication to June 12 (3-day slip); Wave 2 sprint kickoff delayed to June 13 (one week slip tolerable per contingency C in timeline) |
| Integrated corpus TOC anchors broken and cannot be fixed in under 1 hour | **HOLD** | Publish individual documents first; publish integrated corpus when TOC is repaired (up to June 11 acceptable) |

### Decision Log (Fill in June 8)

```
Date / Time: ___________
Checker: ___________

Section 1 (Content Readiness):       PASS / HOLD / FAIL — notes: ___________
Section 2 (Technical Readiness):     PASS / HOLD / FAIL — notes: ___________
Section 3 (Asset Inventory):         PASS / HOLD / FAIL — notes: ___________
Section 4 (Quality Gates):           PASS / HOLD / FAIL — notes: ___________

Platform deployment status:          DEPLOYED / PARTIAL / NOT STARTED

Overall Decision: GO / HOLD / DEFER

If HOLD: Items to fix before publication:
  1. ___________
  2. ___________
  Estimated fix time: ___________
  Revised publication window: June 9 ___:___ UTC (or June 12 if slip required)

If DEFER: Reason: ___________
  New publication date: ___________
  Wave 2 recruitment adjustment (from timeline contingency C): ___________
```

### Confidence Assessment

Based on the June 1 verification (zero placeholder markers, all five documents cleared), the primary publication risks are operational: frontmatter standardization, platform deployment, and asset generation. All three are within normal operational execution range.

**Confidence**: 92% that all five documents publish June 9 with no DEFER condition triggered. 99% confidence that at least three documents publish June 9 (with any delay applying only to the integrated corpus or advisory-flagged documents).

---

## SECTION 6: Publication Day Procedures (June 9)

### Morning Block — Final Checks (09:00–11:00 UTC, 2 hours)

1. Re-run document presence verification (5 minutes — confirm no accidental file deletions)
2. Confirm frontmatter-stripped copies in `/tmp/phase5-pub/` are present and current (5 minutes)
3. Confirm PDFs generated and accessible (5 minutes — check file sizes are reasonable)
4. Confirm platform is accessible and deployment is complete (10 minutes — log in, navigate to publication location)
5. Confirm announcement assets are staged and platform URL is filled in (5 minutes)
6. Confirm Git repository is clean (no uncommitted changes to corpus files): `git status projects/systems-resilience/phase-5*.md` (2 minutes)

**Total morning check**: approximately 30 minutes. If anything fails, you have 2 hours to fix before the publication window opens.

### Publication Window (13:00–17:00 UTC, 4 hours)

**[NEXTCLOUD+MATRIX ONLY] — Publication steps in order:**

1. Navigate to Nextcloud as admin → `Phase5-Wave1-Published` folder
2. Upload all five frontmatter-stripped markdown files from `/tmp/phase5-pub/` (drag and drop or WebDAV)
3. Upload the integrated corpus (`PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md`) in stripped form
4. Set folder sharing: "Share with link" → read-only → enable "Download" → copy the share URL
5. Optional: create a `README.md` in the published folder with document list and one-sentence descriptions
6. Pin the folder share link in Matrix room `#phase5-discussion:resilience-hub` with the message: "Phase 5 Wave 1+2 published. Five research documents + integrated corpus available at [LINK]. Five topics: microgrids, community implementation, conflict resolution, psychological support, veterinary care."
7. Send the founding coalition announcement email (template from WAVE_2_AUTHOR_ONBOARDING_KIT) with the now-filled platform URL
8. Note publication timestamp

**[DISCOURSE ONLY] — Publication steps in order:**

1. Log in to Discourse as admin → navigate to "Phase 5 Wave 1 — Published Research" category
2. Create topics in reverse order (so governance appears first in category view):
   - Create "Veterinary Care in Crisis Contexts" — paste stripped content → Submit
   - Create "Psychological Support and Trauma Recovery" — paste stripped content → Submit
   - Create "Conflict Resolution and Governance Framework" — paste stripped content → Submit
   - Create "Community Implementation Playbook — Tier 3 Coordination Framework" — paste stripped content → Submit
   - Create "Distributed Microgrids as Community Resilience Infrastructure" — paste stripped content → Submit
3. Create announcement topic: "Phase 5 Wave 1+2 Published — Five Community-Scale Resilience Documents" — brief description + links to all five topics → Pin as category announcement
4. Log out of Discourse. In an anonymous browser tab, navigate to the category and confirm all five topics are visible and readable
5. Send the founding coalition announcement email with Discourse category URL
6. Note publication timestamp

### Monitoring Checkpoints (17:00–22:00 UTC)

Run these post-publication checks within 4–5 hours of going live:

**T+1 hour (approximately 14:00 or 17:00 UTC depending on publication start):**
- [ ] All 5 documents accessible in anonymous browser session (not just admin-view)
- [ ] Platform search returns results for "governance", "microgrids", and "veterinary"
- [ ] No error messages on any document page (rendering failures, 404s on images)
- [ ] Announcement email confirmed sent (check outbox, no bounce-back)

**T+4 hours (approximately 21:00 UTC):**
- [ ] Check for any access control failures (user reports unable to access, or unexpected anonymous access to restricted content)
- [ ] Confirm at least one other person (from the founding coalition list or a Wave 2 author candidate) has accessed the content (check access logs or first replies/acknowledgments)
- [ ] Log publication completion with timestamp in WORKLOG.md

**Critical hold condition**: If anonymous access test fails (content is not visible to non-logged-in users when it should be), do not send the announcement email until access is restored. Send to Wave 2 author candidates first (they will have accounts regardless).

### 24-Hour Post-Launch Review (June 10 09:00–11:00 UTC)

Run this review June 10 morning, approximately 24 hours after publication:

- [ ] Access audit: all five documents still accessible; no accidental permission change overnight
- [ ] Content integrity: spot-check one table and one numbered list in two documents; confirm they still render correctly
- [ ] Announcement delivery: count how many announcement emails bounced (check bounce log in email provider); note delivery rate
- [ ] Engagement baseline: note initial views, downloads, or replies per document (this is the T+1 day baseline for the June 15 engagement assessment)
- [ ] Wave 2 status: confirm Wave 2 author invitations sent June 5-6 are receiving responses (see timeline document for June 10 sprint kickoff)
- [ ] Any issues logged: document any unexpected behavior observed in the first 24 hours in a short note appended to this checklist

**Decision from 24-hour review**:
- If platform functioning normally and content accessible: mark publication complete, proceed with Wave 2 sprint as scheduled
- If access issue discovered: fix immediately; if fix requires more than 2 hours, send temporary GitHub Pages link to Wave 2 authors so their sprint is not blocked
- If critical content error discovered (factual error in clinical guidance, broken table structure throughout a document): issue an erratum note in the platform (Nextcloud: a `ERRATUM.md` file in the folder; Discourse: a reply to the affected topic) and schedule a patch publication within 48 hours

---

## Summary: Total Time Budget for This Checklist

| Activity | When | Estimated Time |
|----------|------|----------------|
| June 5 morning verification pass (Sections 1–4) | June 5, 06:00–10:00 UTC | 90 minutes |
| Frontmatter standardization (if not already done) | June 5 | 10 minutes |
| Asset generation (frontmatter stripping, PDFs, metadata sidecar) | June 5–7 | 60–90 minutes |
| June 8 go/no-go confirmation (re-run critical checks) | June 8, 16:00–18:00 UTC | 30 minutes |
| Publication day morning pre-check | June 9, 09:00–11:00 UTC | 30 minutes |
| Publication window (upload + announcement) | June 9, 13:00–17:00 UTC | 4 hours |
| Post-publication monitoring checkpoints | June 9, 17:00–22:00 UTC | 60 minutes |
| 24-hour post-launch review | June 10, 09:00–11:00 UTC | 60 minutes |
| **Total orchestrator hours for publication** | | **~9–10 hours across June 5–10** |

---

*Version 2.0 — supersedes WAVE_1_PUBLICATION_READINESS_CHECKLIST.md (June 1 version)*
*Created June 4, 2026 | Publication target June 9, 2026 13:00 UTC*
