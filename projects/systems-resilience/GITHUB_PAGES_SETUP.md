# systems-resilience — GitHub Pages Setup

**Recommended repo name**: `midwest-resilience-guide`
**GitHub URL (after creation)**: `https://github.com/esca8peArtist/midwest-resilience-guide`
**GitHub Pages URL**: `https://esca8peArtist.github.io/midwest-resilience-guide/`
**Status**: Repo does not yet exist. Content prepared in `projects/systems-resilience/docs/`.

Rationale for name: matches the existing pattern (`off-grid-living-guide`), is searchable, and names the geographic scope (Midwest) which is the defining constraint of this project. Alternatives: `zone5-resilience-guide`, `systems-resilience-midwest`.

---

## Step 1 — Create the GitHub repo

```bash
gh repo create esca8peArtist/midwest-resilience-guide \
  --public \
  --description "A practical resilience guide for Midwest Zone 5 — individual, household, and community scale" \
  --homepage "https://esca8peArtist.github.io/midwest-resilience-guide/" \
  --clone
```

This creates the repo and clones it locally to `./midwest-resilience-guide/`.

---

## Step 2 — Decide what to publish initially

### Initial publish (Phase 6 Domain A — ready now)

The Phase 6 Domain A document (`01-community-economic-resilience.md`, ~6,800 words, 38 citations) is production-ready and prepared for web publication at:

```
projects/systems-resilience/docs/
├── _config.yml                                  ← Jekyll config (prepared)
├── index.md                                     ← Site landing page (prepared)
└── phase-6/
    ├── index.md                                 ← Phase 6 landing (prepared)
    └── community-economic-resilience.md         ← Domain A full content (prepared)
```

### Phase 5 corpus (pending maintainer permissions — see MAINTAINER_PERMISSIONS_REQUEST.md)

The Phase 5 Waves 1+2 Integrated Corpus (16,234 words, 5 domains) at `PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md` is publication-ready but blocked on push access to the target release repo. Once access is resolved, add to docs/ using the structure in the Phase 5 GitHub Pages Staging Report (`PHASE_5_GITHUB_PAGES_STAGING.md`).

---

## Step 3 — Copy docs/ to the new repo

After Step 1 clone, copy the prepared docs content:

```bash
# Run from SuperClaude_Framework root
cp -r projects/systems-resilience/docs/* ../midwest-resilience-guide/docs/
cp projects/systems-resilience/README.md ../midwest-resilience-guide/README.md
```

Directory structure in the new repo:

```
midwest-resilience-guide/
├── README.md
└── docs/
    ├── _config.yml
    ├── index.md
    └── phase-6/
        ├── index.md
        └── community-economic-resilience.md
```

---

## Step 4 — Enable GitHub Pages on the new repo

```bash
cd ../midwest-resilience-guide

git add .
git commit -m "feat: initial publication — Phase 6 Domain A community economic resilience"
git push origin main

# Enable Pages pointing at /docs on main branch:
gh api \
  --method POST \
  repos/esca8peArtist/midwest-resilience-guide/pages \
  --field source='{"branch":"main","path":"/docs"}' \
  --header "Accept: application/vnd.github.v3+json"
```

If the API call fails, enable via:
**Settings → Pages → Source → Deploy from a branch → Branch: `main`, Folder: `/docs`**

---

## Step 5 — Verify

After the GitHub Actions Pages build completes (typically 1-2 minutes):

```bash
# Check build status
gh run list --repo esca8peArtist/midwest-resilience-guide --limit 3

# Expected URLs after build:
# https://esca8peArtist.github.io/midwest-resilience-guide/
# https://esca8peArtist.github.io/midwest-resilience-guide/phase-6/
# https://esca8peArtist.github.io/midwest-resilience-guide/phase-6/community-economic-resilience/
```

---

## Phase 5 GitHub Release (after maintainer permissions resolved)

Once push access to the release target repo is granted (see `MAINTAINER_PERMISSIONS_REQUEST.md`), create the Phase 5 GitHub Release:

```bash
# Tag the Phase 5 release
git tag -a v0.5.0 -m "Phase 5 Waves 1+2 — Community Resilience Infrastructure and Governance"
git push origin v0.5.0

# Create GitHub Release with the corpus as a downloadable asset
gh release create v0.5.0 \
  --title "Phase 5: Community Resilience Infrastructure and Governance" \
  --notes "$(cat <<'EOF'
Phase 5 Waves 1+2 Integrated Corpus — complete community resilience framework for Zone 5 Midwest.

**Domains covered**:
- Distributed Microgrids (687 operational U.S. microgrids, Zone 5 deployment patterns)
- Community Implementation Playbook (Tier 3 coordination framework, 50-150 people)
- Conflict Resolution and Governance Framework
- Psychological Support and Trauma Recovery
- Veterinary Care in Crisis Contexts

**Stats**: 16,234 words, 5 domains, sourced from 45,380-word research corpus.

For individual, household, and community practitioners in Midwest Zone 5 (Illinois, Wisconsin, Iowa, Minnesota, Michigan, Indiana).
EOF
)" \
  PHASE_5_WAVE_1_2_INTEGRATED_CORPUS.md
```

---

## Jekyll Config (already written at `docs/_config.yml`)

```yaml
title: Midwest Resilience Guide
description: A practical resilience guide for Midwest Zone 5 — individual, household, and community scale
baseurl: "/midwest-resilience-guide"
url: "https://esca8peArtist.github.io"
theme: minima
markdown: kramdown
kramdown:
  input: GFM
```

---

*Prepared 2026-06-28. No server hosting required — GitHub Pages is static and free.*
