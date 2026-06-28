---
title: "Kit.com Account Setup Checklist"
project: career-training
phase: "2"
created: 2026-06-28
status: pre-trial-documentation
confidence: 92%
---

# Kit.com Account Setup Checklist

**Purpose**: Complete walkthrough for creating a Kit free-tier account, extracting the API key, building subscriber tags for path segmentation, and verifying all free-plan features against the PHASE_2_3_EXECUTION_ROADMAP.md requirements. Written for a first-time Kit user. Intended to be followed step-by-step before the Phase 2 email infrastructure build.

**Critical finding from research**: The Kit free plan has diverged from what PHASE_2_EMAIL_SERVICE_COMPARISON_MATRIX.md documented in Session 4469. API access and visual automation branching are gated differently than expected. Read the Feature Audit section (Step 6) before committing to the free plan for automation-heavy use.

---

## Pre-Setup Requirements

- A working email address you control (not the test subscriber address — your own address)
- 30 minutes uninterrupted
- No credit card required at any point on the free plan

---

## Step 1: Account Creation

**URL**: https://app.kit.com/users/signup

**What you will see**: A simple signup form. Fields: First name, Last name, Email address, Password.

**Steps**:
1. Go to https://app.kit.com/users/signup
2. Enter your name, working email address, and a strong password
3. Click "Create account"
4. Kit will send a verification email immediately — check your inbox (check spam if not received within 2 minutes)
5. Click the verification link in the email
6. Kit redirects you to the onboarding flow

**Payment card**: Not requested at signup for the Newsletter (free) plan. If Kit asks for payment card before you use any feature, you have accidentally clicked a paid plan link. Return to https://app.kit.com/users/signup and restart.

**Onboarding flow** (5-step wizard): Kit presents a guided setup. You can skip every step and return later. Do not spend time here — this checklist covers each step in the correct order.

---

## Step 2: Dashboard Orientation (Where Is Everything?)

After account creation, you land on the Kit dashboard. The navigation is a left sidebar with icons. Here is what each icon opens:

| Sidebar Item | Label | What It Does |
|---|---|---|
| Home icon | Dashboard | Overview: subscriber count, recent broadcasts, quick links |
| Person icon | Subscribers | Your subscriber list — search, filter, tag, export |
| Grid icon | Broadcasts | One-time email sends to your full list or segments |
| Play icon | Automations | Visual automation builder — the core workflow engine |
| Stack icon | Sequences | Pre-scheduled email drip series (not the same as automations) |
| Form icon | Forms | Create and manage opt-in forms for embedding on your site |
| Page icon | Landing Pages | Kit-hosted signup pages (no code needed) |
| Gear icon | Settings | Account info, email sending defaults, billing, API keys |

**Key navigation labels by use case**:
- "Where do I see who has subscribed?" — Subscribers (person icon)
- "Where do I build the welcome email flow?" — Automations (play icon)
- "Where do I get the embed code for my GitHub Pages site?" — Forms (form icon)
- "Where is the API key?" — Settings > Developer > API Keys (gear icon, then Developer tab)
- "Where do I send a one-time email?" — Broadcasts (grid icon)

---

## Step 3: API Key Extraction

**Important caveat**: Kit's pricing page (verified June 2026) lists "API access" as a feature NOT included in the free Newsletter plan. The Kit help documentation states "V3 and V4 API keys are not restricted" and available to all plans. This is contradictory. The practical test: attempt to generate an API key on the free plan. If successful, document it here. If blocked, note the error message.

**Steps to find the API key**:
1. Click the gear icon (Settings) in the left sidebar
2. Click the "Developer" tab at the top of the Settings page
3. You will see two sections: "V3 API Key" and "V4 API (Beta)"
4. For the V3 key: it is displayed as a long string (e.g., `xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`). Click "Copy" to copy it
5. For the V4 key: click "New V4 API Key", give it a name (e.g., "career-training-integration"), click "Create"

