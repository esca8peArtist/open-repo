---
title: "WCAG 2.1 AA Audit Checklist — open-repo Phase 5.2 Wave 2"
project: open-repo
phase: "5.2"
wave: 2
candidate: 3-A11y
status: ready-for-execution
audit_target: "WCAG 2.1 Level AA"
execution_window: "June 1–6, 2026"
created: 2026-05-27
---

# WCAG 2.1 AA Audit Checklist
## open-repo Phase 5.2 Wave 2 — A11y Audit

**Compliance target**: WCAG 2.1 Level AA (W3C Recommendation, June 2018)
**Audit scope**: All HTML surfaces produced or served by open-repo:
- ZIM export HTML templates (rendered inside Kiwix WebView)
- REST API response pages (admin, health, error pages)
- OPDS catalog endpoints (UI, if any)
- Any web-rendered content at `/`, `/admin/`, `/api/` routes

**Severity mapping** used throughout this document:
- WCAG Level A failure = **P0** (blocking; must fix before release)
- WCAG Level AA failure = **P1** (high-impact; fix by Day 5 of audit window)
- WCAG Level AAA / enhancement = **P2** (nice-to-have; backlog)

**Time estimate**: Running the full checklist takes 4–6 hours. Automated sections take ~1 hour; manual sections take 3–5 hours depending on content depth.

---

## Section 1: Keyboard Navigation

Keyboard-only navigation is a WCAG 2.1 Level A requirement. Users who cannot use a mouse (motor impairment, power users) must be able to operate all interactive elements with Tab, Shift+Tab, Enter, Space, and arrow keys alone.

**Setup for manual keyboard testing:**
1. Disconnect or disable your mouse/trackpad
2. Open the page in Firefox or Chrome
3. Press Tab repeatedly to traverse focusable elements
4. Document every element that cannot be reached, activated, or exited with keyboard alone

### 1.1 Tab Order (WCAG 2.1.1 — Level A → P0)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| All interactive elements reachable by Tab | Every button, link, input, select, and form control receives keyboard focus | Tab through entire page; verify each interactive element is reached | |
| Tab order is logical | Focus moves in a predictable reading order (top-to-bottom, left-to-right or following DOM order) | Tab 20+ times; confirm focus sequence matches visual flow | |
| No keyboard trap | Focus can always leave any widget or component with standard key (Tab/Shift+Tab/Esc) | Tab into every modal, popup, dropdown, and embedded widget; verify Esc or Tab exits cleanly | |
| `tabindex` values are valid | No `tabindex` value other than `-1` or `0` is used without explicit justification | `grep -r "tabindex" app/templates/ && grep -r "tabindex" app/static/` | |
| Skip navigation link present | A "Skip to main content" link is the first focusable element on every page | Tab once from page load; "Skip to main content" should be first focus target | |

### 1.2 Focus Visibility (WCAG 2.4.7 — Level AA → P1)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Focus indicator visible on all elements | Every focused element has a visible outline or highlight with 3:1 contrast ratio vs. background | Tab through all elements; verify visible ring/outline on each | |
| No CSS `outline: none` without replacement | Any element with `outline: none` must have an alternative visible focus style | `grep -r "outline: none\|outline:none" app/static/` | |
| Focus visible on custom components | Custom dropdowns, sliders, toggles show visible focus state | Tab into each custom widget; verify focus indicator present | |

### 1.3 Keyboard Operation of Components (WCAG 2.1.1 — Level A → P0)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Buttons activatable with Enter and Space | Any `<button>` or `role="button"` activates with both Enter and Space | Focus button with Tab; press Enter; press Space; both should trigger action | |
| Links activatable with Enter | `<a>` elements activate with Enter | Focus link; press Enter; should navigate | |
| Dropdowns/selects operable with arrows | `<select>` elements respond to arrow keys for option navigation | Focus select; press Down arrow; options should cycle | |
| Modal dialogs: focus stays inside | When a modal/dialog opens, keyboard focus is constrained inside it until closed | Open any modal; Tab; focus must not escape to background page | |
| Carousel/slider: arrow key operation | Any carousel or image slider responds to arrow keys | Focus carousel controls; press left/right arrow; slides should advance | |

