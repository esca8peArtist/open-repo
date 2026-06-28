---
title: "Phase 1 A/B Testing Framework — Landing Page Variants"
project: career-training
phase: "1"
created: 2026-06-28
status: implementation-ready
---

# Phase 1 A/B Testing Framework — Landing Page Variants

**Scope**: Structured A/B testing plan for the Phase 1 GitHub Pages homepage. Covers three CTA variant hypotheses, email signup placement tests, decision rules (when to stop tests, when to roll out winners), and a no-code implementation path compatible with GitHub Pages (no server required).

**Context**: The current homepage has a "choose your path" structure with three CTAs. Phase 1 data will determine which CTA framing drives the most path selections and email signups. This framework must run from static files with no backend — all measurement is via GA4 events.

---

## Core Testing Hypotheses

The three CTA framings represent different value propositions for different visitor motivations:

| Variant | CTA Text | Value Proposition | Predicted Best For |
|---|---|---|---|
| A (Control) | "Start with your path" / "Choose your path" | Curriculum access, structured learning | Learners who already know they want training |
| B | "Free module library — browse 33 modules" | Zero-commitment exploration, browsing | First-time visitors unsure about commitment |
| C | "Get certified — complete your path" | Credential / career advancement signal | Career changers, promotion-seekers |
| D | "Join the community — see what others are learning" | Social proof, belonging | Less experienced visitors who want peer validation |

**Starting with Variants A vs B vs C**: Test three variants simultaneously in Phase 1 (Weeks 1-4). Add Variant D only if traffic is sufficient to run 4-way test (see minimum traffic requirements below).

---

## Test 1: Homepage CTA Framing

### Hypothesis

Visitors who see "Free module library — browse 33 modules" (Variant B) will click a path CTA at a higher rate than visitors who see "Start with your path" (Variant A), because the word "free" and the specific module count (33) reduce the perceived commitment barrier before they have established trust.

### Variant Specifications

**Variant A (Control)** — Current homepage CTA block:

```markdown
## Choose Your Path

Ready to move into construction management or business ownership?

**[Quick Start Guide →](navigation/quick-start.md)** — Unsure which path? Start here.
**[All Modules →](navigation/module-quick-reference.md)** — Browse the full curriculum.
```

**Variant B — "Free module library"**:

```markdown
## Free Module Library — 33 Modules, No Signup Required

Every module is free to read. No account, no paywall, no trial.

**[Browse all 33 modules →](navigation/module-quick-reference.md)**
**[Or pick a path and start immediately →](navigation/quick-start.md)**
```

**Variant C — "Get certified"**:

```markdown
## Complete Your Path. Advance Your Career.

A structured program for construction professionals moving into GC, PM, or business ownership roles.

**[Start your learning path →](navigation/quick-start.md)**
**[View all 33 modules →](navigation/module-quick-reference.md)**
```

### Metrics

**Primary metric** (the one that determines the winner): `path_selection` event rate per session

**Secondary metrics** (directional, not decisive):
- `email_signup_conversion` rate per session (how many path-selectors also sign up)
- Bounce rate (GA4 "engagement rate" — sessions with 10+ seconds or 2+ page views)
- Average session duration on homepage

**Why `path_selection` is primary, not `email_signup`**: An email signup requires several steps after the CTA click (path selection → module engagement → signup form). The CTA's direct effect is path selection; email signup is 2-3 actions downstream and confounds CTA influence with module quality.

### Implementation (No-Code, Static Site)

GitHub Pages cannot serve different HTML variants to different users from the server. Two approaches work without a backend:

**Option 1: JavaScript URL-parameter routing (recommended)**

Add a query parameter to paid/social traffic links (`?v=b`, `?v=c`). The homepage JS reads the parameter and swaps the CTA block:

