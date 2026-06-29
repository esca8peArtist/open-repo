# open-repo — GitHub Pages Setup

**Repo**: `esca8peArtist/open-repo` (already exists and is public)
**GitHub Pages URL (after setup)**: `https://esca8peArtist.github.io/open-repo/`
**Status**: Repo exists. Pages not yet enabled. Content prepared in `docs/`.

---

## What Goes on GitHub Pages

The open-repo GitHub Pages site is the **project documentation and public landing page** — not the application itself (the FastAPI backend runs on a separate server). The site covers:

- What open-repo is and why it exists
- How to download ZIM files for offline use (Kiwix)
- Content schemas for contributors (Phase 5.2 Wave 0)
- API documentation for federation partners
- Contributing guide

The application backend is deployed separately (see `DOCKER_DEPLOYMENT_RUNBOOK.md`).

---

## Step 1 — Enable GitHub Pages

Run this once:

```bash
gh api \
  --method POST \
  repos/esca8peArtist/open-repo/pages \
  --field source='{"branch":"main","path":"/docs"}' \
  --header "Accept: application/vnd.github.v3+json" 2>&1 || \
gh api \
  --method PUT \
  repos/esca8peArtist/open-repo/pages \
  --field source='{"branch":"main","path":"/docs"}' \
  --header "Accept: application/vnd.github.v3+json"
```

If the CLI call fails (Pages may need to be enabled via UI first), go to:
**Settings → Pages → Source → Deploy from a branch → Branch: `main`, Folder: `/docs`**

---

## Step 2 — Confirm docs/ content is ready

The following files are already prepared in `projects/open-repo/docs/`:

```
docs/
├── index.md                  ← GitHub Pages landing page (prepared)
├── _config.yml               ← Jekyll config (needs to be created — see Step 3)
└── [existing audit docs]     ← internal docs, will not appear in nav unless linked
```

And in `schemas/` (already complete — Phase 5.2 Wave 0):
```
schemas/
├── medical_article.schema.json
├── botanical_knowledge.schema.json
├── water_systems.schema.json
├── seed_preservation.schema.json
└── food_preservation.schema.json
```

---

## Step 3 — Create Jekyll config

Create `projects/open-repo/docs/_config.yml` with:

```yaml
title: open-repo
description: A free, open, distributed library of human knowledge — guides, schematics, recipes, 3D models, and more
baseurl: "/open-repo"
url: "https://esca8peArtist.github.io"
theme: minima
markdown: kramdown
kramdown:
  input: GFM
exclude:
  - deployment-planning/
  - "A11Y_*.md"
```

---

## Step 4 — Push and verify

```bash
# From the repo root — commit only the docs/ additions
git add projects/open-repo/docs/index.md projects/open-repo/docs/_config.yml
git commit -m "feat(open-repo): GitHub Pages landing page and Jekyll config"
git push origin master

# After push, check that Pages build starts:
gh run list --repo esca8peArtist/open-repo --limit 5

# Once build completes (typically 1-2 min):
# Visit: https://esca8peArtist.github.io/open-repo/
```

Note: GitHub Pages builds from the `/docs` folder of the `main` (or `master`) branch. If the remote default branch is `main`, change `master` in the push command above.

---

## Step 5 — Publish schemas to Pages (optional but recommended)

The JSON schemas in `schemas/` are not automatically served by GitHub Pages because they're outside `/docs`. To make them available at a stable URL:

```bash
mkdir -p projects/open-repo/docs/schemas
cp projects/open-repo/schemas/*.schema.json projects/open-repo/docs/schemas/
git add projects/open-repo/docs/schemas/
git commit -m "feat(open-repo): publish Phase 5.2 content schemas to GitHub Pages"
git push origin master
```

This makes schemas available at:
- `https://esca8peArtist.github.io/open-repo/schemas/medical_article.schema.json`
- `https://esca8peArtist.github.io/open-repo/schemas/botanical_knowledge.schema.json`
- (etc.)

These stable URLs can be referenced in the JSON schema `$schema` field and in contributor documentation.

---

## Medical Reviewer Outreach

The draft outreach email is at `projects/open-repo/medical-reviewer-outreach-draft.md`.

**Before sending**: replace the `[Project repository]` placeholder with:
`https://github.com/esca8peArtist/open-repo`

The three primary contacts are already identified in the draft:
1. Wilderness Medical Society — `guidelines@wms.org`
2. MSF Clinical Guidelines team — `medicalguidelines@msf.org`
3. ICRC First Aid program — `assist@icrc.org`

No additional content can be prepared autonomously (requires actual outreach with specific reviewer identity). The email is ready to send as written, with only the GitHub URL placeholder to fill in.

---

## Phase 5.2 Wave 0 Schemas — Status

All five Phase 5.2 Wave 0 content-type schemas are complete in `projects/open-repo/schemas/`:

| Schema | File | Status |
|---|---|---|
| Medical article (drug monographs, procedures) | `medical_article.schema.json` | Complete |
| Botanical knowledge (species cards, seed saving) | `botanical_knowledge.schema.json` | Complete |
| Water systems (treatment, sourcing, safety) | `water_systems.schema.json` | Complete |
| Seed preservation (genetics, viability, storage) | `seed_preservation.schema.json` | Complete |
| Food preservation (canning, fermentation, storage) | `food_preservation.schema.json` | Complete |

These cover all three Priority 1 Phase 5.2 candidates (Medical Reference, Water Systems, Seed Preservation) plus Botanical Knowledge (Phase 5.2 Candidate 1) and Food Preservation. No new schemas are needed for Phase 5.2 Wave 0 activation.

---

*Prepared 2026-06-28. Repo exists: esca8peArtist/open-repo. No server hosting required — GitHub Pages is static.*