**Screenshot label — what to look for**:
- Settings page URL: `app.kit.com/account_settings/developer`
- The V3 key section header reads: "API Key"
- Below it: "API Secret" — copy both; the secret is used for some V3 endpoints
- V4 section shows a "Generate new token" button or "New V4 API Key" depending on interface version

**Store these values** (do not commit to git):
```
V3 API Key: [copy from dashboard]
V3 API Secret: [copy from dashboard]
V4 API Key: [generate and copy]
```

**If API key section is locked behind a paywall prompt**: This confirms the free plan does not include API access. Document the exact error or prompt shown. See Feature Audit section for the impact on Phase 2 integrations.

---

## Step 4: Subscriber Tag Creation

Tags are the mechanism that routes subscribers to different email sequences. The career-training model requires these tags applied at subscribe time:

| Tag Name | Applied When | Routes To |
|---|---|---|
| `residential-gc` | Subscriber uses Residential GC Path form | Residential welcome sequence |
| `industrial-gc` | Subscriber uses Industrial GC Path form | Industrial welcome sequence |
| `specialty-sub` | Subscriber uses Specialty Sub Path form | Specialty sub welcome sequence |
| `generic` | Subscriber uses homepage form (no path selected) | Generic welcome + Day 2 path confirmation |
| `instructor` | Applied manually or via link-click | Instructor-specific monthly digest |
| `high-engagement` | Applied by automation when subscriber opens 3+ emails | Future: deeper content drip |
| `inactive-30d` | Applied by automation after 30 days no open | Future: re-engagement sequence |

**Steps to create tags**:
1. Click the Subscribers icon in the sidebar
2. Click "Subscribers" at the top, then look for "Tags" in the sub-navigation (or find Tags in the left sidebar)
3. Click "+ New Tag" or the equivalent button
4. Type the tag name exactly as listed above (use lowercase, hyphens, no spaces)
5. Click "Create Tag"
6. Repeat for each tag in the table above

**Note**: Tags do not do anything until they are (a) applied to a subscriber manually, (b) set as the default tag for a form, or (c) applied by an automation rule. Creating them now lets you reference them when building forms and automations in the next step.

**Screenshot label — what to look for**:
- Tag list page URL: `app.kit.com/subscribers/tags` or similar
- Each created tag shows with a subscriber count (0 at creation)
- Tags are searchable and sortable by subscriber count

---

## Step 5: Signup Form Creation

Create 4 forms — one per subscriber path. Each form applies a different tag at subscribe time, automatically segmenting subscribers by path from the first touchpoint.

**Form 1: Residential GC Path**

1. Click the Forms icon (or navigate to Forms in left sidebar)
2. Click "New Form" or "+ Create Form"
3. Select form type: "Inline form" (embeds directly in a page — best for GitHub Pages)
4. Select a template (minimal is fine — the simpler the better for professional audiences)
5. In the form settings, set:
   - Form name: "Residential GC Path — Signup"
   - Success message or redirect: "You're in. Check your inbox for your first module." (or redirect to a "thank you" page URL on your site)
   - Tag to apply at subscribe: select `residential-gc` from the dropdown
6. Click "Save"
7. Go to the Embed section and copy the embed code

The embed code looks like this (approximately):
```html
<script async data-uid="[YOUR_FORM_ID]" 
  src="https://[YOUR_USERNAME].kit.com/[FORM_ID]/index.js">
</script>
```

Paste this code into your Jekyll layout or module page HTML where you want the form to appear.

**Repeat for Forms 2-4**:
- Form 2: "Industrial GC Path — Signup" → tag: `industrial-gc`
- Form 3: "Specialty Sub Path — Signup" → tag: `specialty-sub`
- Form 4: "General Interest — Signup" → tag: `generic`

