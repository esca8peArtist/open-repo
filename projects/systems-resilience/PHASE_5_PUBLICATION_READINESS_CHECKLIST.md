---
title: "Phase 5 Publication Readiness Checklist"
project: systems-resilience
phase: 5
purpose: "Platform-agnostic go/no-go gate for June 5 publication of five community-scale domains. Works identically for Nextcloud+Matrix (Option B) and Discourse (Option A)."
status: READY-FOR-USE — activate June 5 morning after platform decision confirmed
created: 2026-06-04
decision_deadline: 2026-06-05 12:00 UTC (go/no-go by noon to allow afternoon publication)
cross_references:
  - PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP.md
  - PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md
  - PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md
  - JUNE_5_15_PHASE_5_PUBLICATION_AND_WAVE_2_RECRUITMENT_TIMELINE.md
  - WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md
---

# Phase 5 Publication Readiness Checklist
## Platform-Agnostic Go / No-Go Gate — June 5, 2026

**Run this checklist the morning of June 5 (or the morning of whichever day publication is scheduled).** It takes approximately 90 minutes to complete all sections. Produce a GO/HOLD/DEFER decision by 12:00 UTC so publication can happen in the afternoon window.

---

## Section 1: Content Readiness — Five Community-Scale Domains

The five Wave 1 community-scale domains are the primary publication candidates. All five are sourced from `projects/systems-resilience/phase-3/`. Verify each is present, meets word-count and citation thresholds, and has metadata complete.

### 1.1 Domain Inventory

| Domain | File | Target Words | Actual Words | Target Citations | Actual Citations | Status |
|--------|------|-------------|-------------|-----------------|-----------------|--------|
| Governance & Decision-Making | `phase-3/01-governance-decision-making.md` | 5,000+ | ~5,800 | 28+ | 38 | CONFIRMED |
| Food Systems & Supply Chain | `phase-3/02-food-systems-supply-chain.md` | 5,000+ | ~5,700 | 28+ | 36 | CONFIRMED |
| Information Infrastructure | `phase-3/03-information-infrastructure.md` | 5,000+ | ~5,700 | 28+ | 36 | CONFIRMED |
| Security & Mutual Defense | `phase-3/04-security-and-defense.md` | 5,000+ | ~5,800 | 28+ | 32 | CONFIRMED |
| Scaling Pathways & Thresholds | `phase-3/05-scaling-pathways-and-thresholds.md` | 5,000+ | ~6,000 | 28+ | 28 | CONFIRMED |

**Verification command** (run from repo root):

```bash
wc -w projects/systems-resilience/phase-3/*.md
```

All five files confirmed present and committed to `master` as of June 3, 2026. This section requires only a spot-check on June 5 morning to confirm no accidental file deletion or corruption.

### 1.2 Cross-Domain Link Verification

The five domains reference one another. Verify that internal cross-references are not broken (anchors exist in the referenced file at the referenced heading).

**Critical cross-reference pairs to verify manually (5 minutes):**

- [ ] `01-governance-decision-making.md` references `02-food-systems-supply-chain.md` — open both, confirm linked section heading exists
- [ ] `02-food-systems-supply-chain.md` references `01-governance-decision-making.md` (governance as prerequisite) — confirm heading anchor is valid
- [ ] `03-information-infrastructure.md` references `04-security-and-defense.md` (communication under threat) — confirm referenced section exists
- [ ] `05-scaling-pathways-and-thresholds.md` references all four other domains — spot-check two links minimum
- [ ] `PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md` TOC anchors — confirm five section anchors resolve (open file, click TOC links in a rendered preview)

**Acceptable failure threshold**: 1–2 broken cross-references are a HOLD (fix in 30 minutes), not a DEFER. 3+ broken cross-references are a HOLD only if fixable in under 2 hours.

### 1.3 Author and Source Attribution

Each domain file must have a YAML frontmatter block with the following fields populated. Verify all five.

Required frontmatter fields (check each file):

