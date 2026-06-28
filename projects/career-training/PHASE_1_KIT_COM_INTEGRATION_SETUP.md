---
title: "Phase 1 Kit.com Integration Setup — Email Signup Workflow"
project: career-training
phase: "1"
created: 2026-06-28
status: integration-ready
---

# Phase 1 Kit.com Integration Setup — Email Signup Workflow

**Scope**: Step-by-step workflow for embedding Kit email signup forms in the GitHub Pages `/docs/signup` page and key module pages. Covers form embed codes, webhook configuration where available on the free plan, automation trigger specification for each subscriber segment, and post-subscribe redirect flow for GA4 event firing.

**Prerequisites**: 
- Kit account created (see `KIT_ACCOUNT_SETUP_CHECKLIST.md` — Steps 1-5)
- Tags created in Kit: `residential-gc`, `industrial-gc`, `specialty-sub`, `generic`, `instructor`
- Four Kit forms created (one per path)
- GitHub Pages site live (Phase 1 push complete)

**Free plan constraints that affect this workflow**:
- 1 automation allowed (use path-tag branching within it)
- "Powered by Kit" badge on all forms (cannot remove without Creator plan)
- API access status unconfirmed — see `KIT_ACCOUNT_SETUP_CHECKLIST.md` Step 3 for test procedure

---

## Part 1: The /docs/signup Page

Create a dedicated signup hub page that presents all four paths and their corresponding forms in one place. This page serves as the destination for email CTA links in modules ("Sign up for this path's email sequence →").

### 1.1 Create docs/signup.md

Create the file at `projects/career-training/docs/signup.md`:

```markdown
---
layout: default
title: Sign Up — Get Your Learning Path by Email
nav_order: 99
nav_exclude: true
permalink: /signup/
---

# Get Your Path Delivered by Email

Choose your learning path below. You'll receive module excerpts, case studies, 
and resources tailored to your track — no spam, unsubscribe anytime.

---

## Industrial GC Path
**For**: Project managers, field supervisors, and specialty contractors 
ready to manage large commercial or industrial projects.

<!-- Kit form embed: Industrial GC Path -->
<div class="kit-form-wrapper" id="form-industrial">
<script async data-uid="INDUSTRIAL_FORM_UID" 
  src="https://YOUR_USERNAME.kit.com/INDUSTRIAL_FORM_ID/index.js">
</script>
</div>

---

## Residential GC Path
**For**: Residential construction professionals ready to start or 
expand their own GC business.

<!-- Kit form embed: Residential GC Path -->
<div class="kit-form-wrapper" id="form-residential">
<script async data-uid="RESIDENTIAL_FORM_UID" 
  src="https://YOUR_USERNAME.kit.com/RESIDENTIAL_FORM_ID/index.js">
</script>
</div>

---

## Specialty Sub → PM Path
**For**: Electricians, plumbers, framers, and specialty contractors 
moving into project management.

<!-- Kit form embed: Specialty Sub Path -->
<div class="kit-form-wrapper" id="form-specialty">
<script async data-uid="SPECIALTY_FORM_UID" 
  src="https://YOUR_USERNAME.kit.com/SPECIALTY_FORM_ID/index.js">
</script>
</div>

---

## Not sure which path? Start here.

The Quick Start Guide helps you choose the right path in about 3 minutes.

[Quick Start Guide →]({{ site.baseurl }}/navigation/quick-start/)

Or sign up for the general list and we'll help you choose:

<!-- Kit form embed: Generic / Homepage -->
<div class="kit-form-wrapper" id="form-generic">
<script async data-uid="GENERIC_FORM_UID" 
  src="https://YOUR_USERNAME.kit.com/GENERIC_FORM_ID/index.js">
</script>
</div>
```

**What to replace**: `YOUR_USERNAME`, `INDUSTRIAL_FORM_UID`, `INDUSTRIAL_FORM_ID`, etc. — get these from Kit Dashboard > Forms > [form name] > Embed tab.

### 1.2 Where to Place Signup Links in Other Pages

Add a signup call-to-action at the bottom of these pages (priority order):

| Page | Link Text | Link Target |
|---|---|---|
| `docs/index.md` ("Start Now" section) | "Get weekly modules by email →" | `/signup/` |
| `docs/navigation/quick-start.md` | "Get your path sequence by email →" | `/signup/?path=quick-start` |
| `docs/navigation/residential-path.md` | "Get Residential GC modules by email →" | `/signup/?path=residential` |
| `docs/navigation/industrial-path.md` | "Get Industrial GC modules by email →" | `/signup/?path=industrial` |
| `docs/navigation/specialty-path.md` | "Get Specialty Sub modules by email →" | `/signup/?path=specialty-sub` |
| First module of each path (Modules 01, 07, or equivalent) | "Continue to Module 2 — or get it by email" | `/signup/` |

