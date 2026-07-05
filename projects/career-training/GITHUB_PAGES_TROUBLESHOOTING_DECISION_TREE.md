---
title: "GitHub Pages Troubleshooting Decision Tree — Symptom to Root Cause to Fix"
project: career-training
phase: "1"
created: 2026-07-04
status: execution-ready
item: "53 (Session 4588)"
cross-reference: "GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md (detailed 6-check cloud build troubleshooting)"
---

# GitHub Pages Troubleshooting Decision Tree

**How to use this document**: Start at Step 0 every time. Work top-to-bottom. Each node has a binary branch — follow the one that matches your situation. The tree routes you to the specific failure from Item 50 that is causing the problem, with a direct link to the fix.

**Estimated time**: 2 minutes to diagnose. 5-30 minutes to fix depending on root cause.

---

## Step 0 — Locate the actual build state

Before diagnosing, determine what actually happened.

```bash
# If you have GitHub CLI installed:
gh repo view --web  # opens repo in browser; click Actions tab

# Or navigate manually:
# github.com/[your-username]/[your-repo] > Actions tab > latest workflow run
```

**What do you see?**

- Green checkmark on latest workflow run → site deployed. Go to **Step 1 (site is live but looks wrong)**.
- Red X on latest workflow run → build failed. Go to **Step 2 (build failure)**.
- No workflow runs at all → Pages may not be configured. Go to **Step 6 (Pages not active)**.
- Yellow circle (spinning) → build in progress. Wait 90 seconds and check again.

---

## Step 1 — Site deployed but looks wrong

The build succeeded (green checkmark) but the live site has rendering problems.

**Symptom: Site loads but shows plain black text on white background, no sidebar, no search box**

Root cause: `jekyll-remote-theme` is missing from the plugins list. GitHub Pages is using Minima (the default) instead of Just the Docs.

```bash
grep "jekyll-remote-theme" projects/career-training/docs/_config.yml
```

- If no output → Fix 2 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md` (add plugin to `_config.yml`)
- If plugin is listed → Go to next symptom

**Symptom: Sidebar present, but module pages show a 404 or raw text**

Root cause: `docs/_layouts/module.html` is missing or was not committed.

```bash
git log --oneline -- projects/career-training/docs/_layouts/module.html
```

- If no output → file was never committed. Fix 1 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md`
- If output shows commits → file is committed. Check it was pushed: `git push origin master` then wait for rebuild.

**Symptom: Navigation links broken (clicking module shows wrong page or blank)**

Root cause: `baseurl` mismatch. If your GitHub Pages URL is `yourusername.github.io/career-training` but `baseurl` is `""`, all links break.

```bash
grep "baseurl:" projects/career-training/docs/_config.yml
# Also check your actual GitHub Pages URL in repo Settings > Pages
```

- Custom domain (`constructiontrainingpath.com`) → `baseurl: ""` is correct
- GitHub subdomain with repo named `career-training` → `baseurl: "/career-training"` is required

**Symptom: Module pages load but no GA4 tracking (analytics empty)**

Root cause: `head_custom.html` missing, empty, or contains placeholder Measurement ID.

```bash
grep "G-" projects/career-training/docs/_includes/head_custom.html
```

- No output → file is missing or empty. Fix 3 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md`
- Output shows `G-XXXXXXXXXX` → placeholder not replaced. Substitute real Measurement ID.
- Output shows real ID (e.g., `G-ABC123DEF4`) → file is correct. Verify the file was committed and pushed.

**Symptom: Clicking "Get this path by email" returns 404**

Root cause: `signup.md` missing or not committed.

```bash
git log --oneline -- projects/career-training/docs/signup.md
```

- No output → file was never committed. Fix 4 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md`
- Output shows commits → file is committed. Confirm permalink is `/signup/` in the file's frontmatter.

**Symptom: Modules 37 or 38 not appearing in site navigation**

Root cause: Files are in `projects/career-training/` root, not `docs/modules/`.

