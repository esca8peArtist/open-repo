---
title: "GitHub Actions Troubleshooting Flowchart — GitHub Pages Build Failures"
project: career-training
phase: "1"
created: 2026-06-29
status: execution-ready
scenario: "Local jekyll serve passes; GitHub Actions red X"
---

# GitHub Actions Troubleshooting Flowchart

**Scenario**: Your local `bundle exec jekyll serve` runs cleanly — the site loads in your browser at `localhost:4000`, all pages render, no errors in the terminal. You push to GitHub. The Actions tab shows a red X. GitHub Pages does not deploy. Nothing is live.

**How to use this flowchart**: Work through every check in order from top to bottom. Do not skip ahead. Most failures are caught by Check 1, 2, or 3. If you reach Check 6 without a resolution, activate the rollback procedure (see `GITHUB_PAGES_ROLLBACK_PROCEDURES.md`).

**Estimated time**: 5-10 minutes per check. Most issues resolve in one check.

---

## Before You Start: Locate the Actual Error

Before running any checks, get the raw error message. Blind troubleshooting without the error wastes time.

**Step 0 — Read the build log**:

1. Go to your GitHub repository
2. Click the **Actions** tab (top navigation)
3. Click the most recent workflow run (the one with the red X)
4. Click the failing job name (typically "build" or "deploy" or "pages build and deployment")
5. Expand each step by clicking the triangle next to the step name
6. Look for red text, lines beginning with `Error:`, `Fatal:`, `Gem::`, or `Liquid Exception`
7. Copy the exact error message

Keep that error message visible while working through the checks below. Each check includes the exact error strings it resolves.

---

## Check 1 — Did you push your latest changes?

**Catches**: 25-30% of "why isn't it deploying" cases.

**What to run**:
```bash
git status
git log --oneline origin/main..HEAD
```

**Interpreting results**:

If `git status` shows "Your branch is ahead of 'origin/main' by N commits":
- You have commits that have not been pushed
- Run: `git push origin main`
- Wait 60-90 seconds for Actions to trigger
- Reload the Actions tab — a new workflow run should appear

If `git status` shows "nothing to commit, working tree clean" AND `git log` shows no output:
- Your code IS pushed and the failure is genuine
- Continue to Check 2

If `git status` shows uncommitted changes (modified files, untracked files):
- Stage and commit those changes first
- Then push and wait for the new build

**Common pattern**: You created `_layouts/module.html` locally, tested it, it worked — but forgot to `git add` and `git commit` before pushing. The remote build has no knowledge of files you created locally unless they are committed and pushed.

**After pushing**:
1. Actions tab shows the new run triggered automatically (usually within 30 seconds of push)
2. Click the new run and watch it progress
3. If it turns green, you are done — skip remaining checks
4. If it turns red again, read the new error message and continue to Check 2

---

## Check 2 — What does the build log say? (Error keyword search)

**Catches**: Build failures due to config errors, missing files, syntax problems, missing gems.

**Where to look**: Actions tab > latest failed run > build job > expand all steps.

**Search the log for these keywords** (Ctrl+F in the browser):

### Error keyword: `Layout 'module' does not exist`

**Meaning**: `docs/_layouts/module.html` is either missing, not committed, or committed to the wrong path.

**Fix**:
```bash
# Confirm file exists
ls projects/career-training/docs/_layouts/module.html

# If missing, create it (see GITHUB_PAGES_REMEDIATION_RUNBOOK.md Fix 1)

# If it exists locally but wasn't committed
git add projects/career-training/docs/_layouts/module.html
git commit -m "fix: add missing module layout"
git push origin main
```

---

### Error keyword: `Could not find gem 'jekyll-remote-theme'`

**Meaning**: `jekyll-remote-theme` is listed in `_config.yml` plugins but GitHub Pages cannot locate it. This is unusual because GitHub Pages supports `jekyll-remote-theme` natively — but can happen if a `Gemfile` is present with conflicting dependencies.

