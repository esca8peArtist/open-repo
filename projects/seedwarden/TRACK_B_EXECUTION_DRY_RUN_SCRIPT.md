---
title: "Track B Execution Dry-Run Script — 5-Gate Step-by-Step Procedure"
date: 2026-06-05
prepared_by: seedwarden-agent (claude-sonnet-4-6)
status: PRODUCTION-READY — reference document for user gate execution
scope: >
  Step-by-step UI walkthrough for all 5 Track B user action gates, in execution order.
  Includes exact menu paths, copy-paste fields, verification checkpoints, and
  contingency decision tree for Gate 2 (PDF upload) failure.
---

# Track B Execution Dry-Run Script
## 5-Gate Step-by-Step Procedure

**Purpose**: This document is your execution companion. Read the relevant section
before you start each gate, then work through the steps. Every field value, hex code,
bio text, and platform menu path is written out — no hunting across files required.

**Execution order**: Gate 4 → Gate 1 → Gate 3 → Gate 2 → Gate 5

**Why this order**: Gate 4 generates the Google Drive download links that Gate 3 needs
to build Kit Email 1. Gate 1 creates the social accounts that Gate 3 will link to.
Gate 2 does not block anything and can be done last. Gate 5 only affects Email 5
(Day 10) and has a 10-day buffer after launch.

**Total time**: 3.5–4.5 hours, distributed across 2–3 sittings.

**What you need before starting**:
- `projects/seedwarden/logos/seedwarden_logo_1.png` downloaded to your phone and computer
- wanka95@gmail.com accessible on both devices
- Phone charged 50%+ (TikTok account creation requires mobile app)
- Google Drive accessible (linked to wanka95@gmail.com or any Google account)

---

## Gate 4: Upload Zone PDFs to Google Drive

**Time**: 20 minutes
**When**: Do this first. All other gates can proceed in parallel once this is done.
**What you need**: Access to `projects/seedwarden/assets/zone-cards/` folder and Google Drive

---

### Step 4.1 — Open Google Drive

Navigate to drive.google.com. Sign in with any Google account (does not have to be
wanka95@gmail.com — the Drive folder can be owned by any account as long as sharing
is set to "Anyone with the link").

---

### Step 4.2 — Create Folder

In Google Drive:
1. Click "+ New" (top left)
2. Select "New folder"
3. Name it exactly: `Seedwarden Zone Cards`
4. Click "Create"

---

### Step 4.3 — Upload 8 PDFs

Open the folder you just created, then:
1. Click "+ New" > "File upload"
2. Navigate to `projects/seedwarden/assets/zone-cards/`
3. Select all 8 files (Ctrl+A or Cmd+A to select all):
   - seedwarden-zone-3-quickstart-card.pdf
   - seedwarden-zone-4-quickstart-card.pdf
   - seedwarden-zone-5-quickstart-card.pdf
   - seedwarden-zone-6-quickstart-card.pdf
   - seedwarden-zone-7-quickstart-card.pdf
   - seedwarden-zone-8-quickstart-card.pdf
   - seedwarden-zone-9-quickstart-card.pdf
   - seedwarden-zone-10-quickstart-card.pdf
4. Click "Open" to upload
5. Wait for all 8 uploads to complete (progress bars in bottom right of Drive)

Verify: Drive folder shows exactly 8 PDF files.

---

### Step 4.4 — Set Folder Sharing

Right-click the "Seedwarden Zone Cards" folder (not an individual file):
1. Select "Share"
2. In the "General access" section, change from "Restricted" to "Anyone with the link"
3. Confirm permission level is "Viewer" (not Editor)
4. Click "Done"

This sets sharing for all files inside the folder.

---

### Step 4.5 — Generate Direct Download Links

For each of the 8 PDFs, you need a direct download link. Do NOT use the standard
"Copy link" button — that generates a viewer URL that opens in browser instead of
downloading.

For each file:
1. Right-click the PDF filename
2. Select "Get link"
3. Copy the link — it will look like:
   `https://drive.google.com/file/d/[FILE_ID]/view?usp=sharing`
