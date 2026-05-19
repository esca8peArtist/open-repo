---
title: "Gate 3 — Kit Pre-Build Brief"
created: 2026-05-19
gate: Gate 3 (Kit account, tags, landing page, email sequence)
gate-window: May 27–28, 2026
purpose: >
  Everything resolved and copy-paste ready before you open kit.co.
  Reading this brief (10 minutes) replaces all decision-making during the Kit session.
  Your Kit session should be pure UI execution, zero decisions.
references:
  - KIT_SETUP_NOTES.md (platform configuration details)
  - TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md (full setup steps)
  - TRACK_B_EMAIL_SEQUENCES.md (copy-paste email bodies + metadata)
  - marketing/email-and-launch-plan.md (email copy source)
prerequisites:
  - Gate 2 complete (Canva Brand Kit live) — brand visuals may be referenced in landing page
  - Zone card PDFs built and on Google Drive with tested download links — required for Email 1
---

# Gate 3 — Kit Pre-Build Brief

**When to read this**: Before your May 27 Kit session. Read once. Then open kit.co and execute.

**Time for the Kit session**: 3–4.5 hours total across May 27–28, split into phases:
- Phase A — Account creation + tags: 15–20 minutes
- Phase B — Landing page: 25–30 minutes
- Phase C — Email sequence (all 5 emails): 60–90 minutes
- Phase D — Zone routing automation: 20–30 minutes
- Phase E — 3-test protocol: 20 minutes
- Phase F — DNS propagation wait: 24–48 hours (passive; start May 27 so DNS is settled by May 29)

**Critical path note**: Start the Kit account on May 27, not May 28. SPF/DKIM DNS records take 24–48 hours to propagate. If you create the account May 28 evening, DNS may not be settled when you run the May 29 3-test protocol, causing deliverability failures that look like automation errors.

---

## Resolved Decisions — Read Before Opening Kit

All decisions below are made. You do not need to evaluate them during your session.

### Account Configuration

| Field | Value | Reason |
|-------|-------|--------|
| Email | wanka95@gmail.com | Single email for all platforms |
| Sender name | Seedwarden | Brand name as sender — not personal name |
| Sender email | wanka95@gmail.com | Upgrade to custom domain in Phase 3 |
| Time zone | Your local time zone | Automation delays are relative to this |
| Business type | Creator | Matches Kit's Creator workflow; e-commerce also acceptable |
| Tier | Free | Free tier supports 10,000 subscribers, unlimited sends, 1 landing page, conditional automation — adequate for launch |

**Do not pay for Kit Creator ($33/month) at signup.** The free tier covers everything needed for Phase 2 launch. The Creator tier decision happens at Gate 3 (May 27–28) based on whether free tier limitations block any specific feature you need. The Gate 3 decision framework is at the bottom of this document.

---

### Tag Names — Create All 15 Before Anything Else

Create tags before building the landing page or automation. Tag names are case-sensitive in Kit.

**Zone tags (8) — create these first**:
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

**Interest cohort tags (7) — create immediately after zone tags**:
```
seed-saver
forager
food-preserver
homesteader
medicinal-herbs
vip-buyer
phase-1-buyer
```

Navigation path in Kit: Subscribers > Tags > "Create a tag" > type name > Enter > repeat.

Do not use spaces in tag names. Do not capitalize. The names above are exact — automation rules reference them by exact string.

---

### Landing Page Configuration — All Fields Pre-Filled

**Template choice**: Select the simplest single-column template available. "Minimal" or "Simple" if those names appear. Seedwarden's audience responds to plain information delivery, not polished marketing aesthetics. A simpler template also loads faster on mobile.

**Page fields — paste exactly as shown**:

Headline:
```
Your Free Zone Quick-Start Card
```

Subheadline:
```
Know exactly what to plant, when to plant it, and what to do right now in your zone — one-page reference card, free.
```

