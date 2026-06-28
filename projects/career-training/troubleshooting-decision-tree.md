---
title: "GitHub Pages Troubleshooting Decision Tree — Construction Career Training"
created: 2026-06-28
status: production-ready
applies_to: Phase 1 GitHub Pages deployment failure diagnosis
---

# Troubleshooting Decision Tree

Use this document when something is wrong with the GitHub Pages deployment and you need to diagnose it quickly. Start at Step 0 every time — the entry point matters.

---

## Step 0: Define the Symptom

Before diagnosing, be precise about what is broken. The decision tree branches differently depending on where in the process the failure occurred.

| Symptom | Go to |
|---------|-------|
| GitHub Actions build shows red (build failed before the site even deployed) | Section A |
| Build shows green but the site URL returns a 404 | Section B |
| Site loads but pages look wrong (unstyled, broken layout, missing content) | Section C |
| Site loads and looks right, but specific links or images are broken | Section D |
| Custom domain does not resolve | Section E |
| Site was working, now stopped working after a push | Section F |
| Site is slow or inaccessible intermittently | Section G |

---

## Section A: Build Fails (Red in GitHub Actions)

**Entry condition:** The "pages build and deployment" workflow in the Actions tab shows a red X.

### A1. Read the build log

Click the failed workflow run → click "build" → expand the failing step. The error will be in plain text. Match it below.

---

**Error: `cannot load such file -- bundler`**

Root cause: No `Gemfile` in `/docs/`, or GitHub Actions cannot find it.

Fix:
1. Confirm `Gemfile` exists at `projects/career-training/docs/Gemfile`
2. If missing, create it:
```ruby
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
```
3. Commit, push. Build reruns automatically.

---

**Error: `Bundler could not find compatible versions`**

Root cause: `Gemfile.lock` pins incompatible versions, or theme version conflicts with GitHub Pages Ruby.

Fix:
```bash
rm projects/career-training/docs/Gemfile.lock
# Replace Gemfile content with:
# gem "github-pages", group: :jekyll_plugins
git add -A && git commit -m "fix: remove Gemfile.lock, use github-pages gem" && git push
```

Decision point: Does the rebuild succeed? If yes, done. If no, continue to A2.

---

**Error: `YAML Exception` or `Psych::SyntaxError`**

Root cause: Malformed YAML in `_config.yml` or in a page's front matter.

Fix procedure:
1. Read the error — it names the file and line number.
2. Open that file. Look for:
   - Tab characters where spaces are required
   - Unquoted colons in values: `title: Foo: Bar` should be `title: "Foo: Bar"`
   - Inconsistent indentation in lists
3. Validate with:
```bash
python3 -c "import yaml; yaml.safe_load(open('projects/career-training/docs/_config.yml'))"
```
4. Fix and push. If the error is in a module file (not `_config.yml`), the same validation applies:
```bash
python3 -c "import yaml; yaml.safe_load(open('projects/career-training/docs/modules/01-foundations-contracts-estimating.md').read().split('---')[1])"
```

---

**Error: `Dependency Error: theme not found`**

Root cause: `_config.yml` references a theme that GitHub Pages does not support natively.

Fix options:
- Switch to a supported theme: `jekyll-theme-minimal`, `jekyll-theme-cayman`, `minima`
- Or keep the current theme but add it explicitly in `Gemfile` so bundler can fetch it
- List of natively supported themes: `https://pages.github.com/themes/`

---

**Error: `Liquid Exception` or `undefined method for nil`**

Root cause: A Liquid template references a page variable that does not exist.

Fix: Add the missing variable to the affected page's front matter, or make the template conditional:
```liquid
{% if page.description %}{{ page.description }}{% endif %}
```

---

**Error: `GitHub Pages: Unverified` or workflow permission error**

Root cause: Repository Actions permissions are set to read-only.

Fix: Settings → Actions → General → Workflow permissions → set to "Read and write permissions" → Save.

---

### A2. Build log shows no clear error but still fails

If the log ends mid-line or shows a timeout:

1. Check if any file in `/docs/` is extremely large (>5MB). Large files cause memory errors during build.
2. Check for binary files that should not be there (PDFs, videos).
3. Remove them: `git rm projects/career-training/docs/assets/large-file.pdf`

Roll back decision: If three successive push-fix cycles fail to resolve a build error, roll back to the last known working commit:
```bash
git revert HEAD~3..HEAD
git push origin master
```

---

## Section B: Build Succeeds but Site Returns 404

**Entry condition:** Actions tab shows green checkmark, but visiting the URL returns "404: There isn't a GitHub Pages site here."

