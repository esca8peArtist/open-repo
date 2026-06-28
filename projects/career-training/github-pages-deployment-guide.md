---
title: "GitHub Pages Deployment Guide — Construction Career Training"
created: 2026-06-28
status: production-ready
applies_to: Phase 1 GitHub Pages deployment
---

# GitHub Pages Deployment Guide

This guide covers the full deployment sequence for the Construction Career Training curriculum to GitHub Pages, starting from a ready `/docs` directory. It assumes your repository already contains the 33-module content, the `/docs` directory structure, and a `_config.yml`. Your job is to push and verify.

---

## Part 1: Pre-Push Verification (15 minutes)

Before touching GitHub settings, confirm the local state is sound.

### 1.1 Verify the /docs directory is complete

```bash
ls projects/career-training/docs/
# Expected: _config.yml  _layouts/  _includes/  index.md  modules/  navigation/  case-studies/  resources/  instructor-guide/  about/  assets/
```

Confirm `_config.yml` exists and contains at minimum:

```yaml
title: Construction Career Training Curriculum
description: Production-ready training for GCs, PMs, and specialty contractors
theme: jekyll-theme-minimal
markdown: kramdown
```

If `baseurl` and `url` are not yet set, add them now (before the first push, not after):

```yaml
baseurl: "/your-repo-name"    # omit if using a custom domain pointing to root
url: "https://yourusername.github.io"
```

Getting `baseurl` wrong is the single most common cause of broken asset links after first deploy. Set it once before pushing.

### 1.2 Check for YAML front matter on key files

Every file in `/docs` that Jekyll should render needs front matter. At minimum, `index.md` must have:

```yaml
---
layout: default
title: Home
---
```

Files without front matter are served as raw Markdown by GitHub Pages, not rendered through the theme. If you see unstyled pages after deploy, missing front matter is usually why.

### 1.3 Run a local Jekyll build (optional but recommended)

If Ruby is available locally:

```bash
cd projects/career-training/docs
bundle install
bundle exec jekyll serve --baseurl ""
# Open http://localhost:4000 and click through all three learning paths
```

If Ruby is not available, skip to Part 2 and rely on the GitHub Actions build log for error detection.

---

## Part 2: Enable GitHub Pages (10 minutes)

### 2.1 Push your current state to GitHub

```bash
git add projects/career-training/docs/
git commit -m "docs(career-training): Phase 1 /docs directory ready for GitHub Pages"
git push origin master
```

### 2.2 Configure Pages in repository settings

1. Navigate to your repository on GitHub.
2. Go to **Settings** → **Pages** (left sidebar, under "Code and automation").
3. Under **Source**, select:
   - Branch: `master` (or `main`, whichever is your primary)
   - Folder: `/docs`
4. Click **Save**.
5. Wait 60–90 seconds. GitHub will display a banner: "Your site is published at `https://yourusername.github.io/repo-name/`"

### 2.3 Verify the build succeeded

Go to **Actions** tab → find the workflow named "pages build and deployment." If it is green, the build succeeded. If it is red, click into it and read the build log — the error message is usually precise and points directly to the failing file.

---

## Part 3: Common Failure Modes and Fixes

### Failure 1: Bundler version mismatch / Ruby version incompatibility

**Symptom:** GitHub Actions build fails with an error like:

```
Bundler could not find compatible versions for gem "jekyll"
Your Ruby version is X.Y.Z, but your Gemfile specified ~> A.B
```

**Root cause:** The `Gemfile` in `/docs` pins a gem version that conflicts with the Ruby version GitHub Pages uses (currently Ruby 3.1.x). Jekyll themes that pin to older versions cause this.

**Fix procedure:**

1. Update `/docs/Gemfile` to use the `github-pages` gem instead of pinning Jekyll directly:

```ruby
source "https://rubygems.org"
gem "github-pages", group: :jekyll_plugins
```

2. Delete `Gemfile.lock` if it exists (stale lock files are the second most common cause):

```bash
rm projects/career-training/docs/Gemfile.lock
```

3. Commit and push:

```bash
git add projects/career-training/docs/Gemfile
git rm --cached projects/career-training/docs/Gemfile.lock 2>/dev/null || true
git commit -m "fix(docs): use github-pages gem; remove stale Gemfile.lock"
git push origin master
```

4. Watch the Actions build. It should now resolve versions against GitHub Pages' supported set.