**Axe-core rule tags for this section**: `keyboard`, `tabindex`, `focus-trap`

**Auto-audit command** (run from backend/ directory):
```bash
# Install axe-puppeteer for CLI automation
npx axe http://127.0.0.1:8000 --tags keyboard --reporter json > reports/keyboard_axe.json
```

---

## Section 2: Screen Reader Compatibility

Screen readers convert HTML structure into speech. WCAG requires that all information conveyed visually is also conveyed semantically (through markup, ARIA, or alt text).

**Setup for manual screen reader testing:**
- Linux: Install [Orca](https://help.gnome.org/users/orca/stable/) (`sudo apt install gnome-orca`)
- Windows: Download [NVDA](https://www.nvaccess.org/download/) (free) or use JAWS (licensed)
- Android: Enable TalkBack under Accessibility settings
- Testing sequence: Open page → enable screen reader → navigate with H (headings), B (buttons), F (form fields), T (tables), arrow keys

### 2.1 Image Alt Text (WCAG 1.1.1 — Level A → P0)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| All informative images have descriptive alt text | `alt` attribute describes the image content meaningfully (not "image" or filename) | Review 30–50 article images from ZIM exports; verify alt text on each | |
| Decorative images have empty alt text | Pure decorative images use `alt=""` (empty string, not missing) | `grep -n 'alt=' app/templates/` — look for missing alt or `alt="image"` | |
| No images of text | No text is rendered purely as an image without a text equivalent | Visual scan of all pages for bitmap text; check logo images for alt | |
| Complex images have extended description | Charts, diagrams, maps have either longdesc or adjacent text description | Identify any complex graphics; verify descriptive text is adjacent or linked | |
| Input images have alt text | `<input type="image">` elements have descriptive alt | `grep -n 'type="image"' app/templates/` | |

**Axe-core rules**: `image-alt`, `input-image-alt`, `area-alt`

**Auto-audit command**:
```bash
npx axe http://127.0.0.1:8000 --tags wcag2a --include '#main-content' --reporter json > reports/images_axe.json
```

### 2.2 ARIA Labels and Roles (WCAG 1.3.1, 4.1.2 — Level A → P0)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| All interactive elements have accessible names | Buttons, links, form controls have visible label text or `aria-label` or `aria-labelledby` | `grep -n 'aria-label\|aria-labelledby' app/templates/` — verify coverage of all controls | |
| Icon buttons have ARIA labels | Buttons with only an icon (no text) have `aria-label` describing the action | Identify icon-only buttons; verify `aria-label` attribute present | |
| ARIA roles match element usage | `role=` attributes match the element's actual behavior (e.g., `role="button"` only on elements that behave as buttons) | Code review of all `role=` attributes in templates | |
| No invalid ARIA attribute usage | ARIA attributes are valid for their host element | axe-core rule `aria-allowed-attr` catches this automatically | |
| aria-live regions for dynamic content | Areas that update dynamically (status messages, search results, alerts) use `aria-live` | Identify all content that changes without page reload; verify `aria-live` attribute | |

**Axe-core rules**: `aria-required-attr`, `aria-valid-attr`, `aria-allowed-attr`, `button-name`, `link-name`

### 2.3 Heading Structure (WCAG 1.3.1 — Level A → P0)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Single `<h1>` per page | Exactly one `<h1>` element per page; it identifies the page topic | `grep -c '<h1' template.html` — must equal 1 | |
| No heading level skips | Headings descend without skipping levels: h1→h2→h3, never h1→h3 | Screen reader H-key navigation; WAVE tool heading map | |
| Heading text is descriptive | Headings describe the section content, not generic ("Section 1", "Click here") | Read all headings aloud; each should make sense out of context | |
| No visual headings using bold/large text | Text styled to look like headings must be marked as actual heading elements | Visual comparison: any large/bold text that is not a heading element? | |

**WAVE tool**: Navigate to `http://wave.webaim.org/` → enter page URL → view "Structural Elements" tab for heading map

**Auto-audit command**:
```bash
npx axe http://127.0.0.1:8000 --tags wcag2a --include 'h1,h2,h3,h4,h5,h6' --reporter json > reports/headings_axe.json
```

---

## Section 3: Color Contrast

Color contrast is one of the most common WCAG failures. WCAG 2.1 AA requires a minimum contrast ratio of 4.5:1 for normal text and 3:1 for large text (18pt or 14pt bold).

**Tools required:**
- [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/) — manual color pair entry
- [WAVE Tool](https://wave.webaim.org/) — automated page scan
- Browser DevTools → Inspector → color picker (shows hex values)
- axe-core `color-contrast` rule

### 3.1 Normal Text Contrast (WCAG 1.4.3 — Level AA → P1)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Body text vs. background ≥ 4.5:1 | Main article text achieves 4.5:1 contrast ratio | Extract foreground/background hex from CSS; enter into WebAIM checker | |
| Link text vs. background ≥ 4.5:1 | Unvisited and visited link colors achieve 4.5:1 | Check `a { color: }` and `a:visited { color: }` in CSS | |
| Placeholder text ≥ 4.5:1 | Input placeholder text (often gray) achieves 4.5:1 vs. white background | Inspect `::placeholder` CSS rule; check contrast | |
| Navigation link text ≥ 4.5:1 | Nav bar links achieve 4.5:1 vs. nav background color | Check nav CSS background-color and link color | |
| Footer link text ≥ 4.5:1 | Footer links (common failure: light gray on white) achieve 4.5:1 | Check footer CSS; footer links are a common gray-on-white failure | |
| Error message text ≥ 4.5:1 | Red error messages achieve 4.5:1 vs. white (pure red #FF0000 on white = 3.99:1, FAILS) | Extract error message color from CSS; verify ratio | |

**Note on red-on-white failure**: Pure red (#FF0000) on white (#FFFFFF) gives a contrast ratio of 3.99:1, which **fails** WCAG AA for normal text. Use a darker red (#C62828 or similar) to achieve 4.5:1.

### 3.2 Large Text Contrast (WCAG 1.4.3 — Level AA → P1)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Heading text (h1–h3) ≥ 3:1 | Large headings (≥18pt/24px or ≥14pt/18.67px bold) achieve 3:1 contrast | Measure heading font size from CSS; use 3:1 threshold if large | |
| Call-to-action buttons ≥ 3:1 | Large button text achieves 3:1 ratio | Check button background vs. button text color | |

### 3.3 UI Component Contrast (WCAG 1.4.11 — Level AA → P1)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Form input borders ≥ 3:1 | Text field, checkbox, radio borders achieve 3:1 vs. background | Inspect input border color; verify ratio against page background | |
| Focus indicator ≥ 3:1 | Focus ring or highlight achieves 3:1 vs. adjacent colors | Inspect `:focus` CSS styles; measure focus color contrast | |
| Active/selected state indicators ≥ 3:1 | Selected tab, active nav item, toggled checkbox indicate state with ≥3:1 contrast change | Check state-indicator CSS (border, background, checkmark) | |

**Auto-audit command**:
```bash
npx axe http://127.0.0.1:8000 --tags wcag2aa --include 'body' --reporter json > reports/contrast_axe.json
# Or use Lighthouse for a scored contrast report:
npx lighthouse http://127.0.0.1:8000 --only-categories=accessibility --output json --output-path reports/lighthouse_contrast.json
```

---

## Section 4: Semantic Markup

Semantic HTML gives assistive technology the structure it needs to interpret content correctly. Structural failures often look fine visually but break completely for screen reader users.

### 4.1 Document Structure (WCAG 1.3.1 — Level A → P0)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| `<html lang="...">` present | Root `<html>` element has `lang` attribute with BCP 47 language code (e.g., `lang="en"`) | `grep -n '<html' app/templates/base.html` | |
| `<title>` element is descriptive | Page `<title>` is unique and describes the page content; not generic ("Page" or "Open-Repo") | `grep -n '<title>' app/templates/` — verify unique and descriptive | |
| `<main>` landmark present | Exactly one `<main>` element per page wrapping primary content | `grep -c '<main' base.html` — must equal 1 | |
| `<nav>` landmark wraps navigation | Primary navigation is inside a `<nav>` element; supplementary navs use `aria-label` | `grep -n '<nav' base.html` | |
| `<header>` and `<footer>` present | Page header and footer use semantic elements | `grep -n '<header\|<footer' base.html` | |
| Lists use `<ul>/<ol>/<li>` | Collections of items are marked as lists, not `<div>` sequences | Review all navigation menus, bullet lists; verify `<ul>/<ol>` markup | |
| Tables have `<caption>` and `<th>` | Data tables have `<caption>` identifying the table and `<th scope="...">` for column/row headers | `grep -n '<table' app/templates/` — verify each table's header markup | |

### 4.2 Form Associations (WCAG 1.3.1, 3.3.2 — Level A → P0)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Every `<input>` has an associated `<label>` | Each input field has a `<label for="input-id">` with matching `id`, or uses `aria-label` | `grep -n '<input\|<label' app/templates/` — verify every input has a label | |
| `<textarea>` has associated label | Text areas have a visible label with `for`/`id` association | Same as above | |
| `<select>` has associated label | Select dropdowns have a visible label | Same as above | |
| Required fields marked | Mandatory fields are marked with `required` attribute or `aria-required="true"` | `grep -n 'required' app/templates/` | |
| Group inputs wrapped in `<fieldset>/<legend>` | Related radio buttons and checkboxes are wrapped in `<fieldset>` with `<legend>` | Check any radio group or checkbox group in forms | |

### 4.3 OPDS XML Endpoint Semantics (open-repo specific)

The OPDS endpoints (`/opds/v2/root.xml`, `/opds/v2/entries`) return Atom XML, not HTML. Accessibility of XML is interpreted differently: the concern is screen-reader-accessible display within Kiwix's WebView.

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Kiwix WebView renders ZIM HTML accessibly | ZIM content opens in Kiwix and is navigable by screen reader | Enable TalkBack (Android) or VoiceOver (iOS); open ZIM; navigate with swipe | |
| ZIM article headings use `<h1>–<h6>` | Article templates in ZIM exports use proper heading markup | Inspect generated HTML in `app/services/export/zim_writer.py` template | |
| ZIM image alt text generated | ZimWriter generates `alt` attributes for embedded images | Code review: `zim_writer.py` — verify `alt=` in image HTML generation | |

---

## Section 5: Form Accessibility

Forms are high-risk for accessibility failures. Error messages, required fields, and validation feedback all require specific markup.

### 5.1 Error Messages (WCAG 3.3.1, 3.3.3 — Level A/AA → P0/P1)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Errors described in text, not color alone | Error state must be conveyed by text or icon, not only by red color | Submit form with errors; verify error message text appears (not just red highlight) | |
| Error messages associated with field | Error text is adjacent to or programmatically associated with the offending field | Error message must be inside `<label>`, adjacent to input, or reference input via `aria-describedby` | |
| Error messages are specific | Errors say what is wrong and how to fix it ("Email must include @", not "Invalid input") | Trigger each validation error; read the error text | |
| Successful submissions confirmed | Success state has a text confirmation message visible to screen readers | Submit valid form; verify success message is visible and announced by screen reader | |
| Error summary provided on multi-field forms | If multiple fields fail, a summary list of errors appears at the top of the form | Submit multi-field form with several errors; verify summary block | |

### 5.2 Auto-complete and Input Assistance (WCAG 1.3.5 — Level AA → P1)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Name, email, password fields have autocomplete attribute | Personal data inputs include `autocomplete` attribute with the appropriate token | `grep -n 'autocomplete' app/templates/` — verify `name`, `email`, `username`, `current-password` etc. | |
| No session timeout without warning | If a form session times out, users are warned with at least 20 seconds to extend | Check for any session timeout behavior on admin forms | |

---

## Section 6: Performance and Load Time

WCAG 2.1 does not directly mandate performance benchmarks, but slow-loading content creates functional barriers for users with cognitive disabilities, users on limited hardware, and users on assistive technology that has its own processing overhead.

**Industry standard**: The open-repo Wave 1 OPDS specification already requires OPDS endpoints to respond in <2 seconds. The same threshold applies here to all HTML pages.

### 6.1 Page Load Performance (WCAG 2.2.1, 2.2.2 — Level A → P0)

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Pages load in <3 seconds on broadband | Initial page load completes in under 3 seconds on a 10 Mbps connection | Lighthouse performance score; check LCP metric | |
| ZIM content loads in <2 seconds | Kiwix renders ZIM articles in under 2 seconds on Pi 5 hardware | Time open ZIM in Kiwix on Pi 5; measure from tap to visible content | |
| OPDS endpoints respond in <2 seconds | `/opds/v2/root.xml`, `/opds/v2/entries`, `/opds/v2/search` respond in <2 seconds | `curl -o /dev/null -w "%{time_total}" http://127.0.0.1:8000/opds/v2/root.xml` | |
| No content autoplay without user control | Animated content, video, or audio that plays automatically has a pause/stop control | Visual scan all pages for autoplaying media | |
| No flashing content | No content flashes more than 3 times per second (seizure risk) | Visual scan; check CSS animations; verify no flash frequency >3Hz | |

### 6.2 Asset and Rendering Efficiency

| Check | Pass Criteria | How to Test | Result |
|-------|--------------|-------------|--------|
| Images are appropriately sized | Images are served at display dimensions, not downloaded oversized then scaled | DevTools Network tab: image download size vs. display size | |
| Critical CSS is inline or fast-loading | First Contentful Paint is not blocked by render-blocking CSS | Lighthouse "Eliminate render-blocking resources" audit | |
| No long JavaScript task blocking interaction | Time to Interactive (TTI) ≤ 5 seconds | Lighthouse performance audit; check TTI metric | |

**Lighthouse audit command** (automated performance + accessibility combined):
```bash
npx lighthouse http://127.0.0.1:8000 \
  --only-categories=accessibility,performance \
  --chrome-flags="--headless --no-sandbox --disable-gpu" \
  --output html \
  --output-path reports/lighthouse_full.html
```

---

## Auto-Audit Tools Reference

### Tool 1: axe-core (Deque Systems)
- **What it catches**: 80+ WCAG A/AA rules; automated DOM analysis
- **Coverage**: ~30–57% of all accessibility issues (manual testing required for the rest)
- **Install**: `npm install -D axe-core axe-puppeteer`
- **Documentation**: [axe-core GitHub](https://github.com/dequelabs/axe-core)
- **WCAG tags**: Use `wcag2a`, `wcag2aa`, `wcag21a`, `wcag21aa` to filter rules by compliance level
- **Run command**: `npx axe URL --tags wcag2a,wcag2aa --reporter json > axe_report.json`

### Tool 2: Lighthouse (Google)
- **What it catches**: Accessibility + performance + best practices scored 0–100
- **Coverage**: Accessibility score reflects subset of WCAG; not exhaustive
- **Install**: `npm install -g lighthouse` (or use Chrome DevTools built-in)
- **Documentation**: [Lighthouse CI](https://github.com/GoogleChrome/lighthouse-ci)
- **Run command**: `npx lighthouse URL --only-categories=accessibility --output json`
- **CI integration**: `@lhci/cli` for GitHub Actions (LHCI 0.15.x uses Lighthouse 12.6.1 as of 2026)

### Tool 3: WAVE (WebAIM)
- **What it catches**: Visual overlay of errors, alerts, structural elements, contrast issues
- **Coverage**: Good for structural and semantic markup; visual output aids manual interpretation
- **URL**: [https://wave.webaim.org/](https://wave.webaim.org/)
- **Chrome extension**: [WAVE Evaluation Tool](https://chrome.google.com/webstore/detail/wave-evaluation-tool/jbbplnpkjmmeebjpijfedlgcdilocofh)
- **Best for**: Heading map visualization, form label detection, quick manual review

### Tool 4: WebAIM Contrast Checker
- **What it checks**: Contrast ratio for a specific foreground/background color pair
- **URL**: [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)
- **Use for**: Verifying Section 3 color contrast checks with specific hex codes

### Tool 5: Pa11y (CLI)
- **What it catches**: WCAG 2.1 AA; runs via Puppeteer; good for batch URL scanning
- **Install**: `npm install -g pa11y`
- **Run command**: `pa11y --standard WCAG2AA --reporter json http://127.0.0.1:8000 > pa11y_report.json`
- **Documentation**: [Pa11y GitHub](https://github.com/pa11y/pa11y)

---

## Manual Testing Procedures

### Screen Reader Testing — Orca (Linux) Step-by-Step

1. Install: `sudo apt install gnome-orca`
2. Start: `orca` (or enable from System Settings → Accessibility)
3. Open Firefox; navigate to `http://127.0.0.1:8000`
4. Orca reads page title aloud — verify it is descriptive
5. Press `H` to cycle through headings — verify logical structure, no level skips
6. Press `F` to cycle through form fields — verify each field is announced with its label
7. Press `B` to cycle through buttons — verify each button's purpose is announced
8. Press `K` to cycle through links — verify link text is meaningful (not "click here")
9. Press `T` to cycle through tables — verify column headers are announced
10. Document any element announced as "blank", "unlabeled button", or "graphic" without description

**Pass criteria**: Screen reader announces meaningful text for every interactive element and heading. No "unlabeled" or "blank" announcements on elements with visual labels.

### Keyboard-Only Navigation Step-by-Step

1. Disconnect mouse
2. Navigate to `http://127.0.0.1:8000`
3. Press Tab 30 times; document every element focused in order
4. Verify sequence is logical (not jumping from footer to header mid-page)
5. Press Enter on every button encountered; verify expected action occurs
6. Press Esc on any modal or overlay that opens; verify focus returns to trigger element
7. Fill in any forms using keyboard only; submit; verify success/error messages appear

**Pass criteria**: All interactive elements reachable; all actions completable; all dialogs escapable; all feedback visible.

### Color Contrast Visual Inspection Step-by-Step

1. Open the page in Chrome
2. Open DevTools (F12) → Inspector
3. Click on body text; DevTools shows the computed CSS color
4. Note the hex value for color and background-color
5. Enter both into [https://webaim.org/resources/contrastchecker/](https://webaim.org/resources/contrastchecker/)
6. Verify ratio ≥ 4.5:1 for normal text, ≥ 3:1 for large text
7. Repeat for: navigation links, footer links, error text, placeholder text, button text

---

## Severity Mapping Summary

| WCAG Level | Severity | Priority | Fix By |
|------------|----------|----------|--------|
| Level A failure | Critical | P0 | Day 3 of audit window (June 4) |
| Level AA failure | High | P1 | Day 5 of audit window (June 6) |
| Level AAA / enhancement | Low | P2 | Phase 6 backlog |

**P0 examples**: Missing alt text on images, keyboard trap, missing form labels, page language not set
**P1 examples**: Color contrast below 4.5:1, missing focus indicator, heading level skips, placeholder text contrast
**P2 examples**: Enhanced color contrast (7:1), pronunciation guides, cognitive simplification

---

## Sources

- [WCAG 2.1 — W3C Recommendation](https://www.w3.org/TR/WCAG21/)
- [WCAG 2.1 AA Compliance Checklist (WebAbility 2026)](https://www.webability.io/blog/wcag-2-1-aa-the-standard-for-accessible-web-design)
- [axe-core GitHub — Deque Systems](https://github.com/dequelabs/axe-core)
- [WebAIM Color Contrast Checker](https://webaim.org/resources/contrastchecker/)
- [WAVE Evaluation Tool](https://wave.webaim.org/)
- [Pa11y CLI Accessibility Testing](https://github.com/pa11y/pa11y)
- [Lighthouse CI Documentation](https://github.com/GoogleChrome/lighthouse-ci)
- [Playwright Accessibility Testing Documentation](https://playwright.dev/docs/accessibility-testing)
- [DWP Accessibility Manual — axe-core and Pa11y](https://accessibility-manual.dwp.gov.uk/best-practice/automated-testing-using-axe-core-and-pa11y)