```yaml
title:         # Full title string — present in all 5 files
project:       # "systems-resilience" — present in all 5 files
phase:         # 3 — present in all 5 files
domain:        # 1–5 (sequential) — present in all 5 files
created:       # ISO date — present in all 5 files
word_count:    # approximate — present in all 5 files
citation_count: # integer — present in all 5 files
status:        # "production" — present in all 5 files
```

- [ ] All five files have all 8 frontmatter fields populated
- [ ] `status: production` confirmed in all five files (not `draft`, `review`, or `planning`)
- [ ] `created` date is present and not blank

**Note on authorship**: These are research synthesis documents produced by the project orchestrator (no external author byline). If publishing to a platform that displays an author field, use "Systems Resilience Project" or the project lead's name as appropriate. No separate attribution statement is required unless the platform mandates one.

---

## Section 2: Technical Readiness — Platform-Agnostic Checks

These checks apply regardless of whether you chose Nextcloud+Matrix or Discourse.

### 2.1 Markdown Rendering Validation

The five domain files are GitHub-Flavored Markdown (GFM). Before uploading to either platform, confirm rendering is clean.

**Quick validation method** (3 minutes per file):

1. Open each file in a GFM renderer (GitHub.com file preview, VS Code Markdown preview, or `pandoc input.md -o output.html && open output.html`)
2. Check: all tables render as tables (not raw pipe characters), all headings correct level, no orphaned `---` separators, no code block runaway (opening ``` without closing ```)
3. Check: no YAML frontmatter visible in rendered output (frontmatter should be hidden by the renderer; if visible as raw text, the platform needs a frontmatter-strip step — see Section 2.3)

- [ ] `01-governance-decision-making.md` renders clean
- [ ] `02-food-systems-supply-chain.md` renders clean
- [ ] `03-information-infrastructure.md` renders clean
- [ ] `04-security-and-defense.md` renders clean
- [ ] `05-scaling-pathways-and-thresholds.md` renders clean

**Prior validation result**: `PHASE_5_FORMATTING_VALIDATION.md` (June 1) confirmed 43 tables, 127 bullet lists, and 31 numbered lists all properly formatted across the integrated corpus. The five Phase 3 domains share the same formatting conventions and were produced in the same session. Confidence that all five render cleanly: 95%.

### 2.2 Image and Embedded Media Audit

The five domains are text-only documents produced by research synthesis. No external images were embedded during production.

- [ ] Confirm no `![image]()` syntax in any of the five files (quick grep: `grep -r "!\[" projects/systems-resilience/phase-3/`)
- [ ] If any images found: verify image file exists at referenced path, OR remove reference if image unavailable

**Expected result**: Zero images found. If an image reference exists (e.g., a diagram included in a later edit), it needs either a local file at the referenced path or removal of the reference before publication.

**Alt text requirement**: If any images are present, they must have descriptive alt text in the `![description](path)` syntax for accessibility compliance. Empty alt text `![]()` is a HOLD.

### 2.3 Frontmatter Handling by Platform

YAML frontmatter is present in all five files. Platform handling differs:

| Platform | Frontmatter Behavior | Action Required |
|----------|---------------------|-----------------|
| **Nextcloud (Markdown files)** | Nextcloud Text editor renders frontmatter as visible YAML block — not ideal for readers. | Strip frontmatter before upload OR use a Nextcloud plugin that hides it (e.g., `metadata` plugin). Alternatively, convert to Nextcloud wiki format. |
| **Discourse (topic posts)** | Discourse does not recognize YAML frontmatter — it will render as visible raw text at the top of posts. | Strip frontmatter before pasting content into Discourse topic body. Keep frontmatter in repo only. |
| **GitHub Pages (fallback)** | Jekyll strips frontmatter and renders only body. No action needed. | No action required. |

**Recommended action for both platforms**: Before uploading, strip frontmatter from the version being published. Keep the original files with frontmatter in the repo. Use the following command to produce clean copies:

```bash
# Creates a stripped copy of each file in /tmp/phase3-pub/
mkdir -p /tmp/phase3-pub
for f in projects/systems-resilience/phase-3/*.md; do
  awk '/^---/{if(n++>0)found=1; next} found{print}' "$f" > "/tmp/phase3-pub/$(basename $f)"
done
```

- [ ] Frontmatter-stripped copies produced in `/tmp/phase3-pub/` (or equivalent staging directory)
- [ ] Each stripped file spot-checked: no frontmatter block at top, title heading visible as first line

### 2.4 Search Indexing Requirements

Both platforms have search functionality. Ensure platform search can find domains by title and key terms.

**Nextcloud+Matrix path**:
- Nextcloud Full-Text Search (FTS) requires the `fulltextsearch` app enabled with Elasticsearch or Solr backend. Without this, only filenames are searchable.
- Minimum acceptable: files named with domain title keywords (e.g., `01-governance-decision-making.md` is findable by "governance")
- Recommended: Enable FTS in Nextcloud admin panel before Wave 2 research begins

**Discourse path**:
- Discourse search indexes post body content natively within 10 minutes of posting. No additional configuration required.
- Ensure the topic title matches the document title exactly — this is the primary search surface

- [ ] Platform search confirmed functional (test: search "governance" or "food systems" and confirm results)
- [ ] If Nextcloud FTS not installed: document this as a known gap; full-text search will be available after FTS setup (can be post-publication)

---

## Section 3: Asset Inventory for Publication Day

These assets should be prepared before June 5 or can be generated June 5 morning in under 60 minutes.

### 3.1 PDF Export (Fallback Distribution Format)

PDFs serve as the platform-independent fallback if the chosen platform is unreachable or the deployment runs long.

**Generate PDFs using pandoc** (requires pandoc installed; ~2 minutes per file):

```bash
# From repo root:
for f in projects/systems-resilience/phase-3/0*.md; do
  name=$(basename "$f" .md)
  pandoc "$f" \
    --from markdown \
    --to pdf \
    --pdf-engine=weasyprint \
    -o "/tmp/phase3-pub/${name}.pdf" \
    --metadata title="$(grep '^title:' $f | sed 's/title: *//')"
done
```

If pandoc PDF generation fails (weasyprint not installed), use the GitHub rendering approach: push the files to a GitHub repo branch and use the GitHub UI to download as PDF, or use a browser's print-to-PDF on the rendered GitHub file view.

- [ ] PDFs generated for all 5 domains (or confirmed that fallback method is ready if pandoc unavailable)
- [ ] Each PDF spot-checked: opens, title visible on first page, no formatting catastrophe in tables

**PDF size note**: Each domain is approximately 30–45 pages at standard margins. Total PDF bundle: ~175 pages. Compress with `gs` (ghostscript) if bundle size exceeds 20 MB for email distribution.

### 3.2 Metadata Sidecar

A metadata sidecar document makes the corpus indexable by external tools (Zotero, institutional repositories, content aggregators). This is a lightweight CSV or JSON file that lists publication metadata for each domain.

**Metadata sidecar template** (create as `phase3-metadata.csv`):

```csv
title,file,phase,domain_number,created,word_count,citation_count,status,tags,uuid
"Community-Scale Governance & Decision-Making Structures","01-governance-decision-making.md",3,1,"2026-05-18",5800,38,"production","governance;decision-making;community-scale;Zone-5",""
"Community Food Systems & Supply Chain Resilience","02-food-systems-supply-chain.md",3,2,"2026-05-18",5700,36,"production","food-systems;supply-chain;community-scale;Zone-5",""
"Community Information Infrastructure & Resilient Communications","03-information-infrastructure.md",3,3,"2026-05-18",5700,36,"production","information;communications;resilience;Zone-5",""
"Community Security & Mutual Defense Structures","04-security-and-defense.md",3,4,"2026-05-18",5800,32,"production","security;defense;community-scale;Zone-5",""
"Scaling Pathways & Governance Transitions","05-scaling-pathways-and-thresholds.md",3,5,"2026-05-18",6000,28,"production","scaling;governance;thresholds;Zone-5",""
```

