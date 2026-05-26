---
title: "May 30 Launch Readiness Checklist — Track B Verification"
date: 2026-05-26
status: production-ready
scope: Gates 1-2 completion verification + May 30 execution sequence
---

# May 30 Launch Readiness Checklist
## Track B Zone Cards — Pre-Launch Verification (May 26, 2026)

**Launch target**: May 30, 2026 08:00 UTC  
**Gates 1-2 deadline**: May 26, 2026 23:59 UTC  
**Verified by**: Orchestrator session — May 26, 2026

---

## 1. Zone PDFs Verification

**Status**: PASS

- 8/8 PDFs present in `projects/seedwarden/assets/zone-cards/` — Zones 3, 4, 5, 6, 7, 8, 9, 10.
- File sizes: 633–634 KB each. Well within the 1.5 MB per-file and 10 MB per-file limits.
- Naming convention correct: `seedwarden-zone-[N]-quickstart-card.pdf` for all 8 files.
- Spot-check result (Zones 3, 6, 9): frost dates, crops, storage tips, heirloom variety spotlight — all correct per ZONE_QUICKSTART_CARD_SPEC.md.
- Formatting verified: US Letter landscape, cream background, zone color bands, three-column layout, Heirloom Variety Spotlight band, Seedwarden wordmark present.
- Known defects: 2 cosmetic text-wrap artifacts (Zone 6 Storage: "ferment hot sauce" wraps; Zone 9 Storage: "ripen" clips). Non-blocking — do not re-export.
- One pre-launch action: footer URL substitution (see Section 7).

---

## 2. Influencer List Verification

**Status**: PASS — 18 contacts staged (15-contact minimum exceeded)

- Contact file: `projects/seedwarden/TRACK_B_HERBALIST_OUTREACH_MATRIX.md`
- 18 pre-selected community leaders across 3 tiers. Reach: 1K–1.8M per contact; Tier 1 aggregate reach exceeds 3M (Reddit channels).
- All 18 contacts have: name/handle, platform, estimated audience, engagement angle, custom hook.
- Contact method confirmed for all 18: 6 named contacts have verified public emails (Sabrena Gwin, Susan Leopold, John Gallagher, Juliet Blankespoor, Herbal Academy partnerships, Chestnut School); 12 contacts use Reddit modmail, Discord DM, Instagram DM, or Facebook message — all platform routes accessible.
- No duplicates. No missing contact methods.
- One open action: Gist URL or Kit landing page URL must be confirmed before May 28 Tier 1 outreach goes out, so it can be inserted into template links.

---

## 3. Email Templates Verification

**Status**: PASS — 5-email welcome sequence complete

- File: `projects/seedwarden/execution/TRACK_B_EMAIL_COPY_FINAL.md`
- 5 distinct emails with separate angles: welcome + download delivery (Day 0), heirloom seed philosophy (Day 2), seed-saving story (Day 5), catalog introduction (Day 7), first offer with discount (Day 10).
- Each email has: subject line, send timing, body copy, Kit build notes, character count.
- Subject lines: 49–59 characters — within safe deliverability range for all major email clients.
- Body copy: 1,190–1,520 characters per email — no truncation risk.
- Copy-paste ready for Kit. Personalization fields clearly marked: `{SUBSCRIBER_FIRST_NAME}`, `[Your Name]`.
- Remaining fill-in fields before Kit build: `[Your Etsy Shop URL]` (Email 3), guide title placeholders and Etsy link (Emails 4-5), and discounted prices (Email 5).
- Action required: confirm coupon code SEEDWARDEN15 is active in Etsy Shop Manager before activating sequence (Email 5 CTA depends on it).
- Outreach email templates (for influencer outreach) are in `TRACK_B_HERBALIST_OUTREACH_MATRIX.md` — 3 templates for Reddit/Discord DM, Instagram DM, and email. All copy-paste ready with clearly marked personalization brackets.

---

## 4. Social Media Calendar Verification

**Status**: PASS

- File: `projects/seedwarden/TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`
- Coverage: May 28–June 7 (11 launch-window posts + 7 June 1-7 ramp-up posts = 18 posts total).
- May 28: 4 pre-written posts (Instagram zone awareness, TikTok zone card flip teaser, Reddit r/herbalism question post, Pinterest seasonal planning pin).
- May 29: 3 pre-written posts (Instagram "Tomorrow" carousel, TikTok walkthrough, Pinterest zone-specific deep-dive).
- May 30 launch day (08:00-09:00 UTC): 4 pre-written posts (Instagram launch carousel, TikTok launch video, Pinterest launch collection pin, Reddit r/herbalism link post).
- June 1-7: 7 posts with captions, hashtags, and visual specs pre-written.
- All captions include hashtags. Platform-specific posting times documented with rationale.
- Hashtag reference table included by audience type (core, zone-specific, herbalist, homesteading).
- One placeholder requiring substitution in all social posts: `[LANDING_PAGE_URL]` — replace with Kit landing page URL or Gist collection URL once confirmed.
- Reddit posts cannot be pre-scheduled — must be posted manually at listed UTC times.