**Screenshot label — what to look for**:
- Form editor URL: `app.kit.com/landing_pages_and_forms/[form_id]/edit`
- "Incentive" tab: this is where you set the tag and success redirect
- "Embed" tab: this is where you copy the inline or modal embed code

---

## Step 6: Feature Audit — Free Tier Verification

Verify each feature required by PHASE_2_3_EXECUTION_ROADMAP.md against actual free-plan availability.

### (a) Unlimited Subscribers

**Required**: Up to 10,000 at free tier  
**Verified**: Yes — Kit pricing page confirms "Up to 10,000 subscribers" on the Newsletter free plan  
**Status**: PASS — Covers all of Phase 2 and most of Phase 3 at target growth rates

### (b) Unlimited Emails

**Required**: Ability to email full list without per-send charges  
**Verified**: Yes — "Unlimited email broadcasts" confirmed on free plan  
**Status**: PASS

### (c) One Automation Rule with Path Branching

**Required by PHASE_2_3_EXECUTION_ROADMAP.md**: "Single automation with path-tag branching (free plan compatible)"  
**Actual free plan**: "1 Basic Visual Automation"  
**Critical gap identified**: Multiple sources (EmailToolTester, Mailsoftly, Automation Atlas) confirm that conditional branching/if-else logic within automations is restricted to paid Creator plans. The free plan's "1 basic visual automation" likely supports a simple trigger-action (e.g., "subscribe → send welcome email") but NOT the if/then branching needed for path routing.  
**Test required**: Attempt to add a conditional branch (e.g., "IF tagged `residential-gc` → send Email A; ELSE send Email B") within the single free-plan automation. Document whether the UI allows this or prompts for upgrade.  
**Contingency if branching unavailable**: Use Kit's Sequences feature (verify if included in free plan) to build separate linear drips per path. The subscriber enters the correct sequence because they subscribed via a path-specific form with the correct tag pre-applied. This avoids needing branching logic inside the automation. See PHASE_2_3_EXECUTION_ROADMAP.md Contingency B for full workaround.

### (d) Forms and Landing Pages

**Required**: Embeddable forms for GitHub Pages  
**Verified**: "Unlimited landing pages and forms" confirmed on free plan  
**Status**: PASS — Forms are unlimited; embed code works on any static HTML page

### (e) API Access

**Required for future integrations** (quiz → tag routing, serverless functions)  
**Claimed in PHASE_2_EMAIL_SERVICE_COMPARISON_MATRIX.md**: API access available on free plan  
**Actual free plan**: Kit pricing page lists "API access" as a feature NOT included in the free plan. Kit help docs say "V3 and V4 API keys are not restricted." This is contradictory.  
**Test required**: Navigate to Settings > Developer and attempt to generate a V3 API key. If the key is generated without a paywall prompt, free plan includes API access. Document the result.  
**Impact if API access requires paid plan**: Phase 2 core email functionality (forms, broadcasts, single automation) is unaffected — API is only needed for programmatic integrations (quiz → tag, serverless subscriber management). These integrations are Phase 3+ features. Deferring API integrations to Creator plan upgrade is acceptable.

### (f) Branding

**Status**: "Powered by Kit" badge required on all emails, forms, and landing pages on the free plan. Cannot be removed without upgrading to Creator ($33/mo). For Phase 2 at launch scale (0-200 subscribers), this is an acceptable tradeoff. Flag for removal when subscriber count justifies the upgrade.

---

## Step 7: All Settings Configured Per Roadmap

Complete these settings before sending any subscriber emails:

**Account Profile (Settings > Profile)**:
- Sender name: Your name or "Construction Career Training" (whichever you want subscribers to see as the "from" name)
- Reply-to email: Your monitored email address
- Company name: Your business name or project name
- Company address: Required by CAN-SPAM. Use your real mailing address. Kit will not send emails without a valid address on file.