**Fix — check for a Gemfile conflict**:
```bash
cat projects/career-training/docs/Gemfile 2>/dev/null || echo "No Gemfile present"
```

If a `Gemfile` exists with a restrictive `source` or missing `gem 'jekyll-remote-theme'`:

Option A (simplest): Delete the Gemfile and let GitHub Pages manage dependencies:
```bash
rm projects/career-training/docs/Gemfile
rm projects/career-training/docs/Gemfile.lock 2>/dev/null
git add -u projects/career-training/docs/
git commit -m "fix: remove Gemfile and let GitHub Pages manage deps"
git push origin main
```

Option B: Add the gem to the Gemfile:
```ruby
# In docs/Gemfile, add:
gem "jekyll-remote-theme"
```
Then `bundle install` locally to update `Gemfile.lock`, commit both, push.

---

### Error keyword: `remote: Theme not found`

**Meaning**: The `remote_theme` value in `_config.yml` is incorrect. GitHub Pages tried to load `just-the-docs/just-the-docs` from GitHub but could not find it.

**Verify the theme repository exists**:
Open `https://github.com/just-the-docs/just-the-docs` in a browser. If it exists, the theme name is correct.

**Fix — check for typos in config**:
```bash
grep "remote_theme" projects/career-training/docs/_config.yml
```

Expected: `remote_theme: just-the-docs/just-the-docs`

Common typos that break this:
- `remote_theme: just-the-docs` (missing the second part)
- `remote_theme: just_the_docs/just_the_docs` (underscores instead of hyphens)
- `theme: just-the-docs/just-the-docs` (wrong key — should be `remote_theme:`)

Correct the typo, commit, push.

---

### Error keyword: `Liquid Exception` or `Liquid::SyntaxError`

**Meaning**: A Markdown or HTML file contains malformed Liquid template syntax (unclosed `{% %}` block, undefined variable, mismatched tag).

**The log will say which file**: e.g., `Liquid Exception: docs/modules/05-civil-engineering.md` — look for the filename in the error.

**Fix**:
1. Open the file named in the error
2. Search for `{%` and `{{` — confirm every opening tag has a matching close
3. Common culprits: a `{% if %}` without `{% endif %}`, a `{{ }}` with extra curly braces
4. Fix, commit, push

For module files that should not contain Liquid syntax (pure Markdown content): the most likely cause is a code block with curly braces that Jekyll is trying to parse. Wrap code blocks in `{% raw %}...{% endraw %}` tags or escape with backticks.

---

### Error keyword: `YAML Exception` or `SyntaxError in frontmatter`

**Meaning**: A file's YAML frontmatter has a syntax error.

**The log will say which file**: e.g., `YAML Exception reading docs/modules/module-29.md`

**Common YAML frontmatter errors**:
- Unquoted strings containing colons: `title: Module 29: Advanced Topics` → should be `title: "Module 29: Advanced Topics"`
- Inconsistent indentation in multi-value fields
- Tab characters instead of spaces in YAML blocks

**Fix**:
```bash
# Open the file named in the error and check its frontmatter
head -20 projects/career-training/docs/modules/module-29.md
```

Fix the YAML, commit, push.

---

### Error keyword: `404: Not Found` (during theme loading)

**Meaning**: GitHub Pages is trying to load a file from the remote theme repository and getting a 404. Usually caused by referencing a theme file or hook that doesn't exist in Just the Docs.

**Common cause**: A `_includes` or `_layouts` file tries to include a Just the Docs template that has moved or been renamed in a newer version.

**Fix**: Check the Just the Docs changelog at `https://github.com/just-the-docs/just-the-docs/releases` for breaking changes. The `remote_theme:` key can pin to a specific release:

```yaml
remote_theme: just-the-docs/just-the-docs@v0.10.0
```

Add the `@version` suffix to pin to a known-good release. Use the latest stable version listed in their releases.

---

### Error keyword: `Permission denied` or `403`

**Meaning**: GitHub Actions does not have write permission to deploy to GitHub Pages.

