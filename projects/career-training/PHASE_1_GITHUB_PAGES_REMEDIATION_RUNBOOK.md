---
title: "Phase 1 GitHub Pages Remediation Runbook — 4 Critical Failures + Directory Fix"
project: career-training
phase: "1"
created: 2026-07-04
status: execution-ready
estimated-time: 18-49 minutes total
item: "53 (Session 4588)"
cross-reference: "GITHUB_PAGES_REMEDIATION_RUNBOOK.md (detailed step-by-step implementation)"
---

# Phase 1 GitHub Pages Remediation Runbook

**Purpose**: Decision-maker entry point for the 4 critical build failures identified in Item 50 (Session 4563). Understand root cause, apply the fix, verify, and know the rollback if needed. For copy-paste commands and detailed sub-steps, see `GITHUB_PAGES_REMEDIATION_RUNBOOK.md`.

**Current state of the repository (as of 2026-07-04)**: All 4 files have been created since the Item 50 audit. The fixes below document the root cause and verification so you can confirm the current state is correct before pushing.

**Run this pre-push verification first:**

```bash
echo "=== Fix 1: module layout ==="
ls projects/career-training/docs/_layouts/module.html && echo "PASS" || echo "FAIL"

echo "=== Fix 2: jekyll-remote-theme in config ==="
grep "jekyll-remote-theme" projects/career-training/docs/_config.yml && echo "PASS" || echo "FAIL"

echo "=== Fix 3: head_custom.html with GA4 ==="
grep "G-" projects/career-training/docs/_includes/head_custom.html 2>/dev/null && echo "PASS" || echo "FAIL"

echo "=== Fix 4: signup.md exists ==="
ls projects/career-training/docs/signup.md && echo "PASS" || echo "FAIL"

echo "=== Bonus: modules 37-38 location ==="
ls projects/career-training/docs/modules/37-*.md projects/career-training/docs/modules/38-*.md 2>/dev/null && echo "IN docs/modules/ — PASS" || echo "Not in docs/modules — see Fix 5"
```

If all 4 numbered fixes show PASS, skip directly to the commit section at the end. If any show FAIL, find the matching section below.

---

## Failure 1 — `layout: module` does not exist

### Root cause (why this is fatal)

`_config.yml` sets a front matter default: every file under `docs/modules/` inherits `layout: module`. Jekyll resolves layouts at build time by looking for `docs/_layouts/module.html`. Just the Docs (your remote theme) provides `default`, `page`, `home`, and `minimal` layouts — not `module`. If `module.html` does not exist, Jekyll halts the entire build with a fatal error: `Layout 'module' does not exist`. The site does not deploy at all; no pages are generated.

### Current status

`docs/_layouts/module.html` was created after the Item 50 audit. Verify:

```bash
cat projects/career-training/docs/_layouts/module.html | head -3
```

Expected first line: `---` (YAML front matter delimiter). If the file is present and begins with `layout: default`, this failure is resolved.

### Fix (if file is missing or empty)

Create `projects/career-training/docs/_layouts/module.html`:

```html
---
layout: default
---

<div class="module-wrapper">

  {% if page.module %}
  <div class="module-meta" style="margin-bottom: 1.5rem; padding: 0.75rem 1rem; background: #f5f6fa; border-left: 4px solid #2869e6; border-radius: 0 4px 4px 0;">
    <span class="module-number" style="font-weight: 700; font-size: 0.9rem; color: #444;">Module {{ page.module }}</span>
    {% if page.discipline %}
    &nbsp;&middot;&nbsp;
    <span class="module-disciplines" style="font-size: 0.85rem; color: #666;">{{ page.discipline | join: " &middot; " }}</span>
    {% endif %}
    {% if page.audience %}
    <br /><span class="module-audience" style="font-size: 0.82rem; color: #888; font-style: italic;">Audience: {{ page.audience }}</span>
    {% endif %}
  </div>
  {% endif %}

  <div class="module-content">
    {{ content }}
  </div>

  <div class="module-footer" style="margin-top: 3rem; padding-top: 1.5rem; border-top: 1px solid #e1e4e8;">
    <p style="font-size: 0.9rem; color: #555;">
      <a href="{{ site.baseurl }}/modules/" style="text-decoration: none;">&larr; All Modules</a>
      &nbsp;&nbsp;|&nbsp;&nbsp;
      <a href="{{ site.baseurl }}/signup/" style="text-decoration: none;">Get this path by email &rarr;</a>
    </p>
  </div>

</div>
```

