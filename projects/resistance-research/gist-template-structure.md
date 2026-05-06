---
title: "GitHub Gist — Structure, API, and Publication Reference"
created: 2026-05-06
status: production-ready
purpose: "Authoritative reference for Gist layout, API integration, and multi-file publication. Complements distribution-gist-template.md (which holds header/footer boilerplate) with technical depth."
companion_files:
  - distribution-gist-template.md — section templates and publication record
  - DISTRIBUTION_GIST_URLS.md — live Gist URL registry
  - github-api-integration-guide.md — API call reference
---

# GitHub Gist — Structure, API, and Publication Reference

Six canonical Gists are already live (created Session 678). This document covers the structural
logic behind those Gists, the API mechanics for creating and updating them, and the design
decisions that make Gist markdown render cleanly across desktop and mobile.

---

## 1. Gist Layout Design

### 1.1 Information Hierarchy

Every Gist in this distribution follows a four-zone layout:

```
┌──────────────────────────────────────────────┐
│  ZONE A: Framework Header (metadata block)   │
├──────────────────────────────────────────────┤
│  ZONE B: Document-type context block         │
│          (domain / tracker / summary tag)    │
├──────────────────────────────────────────────┤
│  ZONE C: Document body (verbatim from local) │
├──────────────────────────────────────────────┤
│  ZONE D: Standard footer (cross-links)       │
└──────────────────────────────────────────────┘
```

Zone A is fixed across all Gists. Zone B varies by document type (see
`distribution-gist-template.md`, Section C). Zone C is the substantive content
copied from the local `.md` file without alteration. Zone D is fixed across all Gists.

### 1.2 Section Order Rationale

Zone A first: a reader arriving from a cold link sees the project attribution and license
immediately before reading a word of content. This is critical for institutional contacts
who need to assess credibility and permissibility of use at a glance.

Zone B second: time-sensitive information (advocacy windows, tracker currency dates)
comes before the document body. Readers who stop after three paragraphs still see the
most operationally important metadata.

Zone C third: the full document body. For the proposal (813 KB), this is the dominant zone.
For tracker documents, it is a structured table set.

Zone D last: cross-links and attribution. Readers who finish the document find pathways to
companion documents. This drives navigation within the framework rather than away from it.

### 1.3 Heading Depth Limits

GitHub Gist renders all six Markdown heading levels, but the visual hierarchy collapses
beyond three levels on the Gist web view (h4–h6 render with no size differentiation from h3
on the Gist stylesheet). The source documents already follow this constraint. Do not introduce
h4 or h5 headings in Zone A, B, or D. If the Zone C body uses h4, that is acceptable —
it reflects the source document structure.

### 1.4 Table Rendering

GitHub Gist renders GitHub Flavored Markdown (GFM) tables. The parser is forgiving about
column width inconsistency. Existing source tables in domain files and tracker files render
correctly as-is. Do not reformat tables before Gist publication — the added whitespace creates
diff noise when updating.

One constraint: GitHub Gist does not render HTML `<table>` tags. Any table must use GFM
pipe syntax. The source documents are already GFM-only.

### 1.5 Multi-File Gists

GitHub Gists support multiple files per Gist. The current six Gists are each single-file.
This is the right approach for the primary documents because:

- Single-file Gists have a cleaner URL structure (gist.github.com/user/hash)
- Multi-file Gists do not display a file selector to readers who arrive without JavaScript
- Each document benefits from independent URL tracking (views counted per Gist, not per file)

**Exception for Domain 37 (Path A+37 only):** A multi-file Domain 37 Gist is useful only
if the standalone Domain 37 Gist needs to include the advocacy window table as a separate
file that institutional contacts can download independently. In practice, appending the
advocacy window table to the single file (see `distribution-gist-template.md` Section F)
is simpler and preferred.

If a multi-file Gist becomes necessary (e.g., a domain + its companion litigation tracker
section published together for a specific contact), use this file naming convention:

```
[domain-slug]-main.md        → primary analysis document
[domain-slug]-timeline.md    → advocacy windows / litigation deadlines
[domain-slug]-sources.md     → source bibliography (if separating for academic contacts)
```

