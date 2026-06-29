---
title: "Phase 1 GitHub Pages Deployment Audit Checklist"
project: career-training
phase: "1"
created: 2026-06-29
status: pre-push-audit
estimated-time: 15-20 minutes
---

# Phase 1 GitHub Pages Deployment Audit Checklist

**Purpose**: Mechanistic pre-push audit to catch the ~80% of common GitHub Pages failure modes before the first `git push`. Run all 18 checks. Document every failure in the Remediation Section. Do not push until all Critical Failure Criteria are clear or remediated.

**Estimated time**: 15-20 minutes if no failures. Allow 30-60 minutes if remediations are needed.

**Commands below assume your working directory is the repo root** (the directory containing `projects/career-training/`). If your repo root IS `career-training/`, drop `projects/career-training/` from all paths.

---

## Part 1: Jekyll Configuration

### Check 1 — baseurl value is correct for your deployment target

**What to run**:
```bash
grep "baseurl:" projects/career-training/docs/_config.yml
```

**Current state** (as of audit creation): `baseurl: ""` with a comment. This is correct IF you are using a custom domain (`constructiontrainingpath.com`) that points to the root of the site. It is WRONG if you are deploying to a GitHub Pages subdirectory (e.g., `yourusername.github.io/career-training`).

**Decision matrix**:
- Custom domain (`constructiontrainingpath.com`) pointing to repo root → `baseurl: ""`
- GitHub Pages default subdomain, repo name is `career-training` → `baseurl: "/career-training"`
- GitHub Pages default subdomain, repo name is something else → `baseurl: "/your-actual-repo-name"`

**Expected outcome**: baseurl value matches the path after your domain in the final URL. A mismatched baseurl breaks all CSS, JS, and internal navigation links — the single most common first-deploy failure.

- [ ] PASS: baseurl value confirmed correct for planned deployment target
- Actual value found: `___________________________`
- Planned URL: `___________________________`

---

### Check 2 — Plugins list is complete and includes jekyll-remote-theme

**What to run**:
```bash
grep -A6 "^plugins:" projects/career-training/docs/_config.yml
```

**Current state**: `_config.yml` lists `jekyll-feed`, `jekyll-sitemap`, `jekyll-seo-tag`. The site uses `remote_theme: just-the-docs/just-the-docs`, which requires `jekyll-remote-theme` to be in the plugins list. Without it, GitHub Pages will fall back to a default theme (no navigation, no search, broken layout).

**Expected outcome**: Plugin list includes at minimum:
```yaml
plugins:
  - jekyll-remote-theme
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
```

**Fix if missing**: Add `- jekyll-remote-theme` as the first entry in the plugins list in `_config.yml`.

- [ ] PASS: `jekyll-remote-theme` is present in the plugins list
- Plugins found: `___________________________`

---

### Check 3 — Permalink structure is valid and consistent

**What to run**:
```bash
grep "permalink\|nav_order\|nav_exclude" projects/career-training/docs/_config.yml
```

**Current state**: No site-wide `permalink` key is set in `_config.yml`. Jekyll defaults to `/:categories/:year/:month/:day/:title/` for posts and `/:path/` for pages. For a documentation site with no blog posts, the default page permalink behavior is acceptable.

**Expected outcome**: No permalink-related errors. The `index.md` has `permalink: /` explicitly set. Module files inherit from `defaults` scope. No typos in any permalink field in frontmatter.

**Spot-check**: Verify three random module files do not contain a `permalink:` line with a typo or absolute URL:
```bash
grep "permalink:" projects/career-training/docs/modules/01-foundations-contracts-estimating.md
grep "permalink:" projects/career-training/docs/modules/module-29.md
grep "permalink:" projects/career-training/docs/modules/28-marketing-business-development.md
```

Expected: no output (no permalink overrides) or valid relative paths.

- [ ] PASS: No invalid permalink values found in config or module frontmatter
- Any unexpected values found: `___________________________`

---

## Part 2: Module Assets and Frontmatter

### Check 4 — All 36 curriculum modules are in docs/modules/

**What to run**:
```bash
ls projects/career-training/docs/modules/*.md | grep -v "module-gap-analysis\|module-index" | wc -l
```

**Expected outcome**: `36`

**Note on count**: The `docs/modules/` directory contains 38 `.md` files. Two are administrative (not curriculum content): `module-gap-analysis.md` and `module-index.md`. The 36 curriculum modules are: 01-28 (numbered), module-29 through module-33 (named differently), and 34-36 (numbered). Modules 29-33 and 34-36 complete the 36-module set. Modules 37 and 38 (`37-industrial-commissioning.md`, `38-multi-family-commercial-fundamentals.md`) are in the top-level `projects/career-training/` directory, not in `docs/modules/`. Verify whether they should be included in the site.

