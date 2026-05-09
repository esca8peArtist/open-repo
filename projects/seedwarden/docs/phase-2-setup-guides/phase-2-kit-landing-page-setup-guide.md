---
title: "Phase 2 Kit Landing Page Setup Guide"
subtitle: "Account creation, landing page builder, email list integration, UTM setup, and custom domain decision"
date: 2026-05-09
status: production-ready
estimated-time: 55–75 min (padded for first-time Kit setup; experienced: 40–50 min)
platform: Kit (kit.co, formerly ConvertKit)
account-email: wanka95@gmail.com
references:
  - kit-account-setup-guide.md (full platform configuration reference — canonical)
  - KIT_SETUP_NOTES.md (working notes)
  - PHASE_2_EMAIL_STRATEGY.md (strategy decisions and platform selection rationale)
  - docs/phase-2-operations/phase-2-email-automation-sequence.md (sequence specs)
---

# Phase 2 Kit Landing Page Setup Guide
## Account Creation, Landing Page, Email Integration, and UTM Setup

**Purpose**: Walk through Kit account creation and the Zone Quick-Start Card landing page setup from first login to a live, tested form that delivers zone card PDFs and triggers the welcome email sequence. This guide is sufficient to complete the setup action before May 30 without referencing `kit-account-setup-guide.md` (which is the extended configuration reference).

**Estimated time by section**:
- Account creation and initial configuration: 10–15 minutes
- Email integration setup (SPF/DKIM): 15–20 minutes (includes DNS propagation wait; most of this is passive)
- Landing page builder: 15–20 minutes
- UTM parameter setup: 5–10 minutes
- Custom domain decision and DNS verification: 5 minutes to decide; 10–30 minutes to execute if you go custom domain
- End-to-end test: 5 minutes

**Total**: 50–70 minutes active, plus up to 48 hours for DNS propagation (passive, no action required during propagation).

---

## Part 1: Account Creation (10–15 minutes)

### Step 1.1 — Create the Kit Account

Navigate to kit.co in a desktop browser. Click "Start for free."

| Field | Value |
|---|---|
| Email | wanka95@gmail.com |
| Password | Create a strong password; store in a password manager |
| Sender name | Seedwarden |
| Time zone | Your local time zone (used for scheduled broadcast timing) |
| Business type | Creator (select "Creator" if prompted — this is the correct category for digital guide products) |

Click "Create account."

Kit sends a verification email to wanka95@gmail.com. Open Gmail, find the Kit verification email (subject: "Confirm your Kit account" or similar), and click the confirmation link.

After confirming: Kit takes you to the onboarding dashboard. You can skip any optional setup prompts (importing contacts, connecting integrations) — complete those manually in the correct order below.

### Step 1.2 — Confirm Sender Name

Navigate to Settings (gear icon in the lower left sidebar) > Profile.

Confirm:
- Sender name: Seedwarden
- Reply-to email: wanka95@gmail.com

If the sender name shows your personal name instead of "Seedwarden": click the name field and change it. Click "Save." All emails sent from this account will appear in subscribers' inboxes as "Seedwarden via Kit" or "Seedwarden" (depending on subscriber email client and whether SPF/DKIM is configured).

### Step 1.3 — Note Free Tier Limits

At the time of setup (confirm at kit.co if changed):
- Up to 10,000 subscribers on the free plan
- Unlimited broadcasts
- Unlimited automation sequences
- 1 published landing page
- Basic conditional automation logic

Seedwarden Phase 2 uses 1 landing page (Zone Quick-Start Card), 1 automation sequence (5-email Welcome), and 1 broadcast (launch day). The free tier covers all of this.

### Step 1.4 — Generate API Key

Even if no integration is needed at launch, generate the API key now so it is available if needed (e.g., Zapier flow connecting Etsy orders to Kit tags).

Settings > Developer > API Keys > Add API Key:
- Name: "Seedwarden Main Key"
- Access: Read and Write
- Click "Generate Key." Copy the key immediately and store it in a secure local note. It will not be shown again.

Do not share this API key — it grants write access to your subscriber list.

---

## Part 2: Sender Domain Configuration — SPF and DKIM (15–20 min, mostly passive)

This is the most technically involved step and the most important for email deliverability. Kit emails sent without SPF and DKIM authentication have a substantially higher probability of landing in subscribers' spam folders, especially at Gmail.

**If you do not have a custom domain** (sending from wanka95@gmail.com): skip this section entirely. Gmail handles authentication automatically for @gmail.com senders. Proceed to Part 3.