### Verification test

```bash
ls projects/career-training/docs/_layouts/module.html
grep "layout: default" projects/career-training/docs/_layouts/module.html
```

Both commands must succeed. If Ruby is available locally: `cd projects/career-training/docs && bundle exec jekyll build 2>&1 | grep -i "layout\|error\|fatal"` — zero matches = pass.

### Rollback if this causes problems

If the module layout introduces rendering issues after deploy:

```bash
# Option A: Revert to the simplest possible layout (no meta block)
cat > projects/career-training/docs/_layouts/module.html << 'EOF'
---
layout: default
---
{{ content }}
EOF

# Option B: Remove the layout file and change _config.yml default to 'default'
# In _config.yml, change: layout: module → layout: default
# Then: git rm projects/career-training/docs/_layouts/module.html
```

---

## Failure 2 — `jekyll-remote-theme` plugin missing

### Root cause (why this is fatal)

`_config.yml` uses `remote_theme: just-the-docs/just-the-docs` to load the Just the Docs theme from GitHub. However, Jekyll only activates the remote theme loading mechanism if `jekyll-remote-theme` appears in the `plugins:` list. Without the plugin entry, the `remote_theme:` key is silently ignored. The site builds and deploys — it just uses GitHub Pages' default Minima theme instead. You get black-and-white text with no sidebar, no search, no navigation, no responsive layout. This is a silent failure: no build error, just a completely wrong appearance.

### Current status

The plugin was added to `_config.yml` after the Item 50 audit. Verify:

```bash
grep -A6 "^plugins:" projects/career-training/docs/_config.yml
```

Expected output must include `- jekyll-remote-theme` as the first list entry.

### Fix (if missing)

Open `projects/career-training/docs/_config.yml`. Find the `plugins:` block and add `jekyll-remote-theme` as the first entry:

```yaml
plugins:
  - jekyll-remote-theme
  - jekyll-feed
  - jekyll-sitemap
  - jekyll-seo-tag
```

Save, verify with `grep -A6 "^plugins:" projects/career-training/docs/_config.yml`.

Both `remote_theme:` and `- jekyll-remote-theme` must be present together. One without the other does nothing.

### Verification test

```bash
grep "jekyll-remote-theme" projects/career-training/docs/_config.yml
grep "remote_theme:" projects/career-training/docs/_config.yml
```

Both must return matching lines.

### Rollback if theme breaks the build

Pin the remote theme to a known-good version tag instead of the floating `main` branch:

```yaml
# In _config.yml, change:
remote_theme: just-the-docs/just-the-docs
# To (check https://github.com/just-the-docs/just-the-docs/releases for latest stable):
remote_theme: just-the-docs/just-the-docs@v0.10.0
```

If the theme breaks catastrophically and you need a live site immediately: change `remote_theme:` to `theme: minima` and remove `jekyll-remote-theme` from the plugins list. Minima is available on GitHub Pages without any plugin. The site will look plain but will be functional.

---

## Failure 3 — `docs/_includes/head_custom.html` missing (GA4 analytics lost)

### Root cause (why this is fatal)

Just the Docs automatically loads `_includes/head_custom.html` into the `<head>` of every page if the file exists. This is the theme's designated hook for injecting custom `<head>` content — specifically the Google Analytics 4 Global Site Tag. Without this file, GA4 never loads, and every page view from Day 1 is permanently lost data. Unlike the layout failure, this does not cause a build error — the site deploys normally, you just have no analytics. You cannot retroactively reconstruct traffic that was never tracked.

### Current status

`docs/_includes/head_custom.html` was created after the Item 50 audit. Verify:

```bash
cat projects/career-training/docs/_includes/head_custom.html
```

Expected: the file contains a `gtag` script block. The GA4 Measurement ID placeholder is `G-XXXXXXXXXX` — this must be replaced with your actual Measurement ID before the site is useful for analytics.

### Action required before pushing

The file exists but contains a placeholder Measurement ID. **You must replace `G-XXXXXXXXXX` with your actual GA4 Measurement ID before pushing.** If you push with the placeholder, GA4 will not record traffic (the placeholder ID routes to nowhere).

