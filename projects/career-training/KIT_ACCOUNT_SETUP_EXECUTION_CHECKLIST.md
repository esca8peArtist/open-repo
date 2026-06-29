---
title: "Kit Account Setup — Execution Checklist"
project: career-training
phase: "2"
created: 2026-06-29
status: execution-ready
confidence: 92%
time-estimate: "2-3 hours for Steps 1-8; 1-2 additional hours for Steps 9-10 (automation build)"
depends_on:
  - KIT_ACCOUNT_SETUP_CHECKLIST.md
  - PHASE_1_KIT_COM_INTEGRATION_SETUP.md
  - WELCOME_SEQUENCE_DRAFT.md
  - EMAIL_DELIVERABILITY_TEST_RESULTS.md
---

# Kit Account Setup — Execution Checklist

**Purpose**: Complete step-by-step Kit setup checklist for Phase 2 email infrastructure. Covers account creation through automation smoke test. Designed to be followed sequentially in a single session. All steps are copy-paste ready.

**Prerequisite**: GitHub Pages site is live with at least one published module visible at the production URL.

**Total time**: 3-5 hours for all 10 steps plus smoke test. Steps 1-5 can be done in 60-90 minutes. Steps 6-10 require additional writing and configuration time.

**Known platform constraints** (documented in KIT_ACCOUNT_SETUP_CHECKLIST.md and EMAIL_DELIVERABILITY_TEST_RESULTS.md):
- Kit free plan allows 1 visual automation only. Conditional branching in that automation may require Creator plan.
- The Sequences workaround (one Sequence per path, enrolled at subscribe via form settings) avoids this limitation.
- "Powered by Kit" badge mandatory on all emails and forms on the free plan.
- API access status contradicted by Kit's own docs — test at Step 3 and document the result.

---

## Step 1: Account Creation

**URL**: https://app.kit.com/users/signup

**Time**: 10-15 minutes

**Steps**:
1. Navigate to https://app.kit.com/users/signup
2. Enter: First name, Last name, your working email address, strong password
3. Click "Create account"
4. Check inbox for verification email from Kit — typically arrives within 2 minutes
5. Click the verification link in the email
6. Kit's onboarding wizard appears — skip every step (click "Skip" or "I'll do this later")
7. You land on the Kit dashboard

**Checkpoint 1 — Account created**:
- [ ] Dashboard visible at app.kit.com
- [ ] No credit card entered or requested
- [ ] Plan shown as "Newsletter" (free) in top-right or account settings

**If Kit requests a credit card during signup**: You have landed on a paid plan link. Return to https://app.kit.com/users/signup and start fresh.

---

## Step 2: Dashboard Orientation

Spend 5 minutes locating these navigation items before building anything. Knowing where things are prevents time lost hunting through menus.

**Left sidebar navigation — what each icon leads to**:

| Icon | Label | Used In This Checklist |
|------|-------|------------------------|
| Home | Dashboard | Step 2 (orientation) |
| Person | Subscribers | Steps 4, 9 (verification) |
| Grid | Broadcasts | Step 10 (test send) |
| Play | Automations | Step 8 (automation build) |
| Stack | Sequences | Step 8 (workaround if branching unavailable) |
| Form | Forms | Step 5 (form creation) |
| Page | Landing Pages | Not used in this checklist |
| Gear | Settings | Steps 3, 7 (API key, sender settings) |

**Checkpoint 2 — Navigation confirmed**:
- [ ] Can locate: Subscribers, Broadcasts, Automations, Sequences, Forms, Settings

---

## Step 3: API Key Documentation (Test, Do Not Skip)

**URL**: app.kit.com/account_settings/developer (or: Settings gear > Developer tab)

**Time**: 5 minutes

This step documents whether API access is available on the free plan. The answer affects Phase 3 integrations (quiz-to-tag routing, serverless subscriber management). Core Phase 2 email capture does NOT require the API.

