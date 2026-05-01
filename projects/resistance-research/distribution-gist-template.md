---
title: "Distribution Gist — Boilerplate Shell Template"
created: 2026-05-01
session: 716
status: template
purpose: "Boilerplate shell for creating any new public GitHub Gist from the resistance-research project. Path-agnostic. Swap in document-specific content after applying this structure."
applies_to: "Any new Gist publication — primary documents, domain files, tracker updates, supplemental materials"
---

# Distribution Gist — Boilerplate Shell Template

This template provides the standard structural sections for any public GitHub Gist published from this research project. The six existing canonical Gists (created Session 678) already follow this structure. Use this template when creating:

- The standalone Domain 37 Gist (required for Path A+37)
- Any domain-specific supplemental Gists requested by institutional contacts
- Future tracker update Gists (litigation tracker, first amendment tracker, etc.)
- Any public-facing document from the research corpus

---

## How to Use This Template

1. Open https://gist.github.com — log in as esca8peArtist
2. Create a new Gist (click the "+" icon in the top right or go to gist.github.com/new)
3. Set visibility to **Public** (not Secret)
4. Set the filename to: `[document-slug].md` (e.g., `domain-37-federal-executive-interference.md`)
5. Copy the document content from the local file
6. Add the header block (Section A below) at the top
7. Add the footer block (Section B below) at the bottom
8. Click "Create public gist"
9. Copy the resulting URL and record it in `DISTRIBUTION_GIST_URLS.md`

---

## Section A: Standard Gist Header

Paste this block at the very top of every public Gist, above the document title. Fill the bracketed fields.

```
---
Research project: Democratic Renewal Framework (35-domain analysis, CC 4.0)
Document: [DOCUMENT TITLE]
Framework version: May 2026
License: Creative Commons Attribution 4.0 International (CC BY 4.0) — cite freely, adapt freely
Full framework: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261
Executive summary: https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4
Contact: [{{YOUR_CONTACT_INFO}} — fill before publishing]
---
```

