---
title: "Wave 0 Contributor Onboarding Template"
project: open-repo
phase: "5.2 Wave 0"
document_type: template
status: copy-paste-ready
date: 2026-06-28
---

# Wave 0 Contributor Onboarding Template

This file contains two copy-paste-ready artifacts:

1. **GitHub Issue Template** — the form a contributor fills out to submit a procedure (place at `.github/ISSUE_TEMPLATE/submit-procedure.md`)
2. **Contribution Guide outline** — content for `docs/contributing/index.md`

Both are designed for non-technical contributors. Target: 5 minutes from discovery to first submission.

---

## Artifact 1 — GitHub Issue Template

**File path**: `.github/ISSUE_TEMPLATE/submit-procedure.md`

Copy-paste the block below verbatim:

```markdown
---
name: Submit a procedure
about: Share a how-to guide for water systems, food preservation, seed saving, or related topics
title: "[SUBMIT] "
labels: contribution, needs-review
assignees: ''
---

## Submit a Procedure

Thank you for contributing to open-repo. This form takes about 5 minutes to complete.

Fill in the sections below. You do not need to know JSON or GitHub to contribute — just answer the questions in plain English.

---

### 1. Procedure title

What is this procedure called?

> Example: "How to make a slow sand water filter"
> Example: "Canning tomatoes with a water-bath canner"
> Example: "Drying and storing bean seeds"

**Title**: 

---

### 2. Domain

Which category does this procedure belong to?

- [ ] Water systems (purification, filtration, harvesting, storage)
- [ ] Food preservation (canning, fermentation, dehydration, root cellaring)
- [ ] Seed preservation (cleaning, drying, storing, testing viability)
- [ ] Other (describe): 

---

### 3. Source

Where does this information come from?

This is important: we only publish procedures that come from authoritative sources OR from your own verified personal practice.

Choose one:

- [ ] I am describing my own practice (I have done this successfully and can vouch for it)
- [ ] This comes from a published source — paste the URL or book/author/page number below:

**Source URL or citation**:

---

### 4. The procedure

Write out the procedure in plain language. Use numbered steps. Include:
- What materials or tools are needed
- Any important measurements, temperatures, or quantities
- Any warnings or safety notes
- How to know when each step is done correctly

There is no minimum or maximum length. A clear 5-step procedure is better than a vague 20-step one.

**Procedure**:

```
Step 1:

Step 2:

Step 3:

(add more as needed)
```

---

### 5. License confirmation

- [ ] I confirm that this content is either:
  - My own original work, OR
  - Reproduced or adapted from a source I cited above that permits redistribution under a Creative Commons or equivalent open license

Content published in open-repo is licensed CC BY-SA 4.0.

---

### 6. Attribution (optional)

How would you like to be credited if we publish this?

- [ ] Use my GitHub username: @{username}
- [ ] Use this name instead: 
- [ ] No attribution needed
- [ ] Link to my website or profile: 

---

*A maintainer will review this submission within 72 hours and respond in this issue thread. We will let you know if we need clarification or if the procedure is ready to publish.*
```

---

## Artifact 2 — Contribution Guide

**File path**: `docs/contributing/index.md`

Copy-paste the block below verbatim. Replace `{GITHUB_REPO_URL}` with `https://github.com/esca8peArtist/open-repo`.