**Email Sending Domain (Settings > Email Sending)**:
- Default: Kit sends from `[yourname]@kit.com` or `@convertkit.com`. This works but is generic.
- Better: Verify a sending domain (Settings > Email Sending > "Add sending domain"). Add a TXT record to your DNS provider. This improves deliverability and removes the generic Kit sender address. Takes 24-48 hours to propagate.
- Not required to start, but do it before reaching 100 subscribers.

**Creator Network Recommendations (Settings > Recommendations)**:
- The free plan requires participation in Kit's Creator Network — other creators' newsletters may be recommended to your subscribers, and vice versa.
- Review what categories your recommendations fall into. If the default recommendations are off-brand (e.g., lifestyle content recommended to construction professionals), you can adjust categories or wait for the Creator plan upgrade to opt out entirely.

---

## Step 8: First Test Email

Send a test broadcast before importing any real subscribers.

1. Click Broadcasts in the left sidebar
2. Click "New Broadcast" or "+ Create Broadcast"
3. Subject line: "Test: Welcome to Construction Career Training"
4. Body: "This is a test email to verify account setup. Deliverability check in progress."
5. Recipients: Send to "All Subscribers" (your list will show 1 subscriber — your own test subscriber)
6. Click "Send Test Email" (sends to your own account email without sending to the full list) — do this first
7. Check your inbox within 5 minutes — note delivery time and whether it lands in Primary or Promotions/Spam
8. If the test looks correct, proceed to the full send flow

---

## Success Criteria: Account Created

Check each box when verified:

- [ ] Account created at kit.com (free tier, no credit card entered)
- [ ] Email verification completed
- [ ] Subscriber tags created: `residential-gc`, `industrial-gc`, `specialty-sub`, `generic`, `instructor`
- [ ] 4 signup forms created with correct tag assignments
- [ ] Embed codes copied for each form
- [ ] Sender name and reply-to email set in Account Profile
- [ ] Company address entered (CAN-SPAM compliance)
- [ ] API key status documented (accessible on free plan or requires upgrade — confirmed either way)
- [ ] Free plan feature audit complete with gaps documented
- [ ] First test email queued and delivered to inbox (not spam)

---

## Known Gaps vs. PHASE_2_EMAIL_SERVICE_COMPARISON_MATRIX.md

The Session 4469 comparison matrix was accurate at time of writing but the Kit free plan has tightened since. These items require re-verification or plan adjustment:

| Claim in Matrix | Actual Status (June 2026) | Action |
|---|---|---|
| "1 automation only" with branching | Branching may require paid plan — test required | Test conditional branch in free-plan automation; use Sequences workaround if blocked |
| "API access on free plan" | Listed as NOT included on Kit pricing page; help docs contradict this | Test in dashboard; document actual result |
| "Unlimited sequences" | May require paid plan — unclear from current sources | Verify: can you create more than one Sequence on the free plan? |
| "Kit branding on free plan" | Confirmed — "Powered by Kit" badge cannot be removed | Acceptable at launch; budget for Creator upgrade at 300+ subscribers |

---

## Sources

- [Kit Pricing Page — Flexible Pricing Plans](https://kit.com/pricing)
- [Kit API Overview — Help Center](https://help.kit.com/en/articles/9902901-kit-api-overview)
- [Kit Developer Documentation Overview](https://developers.kit.com/api-reference/overview)
- [ConvertKit Free Plan 2026: What's Included — Mailsoftly](https://mailsoftly.com/blog/kit-free-plan/)
- [Kit's New Free Plan Review — Matt Giaro](https://mattgiaro.com/kit-free-plan-review/)
- [ConvertKit Review 2026 — Automation Atlas](https://automationatlas.io/tools/convertkit/)
- [Kit Email Deliverability Best Practices 2026 — Warmy.io](https://www.warmy.io/blog/convertkit-deliverability-not-working-improve-email-deliverability/)
- [Kit Tutorial for Beginners — EmailToolTester](https://www.emailtooltester.com/en/reviews/convertkit/kit-tutorial/)