### B1. Is GitHub Pages actually enabled?

Go to Settings → Pages. If you see "GitHub Pages is currently disabled," re-enable it:
- Source: Deploy from a branch
- Branch: master (or main)
- Folder: /docs
- Save

### B2. Is the URL correct?

The URL format is `https://yourusername.github.io/repository-name/` — note the trailing path. Visiting just `https://yourusername.github.io/` returns 404 if you do not have a `username.github.io` repository.

### B3. Is `index.md` present in `/docs/`?

GitHub Pages looks for `index.html` or `index.md` at the root of the source folder. If it is missing, you get a 404.

```bash
ls projects/career-training/docs/index.md
```

If missing, create it with at minimum:
```markdown
---
layout: default
title: Home
---
# Construction Career Training
```

### B4. Did the deployment actually complete?

After enabling Pages, there is a 1–5 minute propagation delay even after the build succeeds. Wait 5 minutes, then hard-refresh the browser (Ctrl+Shift+R) before concluding the site is broken.

---

## Section C: Site Loads but Looks Wrong

**Entry condition:** URL resolves, but pages are unstyled (plain HTML), broken layout, or missing navigation.

### C1. Unstyled HTML (no theme applied)

Most common cause: `index.md` or other pages lack front matter entirely. Jekyll only applies the theme layout to files that have a front matter block (even an empty one).

Fix: Add front matter to affected files:
```markdown
---
layout: default
title: Module 01 — Foundations
---
(content here)
```

### C2. Layout exists but sidebar/navigation is missing

Cause: The layout file references an include (`_includes/navigation.html`) that does not exist.

Fix: Create the missing include, or use a theme that provides navigation out of the box. The `just-the-docs` theme has built-in navigation. The `jekyll-theme-minimal` does not — it requires manual navigation in the layout.

### C3. baseurl is wrong — all asset paths are broken

Symptom: CSS and JS load (the page is styled) but navigation links go to the wrong paths, or internal links 404.

Diagnosis: In your browser developer tools, check what URL the broken CSS/JS is requesting. If it shows `/career-training/assets/` when the actual path is `/assets/`, the `baseurl` is set but assets aren't using `relative_url`.

Fix: In `_config.yml`, confirm `baseurl` matches your repository name exactly (case-sensitive). Then in all layout files, use `{{ site.baseurl }}` or the `relative_url` filter:
```html
<link rel="stylesheet" href="{{ '/assets/css/style.css' | relative_url }}">
```

---

## Section D: Specific Links or Images Broken

**Entry condition:** The site mostly works, but certain images show as broken icons, or specific links return 404.

### D1. Image 404s

Step 1: Open browser developer tools → Console. Note the full URL that returned 404.

Step 2: Compare that URL to the actual file path in your repository.

If the URL is missing the `baseurl` prefix (e.g., requests `/images/x.png` but file is at `/career-training/images/x.png`): fix the reference to use `relative_url` filter or a relative path.

If the file simply does not exist: add it.
```bash
ls projects/career-training/docs/assets/images/
# Verify the file is there with exact filename (case-sensitive on GitHub)
```

Note: GitHub is case-sensitive. `Diagram.PNG` and `diagram.png` are different files. Match case exactly.

### D2. Internal cross-module links return 404

Cause: Markdown link uses an absolute path that does not account for the baseurl, or the filename changed.

Example of broken pattern:
```markdown
See [Module 13](/docs/modules/13-construction-law-lien-rights-california.md)
```

Example of correct pattern for a Jekyll site (links should not include `.md` extension):
```markdown
See [Module 13](../modules/13-construction-law-lien-rights-california)
```

Or use absolute paths with baseurl in liquid:
```markdown
See [Module 13]({{ site.baseurl }}/modules/13-construction-law-lien-rights-california)
```

Quick check: Run an automated link scan against the live site:
```bash
# Using htmlproofer (requires Ruby)
bundle exec htmlproofer docs/ --disable-external
```

---

## Section E: Custom Domain Does Not Resolve

**Entry condition:** `github.io` URL works, but the custom domain shows a DNS error or "Site not found."

### E1. Check DNS propagation

```bash
dig yourdomain.com +short
# Should return: 185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153
```

If empty or returns wrong IPs: DNS change has not propagated yet. Wait 24–48 hours. Check at `dnschecker.org` to see propagation progress by region.

### E2. Check the CNAME file

GitHub Pages requires a `CNAME` file in the source directory containing your domain:

```bash
cat projects/career-training/docs/CNAME
# Should contain exactly: yourdomain.com
```

If this file is missing, GitHub Pages does not know to serve your domain. GitHub adds it automatically when you enter the domain in Settings → Pages, but verify it committed.