```bash
ls projects/career-training/37-*.md projects/career-training/38-*.md 2>/dev/null
ls projects/career-training/docs/modules/37-*.md projects/career-training/docs/modules/38-*.md 2>/dev/null
```

- Files exist in root but not in `docs/modules/` → Fix 5 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md`

---

## Step 2 — Build failure (red X in Actions)

The build failed. Do not try to diagnose without reading the actual error message.

### Step 2A — Get the error message

1. GitHub repo > Actions tab > click the failed workflow run
2. Click the failing job (usually "build" or "pages build and deployment")
3. Expand all steps (click each triangle)
4. Find lines beginning with `Error:`, `Fatal:`, `Gem::`, or `Liquid Exception`
5. Copy the exact error text before continuing

### Step 2B — Match the error to a fix

**Error: `Layout 'module' does not exist`**

This is Item 50 Failure 1. Root cause: `docs/_layouts/module.html` does not exist on the remote (even if it exists locally).

```bash
git status projects/career-training/docs/_layouts/module.html
```

- "Changes not staged" or "Untracked files" → file exists locally but was not committed. Add, commit, push.
- No output → file does not exist. Apply Fix 1 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md`.

Full detailed fix: `GITHUB_PAGES_REMEDIATION_RUNBOOK.md` Fix 1.

---

**Error: `Could not find gem 'jekyll-remote-theme'` or `remote: Theme not found`**

Two distinct causes:

Cause A — `jekyll-remote-theme` not in `_config.yml` plugins list (Item 50 Failure 2):
```bash
grep "jekyll-remote-theme" projects/career-training/docs/_config.yml
```
No output → apply Fix 2 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md`.

Cause B — A `Gemfile` is present that conflicts with GitHub Pages' managed gem set:
```bash
ls projects/career-training/docs/Gemfile 2>/dev/null
```
If a Gemfile exists, it must include `gem "jekyll-remote-theme"` or the file should be deleted to use GitHub Pages' managed build. See `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` Check 2.

---

**Error: `Liquid Exception` or `Liquid::SyntaxError`**

The error log will name the specific file. This is a Liquid template syntax error in a Markdown or HTML file — not one of the Item 50 failures.

1. Find the file named in the error
2. Search for unclosed `{% %}` or `{{ }}` tags
3. Common cause: a curly-brace code block in a module file that Jekyll interprets as Liquid syntax
4. Fix: wrap the code block in `{% raw %}...{% endraw %}` tags or ensure the content is in a fenced code block (\`\`\`)

---

**Error: `YAML Exception` or `SyntaxError in frontmatter`**

The error log will name the specific file. This is a YAML syntax error in a file's frontmatter.

Common causes:
- Unquoted string containing a colon: `title: Module 5: Civil Engineering` → should be `title: "Module 5: Civil Engineering"`
- Tab characters in YAML (YAML requires spaces only)
- Inconsistent indentation in multi-value fields

Fix: open the named file, inspect the first 10-15 lines (`---` to `---`), correct the YAML.

---

**Error: `Permission denied` or `403`**

GitHub Actions does not have write permission to deploy.

1. Repository Settings > Actions > General > Workflow permissions
2. Set to "Read and write permissions"
3. Also check Settings > Pages — confirm source branch is `master` (not `main`, which is the default GitHub name but this repo uses `master`)

See `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` Check 2 "Permission".

---

**Error: `Gem::InstallError` / `Bundler could not find compatible versions`**

Ruby or gem version mismatch between local and cloud build.

Check if a `Gemfile` exists in `docs/`:
```bash
ls projects/career-training/docs/Gemfile 2>/dev/null || echo "No Gemfile"
```

- No Gemfile → using GitHub Pages managed build → version mismatch is not the issue → re-read the error more carefully
- Gemfile present → see `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` Checks 4 and 5 for Gemfile resolution

---

**No error matches above / error not recognized**

Go to `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` Step 0 and work through all 6 checks sequentially.

---

## Step 3 — Local build works, cloud build fails

This is the most confusing failure mode. Everything works at `localhost:4000`. GitHub Actions shows red.

**First check**: Was everything committed and pushed?

```bash
git status
git log --oneline origin/master..HEAD
```

- Uncommitted changes → stage, commit, push, wait for rebuild
- Commits not pushed → `git push origin master`, wait for rebuild
- Everything pushed → continue below

**Second check**: Is the error one of the Item 50 failures?

The most common reason local builds work but cloud builds fail is that you created a file locally (like `_layouts/module.html`) but forgot to commit it. The local build sees the file; the cloud build does not.

```bash
git diff --name-only HEAD
git status --short | grep "^?"
```

Any untracked or unstaged file that the build needs → add, commit, push.

**Third check**: Gemfile.lock platform issue

If you have a `Gemfile.lock` generated on macOS or Windows, it may lack Linux platform entries:

```bash
cd projects/career-training/docs
bundle lock --add-platform x86_64-linux
git add Gemfile.lock
git commit -m "fix: add linux platform to Gemfile.lock"
git push origin master
```

**Fourth check**: Jekyll version or theme version pinning

If none of the above resolves it, pin the Just the Docs theme to a specific release to prevent floating-version issues:

```yaml
# In _config.yml, change:
remote_theme: just-the-docs/just-the-docs
# To (check https://github.com/just-the-docs/just-the-docs/releases):
remote_theme: just-the-docs/just-the-docs@v0.10.0
```

Commit and push. See `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` Check 2 "404: Not Found (during theme loading)".

---

## Step 4 — Build succeeded but site is not live

Green checkmark in Actions, but navigating to your GitHub Pages URL shows 404 or "There isn't a GitHub Pages site here."

**Check 1: Is GitHub Pages configured?**

1. Repository Settings > Pages (left sidebar)
2. Build and deployment > Source > must be "Deploy from a branch"
3. Branch: `master` — this repo uses `master`, not `main`
4. Folder: `/docs`

If Source shows "GitHub Actions" but you have no `.github/workflows/pages.yml`: switch to "Deploy from a branch" with `/docs`.

If Pages shows as disabled: the repository may be private on a free plan. GitHub Pages requires either a public repository or a paid plan for private repos.

**Check 2: Has enough time passed?**

First deployments can take 3-10 minutes to propagate. Subsequent deploys after a successful first deploy are usually faster (1-3 minutes). If it has been less than 10 minutes since the green checkmark appeared, wait.

**Check 3: Custom domain DNS**

If you configured a custom domain (`constructiontrainingpath.com`) and DNS has not propagated yet, the GitHub Pages URL (`yourusername.github.io`) still works but the custom domain does not. Test with the raw `github.io` URL to isolate DNS issues from build issues.

DNS propagation takes 24-48 hours after a DNS record change. Check propagation status at [dnschecker.org](https://dnschecker.org).

---

## Step 5 — Specific failure isolation: which of the 4 Item 50 failures is active?

Use this quick diagnostic if you are not sure which failure you are dealing with. Run all 4 checks in sequence:

```bash
echo ""
echo "DIAGNOSTIC: Item 50 Failure Isolation"
echo "======================================"
echo ""

echo "[Failure 1] layout: module exists?"
ls projects/career-training/docs/_layouts/module.html 2>/dev/null && echo "  PRESENT — not Failure 1" || echo "  MISSING — apply Fix 1"

echo ""
echo "[Failure 2] jekyll-remote-theme in plugins?"
grep "jekyll-remote-theme" projects/career-training/docs/_config.yml >/dev/null 2>&1 && echo "  PRESENT — not Failure 2" || echo "  MISSING — apply Fix 2"

echo ""
echo "[Failure 3] head_custom.html with real GA4 ID?"
if [ -f projects/career-training/docs/_includes/head_custom.html ]; then
  if grep -q "G-XXXXXXXXXX" projects/career-training/docs/_includes/head_custom.html; then
    echo "  FILE EXISTS but PLACEHOLDER ID — replace with real Measurement ID"
  elif grep -q "G-" projects/career-training/docs/_includes/head_custom.html; then
    echo "  PRESENT with real ID — not Failure 3"
  else
    echo "  FILE EXISTS but no GA4 ID found — check file contents"
  fi