**Reference:** GitHub maintains a [dependency versions page](https://pages.github.com/versions/) listing exactly which gem versions are supported. If you need a specific theme version, check there first.

---

### Failure 2: YAML parsing errors in _config.yml

**Symptom:** Build fails with:

```
Error reading file /docs/_config.yml: (<unknown>): found character that cannot start any token
```
or:
```
YAML Exception reading _config.yml: mapping values are not allowed here
```

**Root cause:** YAML is whitespace-sensitive. Common errors: tabs instead of spaces, a colon inside an unquoted value, incorrect list indentation.

**Fix procedure:**

1. Validate the file before pushing using an online YAML linter (yamllint.com) or locally:

```bash
python3 -c "import yaml; yaml.safe_load(open('projects/career-training/docs/_config.yml'))" && echo "YAML valid"
```

2. Common patterns that cause failures:

```yaml
# WRONG — tab character before "description"
title: My Site
	description: Bad indentation

# WRONG — unquoted colon in value
tagline: Construction: The Career

# RIGHT
tagline: "Construction: The Career"
```

3. After fixing, commit and push. The Jekyll build will rerun automatically within 30 seconds of the push.

---

### Failure 3: Image asset 404s

**Symptom:** Site loads, theme renders, but images display as broken icons. Browser console shows `GET https://yourusername.github.io/images/diagram.png 404`.

**Root cause:** Markdown image paths do not account for the `baseurl`. An image referenced as `![alt](/images/diagram.png)` resolves to the root of the domain, not to `/repo-name/images/diagram.png`.

**Fix procedure:**

Option A — Use relative paths from the file's location:

```markdown
<!-- In /docs/modules/01-foundations.md, image is at /docs/assets/images/diagram.png -->
![Diagram](../assets/images/diagram.png)
```

Option B — Use the Jekyll `relative_url` filter in HTML (works reliably across all baseurl configurations):

```html
<img src="{{ '/assets/images/diagram.png' | relative_url }}" alt="Diagram">
```

Option C — If all images are in `/docs/assets/images/`, verify that directory exists and contains the files:

```bash
ls projects/career-training/docs/assets/images/
```

If the directory is empty or missing, create it and add a `.gitkeep`:

```bash
mkdir -p projects/career-training/docs/assets/images
touch projects/career-training/docs/assets/images/.gitkeep
git add projects/career-training/docs/assets/images/.gitkeep
git commit -m "fix(docs): create assets/images directory"
```

**Note for this curriculum:** The current Phase 1 content is primarily text-based with no images in the modules. If images are added later, use the `relative_url` filter (Option B) to avoid this failure mode entirely.

---

### Failure 4: DNS CNAME propagation delay (custom domain)

**Symptom:** Custom domain is configured in GitHub Pages settings, but visiting the domain shows a "Site not found" or DNS error. The `github.io` URL works fine.

**Root cause:** DNS changes propagate across global DNS servers over 24–48 hours. This is not a GitHub Pages bug; it is a DNS infrastructure reality.

**Fix procedure:**

1. Confirm the DNS record is correctly set at your registrar:
   - For apex domain (`yoursite.com`): Add four A records pointing to GitHub's IPs:
     ```
     185.199.108.153
     185.199.109.153
     185.199.110.153
     185.199.111.153
     ```
   - For `www` subdomain: Add a CNAME record pointing to `yourusername.github.io`

2. Check current propagation status (does not require waiting):

```bash
dig yoursite.com +noall +answer
# Should show GitHub's IPs if propagation is complete
```

Or use the online tool at `dnschecker.org` to see propagation status across regions.

3. While waiting, use the `github.io` URL to verify content is correct. Do not change GitHub Pages settings during propagation — it resets the HTTPS certificate provisioning timer.

4. HTTPS certificate: After DNS propagates, GitHub automatically provisions a Let's Encrypt certificate. This takes an additional 5–30 minutes after DNS resolves. During this window, you may see an HTTPS error; this resolves on its own. Do not click "Enforce HTTPS" until the certificate shows as "Active" in Pages settings.

5. If propagation exceeds 72 hours, the most common cause is a conflicting DNS record (old A record, conflicting CNAME). Check for and delete any pre-existing records pointing to your domain.

---

### Failure 5: GitHub Actions workflow failures

**Symptom:** The build workflow in the Actions tab shows red. Error types vary.

**Sub-case A: Permission denied / workflow not running**

GitHub Pages workflows require specific repository permissions. Go to **Settings** → **Actions** → **General** → **Workflow permissions** and ensure "Read and write permissions" is selected.

**Sub-case B: Theme not found / unsupported theme**

```
Dependency Error: Yikes! It looks like you don't have jekyll-theme-minimal or one of its dependencies installed.
```

GitHub Pages only supports a specific set of themes natively. The [supported themes list](https://pages.github.com/themes/) includes `jekyll-theme-minimal`, `jekyll-theme-cayman`, `minima`, and others. If `_config.yml` references a theme not on this list, the build will fail.

Fix: Either switch to a supported theme, or add the theme as a gem in your `Gemfile`:

```ruby
gem "just-the-docs"  # example of a non-default theme that still works via Gemfile
```

**Sub-case C: Build timeout**

GitHub Pages builds time out at 10 minutes. With 33 modules, this is unlikely to be an issue, but if the docs directory grows significantly:

- Ensure no large binary files (PDFs, images >1MB) are in `/docs/`. Move binaries to GitHub Releases or a CDN.
- Check that `_config.yml` excludes unnecessary directories: `exclude: [node_modules, vendor]`

**Sub-case D: Liquid template errors**

```
Liquid Exception: undefined method for nil:NilClass in _layouts/default.html
```

Cause: A Liquid template references a variable that does not exist in the page's front matter. Fix: Add the missing variable to the page's front matter, or add a conditional in the layout:

```liquid
{% if page.title %}{{ page.title }}{% else %}{{ site.title }}{% endif %}
```

---

## Part 4: Post-Deploy Testing Checklist

Run through this checklist immediately after the build shows green. This covers the scenarios most likely to have silently broken during deploy.

### 4.1 Navigation and structure

- [ ] Homepage loads at the correct URL (both `github.io` URL and custom domain if configured)
- [ ] All three learning path links on homepage resolve (Industrial GC, Residential GC, Specialty Sub)
- [ ] Navigation sidebar or menu (if using a theme with one) shows all major sections
- [ ] `quick-start.md` page loads and links to the three paths

### 4.2 Module loading

Spot-check a sample across the 33 modules — check at least the first, last, and a middle module:

```bash
# Example URLs to verify (adjust for your repo name / domain)
https://yourusername.github.io/career-training/modules/01-foundations-contracts-estimating
https://yourusername.github.io/career-training/modules/17-construction-technology-software
https://yourusername.github.io/career-training/modules/33-advanced-pm
```

- [ ] Modules render with theme (not as raw Markdown)
- [ ] Headings are formatted correctly (H1 is prominent, H2/H3 hierarchical)
- [ ] Code blocks (if any) render with monospace font
- [ ] Long modules do not cut off mid-content

### 4.3 Links

- [ ] Cross-module links (e.g., "See Module 13 for lien rights") resolve correctly
- [ ] External links (CSLB, Cal/OSHA, GitHub docs) open to the right destinations
- [ ] Navigation "next module" or breadcrumb links (if implemented) work in both directions

Quick automated check using a broken-link scanner (run locally or use a free online service):

```bash
# If htmlproofer is available via bundler:
bundle exec htmlproofer docs/ --disable-external --allow-hash-href
```

Or use the free online tool at `deadlinkchecker.com` with your published URL.

### 4.4 Images and assets

- [ ] If any images exist in `/docs/assets/images/`, they render (no broken icon)
- [ ] CSS theme is applied (not plain unstyled HTML)
- [ ] Favicon (if added) shows in browser tab

### 4.5 Mobile responsiveness

Open the site on a mobile device or use Chrome DevTools (F12 → toggle device toolbar):

- [ ] Homepage readable on 375px width (iPhone SE)
- [ ] Module text wraps correctly; not clipped or overflowing
- [ ] Navigation accessible on mobile (hamburger menu or scrollable sidebar)
- [ ] Tables (if any) scroll horizontally rather than breaking layout

### 4.6 Performance

- [ ] Homepage loads in under 3 seconds on a standard connection
- [ ] Individual module pages load in under 2 seconds
- [ ] No console errors in browser developer tools

If load time is slow, the most common cause is uncompressed images. Use `imageoptim` or `squoosh.app` to compress any images below 100KB each.

---

## Part 5: After Successful Deploy

Once the testing checklist is clear:

1. Create a GitHub release tag to mark Phase 1 as stable:

```bash
git tag -a v1.0.0 -m "Phase 1 launch: 33 modules, 3 learning paths, GitHub Pages"
git push origin v1.0.0
```

2. Copy the live URL and confirm it in the deployment plan for distribution outreach.

3. Submit the sitemap to Google Search Console. The Jekyll `jekyll-sitemap` plugin generates it automatically at `/sitemap.xml`. Go to [search.google.com/search-console](https://search.google.com/search-console), add the property, and submit `https://yoursite.com/sitemap.xml`.

4. If anything broke during this deploy, consult the troubleshooting decision tree (`troubleshooting-decision-tree.md`) for a structured diagnostic path.