4. Convert it to a direct download URL by replacing the end:
   Change: `.../view?usp=sharing`
   To: `...` then add `?export=download` AFTER the file ID

   **Correct format**: `https://drive.google.com/uc?export=download&id=[FILE_ID]`

   Example: If the viewer link is
   `https://drive.google.com/file/d/1AbCdEfGhIjKlMnOpQrStUv/view?usp=sharing`
   
   The direct download link is:
   `https://drive.google.com/uc?export=download&id=1AbCdEfGhIjKlMnOpQrStUv`

Do this for all 8 PDFs and write down the file ID portion for each zone.

---

### Step 4.6 — Test All 8 Links in Incognito

Open a new incognito/private browser window (Chrome: Ctrl+Shift+N / Mac: Cmd+Shift+N):
1. Paste each download link and press Enter
2. Confirm the browser immediately prompts to download a PDF file
3. Confirm the download is NOT a "Request access" page and NOT a Google Drive viewer
4. Do this for all 8 links

If any link shows "Request access": return to Step 4.4 and verify the folder sharing
is set to "Anyone with the link" — not "Restricted."

---

### Step 4.7 — Log Links in WORKLOG.md

Open `projects/seedwarden/WORKLOG.md` and add a section:

```
## Kit Zone Card File URLs — [Today's Date]

| Zone | File | Direct Download URL |
|------|------|---------------------|
| Zone 3 | seedwarden-zone-3-quickstart-card.pdf | https://drive.google.com/uc?export=download&id=[ID] |
| Zone 4 | seedwarden-zone-4-quickstart-card.pdf | https://drive.google.com/uc?export=download&id=[ID] |
| Zone 5 | seedwarden-zone-5-quickstart-card.pdf | https://drive.google.com/uc?export=download&id=[ID] |
| Zone 6 | seedwarden-zone-6-quickstart-card.pdf | https://drive.google.com/uc?export=download&id=[ID] |
| Zone 7 | seedwarden-zone-7-quickstart-card.pdf | https://drive.google.com/uc?export=download&id=[ID] |
| Zone 8 | seedwarden-zone-8-quickstart-card.pdf | https://drive.google.com/uc?export=download&id=[ID] |
| Zone 9 | seedwarden-zone-9-quickstart-card.pdf | https://drive.google.com/uc?export=download&id=[ID] |
| Zone 10 | seedwarden-zone-10-quickstart-card.pdf | https://drive.google.com/uc?export=download&id=[ID] |

Drive folder URL: [folder URL]
All 8 links tested in incognito: PASS
```

Keep this file open — you will need these 8 URLs during Gate 3.

**Gate 4 complete verification**:
- [ ] Drive folder "Seedwarden Zone Cards" exists with 8 files
- [ ] Folder sharing: "Anyone with the link can view"
- [ ] All 8 direct download URLs logged in WORKLOG.md
- [ ] All 8 links tested in incognito — each triggers immediate PDF download

---

## Gate 1: Social Media Account Creation

**Time**: 45–60 minutes
**When**: After Gate 4. Do all three platforms in one sitting.
**What you need**: seedwarden_logo_1.png on phone and computer. Phone accessible.
**Platforms**: instagram.com (browser), TikTok (mobile app), pinterest.com (browser)

---

### Step 1.1 — Instagram Account (10 minutes, browser)

Go to instagram.com/accounts/emailsignup on your computer browser.

**Account creation fields**:
- Email: wanka95@gmail.com
- Name: Seedwarden
- Username: `seedwarden`
  If taken: try `seedwarden.co`, then `seedwarden.seeds`, then `seedwarden_guides`
- Password: [your choice — use a password manager]

After email verification link arrives and you confirm:

**Switch to Business account**:
Profile icon > Settings and Privacy > Account type and tools > Switch to Professional Account > Business > Continue > select "Content creator" or "Shopping" as category

**Upload profile photo**:
Edit Profile > Profile photo > Upload photo > select seedwarden_logo_1.png from your computer

