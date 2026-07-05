---
title: "Phase 1 Post-Launch Verification Checklist — 10 Tests with GREEN/YELLOW/RED Criteria"
project: career-training
phase: "1"
created: 2026-07-04
status: execution-ready
item: "53 (Session 4588)"
cross-reference: "POST_DEPLOYMENT_VERIFICATION_CHECKLIST.md (10-check detailed post-deploy verification with diagnostic paths)"
trigger: "Run immediately after first successful deployment (GitHub Pages, Netlify, or Vercel)"
estimated-time: 20-30 minutes
---

# Phase 1 Post-Launch Verification Checklist

**Run this immediately after the first successful build** — the moment the platform shows a green deployment status. Not an hour later. Not the next day. Some issues (missing analytics, broken forms) are harder to diagnose once real traffic has started accumulating.

**Site URL**: Fill in before starting:

- Deployed URL: `______________________________________`
  (Example: `https://construction-career-training.netlify.app` or `https://constructiontrainingpath.com`)
- Substitute this for `[SITE_URL]` in every check below

**Test environment**: Use Chrome Incognito for all checks. Incognito bypasses browser cache and extensions, which ensures you see what a first-time visitor sees.

**Who runs this**: The person who pushed the deployment. Run all 10 checks in one session. Mark each with GREEN, YELLOW, or RED.

---

## Check 1 — Homepage loads with correct layout

**What to do**: Open `[SITE_URL]` in Chrome Incognito.

**Pass criteria (GREEN)**:
- [ ] Page loads within 5 seconds
- [ ] Just the Docs sidebar is visible on the left (module navigation categories, search box)
- [ ] Page title in browser tab: "Construction Career Training Curriculum"
- [ ] "Choose Your Path" or path navigation visible with Industrial GC, Residential GC, Specialty Sub sections
- [ ] No raw Markdown text visible (no literal `##`, `---`, `**` characters in page content)
- [ ] No broken layout (nav piled on content, text running off right edge)

**Result criteria**:
- GREEN: All 6 pass criteria met
- YELLOW: Page loads but minor styling issues (e.g., font size slightly off, one element misaligned)
- RED: Raw Markdown visible, no sidebar, page fails to load, or 404