**Fix — Check repository permissions**:
1. Go to repository Settings > Actions > General
2. Under "Workflow permissions", confirm "Read and write permissions" is selected
3. Also check Settings > Pages to confirm the source branch is set correctly

If the repository is private: GitHub Pages for private repos requires a GitHub Pro, Team, or Enterprise plan. If on the free plan, the repository must be public for GitHub Pages to work.

---

## Check 3 — GitHub Pages Settings: is the source branch correct?

**Catches**: Deployment not triggering, wrong branch, wrong folder.

**Scenario**: Build log shows no errors — the Jekyll build succeeds — but the site is still not live or shows an old version.

**Steps**:

1. Go to your repository on GitHub
2. Click **Settings** (top right tab)
3. Click **Pages** (left sidebar, under "Code and automation")
4. Under "Build and deployment", confirm:
   - Source: **Deploy from a branch** (not "GitHub Actions" unless you have a custom workflow)
   - Branch: **main** (or whatever your primary branch is)
   - Folder: **/docs** (not `/root` and not `/(root)`)
5. If these are wrong, correct them and click Save
6. If these are correct and still not deploying: look for a yellow "Your site is being built" banner or a recent deployment in the deployments list below the Settings panel

**Common wrong settings**:
- Folder set to `/(root)` instead of `/docs` — deploys the whole repo, fails because `_config.yml` is not at root
- Branch set to `master` but you're pushing to `main` (or vice versa)
- Source set to "GitHub Actions" but you don't have a `.github/workflows/pages.yml` file

**If source is "GitHub Actions" and you don't have a workflow file**:

Switch source back to "Deploy from a branch" and select `/docs`. This uses GitHub Pages' managed build (no workflow file needed).

Alternatively, create a minimal workflow file. But "Deploy from a branch" with `/docs` is simpler for a standard Jekyll site.

**Custom domain issues**: If you have a custom domain configured under Settings > Pages and you're getting DNS errors or redirect loops, temporarily remove the custom domain and test with the default `yourusername.github.io/repo-name` URL. This isolates whether the problem is Jekyll/build or DNS.

---

## Check 4 — Ruby version mismatch between local and GitHub Actions

**Catches**: Gems that install successfully locally but fail in the cloud build.

**Scenario**: Local build works. Cloud build fails with `Gem::InstallError`, `Could not find compatible versions`, or `LoadError`.

**Background**: GitHub Pages runs a specific Ruby version. As of mid-2026, GitHub Pages uses Ruby 3.1.x for its managed build. If your local Ruby is 3.3.x, some gems may behave differently.

**Check your local Ruby version**:
```bash
ruby --version
```

**Check what GitHub Pages is using**: Visit `https://pages.github.com/versions/` — it lists exact Ruby and gem versions.

**Fix A (no Gemfile — simplest)**: If you don't have a `Gemfile` in `docs/`, you're using GitHub Pages' managed build. There is no version mismatch to fix. Skip to Check 5.

**Fix B (have a Gemfile)**: Pin the Ruby version in your GitHub Actions workflow file. If you have a `.github/workflows/pages.yml`:

```yaml
# In .github/workflows/pages.yml, find the setup-ruby step and add:
- uses: ruby/setup-ruby@v1
  with:
    ruby-version: '3.1'   # match GitHub Pages' version
    bundler-cache: true
```

**Fix C (Gemfile.lock has wrong platform gems)**: If `Gemfile.lock` was generated on macOS or Windows, it may contain platform-specific gems that fail on Linux (GitHub Actions runs Ubuntu).

```bash
cd projects/career-training/docs
bundle lock --add-platform x86_64-linux
git add Gemfile.lock
git commit -m "fix: add linux platform to Gemfile.lock for GitHub Actions"
git push origin main
```

---

## Check 5 — Gemfile.lock is outdated or missing

**Catches**: Gem resolution failures, "bundler could not find compatible versions".

