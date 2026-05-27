---
title: "Track B Launch Day Runbook — May 30, 2026"
date: 2026-05-27
version: 1.0
session: 1691
status: production-ready
purpose: >
  Step-by-step execution runbook for May 30 08:00 UTC launch. Covers the
  full 07:30–21:00 UTC operator window: pre-launch system verification,
  launch window 3-channel sequencing, post-launch monitoring cadence,
  and end-of-day wrap-up. Executable without reference to any other
  document during the launch window.
references:
  - TRACK_B_LAUNCH_DAY_CHECKLIST.md (Version 2.0 — pre-launch verification detail)
  - TRACK_B_SOCIAL_CALENDAR_MAY28_30.md (post copy for all launch posts)
  - INFLUENCER_STAGING_VERIFICATION.md (contact list + template assignments)
  - HERBALIST_PARTNERSHIP_EMAIL_TEMPLATE.md (Templates A–E, copy-paste ready)
  - CONTINGENCY_DECISION_THRESHOLDS.md (Day 3/7/14 threshold framework)
  - TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md (monitoring checkpoint decision trees)
  - CONTINGENCY_DECISION_PLAYBOOK.md (this session, Scenario 1–6 responses)
---

# Track B Launch Day Runbook
## May 30, 2026 — 07:30–21:00 UTC

**Launch**: May 30, 2026, 08:00 UTC
**Status entering launch day**: 100% production-ready (verified May 26, Session 1687)
**Total operator time budget**: 3.5–4.0 hours across the full day
**This document is self-contained**: all post copy, threshold numbers, and decision points are here. No other documents need to be open during the launch window.

---

## Phase 1 — Pre-Launch Checklist
### 07:30–07:55 UTC (25 minutes)

Complete all items below before touching any live platform. Work through the four blocks in order. Each block has a GO / HOLD decision at the end.

---

### Block 1A: System Logins (07:30–07:38 UTC)
**Time budget: 8 minutes**

Verify access to every tool you will use during the launch window. If any login fails, resolve it now — not during the launch window.

- [ ] **Canva** — Log in at canva.com (wanka95@gmail.com). Confirm Brand Kit is accessible: Brand Hub > your Brand Kit name. Confirm the zone card Canva files are present in "Projects."
- [ ] **Kit (email automation)** — Log in at kit.com. Confirm you land on the dashboard with the zone card automation visible. Confirm the subscriber count is greater than 0 (if any pre-launch subscribers enrolled).
- [ ] **Instagram** — Log in to the @seedwarden account (or the handle you claimed). Confirm you reach the profile page without 2FA friction. Have the launch post draft queued in Buffer/Later or saved in Notes.
- [ ] **TikTok** — Log in to the @seedwarden TikTok account. Confirm the launch video draft is saved in Drafts or a local folder ready to upload.
- [ ] **Pinterest** — Log in to the seedwarden Pinterest business account. Confirm the launch pin draft is staged.
- [ ] **Gmail / email client** — Log in and confirm you can send from the Seedwarden email address. Compose window open and ready.
- [ ] **Reddit** — Log in to your Reddit account. Navigate to r/herbalism. Confirm you can submit a new post (the "Create Post" button is visible). If the community requires mod approval, confirm the May 28 outreach to r/herbalism mods has been sent.

**Block 1A decision**:
- All 7 logins confirmed → proceed to Block 1B
- Any login inaccessible → resolve before 07:45 UTC. If not resolved by 07:45, note it and proceed; address during Block 1B recovery time.

---

### Block 1B: File Integrity Checks (07:38–07:48 UTC)
**Time budget: 10 minutes**

Verify all 8 zone card PDFs are reachable at their public distribution URL, and that template files are loaded in their platforms.

**PDF verification (open an incognito / private-mode browser window for each check):**

- [ ] Navigate to the Gist URL (your primary distribution URL)
- [ ] Confirm the Gist loads without an authentication prompt
- [ ] Confirm all 8 zone card files are listed:
  - seedwarden-zone-3-quickstart-card.pdf
  - seedwarden-zone-4-quickstart-card.pdf
  - seedwarden-zone-5-quickstart-card.pdf
  - seedwarden-zone-6-quickstart-card.pdf
  - seedwarden-zone-7-quickstart-card.pdf
  - seedwarden-zone-8-quickstart-card.pdf
  - seedwarden-zone-9-quickstart-card.pdf
  - seedwarden-zone-10-quickstart-card.pdf
