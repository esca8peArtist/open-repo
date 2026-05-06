---
title: "Kit Account Setup Guide — Complete Configuration Reference"
date: 2026-05-06
status: production-ready
platform: Kit (kit.co, formerly ConvertKit)
account-email: wanka95@gmail.com
references:
  - KIT_SETUP_NOTES.md
  - PHASE_2_EMAIL_STRATEGY.md
  - phase-2-day-by-day-execution.md
  - marketing/email-and-launch-plan.md
---

# Kit Account Setup Guide
## Complete Configuration Reference for Seedwarden Email Platform

**Purpose**: A complete, standalone guide for setting up the Seedwarden Kit account from first login to live automation. This document supersedes KIT_SETUP_NOTES.md where they overlap — KIT_SETUP_NOTES.md is a working notes file while this is the authoritative configuration reference.

**Time required**: 3–4 hours for a complete first-time setup following this guide. 90 minutes for someone who has used Kit before.

**What is already decided**: Platform selection (Kit free tier), email sequence structure (5-email welcome sequence), segmentation strategy (zone-based + behavioral click tags), and lead magnet delivery method (Google Drive hosted PDFs). These decisions are documented in PHASE_2_EMAIL_STRATEGY.md.

---

## Part 1: Account Creation and Initial Configuration

### Step 1.1 — Account Creation

Navigate to kit.co. Click "Start for free."