**If you have a custom domain** (e.g., seedwarden.com): complete this section.

### Step 2.1 — Access Your Domain Registrar's DNS Panel

Log into the registrar where your domain is registered (Namecheap, GoDaddy, Google Domains, Squarespace, etc.). Locate the DNS management panel for your domain. You will add two records here.

If you are not sure which registrar holds your domain: run a WHOIS lookup at lookup.icann.org — it shows the registrar name under "Registrar."

### Step 2.2 — Add SPF Record

In Kit: Settings > Email Settings > Custom Sender Domain. Kit shows the SPF record value to add.

The standard Kit SPF record is:
`v=spf1 include:sendgrid.net ~all`

In your DNS registrar, add a TXT record:
- Host/Name: `@` (this means the root domain, e.g., seedwarden.com itself)
- Value: `v=spf1 include:sendgrid.net ~all`

**Important**: If your domain already has an SPF record (check for any existing TXT record starting with `v=spf1`), do not add a second record — DNS only permits one SPF record per domain. Instead, merge the Kit value into the existing record:

Existing record: `v=spf1 include:_spf.google.com ~all`
After merging: `v=spf1 include:_spf.google.com include:sendgrid.net ~all`

Edit the existing SPF record to add `include:sendgrid.net` before the `~all` at the end.

### Step 2.3 — Add DKIM Record

In Kit: Settings > Email Settings > DKIM Signing. Kit provides a CNAME record value.

In your DNS registrar, add a CNAME record:
- Host/Name: the string Kit provides (typically `k1._domainkey` or similar)
- Value/Target: the address Kit provides

Kit may provide two CNAME records. Add both.

### Step 2.4 — Wait for Propagation

DNS changes take between 15 minutes and 48 hours to propagate. You do not need to wait before continuing to Part 3 — continue with landing page and sequence setup in parallel with propagation.

To check propagation status: return to Kit > Settings > Email Settings. When both records show a green checkmark, propagation is complete and your emails are authenticated.

**Verification test**: After Kit shows green checkmarks, send a test email from Kit to wanka95@gmail.com. Open it in Gmail. Click the three-dot menu > "Show original." Confirm `dkim=pass` and `spf=pass` appear in the "Authentication-Results" line of the email header.

---

## Part 3: Landing Page Builder (15–20 minutes)

### Step 3.1 — Create the Landing Page

Kit > Landing Pages and Forms > Create New > Landing Page.

Select the simplest single-column template. Simple layouts perform better for high-intent sign-ups than visually complex layouts — Seedwarden's audience responds to directness.

After selecting a template, you enter the landing page editor.

### Step 3.2 — Configure Page Content

Edit each element by clicking on it. Kit's editor uses an inline click-to-edit approach — click any text block to edit it.

**Headline**: "Your Free Zone Quick-Start Card"

**Subheadline**: "Know exactly what to plant, when to plant it, and what to do right now in your zone — one-page reference card, free."

**Form fields** (in this order, all required):
1. First Name — label: "First Name," placeholder: "Your first name"
2. Email Address — label: "Email Address," placeholder: "Your email"
3. Growing Zone — label: "Your Growing Zone," field type: Dropdown

**To add a dropdown field**:
- In the form editor: click "Add field" or the "+" icon in the form section
- Field type: select "Dropdown" or "Select"
- Label: "Your Growing Zone"
- Add the following options in order: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10
- Mark as Required: Yes

**Submit button**:
- Button text: "Send My Zone Card"
- Button color: `#143B28` (deep forest green) — enter this hex code in the button color picker
- Button text color: `#F5EDD6` (warm cream)

**Trust text below button** (add a text block below the form):
"No spam. Unsubscribe anytime. Seedwarden sends one email per week about growing, foraging, and real food."
Style: small font (12–14px), gray text, center-aligned.

**Background color**: If the template supports hex input, set to `#F5EDD6` (warm cream). If not, white is acceptable — do not use a dark background; it will not match the product card aesthetic.

### Step 3.3 — Map the Zone Dropdown to Kit Tags

The zone dropdown must trigger the correct zone-specific email delivery when a subscriber submits the form. Kit handles this via an automation rule.

**In the form editor**: look for a "Settings," "Automation," or "Actions on submit" option within the form section. If the form editor has per-field options: select the Growing Zone dropdown field > look for "Apply tag based on value" or "Trigger automation based on value."

Configure:
- If value = "Zone 3" → Apply tag `zone-3`
- If value = "Zone 4" → Apply tag `zone-4`
- (Continue for Zones 5 through 10)

