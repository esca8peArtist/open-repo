---
title: "Track B Launch Day Checklist — Zone Cards May 30"
date: 2026-05-26
version: 1.0
status: ready-for-execution
purpose: >
  Step-by-step pre-launch and launch-day execution checklist for Track B Zone Cards.
  May 30, 2026. Zero ambiguity. Contingency plans included.
---

# Track B Launch Day Checklist
## Zone Cards — May 30, 2026

**Launch day**: Friday May 30, 2026
**Announcement window**: May 30 afternoon/evening (aim for 12:00 PM–8:00 PM local time)
**Solo operator time budget**: 2–3 hours total on May 30 (prep + post + monitor)

---

## Pre-Launch Checklist (Complete by May 29 evening OR May 30 morning)

Work through this list in order. Each item must be checked before moving to the next section.

### Step 1 — Verify All 8 PDFs Are Accessible

- [ ] Open `projects/seedwarden/assets/zone-cards/` and confirm all 8 PDF files are present
- [ ] Spot-check: open Zone 3, Zone 6, and Zone 9 PDFs directly to confirm they render without errors
- [ ] File sizes all in 630–640 KB range (any file under 100 KB or over 2 MB indicates a corrupt file — regenerate from `scripts/generate_zone_cards.py` if needed)

**Expected files**:
```
seedwarden-zone-3-quickstart-card.pdf
seedwarden-zone-4-quickstart-card.pdf
seedwarden-zone-5-quickstart-card.pdf
seedwarden-zone-6-quickstart-card.pdf
seedwarden-zone-7-quickstart-card.pdf
seedwarden-zone-8-quickstart-card.pdf
seedwarden-zone-9-quickstart-card.pdf
seedwarden-zone-10-quickstart-card.pdf
```

---

### Step 2 — Update Footer URLs (If Not Already Done)

The PDFs currently contain placeholder footer URLs (`seedwarden.co/zone-calendar` and `seedwarden.co/zone`). Before launch, decide whether to:

**Option A — Replace with live URLs**: Edit the `ZONES` dict `footer` section in `projects/seedwarden/scripts/generate_zone_cards.py`, set the actual landing page and calendar URLs, and re-run the script to regenerate all 8 PDFs. Re-verify the regenerated files open correctly.

**Option B — Launch with placeholder URLs**: Acceptable for a Gist-based free distribution where the primary call-to-action is the Gist link itself. The placeholder URLs are readable and not broken links — they simply redirect to a page that does not exist yet. If the landing page (`seedwarden.co/zone`) is not live by May 30, keep placeholders and update PDFs in the Week 1 refresh after launch.

- [ ] Decision made: Option A (updated URLs) or Option B (placeholders acceptable)
- [ ] If Option A: Script re-run complete, 8 new PDFs verified

---

### Step 3 — Set Up Gist Distribution

- [ ] Log in to github.com with the Seedwarden account
- [ ] Create a new Gist (gist.github.com > + New Gist)
- [ ] Gist title: "Seedwarden Zone Quick-Start Cards — Free Download (Zones 3–10)"
- [ ] Gist description: "One-page quick-start guides for every USDA growing zone. Free PDF download. Each card includes frost dates, crop timing, storage tips, and heirloom variety spotlight for your zone."
- [ ] Upload all 8 PDFs to the Gist OR create a Gist with a README-style text file that contains direct GitHub raw file URLs for each PDF (direct links are more reliable for download tracking)
- [ ] Set Gist to Public
- [ ] Copy and save the Gist URL: _______________________________
- [ ] Test the Gist link: open it in a private/incognito browser window to confirm it is publicly accessible without being logged in

**Gist contingency**: If Gist upload fails or PDFs do not render correctly in Gist:
- Alternative 1: Upload to Google Drive (set to "Anyone with the link can view"), create a shared folder link, share that link in your announcement posts
- Alternative 2: Upload to Dropbox public folder
- Alternative 3: Use GitHub repository direct raw URLs: `https://raw.githubusercontent.com/[username]/[repo]/master/projects/seedwarden/assets/zone-cards/[filename].pdf`

- [ ] Backup URL saved (in case Gist is unavailable on launch day): _______________________________

---

### Step 4 — Test on Mobile

- [ ] Open the Gist URL on a mobile phone (both iOS Safari and Android Chrome if possible)
- [ ] Tap the Zone 3 PDF link and confirm it opens in the browser or downloads correctly
- [ ] Confirm the PDF is readable at mobile zoom level (the cards are landscape format — users may need to rotate or zoom; this is expected and acceptable)
- [ ] If PDF does not open on mobile: save the mobile-friendly alternative link (Google Drive or Dropbox viewer link works better on mobile than raw GitHub PDFs)

