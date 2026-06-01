---
title: "Gate 1 Launch Sequence Checklist — Step-by-Step Execution Plan"
date: 2026-06-01
prepared_by: seedwarden-agent (claude-sonnet-4-6)
status: READY — execute when user approves Gate 1 activation
scope: "Step-by-step execution plan from gate activation through launch day, June 2026"
---

# Gate 1 Launch Sequence Checklist

**Purpose**: Step-by-step guide for everything from user gates to launch day.  
**When to use**: The moment you decide to activate. Work through each section in order.  
**Total time**: 3.5–4.5 hours for all 5 gates + 3.5–4.0 hours on launch day.

---

## Pre-Gate Prerequisites (5 minutes, do before starting)

Before opening any platform:

- [ ] Have `projects/seedwarden/logos/seedwarden_logo_1.png` downloaded to your phone  
- [ ] Have `projects/seedwarden/logos/seedwarden_logo_1.png` downloaded to your computer  
- [ ] Gmail wanka95@gmail.com is open and accessible  
- [ ] TikTok app installed on phone (account creation is mobile-only — desktop will not work)  
- [ ] Phone charged above 50% or plugged in  
- [ ] `track-b-activation/READINESS_REPORT_JUNE_1.md` open in another tab for reference  
- [ ] `track-b-activation/ACTIVATION_RUNBOOK.md` open — you will fill in the Gate Completion Record as you go  
- [ ] 4-hour uninterrupted window blocked on your calendar  

---

## Gate 4 — Google Drive PDF Upload (Do First)

**Time**: 20 minutes  
**Why first**: Kit Email 1 needs the Drive download links. Gate 3 cannot be fully built without them.

- [ ] Open Google Drive in browser (drive.google.com)  
- [ ] Create a folder named "Seedwarden Zone Cards"  
- [ ] Upload all 8 PDFs from `projects/seedwarden/assets/zone-cards/`:
  - [ ] seedwarden-zone-3-quickstart-card.pdf  
  - [ ] seedwarden-zone-4-quickstart-card.pdf  
  - [ ] seedwarden-zone-5-quickstart-card.pdf  
  - [ ] seedwarden-zone-6-quickstart-card.pdf  
  - [ ] seedwarden-zone-7-quickstart-card.pdf  
  - [ ] seedwarden-zone-8-quickstart-card.pdf  
  - [ ] seedwarden-zone-9-quickstart-card.pdf  
  - [ ] seedwarden-zone-10-quickstart-card.pdf  
- [ ] Set folder sharing to "Anyone with the link can view"  
- [ ] For each file, get the FILE_ID from the share link and construct the download URL:  
  `https://drive.google.com/uc?export=download&id=[FILE_ID]`  
  (NOT the standard /file/d/[ID]/view format — that opens a viewer, not a download)  
- [ ] Test all 8 download links in an incognito browser window — each must trigger a PDF download  
  with no "Request access" error  
- [ ] Log all 8 links in `WORKLOG.md` under a new section "Kit Zone Card File URLs — Gate 4"  
- [ ] Record Drive folder URL in ACTIVATION_RUNBOOK.md Gate Completion Record  

**Gate 4 verification**: 8 links tested in incognito, all download correctly, all logged in WORKLOG.md.

---

## Gate 1 — Social Media Accounts (45–60 minutes)

**Platform order**: Instagram (desktop) → TikTok (phone) → Pinterest (desktop)  
**Note**: Do all three in one sitting with the logo file already downloaded.

### Instagram

- [ ] Go to instagram.com/accounts/emailsignup  
- [ ] Sign up with wanka95@gmail.com  
- [ ] Attempt handle: `seedwarden` (fallbacks: `seedwarden.co`, `seedwarden.seeds`, `seedwarden_guides`)  
- [ ] Switch to Business account: Profile > Edit Profile > Account type > Switch to Professional  
- [ ] Business category: Agriculture  
- [ ] Upload profile photo: `seedwarden_logo_1.png`  
- [ ] Bio (copy exactly — 150-char limit):  
  `Field guides for growers, foragers + food preservers. Heirloom seeds. Wild edibles. Real food skills. Zone-specific free card below`  
- [ ] Leave bio link BLANK (you will add Kit URL after Gate 3)  
- [ ] Check Gmail spam folder — Instagram verification email may land there  
- [ ] Record handle and profile URL in ACTIVATION_RUNBOOK.md Gate Completion Record  

### TikTok (phone required)

- [ ] Open TikTok app on phone  
- [ ] Sign up > Use Phone or Email > Email: wanka95@gmail.com  
- [ ] Birthday: (enter your actual birthday to avoid content restrictions)  
- [ ] Attempt handle: `seedwarden` (same fallback priority as Instagram)  
- [ ] Switch to Business account: Profile > Three dots > Creator Tools > Switch to Business Account  
- [ ] Business category: Agriculture or Education (whichever is available)  
- [ ] Upload profile photo: `seedwarden_logo_1.png`  
- [ ] Bio (80-char limit, 2 lines — type manually, press Enter between lines):  
  Line 1: `Field guides for growers + foragers`  
  (press Enter)  
  Line 2: `Free zone card in bio`  
