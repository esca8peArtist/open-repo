---
title: "GitHub Pages Remediation Runbook — 4 Critical Fixes"
project: career-training
phase: "1"
created: 2026-06-29
status: execution-ready
estimated-time: 35-50 minutes total
---

# GitHub Pages Remediation Runbook

**Purpose**: Step-by-step remediation for the 4 critical failures identified in the Phase 1 GitHub Pages Deployment Audit (Item 50, Session 4563). Complete all 4 fixes in order before the first `git push`. Also covers the bonus directory reorganisation for modules 37-38.

**All paths assume your working directory is the repo root** (`/home/awank/dev/SuperClaude_Framework`). If your repo root IS `career-training/`, drop `projects/career-training/` from every path.

**Estimated total time**: 35-50 minutes if you have a GA4 Property and Kit account. Allow an extra 30-45 minutes if you need to create those accounts first.

**Order of operations**: Do these in sequence. Fix 1 and Fix 2 are pure config and can be done in under 5 minutes combined. Fix 3 (GA4) requires a Google Analytics account. Fix 4 (signup page) requires a Kit account or can be deferred with a placeholder. Bonus fix 5 is two file moves.

---

## Fix 1 — Create `docs/_layouts/module.html` (layout: module does not exist)

**Failure**: `_config.yml` sets `layout: module` as the default for all files under `docs/modules/`. No `docs/_layouts/module.html` exists. GitHub Pages will throw a fatal build error: `Layout 'module' does not exist`.

**Time to fix**: 3 minutes.

**Background**: Just the Docs (your remote theme) provides `default`, `page`, `home`, and `minimal` layouts. It does not provide a `module` layout — you have to create it. The simplest approach is a thin wrapper that calls Just the Docs' `default` layout, which gives you the full sidebar navigation, search, and responsive layout. You can add module-specific sections inside the wrapper later.

### Step 1.1 — Confirm the layouts directory exists

```bash
ls projects/career-training/docs/_layouts/
```

Expected: an empty directory listing (no files, no error). If the directory does not exist:

```bash
mkdir -p projects/career-training/docs/_layouts
```

### Step 1.2 — Create the layout file

Create `projects/career-training/docs/_layouts/module.html` with this exact content:

```html
---
layout: default
---

<div class="module-wrapper">

  {% if page.module %}
  <div class="module-meta">
    <span class="module-number">Module {{ page.module }}</span>
    {% if page.discipline %}
    <span class="module-disciplines">{{ page.discipline | join: " · " }}</span>
    {% endif %}
    {% if page.audience %}
    <span class="module-audience">Audience: {{ page.audience }}</span>
    {% endif %}
  </div>
  {% endif %}

  <div class="module-content">
    {{ content }}
  </div>

  {% if page.module %}
  <div class="module-footer">
    <hr />
    <p class="module-nav-hint">
      {% assign current_num = page.module | plus: 0 %}
      {% assign prev_num = current_num | minus: 1 %}
      {% assign next_num = current_num | plus: 1 %}
      <a href="{{ site.baseurl }}/modules/">← All Modules</a>
      &nbsp;&nbsp;|&nbsp;&nbsp;
      <a href="{{ site.baseurl }}/signup/">Get this path by email →</a>
    </p>
  </div>
  {% endif %}

</div>
```

**What this does**:
- Inherits all Just the Docs layout: sidebar, search, header, breadcrumbs, responsive CSS
- Adds a `module-meta` block that renders the module number, disciplines, and audience from frontmatter — if those fields are present
- Adds a footer with links back to the module index and the signup page
- If any of these fields are missing in a module's frontmatter, the corresponding block is simply omitted (no error)

### Step 1.3 — Verify the file was created

```bash
cat projects/career-training/docs/_layouts/module.html | head -5
```

Expected output: the `---` frontmatter delimiter followed by `layout: default`.

### Step 1.4 — Optional: test locally if Ruby is available

```bash
cd projects/career-training/docs && bundle exec jekyll build 2>&1 | grep -i "layout\|error\|fatal" | head -20
```

Expected: zero lines containing `Layout 'module' does not exist`. If `bundle` is not installed, skip this step and proceed — the cloud build on GitHub Actions will catch any remaining issues.