```javascript
// Add to docs/assets/js/ab-test.js
(function() {
  var params = new URLSearchParams(window.location.search);
  var variant = params.get('v') || 'a';
  
  // Store variant for the session
  if (!sessionStorage.getItem('ab_variant')) {
    sessionStorage.setItem('ab_variant', variant);
  } else {
    variant = sessionStorage.getItem('ab_variant');
  }
  
  // Fire variant assignment event to GA4
  if (typeof gtag === 'function') {
    gtag('event', 'ab_variant_assigned', {
      'test_name': 'homepage_cta_framing',
      'variant': variant
    });
  }
  
  // Swap CTA content based on variant
  document.addEventListener('DOMContentLoaded', function() {
    var ctaBlock = document.getElementById('homepage-cta');
    if (!ctaBlock) return;
    
    if (variant === 'b') {
      ctaBlock.innerHTML = `
        <h2>Free Module Library — 33 Modules, No Signup Required</h2>
        <p>Every module is free to read. No account, no paywall, no trial.</p>
        <p><a href="navigation/module-quick-reference.html" 
              onclick="gtag('event','path_selection',{'path_selected':'browse-all','selection_source':'homepage-cta-b'})">
          Browse all 33 modules →</a></p>
        <p><a href="navigation/quick-start.html"
              onclick="gtag('event','path_selection',{'path_selected':'quick-start','selection_source':'homepage-cta-b'})">
          Or pick a path and start immediately →</a></p>`;
    } else if (variant === 'c') {
      ctaBlock.innerHTML = `
        <h2>Complete Your Path. Advance Your Career.</h2>
        <p>A structured program for construction professionals moving into GC, PM, or business ownership roles.</p>
        <p><a href="navigation/quick-start.html"
              onclick="gtag('event','path_selection',{'path_selected':'quick-start','selection_source':'homepage-cta-c'})">
          Start your learning path →</a></p>
        <p><a href="navigation/module-quick-reference.html"
              onclick="gtag('event','path_selection',{'path_selected':'browse-all','selection_source':'homepage-cta-c'})">
          View all 33 modules →</a></p>`;
    }
    // Variant 'a' (control): no swap needed
  });
})();
```

Add `<div id="homepage-cta">` wrapper around the CTA block in `docs/index.md` (via raw HTML block in Markdown), and include the script in `head_custom.html` or at the bottom of `default.html`.

**Traffic assignment to variants**: Use UTM parameters in social/email traffic to assign variants:
- Organic/direct traffic: always Variant A (control)
- LinkedIn post 1: `?v=b` appended to link
- LinkedIn post 2: `?v=c` appended to link
- Email Day 7 social invite: `?v=b` or `?v=c` alternating by send date

This means you are not randomly assigning visitors — you are assigning by source. This creates a confounder (LinkedIn visitors may differ from direct visitors). Accept this for Phase 1 at low traffic volumes. If traffic reaches 500+/week, consider proper random assignment via a cookie-based approach.

**Option 2: Separate URLs (simpler, less elegant)**

Create `docs/index-b.md` and `docs/index-c.md` as separate pages with different CTA content. Direct LinkedIn/email traffic to those URLs. GA4 automatically tracks each URL separately, so event rates per URL give you the variant comparison. No JavaScript required.

Downside: search engines may index all three pages as duplicate content, diluting SEO. Mitigate with `<meta name="robots" content="noindex">` in Variants B and C front matter.

---

## Test 2: Email Signup Placement

### Hypothesis

Email signup forms placed immediately after the "Choose Your Path" intro section (above-the-fold on scroll) will convert at a higher rate than forms placed at the bottom of the page (below-the-fold), because visitors who have just engaged with the path descriptions are at peak motivation.

### Variants

**Placement A (Control)**: Email signup form appears at the bottom of the homepage, after "Start Now" section

**Placement B**: Email signup form appears after the "Choose Your Path" section intro, before the three path descriptions (very early on page)

**Placement C**: Email signup form appears as a modal/popup triggered by scroll depth (fires at 60% scroll depth — visitor has read the paths but has not yet hit the bottom CTA)

### Placement Implementation

**Placement A (Control)**: Current `docs/index.md` — add Kit embed code at the bottom of the "Start Now" section:

```html
<!-- Add to docs/index.md after "Start Now" section -->
<div class="signup-section" id="email-signup-bottom">
  <h3>Get weekly module excerpts and case studies by email</h3>
  <!-- Kit embed code goes here -->
  <script async data-uid="YOUR_GENERIC_FORM_ID" 
    src="https://YOUR_USERNAME.kit.com/YOUR_FORM_ID/index.js"></script>
</div>
```

**Placement B (After path intro, before path cards)**: In `docs/index.md`, add the Kit embed block immediately after the "Choose Your Path" heading and intro paragraph, before the first `---` separator for the Industrial GC Path section.

**Placement C (Scroll-triggered modal)**: Kit's modal form variant fires on exit intent or scroll depth. In Kit, create a new form of type "Modal" (if available on free plan) and set trigger to "scroll 60%". Alternatively, implement with JavaScript:

```javascript
// docs/assets/js/scroll-modal.js
var modalFired = false;
window.addEventListener('scroll', function() {
  if (modalFired) return;
  var scrollPercent = (window.scrollY / (document.body.scrollHeight - window.innerHeight)) * 100;
  if (scrollPercent > 60) {
    modalFired = true;
    document.getElementById('signup-modal').style.display = 'block';
    gtag('event', 'signup_modal_triggered', {'trigger': 'scroll-60'});
  }
});
```

### Metrics for Placement Test

- **Primary**: `email_signup_conversion` rate per page view (conversion rate per visit, not per impression of the form)
- **Secondary**: Scroll depth at signup (did people who converted scroll far or sign up early?)

---

## Test 3: Module Page "Also Signup" CTA

### Hypothesis

Visitors who have read at least 50% of a module are more likely to convert to email subscribers if offered a module-specific value proposition ("Get the next 5 modules delivered to your inbox") than a generic newsletter offer ("Subscribe to updates").

### Variants

**Module CTA A (Control)**: Generic offer at bottom of each module:
> "Get new modules and case studies delivered weekly. [Subscribe →]"

**Module CTA B**: Path-specific offer:
> "You're on the Residential GC Path. Get Modules 2-5 sent to your inbox over the next two weeks. [Get the sequence →]"

**Module CTA C**: Case study hook:
> "Test your knowledge with 150 real construction scenarios. Subscribe for a new case study every week. [Get cases →]"

**Implementation note**: Module CTA B requires knowing which path the visitor is on. Without a login system, infer from the module number (Modules 07-28 are Residential GC heavy; Modules 01-05 are cross-path). Tag the variant in the module front matter:

```yaml
---
module_cta_variant: b
module_cta_path: residential
---
```

---

## Decision Rules

### When to Declare a Winner

**Minimum requirements before stopping a test**:
1. At least 200 unique sessions on each variant (not page views — sessions)
2. At least 14 days of data (to capture weekday/weekend variation in construction professional traffic)
3. Both conditions must be met, whichever takes longer

**At Phase 1 traffic volumes** (estimated 50-150 sessions/week in early weeks), expect 4-8 weeks to reach 200 sessions per variant. Do not stop early.

**Statistical threshold**: With a static site and GA4, you do not have a native p-value calculator. Use this rule-of-thumb decision framework:

| Observed lift | Confidence | Action |
|---|---|---|
| Control and variant within 5% of each other | Inconclusive | Extend test 2 more weeks |
| One variant 10-20% higher, consistent for 2+ weeks | Directional signal | Proceed with caution; extend to confirm |
| One variant 20%+ higher, consistent for 3+ weeks | Probable winner | Roll out winner; document result |
| One variant underperforms control by 20%+ | Clear loser | Stop serving this variant; note in test log |