**If per-field tag logic is not available in the form editor** (depends on Kit tier): configure this logic in the automation (Step 4.3 in `kit-account-setup-guide.md`). The automation checks the zone custom field after form submission and applies the correct zone tag. Either approach results in the correct zone tag being applied — the form-level approach is simpler; the automation-level approach is equivalent.

### Step 3.4 — Confirm Form → Email Sequence Connection

Before publishing: verify that the form is connected to the "Seedwarden Welcome" email sequence (if the sequence is already built) or that the automation trigger is set to fire on this form submission.

Kit > Settings within the landing page editor: look for "Send subscribers to a sequence" or "On form submit, add to: [sequence name]." Select "Seedwarden Welcome" if it exists.

If the sequence is not built yet: publish the landing page now and connect the sequence after building it. Subscribers who sign up before the sequence is connected will not receive emails automatically — you will need to manually trigger the sequence for those subscribers. Build the sequence as early as possible (target: before May 28).

### Step 3.5 — Publish and Record the URL

Click "Publish." Kit generates a landing page URL. This URL is the link you will add to every social bio and email footer.

**Kit URL formats**:
- Default: `kit.com/[account-slug]/[page-slug]` — this is the standard free-tier URL
- Custom subdomain: `[your-slug].ck.page/[page-slug]` — available on some plans

Copy the published URL and record it:
- In KIT_SETUP_NOTES.md
- In WORKLOG.md
- In a local note labeled "Phase 2 Live URLs"

This URL gets placed in:
- Instagram bio link
- TikTok bio website field
- Pinterest profile website field
- Etsy shop announcement or bio
- All Kit email footers

---

## Part 4: Email List Integration — MailerLite vs. Klaviyo Decision

Seedwarden uses **Kit** as the sole email platform for Phase 2. MailerLite and Klaviyo are not needed.

**When would migration to MailerLite or Klaviyo make sense?**

```
PLATFORM DECISION TREE

Is your Kit free tier at risk of hitting the 10,000 subscriber limit within Phase 2?
  YES → Consider Kit paid tier ($29/month for up to 1,000 subscribers, $49/month for up to 3,000)
        OR migrate to MailerLite ($10/month for up to 1,000 subscribers on Starter plan)
  NO  → Stay on Kit

Do you need Etsy order-triggered automation (e.g., send a product bundle offer
automatically when a subscriber buys a specific product)?
  YES → Consider Klaviyo (native e-commerce integrations, Etsy connection via Zapier)
        Cost: $20/month for up to 500 contacts; $45/month for up to 1,000
  NO  → Stay on Kit

Does Kit lack a feature you need for Phase 2 right now?
  YES → Identify the specific feature and check if Kit's paid tier adds it before migrating
  NO  → Stay on Kit

DECISION: No migration before Phase 3. Kit free tier handles all Phase 2 requirements.
```

**If migration becomes necessary later**:
- MailerLite migration: Export Kit subscriber list as CSV (Kit > Subscribers > Export). Import into MailerLite (Subscribers > Import CSV). Rebuild sequences in MailerLite's automation builder. Migration time: 2–3 hours. No subscriber data loss — tags export with the CSV.
- Klaviyo migration: Same CSV export/import process. Klaviyo's automation builder is more powerful but more complex. Migration time: 3–5 hours.

---

## Part 5: Form Customization

### Form Preview

After publishing, open the landing page in an incognito browser window and fill in the form to verify:
1. All three fields (First Name, Email, Growing Zone) appear and accept input.
2. The dropdown shows Zone 3 through Zone 10 in order.
3. Submitting the form shows a confirmation message or redirects to a thank-you page.
4. The thank-you/confirmation message reads: "Your zone card is on the way — check your inbox in the next minute." (Set this in Kit: landing page editor > Settings > Success message or Redirect URL.)
5. Within 60 seconds: the test email (wanka95+test@gmail.com) receives Email 1 with the correct zone card download link.

### Example Populated Form (for reference)

This is what a correctly filled form looks like:
- First Name: Jessica
- Email: jessica.example@gmail.com
- Growing Zone: Zone 7

After Jessica clicks "Send My Zone Card":
1. Kit creates a subscriber record for jessica.example@gmail.com with name "Jessica" and zone tag "zone-7."
2. Kit's automation fires: adds Jessica to the Seedwarden Welcome sequence.
3. Email 1, Zone 7 variant is sent immediately: subject "Your Zone 7 Quick-Start Card is ready, Jessica."
4. Email 1 body contains a download button linking directly to the Zone 7 PDF on Google Drive.

