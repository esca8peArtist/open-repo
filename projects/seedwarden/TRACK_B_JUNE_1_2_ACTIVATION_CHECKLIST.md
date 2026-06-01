---
title: "Track B Launch Activation Checklist — June 1-2, 2026"
created: 2026-06-01
status: READY-TO-ACTIVATE
scope: >
  Final pre-launch checklist for Track B zone-card distribution launch.
  Launch was originally targeted May 30; all infrastructure remains
  production-ready and the June 1-2 window is open. Blocked only on
  user action gates (accounts + Kit setup).
---

# Track B Launch Activation Checklist
## June 1-2, 2026

**Launch status**: All infrastructure production-ready. Launch is blocked only on
user action gates listed in Section 1. Once those gates are cleared, the orchestrator
can execute everything in Section 2 autonomously.

**Track A independence**: Track A (Etsy tag corrections) is a separate workstream and
does not block or affect Track B execution. See Section 5 for confirmation.

---

## Deliverable Verification

The following items were verified as of the time this checklist was created (June 1, 2026).

### Zone PDFs

**Status: PASS — 8/8 present and verified**

All 8 zone quickstart card PDFs are staged at:
`projects/seedwarden/assets/zone-cards/`

| File | Size | Status |
|------|------|--------|
| seedwarden-zone-3-quickstart-card.pdf | 648 KB | PRESENT |
| seedwarden-zone-4-quickstart-card.pdf | 649 KB | PRESENT |
| seedwarden-zone-5-quickstart-card.pdf | 648 KB | PRESENT |
| seedwarden-zone-6-quickstart-card.pdf | 648 KB | PRESENT |
| seedwarden-zone-7-quickstart-card.pdf | 649 KB | PRESENT |
| seedwarden-zone-8-quickstart-card.pdf | 648 KB | PRESENT |
| seedwarden-zone-9-quickstart-card.pdf | 648 KB | PRESENT |
| seedwarden-zone-10-quickstart-card.pdf | 648 KB | PRESENT |

Naming convention correct. File sizes consistent (630-650 KB range). Formatting
verified: US Letter landscape, zone color bands, three-column layout, Heirloom
Variety Spotlight band, Seedwarden wordmark.

Known cosmetic defects (non-blocking, do not re-export):
- Zone 6 Storage: "ferment hot sauce" text-wrap artifact
- Zone 9 Storage: "ripen" clips at column edge

Footer URLs are placeholder values (`seedwarden.co/zone-calendar`,
`seedwarden.co/zone`). These can be updated after Kit account is created
by editing lines 594-600 of `projects/seedwarden/scripts/generate_zone_cards.py`
and re-running. This is optional — existing PDFs are distributable as-is via
the Gist URL.

Note: A Gist distribution URL is already live and inserted into the launch
runbook: `https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d`

---

### Influencer Contact List

**Status: PASS — 15 verified contacts staged**

Contact file: `projects/seedwarden/HERBALIST_OUTREACH_CONTACT_LIST.md`

All 15 contacts have name/handle, platform, estimated audience, and contact method.
Contact methods confirmed: 4 named individuals with verified public email addresses
(Sabrena Gwin/AHG, Susan Leopold/UpS, John Gallagher/LearningHerbs, Juliet
Blankespoor/Chestnut School), plus Reddit modmail, Discord DM, Instagram DM, and
Facebook message routes for remaining contacts.

Tiered outreach sequencing:
- Tier 1 (pre-launch): Sabrena Gwin, Susan Leopold, John Gallagher, Reddit mods
- Tier 2 (pre-launch): Juliet Blankespoor, Herbal Academy, Discord admins, Seattle Herbalism Society
- Tier 3 (launch day): AHG chapter routing, live engagement

Note: A secondary contact file exists at
`projects/seedwarden/TRACK_B_HERBALIST_OUTREACH_MATRIX.md` with 18 contacts
(3 additional vs. the 15-contact minimum) and includes 3 ready-to-send outreach
message templates (Reddit/Discord DM, Instagram DM, email) with all
personalization brackets clearly marked.

---

### Email Templates

**Status: PASS — 5-email welcome sequence complete**

File: `projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md`

5-email Kit automation sequence:
- Email 1 (Day 0, immediate): Welcome + zone card delivery
- Email 2 (Day 2): Heirloom seed philosophy
- Email 3 (Day 5): Seed-saving origin story
- Email 4 (Day 7): Guide catalog introduction
- Email 5 (Day 10): First offer with SEEDWARDEN15 coupon code

All subjects are 49-59 characters (deliverability safe). Bodies are 1,190-1,520
characters (no truncation risk). All personalization fields are clearly marked
(`{SUBSCRIBER_FIRST_NAME}`, `[Your Name]`).