---

## 5. Day 3/7/14 Monitoring Framework Verification

**Status**: PASS

- File: `projects/seedwarden/TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md`
- Day 3 checkpoint: June 2, 2026 (Monday). Metrics: combined reach target 500–2,000; Reddit baseline 300–800 upvotes + 50 comments; Instagram/TikTok minimum 50 likes + 10 comments; email open rate 20%+. Go/Marginal/Fail decision framework defined with clear criteria.
- Day 7 checkpoint: June 6, 2026 (Friday). Metrics: cumulative reach target 2,000–5,000; engagement rate by channel (2–8% per platform); Tier 2 partnership candidates identified (3+ for strong confidence). Three-scenario decision: Strong confidence / Moderate confidence / Weak confidence.
- Day 14 checkpoint: June 13, 2026 (Friday). Metrics: cumulative reach target 5,000–15,000. Final Phase 3 launch decision: GO (June 22) / GO with adjustments (June 29) / DEFER. All threshold numbers are explicit and numerical.
- Measurement tools documented: UTM link structure for all channels, tracking spreadsheet template with 3 tabs.
- Decision thresholds are clear and numerical throughout. No ambiguous language at any checkpoint.

---

## 6. Kit Landing Page Verification

**Status**: PARTIAL — copy and specs are production-ready; account not yet built

- Landing page copy and configuration documented in: `projects/seedwarden/KIT_SETUP_NOTES.md` Step 3.
- Headline: "Your Free Zone Quick-Start Card"
- Subheadline: "Know exactly what to plant, when to plant it, and what to do right now in your zone — one-page reference card, free."
- Form fields: First name (required), Email address (required), Growing zone dropdown Zones 3–10 (required).
- CTA button: "Send My Zone Card"
- Trust text below button: "No spam. Unsubscribe anytime. Seedwarden sends one email per week about growing, foraging, and real food."
- Zone routing automation logic documented. All 15 Kit tags documented. Email sequence build order documented.
- Gate 3 pre-flight validation (May 26) confirmed: all Kit infrastructure documents are production-ready and copy-paste ready.
- BLOCKER: Kit account not yet created (user action required). Social accounts (Instagram, TikTok, Pinterest) creation is also pending (Gate 1). Canva Brand Kit setup pending (Gate 2). These are the only remaining blockers.
- Deployment script with step-by-step execution guide: `projects/seedwarden/MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md`

---

## 7. Footer URL Substitution Task

**Status**: DOCUMENTED — 5-minute task, user action required before May 29

- Full documentation: `projects/seedwarden/ZONE_PDF_VERIFICATION_REPORT.md` (Footer URL Substitution section)
- Current placeholder URLs embedded in all 8 PDFs (footer band):
  - Left: `Get the full Zone {zone} Calendar — seedwarden.co/zone-calendar`
  - Right: `Free guides: seedwarden.co/zone  |  Unsubscribe anytime`
- Generator lines to edit: `projects/seedwarden/scripts/generate_zone_cards.py`, lines 594–600

**Exact substitution required:**

| Current text | Replace with |
|---|---|
| `seedwarden.co/zone-calendar` | Kit landing page URL (once account is built) |
| `seedwarden.co/zone` | Kit landing page URL or Gist collection URL |

**Execution steps (5 minutes):**
1. Open `projects/seedwarden/scripts/generate_zone_cards.py`
2. Edit lines 594–600: replace both placeholder domains with live URLs
3. Save the file
4. Run: `cd projects/seedwarden/scripts && uv run python generate_zone_cards.py`
5. New PDFs overwrite existing files in `assets/zone-cards/` — no renaming needed
6. Upload updated PDFs to Google Drive (sharing links remain the same if overwriting in place)

- Decision: If Kit landing page URL is not confirmed by May 28, the existing PDFs with placeholder URLs are acceptable for initial Gist distribution. The placeholder text is readable and the domain does not return an error. Update in next export batch once Kit URL is live.

---

## 8. May 30 Launch Execution Checklist