Form fields (add in this order):
1. First Name — required
2. Email — required
3. Growing zone — required, type: Dropdown, options: Zone 3, Zone 4, Zone 5, Zone 6, Zone 7, Zone 8, Zone 9, Zone 10

CTA button text:
```
Send My Zone Card
```

Trust text (add below the button — smaller font, gray):
```
No spam. Unsubscribe anytime. Seedwarden sends one email per week about growing, foraging, and real food.
```

Background color: white or `#F5EDD6` (Warm Cream — your Brand Kit color). White is acceptable if the template does not support custom hex backgrounds without Pro.

**After publishing**: Copy the landing page URL. You will add it to Instagram bio, TikTok bio, and Pinterest website field immediately after Gate 3 is complete.

---

### Zone Routing — Option A (Recommended for Launch)

Build 8 variants of Email 1, one per zone. Use Kit's automation rule: "If subscriber has tag zone-5, send Email 1 Zone 5 variant."

Do not attempt Option B (liquid tag dynamic insertion) for launch. Option B requires correct custom field mapping and is fragile to debug under time pressure. Option A is explicit and verifiable.

**Build order for Email 1 variants** (build Zone 5 first — statistically the most common):
Zone 5 → Zone 6 → Zone 7 → Zone 8 → Zone 3 → Zone 4 → Zone 9 → Zone 10

**What changes between Email 1 variants**:
- Zone number in subject line: "Your Zone 5 Quick-Start Card is here"
- Zone card download link: the Google Drive `/uc?export=download&id=[FILE_ID]` URL for that zone
- Zone reference in body: one mention of the zone number ("your Zone 5 card")

**What stays the same between Email 1 variants**:
- Subject prefix: "Your Zone [X] Quick-Start Card is here"
- Preview text: same across all variants
- Body copy (except zone-number reference): identical
- CTA button text: "Download Your Zone Card"
- Everything after the first paragraph

---

### Email Sequence Build Plan

Full copy for all 5 emails is in `TRACK_B_EMAIL_SEQUENCES.md`. Do not write new copy during the Kit session — all text is copy-paste ready.

**Build order**: Email 1 (8 variants) → Email 2 → Email 3 → Email 4 → Email 5

Do not build Email 1 last. Email 1 is the delivery email and must be verified first in the 3-test protocol. Building it first lets you test early.

**Email 1 critical fix before saving**: After pasting body copy, search for any reference to a specific calendar date (e.g., "May 20 (tomorrow)"). Delete the parenthetical if found. The correct reference is just "the guide preview."

**Email 5 critical fix before saving**: `TRACK_B_USER_GATES.md` flags a stale date reference "May 20 (tomorrow)" in Email 5. Find and remove this before saving Email 5. Search the body for "tomorrow" and replace the entire parenthetical with nothing — just the surrounding sentence without the date reference.

**Automation trigger**: Set to "When subscriber joins via landing page" — not manual, not other trigger. This is the only trigger that connects form submission to Email 1 delivery.

**Delay settings** (from `TRACK_B_EMAIL_SEQUENCES.md`):
- Email 1: Immediately
- Email 2: 2 days after Email 1
- Email 3: 3 days after Email 2 (Day 5 from subscribe)
- Email 4: 2 days after Email 3 (Day 7)
- Email 5: 3 days after Email 4 (Day 10)

---

### Google Drive Link Format — Critical

Zone card PDF links in Email 1 must use this URL format:
```
https://drive.google.com/uc?export=download&id=[FILE_ID]
```

NOT this format (which opens a viewer page, not a download):
```
https://drive.google.com/file/d/[FILE_ID]/view
```

The `/uc?export=download` format triggers an immediate file download in the subscriber's browser. The `/view` format opens a Drive viewer that requires the subscriber to click "Download" again, and in Gmail it opens inline — subscribers may not find the actual PDF.

To get the FILE_ID: right-click any file in Google Drive > "Get link" > copy the URL. The FILE_ID is the long string between `/d/` and `/view` in the share URL. Paste it into the template above.