**Field guidance**:
- `[DOCUMENT TITLE]`: The document's human-readable title (e.g., "Domain 37 — Federal Executive Interference in the 2026 Midterms")
- `Contact`: Use your preferred outreach email or leave blank for anonymous distribution. For institutional outreach Gists (where you've already contacted someone), include your email. For public distribution Gists, leaving contact blank is acceptable.

---

## Section B: Standard Gist Footer

Paste this block at the very bottom of every public Gist, after all document content.

```
---

## About This Document

**Part of**: The 35-domain Democratic Renewal Research Framework  
**Full framework**: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261  
**Executive summary**: https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4  
**Litigation tracker**: https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0  
**License**: Creative Commons Attribution 4.0 International. Cite, adapt, and distribute freely with attribution.

**Other documents in this series**:
- First Amendment Suppression Tracker: https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c
- Environmental Rollbacks Tracker: https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4
- Police Consent Decree Tracker: https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731

**Research standard**: All claims are sourced to primary materials — court filings, congressional records, peer-reviewed research, official government documents, and primary journalism from named reporters at identified outlets. No anonymous sources used as primary evidence.

**Currency**: [INSERT CURRENCY NOTE — e.g., "Current through April 29, 2026. Domain-specific update log maintained in source repository."]

**How to stay current**: This document is updated in research sessions tracking active developments. If you received this document via direct outreach and would like to be notified of significant updates, reply to the email you received it through.
```

---

## Section C: Domain-Specific Gist Additions

### For Domain File Gists

When creating a Gist for a specific domain file (e.g., Domain 37), add this block immediately after the Section A header and before the document title:

```
---
**Domain**: [DOMAIN NUMBER] — [DOMAIN TITLE]
**Parent framework section**: [e.g., "Part III — Political Process and Democratic Infrastructure"]
**Framework domains total**: 35
**Advocacy windows**: [list the one to three most time-sensitive action dates from this domain]
**Cross-reference domains**: [list 2-4 related domain numbers and titles]
---
```

For the Domain 37 Gist specifically, use this pre-filled version:

```
---
**Domain**: 37 — Federal Executive Interference in the 2026 Midterms
**Parent framework section**: Part IV — Electoral Security and Democratic Process
**Framework domains total**: 35
**Advocacy windows**:
  - May 30, 2026: DOJ consent decree finalization — first legal challenge window
  - August 7, 2026: NVRA 90-day quiet period begins — systematic voter purge injunction deadline
  - September 2026: Pre-election litigation positioning (Section 3 disqualification prep)
**Cross-reference domains**: Domain 1 (Voting Rights and Elections), Domain 6 (Judicial Independence), Domain 29 (Prosecutorial Weaponization), Domain 33 (State Legislative Autocratization)
---
```

### For Tracker File Gists

When creating or updating a Gist for a tracker file (litigation tracker, first amendment tracker, etc.), add this block after the Section A header:

```
---
**Tracker**: [TRACKER NAME]
**Last updated**: [DATE]
**Update cadence**: [e.g., "Monthly; major developments added within 48 hours"]
**New entries this update**: [COUNT and brief description of most recent entries]
**Companion framework domain(s)**: [Domain numbers most directly related to this tracker]
---
```

### For Executive Summary or Proposal Updates

When the main proposal or executive summary is updated and a new Gist version is published, add:

```
---
**Version note**: Updated [DATE]. Changes from prior version: [brief description — e.g., "Domain 1 Section 4.2 FISA correction; Domain 37 Hungary comparative evidence added"]
**Prior version**: [prior Gist URL if preserved]
---
```

---

## Section D: Gist Formatting Standards

These formatting standards apply to all Gist publications. They ensure the document renders correctly in GitHub's Markdown viewer, which is the default display for anyone clicking a Gist link.

**Headings**: Use `#` for document title, `##` for major sections, `###` for subsections. Do not use more than three heading levels in Gist-facing documents — GitHub's Markdown renderer handles four levels but the visual hierarchy becomes confusing.

**Tables**: GitHub Gist renders standard Markdown tables correctly. Maintain the existing table structure from source documents. Column widths are auto-adjusted by the renderer — do not add padding.

**Links**: All URLs should be fully spelled out, not wrapped in Markdown link syntax, in the header and footer blocks. This makes them copy-paste accessible. Within document body text, Markdown link syntax `[text](URL)` is acceptable.

**Code blocks**: Use triple backtick fencing for any code, JSON, or structured data. Specify language where relevant (e.g., ` ```json ` or ` ```python `).

**Footnote handling**: The source domain files use inline citations in the form `([Source Name](URL), [Date])`. This format renders correctly in Gist. Do not convert to numbered footnotes — it creates broken reference chains when documents are excerpted.

**Line breaks**: GitHub Gist renders Markdown line breaks correctly. Paragraph breaks (two carriage returns) create visible spacing. Single carriage returns within a paragraph are treated as spaces.

**File size guidance**: GitHub Gist has no documented maximum file size for Markdown files, but files over 500KB begin to load slowly on mobile. The main proposal (35 domains, full evidence) is approximately 537KB and loads acceptably. Individual domain files (200-700KB) load quickly. If a tracker file grows above 1MB, consider splitting into annual or quarterly files.

---

## Section E: Gist Publication Record

Record all new Gists here as they are created. This section supplements `DISTRIBUTION_GIST_URLS.md`.

### Existing Canonical Gists (created Session 678)

| # | Document | Gist URL | Published |
|---|----------|----------|-----------|
| 1 | Democratic Renewal Proposal (35 domains) | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | Session 678 |
| 2 | Executive Summary (2-page) | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | Session 678 |
| 3 | Litigation Tracker 2026 | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | Session 678 |
| 4 | First Amendment Suppression Tracker | https://gist.github.com/esca8peArtist/10d0a86e386e6c3c11c3830295a6503c | Session 678 |
| 5 | Environmental Rollbacks Tracker | https://gist.github.com/esca8peArtist/87e2bdb931b77480e56a08044c567bc4 | Session 678 |
| 6 | Police Consent Decree Tracker | https://gist.github.com/esca8peArtist/1f5cb28527c98d12526c14302c725731 | Session 678 |

### Pending Gists (create on path decision)

| # | Document | Status | Path | Notes |
|---|----------|--------|------|-------|
| 7 | Domain 37 (standalone) | PENDING — create at Phase A+37 execution Block 7-add | A+37 only | Title: "Domain 37 — Federal Executive Interference in the 2026 Midterms"; add advocacy window table footer from EXECUTION_PLAN_PATH_A_PLUS_37.md Section 5 |

### Future Gists (create as needed)

| # | Document | Trigger | Notes |
|---|----------|---------|-------|
| 8 | Domain 37b (State Election Security) | If fully researched before Phase 1b | Only if domain-37b-state-election-security-coordination.md receives full research |
| 9 | Litigation Tracker update | At 90-day mark or when Category 10+ entries require a full update | Update Gist 3 in place (edit the existing Gist) or create new dated version |
| 10 | Domain-specific one-pager | When Tier 1 contact requests a specific domain in briefing format | Use Section C Domain-Specific format; cite parent domain and Gist |

---

## Section F: Quick Reference for Domain 37 Gist Creation (Path A+37 Block 7)

This section is the exact procedure for creating the Domain 37 standalone Gist at the start of Path A+37 execution. Estimated time: 5 minutes.

1. Open https://gist.github.com — confirm logged in as esca8peArtist
2. Click "+" or navigate to https://gist.github.com/new
3. Set filename: `domain-37-federal-executive-interference-2026-midterms.md`
4. Set description: `Domain 37 — Federal Executive Interference in the 2026 Midterms | Democratic Renewal Research Framework`
5. Copy the Section A header block above (pre-filled Domain 37 version from Section C)
6. Paste below the header: the full content of `domains/domain-37-federal-executive-interference-2026-midterms.md`
7. Paste below the domain content: the advocacy window footer from `EXECUTION_PLAN_PATH_A_PLUS_37.md` Section 5 (reproduced here for convenience):

```
---

## Advocacy Windows — 2026 Midterm Timeline

| Date | Window | Action Needed |
|------|--------|---------------|
| May 30, 2026 | DOJ consent decrees finalized or challenged | Legal challenge and public pressure positioning |
| June 30, 2026 | Emergency EO routing window | OMB/legal review challenge opportunity |
| August 7, 2026 | NVRA 90-day quiet period begins | Pre-filed emergency injunction templates required |
| September 2026 | Pre-election litigation positioning | Section 3 disqualifications, voter roll restoration |
| October 2026 | Poll observer deployment | Legal hotline readiness, real-time election monitoring |

*This is a standalone excerpt from Domain 37 of the 35-domain Democratic Renewal Research framework.*
*Full proposal: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261*
```

8. Paste Section B footer at the very bottom
9. Set visibility to **Public**
10. Click "Create public gist"
11. Copy the resulting Gist URL
12. Record the URL in:
    - `DISTRIBUTION_GIST_URLS.md` (Domain 37 entry)
    - `PHASE_1_CONTACT_VERIFICATION.json` (`gist_url_log.domain_37` field)
    - The `[domain 37 link]` placeholder in `EXECUTION_PLAN_PATH_A_PLUS_37.md` Section 5 and Block 8
    - The `distribution-institutional-outreach-templates.md` Phase 1b template
13. Proceed to Block 8: Phase 1b email personalization

---

*Template created: May 1, 2026 (Session 716). Use this shell for all future Gist publications from the resistance-research project.*