**Background**: `Gemfile.lock` pins exact gem versions. If it's missing or stale, Bundler re-resolves all dependencies at build time. This can produce version conflicts between gems that were compatible months ago but have since released incompatible versions.

**Scenario**: Build fails with messages like `Bundler could not find compatible versions for gem 'jekyll'` or `An error occurred while installing XYZ`.

**Fix — regenerate Gemfile.lock locally**:

```bash
cd projects/career-training/docs
# Delete the stale lock file
rm Gemfile.lock

# Regenerate with current compatible versions
bundle install

# Commit the new lock file
git add Gemfile.lock
git commit -m "fix: regenerate Gemfile.lock with compatible gem versions"
git push origin main
```

**If you don't have a `Gemfile` at all**: GitHub Pages' managed build does not use `Gemfile.lock`. This check is not relevant. Skip to Check 6.

**If `bundle install` fails locally**: The failure message will point to the incompatible gem. Search that gem's GitHub issues for "jekyll compatibility" — often a newer gem version requires a Jekyll version that conflicts with `github-pages` gem constraints.

The safest Gemfile for GitHub Pages managed builds:
```ruby
source "https://rubygems.org"

gem "github-pages", group: :jekyll_plugins
gem "jekyll-remote-theme"
```

This defers almost all versioning to the `github-pages` gem, which GitHub Pages maintains to be compatible with its own build environment.

---

## Check 6 — Repository access and Pages plan tier

**Catches**: Pages not available at all, or access restricted by plan.

**Check your plan**:
1. In GitHub, click your avatar > Settings > Billing & plans
2. Note your current plan (Free, Pro, Team, Enterprise)

**Free plan**:
- GitHub Pages works for PUBLIC repositories
- GitHub Pages does NOT work for private repositories on the free plan
- If your repo is private and you're on the free plan: either make the repo public, or upgrade to GitHub Pro ($4/month)

**If repository is public but Pages still won't activate**:
- Go to repository Settings > Pages
- If you see "GitHub Pages is disabled" with no option to enable it: wait 5 minutes and refresh — there is occasionally a propagation delay after a new repository is created or made public
- If you see "GitHub Pages is not available for this repository": contact GitHub support

**Check repository visibility**:
```bash
# From GitHub CLI (if installed):
gh repo view --json visibility -q '.visibility'
```
Expected: `PUBLIC`. If `PRIVATE`, make the repository public via Settings > General > Danger Zone > "Change repository visibility".

---

## Escalation Path: All 6 Checks Pass, Build Still Fails

If you have worked through all 6 checks and the build continues to fail, you have two options:

**Option 1: GitHub Pages support ticket**

1. Go to [support.github.com](https://support.github.com)
2. Submit a ticket: "Jekyll GitHub Pages build failing after successful local build"
3. Include: the repository URL, the exact error from the Actions log, and the Ruby/Jekyll versions you are using

Response time on the free plan: 2-7 business days.

**Option 2: Activate rollback to Netlify or Vercel**

If you need the site live within hours, do not wait for support. See `GITHUB_PAGES_ROLLBACK_PROCEDURES.md` — Netlify deployment takes 30 minutes and is high-confidence.

---

## Quick Reference — Error Message to Check Mapping

| Error message | Go to |
|---------------|-------|
| (no push happened) | Check 1 |
| `Layout 'module' does not exist` | Check 2 — "Layout" |
| `Could not find gem 'jekyll-remote-theme'` | Check 2 — "gem not found" |
| `remote: Theme not found` | Check 2 — "Theme not found" |
| `Liquid Exception` | Check 2 — "Liquid" |
| `YAML Exception` | Check 2 — "YAML" |
| `404: Not Found` (theme loading) | Check 2 — "404" |
| `Permission denied` / `403` | Check 2 — "Permission" |
| Site not live despite green build | Check 3 |
| `Gem::InstallError` / version conflict | Check 4 |
| `Bundler could not find compatible versions` | Check 5 |
| Pages not available at all | Check 6 |
| None of the above | Escalation path |