**Verify each link in incognito before using in Kit**: paste the full `/uc?export=download&id=[FILE_ID]` URL into an incognito browser window. It must trigger an immediate PDF download. If it shows a "Request access" error, the file sharing is not set to "Anyone with the link."

---

### 3-Test Protocol — Run After Automation is Published

**Test 1**: Sign up via landing page with `wanka95+test1@gmail.com`, select Zone 5. Verify Email 1 arrives within 60 seconds and Zone 5 PDF downloads.

**Test 2**: Sign up again with `wanka95+test2@gmail.com`, select Zone 8. Verify Email 1 arrives with Zone 8 card.

**Test 3**: Wait 1 minute after Test 2. Check `wanka95+test2@gmail.com`. Only Email 1 should be present. Email 2 must NOT have arrived (it is set to a 2-day delay). Presence of Email 2 means the delay logic is broken.

If Test 3 fails (Email 2 arrives within 1 minute): Kit > Automations > edit automation > check each email delay setting. Email 2 must show a `2 days` delay, not `0` or `immediately`.

**After tests pass**: Switch automation status from Draft to Published (if Kit requires a draft > publish step; some plans auto-publish). Confirm status shows Published before closing.

---

## Gate 3 Decision Framework — Kit Creator Tier ($33/month)

**Current assumption**: Kit free tier is sufficient for launch. Do not pay on May 27.

**The one free-tier limitation that could affect Gate 3**: Kit's free tier may limit the number of automation sequences or the complexity of conditional logic. If Kit blocks building 8 Email 1 variants behind conditional rules (zone-tag-based routing), the free tier may not support this.

**Check this during account creation** (before building anything else):
- Kit > Automations > create a new automation
- Can you add a conditional step ("If subscriber has tag zone-5, then send email X")?
- If YES: free tier supports conditional routing. Proceed with Option A (8 variants).
- If NO (feature locked behind paid tier): use Option B (single Email 1 with `{{ subscriber.zone }}` liquid tag for zone number, and a single Google Drive folder link that routes subscribers to a zone-selector page).

**Option B fallback landing page for zone card delivery** (if conditional automation is locked):
Instead of 8 Email 1 variants, deliver a single Email 1 that links to a landing page or Google Form where the subscriber selects their zone and gets the correct card link displayed. This adds one friction step but requires zero Kit conditional logic. Build this only if conditional automation is confirmed locked on the free tier.

**Creator tier ($33/month) is justified if**:
- Conditional automation is locked on free tier AND zone routing is impossible without it
- More than 1 landing page is needed before launch (it is not — 1 is sufficient)