- [ ] Download Zone 5 PDF. Confirm it opens in-browser and is 630–650 KB (any file under 100 KB signals corruption — see Scenario 7 in the Contingency Playbook)
- [ ] Test the Gist URL from your phone in a browser (not the app). Confirm PDFs are downloadable without logging in.

**Backup URL check:**
- [ ] Confirm your backup Google Drive / Dropbox folder URL is written down somewhere accessible (not just in your memory). Write it here: `_______________________`
- [ ] Open the backup URL in incognito to confirm it resolves (this is a 30-second check)

**Template and automation check:**
- [ ] Open Kit dashboard. Confirm the zone-card delivery automation is in "Published" state (not Draft). If it shows "Draft," publish it now before proceeding.
- [ ] Confirm the Kit landing page URL is live: open it in incognito and confirm the sign-up form appears and the "Send My Zone Card" button is visible.
- [ ] Confirm the Instagram, TikTok, and Pinterest bio links all point to the correct URL (Gist URL or Kit landing page — whichever is your primary CTA).

**Block 1B decision**:
- All PDFs accessible + automation Published + bios correct → proceed to Block 1C
- Any PDF inaccessible → switch to backup URL immediately. Update all bio links before proceeding. (See CONTINGENCY_DECISION_PLAYBOOK.md Scenario 7)
- Kit automation in Draft → publish it now. This is a 2-minute action in Kit settings.

---

### Block 1C: Channel Test Sends (07:48–07:53 UTC)
**Time budget: 5 minutes**

One test action per channel to confirm everything fires before going public.

- [ ] **Email test**: In Kit, send a test email to yourself (wanka95@gmail.com). Open it in your email client. Confirm the zone card download link in the email resolves to the correct Gist URL. Confirm no [PLACEHOLDER] text is visible anywhere in the email.
- [ ] **Social post preview**: Open the launch Instagram post draft (in Buffer, Later, or Notes). Read through the full caption. Confirm the Gist URL is inserted where [LANDING_PAGE_URL] appeared in the template. Confirm no bracket placeholders remain.
- [ ] **DM template scan**: Open the launch-day influencer DM template (Email subject: "Zone guides are live — [CONTACT_NAME], here's the link" from TRACK_B_LAUNCH_DAY_CHECKLIST.md Section 5). Confirm the Gist URL placeholder has been replaced with the real URL.

**Block 1C decision**:
- All three tests pass (no placeholders, links resolve) → proceed to Block 1D
- Placeholder URL found in Kit email → update the email in Kit before proceeding (2 minutes)
- Placeholder URL found in social posts → update the draft before proceeding (1 minute)

---

### Block 1D: Final Pre-Launch Decision (07:53–07:55 UTC)
**Time budget: 2 minutes**

Answer these three questions. All three must be YES to proceed to the launch window.

1. Are all 8 zone card PDFs publicly accessible at the distribution URL? **YES / NO**
2. Is the Kit zone-card delivery automation in Published state? **YES / NO**
3. Do all social post drafts contain the real distribution URL (not a placeholder)? **YES / NO**

**All three YES**: You are cleared for launch. Move to Phase 2 at 08:00 UTC.

**Any NO**: Hold. Resolve the failing item. The 08:00 UTC launch time is a soft target. A 15–30 minute delay to fix a critical issue is better than a broken launch. Do not proceed with a broken distribution link.

---

## Phase 2 — Launch Window
### 08:00–08:30 UTC (30 minutes)

Execute the 3-channel activation in the order below. The order matters: Reddit posts first because Reddit's algorithm rewards early organic engagement before external links appear on social; email goes second to notify the pre-qualified audience; influencer DMs go last because they get best response during business hours and should accompany, not precede, public posts.

---

### Step 1: Reddit (08:00 UTC — Manual)
**Time budget: 5 minutes**

Reddit posts cannot be pre-scheduled. Post manually.

Navigate to r/herbalism. Submit a new post using the launch post copy from `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` Post 11.

**Post title** (copy exactly):
```
Free zone-specific quick-start guides for herbalists and gardeners — all 8 USDA zones, no email required
```