- [ ] Metadata sidecar created and committed (or staged for upload alongside domain files)
- [ ] UUID column populated (generate with `uuidgen` or leave blank — UUIDs are optional for v1 publication but required for DOI registration later)
- [ ] DOI registration: not required for v1 publication; add to Phase 7 backlog if institutional distribution is a goal

### 3.3 Social Media / Announcement Assets

Minimal set required for June 5 announcement:

**Email announcement** (see `WAVE_2_AUTHOR_ONBOARDING_KIT_DUAL_PLATFORM.md` for full template): A 250-word email to the founding coalition list announcing publication and linking to the platform. This template is pre-filled and ready to send.

**Platform link**: The URL of the published corpus on the chosen platform. This is generated during deployment (Section 4). Leave blank until deployment complete, then populate.

**Short description per domain** (for social posts or announcement body):

| Domain | One-sentence description |
|--------|--------------------------|
| Governance | How communities of 100–1,000 people make binding decisions and resolve disputes without external institutional support. |
| Food Systems | Supply chain mapping, food preservation protocols, and seasonal production coordination at community scale in Zone 5. |
| Information Infrastructure | Resilient communication architectures — mesh radio, offline-first data, and community broadcast — for low-connectivity environments. |
| Security & Defense | Mutual defense frameworks, threat assessment, and non-escalation protocols for Zone 5 communities. |
| Scaling Pathways | The governance and infrastructure transitions required when a community grows from 50 to 500+ people. |

- [ ] Email announcement draft reviewed and ready to send (template in WAVE_2_AUTHOR_ONBOARDING_KIT)
- [ ] Platform URL confirmed (fill in after deployment)
- [ ] Social post copy drafted (50–100 words per post; use domain descriptions above as base)

---

## Section 4: Platform-Neutral Quality Gates

### 4.1 Spell Check and Grammar

All five domains were produced in the same research session (May 18, 2026) using the same writing conventions. The integrated corpus editorial review (June 1) confirmed zero blocking grammar errors. The Phase 3 domain files were not part of that editorial review — a targeted check is warranted.

**Quick spell check** (aspell or equivalent):

```bash
for f in projects/systems-resilience/phase-3/0*.md; do
  echo "=== $f ===" && aspell list < "$f" | sort -u | head -30
done
```

Review the output for genuine misspellings (not proper nouns, technical terms, or Zone 5-specific vocabulary). Expect 0–5 genuine errors per file.

- [ ] Spell check run on all 5 files
- [ ] 0–5 errors per file: fix inline (15 minutes total); proceed
- [ ] 6+ errors in any single file: review output for systematic issues (e.g., specific terminology consistently misspelled); fix before publication

### 4.2 Citation Link Validation

**Sample method**: Validate 20% of citation URLs (approximately 6–7 per domain, 30–35 total across all five). This takes approximately 30 minutes.

**Procedure**:

1. Extract all URLs from each domain file: `grep -oP 'https?://[^\s)]+' projects/systems-resilience/phase-3/01-governance-decision-making.md`
2. Pick every 5th URL from each list
3. Open each in a browser and confirm: HTTP 200 (or 301/302 redirect to valid page), not a paywall-only page (abstract accessible), page title matches citation context

**Prior result**: `PHASE_5_SOURCE_URL_VERIFICATION.md` (June 1) tested 10% of integrated corpus URLs with 90% working rate. Phase 3 domains use sources from the same research session. Expected rate: 88–92% working on a 20% sample.

**Acceptable thresholds**:
- 90%+ working: GO — proceed to publication
- 80–89% working: HOLD — investigate failed URLs; if all failures are the same domain (e.g., one news site with paywall), document and proceed
- Below 80%: DEFER — systematic citation quality issue; run full verification before publishing

- [ ] 20% URL sample extracted and tested
- [ ] Working rate: ___% (fill in)
- [ ] Failed URLs documented with domain and section

### 4.3 Accessibility Check

