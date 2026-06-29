---
title: "Post-Deployment Verification Checklist — 10 Mechanical Checks"
project: career-training
phase: "1"
created: 2026-06-29
status: execution-ready
estimated-time: 15-20 minutes
trigger: "Run immediately after GitHub Pages (or Netlify/Vercel) shows first successful deployment"
---

# Post-Deployment Verification Checklist

**Purpose**: Confirm the GitHub Pages deployment is working correctly before any promotion or distribution. Run all 10 checks in order. Each check has a pass condition and a remediation path. Allow 15-20 minutes total.

**Run this immediately after the first successful build** — not an hour later, not the next day. Some issues (like broken forms or missing analytics) become harder to diagnose after traffic accumulates.

**Site URL**: Fill in before starting:
- GitHub Pages URL: `https://_______.github.io/career-training/` (or your custom domain)
- Substitute your URL for `[SITE_URL]` in every check below.

---

## Check 1 — Homepage loads with correct layout

**What to do**: Open `[SITE_URL]` in Chrome Incognito mode.

**Why Incognito**: Incognito clears cache and cookies, so you see what a first-time visitor sees. This is critical — local caching can mask deployment issues.

**Pass criteria**:
- [ ] Page loads within 5 seconds
- [ ] Just the Docs sidebar is visible on the left (module navigation categories, search box)
- [ ] Page title matches: "Construction Career Training Curriculum"
- [ ] The "Choose Your Path" section is visible with Industrial GC, Residential GC, and Specialty Sub headings
- [ ] No raw Markdown text visible (no `##` headings, no `---` horizontal rules displayed as literal dashes)
- [ ] No broken layout (navigation piled on top of content, text running off the right edge)

**If FAIL — layout is broken or sidebar missing**:
- Likely cause: `jekyll-remote-theme` not in plugins list → Fix 2 in `GITHUB_PAGES_REMEDIATION_RUNBOOK.md`
- Quick check: `view-source:[SITE_URL]` — if you see raw Markdown, Jekyll did not process the files. If you see HTML but no styling, the theme is not loading.
- If page loads with minima theme (black text on white, no sidebar): `jekyll-remote-theme` plugin is missing.

**If FAIL — completely blank page or 404**:
- Likely cause: baseurl mismatch. If you deployed to `yourusername.github.io/career-training` but `baseurl` is `""`, all assets load from the wrong path.
- Fix: set `baseurl: "/career-training"` in `_config.yml`, commit, push, wait for rebuild.

**Result**: [ ] PASS [ ] FAIL — Notes: _______________

---

## Check 2 — Module links return 200 (not 404)

**What to do**: Click 5 module links from the sidebar or the module index page. Specifically test modules 34-38 (the ones that were recently moved or added).

**Test these URLs** (replace `[SITE_URL]` with your actual domain):
- `[SITE_URL]/modules/34-residential-scheduling-practice/`
- `[SITE_URL]/modules/35-construction-insurance-program-design/`
- `[SITE_URL]/modules/36-safety-program-construction/`
- `[SITE_URL]/modules/37-industrial-commissioning/` (only if module 37 was moved to docs/modules/)
- `[SITE_URL]/modules/38-multi-family-commercial-fundamentals/` (only if module 38 was moved)

**Pass criteria for each URL**:
- [ ] Page loads (no 404 error page)
- [ ] Module title is visible in the page header
- [ ] Sidebar shows the module in the navigation

**Batch check (optional, Chrome DevTools)**:
1. Open Chrome DevTools (F12) > Console tab
2. Paste this snippet to check all anchor links on the module index page:
```javascript
// Checks all links on current page for 404s
Promise.all(
  Array.from(document.querySelectorAll('a[href]'))
    .filter(a => a.href.startsWith(location.origin))
    .map(a => fetch(a.href, {method:'HEAD'}).then(r => ({url:a.href, status:r.status})))
).then(results => {
  const broken = results.filter(r => r.status === 404);
  console.log('Broken links:', broken.length);
  broken.forEach(r => console.log('404:', r.url));
});
```
Expected: "Broken links: 0"

**If FAIL — specific module returns 404**:
- Confirm the module file is in `docs/modules/` and was committed: `git log --oneline -- projects/career-training/docs/modules/37-industrial-commissioning.md`
- Confirm the permalink is correct in frontmatter (if overridden) or relies on default path rules
- If the file was just moved from root to `docs/modules/`, confirm the move was committed (not just saved locally)

**Result**: [ ] PASS [ ] FAIL — Failed URLs: _______________

---

## Check 3 — Case study links load full content

**What to do**: Navigate to the case studies section and open two case studies. Confirm full content is present, not truncated.