**Post body** (copy exactly):
```
I spent the last few weeks building zone-specific quick-start cards for gardeners and herbalists. Each card covers:

- First/last frost dates for your zone
- Best planting windows for medicinal herbs + vegetables
- Top 5 wild edibles in season by month
- Soil prep notes and variety recommendations

All 8 zones (3–10) are free to download here: https://gist.github.com/esca8peArtist/db0b1798b5b70ff988367982176dc49d

Zone 5 and Zone 7 are the most requested — if you're in one of those, the timing tables in the card are the main thing people find useful.

Happy to answer questions about specific zones or what went into the research.
```

After posting:
- [ ] Confirm post is live on r/herbalism
- [ ] Take a screenshot of the submitted post (for audit trail)
- [ ] Note the post URL: `_______________________`

**Timing rationale**: 08:00 UTC = 04:00 AM EDT. This is a low-traffic Reddit window, which means your post gets indexed without being immediately buried by competition. Early upvotes in the first 2 hours are more algorithmically valuable than posting into a busy mid-day window. If the post needs more traction, a follow-up comment at 12:00–14:00 UTC can revive it.

---

### Step 2: Email to Pre-Approved Influencer Contacts (08:05–08:15 UTC)
**Time budget: 10 minutes**

Send the launch notification email to every herbalist contact who responded to pre-launch outreach (any response: reply, preview request, expressed interest, or mod approval for community post). Do not send to contacts who have not responded — those go in Phase 3 (DMs, 08:15 UTC).

**Email subject**: Zone guides are live — [CONTACT_NAME], here's the link

**Email body**:
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

Send to all contacts who responded to pre-launch outreach:
- [ ] Sabrena Gwin (chapters@americanherbalistsguild.com) — if she confirmed interest
- [ ] Susan Leopold (info@unitedplantsavers.org) — if she confirmed interest
- [ ] John Gallagher (partnerships@learningherbs.com) — if he confirmed interest
- [ ] Juliet Blankespoor (chestnutherbs.com form or Instagram DM) — if she confirmed interest
- [ ] Any other contact who responded to pre-launch outreach

**After sending**: Check email sent folder and confirm each message delivered (no bounce notification within 2 minutes).

**Timing rationale**: Email at 08:05 UTC (04:05 AM EDT) lands in inboxes before the US business day starts. Contacts who check email at 08:00–09:00 their local time (noon–13:00 UTC for US East) will see a message that arrived at a predictable professional time. Do not wait until afternoon — same-day delivery with morning arrival is the goal.

---

### Step 3: Instagram Launch Post (08:30 UTC)
**Time budget: 3 minutes (if pre-scheduled) or 5 minutes (if manual)**

Publish or confirm the scheduled Instagram launch post from `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` Post 8.

If pre-scheduled via Buffer/Later: confirm the post is queued for 08:30 UTC and the URL is correct. Let it fire automatically.

If posting manually:
- Open the launch post draft
- Confirm the Gist URL is in the caption
- Post and immediately check that the link-in-bio also shows the Gist URL
- [ ] Instagram launch post live

**Screenshot record**: Take a screenshot of the live post showing the timestamp. Save to a local folder for audit trail.

**Timing rationale**: 08:30 UTC = 04:30 AM EDT. Instagram's algorithm gives the first 30 minutes of engagement outsized ranking weight. By posting at 08:30 UTC, the post accumulates early engagement from UTC+0 through UTC+3 audiences (UK, Western Europe, Middle East gardening and herbalism communities) before US audiences wake. This 3–4 hour head start on engagement signals improves algorithmic visibility for US prime-time feed rankings (12:00–18:00 UTC).

---

### Step 4: TikTok Launch Video (08:45 UTC)
**Time budget: 3 minutes (if pre-scheduled) or 5 minutes (if uploading natively)**

Post the TikTok launch video from `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` Post 9.

TikTok requires native upload for full algorithmic reach — do not cross-post from Instagram.

If uploading manually:
- Open TikTok app or creator studio
- Upload the launch video (saved locally or in Drafts)
- Use the caption from the social calendar
- Add the Gist URL to the TikTok bio if not already there (TikTok does not allow clickable links in video descriptions — only in bio)
- Post at 08:45 UTC
- [ ] TikTok launch video live