**Getting your Measurement ID:**
1. Go to [analytics.google.com](https://analytics.google.com)
2. Admin (gear icon) > Data Streams > your web stream
3. Copy the Measurement ID (format: `G-XXXXXXXXXX`, e.g. `G-ABC123DEF4`)

**Substituting the ID:**
```bash
# Replace BOTH occurrences of G-XXXXXXXXXX in the file with your actual ID
# Example if your ID is G-ABC123DEF4:
sed -i 's/G-XXXXXXXXXX/G-ABC123DEF4/g' projects/career-training/docs/_includes/head_custom.html

# Verify:
grep "G-" projects/career-training/docs/_includes/head_custom.html
```

Expected: two lines containing your actual Measurement ID (not the placeholder).

**If you do not yet have a GA4 account:** Create one at analytics.google.com (free). Name the property "Construction Career Training — Phase 1", create a web data stream with your site URL. The Measurement ID is shown immediately after stream creation. This takes 5-8 minutes.

**Acceptable deferral:** If you cannot complete GA4 setup now, you may push with the placeholder. The site will build and be live. You will have no analytics until you update the ID, commit, and push again. Every day of traffic before the real ID is in place is permanently lost — weigh this against the cost of delay.

### Verification test

```bash
grep -c "G-" projects/career-training/docs/_includes/head_custom.html
```

Expected: `2` (your real Measurement ID appears twice — once in the script src URL, once in the config call). If output is `0`: file is empty. If the IDs shown are `G-XXXXXXXXXX`: placeholder not replaced.

### Rollback

If GA4 causes unexpected issues (unlikely — it's a passive tracking script):

```bash
# Remove the GA4 script by commenting out the jekyll.environment guard:
# Change {% if jekyll.environment == "production" %} to {% comment %} and {% endif %} to {% endcomment %}
# Or simply empty the file:
echo "<!-- GA4 temporarily disabled -->" > projects/career-training/docs/_includes/head_custom.html
```

---

## Failure 4 — `docs/signup.md` missing (email signup 404)

### Root cause (why this is fatal)

Every module page footer contains a CTA link: "Get this path by email →" pointing to `/signup/`. The module layout (`module.html`) hardcodes this link. If `docs/signup.md` does not exist, every click on that CTA returns a 404. First-time visitors who want to subscribe cannot. This is not a build failure — Jekyll builds successfully — but it is a broken user experience on every single module page.

### Current status

`docs/signup.md` was created after the Item 50 audit. Verify:

```bash
ls -la projects/career-training/docs/signup.md
grep "permalink" projects/career-training/docs/signup.md
```

Expected: file exists with non-zero size; frontmatter contains `permalink: /signup/`.

### Action required before pushing

The signup page contains Kit form embed code placeholders. Three states are possible:

**State A — Placeholder ("coming soon") page**: The current `signup.md` has placeholder text where the Kit `<script>` tags should be. This is acceptable for launch — the page loads (no 404), visitors see a message, but cannot subscribe yet. You can add Kit forms later without taking the site down.

**State B — Live Kit forms embedded**: Replace the placeholder comment blocks in `signup.md` with your actual Kit `<script>` embed tags. Requires Kit account with 3 forms created (Industrial GC, Residential GC, Specialty Sub to PM). Embed codes are in: Kit dashboard > Forms > your form > Embed > Inline embed > copy `<script>` tag.

**State C — Hybrid**: Add live Kit forms for the paths where setup is complete; leave placeholders for others.

Any state is acceptable for launch. State A prevents 404s. State B enables email capture from Day 1. State B is strongly preferred if Kit is already set up (see `PHASE_1_KIT_COM_INTEGRATION_SETUP.md`).

### Verification test

```bash
# File exists
ls projects/career-training/docs/signup.md

# Permalink is correct
grep "permalink: /signup/" projects/career-training/docs/signup.md

# Kit embed status (check for placeholder vs live)
grep -c "data-uid" projects/career-training/docs/signup.md
```

If the last command returns `0`: placeholder page (no Kit forms yet). If `3` or more: live Kit forms embedded.

### Rollback

If the signup page causes any build issue (YAML syntax error, Liquid error):

```bash
git checkout HEAD -- projects/career-training/docs/signup.md
```

Or create a minimal valid placeholder:

```bash
cat > projects/career-training/docs/signup.md << 'EOF'
---
layout: default
title: Sign Up
nav_exclude: true
permalink: /signup/
---

# Email signup coming soon.

[Return to all modules]({{ site.baseurl }}/modules/)
EOF
```

---

## Bonus Fix 5 — Modules 37-38 in wrong directory

### Root cause

`37-industrial-commissioning.md` and `38-multi-family-commercial-fundamentals.md` are in the `projects/career-training/` root directory, not in `docs/modules/`. Files outside the `docs/` directory are never processed by Jekyll. They will not appear on the GitHub Pages site regardless of any configuration change.

### Decision required

This is not a build failure — the site builds without these files. The question is whether you want them on the Phase 1 site.

**Include them (recommended):** Move both files to `docs/modules/`. They become modules 37-38 on the site and the total module count rises from 36 to 38.

**Exclude them from Phase 1:** Leave them where they are. They are not on the site but are preserved in the repository.

### Fix (if including)

```bash
mv projects/career-training/37-industrial-commissioning.md \
   projects/career-training/docs/modules/37-industrial-commissioning.md

mv projects/career-training/38-multi-family-commercial-fundamentals.md \
   projects/career-training/docs/modules/38-multi-family-commercial-fundamentals.md
```

Verify:

```bash
ls projects/career-training/docs/modules/37-*.md projects/career-training/docs/modules/38-*.md
ls projects/career-training/37-*.md 2>&1  # should say "No such file"
```

### Rollback

```bash
git mv projects/career-training/docs/modules/37-industrial-commissioning.md \
       projects/career-training/37-industrial-commissioning.md
git mv projects/career-training/docs/modules/38-multi-family-commercial-fundamentals.md \
       projects/career-training/38-multi-family-commercial-fundamentals.md
```

---

## Pre-Push Sign-Off

Run this consolidated check after verifying all fixes:

```bash
echo "=== Fix 1: module layout ===" && \
  ls projects/career-training/docs/_layouts/module.html && echo "PASS" || echo "FAIL"

echo "=== Fix 2: jekyll-remote-theme ===" && \
  grep "jekyll-remote-theme" projects/career-training/docs/_config.yml && echo "PASS" || echo "FAIL"

echo "=== Fix 3: head_custom.html — REAL Measurement ID ===" && \
  grep "G-" projects/career-training/docs/_includes/head_custom.html | grep -v "XXXXXXXXXX" && echo "PASS" || echo "FAIL or placeholder still set"

echo "=== Fix 4: signup.md ===" && \
  ls projects/career-training/docs/signup.md && echo "PASS" || echo "FAIL"

echo "=== Module count (should be 36-38) ===" && \
  ls projects/career-training/docs/modules/*.md | grep -v "module-gap-analysis\|module-index" | wc -l
```

**Gate**: Do not push if Fix 1 or Fix 2 show FAIL. Fix 3 failure means analytics won't work (acceptable risk if deferred). Fix 4 failure means signup page 404 (must resolve).

### Commit when all fixes are verified

```bash
git add projects/career-training/docs/_layouts/module.html
git add projects/career-training/docs/_config.yml
git add projects/career-training/docs/_includes/head_custom.html
git add projects/career-training/docs/signup.md
# If including modules 37-38:
git add projects/career-training/docs/modules/37-industrial-commissioning.md
git add projects/career-training/docs/modules/38-multi-family-commercial-fundamentals.md
git status
git commit -m "fix: career-training Phase 1 GitHub Pages remediation — 4 critical fixes + module 37-38 move"
git push origin master
```

After pushing, proceed to `PHASE_1_POST_LAUNCH_VERIFICATION_CHECKLIST.md` immediately.

---

## Summary

| Failure | File | Fatal? | Status |
|---------|------|--------|--------|
| 1. `layout: module` does not exist | `docs/_layouts/module.html` — create | YES — build halts | `[ ] Verified present` |
| 2. `jekyll-remote-theme` missing | `docs/_config.yml` — add to plugins | YES — theme silently ignored | `[ ] Verified present` |
| 3. `head_custom.html` missing | `docs/_includes/head_custom.html` — create | NO — site live, analytics lost | `[ ] Real ID substituted` |
| 4. `signup.md` missing | `docs/signup.md` — create | NO — site live, CTAs 404 | `[ ] File exists` |
| 5. Modules 37-38 wrong directory | `docs/modules/37-*.md`, `38-*.md` — move | NO — modules absent from site | `[ ] Decision made` |

**Cross-reference**: `GITHUB_PAGES_REMEDIATION_RUNBOOK.md` contains the full copy-paste implementation for all 5 fixes including sub-steps, alternatives, and local test commands.