**Navigate to**: `[SITE_URL]/case-studies/` or use the sidebar navigation.

**Pass criteria**:
- [ ] Case study page loads (not 404)
- [ ] Full scenario is readable (not cut off mid-sentence)
- [ ] Solution/worked answer section is present (not just the problem statement)
- [ ] If case studies are embedded in module pages, open Module 01 and scroll to the first case study section — confirm it is complete

**If FAIL — content truncated**:
- Check for a `truncate:` filter in `_config.yml` or in any layout file
- Check for an `excerpt_separator` that splits content prematurely
- If using Jekyll `page.excerpt`, this takes only the first paragraph by default — full content requires `{{ content }}`, not `{{ page.excerpt }}`

**If FAIL — 404 on case-studies directory**:
- Check that case study files are under `docs/case-studies/` and have correct frontmatter
- Confirm the directory is not in the `exclude:` list in `_config.yml`

**Result**: [ ] PASS [ ] FAIL — Notes: _______________

---

## Check 4 — Mobile responsive design

**What to do**: Test the site on a mobile viewport using Chrome DevTools.

**Steps**:
1. Open `[SITE_URL]` in Chrome
2. Press F12 to open DevTools
3. Click the phone/tablet icon ("Toggle Device Toolbar") in the top-left of DevTools
4. Select device: **iPhone 12 Pro** (390px wide) from the dropdown
5. Navigate through three pages: homepage, one module page, the signup page

**Pass criteria for each page**:
- [ ] Text is readable without zooming (minimum 14px effective font size)
- [ ] No horizontal scroll bar at 390px (page content fits within screen width)
- [ ] Long code blocks or tables scroll horizontally within their container (not the whole page)
- [ ] Navigation is accessible (hamburger menu icon visible; tapping it opens the sidebar or a nav menu)
- [ ] Call-to-action buttons and links are large enough to tap (minimum 44px touch target)