**Optional afternoon boost**: TikTok's algorithm is more time-zone sensitive than Instagram. If you have 10 minutes available at 16:00–18:00 UTC, post a 15-second follow-up TikTok ("checking in on zones — what zone did you pick up?") to create a second algorithmic push during US peak hours. This is additive, not required.

---

### Step 5: Pinterest Launch Pin (09:00 UTC)
**Time budget: 2 minutes (if pre-scheduled) or 4 minutes (if manual)**

Publish the Pinterest launch collection pin from `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` Post 10.

If pre-scheduled: confirm it fires at 09:00 UTC.

If posting manually:
- Open Pinterest creator hub
- Create a new pin with the launch pin image (saved in Canva or locally exported)
- Add the caption + Gist URL as the destination link
- Pin to the primary Seedwarden board
- [ ] Pinterest launch pin live

**Timing note**: Pinterest is the least time-sensitive platform in this launch stack. The 09:00 UTC time keeps all channels within a 60-minute window for a coordinated launch signal. Pinterest's highest-traffic window is 20:00–22:00 UTC — if you want a second Pinterest push later in the day, post a Zone 5 deep-dive pin at 20:00 UTC.

---

### Step 6: Influencer DMs — Non-Responded Contacts (08:15–08:30 UTC, during other steps)
**Time budget: 10 minutes (parallel to Steps 3–5)**

For contacts who did NOT respond to pre-launch outreach, send a brief launch-day DM. Keep these short — this is a notification, not a pitch.

**DM format** (adapt by platform — Reddit modmail, Discord DM, Instagram DM, or Facebook message):
```
Hi [NAME] — the Seedwarden Zone Quick-Start Cards are live today. Free download for all 8 zones: [GIST_URL]. Thought your community might find them useful. No obligation.
```

Send to all 15 influencer contacts who have not yet responded. Check off each as sent:
- [ ] r/herbalism mods (Reddit modmail)
- [ ] r/gardening mods (Reddit modmail)
- [ ] r/HerbalMedicine mods (Reddit modmail)
- [ ] The Herbal Haven Discord admin (Discord DM)
- [ ] Materia Medica Discord admin (Discord DM)
- [ ] Herb Club Discord admin (Discord DM)
- [ ] Seattle Herbalism Society admin (Facebook message)
- [ ] AHG chapter coordinator contacts (via Sabrena Gwin if not yet responded)
- [ ] Herbal Academy (partnerships@theherbalacademy.com)
- [ ] Any remaining contacts from `INFLUENCER_STAGING_VERIFICATION.md`

**Timing rationale**: 08:15 UTC DMs arrive in inboxes before US business hours. Contacts checking messages at 09:00–10:00 their local time (13:00–14:00 UTC for East Coast) see the notification as a same-morning message, not an overnight one.

---

### Launch Window Completion Check (08:30 UTC)

Before moving to post-launch monitoring, confirm:

- [ ] Reddit post live at r/herbalism (post URL recorded)
- [ ] Email sent to all pre-approved influencer contacts (sent folder confirmed)
- [ ] DMs sent to all 15 non-responded contacts (all boxes checked above)
- [ ] Instagram launch post live (screenshot taken)
- [ ] TikTok launch video live (screenshot taken)
- [ ] Pinterest launch pin live (screenshot taken)

**All 6 confirmed**: Proceed to Phase 3 monitoring.

**Any item not yet done**: Complete it before the 09:00 UTC first check. The launch window extends to 08:30 UTC — a 30-minute delay on any single channel is acceptable. Do not skip any channel entirely.

---

## Phase 3 — Post-Launch Monitoring
### 08:30–20:00 UTC

The monitoring phase has two cadences: hourly pulse checks for the first 6 hours (08:30–14:30 UTC), then 4-hour intervals for the remainder of the day.

---

### Monitoring Dashboard — What to Track

Use the Google Sheets KPI dashboard (`projects/seedwarden/analytics/` or the template in `CONTINGENCY_DECISION_THRESHOLDS.md`). Record these metrics at each check-in:

| Metric | Where to check | Notes |
|--------|---------------|-------|
| Gist views (cumulative) | gist.github.com — view counter (owner-visible) | Subtract prior checkpoint count for delta |
| Reddit upvotes | Your Reddit profile > submitted posts | r/herbalism post + any other communities |
| Instagram reach | Instagram Insights > Content > launch post | Reach, not impressions — unique accounts |
| TikTok views | TikTok app > your videos | View count on launch video |
| Kit subscribers (new) | Kit dashboard > subscriber count | New sign-ups since launch |
| Email open rate | Kit dashboard > Broadcasts or automation analytics | For any launch-day broadcast sent |
| DM / email replies received | Gmail inbox + Instagram DMs | Count inbound messages referencing zone cards |
| Influencer confirmations | Email / DM sent folder | Count of contacts who confirmed they'll share |

---

### Hourly Pulse Checks (09:00, 10:00, 11:00, 12:00, 13:00, 14:30 UTC)

Each check takes 5 minutes. Record numbers in the tracking log. At each check, answer one question: is anything below the concern threshold?

**Concern thresholds for Day 0 pulse checks:**

| Metric | By 12:00 UTC (4 hours) | By 16:00 UTC (8 hours) | Escalation if below |
|--------|------------------------|------------------------|---------------------|
| Reddit post is live (not removed) | YES | YES | See Contingency Scenario 4 |
| Gist views | 10+ | 25+ | See Contingency Scenario 3 |
| Any influencer response (reply/DM) | 1+ | 2+ | See Contingency Scenario 4 |
| Instagram post reach | 30+ | 75+ | See Contingency Scenario 2 |
| No platform error messages | YES | YES | See Contingency Scenario 7 |

**12:00 UTC is the first hard decision point**: If Gist views are below 10 by 12:00 UTC, run the distribution diagnostic from `CONTINGENCY_DECISION_PLAYBOOK.md` before the next check.

At each hourly check, take 1 minute to reply to any comments or DMs received. Responding to Reddit comments on launch day is the single highest-ROI action for early post performance.

---

### 4-Hour Interval Checks (16:00 and 20:00 UTC)

**16:00 UTC check (full Day 0 mid-point)**

Record all metrics in the tracking log. Make one binary decision:

- Is anything triggering a contingency scenario? If yes, open `CONTINGENCY_DECISION_PLAYBOOK.md` and follow the matching decision tree.
- Is everything on track? Log the numbers and continue.

At 16:00 UTC, also post a Reddit follow-up comment on your r/herbalism launch post if it has received upvotes. Format: "Thanks for the interest — Zone 7 seems to be the most popular so far. Happy to answer any questions about specific zones." This re-engages the thread and boosts algorithmic visibility.

**Optionally at 16:00 UTC**: Post the additional TikTok video if you have 10 minutes available (see Step 4 note above).

**20:00 UTC check (Day 0 wrap-up)**

Final check of the day. Record all metrics. Respond to any outstanding comments or DMs. Complete the end-of-day wrap-up (Phase 4).

---

## Phase 4 — End-of-Day Wrap-Up
### 20:00–21:00 UTC

**Time budget: 30–45 minutes**

---

### Step 1: Aggregate Day 0 Metrics (20:00–20:15 UTC)

Fill in the Day 0 snapshot (copy this into your tracking log or Google Sheet):

```
Day 0 (May 30) Snapshot — logged [TIME] UTC

DISTRIBUTION
Gist views (cumulative): ___
Reddit r/herbalism upvotes: ___
Reddit comments: ___
Instagram reach (launch post): ___
Instagram new followers: ___
TikTok views (launch video): ___
Pinterest saves: ___
Kit new subscribers: ___
Bitly clicks (if tracking): ___

INFLUENCER ENGAGEMENT
Contacts reached (DM/email sent): ___ of 15
Contacts who responded (any response): ___
Contacts who confirmed they'll share: ___
Contacts who shared publicly: ___

CUSTOMER / COMMUNITY
DM or email inquiries received: ___
Comments responded to: ___
Any notable qualitative feedback (1–3 sentences): ___

TECHNICAL
Any platform errors or issues: YES / NO (describe if YES)
Gist URL accessible throughout day: YES / NO
Kit automation fired correctly: YES / NO (test a subscriber flow if unsure)
```

---