**Steps**:
1. Click the gear icon (Settings) in the left sidebar
2. Look for a "Developer" tab at the top of the Settings page
3. If the Developer tab exists and shows an API Key field without a paywall prompt:
   - Copy the V3 API Key: `____________________________`
   - Copy the V3 API Secret: `____________________________`
   - (Optional) Click "New V4 API Key" → name it "career-training-phase2" → click Create
4. If the Developer section shows a paywall or upgrade prompt: document this exact message below

**Result** (circle one):
- API accessible on free plan — key copied and stored securely outside git
- API behind paywall — paywall message: `____________________________`

**Checkpoint 3 — API status documented**:
- [ ] V3 API key status documented (accessible or blocked — not left blank)

**API key storage**: Do NOT commit the API key to this file or to git. Store it in a password manager or local plaintext file outside the git repo. The key belongs in an environment variable when used in serverless functions (see PHASE_1_KIT_COM_INTEGRATION_SETUP.md Part 5.2).

---

## Step 4: Subscriber Tag Creation

**URL**: From Subscribers view, look for "Tags" in sub-navigation or sidebar

**Time**: 10 minutes

Create all 7 tags now. Tags do nothing until applied — creating them in advance makes form and automation setup faster.

**Tags to create** (exact names — lowercase, hyphens, no spaces):

| Tag Name | Applied When | Routes To |
|----------|-------------|-----------|
| `residential-gc` | Residential GC Path form submit | Residential welcome sequence |
| `industrial-gc` | Industrial GC Path form submit | Industrial welcome sequence |
| `specialty-sub` | Specialty Sub Path form submit | Specialty sub welcome sequence |
| `generic` | Homepage / untagged form submit | Generic welcome + Day 2 path confirmation |
| `instructor` | Manual application or self-identification | Instructor monthly digest |
| `high-engagement` | Applied by automation: opened 3+ emails in 14 days | Fast-track content drip (Month 2+) |
| `inactive-30d` | Applied by automation: no open in 30 days | Re-engagement sequence |

**How to create each tag**:
1. Click Subscribers icon in sidebar
2. Find "Tags" in sub-navigation (may appear as a tab or sidebar item depending on Kit UI version)
3. Click "+ New Tag" or equivalent button
4. Type tag name exactly as listed above
5. Click "Create Tag"
6. Verify tag appears in the list with subscriber count "0"

**Checkpoint 4 — All tags created**:
- [ ] `residential-gc` created
- [ ] `industrial-gc` created
- [ ] `specialty-sub` created
- [ ] `generic` created
- [ ] `instructor` created
- [ ] `high-engagement` created
- [ ] `inactive-30d` created

---

## Step 5: Signup Form Creation

**URL**: Forms icon in sidebar → "New Form" or "+ Create Form"

**Time**: 30-45 minutes for all 4 forms

Create 4 forms. Each form applies a different tag at subscribe time. This is the segmentation mechanism — no branching logic needed in automations if forms do the routing.

### Form 1: Residential GC Path

1. Click Forms icon → New Form
2. Select form type: **Inline** (embeds in page — do not select Modal or Slide-in for GitHub Pages)
3. Select a minimal template (the simpler, the better — construction professionals respond to clean, not ornate)
4. In form settings / Incentive tab:
   - Form name: `Residential GC Path — Signup`
   - Tag to apply at subscribe: `residential-gc`
   - Success action: Redirect to external URL → `https://[YOUR-SITE-URL]/signup-thank-you/?form=residential-gc&placement=signup-page`
5. Save the form
6. Click "Embed" tab → select "Inline" → copy the embed code
7. Paste the embed code here for reference:

```html
<!-- RESIDENTIAL GC FORM EMBED — paste this into docs/signup.md -->
<script async data-uid="[COPY FROM KIT]"
  src="https://[YOUR-USERNAME].kit.com/[FORM-ID]/index.js">
</script>
```