```markdown
---
layout: page
title: "How to Contribute"
permalink: /contributing/
---

# How to Contribute to open-repo

open-repo is a free, offline-accessible library of practical knowledge. You do not need to be a programmer to contribute. If you know how to do something — purify water in an emergency, preserve food without refrigeration, save seeds for next season — your knowledge belongs here.

---

## What we publish

We publish structured, step-by-step procedures in these domains:

- **Water systems**: Purification, filtration, collection, storage, testing
- **Food preservation**: Canning, fermentation, dehydration, root cellaring, smoking
- **Seed preservation**: Cleaning, drying, storing, viability testing

We do not currently accept general advice, opinion pieces, or content without a cited source or personal practice basis.

---

## How to submit (5 minutes)

**Step 1**: Go to the issue submission form:  
[Submit a procedure →]({GITHUB_REPO_URL}/issues/new?template=submit-procedure.md)

**Step 2**: Fill in the form. The key fields are:
- What the procedure is called
- Which domain it belongs to
- Where the information comes from (your own practice, or a source you can cite)
- The procedure itself, written in plain numbered steps

**Step 3**: Click "Submit new issue." You are done.

A maintainer will review your submission within 72 hours and respond in the issue thread.

---

## What happens after you submit

1. A maintainer reads your submission and checks the source
2. If it looks good, we convert it to the structured format and prepare it for publishing
3. We let you know when it goes live — you can share the direct link to your published procedure
4. Your name (or chosen attribution) appears on the published procedure page

If we need clarification, we will ask one specific question in the issue thread. We will not ask you to learn JSON or GitHub formatting.

---

## What makes a good submission

**Do:**
- Use numbered steps
- Include specific measurements where they matter (temperatures, times, quantities)
- Cite your source (a URL, book title, or "my own 10 years of practice")
- Include a note on how to tell each step is done correctly
- Flag any safety warnings

**Do not:**
- Copy-paste copyrighted text without permission
- Submit general background information (we need procedures, not encyclopedia articles)
- Submit anything requiring a licensed professional to verify without contacting us first (especially medical treatment protocols)

---

## Content types we accept with immediate review

| Content type | Review requirements | Expected time to publish |
|---|---|---|
| Water purification (boiling, chemical, filtration) | Source verification only | 2–5 days |
| Food preservation from NCHFP or USDA | Source verification only | 2–5 days |
| Your own tested practice | Source verification + one corroborating source | 3–7 days |
| Seed saving procedures | Source verification | 3–7 days |
| Medical or clinical content | Requires medical reviewer sign-off | Not in Wave 0 — contact us first |

---

## For technical contributors

If you are comfortable with JSON and GitHub pull requests, you can submit structured JSON-LD directly:

1. Clone the repository
2. Write a procedure using one of the published schemas: [schemas/]({GITHUB_REPO_URL}/blob/main/projects/open-repo/docs/schemas/)
3. Validate against the schema (any JSON Schema validator works)
4. Open a pull request against `main` with your new file in `content/{domain}/{slug}.json`

Schema documentation: [{GITHUB_REPO_URL}/blob/main/projects/open-repo/SCHEMA_DOCUMENTATION.md]

---

## Attribution and licensing

Every procedure you contribute is attributed to you (by name, GitHub username, or anonymously — your choice). Attribution is permanent and travels with the content in all formats, including ZIM files for offline distribution.

All content in open-repo is published under [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). By submitting, you confirm you have the right to release the content under this license.

---

## Questions?

Open an issue with the label `question` and a maintainer will respond within 72 hours.

[Ask a question →]({GITHUB_REPO_URL}/issues/new?labels=question&title=Question%3A+)
```

---

## Maintainer Playbook — Reviewing Submissions

This section is for the maintainer, not for contributors. Not published on GitHub Pages.

### Review checklist (per submission)

- [ ] Source is real and accessible (visit the URL or confirm the publication exists)
- [ ] Procedure matches what the source says (not contradicted by the cited source)
- [ ] Measurements and quantities are present where safety-relevant (canning temps, chemical doses)
- [ ] No content that requires professional licensure to validate (medical treatment, electrical code, structural engineering) — if present, hold for specialist review
- [ ] License checkbox is checked in the submission
- [ ] Steps are numbered and individually comprehensible
- [ ] Attribution preference is noted

### Conversion workflow (Type A contributor — plain text to JSON-LD)

1. Open the relevant schema file: `projects/open-repo/schemas/{domain}.schema.json`
2. Create `content/{domain}/{slug}.json` from the submission
3. Validate: `cat content/water/{slug}.json | python3 -c "import json,sys,jsonschema; jsonschema.validate(json.load(sys.stdin), json.load(open('schemas/water_systems.schema.json')))"`
4. Create `docs/content/{domain}/{slug}.md` with the human-readable Markdown version
5. Add the item to `docs/content/{domain}/index.md` table
6. Add contributor to `docs/contributors.md`
7. Commit and push to `main`
8. Reply to the GitHub issue with the live URL

### Response templates

**Accepting with publication date:**
```
Thank you for submitting! We have reviewed your procedure and it looks great. 

We will publish it at: [URL] within the next 2 days. Once live, you can share this link directly.

Your attribution will appear as: [name/username]

If you have more procedures to share, use the same submission form — each submission gets its own issue thread.
```

**Requesting clarification:**
```
Thank you for submitting! We have one question before we can publish:

[ONE SPECIFIC QUESTION]

Once you respond, we will complete the review within 24 hours.
```

**Declining:**
```
Thank you for submitting. We are not able to publish this procedure in its current form because:

[SPECIFIC REASON — e.g., "the source you cited is commercially licensed and does not permit redistribution" OR "we could not verify the measurements in your cited source"]

If you can [SPECIFIC FIX — e.g., "find a public-domain alternative source for the same information" OR "clarify the temperature ranges"], we would be happy to review a revised submission.
```

---

*Prepared 2026-06-28. Copy-paste ready for production use.*