### Step 2: Compare Against Day 3 Baseline (20:15–20:25 UTC)

The Day 3 threshold from `CONTINGENCY_DECISION_THRESHOLDS.md`:
- Gist views > 30 by Day 3 (June 2) = baseline working
- Gist views > 70 by Day 3 = activate Track A holdout influencers
- Reddit upvotes > 10 by Day 3 = healthy distribution

At Day 0, you are targeting at least 20–30% of the Day 3 baseline. A rough target for end-of-day May 30:
- Gist views: 10–25 (organic/launch day without major influencer amplification)
- Reddit upvotes: 5–15 on the r/herbalism post
- Instagram reach: 50–150 (new account baseline)

If Day 0 numbers are higher than these rough targets: strong start, influencer outreach is working, no action change.

If Day 0 numbers are lower: do not panic. New product, new accounts, new subreddit post — Day 0 is rarely a strong indicator. The Day 3 data (June 2) is the first meaningful checkpoint.

---

### Step 3: Qualitative Notes (20:25–20:40 UTC)

Record answers to these questions in the tracking log (3–5 sentences total):

1. What did the customer / community response look like? Any notable comments, questions, or DMs?
2. Which platform showed the most activity?
3. Were there any technical issues (login problems, broken links, Kit automation errors)?
4. Were there any unexpected positive signals (organic repost, influencer share, unexpected community engagement)?
5. What is the single most important action for tomorrow (May 31)?

---

### Step 4: Prepare for Day 3 Checkpoint (20:40–21:00 UTC)

The Day 3 checkpoint is June 2, 2026 at 08:00 UTC. It is documented in `TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md` and `CONTINGENCY_DECISION_THRESHOLDS.md`.

Before closing out May 30:

- [ ] Post May 31 / June 1 social content is queued (check `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md` for June 1–7 ramp-up schedule)
- [ ] Day 0 snapshot is logged in tracking log
- [ ] Any open influencer responses have been replied to
- [ ] No unresolved platform issues (if any exist, document them for the June 2 review)

**The Day 3 decision gate (June 2, 08:00 UTC)** is covered in full in `DAY_3_AND_7_DECISION_GATES.md`. The primary Day 3 question is whether to activate the Track A holdout influencer cohort.

---

## Quick-Reference Card (Print or Screenshot This)

```
MAY 30 LAUNCH — ALL TIMES UTC

PRE-LAUNCH (07:30–07:55)
  07:30 — Verify 7 platform logins
  07:38 — Verify all 8 PDFs accessible (incognito)
  07:48 — Test email send to self; scan post drafts for placeholders
  07:55 — GO / HOLD decision (all 3 YES required)

LAUNCH WINDOW (08:00–08:30)
  08:00 — Reddit r/herbalism post (manual, copy from social calendar Post 11)
  08:05 — Email to pre-approved influencer contacts
  08:15 — DMs to all 15 non-responded contacts (parallel)
  08:30 — Instagram launch post
  08:45 — TikTok launch video
  09:00 — Pinterest launch pin

MONITORING (hourly 09:00–14:30, then 16:00, 20:00)
  12:00 — First hard decision point (any contingency scenarios?)
  16:00 — Mid-day check + optional Reddit comment + optional TikTok boost
  20:00 — End-of-day wrap-up begins

CONCERN THRESHOLDS (Day 0)
  By 12:00 UTC: Reddit post still live, 10+ Gist views, 1+ influencer response
  By 16:00 UTC: 25+ Gist views, 2+ influencer responses, no platform errors

END-OF-DAY (20:00–21:00)
  Log Day 0 snapshot
  Queue May 31 content
  No open platform issues

BACKUP URL: ___________________________

CONTINGENCY PLAYBOOK: CONTINGENCY_DECISION_PLAYBOOK.md
```

---

*Document version: 1.0 — May 27, 2026, Session 1691*
*Reference documents (do not open during launch window unless a contingency fires): TRACK_B_LAUNCH_DAY_CHECKLIST.md, TRACK_B_SOCIAL_CALENDAR_MAY28_30.md, INFLUENCER_STAGING_VERIFICATION.md, HERBALIST_PARTNERSHIP_EMAIL_TEMPLATE.md, CONTINGENCY_DECISION_THRESHOLDS.md, TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md*