---

### Step 5 — Prepare Social Media Posts

- [ ] Draft all 5 launch-day posts using templates from `TRACK_B_SOCIAL_MEDIA_CALENDAR.md`
- [ ] Replace "[Gist link or seedwarden.co/zone]" placeholder in each template with the actual Gist URL saved in Step 3
- [ ] Save all post drafts (Notes app, Google Doc, or scheduling tool)
- [ ] Update Instagram bio/link-in-bio with Gist URL
- [ ] If scheduling: queue LinkedIn post for 8:00 AM May 30, Instagram for 12:00 PM, TikTok for 7:00 PM
- [ ] If posting manually: set a reminder alarm for each posting time

---

### Step 6 — Confirm Herbalist Outreach Sent

- [ ] All Tier 1 contacts (7) contacted by May 28 (per `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`)
- [ ] All Tier 2 contacts (7) contacted by May 29
- [ ] Response tracking table in `TRACK_B_HERBALIST_OUTREACH_MATRIX.md` updated with any replies received
- [ ] Any contact who asked for the Gist link before launch: send them the link now (before public announcement is fine — give them a preview)

---

### Step 7 — Final Readiness Check (5 minutes, May 30 morning)

Complete this the morning of May 30 before you begin posting.

- [ ] Gist is still accessible (test the URL again in incognito)
- [ ] All 8 PDFs confirmed downloadable from the Gist
- [ ] Social posts are drafted and ready
- [ ] Backup URL is saved and tested
- [ ] Instagram bio updated with Gist link
- [ ] Phone charged, notifications on for DM responses

**If all 7 boxes checked**: You are cleared to launch. Proceed to the Launch Day Timeline below.

---

## Launch Day Timeline (May 30)

| Time | Action | Platform | Notes |
|------|--------|----------|-------|
| 8:00 AM | Post LinkedIn launch announcement | LinkedIn | Use Template 3 from outreach matrix, add Gist URL |
| 10:00 AM | Post Reddit launch thread | Reddit r/vegetablegardening (and r/herbalism if mod-approved) | Use Reddit template from social calendar |
| 12:00 PM | Post Instagram launch post | Instagram | Fan/grid image of all 8 cards; full caption from social calendar |
| 12:00 PM | Post Instagram Story sequence | Instagram Stories | 3-story sequence: "They're live" + zone finder + "share with a Zone X friend" |
| 12:30 PM | Email herbalist contacts who responded | Email | Short note: "Cards are live — here's the link: [Gist URL]" |
| 2:00 PM | Check Reddit post — respond to any comments | Reddit | Respond within 2 hours of posting for algorithm benefit |
| 4:00 PM | Post Pinterest launch pin | Pinterest | Full product grid image with direct Gist link |
| 7:00 PM | Post TikTok launch video | TikTok | Walkthrough video script from social calendar |
| 8:00 PM | Check all platforms — reply to comments and DMs | All | 20 minutes of engagement to close the launch window |
| Before bed | Record Day 1 metrics | Monitoring doc | Gist views, Reddit upvotes, IG reach — take a screenshot |

---

## Contingency Plan: If Gist Is Unavailable

If github.com is down or the Gist is inaccessible on launch day:

1. Immediately switch to the backup URL saved in Step 3 (Google Drive or Dropbox folder link)
2. Update the Instagram bio link-in-bio to the backup URL
3. Edit the Reddit post (if already submitted) to replace the Gist link with the backup URL
4. Add an Instagram Story: "Link updated — new link in bio" with link sticker
5. Do not delay the launch — proceed with backup URL. The content is what matters.

---

## Contingency Plan: If No Reddit Mod Approval

If Reddit moderators have not approved your post by launch day morning:

1. Post in r/vegetablegardening as a regular member post (not a promotional post) with personal framing: "I built a free zone guide — here's what Zone [X] looks like" and share one card as an image upload, not a link
2. Image posts perform better than link posts on Reddit anyway — this may be the better launch format regardless
3. Separately: post in r/selfhosted, r/homesteading, or r/gardening as alternative communities if the primary subreddits are blocked

---

## Post-Launch (May 31+)

- [ ] Record Day 1 stats (Gist views, Reddit upvotes, Instagram reach) in the monitoring checkpoint log (`TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md`)
- [ ] Respond to all DMs and comments within 24 hours
- [ ] Follow up with any herbalist contact who expressed sharing interest but did not post yet (one short follow-up only)
- [ ] Day 3 checkpoint: June 2 — review metrics against targets in monitoring doc