- [ ] Leave bio link BLANK (add Kit URL after Gate 3)  
- [ ] Record handle and profile URL in ACTIVATION_RUNBOOK.md  

### Pinterest

- [ ] Go to pinterest.com/join/  
- [ ] Sign up with wanka95@gmail.com  
- [ ] Convert to Business account: Settings > Account Settings > Convert to Business account  
- [ ] Business name: Seedwarden  
- [ ] Attempt username: `seedwarden` (same fallback priority)  
- [ ] Upload profile photo: `seedwarden_logo_1.png`  
- [ ] About your business (160-char limit):  
  `Seedwarden — heirloom seeds, wild edibles, food preservation + zone-specific growing guides. Practical field guides for real food growers.`  
- [ ] Leave website field BLANK (add Kit URL after Gate 3)  
- [ ] Record handle and profile URL in ACTIVATION_RUNBOOK.md  

**Gate 1 verification**: All three accounts show Business account type, identical profile photo,
correct bio text. Record handles in Gate Completion Record.

---

## Gate 3 — Kit Account + Landing Page + Email Automation (2–3 hours)

**This is the critical-path gate.** Kit landing page URL is required before launch posts can go live.  
Full setup procedure: `MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md`  
Email copy: `execution/TRACK_B_EMAIL_COPY_FINAL.md`  
Zone card Drive links: log from Gate 4 in WORKLOG.md (needed for Email 1)

### Kit Account Creation

- [ ] Go to kit.com  
- [ ] Sign up with wanka95@gmail.com  
- [ ] Sender name: Seedwarden  
- [ ] Confirm email verification arrives (check Gmail spam if needed)  
- [ ] Record Kit account URL in ACTIVATION_RUNBOOK.md  

### Create 15 Tags

In Kit > Audience > Tags, create:

- [ ] zone-3  
- [ ] zone-4  
- [ ] zone-5  
- [ ] zone-6  
- [ ] zone-7  
- [ ] zone-8  
- [ ] zone-9  
- [ ] zone-10  
- [ ] seed-saver  
- [ ] forager  
- [ ] food-preserver  
- [ ] homesteader  
- [ ] medicinal-herbs  
- [ ] vip-buyer  
- [ ] phase-1-buyer  

### Build Landing Page

- [ ] Kit > Landing Pages > Create New Landing Page  
- [ ] Headline: "Get Your Zone Quick-Start Card — Free"  
- [ ] Subheading: "Select your USDA growing zone and we'll send you a PDF zone guide — planting windows, seed selection, and preservation timing for your region."  
- [ ] Form fields: First Name, Email, Growing Zone dropdown (options: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10)  
- [ ] CTA button text: "Send My Zone Card"  
- [ ] Publish landing page  
- [ ] Copy the landing page URL  
- [ ] Record Kit landing page URL in ACTIVATION_RUNBOOK.md Gate Completion Record  

### Build 5-Email Automation Sequence

- [ ] Kit > Automations > Sequences > New Sequence  
- [ ] Name: "Seedwarden Welcome"  
- [ ] Build Email 1 (copy from `execution/TRACK_B_EMAIL_COPY_FINAL.md`):  
  - Subject: `Your Seedwarden Starter Pack is here (+ a quick hello)`  
  - Send timing: Immediately on subscribe  
  - Add zone-card download button linked to correct Google Drive download URL (conditional per zone tag, or use Zone 5 as default for initial test)  
  - Replace `[Your Name]` with your first name  
- [ ] Build Email 2:  
  - Subject: `The difference between an heirloom tomato and a lie`  
  - Delay: 2 days after Email 1  
  - No links or buttons  
  - Bold the 3 definition labels: Heirloom, Hybrid (F1), GMO  
- [ ] Build Email 3:  
  - Subject: `The mistake that wiped out a full season of seeds`  
  - Delay: 3 days after Email 2 (Day 5 total)  
  - Replace `[Your Etsy Shop URL]` with live Etsy shop URL  
- [ ] Build Email 4:  
  - Subject: `What I've been building (and why digital guides made sense)`  
  - Delay: 2 days after Email 3 (Day 7 total)  
  - Replace 4 guide title/price placeholders with actual Etsy listings  
  - Add Etsy shop link button  
- [ ] Build Email 5:  
  - Subject: `One more thing before I stop showing up in your inbox`  
  - Delay: 3 days after Email 4 (Day 10 total)  
  - Replace 3 guide recommendation placeholders  
  - Calculate post-discount prices (multiply by 0.85)  
  - Verify SEEDWARDEN15 coupon is active in Etsy before saving (see Gate 5)  