**Online alternative (no DevTools needed)**:
Go to [responsivedesignchecker.com](https://responsivedesignchecker.com), enter your site URL, and test with the iPhone 12 preset.

**If FAIL — horizontal scroll**:
- Most common cause: a table or code block with fixed width
- Just the Docs' default CSS handles this, but a custom code block might not
- Temporary fix: add `overflow-x: auto;` to the wrapping element via `docs/assets/css/custom.css` (create if not present)

**If FAIL — navigation not accessible on mobile**:
- Just the Docs provides responsive navigation automatically if the remote theme loaded correctly
- If sidebar is completely missing on mobile: the remote theme is not loading — return to Check 1

**Result**: [ ] PASS [ ] FAIL — Notes: _______________

---

## Check 5 — Email signup form submits successfully

**What to do**: Submit a test email address via the signup form on `[SITE_URL]/signup/`.

**If signup page has live Kit forms**:
1. Navigate to `[SITE_URL]/signup/`
2. Enter a test email address (one you can access)
3. Click the subscribe button
4. Within 2 minutes: check that email inbox for a Kit confirmation email
5. Click the confirmation link in the email
6. In Kit dashboard, verify the subscriber appears in your list

**Pass criteria**:
- [ ] Signup page loads (not 404)
- [ ] Form is visible and renders correctly (input field, submit button visible)
- [ ] Form submission does not produce a JavaScript error (check Chrome DevTools Console while submitting)
- [ ] Confirmation email arrives within 5 minutes
- [ ] Subscriber appears in Kit dashboard after confirming

**If signup page is a "coming soon" placeholder**:
- [ ] Placeholder page loads (not 404)
- [ ] Text reads clearly (not raw Markdown)
- [ ] Links to module pages work (not broken)
- Mark as PASS with note that live forms are deferred

**If FAIL — Kit form does not render**:
- Check page source for the Kit script tag: `view-source:[SITE_URL]/signup/`
- If script tag is present but form does not render: Kit script may be blocked by an ad blocker. Test in Incognito with extensions disabled.
- If script tag is absent: the embed code in `signup.md` was not formatted correctly. Confirm the `<script>` tag is not inside a code block (backticks). It must be raw HTML in the Markdown file.

**If FAIL — confirmation email does not arrive**:
- Check Kit dashboard > Subscribers to see if the submission was received (may show as "unconfirmed")
- Check spam folder
- In Kit > Settings > Email, confirm your sending domain is verified

**Result**: [ ] PASS [ ] FAIL — Notes: _______________

---

## Check 6 — Google Analytics is tracking

**What to do**: Verify the GA4 script tag is present in the page source AND that traffic appears in GA4 Realtime.

### Part A — Script tag in page source

1. Open `[SITE_URL]` in Chrome
2. Right-click anywhere on the page > "View Page Source"
3. Press Ctrl+F and search for `gtag`

**Pass criteria (Part A)**:
- [ ] `gtag` appears in the page source (at least one match)
- [ ] The script tag references your GA4 Measurement ID (`G-XXXXXXXXXX` — replace with your actual ID)

**If FAIL — gtag not in source**:
- Confirm `head_custom.html` was committed: `git log --oneline -- projects/career-training/docs/_includes/head_custom.html`
- Confirm the file contains your GA4 snippet and not just the `jekyll.environment == "production"` guard with a missing ID
- Note: if the `jekyll.environment` guard is in place, `gtag` only appears in the source when the site is deployed with `JEKYLL_ENV=production`. GitHub Pages sets this automatically. Netlify requires the environment variable set (see rollback doc Step A.4). Local builds will NOT show `gtag` in source.

### Part B — Realtime traffic in GA4

1. Open [analytics.google.com](https://analytics.google.com) in a separate browser tab
2. Navigate to your Construction Career Training property
3. Click **Reports** > **Realtime**
4. Return to your site tab and navigate between 2-3 pages

**Pass criteria (Part B)**:
- [ ] Your visit appears in GA4 Realtime within 60 seconds (shown as "1 user in the last 30 minutes")
- [ ] Page views are recording (listed under "Pages and screens" in Realtime)

**If FAIL — traffic not appearing in Realtime**:
- Confirm the Measurement ID in `head_custom.html` matches the property you are viewing in GA4
- Confirm the data stream in GA4 is connected to the correct URL (Admin > Data Streams > your stream > Stream URL)
- Wait 5 minutes and refresh Realtime — there is occasionally a delay on new properties

**Result**: [ ] PASS [ ] FAIL — Notes: _______________

---

## Check 7 — Navigation menu functions

**What to do**: Test the sidebar navigation and all top-level navigation links.

**Steps**:
1. On the homepage, confirm the left sidebar shows category sections (Industrial GC Path, Residential GC Path, etc. or similar groupings)
2. Click one module link in the sidebar — confirm it navigates correctly
3. Hover over navigation items — confirm hover effects apply (background color change or underline)
4. Click "Back to top" link at the bottom of a long page (if present)
5. Click the site title/logo — confirm it returns to the homepage

**Pass criteria**:
- [ ] Sidebar is visible and populated with navigation links
- [ ] Clicking a nav link navigates to the correct page
- [ ] No links return 404
- [ ] Hover effects work (even basic CSS hover styling)
- [ ] Breadcrumbs display the correct path (Module > [Module Name]) on module pages
- [ ] Search box is visible and typing shows results

**If FAIL — sidebar is empty**:
- Module files may be missing `nav_order` in their frontmatter, or the `defaults:` scope in `_config.yml` is not being applied
- Confirm the `defaults:` section in `_config.yml` uses `path: "modules"` (not a full filesystem path)

**If FAIL — search returns no results**:
- Just the Docs generates a search index during build. If the build succeeded but search doesn't work, the index file may not have been generated.
- Check: `[SITE_URL]/assets/js/search-data.json` — should return a JSON file with your content. If 404, search index generation failed during build.

**Result**: [ ] PASS [ ] FAIL — Notes: _______________

---

## Check 8 — Images load (if any were added)

**What to do**: Verify no broken image icons appear on any page.

**Quick check**:
1. Open Chrome DevTools > Console tab
2. Look for any red error lines containing `404` referencing `.png`, `.jpg`, `.svg`, or `.webp` URLs
3. Also check the Network tab: filter by "Img" and refresh the page — any red rows indicate broken image requests

**Pass criteria**:
- [ ] No broken image icons visible on homepage
- [ ] No 404 errors for image files in DevTools Network tab

**If no images have been added to the site** (the audit confirmed zero image references in module files):
- [ ] SKIP: No images to verify. The `docs/assets/images/` directory is empty. This check is not applicable.

**If FAIL — broken images**:
- Check the URL of the broken image request (visible in DevTools Network tab)
- Confirm the image file exists at that path in the repo under `docs/assets/images/`
- Confirm the image was committed: `git log --oneline -- projects/career-training/docs/assets/images/FILENAME`
- Check for path issues: if `baseurl` is set, image paths in Markdown must use `{{ site.baseurl }}/assets/images/filename.png` not `/assets/images/filename.png`

**Result**: [ ] PASS [ ] SKIP (no images) [ ] FAIL — Notes: _______________

---

## Check 9 — Mobile menu expands and collapses

**What to do**: On a mobile viewport (390px in DevTools), verify the hamburger menu works.

**Steps**:
1. Open `[SITE_URL]` in Chrome DevTools at 390px
2. Look for a hamburger menu icon (three horizontal lines) typically in the top-right or top-left of the mobile header
3. Tap/click the hamburger icon
4. Confirm the navigation menu expands (slides in from the left or drops down)
5. Tap/click the hamburger icon again or a close button
6. Confirm the menu collapses

**Pass criteria**:
- [ ] Hamburger icon is visible at 390px viewport
- [ ] Tapping the icon expands the navigation
- [ ] Navigation links are visible and tappable within the expanded menu
- [ ] Menu collapses when closed
- [ ] After menu closes, page content is fully visible and accessible

**Just the Docs behavior**: Just the Docs uses JavaScript to handle the mobile sidebar toggle. If JavaScript is disabled or failed to load, the mobile menu will not work. Do not test with JavaScript disabled for Phase 1.

**If FAIL — no hamburger icon visible**:
- Likely cause: the remote theme (Just the Docs) did not load correctly
- Return to Check 1 and confirm the theme is loading

**If FAIL — menu opens but does not close**:
- This is a JavaScript issue in the theme. It is unlikely with Just the Docs unless you have conflicting custom JavaScript.
- Check `docs/assets/js/` for any custom scripts that might conflict with Just the Docs' navigation JS.

**Result**: [ ] PASS [ ] FAIL — Notes: _______________

---

## Check 10 — Lighthouse performance score

**What to do**: Run a Lighthouse audit on the homepage and one module page.

**Steps**:
1. Open Chrome DevTools (F12)
2. Click the "Lighthouse" tab (may need to click ">>" to find it)
3. Select: Categories: Performance, Accessibility, Best Practices, SEO
4. Device: Mobile (test mobile first)
5. Click "Analyze page load"
6. Wait 60-90 seconds for results
7. Note the four scores
8. Repeat for one module page (e.g., `[SITE_URL]/modules/01-foundations-contracts-estimating/`)

**Target scores for Phase 1**:
- Performance: > 80 (acceptable: > 70)
- Accessibility: > 90 (must fix if below 80)
- Best Practices: > 80
- SEO: > 90

**Pass criteria**:
- [ ] Performance > 70 on mobile (Just the Docs is not the fastest theme — 70+ is realistic at launch)
- [ ] Accessibility > 80 (failing this means your content is not usable by some learners)
- [ ] Best Practices > 80
- [ ] SEO > 85

**If Performance is 50-70 on mobile**:
- Common causes for documentation sites: render-blocking resources, large JavaScript bundles from Just the Docs
- For Phase 1, a score of 60-70 is acceptable — the content and usability matter more than perfect performance scores
- Defer performance optimization to Phase 2

**If Accessibility is below 80**:
- Check the "Accessibility" section of the Lighthouse report for specific failures
- Common quick fixes: add `alt` attributes to images, ensure sufficient color contrast, use heading levels in order (H1 → H2 → H3, no skipping)

**If SEO is below 85**:
- Common causes: missing `<meta>` description, missing structured data, no `robots.txt`
- `jekyll-seo-tag` plugin generates SEO tags automatically from frontmatter. Confirm it is in the plugins list.
- Check that `index.md` has a `description:` field in frontmatter

**Record scores**:
- Homepage Mobile: Performance ___ / Accessibility ___ / Best Practices ___ / SEO ___
- Module page Mobile: Performance ___ / Accessibility ___ / Best Practices ___ / SEO ___

**Result**: [ ] PASS (all > 70/80/80/85) [ ] PARTIAL (some below target — note which) [ ] FAIL

---

## Verification Sign-Off

Run date/time: ___________________________ UTC

Site URL verified: ___________________________

| Check | Result | Notes |
|-------|--------|-------|
| 1. Homepage layout | | |
| 2. Module links (no 404) | | |
| 3. Case study content complete | | |
| 4. Mobile responsive (390px) | | |
| 5. Email signup form | | |
| 6. GA4 analytics firing | | |
| 7. Navigation menu | | |
| 8. Images (or N/A) | | |
| 9. Mobile hamburger menu | | |
| 10. Lighthouse scores | | |

**Go / No-Go for Phase 1 distribution**:
- [ ] ALL 10 checks PASS → GREEN: proceed to Phase 1 distribution (see `PHASE_2_3_EXECUTION_ROADMAP.md`)
- [ ] 1-2 checks FAIL (non-critical) → YELLOW: proceed with caution, fix within 48 hours
- [ ] 3+ checks FAIL → RED: resolve failures before any promotion or distribution

Non-critical failures that can be deferred (site is still usable): Check 8 (no images), Check 10 score in 60-70 range, Check 9 minor cosmetic issues.

Critical failures that must be resolved before distribution: Check 1 (homepage broken), Check 2 (404 on modules), Check 5 (signup 404), Check 6 (no GA tracking).
