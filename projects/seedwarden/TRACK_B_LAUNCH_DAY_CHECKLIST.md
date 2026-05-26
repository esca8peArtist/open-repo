---
title: "Track B Launch Day Checklist — Production Execution Guide"
date: 2026-05-30
version: 2.0
status: production-ready
purpose: >
  Zero-ambiguity execution guide for May 30 08:00 UTC launch. Covers pre-launch
  verification, launch window activation, post-launch monitoring, and escalation
  triggers. Built for solo operator. Total time budget: 2.5 hours on launch day.
---

# Track B Launch Day Checklist
## Zone Cards — May 30, 2026 — Production Execution Guide

**Launch date**: Friday May 30, 2026
**Launch window**: 08:00–08:30 UTC
**Solo operator time budget**: 2–2.5 hours total (15 min pre-launch + 30 min launch window + 60 min post-launch + 30 min Day 0 monitoring)

---

## PRE-LAUNCH VERIFICATION (08:00–08:15 UTC)

Complete all items in order before posting anything publicly. This window must take no more than 15 minutes.

### 1. Zone PDF URL Live Check

- [ ] Open the Gist URL in an incognito/private browser window (not logged in)
- [ ] Confirm the Gist loads without authentication prompt
- [ ] Click through to verify all 8 PDF files are listed:
  - seedwarden-zone-3-quickstart-card.pdf
  - seedwarden-zone-4-quickstart-card.pdf
  - seedwarden-zone-5-quickstart-card.pdf
  - seedwarden-zone-6-quickstart-card.pdf
  - seedwarden-zone-7-quickstart-card.pdf
  - seedwarden-zone-8-quickstart-card.pdf
  - seedwarden-zone-9-quickstart-card.pdf
  - seedwarden-zone-10-quickstart-card.pdf
- [ ] Download one PDF (Zone 5 or Zone 6) to confirm it opens cleanly in browser
- [ ] Confirm file size is in the 630–650 KB range (any file under 100 KB signals corruption)

**Gist URL**: ___________________________________
**Backup URL** (Google Drive or Dropbox): ___________________________________

### 2. Gist Accessibility Confirmation

- [ ] Test Gist URL from mobile (iOS Safari or Android Chrome)
- [ ] Confirm PDFs are downloadable from mobile without login
- [ ] If PDFs do not open on mobile: switch to backup Google Drive link immediately (do not delay launch)

### 3. Influencer Staging Final Check

- [ ] Confirm Tier 1 outreach sent May 28 (Sabrena Gwin / AHG, Susan Leopold / UpS, John Gallagher / LearningHerbs, Reddit mods for r/herbalism, r/foraging, r/vegetablegardening) — check email sent folder or response tracking log
- [ ] Confirm Tier 2 outreach sent May 28–29 (Juliet Blankespoor, Herbal Academy, Discord admins) — check response tracking log
- [ ] Log any pre-launch responses received (herbalists who asked for preview, mods who approved posts) — these are ready to receive the launch URL right now
- [ ] If any Tier 1 contact is in the "preview requested" state: send them the Gist URL now, before public post

### 4. Social Calendar Timestamp Sync

- [ ] Confirm all scheduled posts in Buffer/Later/native schedulers reflect UTC times (not local time):
  - Instagram: 08:30 UTC (launch post)
  - TikTok: 08:45 UTC
  - Pinterest: 09:00 UTC
  - Reddit r/herbalism: 08:00 UTC (post manually — cannot be pre-scheduled)
- [ ] Confirm Instagram bio/link-in-bio shows the Gist URL
- [ ] If using a scheduling tool: verify the "May 30 zone guides are LIVE" posts have the correct final Gist URL (not the placeholder [LANDING_PAGE_URL] from the calendar template)
- [ ] If posting manually: open all post drafts in Notes app or Google Doc and verify the Gist URL is pasted in

**Pre-launch verification complete. All 4 boxes checked?** Proceed to Launch Window.

---

## LAUNCH WINDOW (08:15–08:30 UTC)

### 5. Activate Influencer Outreach — Copy-Paste Email Templates

Send the following to any herbalist contact who pre-approved sharing or who will receive the launch notification:

**Email subject**: Zone guides are live — [CONTACT_NAME], here's the link

**Email body** (copy-paste, fill bracketed fields):
```
Hi [FIRST_NAME],

The Seedwarden Zone Quick-Start Cards are live as of this morning.

All 8 zone guides — free, direct download, no email required:
[GIST_URL]

If you'd still like to share these with your [community/audience/newsletter], 
I'd love that. No obligation and no particular ask — just letting you know 
they're up.

Happy to provide pre-written social copy or a short newsletter blurb 
if that would help.

Best,
[YOUR_NAME]
Seedwarden
```