Remaining fill-in fields before Kit build:
- `[Your Etsy Shop URL]` in Email 3
- Guide title placeholders and Etsy link in Emails 4-5
- Discounted prices in Email 5

SEEDWARDEN15 coupon code must be active in Etsy Shop Manager before activating
sequence (Email 5 CTA depends on it).

---

### Social Media Templates

**Status: PASS — 18 posts pre-written**

File: `projects/seedwarden/TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`

Coverage: 11 launch-window posts + 7 June 1-7 ramp-up posts.

All captions include hashtags. Platform-specific posting times documented.
Hashtag reference table by audience type is included (core, zone-specific,
herbalist, homesteading).

One placeholder remains in all social posts: `[LANDING_PAGE_URL]`. This must
be replaced with the Kit landing page URL or Gist URL before posting.

Reddit posts cannot be pre-scheduled and must be posted manually.

---

### Launch-Day Runbook

**Status: PASS — hour-by-hour guide complete**

File: `projects/seedwarden/MAY_30_LAUNCH_DAY_RUNBOOK.md`

The runbook covers 07:30-21:00 UTC and includes:
- 4-block pre-launch verification (platform logins, PDF access check, test sends, GO/HOLD gate)
- Launch window execution order (Reddit 08:00, email 08:05, DMs 08:15, Instagram 08:30, TikTok 08:45, Pinterest 09:00)
- Hourly pulse check schedule with concern thresholds
- Day 0 snapshot template
- Quick-reference card on last page

Note: All times in the runbook reference May 30 dates. For June 1-2 execution,
read "May 30" as your chosen launch date. All other content is date-agnostic.

Companion files (referenced in runbook, all confirmed present):
- `TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md`
- `TRACK_B_LAUNCH_DAY_ROLLBACK_PROCEDURES.md`
- `TRACK_B_LAUNCH_DAY_SUCCESS_SIGNAL_CHECKPOINTS.md`
- `TRACK_B_MONITORING_CHECKPOINTS.md` (Day 3/7/14 checkpoint framework)

---

## Section 1: User Action Gates

These are the only things blocking launch. Nothing else is missing.

### Gate 1: Create Social Media Accounts
**Required before**: any social posting

- [ ] Create Instagram Business account with handle `@seedwarden`
  (alternatives if taken: `@seedwarden.co`, `@seedwarden.seeds`)
- [ ] Create TikTok account with handle `@seedwarden`
- [ ] Create Pinterest Business account with handle `seedwarden`
- [ ] Upload profile image to all three: `projects/seedwarden/logos/seedwarden_logo_1.png`
- [ ] Write and publish bio text on all three accounts
- [ ] Add link-in-bio to all three (use Gist URL initially; update to Kit URL once built)

**Time required**: 30-60 minutes  
**Blocks**: social post publishing, Kit bio links, Buffer/Later scheduling

---

### Gate 2: Set Up Canva Brand Kit
**Required before**: creating new visual content (optional if reusing existing zone card PDFs)

- [ ] Log in to Canva at canva.com (wanka95@gmail.com)
- [ ] Navigate to Brand Hub > Create a Brand Kit
- [ ] Add 6 brand colors by hex code:
  - Deep Forest Green: #143b28
  - Deep Ink Green: #1A3A2A
  - Warm Cream: #F5EDD6
  - Parchment: #EDE0C4
  - Sage: #8FA882
  - Burnt Sienna: #A0522D
- [ ] Add 3 fonts: Playfair Display (heading), Lato (body), Cormorant Garamond (accent)
- [ ] Upload `projects/seedwarden/logos/seedwarden_logo_1.png` as Brand Kit logo

**Time required**: 30 minutes  
**Blocks**: new visual content production  
**Note**: This gate does not block the zone card PDF distribution or influencer outreach.
It only blocks new Instagram/TikTok/Pinterest creative production.

---

### Gate 3: Create Kit Account and Build Landing Page
**Required before**: email automation goes live

- [ ] Create Kit account at kit.com (use wanka95@gmail.com)
- [ ] Follow `projects/seedwarden/MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md` for full setup
- [ ] Build landing page using copy from `projects/seedwarden/KIT_SETUP_NOTES.md` Step 3:
  - Headline: "Your Free Zone Quick-Start Card"
  - Form fields: First name, Email, Growing zone dropdown (Zones 3-10)
  - CTA: "Send My Zone Card"
- [ ] Set up 15 zone-routing tags (Zones 3-10 + combinations)
- [ ] Build 5-email welcome sequence using copy from `projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md`
- [ ] Send test email to wanka95@gmail.com — verify zone card download link resolves, no placeholder text visible
- [ ] Publish automation (status must read "Published" not "Draft")
- [ ] Copy Kit landing page URL
- [ ] Update all three social media bios with Kit landing page URL

**Time required**: 2-3 hours  
**Blocks**: email list building, zone card delivery automation