**Verification command before pushing**:
```bash
ls projects/career-training/docs/_layouts/module.html
```
Expected: file path printed (no "No such file" error).

---

## Fix 2 — Add `jekyll-remote-theme` to `_config.yml` plugins

**Failure**: `_config.yml` uses `remote_theme: just-the-docs/just-the-docs` but `jekyll-remote-theme` is not in the plugins list. GitHub Pages will fall back to its default theme (minima), losing all sidebar navigation, search, and custom styling.

**Time to fix**: 2 minutes.

**Background**: The `remote_theme` key tells Jekyll which theme to use, but GitHub Pages only activates remote theme loading if `jekyll-remote-theme` is in the `plugins` list. Without it, `remote_theme:` is silently ignored. The site will still build and deploy — it just looks nothing like you designed. This is a non-obvious failure because it does not produce an error.

### Step 2.1 — Confirm the current plugins list

```bash
grep -A8 "^plugins:" projects/career-training/docs/_config.yml
```

Current output (as of audit):
```
plugins:
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
```

`jekyll-remote-theme` is absent.

### Step 2.2 — Add the plugin

Open `projects/career-training/docs/_config.yml`. Find the `plugins:` block (line 24) and add `- jekyll-remote-theme` as the first entry:

```yaml
plugins:
  - jekyll-remote-theme
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
```

**Important**: order matters for debugging — put `jekyll-remote-theme` first so if it fails, the error appears immediately in build logs.

### Step 2.3 — Verify the change

```bash
grep -A6 "^plugins:" projects/career-training/docs/_config.yml
```

Expected output:
```
plugins:
  - jekyll-remote-theme
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
```

### Step 2.4 — Confirm remote_theme is also present

```bash
grep "remote_theme:" projects/career-training/docs/_config.yml
```

Expected: `remote_theme: just-the-docs/just-the-docs`

Both `remote_theme:` and `- jekyll-remote-theme` in plugins must be present together. One without the other does nothing.

**Verification command before pushing**:
```bash
grep "jekyll-remote-theme" projects/career-training/docs/_config.yml
```
Expected: two matches — one under `plugins:` and optionally a comment line.

---

## Fix 3 — Create `docs/_includes/head_custom.html` with GA4 snippet

**Failure**: `docs/_includes/head_custom.html` does not exist. Without it, GA4 tracking never fires. Every page view from Day 1 is permanently lost data — you cannot retroactively reconstruct traffic that was never tracked.

**Time to fix**: 8-12 minutes (includes GA4 account steps if account already exists; add 15 minutes if creating account from scratch).

**Background**: Just the Docs loads `_includes/head_custom.html` into the `<head>` of every page if the file exists. This is the theme's designated hook for custom head content. The GA4 Global Site Tag must go here. Putting it in `_layouts/module.html` alone is insufficient — it would only fire on module pages, not index, navigation, or resource pages.

### Step 3.1 — Prerequisites: Get your GA4 Measurement ID

If you have already created a GA4 property (per `PHASE_1_GOOGLE_ANALYTICS_SETUP.md`):