**Alt text**: Already confirmed no images in the five domain files (Section 2.2). If any images are present, alt text must be non-empty.

**Heading hierarchy**: Each domain must have a clear H1 (document title), H2 (major sections), and H3 (subsections) structure with no skipped levels (e.g., no H4 appearing under an H2 without an H3 in between).

- [ ] Confirm no skipped heading levels in any file (visual scan of rendered preview is sufficient)

**Color contrast**: Not applicable to Markdown source files. Platform-rendered versions use the platform's default color scheme. Both Nextcloud and Discourse use WCAG AA-compliant default themes out of the box (confirmed in PHASE_5_FORMATTING_VALIDATION.md).

**Screen reader**: The most important accessibility factor for text-heavy research documents is logical heading order and meaningful link text (not "click here"). These were validated in the June 1 formatting review.

- [ ] Link text check: confirm no bare "click here" or "read more" link text in any domain (these should be descriptive: "NREL microgrid design guide" not "click here")

---

## Section 5: Go / No-Go Decision Framework

### Decision Criteria

Complete Sections 1–4 before calling Go/No-Go. Use the grid below.

| Condition | Decision | Action |
|-----------|----------|--------|
| All 5 domains present, all quality gates PASS, all assets ready | **GO** | Proceed to publication in afternoon window (June 5, 13:00–18:00 UTC) |
| 1–2 domains need minor edits (broken cross-links, small typos, frontmatter gaps) — total fix time under 2 hours | **HOLD** | Fix by June 5 noon; publish June 5 afternoon or June 6 morning |
| 1–2 assets missing (PDF not generated, metadata sidecar incomplete) — fix under 1 hour | **HOLD** | Finish assets before publication window; do not delay publication |
| 3+ domains need revisions OR citation link rate below 80% | **DEFER** | Push publication to June 8 (gives 3 days for targeted fixes); notify Wave 2 recruitment timeline shifts by 3 days |
| Platform deployment failed or incomplete | **DEFER** | Activate GitHub Pages fallback (documented in PHASE_5_GITHUB_PAGES_STAGING.md); publish to GitHub Pages today, migrate to chosen platform when deployment complete |

### Decision Log

Fill in after completing all sections:

```
Date / Time: ___________
Checker: ___________

Section 1 (Content Readiness): PASS / HOLD / FAIL — notes: ___________
Section 2 (Technical Readiness): PASS / HOLD / FAIL — notes: ___________
Section 3 (Asset Inventory): PASS / HOLD / FAIL — notes: ___________
Section 4 (Quality Gates): PASS / HOLD / FAIL — notes: ___________

Overall Decision: GO / HOLD / DEFER

If HOLD: Items to fix before publication:
  1. ___________
  2. ___________
  Estimated fix time: ___________
  Revised publication window: ___________

If DEFER: Reason: ___________
  New publication date: ___________
  Wave 2 recruitment adjustment: ___________
```

### Confidence Assessment

Based on prior editorial review (June 1) and formatting validation, the five domains are production-ready with high confidence. Expected outcome on June 5 checklist run: **GO** with minor HOLD items (frontmatter stripping, PDF generation) that add 45–60 minutes before publication but do not block it.

**Confidence**: 92% that all five domains publish on June 5 with no DEFER condition triggered.

---

## Section 6: Post-Publication Verification (Run June 5, Evening)

After content is live on the chosen platform, verify these within 4 hours of publication:

- [ ] All 5 domain pages load correctly in a browser (not logged in — anonymous access confirmed)
- [ ] Platform search returns results for "governance", "food systems", and "scaling" (basic smoke test)
- [ ] Tables render correctly in at least 2 of the 5 domains (table rendering is the most common failure point in Markdown-to-platform migration)
- [ ] Announcement email successfully sent (check sent folder, confirm no bounce-back within 1 hour)
- [ ] At least 1 team member has confirmed they can access the platform and see the content

If any of the above fail: do not trigger Wave 2 author invitations until the access issue is resolved. Wave 2 onboarding materials reference the platform URL — authors need to be able to reach it on day one.