---

## 2. GitHub Gist API Integration Requirements

### 2.1 Authentication

**Personal Access Token (PAT)** is the correct authentication method for this distribution.
A GitHub App token is appropriate for multi-user applications; for a single-author
research publication, PAT with minimal scopes is correct and lower-risk.

Required scope: `gist` (read + write access to gists only). No `repo`, `user`, or other
scopes are needed.

Generate at: https://github.com/settings/tokens (classic token) or
https://github.com/settings/tokens?type=beta (fine-grained token).

Fine-grained tokens do not currently support Gist resource selection (as of May 2026).
Use a classic token with `gist` scope only.

**Token storage**: Store as an environment variable, never in a script file.

```bash
export GITHUB_PAT="ghp_your_token_here"
```

Do not commit the token value to any file in this repository.

### 2.2 API Base URL and Rate Limits

Base URL: `https://api.github.com`
Gist endpoint: `https://api.github.com/gists`

**Rate limits (authenticated)**:
- Primary limit: 5,000 requests per hour per authenticated user
- Secondary limits: No more than 100 concurrent requests; no more than 1 second between
  mutating requests (POST/PATCH) to the same resource

For this distribution (creating or updating 7 Gists maximum), rate limits are irrelevant.
The secondary limit of 1 second between mutations means a batch script should include a
1-second sleep between each Gist creation or update call.

**Unauthenticated rate limit**: 60 requests per hour. Always authenticate.

### 2.3 Markdown Rendering

GitHub Gist renders markdown using GitHub's `commonmark-markdown-api`. This is the same
renderer used in GitHub repository README files. GFM extensions supported:

- Tables (pipe syntax)
- Fenced code blocks with syntax highlighting (` ```python `, ` ```bash `, ` ```json `)
- Task lists (`- [ ]` and `- [x]`)
- Strikethrough (`~~text~~`)
- Autolinks (bare URLs in body text become clickable)
- Footnotes (not supported — the source documents use inline citation style, which is correct)

**CSS rendering**: Gist uses GitHub's Primer CSS system. There is no mechanism to inject
custom CSS into a public Gist page. Design choices that work with Primer:

- Bold (`**text**`) renders with weight 600 at body font size
- Horizontal rules (`---`) render as thin separators, useful for zone boundaries
- Blockquotes (`> text`) render with a left-border accent in Primer blue — suitable for
  callout boxes within document bodies
- Badge-style metadata (e.g., ` `STATUS: LIVE` ` in backticks) renders as inline code blocks,
  which creates a distinctive visual treatment for status indicators

**Mobile rendering**: Primer is responsive. Tables render with horizontal scroll on narrow
viewports. Documents with many wide tables (litigation tracker, policy tracker) are readable
on mobile but require horizontal scrolling per table. This is acceptable and standard.

---

## 3. Step-by-Step Gist Creation Checklist

This is the exact procedure for any new Gist. The Domain 37 Gist is the most likely
next creation after path decision; the steps are the same for any document.

### Pre-Creation (5 minutes)

- [ ] Identify source file in local directory (e.g., `domains/domain-37-federal-executive-interference-2026-midterms.md`)
- [ ] Verify file is current: check the `last_updated` field in the file's YAML frontmatter
- [ ] Confirm all internal cross-references in the file resolve to existing files (grep for `[Domain` cross-references)
- [ ] Decide filename for the Gist (see naming convention below)
- [ ] Decide description text (one sentence, include "Democratic Renewal Research Framework" and document type)

**Filename convention**: `[topic-slug]-[year].md`
Examples:
- `domain-37-federal-executive-interference-2026-midterms.md`
- `litigation-tracker-2026.md`
- `democratic-renewal-executive-summary-2026.md`

### Header Preparation (3 minutes)

Copy the standard header block from `distribution-gist-template.md`, Section A.
Fill the bracketed fields:
- `[DOCUMENT TITLE]`: human-readable title matching the document's `# Title` heading
- `Contact`: your preferred contact email, or leave blank for anonymous distribution

For domain files, also copy and fill the domain-context block from Section C of
`distribution-gist-template.md`.

### Gist Creation — Manual (5 minutes)

1. Navigate to https://gist.github.com — confirm logged in as esca8peArtist
2. Click "+" or navigate to https://gist.github.com/new
3. Set the description field (one sentence)
4. Set the filename field (e.g., `domain-37-federal-executive-interference-2026-midterms.md`)
5. In the file content area, paste: Header block → Zone B context block → document body → Footer block
6. Set visibility: **Public** (not Secret)
7. Click "Create public gist"
8. Copy the URL from the browser address bar (format: `https://gist.github.com/esca8peArtist/[hash]`)

### Gist Creation — API (preferred for batch operations)

See `github-api-integration-guide.md` for the full curl and Python examples.
Summary: POST to `https://api.github.com/gists` with JSON body containing
`description`, `public: true`, and `files` object. The URL is in the response `html_url` field.

### Post-Creation (5 minutes)

- [ ] Visit the Gist URL in a browser and confirm rendering is correct
  - Check that the header block renders as a horizontal-rule-delimited block
  - Check that tables render (not raw pipe characters)
  - Check that at least one internal link resolves
- [ ] Record the URL in `DISTRIBUTION_GIST_URLS.md`
- [ ] Record the URL in `PHASE_1_CONTACT_VERIFICATION.json` (relevant field per document type)
- [ ] If this is the Domain 37 Gist: also update the placeholder `[domain 37 link]` in
  `STAGE_PATH_A_DOMAIN37/DEPLOY_CHECKLIST_PATH_A_DOMAIN37.md` and in the Phase 1b
  email templates

---

## 4. Gist Update Procedure

When updating a Gist that is already live (e.g., updating the Litigation Tracker after
new case filings), use the PATCH endpoint rather than creating a new Gist.

**Why PATCH not new Gist**: External links to the existing Gist URL will continue to work.
Any bookmark, email, or citation pointing to the original URL will show the updated content.
Creating a new Gist breaks all existing links.

**When to create a new Gist instead of updating**: Only if the document has structurally
changed in a way that is not backward-compatible (e.g., the proposal is split into a
domain-by-domain series). In that case, update the old Gist to include a redirect notice
pointing to the new URL.

PATCH procedure (manual): Edit the Gist directly at its gist.github.com URL by clicking
the pencil/edit icon. Paste updated content. Click "Update public gist."

PATCH procedure (API): See `github-api-integration-guide.md`, Section 3.

---

## 5. Existing Canonical Gists — Quick Reference

All six Gists are live as of Session 678. Do not recreate them.

| Document | Gist URL | Update cadence |
|----------|----------|----------------|
| Proposal (35 domains) | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | Major framework updates only |
| Executive Summary | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | Major framework updates only |
| Litigation Tracker 2026 | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | Monthly or when 10+ new cases filed |
| First Amendment Tracker | https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c | Monthly or major development |
| Environmental Rollbacks | https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4 | Monthly or major rollback |
| Police Consent Decrees | https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731 | Monthly or major decree action |

**Pending**: Domain 37 standalone Gist — create at start of Path A+37 execution.
Procedure in `distribution-gist-template.md`, Section F.

---

## 6. Domain 37 Gist — Specific Structural Notes

The Domain 37 Gist has one structural element not present in the other six Gists:
the Advocacy Windows table. This table must appear in Zone B (after the document-context
block, before the body) because it is operationally important to election-protection
contacts who may not read the full domain analysis.

The table is reproduced in `distribution-gist-template.md`, Section F. Copy it verbatim.

The Domain 37 body itself (from `domains/domain-37-federal-executive-interference-2026-midterms.md`)
should be copied without editing. Its own internal section structure includes a comparable
advocacy window analysis in the body — the Zone B table is a summary extraction, not a duplicate.
Both are necessary: the Zone B table gives time-pressed readers immediate orientation;
the body analysis gives litigation teams the supporting evidence.

---

*Created May 6, 2026. Complements `distribution-gist-template.md` with API and structural depth.*
*The six canonical Gists it describes were created in Session 678.*