- [ ] Send test email to wanka95@gmail.com for each — verify formatting, links, merge fields  
- [ ] Change automation status from Draft to Published  
- [ ] Record Kit automation status in ACTIVATION_RUNBOOK.md  

### Update Social Bios with Kit URL

After landing page is published:

- [ ] Add Kit landing page URL to Instagram bio link field  
- [ ] Add Kit landing page URL to TikTok bio link field  
- [ ] Add Kit landing page URL to Pinterest website field  

**Gate 3 verification**: Kit Automations screen shows "Seedwarden Welcome" with status Published.
Test signup (using incognito browser) receives correct zone card within 60 seconds.

---

## Gate 2 — Canva Brand Kit (20–30 minutes)

**This gate does not block launch.** Zone cards already exist as PDFs. Brand Kit only enables new
visual content production. Complete it before or alongside Gate 3 — it has no dependency on Kit.

- [ ] Log in at canva.com with wanka95@gmail.com  
- [ ] Navigate: Left sidebar > Brand Hub > Create a Brand Kit > Name: "Seedwarden"  
- [ ] Add 6 brand colors (by hex code):  
  - [ ] #143b28 (Dark Forest)  
  - [ ] #1A3A2A (Deep Olive)  
  - [ ] #F5EDD6 (Parchment Light)  
  - [ ] #EDE0C4 (Parchment Dark)  
  - [ ] #8FA882 (Sage Green)  
  - [ ] #A0522D (Burnt Sienna)  
- [ ] Add 4 zone band colors (these complete the 10-color kit):  
  - [ ] #3D6B8A (Cool Band — Zones 3–4)  
  - [ ] #2D5016 (Temperate Band — Zones 5–6)  
  - [ ] #C9943A (Warm Band — Zones 7–8)  
  - [ ] #A0522D (Hot Band — Zones 9–10 — same hex as Burnt Sienna, add as separate label)  
- [ ] Add 3 fonts: Playfair Display (heading), Lato (body — fallback: Source Sans 3), Cormorant Garamond (accent)  
- [ ] Upload `seedwarden_logo_1.png` as Brand Kit logo  
- [ ] Verify: Brand Kit screen shows 10 colors (Canva may show 9 swatches if it deduplicates  
  the identical Burnt Sienna / Hot Band hex — confirm both labels appear)  
- [ ] Take screenshot for verification record  

**Gate 2 verification**: Brand Hub "Seedwarden" visible with 10 color labels, 3 fonts, logo thumbnail.

---

## Gate 5 — Etsy Coupon Confirmation (5 minutes)

**This gate has a 10-day buffer.** Email 5 fires on Day 10 after signup. You have 10 days from
launch before any subscriber receives the coupon email. Confirm as early as convenient.

- [ ] Log in to Etsy Shop Manager  
- [ ] Navigate: Marketing > Coupons and Sales  
- [ ] Confirm SEEDWARDEN15 is listed and status shows "Active"  
- [ ] Confirm discount: 15% off  
- [ ] If SEEDWARDEN15 is not present: Create it (Marketing > Coupons > Create Coupon > 15% off > Code: SEEDWARDEN15)  
- [ ] Record coupon status in ACTIVATION_RUNBOOK.md  

---

## Pre-Launch Autonomous Sequence (After All 5 Gates Clear)

Once all 5 gates are verified complete, provide the Kit landing page URL to the orchestrator.
The following 7-step autonomous sequence then executes:

1. Replace `[LANDING_PAGE_URL]` in all 18 social post drafts (`TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`)  
2. Replace `[LANDING_PAGE_URL]` in all influencer DM templates (`TRACK_B_HERBALIST_OUTREACH_MATRIX.md`)  
3. Verify Kit automation status shows Published  
4. Run pre-launch delivery test (incognito signup, confirm PDF delivery within 60 seconds)  
5. Verify all 3 social bio links resolve to Kit landing page  
6. Confirm SEEDWARDEN15 coupon status  
7. Prepare scheduling queue (Buffer/Later post times, or manual reminder timestamps)  

After step 7: Pre-launch verification checklist is complete. Proceed to launch day.

---

## Launch Day Sequence

**Reference**: `MAY_30_LAUNCH_DAY_RUNBOOK.md` — read "May 30" as your launch date throughout.