**Check for the two extra modules**:
```bash
ls projects/career-training/37-*.md projects/career-training/38-*.md 2>/dev/null
```

If these files exist and should be on the site, they need to be moved to `docs/modules/` before pushing.

- [ ] PASS: Module count confirmed. Expected: 36 in docs/modules (or higher if 37/38 moved in)
- Actual count: `___________________________`
- Modules 37/38 status: `[ ] in docs/modules/` `[ ] intentionally excluded` `[ ] need to be moved`

---

### Check 5 — Module frontmatter is valid; layout defaults are wired correctly

**What to run**:
```bash
head -5 projects/career-training/docs/modules/01-foundations-contracts-estimating.md
head -5 projects/career-training/docs/modules/module-29.md
head -5 projects/career-training/docs/modules/34-residential-scheduling-practice.md
```

**Known state**: Module files do NOT have a `layout:` field in their individual frontmatter. This is intentional — `_config.yml` sets a default: `layout: module` for `path: "modules"`.

**Critical gap**: There is no `docs/_layouts/module.html` file. If this file does not exist, GitHub Pages will throw a build error ("Layout 'module' does not exist"). The Just the Docs remote theme provides a `default` layout but not a `module` layout unless you define it.

**Fix options (choose one before pushing)**:
1. Create `docs/_layouts/module.html` that extends Just the Docs default:
   ```html
   ---
   layout: default
   ---
   {{ content }}
   ```
2. Change the default in `_config.yml` from `layout: module` to `layout: default`.

**Check**:
```bash
ls projects/career-training/docs/_layouts/
```
Expected: directory exists and contains `module.html` (or you have applied Fix Option 2).

- [ ] PASS: `layout: module` references are satisfied (either layout file exists or default changed)
- Layout resolution chosen: `[ ] created _layouts/module.html` `[ ] changed default to layout: default`

---

### Check 6 — No broken image links

**What to run**:
```bash
grep -r "!\[" projects/career-training/docs/modules/ | wc -l
ls projects/career-training/docs/assets/images/ | wc -l
```

**Current state**: Module files contain zero image links (confirmed). The `docs/assets/images/` directory is empty or contains only supporting files.

**Expected outcome**: Image link count = 0 (or each image reference has a corresponding file in `docs/assets/images/`). If you have added images since audit creation, verify each one:
```bash
grep -r "!\[" projects/career-training/docs/modules/ | grep -oP '(?<=\()([^)]+)' | sort -u
```
Each path listed should exist as a file under `docs/`.

- [ ] PASS: Zero broken image links (0 image references in modules, or all referenced images confirmed present)
- Image links found: `___` — Images in assets/images/: `___`

---

### Check 7 — Internal links use correct path structure

**What to run**:
```bash
grep -r "\](/" projects/career-training/docs/modules/01-foundations-contracts-estimating.md | head -5
grep -r "\](.." projects/career-training/docs/modules/01-foundations-contracts-estimating.md | head -5
grep -r "site.baseurl" projects/career-training/docs/modules/ | head -5
```

**Expected behavior**: Cross-module links should use either `{{ site.baseurl }}/modules/filename/` (Liquid template syntax, works with any baseurl) or relative paths (`../modules/other-module`). Absolute paths like `/modules/01-...` work only when `baseurl` is empty. If baseurl is `/career-training`, absolute links break.

**Rule**: If you set `baseurl: "/career-training"`, all links starting with `/` in module files must be updated to use `{{ site.baseurl }}/`.

- [ ] PASS: Internal link format is consistent with the baseurl chosen in Check 1
- Link patterns found: `___________________________`

---

## Part 3: Analytics Pre-Configuration

### Check 8 — GA4 tracking snippet is embedded in head_custom.html

**What to run**:
```bash
cat projects/career-training/docs/_includes/head_custom.html 2>/dev/null || echo "FILE DOES NOT EXIST"
```

**Current state**: `docs/_includes/head_custom.html` does not exist yet. Per `PHASE_1_GOOGLE_ANALYTICS_SETUP.md`, this file must be created and must contain your GA4 Measurement ID (format: `G-XXXXXXXXXX`).

**This is a critical failure criterion if not resolved before push.** Every day of traffic before GA4 is live is permanently lost data.

**Fix**: Follow `PHASE_1_GOOGLE_ANALYTICS_SETUP.md` Part 1 completely. Create `docs/_includes/head_custom.html` with the GA4 Global Site Tag. The file must be committed to the repo.