---

### Gate 4: Upload Zone PDFs to Google Drive
**Required before**: Kit email delivery links are live

- [ ] Upload all 8 zone card PDFs from `projects/seedwarden/assets/zone-cards/` to Google Drive
- [ ] Set sharing to "Anyone with the link can view"
- [ ] Test all 8 download links in an incognito browser window
- [ ] Note: Gist URL (`https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d`) is already live as backup distribution — Google Drive provides a redundant delivery path

**Time required**: 20 minutes

---

### Gate 5: Confirm SEEDWARDEN15 Coupon Code
**Required before**: Email 5 (Day 10) of the welcome sequence is activated

- [ ] Log in to Etsy Shop Manager
- [ ] Navigate to Marketing > Coupons and Sales
- [ ] Confirm SEEDWARDEN15 coupon code is active and set to correct discount

**Time required**: 5 minutes  
**Note**: This gate only blocks Email 5. Emails 1-4 of the automation can fire
before this is complete.

---

## Section 2: Autonomous Orchestrator Work

Once the gates above are cleared, the following work can proceed automatically
without user involvement. Items are listed in dependency order.

**After Gate 1 (social accounts created)**:
- Replace `[LANDING_PAGE_URL]` placeholder in all 18 social media post drafts in `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` with confirmed Gist URL or Kit URL
- Replace placeholder in influencer DM templates in `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`
- Draft scheduling queue for Buffer/Later for all non-Reddit posts
- Prepare Day 3/7/14 monitoring spreadsheet from template in `TRACK_B_MONITORING_CHECKPOINTS.md`

**After Gate 3 (Kit account live)**:
- Verify Kit automation status is Published
- Confirm zone-routing tag logic is correctly configured
- Stage Day 3 checkpoint tracking sheet

**On launch day (user posts manually)**:
- Reddit r/herbalism post (08:00 UTC, manual — cannot be pre-scheduled)
- Emails to pre-approved influencer contacts (08:05 UTC)
- DMs to all 15 non-responded contacts (08:15 UTC, parallel with social)
- Instagram launch post (08:30 UTC — can be pre-scheduled in Buffer/Later)
- TikTok launch video (08:45 UTC — must be uploaded natively, not cross-posted)
- Pinterest launch pin (09:00 UTC — can be pre-scheduled)

**Ongoing after launch**:
- Hourly pulse checks at 09:30, 11:00, 12:00, 13:00, 14:30 UTC (per runbook)
- Day 3 checkpoint (June 4 if launching June 1): review against thresholds in `TRACK_B_MONITORING_CHECKPOINTS.md`
- Day 7 checkpoint (June 8): partnership candidate identification
- Day 14 checkpoint (June 15): Phase 3 launch GO/GO-with-adjustments/DEFER decision

---

## Section 3: June 1-2 Launch Timeline

This timeline covers the two-day window for completing gates and executing launch.
Choose either June 1 or June 2 as your launch date; the sequence is the same.

### Pre-Launch Day (Day Before Launch — 2.5 to 4 hours total)

**Hour 0-1: Accounts and Brand Kit (Gates 1 and 2)**
- Create Instagram, TikTok, Pinterest accounts (30-60 min)
- Set up Canva Brand Kit (30 min)
- Upload PDFs to Google Drive, test all 8 links (20 min)

**Hour 1-4: Kit Setup (Gate 3)**
- Create Kit account and build landing page (30 min)
- Build 5-email welcome sequence (45-60 min)
- Configure zone-routing automation (30 min)
- Test send and publish (15 min)
- Update social bios with Kit URL (10 min)
- Confirm SEEDWARDEN15 coupon code (5 min)

**End of pre-launch day**:
- All 5 gates cleared
- Social bios live with Kit URL
- Kit automation published
- Influencer DM templates ready (Gist URL confirmed present)
- Social post drafts have real URL substituted for `[LANDING_PAGE_URL]`

---

### Launch Day (07:30-21:00 UTC)

Follow `projects/seedwarden/MAY_30_LAUNCH_DAY_RUNBOOK.md` exactly.
Substitute your launch date wherever the runbook reads "May 30."

| UTC Time | Action | Who |
|----------|--------|-----|
| 07:30 | Verify 7 platform logins | User |
| 07:38 | Verify all 8 PDFs accessible at Gist URL, Kit Published, bios correct | User |
| 07:48 | Test email send to self; scan drafts for placeholder text | User |
| 07:53 | GO/HOLD decision — all 3 criteria must be YES | User |
| 08:00 | Post Reddit r/herbalism launch post (manual) | User |
| 08:05 | Email pre-approved influencer contacts | User |
| 08:15 | DMs to all 15 non-responded contacts | User |
| 08:30 | Instagram launch post | User (or Buffer/Later) |
| 08:45 | TikTok launch video (upload natively) | User |
| 09:00 | Pinterest launch pin | User (or scheduled) |
| 09:30-14:30 | Hourly pulse checks (5 min each), reply to Reddit comments | User |
| 16:00 | Mid-day extended check + optional TikTok boost post | User |
| 18:00 | Day 1 wrap-up: log Day 0 snapshot, queue Day 2 content | User |
| 20:00 | Final monitoring check, close out launch day | User |