**Checkpoint — Form 1**:
- [ ] Form created with name "Residential GC Path — Signup"
- [ ] Tag `residential-gc` assigned in form settings
- [ ] Post-subscribe redirect URL set
- [ ] Embed code copied and stored

### Form 2: Industrial GC Path

Repeat the process above with these values:
- Form name: `Industrial GC Path — Signup`
- Tag: `industrial-gc`
- Redirect: `https://[YOUR-SITE-URL]/signup-thank-you/?form=industrial-gc&placement=signup-page`

```html
<!-- INDUSTRIAL GC FORM EMBED -->
<script async data-uid="[COPY FROM KIT]"
  src="https://[YOUR-USERNAME].kit.com/[FORM-ID]/index.js">
</script>
```

**Checkpoint — Form 2**:
- [ ] Form created, tag `industrial-gc` assigned, redirect set, embed code copied

### Form 3: Specialty Sub Path

- Form name: `Specialty Sub Path — Signup`
- Tag: `specialty-sub`
- Redirect: `https://[YOUR-SITE-URL]/signup-thank-you/?form=specialty-sub&placement=signup-page`

```html
<!-- SPECIALTY SUB FORM EMBED -->
<script async data-uid="[COPY FROM KIT]"
  src="https://[YOUR-USERNAME].kit.com/[FORM-ID]/index.js">
</script>
```

**Checkpoint — Form 3**:
- [ ] Form created, tag `specialty-sub` assigned, redirect set, embed code copied

### Form 4: General Interest (Homepage)

- Form name: `General Interest — Homepage`
- Tag: `generic`
- Redirect: `https://[YOUR-SITE-URL]/signup-thank-you/?form=generic&placement=homepage`

```html
<!-- GENERAL INTEREST FORM EMBED -->
<script async data-uid="[COPY FROM KIT]"
  src="https://[YOUR-USERNAME].kit.com/[FORM-ID]/index.js">
</script>
```

**Checkpoint — Form 4**:
- [ ] Form created, tag `generic` assigned, redirect set, embed code copied

---

## Step 6: Embed Codes on GitHub Pages Site

**Time**: 30-45 minutes

**Files to modify**: `docs/signup.md` (create if it does not exist), plus CTA links in homepage and path pages.

### 6.1 Create docs/signup.md

The complete file content for `docs/signup.md` is specified in PHASE_1_KIT_COM_INTEGRATION_SETUP.md Part 1.1. Replace the placeholder `YOUR_USERNAME`, `FORM_ID`, and `FORM_UID` values with the actual values from Step 5.

Key things to confirm after saving:
- The file has `permalink: /signup/` in front matter
- The file has `nav_exclude: true` (keeps it out of the sidebar)
- Each form section has a clear path description above it

### 6.2 Create docs/signup-thank-you.md

This page fires the GA4 `email_signup_conversion` event on page load. Complete file content in PHASE_1_KIT_COM_INTEGRATION_SETUP.md Part 3.2. Replace `[SITE URL]` with your production URL.

### 6.3 Add Signup CTAs to Existing Pages

In each file listed below, add a signup link at the bottom:

| File | CTA Text | Link |
|------|----------|------|
| `docs/index.md` | `[Get weekly modules by email →](/signup/)` | `/signup/` |
| `docs/navigation/quick-start.md` | `[Get your path sequence by email →](/signup/?path=quick-start)` | `/signup/?path=quick-start` |
| `docs/navigation/residential-path.md` | `[Get Residential GC modules by email →](/signup/?path=residential)` | `/signup/?path=residential` |
| `docs/navigation/industrial-path.md` | `[Get Industrial GC modules by email →](/signup/?path=industrial)` | `/signup/?path=industrial` |
| `docs/navigation/specialty-path.md` | `[Get Specialty Sub modules by email →](/signup/?path=specialty-sub)` | `/signup/?path=specialty-sub` |

### 6.4 Push Changes to GitHub