**Verify after creating**:
```bash
grep "G-" projects/career-training/docs/_includes/head_custom.html
```
Expected: a line containing your GA4 Property ID in format `G-XXXXXXXXXX`.

- [ ] PASS: `head_custom.html` exists and contains a valid GA4 Property ID
- GA4 Property ID embedded: `G-___________`

---

### Check 9 — Event tracking tags are present (optional but strongly recommended)

**What to run**:
```bash
grep -i "gtag\|event" projects/career-training/docs/_includes/head_custom.html 2>/dev/null | head -10
```

**Expected**: GA4 Global Site Tag automatically tracks `page_view` events via Enhanced Measurement if left enabled during stream creation (Step 1.2 of `PHASE_1_GOOGLE_ANALYTICS_SETUP.md`). No custom event code is required for basic page_view tracking.

For custom events (module_complete, email_signup): these are wired via Kit's confirmation redirect page, not via manual gtag calls in the head. Verify Kit's thank-you redirect page URL is set to fire a conversion in GA4 (per `PHASE_1_GOOGLE_ANALYTICS_SETUP.md` Part 3).

- [ ] PASS: GA4 gtag snippet present, Enhanced Measurement enabled at stream level
- [ ] ACCEPTABLE: page_view tracking only for Phase 1 launch; custom events deferred to Phase 2
- Enhanced Measurement enabled in GA4 stream settings: `[ ] Yes` `[ ] Not confirmed`

---

### Check 10 — Analytics dashboard URL documented

**Fill in before pushing**:

GA4 Property URL (for post-launch daily check): `https://analytics.google.com/analytics/web/#/p/___________`

Where `___________` is your numeric GA4 Property ID (found in GA4 Admin > Property Settings > Property ID, NOT the G-XXXXXXXXXX Measurement ID — this is a different number).

Google Search Console URL: `https://search.google.com/search-console?resource_id=https%3A%2F%2F[your-domain]`

- [ ] PASS: Both URLs filled in above and bookmarked in browser before pushing

---

## Part 4: Email Signup Form Integration

### Check 11 — Kit signup page exists in docs/

**What to run**:
```bash
ls projects/career-training/docs/signup.md 2>/dev/null || echo "FILE DOES NOT EXIST"
```

**Current state**: `docs/signup.md` does not exist yet. Per `PHASE_1_KIT_COM_INTEGRATION_SETUP.md` Part 1, this file must be created before push. Without it, any module-level "Sign up for this path" link goes to a 404.

**Fix**: Follow `PHASE_1_KIT_COM_INTEGRATION_SETUP.md` Part 1.1 to create `docs/signup.md`. Embed Kit form embed codes for each learning path.

**Note on prerequisites**: The signup page requires Kit account created, forms created in Kit, and embed codes copied. If Kit account is not yet set up, complete `KIT_ACCOUNT_SETUP_CHECKLIST.md` Steps 1-5 first. If kit setup is deferred past launch, create a placeholder `signup.md` that says "Email signup coming soon — check back" to prevent 404s.

- [ ] PASS: `docs/signup.md` exists with at least a placeholder (form or "coming soon" message)
- Form embed status: `[ ] Live Kit forms embedded` `[ ] Placeholder "coming soon" page`

---

### Check 12 — Form submission destination is configured

**For live Kit forms**: Kit routes submissions to your Kit subscriber list automatically. No webhook configuration required on the free plan.

**Verify**:
1. In Kit dashboard, navigate to your form
2. Click Settings > Incentive > After subscribing
3. Confirm the redirect is set to either: a thank-you message (Kit default) or your custom `/signup-thank-you/` page

**For GA4 conversion tracking**: If using a redirect to `/signup-thank-you/`, confirm that page exists in `docs/`:
```bash
ls projects/career-training/docs/signup-thank-you* 2>/dev/null || echo "PAGE DOES NOT EXIST"
```

- [ ] PASS: Kit form submission destination is configured (redirect or thank-you message set in Kit)
- Post-submission behavior: `[ ] Kit default thank-you message` `[ ] Redirect to /signup-thank-you/` `[ ] Other: ___`

---

### Check 13 — Post-submission user experience is clear

**What to verify manually**: Open your Kit form preview (Kit dashboard > Forms > Preview). After submitting a test email address:
- Does a confirmation message appear? Text: `___________________________`
- Does a confirmation email arrive at the test address within 2 minutes? `[ ] Yes` `[ ] No`
- If redirect: does `/signup-thank-you/` render correctly? `[ ] Yes` `[ ] Not applicable`