Complete these steps in order on launch day. Times are UTC.

**May 27 (user, 2-3 hours):**
1. Complete Gate 1: create Instagram, TikTok, Pinterest accounts with @seedwarden handle. Add Seedwarden logo from `projects/seedwarden/logos/seedwarden_logo_1.png`.
2. Complete Gate 2: set up Canva Brand Kit — 6 colors, 3 fonts, logo per CANVA_SETUP_STATUS.md.
3. Create Kit account at kit.co (email: wanka95@gmail.com). Follow `projects/seedwarden/MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md`.
4. Upload 8 zone card PDFs to Google Drive. Set sharing to "Anyone with the link." Test all 8 download links.
5. Build Kit landing page using copy from KIT_SETUP_NOTES.md Step 3. Publish and copy URL.
6. Add Kit landing page URL to Instagram, TikTok, and Pinterest bios.

**May 28 (user, 45-60 minutes):**
7. Execute footer URL substitution (5 min) — replace placeholder URLs with Kit landing page URL and re-run generator. Upload updated PDFs to Google Drive.
8. Replace `[LANDING_PAGE_URL]` in social calendar posts with confirmed Kit URL.
9. Insert confirmed Gist or Kit URL into outreach message templates before sending.
10. Begin Tier 1 outreach (Reddit mods, Discord admin, Juliet Blankespoor, John Gallagher, Mason Hutchinson) per `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`.
11. Schedule or draft May 28 social posts: Instagram 18:00 UTC, TikTok 17:00 UTC, Reddit 12:00 UTC, Pinterest 21:00 UTC.

**May 29 (user, 30-60 minutes):**
12. Verify SEEDWARDEN15 coupon code is active in Etsy Shop Manager (Marketing > Coupons and Sales).
13. Complete Tier 2 and Tier 3 outreach (contacts 8–18).
14. Schedule May 29 social posts: Instagram 18:00 UTC, TikTok 16:00 UTC, Pinterest 21:00 UTC.
15. Schedule May 30 launch posts: Instagram 08:30 UTC, TikTok 08:45 UTC, Pinterest 09:00 UTC.
16. Send Kit test email to yourself — verify merge fields, PDF download links, Etsy links, formatting.
17. Final pass: confirm all 8 zone PDFs are live on Google Drive and download correctly.

**May 30 launch window (user, 20-30 minutes):**
18. 08:00 UTC: Post Reddit r/herbalism launch post manually.
19. 08:15-08:30 UTC: Verify scheduled Instagram, TikTok, Pinterest posts went live.
20. 08:30-09:00 UTC: Monitor comments, react and reply to early engagement.
21. Check that Zone Card PDF download links are working (test one live link).
22. Set calendar reminders: Day 3 check June 2, Day 7 check June 6, Day 14 check June 13.

---

## Summary: Gate Status as of May 26, 2026

| Item | Status | Blocking Launch? |
|------|--------|-----------------|
| 8 Zone PDFs | PASS — 8/8 present, verified, production-ready | No |
| 18 influencer contacts | PASS — all staged, contact methods confirmed | No |
| 5 email templates | PASS — copy-paste ready for Kit build | No |
| Social calendar (11+ posts) | PASS — all copy pre-written | No |
| Monitoring framework (Day 3/7/14) | PASS — numerical thresholds defined | No |
| Kit landing page copy | PASS — all spec fields resolved | No |
| Footer URL substitution | DOCUMENTED — 5-min task, requires live Kit URL | No (non-blocking for Gist launch) |
| Gate 1: Social accounts | PENDING — user action required May 27 | YES — blocks Kit URL in social bios |
| Gate 2: Canva Brand Kit | PENDING — user action required May 27 | YES — blocks visual content |
| Gate 3: Kit account + automation | PENDING — user action required May 27-28 | YES — blocks email delivery |
| Google Drive PDF upload | PENDING — user action required May 27 | YES — blocks Kit email delivery |

**Launch verdict**: Infrastructure is production-ready. May 30 launch is achievable if Gates 1-2 are completed by tonight (May 26 23:59 UTC) and Gate 3 is executed May 27.

---

*Created: May 26, 2026. Verification session for Track B pre-launch assets.*
*Key files: `assets/zone-cards/` (8 PDFs), `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`, `execution/TRACK_B_EMAIL_COPY_FINAL.md`, `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`, `TRACK_B_MONITORING_CHECKPOINTS.md`, `ZONE_PDF_VERIFICATION_REPORT.md`, `MAY_27_GATE_3_DEPLOYMENT_SCRIPT.md`.*