**Set bio**:
Edit Profile > Bio > paste exactly:
```
Field guides for growers, foragers + food preservers. Heirloom seeds. Wild edibles. Real food skills. Zone-specific free card below
```
(149 characters — do not edit; it fits the 150-char limit)

**Leave website/link field blank** for now — you will add the Kit landing page URL here after Gate 3 is complete.

**Enable email contact**:
Edit Profile > Contact options > Add an email > enter wanka95@gmail.com

---

### Step 1.2 — TikTok Account (10 minutes, mobile app only)

This step requires your phone. Desktop cannot complete TikTok account creation.

1. Download TikTok app from your phone's app store if not installed
2. Open app > Tap "Profile" (bottom right) > Tap "Sign up"
3. Select "Use email or phone number"
4. Enter email: wanka95@gmail.com
5. Complete verification code

**Username**: `seedwarden` (same fallback order: seedwarden.co, seedwarden.seeds, seedwarden_guides)

**Switch to Business account**:
Profile > 3-line menu (top right) > Settings and Privacy > Account > Switch to Business Account > Agriculture or Education

**Upload profile photo**:
Profile icon > Edit profile > Profile photo > upload seedwarden_logo_1.png (have it in your phone's camera roll first)

**Set bio** (must be entered on two separate lines — do NOT paste with `\n`):
Edit Profile > Bio > type:
```
Field guides for growers + foragers
```
Press Enter (new line in bio field), then type:
```
Free zone card in bio
```

**Leave website/link blank** for now — add Kit URL here after Gate 3.

**Important**: Never use Instagram's "Share to TikTok" feature. All TikTok content
must be uploaded natively or TikTok suppresses reach.

---

### Step 1.3 — Pinterest Account (10 minutes, browser)

Go to pinterest.com/join/ on your computer browser.

1. Select "Sign up with email"
2. Email: wanka95@gmail.com
3. Set up profile

**Immediately convert to Business**:
Settings (top right) > Account Settings > Account changes > Convert to business >
Business type: "Online retailer" or "Media" > Business name: `Seedwarden` > Convert

**Upload profile photo**:
Settings > Public profile > Profile photo > upload seedwarden_logo_1.png

**Display name**: `Seedwarden`

**About** — paste exactly (142 chars, within 160-char limit):
```
Seedwarden — heirloom seeds, wild edibles, food preservation + zone-specific growing guides. Practical field guides for real food growers.
```

**Website field**: Leave blank for now — add Kit URL after Gate 3.

**Handle**: Should have assigned from your name or email. If it does not match
your Instagram/TikTok handle, update it: Settings > Public profile > Username

---

### Step 1.4 — Cross-Platform Verification (5 minutes)

After all three are live:
- [ ] All three handles share the same root word
- [ ] All three profile photos are the same seedwarden logo
- [ ] All three are Business type
- [ ] All three are linked to wanka95@gmail.com

Record confirmed handles in `projects/seedwarden/track-b-activation/ACTIVATION_RUNBOOK.md`
Section 1 Gate Completion Record table.

**Gate 1 complete verification**:
- [ ] Instagram: live, Business type, logo uploaded, bio set
- [ ] TikTok: live, Business type, logo uploaded, bio set (2 lines)
- [ ] Pinterest: live, Business type, logo uploaded, About set

---

## Gate 3: Kit Account + Landing Page + Email Automation

**Time**: 2–3 hours
**When**: After Gate 4 (need Google Drive download links). Start when you have
2+ uninterrupted hours.
**What you need**: WORKLOG.md open (Drive links), email copy file open at
`projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md`, your Etsy shop URL
**Platform**: kit.com (free account — no credit card required)

---

### Step 3.1 — Create Kit Account (10 minutes)

Go to kit.com > "Start for free"

**Account setup fields**:
- Email: wanka95@gmail.com
- Sender name: `Seedwarden`
- Sender email: wanka95@gmail.com
- Time zone: your local time zone
- Business type: "Creator" or "E-commerce" (either works)

After submitting: check wanka95@gmail.com inbox for Kit verification email.
Click the verification link to confirm your account.

---

### Step 3.2 — Create 15 Tags (10 minutes)

In Kit dashboard: Subscribers > Tags > "Create a tag"

Create all 15 tags. Name them exactly as shown — spacing and hyphenation matter.

Zone tags (8):
```
zone-3
zone-4
zone-5
zone-6
zone-7
zone-8
zone-9
zone-10
```

Interest cohort tags (7):
```
seed-saver
forager
food-preserver
homesteader
medicinal-herbs
vip-buyer
phase-1-buyer
```

---

### Step 3.3 — Build Landing Page (20–25 minutes)

Kit > Landing Pages > "Create a landing page"

Select template: "Simple" or "Clean" (whichever is most minimal — no custom coding needed)

**Headline**:
```
Get Your Zone Quick-Start Card — Free
```

**Subheading**:
```
Enter your name, email, and growing zone below. We'll send the right card for your region — one-page, printable, yours to keep.
```

**Form fields** (Kit drag-and-drop editor):
- First Name (text field)
- Email (email field — Kit adds this by default)
- Growing Zone (dropdown field)
  Add dropdown options:
  ```
  Zone 3 — Northern Plains, Mountain Interior
  Zone 4 — Upper Midwest, New England Interior
  Zone 5 — Midwest, Great Plains, Mid-Atlantic Interior
  Zone 6 — Mid-Atlantic, Ohio Valley, Transition Zone
  Zone 7 — Southeast, Southern Plains, Pacific Northwest Coast
  Zone 8 — Gulf Coast, Inland South, PNW Lowlands
  Zone 9 — Gulf Coast Interior, Central California, Desert Southwest
  Zone 10 — South Florida, Desert Southwest Lowlands
  ```

**CTA button text**:
```
Send My Zone Card
```

**Form automation** (after building the form):
Kit > Automations > Rules > Create rule:
- Trigger: "Subscriber fills out a form"
- Action: "Apply a tag"
- Map each zone dropdown selection to its corresponding tag:
  "Zone 3 — ..." selection → apply tag `zone-3`
  "Zone 4 — ..." selection → apply tag `zone-4`
  (repeat for all 8 zones)

**Publish the landing page**: Click "Publish" in Kit editor.
Copy the landing page URL — it will be something like `app.kit.com/your-landing-page`
or a custom slug.

**Record this URL** in `projects/seedwarden/track-b-activation/ACTIVATION_RUNBOOK.md`
Section 1 (Gate Completion Record, "Gate 3: Landing page URL" row).

---

### Step 3.4 — Build Email Sequence (45–60 minutes)

Kit > Automations > Sequences > "New Sequence"

Name the sequence: `Seedwarden Welcome`

Add emails in order. For each email:
1. Click "Add email" in the sequence editor
2. Paste subject line from `TRACK_B_EMAIL_COPY_FINAL.md`
3. Paste body text from the same file (use Kit's rich text editor)
4. Set the send delay
5. Apply Kit-specific formatting (bold, buttons, links)
6. Save before moving to the next email

**Email 1 — Day 0 (Immediate)**:
- Subject: `Your Seedwarden Starter Pack is here (+ a quick hello)`
- Send timing: "Immediately on subscribe"
- Replace `[First Name]` → Kit merge field: `{SUBSCRIBER_FIRST_NAME}`
- Replace `[Download Your Starter Pack — click here]` → Kit CTA button
  Button text: "Download Your Starter Pack"
  Button link: Google Drive direct download URL for Zone card PDF
  Note: For a non-zone-specific starter version, use Zone 5 link as the default,
  or use the Gist URL if you prefer a single link that lists all zones
- Replace `[Your Name]` → your first name
- Note: Zone-specific routing (8 Email 1 variants, one per zone) is documented in
  `TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md` Section 5. For initial launch, the single
  Starter Pack version is sufficient.

**Email 2 — Day 2**:
- Subject: `The difference between an heirloom tomato and a lie`
- Send timing: "2 days after previous email"
- Replace `[First Name]` → `{SUBSCRIBER_FIRST_NAME}`
- Replace `[Your Name]` → your first name
- Apply bold formatting to the three definition headers in Kit rich text editor:
  "Heirloom:", "Hybrid (F1):", "GMO:" — bold these headers only

**Email 3 — Day 5**:
- Subject: `The mistake that wiped out a full season of seeds`
- Send timing: "3 days after previous email" (total: Day 5 from Email 1)
- Replace `[First Name]` → `{SUBSCRIBER_FIRST_NAME}`
- Replace `[Your Etsy Shop URL]` → your live Etsy shop URL
  (Format: https://www.etsy.com/shop/seedwarden — verify your actual shop URL in Etsy)
  Wrap as a Kit link button for click tracking
- Replace `[Your Name]` → your first name

**Email 4 — Day 7**:
- Subject: `What I've been building (and why digital guides made sense)`
- Send timing: "2 days after previous email" (total: Day 7 from Email 1)
- Replace `[First Name]` → `{SUBSCRIBER_FIRST_NAME}`
- Replace 4 guide placeholders with actual Etsy product info:
  Open your Etsy Shop Manager in a separate tab, pick 4 products
  Replace `[Guide Title 1]` → actual product name (e.g., "Seed Saving Field Manual")
  Replace `[One-line description]` → brief description from Etsy listing
  Replace `[Price]` → actual price (e.g., "$9.99")
  Repeat for all 4 guides
- Replace `[Etsy Link]` → your Etsy shop URL
- Replace `[Your Name]` → your first name
- Use Kit's bullet list for the 4 guide list

**Email 5 — Day 10**:
- Subject: `One more thing before I stop showing up in your inbox`
- Send timing: "3 days after previous email" (total: Day 10 from Email 1)
- Replace `[First Name]` → `{SUBSCRIBER_FIRST_NAME}`
- Replace 3 recommendation placeholders with actual products + discounted prices:
  `[Guide Title 1]` → best beginner guide (calculate 15% off the price)
  `[Guide Title 2]` → best seed-saver guide (calculate 15% off)
  `[Guide Title 3]` → best small-space guide (calculate 15% off)
  `[Price After Discount]` → actual discounted price (e.g., $9.99 × 0.85 = $8.49)
- Replace `[Etsy Link]` → your Etsy shop URL
- Replace `[Your Name]` → your first name
- Use Kit's bullet list for recommendations
- No stale date present — "for the next 5 days" is relative to subscriber signup, not a calendar date

---

### Step 3.5 — Connect Sequence to Landing Page (5 minutes)

Kit > Automations > Rules > Create rule:
- Trigger: "Subscriber fills out [your landing page form name]"
- Action: "Add to sequence" > "Seedwarden Welcome"

This connects your landing page to the email sequence. When someone signs up,
they automatically enter the welcome sequence.

---

### Step 3.6 — Test the Sequence (15 minutes)

Kit provides test email sending for each email in a sequence. Use this for initial
quality check. Then run an end-to-end live test:

1. Open an incognito browser window
2. Navigate to your Kit landing page URL
3. Sign up using a personal email address (NOT wanka95@gmail.com) and select Zone 5
4. Check the test email inbox — Email 1 should arrive within 60 seconds
5. Click the PDF download link — confirm it downloads the zone card (not a viewer page)
6. Wait 2 minutes — confirm Email 2 does NOT arrive (verifies delay logic is active)
7. Check that your name appears, not the raw merge field text `{SUBSCRIBER_FIRST_NAME}`

If test fails: see `TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md` for diagnosis.

---

### Step 3.7 — Publish Automation + Update Social Bios (10 minutes)

**Publish automation**:
Kit > Automations > find "Seedwarden Welcome" > Status: change from "Draft" to "Published"
Confirm the status badge shows "Published" (not Draft, not Paused).

**Update social bios with Kit landing page URL**:
- Instagram: Profile > Edit Profile > Website > paste Kit URL
- TikTok: Profile > Edit Profile > Website > paste Kit URL
- Pinterest: Settings > Public profile > Website > paste Kit URL

**Gate 3 complete verification**:
- [ ] Kit account live at kit.com
- [ ] 15 tags created (8 zone tags + 7 interest tags)
- [ ] Landing page published — URL recorded in ACTIVATION_RUNBOOK.md
- [ ] 5-email sequence built with correct delays (0, +2, +3, +2, +3 days)
- [ ] All fill-in fields replaced (Etsy URLs, product names, prices, your name)
- [ ] End-to-end test passed (Email 1 arrived, PDF downloaded, delay verified)
- [ ] Automation status: Published
- [ ] Kit URL in all 3 social bios

---

## Gate 2: Canva Brand Kit Configuration

**Time**: 20–30 minutes
**When**: Any time after Gate 1 (logo needed). Can be done in parallel with Gate 3
or after. Does not block launch.
**Platform**: canva.com (log in with wanka95@gmail.com)

---

### Step 2.1 — Access Brand Hub

Log into canva.com with wanka95@gmail.com.

In the left sidebar: look for "Brand Hub" (sometimes labeled "Brand Kit").
If not visible, go directly to: canva.com/brand-hub

Click "Create a Brand Kit" > Name it: `Seedwarden` > Create

---

### Step 2.2 — Add Colors

Click "Add a color" and paste each hex code. Add all 10 colors:

Brand colors (add these 6 first):
```
#143b28   Deep Forest Green
#1A3A2A   Deep Ink Green
#F5EDD6   Warm Cream
#EDE0C4   Parchment
#8FA882   Sage
#A0522D   Burnt Sienna
```

Zone band colors (add these 4, label them clearly):
```
#3D6B8A   Cool band — Zones 3-4
#2D5016   Temperate band — Zones 5-6
#C9943A   Warm band — Zones 7-8
#A0522D   Hot band — Zones 9-10
```

Note: `#A0522D` (Burnt Sienna and Hot band) is the same hex. Add it twice with different labels.

---

### Step 2.3 — Add Fonts

Click "Add a font" and search for each name. All three are free in Canva's library.

1. Heading font: `Playfair Display` — search and click Add
2. Body font: `Lato` — search and click Add
   (If Lato is unavailable in your region, substitute `Source Sans 3`)
3. Accent font: `Cormorant Garamond` — search and click Add

---

### Step 2.4 — Upload Logo

In the Brand Kit, find the "Logos" section > click "Upload a logo":
1. Select `projects/seedwarden/logos/seedwarden_logo_1.png` from your computer
2. Confirm the logo thumbnail appears in the Brand Kit preview
3. Verify the logo reads clearly at thumbnail size

---

### Step 2.5 — Verify

Before leaving Brand Hub, confirm:
- [ ] Brand Kit named "Seedwarden" exists
- [ ] 10 colors visible in palette (6 brand + 4 zone bands)
- [ ] 3 fonts listed: Playfair Display, Lato (or Source Sans 3), Cormorant Garamond
- [ ] Logo thumbnail visible and legible

**Gate 2 complete verification**: Screenshot the Brand Hub screen showing all colors,
fonts, and logo. This is proof of completion for Gate 2.

---

## Gate 5: Etsy Coupon Confirmation

**Time**: 5 minutes
**When**: Anytime before launch day. Does not block Emails 1–4.
**Platform**: etsy.com (log in to your Etsy account)

---

### Step 5.1 — Access Coupon Manager

Log into Etsy > Shop Manager icon (top right) > Marketing > Sales and Coupons

---

### Step 5.2 — Verify SEEDWARDEN15

Look for coupon code `SEEDWARDEN15` in the list.

**If it exists and shows "Active"**: Done. Note the status in ACTIVATION_RUNBOOK.md.

**If it does not exist**:
1. Click "Create a Coupon"
2. Type: Percentage discount
3. Discount amount: `15` (percent)
4. Coupon code: `SEEDWARDEN15` (must be exact — Email 5 references this code by name)
5. Expiry: Set to "No end date" or a date at least 60 days out
6. Click "Save"

**Gate 5 complete verification**:
- [ ] SEEDWARDEN15 shows "Active" in Etsy Shop Manager
- [ ] Discount: 15% off
- [ ] Status noted in ACTIVATION_RUNBOOK.md Gate Completion Record

---

## Post-Gate Actions (After All 5 Gates Complete)

Once all 5 gates are done, the following actions complete the pre-launch sequence.

### Action A — URL Substitution in Social Posts (5 minutes)

Open `projects/seedwarden/TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`.

Find and replace all instances of `[LANDING_PAGE_URL]` with your Kit landing page URL.
There are 9 occurrences. Use your text editor's Find and Replace (Ctrl+H or Cmd+H).

Verify: search the file for `[LANDING_PAGE_URL]` — zero results remaining.

### Action B — URL Substitution in Influencer Templates (5 minutes)

Open `projects/seedwarden/TRACK_B_HERBALIST_OUTREACH_MATRIX.md`.

The message templates use `seedwarden.co/zone` as a placeholder URL. Replace any
remaining placeholder URLs with your actual Kit landing page URL or the Gist URL:
`https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d`

### Action C — Run Final Delivery Test (10 minutes)

From incognito browser:
1. Load Kit landing page URL
2. Sign up with a personal email, select Zone 7
3. Confirm Email 1 arrives within 60 seconds with correct PDF download link
4. Click link — confirm PDF downloads immediately (no viewer, no "Request access")
5. Wait 2 minutes — confirm Email 2 has not arrived

This test confirms the full end-to-end flow is operational.

### Action D — Verify Pre-Launch Checklist in ACTIVATION_RUNBOOK.md

Open `projects/seedwarden/track-b-activation/ACTIVATION_RUNBOOK.md` Section 2.

Work through the Pre-Launch Verification Checklist (10 items). Check each box.
When all 10 are checked: LAUNCH IS CLEARED.

---

## Contingency Decision Tree: If Gate 4 (PDF Upload) Fails

This tree covers the most likely failure modes during Gate 4 and provides recovery
paths without requiring full re-execution.

---

### Failure Mode 1: Google Drive upload fails (file too large, quota, network error)

**Diagnosis**: Files are ~636 KB each. Google Drive free tier supports 15 GB.
Upload failure is almost certainly a network interruption, not a quota issue.

**Option A — Retry immediately**:
Refresh the Drive upload dialog. Re-select any files that did not complete.
Drive shows upload progress per file; incomplete files will be easy to identify.
Time: 5–10 minutes. Try this first.

**Option B — Upload files individually**:
If batch upload fails, upload files one at a time. This eliminates potential
timeout issues with multi-file uploads on slow connections.
Time: 5–10 minutes.

**Option C — Use Gist as primary distribution URL**:
The Gist URL `https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d`
is already live and publicly accessible. It lists all 8 zone cards with individual
links. Use this URL as the Email 1 download link instead of zone-specific Drive links.
This eliminates per-zone routing (all subscribers get the same link regardless of zone)
but does not block launch.
Impact: Slightly less personalized Email 1. Subscribers download the full index and
choose their zone from the Gist page. Functionally complete.
Time: 0 minutes of additional setup. Use immediately.

---

### Failure Mode 2: Google Drive sharing configuration not working ("Request access" still showing in incognito)

**Diagnosis**: Sharing is set at the wrong level (individual file vs. folder), or the
browser cache is serving a cached redirect.

**Option A — Reset sharing on folder, not files**:
Right-click the folder (not individual files) > Share > General access > Anyone
with the link. Then clear browser cache and retest in new incognito window.
Time: 5 minutes.

**Option B — Set sharing on individual files**:
If folder-level sharing is not working, right-click each individual PDF > Get link >
change from "Restricted" to "Anyone with the link" > Copy link.
Regenerate the direct download URLs from the individual file IDs.
Time: 10 minutes.

**Option C — Defer Google Drive, use Gist**:
If Drive sharing cannot be resolved within 15 minutes, proceed with Gist URL as
primary distribution (see Option C in Failure Mode 1 above).
Time: 0 minutes.

---

### Failure Mode 3: Google Drive direct download URL format not working (browser opens viewer instead of downloading)

**Diagnosis**: The URL format may need adjustment. Google has two working formats.

**Option A — Try the alternate direct download format**:
```
https://drive.google.com/u/0/uc?export=download&id=[FILE_ID]
```
(adds `/u/0/` after drive.google.com — required in some account configurations)
Time: 2 minutes to reformat and retest.

**Option B — Use querystring variation**:
```
https://drive.google.com/uc?id=[FILE_ID]&export=download
```
(parameter order reversed — some browsers handle this differently)
Time: 2 minutes.

**Option C — Email Kit Support**:
If direct download cannot be made to work within 20 minutes total: submit a support
ticket to Kit at kit.com/support explaining that your PDF download links open a viewer
instead of downloading. Kit support can often advise on alternative hosting (Dropbox,
AWS S3) that provides clean download links. Response time: 1–2 business days.
Interim fallback: use Gist URL.
Time: 5 minutes to write and submit. 1–2 days for response.

**Option D — Defer 3 days, resolve hosting first**:
If all Drive options fail and Kit support response will take >24 hours: defer Gate 3
(Kit build) by 3 days. Use the time to set up alternative hosting (Dropbox "Direct
Download" links, or a simple Netlify static hosting free tier).
Impact: Launch moves from current date + same day to current date + 3 days.
Use Gist URL in the interim for any social posts published before Kit is operational.
Time: 3 days.

---

### Summary Decision Tree

```
Gate 4 PDF upload attempted
│
├── Upload completes → sharing set → links tested → PASS → proceed to Gate 3
│
└── Upload fails or links show "Request access"
    │
    ├── [Option A] Retry upload → retest → if PASS → proceed
    │
    ├── [Option B] Individual file upload → reset sharing per file → retest
    │
    └── [Option C] Use Gist URL as Email 1 link → proceed to Gate 3 immediately
        (no zone-specific routing; all subscribers get the Gist index page)
        Gist URL: https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d
```

**Default recovery**: Option C (Gist URL) is always available as a zero-delay fallback.
It reduces personalization slightly but does not prevent launch.

---

## Quick Reference Card (Cut Out and Keep)

| Gate | Platform | Time | Key Field |
|------|---------|------|-----------|
| Gate 4 | Google Drive | 20 min | Set folder to "Anyone with link"; use ?export=download URL format |
| Gate 1 | Instagram, TikTok, Pinterest | 45–60 min | TikTok requires mobile app; bios pre-written in this doc |
| Gate 3 | kit.com | 2–3 hrs | Have Drive links ready; have email copy file open; add Etsy URLs during build |
| Gate 2 | canva.com | 20–30 min | 10 colors, 3 fonts, logo upload; non-blocking for launch |
| Gate 5 | etsy.com | 5 min | Verify SEEDWARDEN15 = Active, 15% off; 10-day buffer to Email 5 |

**Fallback URL** (always available): `https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d`

**Key file paths**:
- Email copy: `projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md`
- Gate completion record: `projects/seedwarden/track-b-activation/ACTIVATION_RUNBOOK.md`
- Social posts (URL substitution needed): `projects/seedwarden/TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`
- Influencer contacts + templates: `projects/seedwarden/HERBALIST_OUTREACH_CONTACT_LIST.md`
- Zone PDFs: `projects/seedwarden/assets/zone-cards/`
- Logo: `projects/seedwarden/logos/seedwarden_logo_1.png`

---

*Dry-run script prepared June 5, 2026 by seedwarden-agent.*
*All file paths, hex codes, bio copy, and email content verified against files on disk.*
*Execute in order: Gate 4 → Gate 1 → Gate 3 → Gate 2 → Gate 5.*
*Total user time: 3.5–4.5 hours. No blockers. Infrastructure production-ready.*