For rigorous significance testing: export GA4 data to Google Sheets and use a two-proportion z-test or a free A/B test calculator ([abtestguide.com](https://abtestguide.com/calc/)) to check p < 0.05.

### When to Stop a Test Early (Loss Prevention)

Stop serving a variant immediately if:
- Bounce rate on the variant exceeds control by 30%+ after 100+ sessions (variant is actively hurting)
- Conversion rate is 0 after 150+ sessions (variant is not converting at all)
- User feedback (from email replies, LinkedIn comments) indicates the variant copy is confusing or misleading

### Roll-Out Protocol

When a winner is declared:

1. Update `docs/index.md` with the winning CTA text as the new default
2. Remove the A/B test JavaScript (or set the default variant to the winner)
3. Document the result in `projects/career-training/AB_TEST_RESULTS_LOG.md` (to be created when you have first results):
   - Test name, start date, end date
   - Variant A vs. B vs. C event rates
   - Winner declared, confidence level
   - Change deployed (commit hash)
4. Move to the next test in the sequence below

### Test Sequence

Run tests in this order to avoid testing multiple things simultaneously:

1. **Week 1-4**: Homepage CTA framing (Variants A/B/C) — highest impact, test first
2. **Week 3-6**: Email signup placement (A/B/C) — can overlap with Test 1 if traffic allows
3. **Week 5-8**: Module page CTA text (A/B/C) — test after placement is settled
4. **Week 8+**: Subject line A/B testing (in Kit, for email broadcasts) — Phase 2 territory

---

## Traffic Requirements Summary

| Test | Sessions Needed per Variant | Estimated Weeks at 100 sessions/week |
|---|---|---|
| Homepage CTA (3 variants) | 200 each = 600 total | 6 weeks |
| Signup placement (3 variants) | 200 each = 600 total | 6 weeks (overlap possible) |
| Module CTA (3 variants) | 200 each = 600 total | Depends on module traffic |

**If Phase 1 traffic is below 50 sessions/week**: Pause formal A/B testing. Instead, run variants sequentially (Variant A for 2 weeks, then Variant B for 2 weeks) and compare time-period averages. This is not rigorous but gives directional signal without requiring simultaneous traffic split.

---

## GA4 Configuration for A/B Tests

### Custom Events to Register

In addition to the events in `PHASE_1_GOOGLE_ANALYTICS_SETUP.md`, register:

- `ab_variant_assigned` — parameters: `test_name`, `variant`
- `signup_modal_triggered` — parameters: `trigger` (scroll-60, exit-intent)

### GA4 Explorations for Test Analysis

After 2+ weeks of data, create a GA4 Exploration (free):

1. GA4 > Explore > Blank Exploration
2. Dimensions: `Event name`, `Custom dimension: CTA Placement` (or use `page_path` filtered to homepage)
3. Metrics: `Event count`, `Sessions`, conversion rate
4. Filter: Event name = `path_selection` OR `email_signup_conversion`
5. Breakdown: by `ab_variant_assigned` event parameter `variant`

This gives you a side-by-side conversion rate by variant.

---

## Test Log Template

Track each test run in `AB_TEST_RESULTS_LOG.md` when created:

```
## Test: Homepage CTA Framing
Start date: [DATE]
End date: [DATE]
Variants: A (control), B (free library), C (get certified)
Traffic split: Organic → A; LinkedIn → B; Email → C

Results:
  Variant A: [N] sessions, [N] path_selections, [X%] rate
  Variant B: [N] sessions, [N] path_selections, [X%] rate
  Variant C: [N] sessions, [N] path_selections, [X%] rate

Winner: [A/B/C or Inconclusive]
Confidence: [High/Medium/Low]
Action taken: [Updated homepage CTA to Variant B text, commit XXXXXXXX]
```

---

## Sources

- [A/B Testing for Static Sites — Netlify Blog](https://www.netlify.com/blog/2020/10/05/ab-testing-with-netlify/)
- [GA4 Event-Based Measurement for A/B Tests — Google Developers](https://developers.google.com/analytics/devguides/collection/ga4/events)
- [Two-Proportion Z-Test for A/B Testing — Statistics How To](https://www.statisticshowto.com/probability-and-statistics/hypothesis-testing/z-test/)
- [AB Test Guide Calculator](https://abtestguide.com/calc/)
- [Email CTA Placement Studies 2026 — Campaign Monitor](https://www.campaignmonitor.com/resources/guides/email-marketing-benchmarks/)
