---
title: "Publication README: OpSec Corpus (Threat Model + Playbook + Implementation Guide)"
project: cybersecurity-hardening
created: 2026-04-26
status: publication-ready
---

# Publication README: OpSec Corpus

This document describes what to publish, who it is for, and how to publish it. The corpus is ready to go as-is.

---

## What Is Being Published

Three documents that work as a unit:

| File | Content | Length |
|------|---------|--------|
| `threat-model.md` | Verified government surveillance capabilities (Palantir, NSA, FBI, data brokers, DOGE) with primary-source citations | ~440 lines |
| `opsec-playbook.md` | Countermeasures mapped directly to confirmed threat capabilities, organized by tier | ~635 lines |
| `implementation-guide.md` | Step-by-step setup instructions for each countermeasure, with verification checkpoints and troubleshooting | ~1,030 lines |

Supporting material in `publication-prep.md`:
- 600-word executive summary (ready to copy-paste as a preface or blog post)
- Full hierarchical table of contents for the entire corpus
- 40-term glossary

---

## Who Benefits Most From This

Primary audience, in order of urgency:

1. **Undocumented people and their immediate support networks** — Part 0 of the implementation guide (data broker opt-outs) is no-technical-expertise-required and directly degrades ELITE's address confidence scoring. The AB 60/AB 1766 path for California residents without government-issued ID is documented.

2. **Immigration advocates, healthcare workers who serve undocumented people, and legal aid organizations** — Tier 1 setup. Elevated risk from administrative surveillance; data broker reduction and Signal configuration are the immediate priorities.

3. **Protest organizers, civil rights litigants, labor organizers** — Tier 2 setup. The GrapheneOS + VPN-then-Tor configuration provides meaningful protection against location data harvesting and ISP-level surveillance.

4. **Journalists, lawyers, and people who believe they are targets of active investigation** — Tier 3 setup. The full stack including VeraCrypt, Qubes OS, Monero, and hardware security keys.

5. **Security researchers and digital rights advocates** — The threat model section is a primary-sourced map of confirmed government contracts and capabilities, useful for advocacy, litigation, and policy work.

Secondary audiences who benefit from awareness even if they don't implement countermeasures:

- General public concerned about commercial surveillance infrastructure
- Policy advocates working on data broker legislation, Section 702 reform, or Fourth Amendment expansion
- Journalists covering immigration enforcement, surveillance technology, or Palantir

---

## What This Corpus Is Not

- It does not cover organizational security for groups (a different threat model)
- It does not cover physical surveillance countermeasures (TSCM)
- It does not cover international travel security
- It does not provide legal strategy around compelled decryption (it provides the facts; consult a lawyer)

---

## Publishing Instructions

### Option A: GitHub Gist (Recommended for Immediate Distribution)

GitHub Gist allows publishing multiple files as a single shareable URL, with rendered Markdown.

1. Go to https://gist.github.com (sign in or create an account)
2. Create a new Gist
3. Add three files in this order:
   - First file: `threat-model.md` — paste the full content
   - Add another file: `opsec-playbook.md` — paste the full content
   - Add another file: `implementation-guide.md` — paste the full content
   - Optional: add `publication-prep.md` as a fourth file for the glossary and TOC
4. Set visibility to **Public**
5. Click "Create public gist"
6. Copy the URL — this is your shareable link

The Gist URL can be shared directly. GitHub renders the Markdown including tables, code blocks, and headers.

### Option B: Static Site (More Durable)

Tools that convert Markdown to a navigable website with minimal configuration:

- **MkDocs** (mkdocs.org) — install with `pip install mkdocs`, place the three files in a `docs/` directory, run `mkdocs build`. Free hosting via GitHub Pages with `mkdocs gh-deploy`.
- **Obsidian Publish** — if you already use Obsidian, Publish ($10/month) creates a navigable site from your vault. These files are Obsidian-compatible.
- **HackMD** (hackmd.io) — free collaborative Markdown platform. Create a Book from multiple notes for a navigable multi-document publication.

### Option C: PDF

To convert to PDF for distribution via email or secure drop:

- macOS: Open each file in Typora or MarkdownPad, File > Export > PDF
- Any OS: Install Pandoc (`brew install pandoc` or `apt install pandoc`) and run:
  ```
  pandoc threat-model.md opsec-playbook.md implementation-guide.md -o opsec-corpus.pdf
  ```
- For a table of contents in the PDF: `pandoc --toc threat-model.md opsec-playbook.md implementation-guide.md -o opsec-corpus.pdf`

### Option D: SecureDrop

If distributing to journalists or researchers through SecureDrop:

1. Upload the three Markdown files (or the combined PDF) as a zip archive
2. Include the executive summary from `publication-prep.md` as the cover note in the SecureDrop submission

---

## How to Cite This Work

There is no standard citation format required, but the following can be used:

**Short form**:
> "OpSec Corpus: Government Surveillance Threat Model and Countermeasure Guide" (2026). Available at: [URL]

**Long form for legal or academic use**:
> "OpSec Corpus: Government Surveillance Infrastructure Threat Model, Defensive Countermeasures Playbook, and Implementation Guide." Version 1.0, April 2026. Primary sources documented inline throughout. For questions about methodology, contact via the publishing platform.

**Attribution note**: The corpus may be reproduced and distributed freely. If you adapt or excerpt it, note the original source and indicate what was changed — readers deserve to know which parts are original and which are modified.

---

## Version and Currency

This corpus reflects the surveillance landscape as of **April 26, 2026**. Key time-sensitive items:

- Section 702 reauthorization status is current as of April 2026 — renewal debate is ongoing
- DOGE litigation (15+ active lawsuits) is evolving; the DOGE section describes the situation as of April 2026
- Palantir contract figures are current as of Q1 2026
- GrapheneOS-supported device list changes; always verify at grapheneos.org/faq before purchasing
- LexisNexis contract values updated from 2021 DHS contract; check USASpending.gov for renewals

The threat model and tool recommendations should be reviewed quarterly. The maintenance schedule in Part 8 of the implementation guide provides a structured review process.

---

## Pre-Publication Final Checklist

- [x] threat-model.md: status field updated to `complete`
- [x] threat-model.md: drafting artifact ("Next document to produce") removed
- [x] opsec-playbook.md: complete, no TODOs
- [x] implementation-guide.md: complete, no TODOs
- [x] Glossary: 40 terms covering all technical vocabulary in the corpus
- [x] Executive summary: 600 words, audience-ready
- [x] Full table of contents: complete, hierarchical
- [x] All internal cross-references verified (threat-model → opsec-playbook → implementation-guide)
- [x] All external URLs checked for format (note: URLs should be spot-checked for liveness before publication, as sites change)