| Time (UTC) | Action |
|------------|--------|
| 07:30 | Log in to all platforms: Kit, Instagram, TikTok, Pinterest, Etsy, Reddit, Buffer/Later |
| 07:38 | Verify all 8 PDFs accessible, Kit shows Published, all 3 bios have Kit URL |
| 07:48 | Send one final test signup through Kit landing page; scan Email 1 for placeholder text |
| 07:53 | GO/HOLD decision: all 3 criteria must be YES (Kit Published, PDFs accessible, bios correct) |
| 08:00 | Post to Reddit r/herbalism (manual only — cannot pre-schedule) |
| 08:05 | Send outreach emails to Tier 1 contacts: Sabrena Gwin (AHG), Susan Leopold (UpS), John Gallagher (LearningHerbs) |
| 08:15 | Send DMs to remaining 12 contacts via platform-specific routes |
| 08:30 | Post Instagram launch post (manual or via Buffer/Later) |
| 08:45 | Upload TikTok launch video natively in app (do NOT cross-post from Instagram) |
| 09:00 | Post Pinterest launch pin (manual or scheduled) |
| 09:30 | First pulse check: Reddit comments, Kit signups, social engagement — log in WORKLOG.md |
| 11:00 | Second pulse check |
| 12:00 | Third pulse check |
| 13:00 | Fourth pulse check |
| 14:30 | Fifth pulse check |
| 16:00 | TikTok boost post if early engagement is strong (optional) |
| 18:00 | Day 1 wrap-up: log Day 0 snapshot metrics to WORKLOG.md, queue Day 2 content |
| 20:00 | Final check, close out launch day |

**Total launch day operator time**: 3.5–4.0 hours spread across the day.

---

## Email Send Sequence and Timing

**Kit broadcast** (to any subscribers already on list before launch): Send manually at 08:00 UTC.  
**Kit automation** (triggered by new signups via landing page): Activates immediately on each signup.

| Outreach type | Method | Timing | Notes |
|---------------|--------|--------|-------|
| Tier 1 email (Sabrena Gwin, AHG) | Email | 08:05 UTC | chapters@americanherbalistsguild.com |
| Tier 1 email (Susan Leopold, UpS) | Email | 08:05 UTC | info@unitedplantsavers.org |
| Tier 1 email (John Gallagher) | Email | 08:05 UTC | partnerships@learningherbs.com |
| Juliet Blankespoor (Chestnut) | Email or Instagram DM | 08:10 UTC | chestnutherbs.com form or @chestnutschoolherbs |
| Herbal Academy Partnerships | Email | 08:10 UTC | partnerships@theherbalacademy.com |
| Reddit modmail (r/herbalism, r/gardening, r/HerbalMedicine) | Reddit modmail | 08:00 UTC | Post to r/herbalism first (130K); modmail first for approval |
| Discord DMs (Materia Medica, Herb Club, The Herbal Haven) | Discord DM | 08:15 UTC | DM to server owner/admin |
| Seattle Herbalism Society | Facebook message | 08:15 UTC | PNW angle, Zones 7–10 |
| AHG Chapter coordinators | Email via Sabrena routing | Day 3+ | Follow Sabrena's response for routing |

**Contingency if any Tier 1 email bounces**: Send to backup Reddit modmail route for that contact.  
**No response after 48 hours**: Send one follow-up ("checking in on the [date] email").

---

## Contingency Triggers

| Situation | Threshold | Action |
|-----------|-----------|--------|
| Kit automation shows Draft at 07:53 UTC | Any | Publish immediately; if cannot, proceed with Gmail manual send as fallback |
| Social bio link missing from any platform | Any | Add it now; delay that platform's post by 15 min |
| PDF download shows "Request access" | Any | Fix Drive sharing to "Anyone with link"; if urgent, use Gist URL |
| Reddit post removed by moderators | Within 60 min | Wait; if not restored, post to r/homesteading and r/foraging |
| TikTok upload fails on web | Any | Use native app upload; do NOT use web upload tool |
| Kit landing page shows error | Any | Check Kit status page; if outage, share Gist URL in bios temporarily |

Full decision trees: `TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md`  
Rollback procedures: `TRACK_B_LAUNCH_DAY_ROLLBACK_PROCEDURES.md`

---

## Post-Launch Schedule (Days 3/7/14 Checkpoints)

| Checkpoint | Date (if June 2 launch) | Key Question |
|------------|------------------------|--------------|
| Day 3 | June 5 | Initial read vs. targets in READINESS_REPORT_JUNE_1.md |
| Day 7 | June 9 | Tier 2 partnership candidates identified from engagement |
| Day 14 | June 16 | Phase 3 GO/GO-with-adjustments/DEFER decision |

Threshold details: `TRACK_B_MONITORING_CHECKPOINTS.md`  
Day 3/7 decision framework: `DAY_3_AND_7_DECISION_GATES.md`

---

*Prepared: 2026-06-01 by seedwarden-agent (claude-sonnet-4-6)*  
*For infrastructure verification context, see `GATE_1_INFRASTRUCTURE_VERIFICATION_CHECKLIST.md`*  
*For monitoring thresholds and decision framework, see `GATE_1_SUCCESS_METRICS_AND_MONITORING.md`*