**Inline form alternative**: For module pages, embed the Kit form directly at the bottom of the module template rather than linking to the signup page. Inline forms on the page where the visitor is already engaged convert better than redirect-to-signup-page. To embed on all module pages, add the generic form embed to `docs/_layouts/module.html` (if it exists) or to a custom include.

---

## Part 2: Embed Code Retrieval (Step-by-Step)

For each form in Kit, retrieve the embed code:

1. In Kit dashboard, click "Forms" (form icon in left sidebar)
2. Find the form (e.g., "Residential GC Path — Signup")
3. Click on the form name to open it
4. Click "Embed" tab (or "Share" depending on Kit UI version)
5. Select "Inline" format (not Modal, not Slide-in, for static page embedding)
6. Copy the code block — it will look like:

```html
<script async data-uid="abc123def456" 
  src="https://yourname.kit.com/abc123def456/index.js">
</script>
```

The `data-uid` value is your form ID. Copy the entire script tag exactly — do not modify it.

**Testing the embed**: Paste the embed code into a local HTML file, open in browser, and verify the form renders. If it shows a blank space, check that your Kit username in the `src` URL is correct and that the form is published (not in draft state).

---

## Part 3: Post-Subscribe Redirect Configuration

The redirect-on-subscribe flow is how GA4 captures email signup conversion events without server-side code. Configure this in Kit for each form.

### 3.1 In Kit: Set Form Success Action

For each of the four forms:

1. Open the form in Kit
2. Go to "Settings" or "Incentive" tab (terminology varies by Kit UI version)
3. Find "Success action" or "What happens after someone subscribes?"
4. Select "Redirect to external URL"
5. Enter the redirect URL with query parameters:

| Form | Redirect URL |
|---|---|
| Residential GC Path | `https://yoursite.com/signup-thank-you/?form=residential-gc&placement=signup-page` |
| Industrial GC Path | `https://yoursite.com/signup-thank-you/?form=industrial-gc&placement=signup-page` |
| Specialty Sub Path | `https://yoursite.com/signup-thank-you/?form=specialty-sub&placement=signup-page` |
| Generic / Homepage | `https://yoursite.com/signup-thank-you/?form=generic&placement=homepage` |

When the same form is embedded in multiple locations (e.g., the signup page AND at the bottom of a module), use a different `placement` parameter for each embed location by creating a separate Kit form for that context, or by accepting that the placement dimension will always show "signup-page" for these conversions.

### 3.2 Create the Thank-You Page

Create `projects/career-training/docs/signup-thank-you.md`:

```markdown
---
layout: default
title: "You're subscribed — check your inbox"
nav_exclude: true
permalink: /signup-thank-you/
---

# You're subscribed.

Check your inbox for a welcome email. It should arrive within 5 minutes.
If you don't see it, check your spam folder and mark it as not spam.

## Your next step

While you wait for the email, start with your first module:

- [Residential GC Path — Start with Module 07 →]({{ site.baseurl }}/modules/07-residential-gc-scope-and-management/)
- [Industrial GC Path — Start with Module 01 →]({{ site.baseurl }}/modules/01-foundations-contracts-estimating/)
- [Specialty Sub Path — Start with Module 06 →]({{ site.baseurl }}/modules/06-architecture-for-contractors/)

---

**Questions?** See the [FAQ →]({{ site.baseurl }}/navigation/faq/)

<!-- GA4 conversion event fire on page load -->
<script>
document.addEventListener('DOMContentLoaded', function() {
  var params = new URLSearchParams(window.location.search);
  var formVariant = params.get('form') || 'unknown';
  var placement = params.get('placement') || 'unknown';
  
  if (typeof gtag === 'function') {
    gtag('event', 'email_signup_conversion', {
      'form_variant': formVariant,
      'cta_placement': placement,
      'signup_page': document.referrer
    });
  }
});
</script>
```

This page fires the `email_signup_conversion` GA4 event with the form variant and placement parameters automatically captured from the URL. No backend required.

---

## Part 4: Kit Automation Trigger Specification

### 4.1 Welcome Automation (Single Automation, Free Plan)

Kit free plan allows 1 automation. Build it as a single automation with path-tag branching.

**Automation name**: `Welcome — All Paths (Phase 1)`

**Trigger**: "Subscriber subscribes to any form" (or configure one trigger per form if Kit supports it on free plan)