If any step in this chain does not work during your pre-launch test, diagnose in order: (1) form submission > (2) Kit automation status > (3) Kit sequence status > (4) Email 1 Zone [X] variant exists and zone tag condition is set correctly > (5) Google Drive link is in `?export=download&id=` format with correct file permissions.

---

## Part 6: UTM Parameter Setup for Analytics

UTM parameters track which source drove each Kit sign-up and each Etsy sale. Without UTMs, all traffic appears as "direct" in GA4 and you cannot determine what is working.

### UTM Parameter System

Every outbound link from Seedwarden must include UTM parameters. The standard format:

`[destination-url]?utm_source=[source]&utm_medium=[medium]&utm_campaign=[campaign]&utm_content=[content-identifier]`

**Master UTM reference for Phase 2**:

| Source | Medium | Campaign | Content | When to use |
|---|---|---|---|---|
| kit | email | phase2_launch | broadcast_cta1 | Launch broadcast — primary CTA link |
| kit | email | phase2_launch | broadcast_listing_[product] | Launch broadcast — specific product links |
| kit | email | phase2_nurture | newsletter_[date] | Weekly newsletter links (e.g., newsletter_jun5) |
| instagram | social | phase2_launch | bio_link | Instagram bio link (Kit landing page) |
| tiktok | social | phase2_launch | bio_link | TikTok bio link |
| pinterest | social | phase2_launch | bio_link | Pinterest bio link |
| instagram | social | phase2_content | [post-slug] | Individual post links (use post date as slug) |

### How to Add UTMs in Kit

**For email CTAs**: In Kit's email editor, click on any button or link > edit the URL. Append the UTM string to the URL before saving. Example:

Original Etsy store URL: `https://www.etsy.com/shop/seedwarden`

With UTMs: `https://www.etsy.com/shop/seedwarden?utm_source=kit&utm_medium=email&utm_campaign=phase2_launch&utm_content=broadcast_cta1`

Paste the full URL including UTMs into Kit's link field. Kit does not automatically shorten these URLs — they remain long but functional.

**For social bio links**: When adding your Kit landing page URL to Instagram, TikTok, and Pinterest bios, add UTMs to the URL:

`[kit-landing-url]?utm_source=instagram&utm_medium=social&utm_campaign=phase2_launch&utm_content=bio_link`

Note: Some social platforms strip UTM parameters from bio links during click tracking. To verify whether UTMs are passing through, check GA4 > Acquisition > Traffic Acquisition > Source/Medium after your first social post goes live and generates clicks.

### GA4 Verification

GA4 must be installed on the Kit landing page for UTM tracking to work on sign-ups. Kit's landing page builder supports custom code injection in some tiers.

**If you have a custom domain with GA4 installed**: add your GA4 snippet to the custom domain's global header. All pages (including the Kit landing page if it uses your custom domain) will be tracked.

**If using the Kit default URL** (kit.com/... or [slug].ck.page/...): GA4 cannot be installed on Kit's subdomain directly. In this case, track sign-ups via Kit's own analytics (Kit > Subscribers > Growth over time) and use GA4 for Etsy traffic tracking. UTMs in email links still flow through to GA4 when subscribers click email links and land on Etsy pages (where GA4 is not installed either — see note below).

**Etsy and GA4**: Etsy does not allow GA4 to be installed on individual shop pages. UTM tracking for Etsy traffic works one of two ways:
1. Use Etsy's own traffic report (Shop Manager > Stats > Traffic sources) — this shows referrer but not UTM-level granularity.
2. Create a redirect page on your own domain (e.g., seedwarden.com/shop → redirects to your Etsy store). GA4 captures the click on your domain before the redirect. This is a Phase 3 optimization — not required for Phase 2.

---

## Part 7: Custom Domain Decision

The Kit landing page default URL is either `kit.com/[slug]/[page]` or `[slug].ck.page/[page-name]`. A custom domain (e.g., `seedwarden.com/zone`) provides:

- Brand consistency in the URL
- GA4 tracking capability on the landing page
- Email authentication credibility (subscribers see "from seedwarden.com" not "from kit.com")