```bash
git add docs/signup.md docs/signup-thank-you.md
git add docs/index.md docs/navigation/
git commit -m "feat: Kit email signup forms and thank-you page"
git push origin main
```

Wait 1-3 minutes for GitHub Pages build. Then verify: visit `[SITE-URL]/signup/` and confirm all 4 forms render (not blank space).

**Checkpoint 6 — Forms live on site**:
- [ ] `/signup/` page loads with all 4 Kit forms visible
- [ ] Each form section has a path description above it
- [ ] `/signup-thank-you/` page exists and loads without 404
- [ ] Signup CTA links visible on homepage, quick-start, and path overview pages
- [ ] CSS overrides applied if needed (see PHASE_1_KIT_COM_INTEGRATION_SETUP.md Part 6)

---

## Step 7: Sender Settings Configuration

**URL**: Settings (gear icon) > Profile or Account Settings

**Time**: 15 minutes

Configure these settings before any real subscriber receives an email.

**Profile / Account settings**:

| Setting | Value to Enter | Location in Kit |
|---------|---------------|-----------------|
| Sender name | "Construction Career Training" or your full name — pick one and be consistent | Settings > Profile |
| Reply-to email | An email you monitor daily | Settings > Profile |
| Company name | Your business name or project name | Settings > Profile |
| Company address | Required by CAN-SPAM — your real mailing address | Settings > Profile |

**Email sending domain** (Settings > Email Sending):

By default, Kit sends from `@kit.com` or `@convertkit.com`. This works but is generic. To improve deliverability:
1. Navigate to Settings > Email Sending > Add Sending Domain
2. Enter your domain (if you have a custom domain — e.g., `constructioncareer.training`)
3. Kit provides DNS records (TXT, CNAME) to add to your domain's DNS settings
4. Add records to your DNS provider (GoDaddy, Namecheap, Cloudflare, etc.)
5. DNS propagation takes 24-48 hours
6. After propagation, return to Kit and click "Verify"

**If you do not have a custom domain**: Skip this step. Kit's shared sending domain is adequate for 0-100 subscribers. Add a custom sending domain before reaching 100 subscribers if possible.

**Creator Network Recommendations** (Settings > Recommendations):
- Kit free plan requires participation in Creator Network — other creators' newsletters may be recommended to your subscribers
- Review the categories. If default recommendations are off-brand, adjust the topic categories to "Education", "Professional Development", or "Business"

**Checkpoint 7 — Sender settings complete**:
- [ ] Sender name set
- [ ] Reply-to email set and monitored
- [ ] Company address entered (required for CAN-SPAM compliance — Kit will not send without this)
- [ ] Custom sending domain added OR decision made to use Kit default domain for now

---

## Step 8: Welcome Sequence or Automation Build

**Time**: 60-90 minutes

**Critical decision point**: Before building, determine which approach the free plan supports.

### 8.1 Test for Conditional Branching (5 minutes)

1. Click Automations (play icon) in sidebar
2. Click "New Automation" or "+ Create Automation"
3. Set trigger: "Subscriber added to any form" or "Subscriber subscribes"
4. Click the "+" button to add a step
5. Look for a "Condition" or "If/Else" step type

**Result** (check one):
- [ ] Condition step is available → **Use Approach A below**
- [ ] Condition step shows upgrade prompt → **Use Approach B below**

### Approach A: Single Automation with Path Branching

Use this if conditional branching is available on the free plan.

**Automation name**: `Welcome — All Paths`

**Trigger**: Subscriber added to any form