Required inputs:
- Email: wanka95@gmail.com
- Password: create a strong password and store in a password manager
- Sender name: Seedwarden
- Time zone: your local time zone (used for scheduled broadcast timing)
- Business type: Creator or E-commerce (either works — select whichever matches Kit's onboarding prompt)

After account creation:
- Confirm the email address via the verification link Kit sends to wanka95@gmail.com.
- Navigate to Settings (gear icon, lower left sidebar) > Profile. Confirm sender name reads "Seedwarden."

**Free tier scope at the time of setup** (confirm at kit.co if this has changed):
- Up to 10,000 subscribers — more than adequate through Phase 3
- Unlimited broadcast emails
- Unlimited automation sequences
- 1 published landing page
- Basic conditional automation logic (zone routing qualifies as basic conditional logic)
- No A/B testing on landing pages (Phase 3 upgrade if needed)

### Step 1.2 — API Key Generation

Kit provides an API key for any future integrations (e.g., Zapier workflows linking Etsy orders to Kit tags). Even if no integration is needed at launch, generate and store the API key now so it is available without a delay if needed.

Navigate to Settings > Developer > API Keys > Add API Key.
- Name: "Seedwarden Main Key"
- Access: Read and Write
- Click "Generate Key." Copy the key and store it in a secure local note alongside the account login. It will not be shown again.

**Do not share this API key** — it grants write access to your subscriber list.

### Step 1.3 — Sender Domain Configuration (SPF, DKIM)

This is the most technically involved step and the most important for deliverability. Do not skip it.

**Why it matters**: Email sent from Kit without SPF/DKIM authentication has a significantly higher probability of landing in subscribers' spam folders. Gmail's spam filter in particular penalizes unauthenticated email from marketing platforms. A list that can't get into inboxes is not a list.

**What you need before starting this step**:
- Access to the DNS settings for your domain registrar. Log into your registrar (Namecheap, GoDaddy, Google Domains, Squarespace, etc.) and locate the DNS management panel for your domain.
- If you do not have a custom domain: proceed with wanka95@gmail.com as the sender address for now. You will still need to configure Gmail-compatible SPF when you add a custom domain later. At this stage, Gmail sender authentication is handled by Google automatically — skip to Step 1.4.

**Adding SPF record** (if custom domain):
In Kit: Settings > Email Settings > Custom Sender Domain. Kit provides the SPF record value to add.
Standard Kit SPF record: `v=spf1 include:sendgrid.net ~all`

If your domain already has an SPF record (check your DNS for an existing TXT record starting with `v=spf1`), merge the Kit value into it rather than adding a second record. DNS only permits one SPF record per domain. Combined example:
`v=spf1 include:_spf.google.com include:sendgrid.net ~all`

In your DNS registrar: Add a TXT record. Host/Name: `@` (root domain). Value: the full SPF string above.

**Adding DKIM record** (if custom domain):
In Kit: Settings > Email Settings > DKIM Signing. Kit provides a CNAME record value.
In your DNS registrar: Add a CNAME record. Host/Name: the string Kit provides (typically something like `k1._domainkey`). Value: the target address Kit provides.

**Propagation and verification**:
DNS changes take 24–48 hours to propagate globally. Kit's Settings > Email Settings panel shows a green checkmark when each record is verified. Check back 24 hours after adding the records.

While awaiting propagation, continue with all other Kit setup steps. DNS verification does not block form creation, sequence building, or automation configuration.

**Test after verification**:
After Kit shows both records as verified: send a test email from Kit to wanka95@gmail.com. Open it in Gmail. Click the three-dot menu > "Show original." Confirm the email header shows `dkim=pass` and `spf=pass` in the Authentication-Results line.

---

## Part 2: Email Template Structure and Zone Architecture

### Step 2.1 — Zone Quick-Start Card Delivery Architecture

The zone card system is the structural core of the Kit setup. Before building any email, understand how the pieces connect:

```
Subscriber fills out landing page form
           ↓
Zone selection stored as custom field "zone"
           ↓
Automation trigger: Form submitted
           ↓
Action 1: Add to Seedwarden Welcome sequence
Action 2: Apply tag "zone-[X]" (based on zone custom field value)
Action 3: Apply tag "new-subscriber"
           ↓
Conditional branch in Email 1:
  IF tag = zone-3 → Send Email 1 Zone 3 variant
  IF tag = zone-4 → Send Email 1 Zone 4 variant
  ...and so on through zone-10
           ↓
Emails 2–5: Identical for all zones (zone-agnostic content)
```

This architecture uses the zone dropdown on the sign-up form as the pivot for all personalization. Every piece of personalization in Phase 2 flows from this single form field.

### Step 2.2 — Building the Zone Custom Field

Navigate to Subscribers > Custom Fields > Create a Custom Field.
- Name: "Growing Zone"
- Type: Text (or Dropdown if Kit's form editor maps dropdown fields to custom fields — verify in Kit's current UI)
- This field stores the value the subscriber selects ("Zone 3," "Zone 4," etc.)

When the sign-up form is built in Step 3, this custom field is mapped to the zone dropdown input. Kit stores the selected value automatically.

### Step 2.3 — Tag Taxonomy

Create all tags before building any automation. Tag creation order matters — creating tags before building automations ensures the automation's tag-based conditional branches find the tags they reference.

Navigate to Subscribers > Tags > Add a Tag. Create each tag below:

**Zone routing tags** (applied via automation based on zone form field):
| Tag | Applied when |
|---|---|
| zone-3 | Subscriber selects Zone 3 on form |
| zone-4 | Subscriber selects Zone 4 |
| zone-5 | Subscriber selects Zone 5 |
| zone-6 | Subscriber selects Zone 6 |
| zone-7 | Subscriber selects Zone 7 |
| zone-8 | Subscriber selects Zone 8 |
| zone-9 | Subscriber selects Zone 9 |
| zone-10 | Subscriber selects Zone 10 |

**Behavioral segment tags** (applied via click triggers in emails):
| Tag | Applied when |
|---|---|
| seed-saver | Clicks Seed Saving Manual link (Email 3) OR food sovereignty link (Email 4) |
| city-grower | Clicks apartment/container growing link (Email 4) |
| preservationist | Clicks preservation/canning link (Email 4) |
| forager | Clicks any wild plants or foraging link |

**Lifecycle tags** (applied via automation actions):
| Tag | Applied when |
|---|---|
| new-subscriber | Applied on form submission |
| etsy-buyer | Applied after confirmed Etsy purchase (manual or via integration) |
| gift-buyer | Applied manually based on gift purchase patterns (Phase 3) |

---

## Part 3: Landing Page Configuration

### Step 3.1 — Landing Page Build

Navigate to Landing Pages and Forms > Create New > Landing Page.
Select the simplest single-column template available. Minimal aesthetic is correct — Seedwarden's audience responds to directness, not polished marketing design.

**Page configuration**:

Headline: "Your Free Zone Quick-Start Card"
Subheadline: "Know exactly what to plant, when to plant it, and what to do right now in your zone — one-page reference card, free."

Form fields (in this order, required):
1. First Name — "First Name" label, placeholder "Your first name"
2. Email — "Email Address" label, placeholder "Your email"
3. Growing Zone — "Your Growing Zone" label, dropdown type
   - Dropdown values: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10
   - Required field: Yes

Button: "Send My Zone Card"
Button color: Deep Forest Green (#143b28)
Button text color: Warm Cream (#F5EDD6)

Trust text below button (small font, gray): "No spam. Unsubscribe anytime. Seedwarden sends one email per week about growing, foraging, and real food."

Background: Set to #F5EDD6 (Warm Cream) if the template supports hex input without custom CSS. If not, white is acceptable.

### Step 3.2 — Form → Tag Mapping

After building the form, configure the zone dropdown to apply the correct zone tag when submitted:

In Kit's form editor: select the Growing Zone dropdown field > Automation/Actions tab > Add action on submit: "Apply tag based on value."
- If value = "Zone 3" → Apply tag zone-3
- If value = "Zone 4" → Apply tag zone-4
- (Repeat for all 8 zones)

If Kit's free tier does not support value-based tag application directly from the form field: use the Zone routing automation in Step 4.3 instead. The automation approach (check zone custom field value after submission, then apply tag) achieves the same result with one additional step.

### Step 3.3 — Publishing and URL Capture

Click "Publish." Kit generates a URL in the format: `kit.com/[your-account-slug]/[page-name]` or `[your-page-name].kit.com`.

Record this URL in:
- KIT_SETUP_NOTES.md Setup Completion Log
- A local note labeled "Phase 2 Live URLs"
- phase-2-day-by-day-execution.md Day 16 completion block

This URL is placed in:
- Etsy shop bio (Etsy > Shop Manager > Settings > Info and Appearance > Shop Announcement or Bio)
- Instagram bio link (replace with this URL or add to a Linktree if multiple links are needed)
- TikTok bio link
- Pinterest bio link
- Zone card PDF footers (once cards are built)
- Kit email footer (all 5 emails)

---

## Part 4: Automation Sequences

### Step 4.1 — Welcome Sequence Email Structure

Navigate to Sequences > New Sequence. Name: "Seedwarden Welcome."

Build emails in this order (build order, not send order):
1. Email 1 — Zone 5 variant (build first — use as the template for all 7 other zone variants)
2. Email 1 — Zone 6, 7, 8, 3, 4, 9, 10 variants (duplicate and substitute)
3. Email 2
4. Email 3
5. Email 4
6. Email 5

### Step 4.2 — Email 1 Build Spec (Zone 5 Master)

Subject line: "Your Zone 5 Quick-Start Card is ready, {{subscriber.first_name}}"

The `{{subscriber.first_name}}` tag is Kit's merge tag for the subscriber's first name. Kit inserts the actual first name when sending. Confirm this tag works by previewing the email with a test subscriber.

Body (reference marketing/email-and-launch-plan.md Email 1 section for full copy):
- Opening: "Hey {{subscriber.first_name}}, here's your Zone 5 Quick-Start Card."
- Primary CTA: Large button or linked text. Button text: "Download your Zone 5 card." Button color: #143b28. Link: [Google Drive Zone 5 download URL — add after PDFs are uploaded to Drive].
- Brief closing paragraph: 1–2 sentences. Founder voice. Warm, not corporate.
- Email footer: Kit automatically appends unsubscribe link. Add manually above Kit's footer: "Questions? Reply to this email — I read every message."

Delay setting: Send immediately (Day 0).

After building Zone 5 Email 1, duplicate it 7 times. For each duplicate, change:
- Zone number in subject line ("Zone 5" → "Zone 3", etc.)
- Zone number in the opening line
- Download button link (zone-specific Google Drive URL — use placeholder "[ZONE-X-URL]" until PDFs are uploaded)

### Step 4.3 — Zone Routing Automation

Navigate to Automations > New Automation. Name: "Seedwarden Welcome Trigger."

Trigger: Form submitted (select the Zone Quick-Start Card landing page).

Action sequence:
1. Add to sequence: Seedwarden Welcome
2. Apply tag: new-subscriber
3. Condition: If [zone custom field] = "Zone 3" → Apply tag zone-3 AND (if not already handled by form) set Email 1 send as Zone 3 variant
4. Condition: If [zone custom field] = "Zone 4" → same for zone-4
5. (Repeat for all 8 zones)

**Kit's conditional email routing in sequences**:
Kit handles zone-specific email delivery in one of two ways:

Option A (Tag-based routing, simpler): Use automations to apply zone tags. In the Sequence, configure Email 1 to send only to subscribers with a specific zone tag. Each zone variant is a separate email in the sequence, each with an "Only send to subscribers with tag: zone-X" condition. This requires 8 separate Email 1 entries in the sequence.

Option B (Custom field liquid tags, advanced): Use Kit's liquid tag syntax `{% if subscriber.fields.growing_zone == "Zone 5" %}[Zone 5 content]{% endif %}` within a single Email 1 template. This requires one Email 1 with conditional content blocks. More elegant but more fragile — a syntax error silently omits content. Recommended for Phase 3 after the sequence has proven delivery.

**Use Option A for Phase 2 launch.** It is more verbose but more transparent — you can see exactly which variant each subscriber receives.

### Step 4.4 — Emails 2–5 Configuration

**Email 2 (Day 2 delay)**:
Subject: "This tomato changed how I think about seeds." (or copy from marketing/email-and-launch-plan.md)
Content: Heirloom seed philosophy story — the Brandywine origin narrative. Educational, no product links. Ends with a question to reply to ("What's your most prized seed or plant?"). No click tracking needed in this email.
Delay: 2 days after Email 1.

**Email 3 (Day 5 delay)**:
Subject: "The seed saving mistake I made (and how to avoid it)."
Content: Seed saving story — vulnerability first, practical lesson second. Key link: Seed Saving Field Manual Etsy listing (UTM-tagged). Configure this link with a click trigger:
- In Kit's email editor: add the link, then enable "Add a tag on click." Tag to apply: seed-saver.
This tag is applied automatically to any subscriber who clicks that link. No manual action required.
Delay: 5 days after Email 1.

**Email 4 (Day 7 delay)**:
Subject: "What kind of grower are you?" (or variant from email-and-launch-plan.md)
Content: Catalog introduction — three paths, three link CTAs. Configure each link with its click trigger:
- Apartment/container growing link → Apply tag: city-grower on click
- Seed saving / food sovereignty link → Apply tag: seed-saver on click
- Food preservation link → Apply tag: preservationist on click

All three links are Etsy listing links, UTM-tagged for GA4 attribution.
Delay: 7 days after Email 1.

**Email 5 (Day 10 delay)**:
Subject: "A note from Seedwarden (and something I don't usually do)."
Content: First offer. SEEDWARDEN15 coupon. Frame as genuine gesture, not a countdown-timer sales pitch. Three product recommendations based on the subscriber's behavioral tags — if Kit's conditional content is available on free tier, show different products based on segment tag. If not, use the three highest-converting Phase 1 products as universal recommendations.
Delay: 10 days after Email 1.

Confirm SEEDWARDEN15 is active in Etsy before this email reaches any real subscriber (i.e., before May 25 if the automation goes live May 25 — the first subscriber to complete Day 10 arrives on June 4).

### Step 4.5 — Post-Purchase Sequence (Phase 2 / deferred to list-size threshold)

Do not build the post-purchase sequence before the Phase 2 list reaches 50 active buyers. The sequence architecture is documented in marketing/email-automation-blueprint.md. Build it when there are enough real buyers to justify the setup time.

The trigger for post-purchase sequence: Etsy purchase → Kit tag "etsy-buyer" applied → Sequence enrollment. Etsy does not natively integrate with Kit — the etsy-buyer tag is applied manually (check Etsy orders daily and manually add the etsy-buyer tag to the subscriber's Kit profile if their email matches) or via a Zapier automation (Etsy new order → Kit add tag). Zapier's free plan supports this workflow.

---

## Part 5: Form Integration — Etsy Customer Import Strategy

### Step 5.1 — Importing Etsy Customers into Kit

Etsy provides buyer email addresses in downloadable order reports. Buyers who have made purchases can be imported into Kit — however, this requires careful compliance handling.

**Compliance requirement**: Importing Etsy buyers into Kit requires that they have given some form of consent to receive email from Seedwarden specifically. An Etsy purchase alone does not constitute consent for marketing emails under CAN-SPAM or GDPR.

Compliant import approach:
1. In the post-purchase message to buyers (Etsy automatically sends a receipt, but you can also send a custom message): include an invitation to join the email list. "If you'd like growing tips and a free Zone Quick-Start Card, sign up here: [Kit landing page URL]."
2. Only import email addresses of buyers who click through and complete the Kit sign-up form.
3. Do not bulk-import all Etsy buyer email addresses directly into Kit. This violates Kit's terms of service and GDPR.

**Etsy buyer segment in Kit**:
Buyers who arrive in Kit via the post-purchase invitation should be tagged "etsy-buyer" in addition to their zone tag. This tag enables a future segment: "subscribers who were already buyers before joining the list" — a high-LTV cohort worth tracking separately.

Tag application: In Kit, when a subscriber signs up via the zone card form, their etsy-buyer tag is not applied automatically. Apply it manually after cross-referencing their email with Etsy order data. This is a 5-minute task after each order.

### Step 5.2 — Purchase History Segmentation

As the buyer list grows, track purchase history in customer-analytics.csv rather than in Kit (Kit's free tier does not support custom numeric fields for tracking order counts). The kit tags that matter for segmentation:

| Tag | Meaning for marketing |
|---|---|
| etsy-buyer | Has made at least one Etsy purchase |
| seed-saver | High interest in seed saving products |
| city-grower | High interest in apartment/container products |
| preservationist | High interest in preservation products |

Subscribers tagged both "etsy-buyer" and one segment tag are the highest-value targets for Phase 3 bundle campaigns: they have already bought and have demonstrated a specific interest area.

---

## Part 6: Analytics Configuration

### Step 6.1 — Kit's Built-In Analytics

Kit's analytics dashboard shows, for each sequence email and broadcast:
- Open rate (note: Apple MPP inflates this 20–40% for iOS users)
- Click rate (more reliable than open rate)
- Unsubscribe rate
- Bounce rate

Navigate to: Kit > Analytics > Sequences > Seedwarden Welcome. Review each email's performance here after the first 50 subscribers have passed through it.

**Weekly review cadence**:
Every Thursday (same day as newsletter send if applicable): check sequence performance for the previous 7 days. Record in a new row in customer-analytics.csv:
- Email 1 click rate (zone card download rate — should stay above 40%)
- Email 3 click rate (seed-saver segmentation signal — should be above 15%)
- Email 5 click rate (coupon redemption signal — should be above 8%)

If any metric falls below these thresholds for two consecutive weeks: diagnose the cause before the third week. Possible causes: subject line not opening, link formatting broken, segment content irrelevant to new audience cohort.

### Step 6.2 — Revenue Attribution (Manual Process)

Kit's free tier does not track revenue. Revenue attribution is a manual cross-reference between:
1. Kit broadcast or sequence email send time
2. UTM parameters in email links (identified in GA4 as utm_source=kit)
3. Etsy order date and time

Cross-reference workflow (post-launch weekly):
- Export Kit subscriber list (Subscribers > Export CSV).
- Export Etsy orders for the same period (Etsy Shop Manager > Orders > Export CSV).
- Match subscriber emails to buyer emails.
- For each matched record: note the UTM campaign that drove the click (from GA4 if integrated, or from link click data in Kit broadcasts).
- Record in customer-analytics.csv under the "acquisition_source" column.

This is time-consuming for large lists but fast at Phase 2 scale (50–200 subscribers). Automate it in Phase 3 via a Zapier workflow that writes matched purchase data into a Google Sheet.

### Step 6.3 — Zone-Level Conversion Analysis

Target insight: which zones produce buyers at the highest rate?

At the end of each month: in Kit, filter subscribers by each zone tag. Note total subscribers per zone and total tagged "etsy-buyer" per zone. Calculate conversion rate: etsy-buyer count / zone subscriber count.

Record in a new table in customer-analytics.csv labeled "Zone Conversion by Month."

High-converting zones indicate: strong geographic demand, good match between zone card content and buyer motivation, or well-distributed social reach in that geography. Use this data to prioritize zone-specific content in Phase 3 (more emails, more Pinterest pins, more Etsy listing SEO for that zone's keywords).

---

## Part 7: Troubleshooting

### Issue: API rate limits

Kit's free tier has API rate limits for programmatic operations (Zapier integrations, etc.). Limit: 120 API calls per minute.

For manual Kit operations (building emails, managing subscribers through the UI), rate limits do not apply. Rate limits only affect automated integrations.

If a Zapier workflow hits a rate limit (error: "429 Too Many Requests"): reduce the polling frequency in Zapier's trigger step from "every 5 minutes" to "every 15 minutes."

### Issue: Webhook failures

If a webhook configured to fire on subscriber form submission stops working:
1. Kit > Settings > Integrations > Webhooks > check the last delivery status.
2. If it shows "failed": click "Resend" to test manually.
3. If it continues to fail: check the receiving endpoint URL is still live and accepting POST requests.
4. For Phase 2, no webhooks are required — the zone routing uses Kit's native conditional automation, not external webhooks. This is worth noting: if a Phase 3 integration adds a webhook, do not add it to the same automation as the welcome sequence trigger without testing it in isolation first.

### Issue: Email deliverability problems

Symptoms: open rates below 10% for two consecutive broadcasts, subscriber replies that emails went to spam.

Diagnosis checklist:
- [ ] Confirm SPF record is in DNS (verify at mxtoolbox.com/SPFRecordLookup)
- [ ] Confirm DKIM CNAME is in DNS (verify at mxtoolbox.com/DKIMCheck)
- [ ] Confirm Kit Settings > Email Settings shows green status for both records
- [ ] Check Kit's bounce rate report: a hard bounce rate above 2% damages sender reputation
- [ ] Check unsubscribe rate: above 0.5% per email is a signal that content relevance has dropped
- [ ] Run the From email through mail-tester.com to generate a deliverability score

If SPF/DKIM are configured correctly and deliverability is still poor: consider warming the sending domain. Domain warming means sending to a small engaged segment first, then expanding. Kit does not have a built-in warming tool, but you can manually schedule broadcasts to send to engaged-only segments (subscribers who opened Email 1 within the first week) for the first 4 weeks before sending to the full list.

### Issue: Subscriber tagged with wrong zone

Symptoms: a subscriber reports receiving the Zone 5 card but they signed up for Zone 3.

Cause: the tag applied via the form or automation was incorrect, or the subscriber accidentally selected the wrong zone.

Fix:
1. Navigate to Kit > Subscribers > find the subscriber by email.
2. Remove the incorrect zone tag (e.g., zone-5). Add the correct zone tag (e.g., zone-3).
3. Manually send the correct Email 1 variant: from the subscriber's profile, click "Send Email" > select Email 1 Zone 3 variant.
4. Log the fix in WORKLOG.md.

If this error occurs for more than 2 subscribers in the first week: re-examine the form's tag-mapping configuration. The most common cause is a mismatch between the dropdown value ("Zone 3") and the expected tag trigger format in the automation condition ("zone-3" vs "Zone 3" — case-sensitive in Kit).