```
CUSTOM DOMAIN DECISION TREE

Do you have a registered custom domain (e.g., seedwarden.com)?
  NO  → Use the Kit default URL for Phase 2. Revisit in Phase 3.
        (The Kit URL is fully functional for all Phase 2 goals — this is not a blocker.)
  YES → Continue

Is the domain currently pointing to a website or page?
  YES, it has a live website → Create a subdirectory (seedwarden.com/zone) or subdomain
    (zone.seedwarden.com) to host the Kit landing page without affecting the main site.
    Connect Kit landing page to the subdomain: Kit > Settings > Custom Domains > Add domain.
  NO, domain is registered but pointing nowhere → Point it directly to Kit.
    Kit > Settings > Custom Domains > Add domain > follow Kit's CNAME setup instructions.
    Kit provides: CNAME Host = www, CNAME Target = [kit-provided-target-address].
    Add the CNAME in your domain registrar's DNS panel. Propagation: up to 48 hours.

COST CONSIDERATION:
  Connecting a custom domain to Kit: FREE on all Kit tiers.
  Registering a domain (if not yet owned): approximately $12–$15/year via Namecheap or Google Domains.
  No other costs for the custom domain setup.

VERIFICATION TIMELINE:
  DNS CNAME propagation: 15 minutes to 48 hours.
  Complete this step by May 27 (3 days before launch) to allow for full propagation.
```

**Recommended for Phase 2**: Use the Kit default URL if you do not already own seedwarden.com. Do not purchase a domain purely for Phase 2 — the Kit URL is adequate. Purchase the domain in Phase 3 when consistent branding justifies the investment.

---

## Part 8: End-to-End Test (5 minutes, required before May 30)

Run this test after completing Parts 1–7 (or at any point during setup to verify the pieces work together):

1. Open the Kit landing page URL in an incognito browser (logged out of all accounts).
2. Fill in the form:
   - First Name: Test
   - Email: wanka95+launchday@gmail.com
   - Growing Zone: Zone 5
3. Click "Send My Zone Card."
4. Confirm the thank-you/confirmation message appears.
5. Open Gmail (wanka95@gmail.com). Within 60 seconds, confirm Email 1 arrives.
6. Open Email 1. Click the "Download your Zone 5 card" button.
7. Confirm a PDF downloads (not a viewer page, not a "request access" error, not a Google Drive sharing gate).
8. Open the PDF. Confirm: (a) Zone 5 is identified in the header, (b) the content is the correct zone card, (c) the PDF is not blank or corrupted.
9. Return to Kit > Subscribers. Confirm the test subscriber (wanka95+launchday@gmail.com) appears in the list with:
   - Tag: `zone-5`
   - Tag: `new-subscriber`
   - Sequence: "Seedwarden Welcome" (status: Active)

If all 9 steps complete without issues: the setup is production-ready.

**If step 7 fails** (PDF does not download):
- Go to Google Drive > find the Zone 5 PDF > click "Share" > set to "Anyone with the link can view."
- Copy the share URL. Change the URL format from `drive.google.com/file/d/[ID]/view` to `drive.google.com/uc?export=download&id=[ID]`.
- Paste the corrected URL into Kit Email 1 Zone 5 variant download button. Save. Re-test.

**If step 5 fails** (Email 1 does not arrive within 60 seconds):
- Kit > Automations > find "Seedwarden Welcome Trigger" > check status is "Published" not Paused.
- Kit > Sequences > find "Seedwarden Welcome" > check status is "Published."
- Kit > Subscribers > find wanka95+launchday@gmail.com > check if a sequence is assigned.

---

## Completion Checklist

- [ ] Kit account created with sender name "Seedwarden" and email wanka95@gmail.com
- [ ] API key generated and stored securely
- [ ] SPF record added to DNS (or skipped for @gmail.com senders)
- [ ] DKIM record added to DNS (or skipped for @gmail.com senders)
- [ ] DNS propagation complete (Kit settings show green checkmarks)
- [ ] Zone Quick-Start Card landing page created with headline, subheadline, 3 form fields, submit button, and trust text
- [ ] Zone dropdown options: Zone 3 through Zone 10
- [ ] Zone dropdown mapped to zone tags (form-level or automation-level)
- [ ] Landing page published and URL recorded in KIT_SETUP_NOTES.md and WORKLOG.md
- [ ] Kit landing page URL placed in all social bios (Instagram, TikTok, Pinterest)
- [ ] UTM parameters appended to launch broadcast links
- [ ] Custom domain connected (or Kit default URL accepted for Phase 2)
- [ ] End-to-end test completed and passed: form submission → Email 1 delivery → Zone 5 PDF download

---

*Estimated total time: 50–70 minutes active. DNS propagation (if using custom domain) is passive — complete this step by May 27 at the latest to allow 72 hours for propagation before the May 30 launch. Reference `kit-account-setup-guide.md` for the extended automation sequence configuration (Emails 2–5, behavioral tag rules, newsletter segment setup).*
