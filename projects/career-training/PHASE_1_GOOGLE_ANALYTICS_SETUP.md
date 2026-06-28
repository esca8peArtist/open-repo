---
title: "Phase 1 Google Analytics 4 Setup Specification"
project: career-training
phase: "1"
created: 2026-06-28
status: implementation-ready
---

# Phase 1 Google Analytics 4 Setup Specification

**Scope**: Complete GA4 configuration for the Construction Career Training GitHub Pages site. Written for implementation immediately before or immediately after the Phase 1 push. Covers property creation, Jekyll snippet integration, event tracking schema, custom dimensions for audience segmentation, and conversion goals.

**Implementation window**: Complete before or within 24 hours of the first GitHub Pages push. Every day without GA4 is traffic data you cannot recover retroactively.

---

## Part 1: Property Creation

### 1.1 Create the GA4 Property

1. Go to [analytics.google.com](https://analytics.google.com) and sign in with your Google account
2. Click "Admin" (gear icon, bottom-left)
3. Under "Account", click "Create Account" if you do not already have a Google Analytics account. Name it "Construction Career Training"
4. Under "Property", click "Create Property"
5. Property name: `Construction Career Training — Phase 1`
6. Reporting time zone: `United States — Pacific Time` (California-focused content)
7. Currency: `US Dollar`
8. Click "Next" and select industry category: `Education`
9. Business size: `Small`
10. Click "Create"

### 1.2 Create a Web Data Stream

After property creation, GA4 prompts you to add a data stream:

1. Select "Web"
2. Website URL: Your GitHub Pages URL (e.g., `https://yourusername.github.io/career-training` or `https://constructiontrainingpath.com` if using a custom domain)
3. Stream name: `GitHub Pages — Production`
4. Leave "Enhanced Measurement" ON — it automatically tracks scroll depth, outbound link clicks, file downloads, and page views without additional code
5. Click "Create Stream"
6. Copy the **Measurement ID** (format: `G-XXXXXXXXXX`) — you will need this for the Jekyll snippet

### 1.3 Add GA4 Snippet to Jekyll

The snippet must go in the `<head>` of every page. For a Just the Docs theme site, the correct file is either:

- `docs/_includes/head_custom.html` (Just the Docs' override hook — preferred)
- `docs/_layouts/default.html` (if you have a custom layout)

Create `docs/_includes/head_custom.html` with this content (replace `G-XXXXXXXXXX` with your Measurement ID):

```html
<!-- Google Analytics 4 — Career Training Phase 1 -->
{% if jekyll.environment == "production" %}
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX', {
    'custom_map': {
      'dimension1': 'user_segment',
      'dimension2': 'learning_path',
      'dimension3': 'module_number'
    }
  });
</script>
{% endif %}
```

The `jekyll.environment == "production"` guard prevents GA from firing on local builds and polluting your data with development traffic. GitHub Pages sets `JEKYLL_ENV=production` automatically.

**If you do not want the production guard** (simpler, fire always):

```html
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-XXXXXXXXXX');
</script>
```

---

## Part 2: Event Tracking Schema

These are the specific, measurable events you need for Phase 1 data quality. Every event has a name, parameters, and a trigger. "Engagement" events with no specifics are excluded — each event here maps to a decision you will actually make in Phase 2.

### 2.1 Module View Events

**Event name**: `module_view`

**What it answers**: Which modules are being read? Which are ignored? Which paths are most active?

**Parameters**:
- `module_number` (string): "01", "02", etc.
- `module_title` (string): "Foundations — Contracts & Estimating"
- `learning_path` (string): "residential", "industrial", "specialty-sub", or "unassigned"
- `module_phase` (string): "phase-1", "phase-2", etc. (Phase 1 = Modules 1-4, Phase 2 = 5-8, etc.)

**Implementation**: Add this script to each module page template, or fire it from the Jekyll front matter via a JavaScript block in `_layouts/module.html`:

```javascript
// Add to each module page, or to _layouts/module.html using page variables
document.addEventListener('DOMContentLoaded', function() {
  if (typeof gtag === 'function') {
    gtag('event', 'module_view', {
      'module_number': '{{ page.module_number }}',
      'module_title': '{{ page.title }}',
      'learning_path': '{{ page.learning_path | default: "unassigned" }}',
      'module_phase': '{{ page.module_phase | default: "phase-1" }}'
    });
  }
});
```

Add `module_number`, `learning_path`, and `module_phase` to the YAML front matter of each module file. Example for Module 01:

```yaml
---
layout: module
title: "Foundations — Contracts & Estimating"
module_number: "01"
learning_path: "residential,industrial,specialty-sub"
module_phase: "phase-1"
nav_order: 1
---
```

**Minimum viable version** (if front matter additions are too time-consuming at launch): Enable GA4 Enhanced Measurement's "Page views" — it will record URL paths. You can filter `/modules/01-*` in GA4 without custom events. Custom events add precision; they are not required for basic module-view data.

### 2.2 Case Study Click Events

**Event name**: `case_study_click`

**What it answers**: Are visitors engaging with the 150-scenario workbook? Which case studies get the most interaction?

**Parameters**:
- `case_study_id` (string): "cs-001", "cs-042", etc.
- `case_study_topic` (string): "lien-rights", "schedule-delay", "change-order", etc.
- `source_page` (string): Which module page the click originated from

**Implementation**: Add `onclick` handlers to case study links in the workbook:

```html
<a href="/case-studies/scenarios#cs-042"
   onclick="gtag('event', 'case_study_click', {
     'case_study_id': 'cs-042',
     'case_study_topic': 'change-order',
     'source_page': window.location.pathname
   });">
  Scenario 42: The Scope Creep Response
</a>
```

**Alternative (zero-code)**: GA4 Enhanced Measurement tracks all outbound link clicks and internal link clicks with the `click` event. You can filter by `link_url` containing `/case-studies` in GA4 Explorations without adding onclick handlers. Less granular, but sufficient for Phase 1.

### 2.3 Email Signup Conversion Events

**Event name**: `email_signup_conversion`

**What it answers**: Which pages drive the most email signups? Which Kit form variant converts best? What is the overall list growth rate?

**Parameters**:
- `form_variant` (string): "residential-gc", "industrial-gc", "specialty-sub", "generic-homepage"
- `signup_page` (string): URL of the page where signup occurred
- `cta_placement` (string): "above-fold", "inline-module", "bottom-of-page", "quick-start-page"

**Implementation via Kit webhook**: Kit can fire a redirect URL or POST webhook on form submit. Configure Kit form success action to redirect to a thank-you page:

1. In Kit form settings, set "Success action" to "Redirect to URL"
2. Redirect URL: `https://yoursite.com/signup-thank-you?form=residential-gc`
3. Create `docs/signup-thank-you.md` with a GA4 event fire on page load:

```html
<script>
document.addEventListener('DOMContentLoaded', function() {
  // Extract form variant from URL parameter
  const params = new URLSearchParams(window.location.search);
  const formVariant = params.get('form') || 'unknown';
  
  if (typeof gtag === 'function') {
    gtag('event', 'email_signup_conversion', {
      'form_variant': formVariant,
      'signup_page': document.referrer,
      'cta_placement': params.get('placement') || 'unknown'
    });
    // Also fire as a GA4 conversion
    gtag('event', 'conversion', {
      'send_to': 'G-XXXXXXXXXX/email_signup'
    });
  }
});
</script>
```

**Mark as conversion in GA4**: In GA4 Admin > Events, find `email_signup_conversion` and toggle "Mark as conversion" ON. This makes it appear in the Conversions report and enables funnel analysis.

### 2.4 Learning Path Selection Events

**Event name**: `path_selection`

**What it answers**: Which path is most popular? Are visitors who select a path more likely to sign up?

**Parameters**:
- `path_selected` (string): "residential", "industrial", "specialty-sub"
- `selection_source` (string): "homepage-cta", "quick-start-guide", "path-page"

**Implementation**: Add to path CTA links:

```html
<a href="/navigation/residential-path"
   onclick="gtag('event', 'path_selection', {
     'path_selected': 'residential',
     'selection_source': 'homepage-cta'
   });">
  Start Residential Path →
</a>
```

### 2.5 Navigation Depth Event

**Event name**: `navigation_depth`

**What it answers**: How deep into the curriculum do visitors get before leaving? This is a proxy for interest-without-conversion.

**Implementation**: GA4 Enhanced Measurement handles scroll depth automatically (`scroll` event at 90% scroll depth). For navigation depth (how many pages in a session), use GA4's "Session depth" dimension in Explorations — no custom event needed.

---

## Part 3: Custom Dimensions for Cohort Segmentation

GA4 custom dimensions let you segment users by the categories that matter for this project. Register these in GA4 Admin > Custom Definitions.

### 3.1 Register Custom Dimensions

In GA4 Admin > Property > Custom definitions > Create custom dimension:

| Dimension Name | Scope | Event Parameter | Description |
|---|---|---|---|
| `User Segment` | User | `user_segment` | instructor / learner / contractor (set at Kit signup; not available in GA4 until linked) |
| `Learning Path` | Event | `learning_path` | residential / industrial / specialty-sub / unassigned |
| `Module Number` | Event | `module_number` | 01 through 36 |
| `Form Variant` | Event | `form_variant` | Which Kit form drove the signup |
| `CTA Placement` | Event | `cta_placement` | Where on page the signup or path-click occurred |

**Note on user_segment**: GA4 cannot read Kit subscriber tags directly. The `user_segment` dimension will only be populated if you (a) add a URL parameter to Kit email links (e.g., `?segment=instructor`) and fire it as a custom dimension on page load, or (b) build a GA4 Audience based on behavioral proxies. See Section 4 for behavioral proxies.

### 3.2 Audience Definitions (Behavioral Proxies for Segmentation)

Since you cannot pass Kit subscriber tags to GA4 directly without server-side infrastructure, use GA4 Audiences to approximate the instructor / learner / contractor segmentation:

**Audience: Probable Instructors**
- Condition: User visited `/instructor-guide/` OR `/navigation/faq` AND session duration > 3 minutes
- Reasoning: Only instructors navigate the instructor guide; extended time suggests content evaluation

**Audience: Active Module Learners**
- Condition: User triggered `module_view` event 3+ times across sessions
- Reasoning: 3+ distinct module views indicates curriculum use, not accidental arrival

**Audience: Probable Contractors (GC Path)**
- Condition: User visited any of: Module 12 (GC Business Setup), Module 13 (Construction Law), Module 9 (Codes & Permits), Module 25 (Construction Finance)
- Reasoning: These modules address GC business operations — the contractor-as-student use case

**Audience: High-Intent Visitors**
- Condition: User triggered `path_selection` event AND session duration > 5 minutes
- Reasoning: Path selection + extended session = motivated visitor

---

## Part 4: Conversion Goals

Set these four as GA4 Conversions (Admin > Events > mark as conversion):

| Goal Name | GA4 Event | Business Question It Answers |
|---|---|---|
| Email List Signup | `email_signup_conversion` | Primary growth metric — is the site capturing leads? |
| Path Selection | `path_selection` | Is the homepage CTA working? Are visitors choosing a path? |
| Module View (3+) | Create via Audience | Are visitors actually reading the curriculum? |
| Case Study Click | `case_study_click` | Is the 150-scenario workbook driving engagement? |

**Setting a conversion**: GA4 Admin > Events > find event name > toggle "Mark as conversion" to blue.

---

## Part 5: Verification Checklist

Complete before confirming analytics are live:

- [ ] GA4 property created; Measurement ID (`G-XXXXXXXXXX`) copied
- [ ] Snippet added to `docs/_includes/head_custom.html`
- [ ] Commit and push `head_custom.html` to repo
- [ ] Visit live site; open browser DevTools > Network tab; filter for `google-analytics` or `gtag` — confirm GA4 requests fire on page load
- [ ] In GA4 > Reports > Realtime: visit site; confirm your own session appears as an active user
- [ ] Trigger each custom event manually (click a case study link, click a path CTA) and verify in Realtime > Events
- [ ] Custom dimensions registered (Admin > Custom definitions)
- [ ] `email_signup_conversion` marked as conversion
- [ ] `path_selection` marked as conversion
- [ ] GA4 Enhanced Measurement ON (scroll, outbound clicks, file downloads)
- [ ] Google Search Console property created; sitemap submitted (separate from GA4 but do it same session)

---

## Part 6: Google Search Console Setup (Do at Same Time)

Search Console is separate from GA4 but equally important — it shows organic search traffic, keyword queries, and indexing status.

1. Go to [search.google.com/search-console](https://search.google.com/search-console)
2. Add property > "URL prefix" > enter your GitHub Pages URL
3. Verify via Google Analytics (if GA4 is already connected to same Google account, verification is automatic)
4. Submit sitemap: in Search Console, go to Sitemaps > enter `sitemap.xml` > Submit
   - Jekyll-sitemap plugin generates `sitemap.xml` automatically if it is in `_config.yml` plugins list (it is, per the current `_config.yml`)
5. Request indexing for the homepage: URL Inspection > enter homepage URL > Request Indexing

**Expected**: First organic search traffic in 2-4 weeks. Do not expect immediate indexing.

---

## Sources

- [GA4 Setup for Jekyll and GitHub Pages — Google Developers](https://developers.google.com/analytics/devguides/collection/ga4)
- [GA4 Custom Dimensions and Metrics — Google Analytics Help](https://support.google.com/analytics/answer/10075209)
- [GA4 Enhanced Measurement — Google Analytics Help](https://support.google.com/analytics/answer/9216061)
- [Just the Docs — Custom Includes — GitHub](https://just-the-docs.github.io/just-the-docs/docs/customization/)
- [GA4 Conversion Events — Google Analytics Help](https://support.google.com/analytics/answer/9267568)