**Free plan behavior**: Kit sends a double opt-in confirmation email by default. Subscribers are not active until they click the confirmation link. Test the full flow (submit > receive email > click confirm > appear in Kit subscriber list) before pushing.

- [ ] PASS: Post-submission UX tested end-to-end; confirmation email received; subscriber appears in Kit

---

## Part 5: Mobile Rendering Spot-Check

### Check 14 — Five modules tested on mobile (or Chrome DevTools)

**Method (no phone required)**:
1. Open `projects/career-training/docs/modules/01-foundations-contracts-estimating.md` in a local Jekyll serve session or in the live site after push
2. In Chrome: press F12 > click the phone/tablet icon (Toggle Device Toolbar) > select "iPhone 12 Pro" (390px width)
3. Test the following 5 modules: 01, 10, 17, 25, module-29

**Per-module checklist** (mark each):
- Module 01: `[ ] Text readable` `[ ] No horizontal scroll` `[ ] Code blocks scrollable` `[ ] Nav accessible`
- Module 10: `[ ] Text readable` `[ ] No horizontal scroll` `[ ] Code blocks scrollable` `[ ] Nav accessible`
- Module 17: `[ ] Text readable` `[ ] No horizontal scroll` `[ ] Code blocks scrollable` `[ ] Nav accessible`
- Module 25: `[ ] Text readable` `[ ] No horizontal scroll` `[ ] Code blocks scrollable` `[ ] Nav accessible`
- Module 29: `[ ] Text readable` `[ ] No horizontal scroll` `[ ] Code blocks scrollable` `[ ] Nav accessible`

**Just the Docs note**: The Just the Docs theme is responsive by default. If the remote theme loads correctly (Check 2 resolves), most mobile issues will not appear. The most likely mobile failure is long code blocks or tables that extend beyond 390px — these should scroll horizontally within their container, not cause the whole page to scroll.

- [ ] PASS: All 5 modules render acceptably on 390px viewport with no layout breaks

---

### Check 15 — Email signup form responsive on mobile

**What to test**: Open `docs/signup.md` (or the live `/signup/` page) in Chrome DevTools at 390px.

- [ ] Form input fields are full-width and tappable (not cut off at right edge)
- [ ] Submit button is visible and tappable
- [ ] "Powered by Kit" badge does not break layout
- [ ] If multiple path forms on one page, all forms render without overlap

- [ ] PASS: Signup form renders correctly at 390px
- [ ] SKIP: Signup page is placeholder "coming soon" (no form to test)

---

## Part 6: Build and Deployment Validation

### Check 16 — Jekyll build succeeds locally (if Ruby available)

**What to run** (only if Ruby 3.x and Bundler are installed locally):
```bash
cd projects/career-training/docs
bundle exec jekyll build 2>&1 | tail -20
```

If no local Ruby: skip this check and rely on Check 17 instead.

**Expected output**:
```
                    done in X.XXX seconds.
 Auto-regeneration: disabled. Use --watch to enable.
```
Zero lines beginning with `Error:` or `Fatal:`. Warnings (e.g., "No GitHub API authentication could be found") are acceptable.

**Common fatal errors at this stage**:
- `Layout 'module' does not exist` — Fix: create `_layouts/module.html` (see Check 5)
- `Liquid Exception` in a specific file — Fix: find the file, look for unclosed `{% %}` or `{{ }}` tags
- `jekyll-remote-theme` not found — Fix: add to Gemfile if running locally (GitHub Pages handles it automatically in cloud build)

- [ ] PASS: Local build exits cleanly with 0 errors
- [ ] SKIP: Ruby not available locally (proceeding to Check 17)
- Build output: `[ ] 0 errors` `[ ] N warnings` `[ ] N fatal errors (see Remediation)`

---

### Check 17 — GitHub Pages cloud build configuration is correct

**Verify before first push**:

1. Your repository has a `docs/` directory at the root (the GitHub Pages source folder)
2. In GitHub repository Settings > Pages, the Source is set to "Deploy from a branch" and the folder is `/docs`
3. The branch selected is `main` (or your primary branch name)

**Check for a Gemfile** (required if using plugins that need local builds; optional for GitHub Pages managed builds):
```bash
ls projects/career-training/docs/Gemfile 2>/dev/null || echo "NO GEMFILE"
```