**Automation flow** (pseudocode — build this in Kit's visual automation builder):

```
TRIGGER: New subscriber added

IF subscriber has tag "residential-gc"
  → Send email: "Welcome — Residential GC Path" (Day 0)
  → Wait 2 days
  → Send email: "Your Phase 1 Reading List — Modules 7-10" (Day 2)
  → Wait 2 days
  → Send email: "Quick scenario: Module 13 — Lien Rights" (Day 4, case study hook)
  → Wait 3 days
  → Send email: "Week 1 check-in — How's the Residential GC Path?" (Day 7)

ELSE IF subscriber has tag "industrial-gc"
  → Send email: "Welcome — Industrial GC Path" (Day 0)
  → Wait 2 days
  → Send email: "Your Phase 1 Reading List — Modules 1-5" (Day 2)
  → Wait 2 days
  → Send email: "Quick scenario: Module 3 — SIMOPS Scheduling" (Day 4)
  → Wait 3 days
  → Send email: "Week 1 check-in — How's the Industrial GC Path?" (Day 7)

ELSE IF subscriber has tag "specialty-sub"
  → Send email: "Welcome — Specialty Sub Path" (Day 0)
  → Wait 2 days
  → Send email: "Your Phase 1 Reading List — Modules 1, 6, 24" (Day 2)
  → Wait 2 days
  → Send email: "Quick scenario: Reading the specs before bidding" (Day 4)
  → Wait 3 days
  → Send email: "Week 1 check-in — How's the Specialty Sub path?" (Day 7)

ELSE (no path tag / generic signup)
  → Send email: "Welcome — pick your path" (Day 0 — includes path selector)
  → Wait 2 days
  → Send email: "Which path did you choose?" (Day 2 — confirms path; applies tag if subscriber clicks path link)
  → Wait 5 days
  → Send email: "Start with this module — it works for all paths" (Day 7)
```

**Kit free plan constraint**: If conditional branching is blocked on the free plan (see `KIT_ACCOUNT_SETUP_CHECKLIST.md` Section 6c), use the Sequences workaround: each form applies a path tag AND subscribes the user to a path-specific Sequence (instead of the single automation). Verify whether Sequences are unlimited on the free plan before building.

### 4.2 Re-engagement Automation

Build this as a second automation if Kit allows (verify free plan limit). If limited to 1 automation, defer to Phase 2.

**Name**: `Re-engagement — 30 Day No Open`

**Trigger**: "Subscriber has not opened any email in 30 days"

**Flow**:
```
→ Send email: "Still want construction training content?" 
    (short email, plain text, 3 sentences max)
→ Wait 7 days
→ IF subscriber opened the re-engagement email: Remove tag "engagement-inactive"; apply "engagement-warm"
→ IF subscriber did NOT open: Apply tag "engagement-inactive"; pause all sequences for this subscriber
→ Wait 30 more days
→ IF still no open: Apply tag "engagement-churned"; remove from all active sequences
```

### 4.3 Automation Smoke Test

After building the automation, complete this smoke test before real subscribers arrive:

1. Create a test subscriber account using a second email address you control (Gmail + alias works: `youremail+test@gmail.com`)
2. Subscribe via each of the 4 forms — use a different test alias for each (`+residential`, `+industrial`, etc.)
3. Check that each test subscriber:
   - Received the correct Day 0 welcome email (path-specific, not generic)
   - Has the correct tag applied (check Subscribers list in Kit)
   - Is enrolled in the automation (check the automation's subscriber list)
4. Wait 2 days OR use Kit's "Test" feature to fast-forward through the sequence
5. Confirm Days 2 and 4 emails arrive correctly

**Do not launch Phase 1 without completing this smoke test.** An incorrect automation that sends the wrong welcome email to the first 10 real subscribers creates a permanently negative first impression.

---

## Part 5: Webhook Configuration

### 5.1 What Webhooks Are Available on the Free Plan

Kit's outbound webhooks (HTTP POST to a URL of your choice on subscriber events) are listed as a paid-plan feature in Kit's documentation. The practical test: go to Kit Settings > Integrations or Settings > Developer and look for "Webhooks" or "Add webhook". If this option appears without a paywall prompt, webhooks are available on the free plan.

**If webhooks are available**: Configure a webhook for the `subscriber.activated` event to fire your own downstream logic (future use: quiz → tag routing, CRM sync). The webhook URL would be a serverless function endpoint (Netlify Functions, Vercel, or Cloudflare Workers). This is a Phase 2+ integration — do not block Phase 1 on it.

**If webhooks require paid plan**: The workaround for Phase 1 is the post-subscribe redirect + GA4 event described in Part 3. This covers all Phase 1 measurement needs without webhooks.

### 5.2 Kit API for Future Integration (Phase 2+)

When API access is confirmed (see `KIT_ACCOUNT_SETUP_CHECKLIST.md` Step 3), the most useful Phase 2 API call is subscriber tag assignment:

```javascript
// Example: Assign tag to subscriber via Kit V4 API (Phase 2+)
// Run from a Netlify Function or Cloudflare Worker — NOT from client-side JS (exposes API key)

const response = await fetch('https://api.kit.com/v4/subscribers', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'X-Kit-Api-Key': process.env.KIT_API_KEY  // stored in environment variable, never in code
  },
  body: JSON.stringify({
    email_address: subscriberEmail,
    tags: ['residential-gc'],  // from quiz result
    fields: { quiz_score: quizResult }
  })
});
```

This enables a quiz → tag → sequence flow without requiring Kit form embeds on every quiz result page. Defer until Phase 2 when the quiz lead magnet is built.

---

## Part 6: Form Styling Compatibility with Just the Docs

Kit inline forms inject their own CSS. On some themes, this creates visual conflicts (mismatched fonts, padding, border styles). Test the form rendering on your live site and apply overrides if needed.

Add to `docs/assets/css/custom.css` (create this file if it does not exist):

```css
/* Kit form overrides for Just the Docs theme compatibility */
.formkit-form {
  font-family: inherit !important;  /* Use site font, not Kit's default */
  max-width: 480px;                 /* Constrain form width within content column */
  margin: 2rem 0;
}

.formkit-form input[type="email"],
.formkit-form input[type="text"] {
  border: 1px solid #d1d5da;       /* Match Just the Docs input style */
  border-radius: 4px;
  padding: 8px 12px;
  width: 100%;
  box-sizing: border-box;
}

.formkit-form button[data-element="submit"] {
  background-color: #0969da;       /* Just the Docs link color */
  color: white;
  border: none;
  padding: 8px 16px;
  border-radius: 4px;
  cursor: pointer;
}

/* Kit branding badge — required on free plan, cannot remove */
.formkit-powered-by-convertkit {
  font-size: 0.75rem;
  color: #6e7781;
}
```

Reference the custom CSS in `docs/_config.yml`:

```yaml
# In docs/_config.yml, add:
color_scheme: light
ga_tracking_id: G-XXXXXXXXXX  # Just the Docs supports this key natively in some versions
```

Or include it via `head_custom.html`:

```html
<link rel="stylesheet" href="{{ site.baseurl }}/assets/css/custom.css">
```

---

## Summary: What You Need to Do Before Phase 1 Push

**Kit setup (30-60 minutes)**:
- [ ] Kit account created (Step 1-2 in KIT_ACCOUNT_SETUP_CHECKLIST.md)
- [ ] Tags created: `residential-gc`, `industrial-gc`, `specialty-sub`, `generic`, `instructor`
- [ ] 4 forms created with correct tag assignments
- [ ] Post-subscribe redirect URLs configured for each form (pointing to `/signup-thank-you/`)
- [ ] Welcome automation built with path-tag branching (or Sequences workaround)
- [ ] Automation smoke test passed

**GitHub Pages additions (30-45 minutes)**:
- [ ] `docs/signup.md` created with 4 Kit form embeds
- [ ] `docs/signup-thank-you.md` created with GA4 event fire
- [ ] Signup links added to homepage, quick-start, and path pages
- [ ] `docs/assets/css/custom.css` created with Kit form overrides
- [ ] Kit embed codes confirmed working in local preview (if Jekyll is installed locally)

**After Phase 1 push**:
- [ ] Submit a real test subscription via each form on the live site
- [ ] Verify GA4 Realtime shows `email_signup_conversion` event firing on the thank-you page
- [ ] Confirm subscriber appears in Kit with correct tag
- [ ] Confirm welcome email delivered to test email address within 5 minutes

---

## Sources

- [Kit Embed Forms Documentation — Kit Help Center](https://help.kit.com/en/articles/2502547-add-a-kit-form-to-your-website)
- [Kit Automations on Free Plan — Kit Help Center](https://help.kit.com/en/articles/2502543-how-to-use-automations)
- [Kit Webhooks — Kit Developers](https://developers.kit.com/api-reference/webhooks)
- [Kit API V4 Overview — Kit Developers](https://developers.kit.com/api-reference/overview)
- [Jekyll Custom CSS with Just the Docs — GitHub](https://just-the-docs.github.io/just-the-docs/docs/customization/)
- [KIT_ACCOUNT_SETUP_CHECKLIST.md](./KIT_ACCOUNT_SETUP_CHECKLIST.md) — Session 4467 findings on free plan feature availability