### E3. HTTPS "certificate not yet provisioned" error

After DNS propagates, certificate provisioning takes 5–30 additional minutes. The error message in the browser will be a certificate error, not a 404. This resolves automatically. Do not click "Enforce HTTPS" until the Pages settings screen shows the certificate as active.

---

## Section F: Site Broke After a Push

**Entry condition:** Site was working, you pushed new content, now it is broken.

### F1. Check the Actions log for the latest push

Did the build fail? If yes, return to Section A.

Did the build succeed but the site changed unexpectedly? The most recent commit changed something. Find it:

```bash
git log --oneline -5
git diff HEAD~1 HEAD -- projects/career-training/docs/
```

Identify the changed file. If it is `_config.yml`, a configuration change broke routing or baseurl. If it is a layout file, a template error is likely.

### F2. Roll back vs. fix forward

**Roll back when:**
- The error is not immediately obvious
- The site being down is blocking distribution or outreach (time-sensitive)
- Three diagnostic cycles have not identified the root cause

```bash
git revert HEAD
git push origin master
# Site returns to prior working state within 2 minutes of build completion
```

**Fix forward when:**
- The error message is clear (e.g., YAML syntax on line X)
- The fix is a one-line change
- You are early in the deployment process (no active users yet)

---

## Section G: Site is Slow or Intermittently Inaccessible

**Entry condition:** Site loads sometimes, or loads but takes 10+ seconds.

GitHub Pages has a global CDN and is generally very fast for static sites. Slowness almost always comes from content, not infrastructure.

### G1. Check for oversized assets

```bash
find projects/career-training/docs/assets -size +500k -type f
```

Any file over 500KB in `/assets/` will slow page loads. Compress images with `imageoptim` or `squoosh.app`. PDFs should be moved to GitHub Releases, not served from the Pages site directly.

### G2. GitHub Pages is experiencing an outage

Check `githubstatus.com`. If "GitHub Pages" shows a yellow or red status, this is GitHub's infrastructure issue, not yours. Wait it out. GitHub Pages outages typically resolve within 1–4 hours.

### G3. Rate limiting from rapid repeated builds

If you have been pushing many commits in quick succession, GitHub may throttle builds. GitHub Pages allows up to 10 builds per hour. Wait 10 minutes and push once with all changes consolidated.

---

## When to Escalate to GitHub Support

Self-service fixes cover 95% of GitHub Pages issues. Escalate to GitHub Support when:

1. **Domain verification failure:** You have added the correct DNS records, waited 72+ hours, and GitHub still shows "domain not verified." This requires GitHub support to investigate their verification system.

2. **Build succeeds but site does not update:** Build shows green, but the live site still shows old content after 30+ minutes. This indicates a CDN cache issue on GitHub's side.

3. **Repository-level Pages settings are missing:** The Settings → Pages section does not appear in your repository. This can happen on free-tier organizations with certain permission configurations.

4. **HTTPS certificate stuck in "pending" for more than 24 hours after DNS propagation confirmed complete.** This requires GitHub to re-trigger certificate issuance.

To contact GitHub Support: `support.github.com` → "GitHub Pages" category. Response time for free accounts is typically 24–72 hours. For time-sensitive launches, use the Netlify fallback from `fallback-distribution-protocol.md` while waiting.

---

## Quick Reference: Error Message to Root Cause

| Error Message (partial) | Root Cause | Section |
|------------------------|------------|---------|
| `cannot load such file -- bundler` | Missing Gemfile | A1 |
| `Bundler could not find compatible versions` | Gemfile.lock conflict | A1 |
| `YAML Exception` / `Psych::SyntaxError` | Bad YAML in config or front matter | A1 |
| `Dependency Error: theme not found` | Unsupported theme | A1 |
| `Liquid Exception: undefined method for nil` | Missing front matter variable | A1 |
| `404: There isn't a GitHub Pages site here` | Pages not enabled or index.md missing | B |
| Pages loads but completely unstyled | Missing front matter block | C1 |
| Navigation links go to wrong URLs | baseurl misconfigured | C3 |
| Image broken (404 in console) | Path does not account for baseurl | D1 |
| Internal link 404s | .md extension in link, or wrong path | D2 |
| `ERR_NAME_NOT_RESOLVED` on custom domain | DNS not propagated yet | E1 |
| Certificate error on custom domain | HTTPS cert still provisioning | E3 |
| Site broke after push | Recent commit introduced error | F |
| Site loads slowly | Oversized assets in /docs | G1 |
| Site intermittently down | GitHub Pages outage | G2 |