1. Go to [analytics.google.com](https://analytics.google.com)
2. Click Admin (gear icon, bottom left)
3. Under Property column, click "Data Streams"
4. Click your web stream
5. Copy the **Measurement ID** (format: `G-XXXXXXXXXX`)

If you have NOT created a GA4 property yet:

1. Go to [analytics.google.com](https://analytics.google.com) and sign in
2. Admin > Create Account > Name it "Construction Career Training"
3. Create Property > Name: `Construction Career Training — Phase 1`
4. Time zone: US/Pacific, Currency: USD, Industry: Education
5. Click through to "Web" data stream
6. Stream URL: your site URL (`https://constructiontrainingpath.com` or your GitHub Pages URL)
7. Stream name: `GitHub Pages — Production`
8. Leave Enhanced Measurement ON
9. Copy the Measurement ID shown (`G-XXXXXXXXXX`)

### Step 3.2 — Confirm the _includes directory exists

```bash
ls projects/career-training/docs/_includes/
```

Expected: empty directory (no files) or a directory listing. If directory does not exist:

```bash
mkdir -p projects/career-training/docs/_includes
```

### Step 3.3 — Create `head_custom.html`

Create `projects/career-training/docs/_includes/head_custom.html`. Replace `G-XXXXXXXXXX` in both places with your actual Measurement ID (e.g. `G-ABC123DEF4`):

```html
<!-- Google Analytics 4 — Construction Career Training Phase 1 -->
<!-- Measurement ID: G-XXXXXXXXXX — replace with your actual ID before pushing -->
{% if jekyll.environment == "production" %}
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX', {
    'anonymize_ip': true,
    'custom_map': {
      'dimension1': 'user_segment',
      'dimension2': 'learning_path',
      'dimension3': 'module_number'
    }
  });
</script>
{% endif %}
```

**About the `jekyll.environment` guard**: GitHub Pages sets `JEKYLL_ENV=production` automatically. Local builds do not set this. The guard means GA4 fires only on the live site, not during local `jekyll serve` sessions. This prevents your own development traffic from polluting analytics. If you prefer to remove the guard (simpler, always fires), use the version in `PHASE_1_GOOGLE_ANALYTICS_SETUP.md` Part 1.3.

### Step 3.4 — Verify the file contains your Measurement ID

```bash
grep "G-" projects/career-training/docs/_includes/head_custom.html
```

Expected: two lines each containing your Measurement ID (once in the script src URL, once in the config call). If you see `G-XXXXXXXXXX` (the placeholder), you forgot to substitute your real ID — do that now.

### Step 3.5 — Post-push verification (do after deploy)

After deploying:
1. Open your live site in Chrome
2. Right-click > View Page Source
3. Press Ctrl+F and search for `gtag`
4. You should see the GA4 script tag in the `<head>` section
5. In GA4 dashboard > Reports > Realtime — your visit should appear within 60 seconds

If the script tag is absent in page source:
- Confirm `head_custom.html` is committed (not just saved locally): `git status projects/career-training/docs/_includes/`
- Confirm the file is in `_includes/`, not `_layouts/` or anywhere else

**Verification command before pushing**:
```bash
cat projects/career-training/docs/_includes/head_custom.html | grep -c "G-"
```
Expected: `2` (Measurement ID appears twice in the file). If output is `0`, you used the placeholder `G-XXXXXXXXXX` — substitute your real ID.

---

## Fix 4 — Create `docs/signup.md` email signup landing page

**Failure**: `docs/signup.md` does not exist. Any link in module pages pointing to `/signup/` returns a 404. Modules contain CTAs ("Sign up for this path's email sequence →") that are currently dead links.

**Time to fix**: 5 minutes for a placeholder. 20-30 minutes for live Kit forms (requires Kit account with forms created).

**Background**: The signup page serves as the hub for all email capture. Module CTAs link here. Kit form embed codes go on this page. If Kit setup is not complete, create a placeholder now to prevent 404s — it takes 3 minutes and prevents an embarrassing broken first impression if anyone visits before you wire up Kit.

### Option A — Placeholder signup page (3 minutes, no Kit account needed)

Use this if Kit account is not yet set up or form embed codes are not ready. The placeholder prevents 404s and sets expectations.

Create `projects/career-training/docs/signup.md`:

```markdown
---
layout: default
title: Sign Up — Get Your Learning Path by Email
nav_order: 99
nav_exclude: true
permalink: /signup/
---

# Get Your Learning Path by Email

Email signups open soon. Check back in a few days.

In the meantime, bookmark this site and start with the module that matches your goals:

- [Quick Start — Which path is right for me?]({{ site.baseurl }}/navigation/quick-start/)
- [All Modules]({{ site.baseurl }}/navigation/module-quick-reference/)
- [Industrial GC Path]({{ site.baseurl }}/navigation/industrial-path/)
- [Residential GC Path]({{ site.baseurl }}/navigation/residential-path/)

Questions? See the [FAQ]({{ site.baseurl }}/navigation/faq/).
```

### Option B — Live Kit forms (20-30 minutes, Kit account required)

Use this if Kit account is set up and form embed codes are available (per `PHASE_1_KIT_COM_INTEGRATION_SETUP.md` Part 1.1). Replace the four `data-uid` and `src` URLs with your actual Kit form embed codes.

Create `projects/career-training/docs/signup.md`:

```markdown
---
layout: default
title: Sign Up — Get Your Learning Path by Email
nav_order: 99
nav_exclude: true
permalink: /signup/
---

# Get Your Learning Path Delivered by Email

Choose your track below. You'll receive module excerpts, case studies, and
resources tailored to your path — no spam, unsubscribe anytime.

---

## Industrial GC Path

For project managers, field supervisors, and specialty contractors
ready to manage large commercial or industrial projects.

<!-- Kit form embed — Industrial GC Path -->
<!-- Replace data-uid and src with your actual Kit embed code -->
<script async data-uid="INDUSTRIAL_FORM_UID"
  src="https://YOUR_USERNAME.kit.com/INDUSTRIAL_FORM_ID/index.js">
</script>

---

## Residential GC Path

For residential construction professionals, remodelers, and custom home
builders ready to start or expand their own business.

<!-- Kit form embed — Residential GC Path -->
<script async data-uid="RESIDENTIAL_FORM_UID"
  src="https://YOUR_USERNAME.kit.com/RESIDENTIAL_FORM_ID/index.js">
</script>

---

## Specialty Sub → PM Path

For electricians, plumbers, framers, HVAC techs, and specialty contractors
moving into project management or foreman roles.

<!-- Kit form embed — Specialty Sub Path -->
<script async data-uid="SPECIALTY_FORM_UID"
  src="https://YOUR_USERNAME.kit.com/SPECIALTY_FORM_ID/index.js">
</script>

---

## Not sure which path?

[Take the Quick Start quiz →]({{ site.baseurl }}/navigation/quick-start/)

---

*No spam. No upsells. Unsubscribe anytime from any email.*  
*Powered by [Kit](https://kit.com).*
```

### Step 4.1 — Getting your Kit embed codes

If using Option B:
1. Log in to your Kit dashboard at [app.kit.com](https://app.kit.com)
2. Navigate to Forms (left sidebar)
3. Click your Industrial GC form
4. Click "Embed" or "Share"
5. Select "Inline embed" (not pop-up or landing page)
6. Copy the `<script>` tag shown
7. Replace the placeholder in `signup.md` with the copied script tag
8. Repeat for each path's form

### Step 4.2 — Verify the file renders correctly (local test)

```bash
cd projects/career-training/docs && bundle exec jekyll serve 2>/dev/null &
sleep 5
curl -s http://localhost:4000/signup/ | grep -i "title\|Learning Path\|email" | head -10
kill %1
```

If Ruby/bundle is not available, skip local test and verify after deploy.

### Step 4.3 — Test Kit form submission (do before pushing)

If using live Kit forms:
1. Open Chrome and navigate to the signup page in your local Jekyll server
2. Enter a test email address (use a personal email you can check)
3. Click subscribe
4. Check that email for Kit confirmation message (arrives within 2 minutes)
5. Click the confirmation link
6. In Kit dashboard, verify the subscriber appears in your list

If the confirmation email does not arrive within 5 minutes:
- Check Kit dashboard > Forms > your form > Subscriber count (should be 1 pending confirmation)
- Check spam folder
- In Kit > Settings > Email, confirm From Address is verified

**Verification command before pushing**:
```bash
ls -la projects/career-training/docs/signup.md
```
Expected: file exists with non-zero size.

---

## Fix 5 (Bonus) — Move modules 37-38 to `docs/modules/`

**Failure**: `37-industrial-commissioning.md` and `38-multi-family-commercial-fundamentals.md` are in the root `projects/career-training/` directory. They will not appear on the GitHub Pages site unless moved to `docs/modules/`.

**Time to fix**: 2 minutes.

**Decision point**: Confirm whether modules 37-38 should appear on the Phase 1 site. The audit audit notes them as "in wrong directory" — this fix assumes you want them included.

### Step 5.1 — Verify the files exist in the root directory

```bash
ls projects/career-training/37-*.md projects/career-training/38-*.md 2>/dev/null
```

Expected:
```
projects/career-training/37-industrial-commissioning.md
projects/career-training/38-multi-family-commercial-fundamentals.md
```

### Step 5.2 — Move the files

```bash
mv projects/career-training/37-industrial-commissioning.md \
   projects/career-training/docs/modules/37-industrial-commissioning.md

mv projects/career-training/38-multi-family-commercial-fundamentals.md \
   projects/career-training/docs/modules/38-multi-family-commercial-fundamentals.md
```

### Step 5.3 — Verify the move completed

```bash
ls projects/career-training/docs/modules/37-*.md projects/career-training/docs/modules/38-*.md
```

Expected: both paths printed. Also confirm the originals are gone:

```bash
ls projects/career-training/37-*.md 2>&1
```

Expected: `No such file or directory`.

### Step 5.4 — Check for any cross-links that reference the old paths

```bash
grep -r "37-industrial\|38-multi-family" projects/career-training/docs/ | grep -v "docs/modules/37\|docs/modules/38"
```

Expected: no output. If any files reference the old paths (e.g., `/37-industrial-commissioning`), update those links to `/modules/37-industrial-commissioning/`.

### Step 5.5 — Verify final module count

```bash
ls projects/career-training/docs/modules/*.md | grep -v "module-gap-analysis\|module-index" | wc -l
```

Expected: `38` (36 original modules + modules 37 and 38 now present).

---

## Pre-Push Verification: All 5 Fixes Applied

Run this consolidated check after completing all fixes above:

```bash
echo "=== Fix 1: module layout ==="
ls projects/career-training/docs/_layouts/module.html && echo "PASS" || echo "FAIL"

echo "=== Fix 2: jekyll-remote-theme in config ==="
grep "jekyll-remote-theme" projects/career-training/docs/_config.yml && echo "PASS" || echo "FAIL"

echo "=== Fix 3: head_custom.html with GA4 ==="
grep "G-" projects/career-training/docs/_includes/head_custom.html 2>/dev/null && echo "PASS" || echo "FAIL — file missing or no Measurement ID"

echo "=== Fix 4: signup.md exists ==="
ls projects/career-training/docs/signup.md && echo "PASS" || echo "FAIL"

echo "=== Fix 5: modules 37-38 in docs/modules/ ==="
ls projects/career-training/docs/modules/37-*.md projects/career-training/docs/modules/38-*.md 2>/dev/null && echo "PASS" || echo "FAIL or intentionally excluded"

echo "=== Module count ==="
ls projects/career-training/docs/modules/*.md | grep -v "module-gap-analysis\|module-index" | wc -l
```

All 5 checks should print `PASS`. Module count should be 36-38 depending on Fix 5 decision.

### Stage and commit all fixes

```bash
git add projects/career-training/docs/_layouts/module.html
git add projects/career-training/docs/_config.yml
git add projects/career-training/docs/_includes/head_custom.html
git add projects/career-training/docs/signup.md
git add projects/career-training/docs/modules/37-industrial-commissioning.md
git add projects/career-training/docs/modules/38-multi-family-commercial-fundamentals.md
git status
```

Confirm all 5-6 files appear in "Changes to be committed". Then commit:

```bash
git commit -m "fix: GitHub Pages pre-push remediation — 4 critical fixes + module 37-38 move"
```

You are now cleared to push.

---

## Summary Table

| Issue | File to create/edit | Fix time | Status |
|-------|-------------------|----------|--------|
| 1. layout: module does not exist | `docs/_layouts/module.html` — create | 3 min | [ ] Done |
| 2. jekyll-remote-theme missing | `docs/_config.yml` — add plugin | 2 min | [ ] Done |
| 3. head_custom.html missing | `docs/_includes/head_custom.html` — create | 8-12 min | [ ] Done |
| 4. signup.md missing | `docs/signup.md` — create | 3-30 min | [ ] Done |
| 5. Modules 37-38 wrong directory | `docs/modules/37-*.md`, `38-*.md` — move | 2 min | [ ] Done |

**Total time**: 18-49 minutes depending on whether Kit/GA4 accounts exist.

**Go/no-go**: Do not push until all 4 numbered fixes are DONE. Fix 5 is optional if you decide to exclude modules 37-38 from Phase 1.