**GitHub Pages managed build**: If no Gemfile is present, GitHub Pages runs its own build using the [github-pages gem](https://pages.github.com/versions/). The `jekyll-remote-theme` plugin is supported. The `just-the-docs` remote theme is supported. This is the simplest path — no Gemfile needed.

**Expected outcome**: No `_github_pages.yml` or GitHub Actions workflow is required for the standard managed build. GitHub handles it when you enable Pages in Settings.

- [ ] PASS: Repo Settings > Pages source confirmed as `/docs` on `main` (or will be set at push time)
- GitHub Pages source path: `[ ] /docs confirmed` `[ ] Will set at push time`
- Gemfile present: `[ ] Yes` `[ ] No (using GitHub Pages managed build — acceptable)`

---

## Part 7: Final Sign-Off

### Check 18 — All 17 checks above are PASS (or failures documented in Remediation below)

Review the checklist above. For every check marked PASS: the item is verified. For every check with a failure or SKIP: it must appear in the Remediation Section below with a resolution plan.

**Critical Failure Criteria — DO NOT PUSH if any are true**:
- [ ] Check 2 FAILED: `jekyll-remote-theme` missing from plugins list
- [ ] Check 5 FAILED: `_layouts/module.html` does not exist and config default not changed
- [ ] Check 8 FAILED: `docs/_includes/head_custom.html` does not exist (GA4 not embedded)
- [ ] Check 1 FAILED: baseurl is incorrect for planned deployment target
- [ ] Check 11 FAILED: `docs/signup.md` does not exist (even a placeholder)
- [ ] Check 4 FAILED: Fewer than 34 module files confirmed present in `docs/modules/`

If all Critical Failure Criteria boxes above are CLEAR (unchecked = not a blocker):

- [ ] APPROVED: All 18 checks PASS or non-critical failures are documented below. I authorize GitHub Pages deployment.

Authorized by: `___________________________`
UTC timestamp of authorization: `___________________________`
GitHub repository URL: `https://github.com/___________________________`
Planned push command: `git push origin main`

---

## Remediation Section

If any check FAILED, document here before pushing. Leave blank if all checks PASSED.

**Template** (copy for each failure):

---

**Check #___ failed**: [Brief description of what was expected vs. found]

Root cause: [Why this happened]

Remediation: [Exact fix to apply]

Status: `[ ] FIXED` `[ ] DEFERRED` `[ ] ACCEPTED RISK`

If DEFERRED or ACCEPTED RISK, explain why it is safe to push anyway:

---

### Known Pre-Existing Issues (as of audit creation, 2026-06-29)

The following are known gaps identified during audit creation. They are not surprises — document resolution here.

**Issue A — Check 8: head_custom.html does not exist**
Root cause: GA4 snippet creation deferred to pre-push step per `PHASE_1_GOOGLE_ANALYTICS_SETUP.md`.
Remediation: Follow `PHASE_1_GOOGLE_ANALYTICS_SETUP.md` Part 1.3. Create file, add snippet, commit.
Status: `[ ] FIXED` `[ ] DEFERRED`

**Issue B — Check 11: docs/signup.md does not exist**
Root cause: Kit account setup deferred to pre-push step per `PHASE_1_KIT_COM_INTEGRATION_SETUP.md`.
Remediation: Either complete Kit setup per `PHASE_1_KIT_COM_INTEGRATION_SETUP.md` Part 1.1, or create a placeholder signup page to prevent 404s.
Status: `[ ] FIXED (live forms)` `[ ] FIXED (placeholder)` `[ ] DEFERRED`

**Issue C — Check 5: No _layouts/module.html file**
Root cause: `_config.yml` defaults reference `layout: module` but no such layout file was created. Just the Docs provides `default` and `page` layouts, not `module`.
Remediation: Create `docs/_layouts/module.html` with a single line calling the default layout (see Check 5 fix). Or change config default to `layout: default`.
Status: `[ ] FIXED` `[ ] DEFERRED`

**Issue D — Check 2: jekyll-remote-theme not in plugins list**
Root cause: Plugin was omitted from initial `_config.yml`.
Remediation: Add `- jekyll-remote-theme` as first entry in plugins list.
Status: `[ ] FIXED` `[ ] DEFERRED`

**Issue E — Check 4: Modules 37 and 38 not in docs/modules/**
Root cause: `37-industrial-commissioning.md` and `38-multi-family-commercial-fundamentals.md` are in the root `career-training/` directory, not in `docs/modules/`. They will not appear on the GitHub Pages site unless moved.
Remediation: Move both files to `docs/modules/` and commit, OR accept that they are not part of Phase 1 site content.
Status: `[ ] MOVED TO docs/modules/` `[ ] INTENTIONALLY EXCLUDED FROM PHASE 1`