**Flow** (build in Kit's visual automation builder):

```
TRIGGER: New subscriber
    ↓
[Condition: Has tag "residential-gc"?]
  YES →
    Send: "You're in — Residential GC Path" (Day 0 email)
    Wait: 3 days
    Send: "The most-cited Cal/OSHA violation in residential construction" (Day 3)
    Wait: 4 days
    Send: "Quick scenario — what would you do?" (Day 7)
  NO →
    [Condition: Has tag "industrial-gc"?]
      YES →
        Send: "You're in — Industrial GC Path" (Day 0)
        Wait: 3 days
        Send: "Why the first thing every industrial GC needs is a written safety program" (Day 3)
        Wait: 4 days
        Send: "Quick scenario — what would you do?" (Day 7 — same as residential, case study is path-agnostic)
      NO →
        [Condition: Has tag "specialty-sub"?]
          YES →
            Send: "You're in — Specialty Sub Path" (Day 0)
            Wait: 3 days
            Send: "One document that protects you from the most common Cal/OSHA citation" (Day 3)
            Wait: 4 days
            Send: "Quick scenario — what would you do?" (Day 7)
          NO (generic / untagged) →
            Send: "You're in. Here's where to start." (Day 0 — path selection email)
            Wait: 3 days
            Send: "Which path did you choose?" (Day 3 — confirms path, applies tag if subscriber clicks)
            Wait: 4 days
            Send: "Quick scenario — what would you do?" (Day 7)
```

All email copy is in WELCOME_SEQUENCE_DRAFT.md — copy directly from that file into Kit's email editor.

### Approach B: Sequences Per Path (Workaround for Branching Limitation)

Use this if conditional branching requires a paid plan (documented finding in EMAIL_DELIVERABILITY_TEST_RESULTS.md Section D).

**Create 4 Sequences** (Sequences icon in sidebar → New Sequence):

| Sequence Name | Path | Tag | Emails |
|---------------|------|-----|--------|
| `Residential GC Welcome` | Residential | `residential-gc` | Day 0, Day 3 (residential variant), Day 7 |
| `Industrial GC Welcome` | Industrial | `industrial-gc` | Day 0, Day 3 (industrial variant), Day 7 |
| `Specialty Sub Welcome` | Specialty | `specialty-sub` | Day 0, Day 3 (specialty variant), Day 7 |
| `Generic Welcome` | Untagged | `generic` | Day 0 (path selection), Day 3 (which path?), Day 7 |

Email copy for all variants is in WELCOME_SEQUENCE_DRAFT.md.

**For each sequence**:
1. Create the sequence (Sequences → New Sequence → enter name)
2. Add Email 1 (Day 0) — paste subject line and body from WELCOME_SEQUENCE_DRAFT.md
3. Set delay: "0 days" (send immediately at subscribe)
4. Add Email 2 (Day 3) — paste the path-specific variant from WELCOME_SEQUENCE_DRAFT.md
5. Set delay: "3 days after previous email"
6. Add Email 3 (Day 7) — paste the case study email from WELCOME_SEQUENCE_DRAFT.md
7. Set delay: "4 days after previous email" (3 + 4 = 7 days from subscribe)

**Link each form to its sequence** (critical — this replaces the branching automation):
1. Open each form in Kit (Forms icon)
2. Look in form settings for "What happens after subscribe?" or "Incentive" settings
3. Find option to "Add to sequence" or "Enroll in sequence"
4. Select the matching sequence (Residential GC form → Residential GC Welcome sequence)
5. Save

If Kit's form settings do not have a direct sequence enrollment option:
- Open Automations → New Automation
- Trigger: "Subscriber adds tag `residential-gc`"
- Action: "Add to sequence: Residential GC Welcome"
- Repeat for each path tag

**Checkpoint 8 — Welcome automation or sequences complete**:
- [ ] Approach A OR Approach B determined and implemented
- [ ] Email copy loaded into Kit for all 3 days × 4 path variants
- [ ] Each form linked to correct sequence or automation path
- [ ] Subject lines match WELCOME_SEQUENCE_DRAFT.md exactly

---

## Step 9: Integration Testing (Embed Verification)

**Time**: 15 minutes

Test that forms on the GitHub Pages site actually connect to Kit.

**Test procedure**:
1. Visit your live GitHub Pages site at the production URL (not localhost)
2. Navigate to `/signup/`
3. Find the Residential GC Path form
4. Submit with a real email you control (e.g., `youraddress+test@gmail.com`)
5. Immediately check Kit → Subscribers — does the test subscriber appear?
6. Check the tag on the test subscriber — is it `residential-gc`?
7. Check your test email inbox — did the Day 0 welcome email arrive within 5 minutes?
8. Visit the thank-you page URL (`/signup-thank-you/`) — does it load without 404?
9. Open GA4 Realtime (analytics.google.com → your property → Realtime) — does the `email_signup_conversion` event appear?

**Repeat for all 4 forms** (use different email aliases: `+industrial`, `+specialty`, `+generic`).

**Integration test results table**:

| Form | Subscriber in Kit? | Correct Tag Applied? | Day 0 Email Received? | Email in Primary/Promotions/Spam? | GA4 Event Fired? |
|------|--------------------|---------------------|-----------------------|----------------------------------|-----------------|
| Residential GC | [ ] Y [ ] N | [ ] Y [ ] N | [ ] Y [ ] N | _____________ | [ ] Y [ ] N |
| Industrial GC | [ ] Y [ ] N | [ ] Y [ ] N | [ ] Y [ ] N | _____________ | [ ] Y [ ] N |
| Specialty Sub | [ ] Y [ ] N | [ ] Y [ ] N | [ ] Y [ ] N | _____________ | [ ] Y [ ] N |
| Generic | [ ] Y [ ] N | [ ] Y [ ] N | [ ] Y [ ] N | _____________ | [ ] Y [ ] N |

**Checkpoint 9 — Integration test passed**:
- [ ] All 4 forms submit without error
- [ ] All 4 subscribers appear in Kit with correct tags
- [ ] All 4 Day 0 emails delivered (Primary or Promotions tab — Spam is a FAIL)
- [ ] GA4 `email_signup_conversion` event visible in Realtime for at least 1 test submission
- [ ] Thank-you page loads and displays correct path-specific module links

**If any integration test FAILS**:

| Failure | Likely Cause | Fix |
|---------|-------------|-----|
| Subscriber not appearing in Kit | Form embed code incorrect; Kit account not verified | Re-copy embed code from Kit; check account verification |
| Wrong tag on subscriber | Form tag setting not saved | Re-open form in Kit → Incentive tab → confirm tag selected → save |
| No Day 0 email | Automation not triggered; sequence not linked to form | Check Automations or Sequences → verify trigger is firing |
| Email in spam | New account, no sending domain | Set up custom sending domain (Settings > Email Sending); test again after 24h DNS propagation |
| GA4 event not firing | Thank-you page missing GA4 snippet OR `gtag` function not loaded | Check that GA4 snippet is in `_layouts/default.html`; open browser DevTools Console on thank-you page and check for `gtag` errors |

---

## Step 10: Smoke Test — Full Sequence Verification

**Time**: 30 minutes (plus 7-day wait to verify all 3 emails send)

The smoke test verifies the full 7-day sequence, not just the Day 0 email.

**Option A — Use Kit's built-in test feature** (if available):
Some Kit accounts allow "preview" or "test" mode on automations that fast-forwards through wait delays. Check Automations → your automation → look for a "Test" or "Preview subscriber flow" option.

**Option B — Real-time wait test**:
Subscribe the test email addresses at D+0. Wait the actual 3 and 7 day delays. Log delivery in the table below.

**Smoke test delivery log**:

| Test Subscriber | D+0 Email | Time Received | D+3 Email | Time Received | D+7 Email | Time Received |
|----------------|-----------|--------------|-----------|--------------|-----------|--------------|
| +residential | Sent / Not sent | ___ | Sent / Not sent | ___ | Sent / Not sent | ___ |
| +industrial | Sent / Not sent | ___ | Sent / Not sent | ___ | Sent / Not sent | ___ |
| +specialty | Sent / Not sent | ___ | Sent / Not sent | ___ | Sent / Not sent | ___ |
| +generic | Sent / Not sent | ___ | Sent / Not sent | ___ | Sent / Not sent | ___ |

**Checkpoint 10 — Smoke test complete**:
- [ ] All 4 path variants sent Day 0 email within 5 minutes of subscribe
- [ ] All 4 path variants sent Day 3 email within 30 minutes of the 3-day delay trigger
- [ ] All 4 path variants sent Day 7 email within 30 minutes of the 7-day delay trigger
- [ ] Day 3 and Day 7 emails match the path-specific copy in WELCOME_SEQUENCE_DRAFT.md
- [ ] No email went to spam during smoke test
- [ ] Email open and click events visible in Kit analytics after opening and clicking the test emails

---

## Final Sign-Off: Kit Account Setup Complete

Check all 10 items:

- [ ] Step 1: Kit free-tier account created, email verified, no credit card entered
- [ ] Step 2: Dashboard orientation complete — can locate all key navigation items
- [ ] Step 3: API key status documented (accessible or blocked — confirmed, not assumed)
- [ ] Step 4: All 7 subscriber tags created with correct exact names
- [ ] Step 5: 4 signup forms created, each with correct path tag and post-subscribe redirect URL
- [ ] Step 6: Forms embedded on GitHub Pages `/signup/` page; thank-you page created; CTAs added to 5 site pages
- [ ] Step 7: Sender name, reply-to email, and company address set; sending domain added or decision documented
- [ ] Step 8: Welcome sequence loaded with all 3 email days × 4 path variants; routing mechanism confirmed working
- [ ] Step 9: Integration test passed — all 4 forms submit, subscribe, tag, and trigger email correctly
- [ ] Step 10: Full 7-day smoke test complete — all 12 emails (4 paths × 3 days) delivered on schedule

**When this checklist is fully checked**: Phase 2 email infrastructure is operational. Proceed to WEEK_1_2_EMAIL_OPERATIONS_RUNBOOK.md for daily monitoring procedures.

---

## Known Gaps and Open Items

These items are documented but not resolved at setup time:

| Item | Gap | Resolution Path |
|------|-----|----------------|
| Conditional branching on free plan | May require Creator upgrade — test result documented in Step 8 | Use Sequences workaround (Approach B) if branching unavailable |
| API access on free plan | Contradicted by Kit pricing page vs. help docs — test result documented in Step 3 | Defer API integrations to Creator plan upgrade; no Phase 2 core function requires API |
| "Powered by Kit" badge | Cannot be removed on free plan | Accept for Phase 2; remove at first paid plan upgrade (300+ subscriber trigger) |
| Sequences limit on free plan | Possibly limited — test in Step 8 | If sequences also limited, fall back to single-path welcome sequence with Day 0 path selection email |

---

## Sources

- KIT_ACCOUNT_SETUP_CHECKLIST.md — original Kit setup research (Session 4467)
- PHASE_1_KIT_COM_INTEGRATION_SETUP.md — form embedding, automation trigger specification, webhook details
- WELCOME_SEQUENCE_DRAFT.md — all email copy for Days 0, 3, 7 across 4 path variants
- EMAIL_DELIVERABILITY_TEST_RESULTS.md — automation branching constraint findings
- PHASE_2_3_EXECUTION_ROADMAP.md — contingency paths for Kit free plan limitations
- [Kit Embed Forms Documentation](https://help.kit.com/en/articles/2502547-add-a-kit-form-to-your-website)
- [Kit Sequences — How to Use](https://help.kit.com/en/articles/2502568-sequences-overview)
- [Kit CAN-SPAM Compliance Requirements](https://help.kit.com/en/articles/2502681-can-spam-compliance)
- [Kit Email Sending Domain Setup](https://help.kit.com/en/articles/2502591-set-up-a-custom-email-sending-domain)