**Send to** (check each when sent):
- [ ] Sabrena Gwin (AHG) — chapters@americanherbalistsguild.com — if she confirmed interest
- [ ] Susan Leopold (UpS) — info@unitedplantsavers.org — if she confirmed interest
- [ ] John Gallagher (LearningHerbs) — partnerships@learningherbs.com — if he confirmed interest
- [ ] Juliet Blankespoor (Chestnut) — via email or Instagram DM — if she confirmed interest
- [ ] Any other contact who responded to pre-launch outreach

### 6. Post Social Media Calendar Teasers

Post in this exact sequence. The launch announcement and teasers are ready in `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`.

| UTC Time | Platform | Post type | Copy location | URL to insert |
|----------|----------|-----------|---------------|---------------|
| 08:00 | Reddit r/herbalism | Text post (manual) | Post 11 in `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` | [GIST_URL] |
| 08:30 | Instagram | Launch post (carousel or single image) | Post 8 in social calendar | [GIST_URL] |
| 08:45 | TikTok | Launch video (30–60 sec) | Post 9 in social calendar | Bio link = [GIST_URL] |
| 09:00 | Pinterest | Launch collection pin | Post 10 in social calendar | [GIST_URL] |

- [ ] Reddit post submitted (manual; cannot be pre-scheduled)
- [ ] Instagram launch post live and link-in-bio confirmed pointing to Gist
- [ ] TikTok video posted
- [ ] Pinterest pin published

**Launch window complete. Verified all 4 platforms active?** Proceed to Post-Launch Monitoring.

---

## POST-LAUNCH MONITORING (08:30 UTC onward)

### 7. Click Tracking — Bitly Setup (If Not Pre-Configured)

If a Bitly short link was not created before launch:

1. Go to bitly.com (free account sufficient)
2. Create a shortened link for your Gist URL
3. Save the Bitly link: bit.ly/seedwarden-zones or similar
4. Update Instagram bio and any remaining unposted social content with the Bitly link (the Gist URL itself still works — Bitly is additive for tracking only)

**Bitly link**: ___________________________________
**Record Day 0 baseline**: Check Bitly at 16:00 UTC and log click count here: ___

### 8. Response Monitoring

Check the following starting at 09:00 UTC and again at 12:00, 16:00, and 20:00 UTC on launch day:

| Platform | What to check | Response action |
|----------|--------------|-----------------|
| Email inbox | Replies from herbalist contacts | Respond within 2 hours; confirm partnership if asked |
| Instagram DMs | Direct messages referencing zone cards | Reply within 2 hours; thank for interest |
| Reddit post | Upvotes + comments on r/herbalism post | Reply to every comment on launch day |
| TikTok | Comments on launch video | Reply to first 5+ comments to signal engagement |
| Pinterest | Pin saves and clicks (check in Pinterest Analytics) | No response needed; note count for Day 3 report |

### 9. Day 3 / Day 7 Checkpoint Thresholds (Reference)

Detailed decision trees are in `TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md`. Summary:

| Checkpoint | Date | Key threshold | Decision if below threshold |
|------------|------|--------------|----------------------------|
| Day 3 | June 2 | 50+ Gist views | Escalate Tier 3 outreach + Reddit repost |
| Day 3 | June 2 | 20+ Reddit upvotes | Revise Reddit post title, re-frame as community resource |
| Day 7 | June 6 | 150+ Gist views | Send follow-up DMs to non-responding Tier 1 contacts |
| Day 7 | June 6 | 3+ organic shares | Create Instagram carousel post if shares = 0 |
| Day 14 | June 13 | 300+ Gist views | Full decision framework in monitoring doc |

Record Day 0 metrics at end of May 30:

```
Day 0 (May 30) Snapshot
Gist views: ___
Reddit upvotes (r/herbalism): ___
Instagram reach: ___
TikTok views: ___
Direct messages received: ___
Herbalist contacts who engaged: ___
```

---

## ESCALATION TRIGGERS

### Escalation 1: Response Falls Below Day 3 Threshold

**Trigger**: Fewer than 50 Gist views by June 2 (Day 3).

**Immediate actions** (in order, each takes 15 minutes or less):
1. Send Tier 3 outreach to any contacts not yet reached: Richo Cech (Strictly Medicinal Seeds, newsletter), Katja Swift + Ryn Midura (Holistic Herbalism Podcast, New England Zone 5–6 audience), Seattle Herbalism Society (Facebook, Pacific Northwest)
2. Post in one additional Reddit community: r/foraging if not yet posted, or r/homesteading as alternative
3. Add one Instagram Story with direct link sticker pointing to Gist: copy "Zone cards are live — free for every zone" + link sticker

**Do not**: run paid promotion at Day 3. Wait for Day 7 data before any budget decision.

### Escalation 2: Gist Goes Down

**Trigger**: Gist URL returns 404 or GitHub is unreachable during launch window.