**If RED — sidebar missing (Minima theme, no navigation)**:
`jekyll-remote-theme` not in plugins list. See Fix 2 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md`.

**If RED — completely blank page or 404**:
`baseurl` mismatch. Check `_config.yml` baseurl against actual URL structure. See `GITHUB_PAGES_TROUBLESHOOTING_DECISION_TREE.md` Step 1.

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — Notes: ___________________

---

## Check 2 — Module links return 200 (no 404s)

**What to do**: Click 5 module links from the sidebar or module index page. Specifically test the modules that were recently moved or added (34-38).

**URLs to test** (replace `[SITE_URL]`):
- `[SITE_URL]/modules/01-foundations-contracts-estimating/`
- `[SITE_URL]/modules/34-residential-scheduling-practice/`
- `[SITE_URL]/modules/35-construction-insurance-program-design/`
- `[SITE_URL]/modules/37-industrial-commissioning/` (if module 37 was moved to docs/modules/)
- `[SITE_URL]/modules/38-multi-family-commercial-fundamentals/` (if module 38 was moved)

**Quick batch check (Chrome DevTools Console)**:

Open `[SITE_URL]/modules/` in Chrome, open DevTools (F12) > Console, paste:

```javascript
Promise.all(
  Array.from(document.querySelectorAll('a[href]'))
    .filter(a => a.href.startsWith(location.origin))
    .map(a => fetch(a.href, {method:'HEAD'}).then(r => ({url:a.href, status:r.status})))
).then(results => {
  const broken = results.filter(r => r.status === 404);
  console.log('Broken links: ' + broken.length);
  broken.forEach(r => console.log('404: ' + r.url));
});
```

Expected: "Broken links: 0"

**Result criteria**:
- GREEN: All tested URLs return 200, batch check shows 0 broken links
- YELLOW: 1-2 broken links on recently-added or optional pages (not core modules 01-36)
- RED: Any core module (01-36) returns 404, or 3+ broken links total

**If RED — module returns 404**:
Confirm the file was committed: `git log --oneline -- projects/career-training/docs/modules/[filename].md`
If module 37 or 38 returns 404: verify the file was moved to `docs/modules/` and committed.

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — Broken links found: ___________________

---

## Check 3 — Email signup form responsive and functional

**What to do**: Navigate to `[SITE_URL]/signup/` and test the email signup form.

**For live Kit forms (Option B signup page)**:
1. Navigate to `[SITE_URL]/signup/`
2. Enter a test email address (one you can check)
3. Click subscribe
4. Within 5 minutes: check that email inbox for a Kit confirmation message
5. Click the confirmation link
6. In Kit dashboard, verify the subscriber appears in your list

**For placeholder signup page (Option A)**:
- [ ] Placeholder page loads (not 404)
- [ ] Text is readable (not raw Markdown)
- [ ] Links to modules work (not broken)

**Kit webhook / conversion check (live forms only)**:
1. In Kit dashboard > Subscribers > find the test subscriber
2. Check the tag or sequence assigned matches your expected automation trigger
3. If using a thank-you redirect: confirm `[SITE_URL]/signup-thank-you/` loads correctly

**Result criteria**:
- GREEN (live forms): Page loads, form submits, confirmation email arrives within 5 minutes, subscriber appears in Kit
- GREEN (placeholder): Page loads, no 404, content readable
- YELLOW: Form renders but confirmation email lands in spam; subscriber still appears in Kit
- RED: `/signup/` returns 404, form does not render, submission produces a JavaScript error

**If RED — signup page 404**:
`signup.md` not committed. Fix 4 in `PHASE_1_GITHUB_PAGES_REMEDIATION_RUNBOOK.md`.

**If RED — Kit form does not render**:
Check page source: `view-source:[SITE_URL]/signup/` — confirm the Kit `<script>` tag is present. If absent: embed code is inside a Markdown code block (backticks) instead of raw HTML in the file.

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — Notes: ___________________

---

## Check 4 — Google Analytics (GA4) firing on pages

**What to do**: Verify the GA4 script tag is in the page source AND that your visit appears in GA4 Realtime.

**Part A — Script tag in page source**:
1. Open `[SITE_URL]` in Chrome (not Incognito for this check — you need extensions disabled, not cleared)
2. Right-click anywhere > "View Page Source"
3. Press Ctrl+F and search for `gtag`

Expected: at least one match showing the GA4 Measurement ID.

**Part B — Realtime traffic in GA4**:
1. Open [analytics.google.com](https://analytics.google.com) in a separate tab
2. Navigate to your Construction Career Training property
3. Reports > Realtime
4. Return to your site tab, navigate between 3-4 pages
5. Within 60 seconds: check GA4 Realtime — your visit should appear

**Result criteria**:
- GREEN: `gtag` found in page source with real Measurement ID; visit appears in GA4 Realtime within 60 seconds
- YELLOW: Script tag present but visit does not appear in Realtime after 5 minutes (occasionally a delay on new properties)
- RED: `gtag` not found in page source; GA4 Realtime shows zero activity after 10 minutes

**If RED — gtag not in page source**:
- If the `head_custom.html` has the `jekyll.environment == "production"` guard: this is expected for local builds. GitHub Pages and Netlify (with JEKYLL_ENV=production set) should fire it. Confirm the environment variable is set.
- Confirm `head_custom.html` was committed: `git log --oneline -- projects/career-training/docs/_includes/head_custom.html`
- Confirm the Measurement ID in the file is your real ID, not `G-XXXXXXXXXX` (the placeholder)

**If YELLOW — script present but no Realtime data**:
Wait 10 minutes and refresh. Check that the Measurement ID in `head_custom.html` matches the property you are viewing in GA4.

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — GA4 Measurement ID confirmed: ___________________

---

## Check 5 — Mobile responsive design (3 screen sizes)

**What to do**: Test homepage, one module page, and the signup page at three viewport widths using Chrome DevTools.

**How to open DevTools responsive mode**:
1. Open Chrome DevTools (F12)
2. Click the phone/tablet icon ("Toggle Device Toolbar") in the top-left
3. Set width manually using the dropdown or width field

**Three viewports to test**:

**Viewport A — 390px (iPhone 12 Pro / most modern phones)**:
- Homepage: [ ] Text readable, [ ] Sidebar accessible, [ ] No horizontal scroll
- Module page: [ ] Text readable, [ ] No horizontal scroll, [ ] Long tables scroll within container
- Signup page: [ ] Form fields full-width and tappable, [ ] Submit button visible

**Viewport B — 768px (iPad / small tablet)**:
- Homepage: [ ] Sidebar visible or hamburger menu present, [ ] Content readable
- Module page: [ ] Module meta block (number, discipline) renders correctly
- Signup page: [ ] Form centered or appropriately laid out

**Viewport C — 1440px (standard desktop)**:
- Homepage: [ ] Sidebar fully expanded, [ ] Content not excessively wide
- Module page: [ ] Readable line length (not spanning full 1440px)

**Result criteria**:
- GREEN: All 3 viewports pass all listed checks
- YELLOW: Minor layout imperfections at 768px or 1440px that do not affect usability; or module meta block alignment slightly off
- RED: Horizontal scroll at 390px, form input fields cut off, navigation inaccessible on mobile

**If RED — horizontal scroll at 390px**:
Most common cause: a table or code block with fixed width. Just the Docs handles this automatically if the remote theme loaded correctly. Add `overflow-x: auto` to the wrapping element via `docs/assets/css/custom.css`.

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — Notes: ___________________

---

## Check 6 — Social preview (OG tags rendering)

**What to do**: Verify that when the site URL is shared on social media, it shows a meaningful preview card (title, description, image) rather than a blank or generic preview.

**Test A — Facebook / LinkedIn preview**:
1. Go to [opengraph.xyz](https://www.opengraph.xyz)
2. Enter `[SITE_URL]`
3. Click "Check"

Expected: Title shows "Construction Career Training Curriculum" (or similar), description is present, preview card renders.

**Test B — Twitter / X card validator**:
1. Go to [cards-dev.twitter.com/validator](https://cards-dev.twitter.com/validator) (requires X account)
2. Enter `[SITE_URL]`

Or use [twittercard.verifyp.com](https://twittercard.verifyp.com) as an alternative.

**What generates the OG tags**:
`jekyll-seo-tag` plugin (already in `_config.yml` plugins list) generates `og:title`, `og:description`, `og:url`, and `og:type` automatically from the page's `title:` and `description:` frontmatter and `_config.yml`. No manual OG tag configuration is required unless you want a custom social image.

**Verify SEO plugin output in page source**:
```
view-source:[SITE_URL]
```
Search for `og:title` — should appear in the `<head>` section.

**Result criteria**:
- GREEN: OG title and description render in preview tool; `og:title` found in page source
- YELLOW: Preview shows correct title but no description or no image (image is optional for Phase 1)
- RED: Preview shows blank card, "No data found", or site URL only

**If RED — no OG tags in page source**:
- Confirm `jekyll-seo-tag` is in the plugins list: `grep "jekyll-seo-tag" projects/career-training/docs/_config.yml`
- Confirm `index.md` has a `description:` field in its frontmatter
- Note: `jekyll-seo-tag` requires the `{% seo %}` Liquid tag in your theme's `<head>`. Just the Docs includes this automatically — if the remote theme loaded correctly (Check 1 GREEN), SEO tags should be present.

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — OG title confirmed: ___________________

---

## Check 7 — Site navigation menu functions

**What to do**: Test the sidebar navigation and all top-level navigation links.

**Steps**:
1. On the homepage, confirm the left sidebar shows category sections (path navigation, modules grouping)
2. Click one module link in the sidebar — confirm it navigates correctly
3. Confirm the search box is visible and typing shows results
4. On a module page, confirm breadcrumbs display correctly
5. Click the site title/logo — confirm it returns to the homepage

**Pass criteria**:
- [ ] Sidebar visible and populated with navigation links
- [ ] Clicking a nav link navigates to the correct page
- [ ] Search box visible; typing returns results
- [ ] Breadcrumbs on module pages show correct path
- [ ] Site title/logo links to homepage

**Result criteria**:
- GREEN: All 5 pass criteria met
- YELLOW: Search returns results but they are slow or UI is slightly misaligned
- RED: Sidebar empty, no search box, navigation links 404

**If RED — sidebar empty**:
Just the Docs auto-populates the sidebar from page frontmatter (`nav_order`, `parent`, `title`). If sidebar is empty, either the remote theme is not loaded (see Check 1) or module files are missing `nav_order` values.

**If RED — search returns no results**:
Check: `[SITE_URL]/assets/js/search-data.json` — should return a JSON file with your site content. If 404, the search index was not generated during build.

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — Notes: ___________________

---

## Check 8 — Case study content complete (not truncated)

**What to do**: Open two case studies from the case studies section and confirm full content is present.

**Navigate to**: `[SITE_URL]/case-studies/` or through a module page that links to case studies.

**Pass criteria**:
- [ ] Case study page loads (not 404)
- [ ] Full scenario is readable (not cut off mid-sentence)
- [ ] Solution/worked answer section is present if it exists in the source file
- [ ] No "Read more" truncation that hides content behind a click

**Result criteria**:
- GREEN: Two case studies load with complete content
- YELLOW: One case study has minor truncation on a non-critical section
- RED: Case study returns 404, content is cut off mid-section, or only the problem statement appears without the solution

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — Notes: ___________________

---

## Check 9 — Mobile hamburger menu (navigation on small screens)

**What to do**: At 390px viewport in Chrome DevTools, test the mobile navigation toggle.

**Steps**:
1. Open `[SITE_URL]` in Chrome DevTools at 390px
2. Look for a hamburger menu icon (three horizontal lines) in the header
3. Tap/click it — menu should expand
4. Tap/click the close button or hamburger again — menu should collapse
5. Navigate to a module page using the expanded menu

**Pass criteria**:
- [ ] Hamburger icon visible at 390px
- [ ] Tapping icon expands navigation
- [ ] Navigation links are visible and tappable within expanded menu
- [ ] Menu collapses when toggled again
- [ ] After menu closes, page content is fully visible

**Result criteria**:
- GREEN: All 5 pass criteria met
- YELLOW: Menu opens but close button is not obvious; content is still accessible
- RED: No hamburger icon visible, menu does not open, or page content is hidden behind the menu

**Just the Docs behavior**: Mobile navigation uses JavaScript for the sidebar toggle. If JavaScript fails to load (usually because the remote theme is not loading — see Check 1), the mobile menu will not work.

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — Notes: ___________________

---

## Check 10 — Lighthouse performance and SEO scores

**What to do**: Run a Lighthouse audit on the homepage and one module page.

**Steps**:
1. Open `[SITE_URL]` in Chrome DevTools (F12) > Lighthouse tab
2. Categories: Performance, Accessibility, Best Practices, SEO
3. Device: Mobile
4. Click "Analyze page load" — wait 60-90 seconds
5. Note the four scores
6. Repeat for `[SITE_URL]/modules/01-foundations-contracts-estimating/`

**Target scores**:

| Score | GREEN | YELLOW | RED |
|-------|-------|--------|-----|
| Performance | > 80 | 60-80 | < 60 |
| Accessibility | > 90 | 75-90 | < 75 |
| Best Practices | > 80 | 65-80 | < 65 |
| SEO | > 90 | 75-90 | < 75 |

**Expected baseline for Just the Docs with GitHub Pages / Netlify**: Performance 70-85 mobile (theme loads JavaScript; typical for documentation sites). Accessibility 90+. Best Practices 90+. SEO 90+ if `jekyll-seo-tag` is working.

**Quick fixes if scores are low**:

- SEO < 90: Confirm `jekyll-seo-tag` is in plugins list; add `description:` to `index.md` frontmatter
- Accessibility < 90: Check Lighthouse report for specific failures — most common is insufficient color contrast or missing `alt` attributes on images (unlikely since module files have no images)
- Performance < 60: Defer optimization to Phase 2; content quality matters more than performance scores at launch

**Record scores**:
- Homepage: Performance ___ / Accessibility ___ / Best Practices ___ / SEO ___
- Module page: Performance ___ / Accessibility ___ / Best Practices ___ / SEO ___

**Result**: [ ] GREEN [ ] YELLOW [ ] RED — Notes: ___________________

---

## Sign-Off and Go/No-Go Decision

Run date/time: ___________________________ UTC

Deployed URL verified: ___________________________

Platform: [ ] GitHub Pages [ ] Netlify [ ] Vercel [ ] Other: ___________

| Check | Result | Notes |
|-------|--------|-------|
| 1. Homepage layout | | |
| 2. Module links (no 404s) | | |
| 3. Email signup form | | |
| 4. GA4 analytics firing | | |
| 5. Mobile responsive (3 sizes) | | |
| 6. Social preview (OG tags) | | |
| 7. Navigation menu | | |
| 8. Case study content complete | | |
| 9. Mobile hamburger menu | | |
| 10. Lighthouse scores | | |

### Go/No-Go for Phase 1 distribution

**GREEN (all 10 GREEN)**: Proceed immediately to Phase 1 distribution. Begin LinkedIn post and outreach sequence per `EMAIL_SOCIAL_FUNNEL_STRATEGY.md`.

**YELLOW (1-3 YELLOW, no RED)**: Proceed with Phase 1 distribution. Document YELLOW issues below and schedule resolution within 48 hours. YELLOW issues are cosmetic or non-blocking.

**RED (any RED on Checks 1, 2, 3, or 4)**: Resolve before any promotion or distribution. RED on Checks 1-4 means the site is broken for a core user experience: layout (1), content (2), email capture (3), or analytics (4).

**RED on Checks 5-10 only**: YELLOW-equivalent for Phase 1 purposes. These are important but do not prevent distribution. Schedule resolution for Week 1 post-launch.

---

### Phase 2 handoff trigger

Once all 10 checks are GREEN or YELLOW and distribution has begun:

1. Fill in `PHASE_2_HANDOFF_DOCUMENT.md` Section 1 with the deployment facts above
2. Set Day 7 reminder: review Week 1 baseline metrics in GA4 to make Phase 2 direction decision
3. Review `PHASE_2_3_EXECUTION_ROADMAP.md` Phase 2 critical path (10-17h: Kit setup, welcome sequence, automation)

Phase 2 activation is not time-gated — it triggers when Week 1 subscriber count and engagement data are in hand (Day 7 post-launch), as documented in `PHASE_2_HANDOFF_DOCUMENT.md` Section 3.

---

**Cross-reference**: `POST_DEPLOYMENT_VERIFICATION_CHECKLIST.md` contains the full 10-check verification with detailed diagnostic paths for each failure mode. This document adds the GREEN/YELLOW/RED decision framework, OG tags check (Check 6), and the Phase 2 handoff trigger.