else
  echo "  FILE MISSING — apply Fix 3"
fi

echo ""
echo "[Failure 4] signup.md exists?"
ls projects/career-training/docs/signup.md 2>/dev/null && echo "  PRESENT — not Failure 4" || echo "  MISSING — apply Fix 4"

echo ""
echo "[Bonus] Modules 37-38 location?"
M37=$(ls projects/career-training/docs/modules/37-*.md 2>/dev/null | wc -l)
M38=$(ls projects/career-training/docs/modules/38-*.md 2>/dev/null | wc -l)
ROOT37=$(ls projects/career-training/37-*.md 2>/dev/null | wc -l)
ROOT38=$(ls projects/career-training/38-*.md 2>/dev/null | wc -l)
echo "  In docs/modules/: 37=$M37, 38=$M38"
echo "  In root (incorrect location): 37=$ROOT37, 38=$ROOT38"
```

Each line tells you which failure is active and points to the specific fix.

---

## Step 6 — GitHub Pages not configured at all

No workflow runs have ever appeared in the Actions tab. The site has never been live.

1. Confirm the repository exists on GitHub and you are looking at the right repo
2. Repository Settings > Pages
3. Under "Build and deployment", set:
   - Source: "Deploy from a branch"
   - Branch: `master`
   - Folder: `/docs`
4. Click Save
5. Wait 90 seconds — a workflow run should appear automatically in the Actions tab
6. If no workflow appears after 2 minutes: make a trivial commit and push (e.g., add a blank line to `README.md`)

If Pages settings are not visible at all: GitHub Pages requires the repository to be public (free plan) or on a paid plan (private repos). Check repository Settings > General > Repository visibility.

---

## Escalation Path

If you have worked through all applicable steps and the issue is unresolved:

**Option 1 (< 2 hours remaining before urgency)**: Activate fallback deployment.
See `PHASE_1_FALLBACK_ACTIVATION_PROCEDURES.md` — Netlify deployment takes 20-30 minutes and runs the identical Jekyll build. The site is live on Netlify while GitHub Pages is being resolved.

**Option 2 (non-urgent)**: Open a GitHub support ticket.
- URL: [support.github.com](https://support.github.com)
- Include: repository URL, exact error text from Actions log, Ruby and Jekyll versions
- Response time on free plan: 2-7 business days

---

## Quick Reference Table

| Symptom | Root Cause | Item 50 Failure | Fix Location |
|---------|-----------|-----------------|-------------|
| Build fails: `Layout 'module' does not exist` | `_layouts/module.html` missing | Failure 1 | Fix 1 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md` |
| Site loads with Minima theme (no sidebar) | `jekyll-remote-theme` not in plugins | Failure 2 | Fix 2 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md` |
| Site live but GA4 empty / no tracking | `head_custom.html` missing or placeholder ID | Failure 3 | Fix 3 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md` |
| `/signup/` returns 404 | `signup.md` missing | Failure 4 | Fix 4 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md` |
| Modules 37-38 not in site nav | Files in wrong directory | Bonus (not fatal) | Fix 5 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md` |
| Local works, cloud fails | File not committed/pushed | Any of the above | `git status` + commit + push |
| Build fails: `Liquid Exception` | Template syntax error in file | Not Item 50 | `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` Check 2 |
| Build fails: `YAML Exception` | Frontmatter syntax error | Not Item 50 | `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` Check 2 |
| Build green but site not live | GitHub Pages not configured | Configuration | Step 6 above |
| Pages not available | Private repo + free plan | Plan tier | Step 4 Check 1 + `GITHUB_ACTIONS_TROUBLESHOOTING_FLOWCHART.md` Check 6 |
| 2h troubleshooting, no resolution | Unknown | — | Activate fallback: `PHASE_1_FALLBACK_ACTIVATION_PROCEDURES.md` |