**Immediate actions** (complete within 10 minutes):
1. Switch to backup URL (Google Drive folder or Dropbox link — must be pre-prepared by May 29)
2. Update Instagram bio/link-in-bio immediately
3. Edit any Reddit posts already submitted: add "Edit: Updated link — [new URL]" to post body
4. Post one Instagram Story: "Link updated — grab it in bio" with new link sticker
5. Update any remaining unposted social content with the backup URL
6. Proceed — do not delay the launch because of a link swap

**Backup URL must be confirmed by May 29 evening.** If backup URL is not ready, create a Google Drive shared folder (Anyone with link, view access) and upload all 8 PDFs before May 30.

### Escalation 3: Influencers Do Not Engage by Day 7

**Trigger**: Fewer than 2 of the 15 herbalist contacts have responded (any response counts: reply, share, DM) by June 6.

**Assess first**: Check whether your May 28 outreach emails were sent. If unsent, send them immediately. This is the most common reason for zero influencer response.

**If outreach was sent and still no response**:
1. Send one gentle follow-up to Tier 1 contacts (Sabrena Gwin, John Gallagher): subject line "Quick follow-up on the zone guides" — one sentence only: "Did you get a chance to look at the cards? Happy to send a direct PDF preview if that would help."
2. Try the Instagram DM route for any contact you only reached by email (shorter message, more likely to get a read)
3. Do not send more than one follow-up per contact. Frequency does not increase response rates at this stage.

**Adjust for Phase 3**: If influencer channel produces fewer than 3 responses total across all 15 contacts by Day 14, de-prioritize influencer outreach as the primary channel for Phase 3. Organic Reddit and Pinterest will be the primary distribution levers instead.

### Escalation 4: Social Platforms Block or Remove Posts

**Trigger**: Reddit removes posts within the first 24 hours, or Instagram reduces post reach below 50 users.

**Reddit removal**:
1. Check removal reason (mod message or automated filter notification)
2. If promotional framing triggered the filter: repost with personal framing — "I built a free zone guide, here's Zone [X] as an image" and upload a single card as an image (not a link post)
3. Image posts bypass most subreddit promotional filters and perform better anyway
4. If mod-banned for the account: do not create a new account; pivot to r/foraging and r/homesteading where post was not attempted

**Instagram shadowban or low reach**:
1. Do not delete and repost (this makes it worse)
2. Post one Instagram Story immediately after the main post to signal account activity
3. Reply to any comment within 1 hour of posting to boost engagement signals
4. Low reach on launch day does not indicate a permanent problem — algorithm visibility improves on Day 2–3 as engagement accumulates

---

## POST-LAUNCH DAILY ACTIONS (May 31+)

| Day | Action | Time estimate |
|-----|--------|---------------|
| May 31 (Day 1) | Respond to all DMs and comments received on launch day | 20 min |
| May 31 (Day 1) | Post June 1 Zone 3 Spotlight content (see `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`) | 15 min |
| June 1 (Day 2) | Post June 2 Wild Edibles angle content | 15 min |
| June 2 (Day 3) | Run Day 3 checkpoint (see monitoring doc) | 10 min |
| June 2 (Day 3) | Post June 3 Native Plants / AHG crossover content | 15 min |
| June 6 (Day 7) | Run Day 7 checkpoint (see monitoring doc) | 10 min |
| June 6 (Day 7) | Post June 6 community milestone engagement post | 15 min |
| June 13 (Day 14) | Run Day 14 checkpoint — Phase 3 go/no-go decision input | 15 min |

---

## Quick-Reference Card (Print This)

```
MAY 30 LAUNCH — TIMES IN UTC

08:00 — Pre-launch verification (15 min)
        - Gist URL test in incognito: YES / NO
        - All 8 PDFs accessible: YES / NO
        - Social posts have real URL (not placeholder): YES / NO

08:00 — Reddit r/herbalism post (manual)
08:15 — Email herbalist contacts who pre-approved
08:30 — Instagram launch post
08:45 — TikTok launch video
09:00 — Pinterest launch pin

16:00 — Check Bitly clicks + Reddit upvotes
20:00 — Reply to all comments and DMs
Before bed — Record Day 0 metrics (Gist views, upvotes, reach)

ESCALATION CONTACTS
Gist down → switch to backup URL (saved here: _________________)
Reddit removed → repost as image post
Influencer no response → one gentle follow-up email/DM (June 2)

DAY 3 THRESHOLD: 50+ Gist views (June 2)
DAY 7 THRESHOLD: 150+ Gist views (June 6)
DAY 14 THRESHOLD: 300+ Gist views (June 13)
```

---

*Document version: 2.0 — May 26, 2026*
*Supersedes: version 1.0 (same filename, dated May 26, 2026 — that version used local-time launch window; this version uses UTC throughout)*
*Reference documents: TRACK_B_HERBALIST_OUTREACH_MATRIX.md, HERBALIST_OUTREACH_CONTACT_LIST.md, TRACK_B_SOCIAL_CALENDAR_MAY28_30.md, TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md, ZONE_PDF_VERIFICATION_REPORT.md*