**Total operator time**: 3.5-4.0 hours across the full day.

---

### Post-Launch Monitoring Schedule

| Date (if June 1 launch) | Date (if June 2 launch) | Checkpoint | Key Decision |
|------------------------|------------------------|------------|--------------|
| June 4 | June 5 | Day 3 | Go/Marginal/Fail initial read |
| June 8 | June 9 | Day 7 | Tier 2 partnership candidates identified |
| June 15 | June 16 | Day 14 | Phase 3 GO/GO-with-adjustments/DEFER decision |

Checkpoint thresholds are defined in `projects/seedwarden/TRACK_B_MONITORING_CHECKPOINTS.md`.

---

## Section 4: Success Metrics (by June 4-5, Day 3)

These are the target ranges from `TRACK_B_MONITORING_CHECKPOINTS.md`.

| Metric | Minimum (Marginal) | Target (On Track) | Strong Signal |
|--------|--------------------|-------------------|---------------|
| Combined reach (all channels) | 500 | 1,000-2,000 | 2,000+ |
| Reddit r/herbalism upvotes | 10 | 30-80 | 80+ |
| Reddit comments | 5 | 50 | 100+ |
| Instagram/TikTok engagement | 50 likes + 10 comments | 100+ likes | 200+ |
| Email open rate (Kit) | 15% | 20-30% | 30%+ |
| New Kit subscribers | 5 | 25-50 | 50+ |
| Influencer responses | 1 | 3-5 | 5+ who commit to sharing |

**By June 8-9 (Day 7)**:
- Cumulative reach: 2,000-5,000 across all channels
- 3+ Tier 2 partnership candidates identified (strong confidence level)
- Email click-through rate: 5-10%

**By June 15-16 (Day 14)**:
- Cumulative reach: 5,000-15,000
- Email list: 50-150 subscribers
- Phase 3 launch decision: GO for June 22 / GO with adjustments for June 29 / DEFER

---

## Section 5: Track A Independence Confirmation

Track B does not depend on Track A (Etsy tag corrections) in any way.

The `concurrent-track-execution-plan.md` and `TRACK_A_CONTINGENCY_LAUNCH_PLAN.md`
both document that Track B was specifically designed as a Phase 1-independent
workstream. The zone card distribution is delivered via Gist URL and Kit email
automation — neither requires the Etsy shop to be in any particular state.

The only connection between Track A and Track B is a downstream revenue path:
once Track A Etsy listings are live and verified, Email 5 of the Kit welcome
sequence links to them with coupon code SEEDWARDEN15. This is already accounted
for in Gate 5 above.

Track B can launch, run, and reach all Day 3/7/14 checkpoints with Track A in
any state. The two tracks share no infrastructure and no execution dependencies.

---

## Section 6: Key File Index

| Purpose | File |
|---------|------|
| Zone PDFs (8 files) | `projects/seedwarden/assets/zone-cards/` |
| Influencer contact list (15 contacts) | `projects/seedwarden/HERBALIST_OUTREACH_CONTACT_LIST.md` |
| Influencer outreach matrix (18 contacts + templates) | `projects/seedwarden/TRACK_B_HERBALIST_OUTREACH_MATRIX.md` |
| Email welcome sequence (5 emails, copy-paste ready) | `projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md` |
| Social media calendar (18 posts) | `projects/seedwarden/TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` |
| Launch-day runbook (hour-by-hour) | `projects/seedwarden/MAY_30_LAUNCH_DAY_RUNBOOK.md` |
| Kit account setup guide | `projects/seedwarden/MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md` |
| Day 3/7/14 monitoring checkpoints | `projects/seedwarden/TRACK_B_MONITORING_CHECKPOINTS.md` |
| Contingency decision trees | `projects/seedwarden/TRACK_B_LAUNCH_DAY_COMMON_ISSUES_DECISION_TREES.md` |
| Rollback procedures | `projects/seedwarden/TRACK_B_LAUNCH_DAY_ROLLBACK_PROCEDURES.md` |
| Logo for profile images | `projects/seedwarden/logos/seedwarden_logo_1.png` |
| Zone card generator (for footer URL update) | `projects/seedwarden/scripts/generate_zone_cards.py` |

---

*Created: June 1, 2026. Verification performed this session.*
*Launch date options: June 1 (today) or June 2 (tomorrow), pending gate completion.*
*All infrastructure verified production-ready. Only user action gates block launch.*