**Creator tier is NOT justified if**:
- Conditional automation works on free tier (likely — Kit's free tier includes basic automation)
- You can complete Option A with 8 Email 1 variants

**Decision trigger**: Check during Phase A (account creation). If conditional automation works, continue on free tier. If locked, evaluate Creator tier or use Option B fallback. Document the outcome in WORKLOG.md.

---

## Kit Session Checklist — Execute in This Order

Copy this into a scratch note before your Kit session. Check each item as you complete it.

**Phase A — Account and Tags (15–20 min)**
- [ ] Create Kit account at kit.co with wanka95@gmail.com
- [ ] Set sender name: Seedwarden
- [ ] Set sender email: wanka95@gmail.com
- [ ] Set time zone: your local time zone
- [ ] Verify email (click confirmation link in Gmail)
- [ ] Test: can you create an automation with conditional logic? (note result: YES / NO)
- [ ] Create all 8 zone tags (zone-3 through zone-10)
- [ ] Create all 7 cohort tags (seed-saver, forager, food-preserver, homesteader, medicinal-herbs, vip-buyer, phase-1-buyer)
- [ ] Verify: 15 tags total visible in Subscribers > Tags

**Phase B — Landing Page (25–30 min)**
- [ ] Kit > Landing Pages > Create > select minimal template
- [ ] Paste headline, subheadline, trust text from this document
- [ ] Add form fields: First Name (required), Email (required), Growing Zone (dropdown, Zones 3–10, required)
- [ ] Set CTA button text: "Send My Zone Card"
- [ ] Publish the landing page
- [ ] Copy the landing page URL and paste it here: ___________________________
- [ ] Test in incognito: page loads, form submits without errors
- [ ] Connect the landing page form to the welcome automation (do after automation is built in Phase C/D)

**Phase C — Email Sequence (60–90 min)**
- [ ] Open TRACK_B_EMAIL_SEQUENCES.md in a second window
- [ ] Create automation: Kit > Automations > New Automation > name it "Seedwarden Welcome"
- [ ] Set trigger: "When subscriber joins via landing page"
- [ ] Build Email 1 Zone 5 variant first (use Email 1 copy from TRACK_B_EMAIL_SEQUENCES.md)
- [ ] Add Zone 5 Google Drive card link (format: /uc?export=download&id=[FILE_ID])
- [ ] Test Email 1 Zone 5 in isolation before building other variants
- [ ] Build remaining 7 Email 1 zone variants (Zone 6, 3, 4, 7, 8, 9, 10 in order)
- [ ] Add conditional routing: if tag = zone-5, send Email 1 Zone 5 variant; repeat for all 8
- [ ] Build Email 2 (paste body from TRACK_B_EMAIL_SEQUENCES.md; set delay: 2 days)
- [ ] Build Email 3 (paste body; set delay: 3 days)
- [ ] Build Email 4 (paste body; set delay: 2 days)
- [ ] Build Email 5 (paste body; set delay: 3 days; FIX stale date reference before saving)
- [ ] Set automation status to Published

**Phase D — Zone Routing (20–30 min)**
- [ ] Verify conditional routing rules are attached to each Email 1 variant
- [ ] Verify delays are set correctly for Emails 2–5 (2, 3, 2, 3 days)
- [ ] Verify trigger is "Joins via landing page" (not manual)
- [ ] Link the landing page form to this automation

**Phase E — 3-Test Protocol (20 min)**
- [ ] Test 1: wanka95+test1@gmail.com, Zone 5 — verify Email 1 arrives < 60 seconds, Zone 5 PDF downloads
- [ ] Test 2: wanka95+test2@gmail.com, Zone 8 — verify Email 1 arrives with Zone 8 card
- [ ] Test 3: wait 1 minute — verify ONLY Email 1 arrived for test2 (Email 2 must NOT be present)
- [ ] All 3 tests PASS — record in WORKLOG.md

**Phase F — Post-Session (2 min)**
- [ ] Record Kit landing page URL in WORKLOG.md under "Kit Zone Card File URLs" section
- [ ] Add landing page URL to Instagram bio link
- [ ] Add landing page URL to TikTok bio link
- [ ] Add landing page URL to Pinterest website field
- [ ] Record Kit account creation date in WORKLOG.md (DNS propagation starts here)

---

## Post-Gate 3 Social Bio Update

After Gate 3 is complete and the Kit landing page URL is confirmed working:

**Instagram**: Edit Profile > Bio link > paste Kit landing page URL
**TikTok**: Edit Profile > Website > paste Kit landing page URL
**Pinterest**: Settings > Public Profile > Website > paste Kit landing page URL

The Zone Quick-Start Card lead magnet only activates when subscribers can find the landing page. Adding the URL to all 3 bios immediately after Gate 3 is a required step, not optional. Include this in your Gate 3 completion confirmation.

---

*Created: 2026-05-19. All decisions in this document are drawn from KIT_SETUP_NOTES.md,
TRACK_B_EMAIL_AUTOMATION_KIT_GUIDE.md, TRACK_B_EMAIL_SEQUENCES.md, and TRACK_B_USER_GATES.md.
This brief removes all decision overhead from the Gate 3 Kit session — the session should be
pure UI execution. Session expected: May 27, 2026.*
