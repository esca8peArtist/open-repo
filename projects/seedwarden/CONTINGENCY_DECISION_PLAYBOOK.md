---
title: "Contingency Decision Playbook — Track B May 30 Launch"
date: 2026-05-27
version: 1.0
session: 1691
status: production-ready
purpose: >
  Decision trees for every realistic failure mode in the May 30 launch window.
  Six primary scenarios plus an escalation protocol for simultaneous failures.
  Executable in under 15 minutes per scenario without requiring a Claude session.
references:
  - TRACK_B_LAUNCH_DAY_RUNBOOK.md (launch window execution order)
  - CONTINGENCY_DECISION_THRESHOLDS.md (Day 3/7/14 numerical thresholds)
  - TRACK_B_LAUNCH_MONITORING_CHECKPOINTS.md (checkpoint decision trees)
  - INFLUENCER_STAGING_VERIFICATION.md (contact list + response tracking)
  - TRACK_B_LAUNCH_DAY_CHECKLIST.md (escalation triggers 1–4)
  - KIT_SETUP_NOTES.md (Kit automation configuration reference)
---

# Contingency Decision Playbook
## Track B — May 30, 2026 Launch

**How to use this document**: When a monitoring check shows a problem, find the matching scenario number below. Read the trigger first to confirm it matches what you're seeing. Then follow the decision tree steps in order. Each tree completes in 15 minutes or less.

**If two or more scenarios trigger simultaneously**: Jump to the Escalation Protocol at the bottom of this document before executing any individual scenario.

---

## Scenario 1: Email Delivery Failure

**Trigger conditions** (check at 08:30–09:00 UTC first monitoring pass):
- Kit broadcast open rate below 3% after 30+ minutes (most email platforms show open data within 15–20 minutes of send)
- Bounce rate above 5% visible in Kit analytics
- You sent the launch-day email to influencers and received a bounce notification within 5 minutes

**When to invoke**: Any of the three conditions above during the 08:30–09:00 UTC check.

---

### Decision Tree

**Step A: Check Kit automation logs (2 minutes)**

Log into Kit. Navigate to Automations > your zone card delivery automation. Check:
- Is the automation status "Published" or "Paused"?
- Are there any error flags on recent subscriber events?
- Look at the last 5 subscriber records: did they receive Email 1 (zone card delivery email)?

**If automation status is Paused**: Click "Resume." This is the most common cause of delivery failure after initial setup. The automation may have auto-paused if Kit detected unusual activity or if the account hit a free-tier sending limit. Resuming it fixes delivery for new subscribers immediately.

**If automation status is Published and no errors**: The automation itself is working. The issue is specific to the broadcast email. Go to Step B.

---

**Step B: Assess bounce type (3 minutes)**

In Kit, navigate to Broadcasts > the specific launch-day broadcast > Delivery report. Look at the bounce breakdown:
- "Hard bounce" (invalid address): These addresses are permanently undeliverable. Remove them from the list. A hard bounce rate above 5% means your list has significant invalid addresses — this is fixable.
- "Soft bounce" (temporary delivery failure): These are usually a spam filter holding the message or a recipient's inbox being full. Wait 2 hours — soft bounces often resolve with a retry.
- "Blocked" (your domain is on a blocklist): This is the most serious case. Go to Step C immediately.

**If hard bounce rate is 2–5%**: This is within normal range for cold outreach lists. Remove the bounced addresses, note the count, and proceed. No action needed beyond cleanup.

**If soft bounce rate is above 10%**: Your sending domain may not have completed SPF/DKIM warmup. Check `GATE_3_AUTOMATION_KIT.md` — was the DNS CNAME submitted by May 28 17:00 UTC? If not, deliverability to strict spam filters will be impaired. The workaround is Step D.

---

**Step C: If Kit platform failure or domain blocked (5 minutes)**

If Kit shows an error indicating the platform itself is down:
1. Check Kit's status page: status.kit.com
2. If Kit is down: do not wait. Send the influencer launch notification emails directly from Gmail (copy the email body from `HERBALIST_PARTNERSHIP_EMAIL_TEMPLATE.md`). These are the 5 highest-priority contacts: Sabrena Gwin, Susan Leopold, John Gallagher, Juliet Blankespoor, Herbal Academy.
3. For zone card delivery to subscribers: temporarily attach the relevant zone card PDF as a Gmail attachment. The zone card PDFs are at `projects/seedwarden/assets/zone-cards/`. Send manually to any subscriber who emails asking where their card is.
4. Document the Kit outage time in the tracking log. File a support ticket with Kit (support@kit.com) with a description of the issue.

If your sending domain is blocked:
1. In Kit, switch the "From" email address to your Gmail address (wanka95@gmail.com) as a temporary sender. This bypasses domain reputation issues.
2. Resend to the bounce-free segment only.
3. Note: this is a short-term fix. Full domain reputation recovery takes 1–2 weeks. Document for Day 7 review.

---

**Step D: Manual resend to bounce-free segment (3 minutes)**

For influencer direct emails (not Kit automation):
1. Export the list of email addresses that did NOT bounce from Kit.
2. Send the launch notification email directly from Gmail in BCC batches of no more than 50 addresses per send (Gmail daily limit for individual sends is higher, but batches reduce spam flag risk).
3. Subject line: "Zone guides are live — free download for your community"
4. Use the email body from TRACK_B_LAUNCH_DAY_RUNBOOK.md Phase 2 Step 2.

---

**Success criteria**: Recover effective delivery to 70%+ of the intended list within 2 hours of identifying the failure. "Effective delivery" means the email was sent without a hard bounce — open rate is a secondary metric.

**Document for Day 3 review**: Log exact bounce count, bounce type, and action taken. Include in the June 2 checkpoint review.

---

## Scenario 2: Social Media Post Limited Reach

**Trigger conditions** (check at 12:00 UTC pulse check):
- Instagram launch post shows fewer than 50 likes, comments, or saves after 4 hours
- TikTok launch video shows fewer than 100 views after 4 hours
- Any post flagged by the platform (you received a notification, or the post does not appear on your own profile)

**When to invoke**: Engagement stalling at the 12:00 UTC check (4 hours post-launch).

---

### Decision Tree

**Step A: Check post format and hashtag compliance (2 minutes)**

On Instagram, go to the launch post and check:
- Are there exactly 5–10 hashtags? (Instagram suppresses posts with 30 hashtag stuffing)
- Does the post caption include any links? (Instagram suppresses posts with external links in captions — links belong in bio only)
- Is the account flagged for any policy violation? (Check "Account Status" in Instagram Settings)

On TikTok, check:
- Did you upload the video natively (not as a link or cross-post)? TikTok's algorithm heavily penalizes cross-posted content.
- Does the video have a sound/music track? Videos without audio are deprioritized.

**If format issue found**: Edit the post (remove excess hashtags, remove links from caption) and note the time of edit. Algorithm suppression from these issues typically lifts within 6–12 hours of correction.

**If no format issue**: Proceed to Step B.

---

**Step B: Assess whether the issue is low engagement vs. low reach (2 minutes)**

Check Instagram Insights for the launch post:
- "Reach" = number of unique accounts who saw the post
- "Impressions" = total times the post was displayed

If reach is low (below 50) but the post has not been flagged, this is a new-account problem, not a content problem. Instagram limits organic reach on accounts with fewer than 50 posts. This is expected and normal for a launch day on a new account. Proceed to Step C.

If reach is above 50 but engagement (likes/comments) is below 10%, the content format may not be resonating. Note this for Day 7 review.

---

**Step C: Instagram Story boost (3 minutes)**

Post an Instagram Story immediately after confirming the engagement is stalling. This signals account activity to the algorithm and drives secondary traffic.

Story format:
- Upload one zone card image (Zone 5 or Zone 7 is most requested — use the card image from the Canva file)
- Add a link sticker pointing to the Gist URL
- Caption overlay: "Zone cards are live. Free for every zone. Link here."
- Post the Story now.

This is the most reliable immediate action for boosting a stalling Instagram post on a new account.

---

**Step D: If engagement remains below 50 total interactions by 16:00 UTC (4 hours after Step C)**

Decision: Boost with paid promotion.
- Budget: $5 per day, per channel (Instagram and/or TikTok), starting immediately.
- Target audience: interests = gardening, herbalism, homesteading, sustainable living. Age 25–55. US only.
- Duration: 3 days ($15 total per platform).
- On Instagram: Go to the launch post > Boost Post > Use the targeting above.
- On TikTok: Go to the video > Promote > use the same targeting.

This is a direct response to algorithm suppression of new accounts. Day 1 paid spend is a diagnostic tool — if boosted reach converts to Gist clicks, the content is working and the only issue was distribution. If boosted reach does not convert, the content framing needs to be adjusted for Day 7.

**If algorithm suppressed (post does not appear on your own feed)**: Do not delete and repost. This typically makes suppression permanent. Instead, post a new organic Story as in Step C, and post one new organic post (a different zone card image) to signal continued account activity. Contact Instagram support via the Help Center if suppression persists beyond 48 hours.

**Repost window option (16:00 UTC)**: If the original launch post accumulated fewer than 10 total interactions by 16:00 UTC and was not boosted, post a fresh version at 16:00–18:00 UTC — the optimal engagement window for Instagram per the platform posting time research in `TRACK_B_SOCIAL_CALENDAR_MAY28_30.md`. Use different caption copy from the June 1–7 ramp-up calendar in that document.

---

**Success criteria**: Cumulative Instagram engagement (likes + comments + saves + Story link clicks) above 200 by 20:00 UTC end of day. TikTok views above 300 by end of day.

**Document for Day 7 review**: Engagement number at 4 hours, 8 hours, and end of day. Whether any paid promotion was activated and the cost.

---

## Scenario 3: Low Initial Website / Gist Traffic

**Trigger conditions** (check at 12:00 UTC):
- Gist view count below 10 by 12:00 UTC (4 hours post-launch)
- Bitly link click count below 10 by 12:00 UTC (if Bitly was set up)
- Kit landing page receives 0 new subscribers 2 hours after launch

**When to invoke**: 12:00 UTC check shows below-threshold traffic.

---

### Decision Tree

**Step A: Verify UTM tracking is firing (2 minutes)**

Check whether the Gist URL in your social posts is the correct URL (not a placeholder). Open each live post and confirm:
- Instagram bio link-in-bio: does it resolve to the Gist (or Kit landing page)?
- Reddit r/herbalism post: is the Gist URL in the post body, not just the title?
- TikTok: is the bio link updated to the Gist URL?

**If any bio link is wrong or shows a placeholder**: Fix it immediately. This is the most common cause of zero Gist traffic — the posts went out but no link was clickable. Update bios, edit Reddit post body, and log the correction time.

**If all links are correct**: Proceed to Step B.

---

**Step B: Check influencer email open rate (2 minutes)**

In Kit Broadcasts, check open rate on any launch-day broadcast that was sent. In your Gmail sent folder, check whether the influencer notification emails have received any replies.

If open rate is below 10% on a broadcast sent to a warm list: it's possible the emails landed in spam. See Scenario 1 for email delivery remediation.

If influencer open rate is 0% (no opens): the influencer emails may not have been sent (check email sent folder) or may have bounced. Send them now if not yet sent.

**If influencers have not yet sent their launch posts to their communities**: This is expected on launch morning. Influencer amplification typically lags 24–48 hours. Low Gist traffic on Day 0 morning is expected. The first meaningful Gist traffic surge usually comes from influencer newsletter sends and social posts, which happen within 48 hours of receiving the launch notification.

---

**Step C: If traffic is genuinely low (not a tracking error) by 16:00 UTC**

4 actions in priority order — execute all four, they each take 5 minutes:

1. **Post an Instagram Story** with a direct link sticker to the Gist. This is the fastest single action to drive incremental traffic from your existing Instagram followers.

2. **Follow up with any Reddit moderator who approved your post but has not yet approved a pinned or featured post**: Send a second Reddit modmail to r/herbalism noting that the launch post is live and asking if they would consider adding a community post tag. This is a minor ask — most mods will either ignore it or apply the tag, improving post visibility.

3. **Send the launch notification DMs to any of the 15 influencer contacts not yet reached**. Re-check the DM sent log from Phase 2 — if any contacts were missed, send now.

4. **Post the launch content to one additional Reddit community not yet reached**. Good options if not already posted: r/foraging (750K+ members), r/homesteading (not yet reached in May 28–30 pre-launch). Use the personal framing variant: "I built a free zone guide for my zone, thought this community might find it useful" + Gist link.

---

**Step D: If Gist remains below 25 views by 20:00 UTC end of day**

This is low but not alarming for Day 0 without influencer amplification. The Day 3 threshold (June 2) is the first meaningful decision point. Take no drastic action on Day 0 based on low traffic alone.

Document the Day 0 Gist view count and carry it to the June 2 Day 3 checkpoint.

**Do not**: activate paid promotion on Day 0. Gist traffic is notoriously difficult to attribute to paid spend. The correct Day 0 response to low traffic is organic amplification (Stories, Reddit, DMs), not paid ads.

---

**Success criteria**: Above 150 Gist views by end of day (20:00 UTC) indicates healthy Day 0 acquisition from organic + influencer channels. Above 50 by end of day is acceptable for a launch with no prior audience. Below 20 by end of day: escalate outreach immediately on May 31.

---

## Scenario 4: Influencer Underperformance

**Trigger conditions** (check at 10:00 UTC):
- Fewer than 3 of 15 influencer contacts have confirmed they'll share (any confirmation: reply, DM, social post, or newsletter mention) by 10:00 UTC
- Fewer than 50% of influencer outreach emails have been confirmed as sent (check email sent folder)

**When to invoke**: 10:00 UTC check shows fewer than 3 confirmed sends.

---

### Decision Tree

**Step A: Confirm all outreach was actually sent (2 minutes)**

Check the email sent folder and DM sent logs:
- Were May 28 Tier 1 emails sent to Sabrena Gwin, Susan Leopold, John Gallagher, Reddit mods?
- Were May 28–29 Tier 2 emails sent to Juliet Blankespoor, Herbal Academy, Discord admins?
- Were launch-day DMs sent to all 15 contacts during Phase 2 Step 6?

**If any batch was not sent**: Send it immediately. This is the highest-priority action. Unsent outreach is the most common cause of influencer underperformance. Do not mark this scenario as failed until all outreach has been sent and 24 hours have passed.

**If all outreach was sent**: Proceed to Step B.

---

**Step B: Send follow-up DM to non-responders (5 minutes)**

For all contacts who received outreach but have not responded, send a short follow-up:

```
Hi [NAME] — just following up on the zone guides I shared. They went live this morning:
[GIST_URL]

If it would help, I can put together a short blurb you could paste into a message to your community. Happy to make it easy.
```

Keep follow-ups to one per contact. Do not send more than one follow-up during the launch window.

Send to:
- All Tier 1 contacts with no response (Sabrena Gwin, Susan Leopold, John Gallagher are highest priority)
- Any Discord or Reddit contacts whose modmail has not received a reply

---

**Step C: By 12:00 UTC, fewer than 3 confirmations received**

This is within normal range. Most herbalist influencer networks send to their communities within 24–72 hours of receiving a resource, not within the same morning. The 10:00 UTC check is an early signal, not a hard failure threshold.

Continue monitoring. The Day 3 checkpoint (June 2) with a target of 10+ of 15 confirmed sends is the real threshold.

**Document**: Track which contacts responded, when, and what type of response (reply only, confirmed sharing, shared publicly). Fill in the response tracking log in `TRACK_B_HERBALIST_OUTREACH_MATRIX.md`.

---

**Step D: By 12:00 UTC, fewer than 2 of 15 confirmed sends AND you can confirm all outreach was sent**

This is the underperformance trigger. Take two actions:

1. **Pivot to direct send link**: Email the 5 highest-priority contacts (Sabrena Gwin, Susan Leopold, John Gallagher, Juliet Blankespoor, Herbal Academy) with a direct PDF attachment of Zone 5 or the zone most relevant to their geography. Subject: "Zone [X] card — preview for sharing." This removes the friction of clicking a link and gives them a tangible asset to forward.

2. **Begin organic amplification to compensate**: Post Zone-specific content to the two Reddit communities not yet reached (r/foraging, r/homesteading). This is a direct substitute for influencer reach. Each Reddit post reaching 10+ upvotes is roughly equivalent to one influencer DM response.

---

**If send confirmation count remains below 5 of 15 by end of May 31**:

Mark as low-trust for Phase 3 vendor scoring (per the task brief). Influencer channel is underperforming. This should factor into the June 6 Day 7 decision gate: if the influencer channel produced fewer than 3 confirmed sends and fewer than 2 organic shares, de-prioritize it for Phase 3 investment in favor of Reddit and Pinterest organic.

---

**Success criteria**: Above 10 of 15 confirmed sends by 12:00 UTC on June 2 (Day 3). "Confirmed send" means the contact replied, shared publicly, or sent a confirmation message. It does not require a public share — a reply saying "I'll include it in my next newsletter" counts.

---

## Scenario 5: Etsy Visibility Suppressed

**Trigger conditions** (check in Etsy analytics, any time on May 30 or May 31):
- Etsy zone card listings show fewer than 200 impressions by end of Day 0
- Etsy search impressions are disproportionately low relative to any click-through traffic arriving from social/email
- One or more Etsy listings appear as "Hidden" or "Under Review" in your Etsy Shop Manager

**When to invoke**: Any of the above conditions visible in Etsy Analytics.

**Note**: Etsy analytics can have a 24–48 hour reporting lag on new listings. If the listing was uploaded within the past 48 hours, wait before treating low impressions as a confirmed issue.

---

### Decision Tree

**Step A: Verify all 8 zone card listings are live (2 minutes)**

Log in to Etsy Shop Manager. Navigate to Listings. Confirm all 8 zone card listings show status "Active" (not "Draft," "Hidden," "Under Review," or "Expired"). If any listing shows a non-Active status, click through and follow the Etsy prompt to address the issue.

Common reasons for non-Active status:
- The listing was created as a draft and not published
- Etsy's automated review flagged the listing for a policy check (common on new digital downloads — typically resolves within 24 hours without any action)
- The listing's digital file is missing or corrupted (Etsy requires the actual PDF to be attached, not just a description)

**If any listing is in "Under Review"**: Do not edit the listing. Editing a listing under review resets the review clock. Wait 24 hours and check again.

**If all listings are Active**: Proceed to Step B.

---

**Step B: Check tag compliance (3 minutes)**

In Etsy Shop Manager, open one listing and check the tags section. Etsy allows 13 tags per listing. Verify:
- Each tag is a phrase or word relevant to the product (zone gardening, herbalist guide, planting calendar, etc.)
- No tag is a brand name or trademark (Etsy may suppress listings with competitor brand names as tags)
- No tag repeats the exact title of the listing (Etsy's algorithm ignores exact-match tag/title duplication)
- All 13 tag slots are used (unused tag slots reduce search visibility)

The correct tag set for zone card listings is documented in `ETSY_PHASE_1_UPLOAD_CHECKLIST.md`. Cross-reference and update any listing with fewer than 13 tags or duplicate/irrelevant tags.

**Tag update time**: Make any tag corrections before Day 3 (June 2). Updated tags take 24–72 hours to be re-indexed in Etsy search.

---

**Step C: If live + compliant, but impressions remain below 200 by end of Day 1**

This is expected behavior for new Etsy sellers. Etsy's search algorithm has a "new seller sandbox" period lasting 1–4 weeks where new listings receive reduced impressions regardless of quality. This is a feature, not a bug — Etsy gradually increases visibility as the listing accumulates views, favorites, and sales.

Action: Do not make any changes to live, compliant listings during the sandbox period. Changes to active listings reset the indexing clock.

**Target metric**: 5%+ impression-to-view ratio by Day 7. This means: if the listing has 200 impressions (times it appeared in search), at least 10 clicks should have occurred. Below 5% suggests the listing thumbnail or title is not compelling enough — addressable by Day 14.

---

**Step D: Cross-traffic check**

If social and email traffic is flowing (Gist views are accumulating) but Etsy impressions are near zero, the two channels are operating independently — which is normal on Day 0. Track B's primary Day 0 channel is the Gist (free download), not Etsy (paid product). Etsy visibility builds over Days 7–30 as the listing accumulates engagement signals.

**Document for weekly monitoring**: Log Etsy impressions and click-through rate weekly (every Monday) in the tracking log template in `CONTINGENCY_DECISION_THRESHOLDS.md`.

---

**Success criteria**: Etsy algorithm learns over Days 1–7. Target 5%+ impression-to-view ratio by Day 7 (June 6). If below 5% by Day 7, update thumbnails and first listing image. Etsy sales are a secondary metric for Track B at this stage — the primary conversion path is Gist downloads > Kit email capture > future paid bundle.

---

## Scenario 6: Customer Support Volume Overwhelming

**Trigger conditions** (any time on launch day):
- More than 20 inquiries, DMs, or messages arrive in the first 4 hours
- Multiple contacts are asking the same question (sign of a FAQ gap)
- Any message requires an urgent response (negative experience, complaint, technical failure)

**When to invoke**: This is a positive problem — high inquiry volume means the launch is working. The issue is managing response quality under volume.

---

### Decision Tree

**Step A: Triage inquiries by category (5 minutes)**

Read through all messages quickly. Do not respond to any yet. Categorize each into one of four types:

| Type | Description | Priority |
|------|-------------|----------|
| Technical issue | "Link doesn't work," "PDF won't open," "Wrong zone card sent" | Urgent — respond within 30 minutes |
| Product question | "Which zone am I in?", "Can I get Zone 4?", "Is this free?" | High — respond within 2 hours |
| Appreciation / general | "This is so helpful," "Thank you," etc. | Standard — respond within 4 hours |
| Partnership / collaboration | "I'd love to share this," "Can we work together?" | High — respond within 2 hours |

---

**Step B: Create FAQ response templates (5 minutes)**

From the most common questions in Step A, create a set of short, copy-paste templates. Common launch-day questions for Seedwarden based on the product:

**"Which zone am I in?"**
```
Good question! You can find your USDA zone at planthardiness.ars.usda.gov — just type in your zip code (takes 10 seconds). Then grab your zone card here: [GIST_URL]
```

**"Is this really free?"**
```
Yes — all 8 zone cards are free, no email required. Direct download here: [GIST_URL]
```

**"PDF won't open"**
```
Sorry about that! Try opening it on a desktop browser — a few mobile browsers have PDF compatibility issues. If that doesn't work, reply and I'll email you the specific zone directly.
```

**"Can I share this with my community?"**
```
Absolutely — please do. The direct link for sharing: [GIST_URL]. If you'd like a short blurb to include, happy to write one for your audience specifically.
```

**"I want to collaborate / affiliate"**
```
That sounds great. I'll follow up with more details — can you share your community size and platform briefly? Happy to set up an arrangement.
```

---

**Step C: Respond to all inquiries using templates (10 minutes per batch of 10)**

Work through inquiries in priority order (Technical > Partnership > Product Question > Appreciation). Use templates from Step B, personalizing with the contact's name and specific zone where relevant.

**30-minute SLA target**: All technical issues and partnership inquiries responded to within 30 minutes of receipt. Product questions and appreciation messages within 2 hours.

---

**Step D: If volume exceeds 50 messages before 12:00 UTC**

This would be an exceptional outcome (50+ messages in 4 hours indicates major viral traction from an influencer share or Reddit thread). If this happens:

1. Post one Instagram Story: "I'm getting a lot of messages — thank you! I'll reply to everyone within the hour. Zone cards are here: [GIST_URL]." This manages expectations and re-directs new inquiries to the resource.
2. Continue responding in batches of 10–15 using templates.
3. Flag any partnership inquiries for a separate follow-up after launch day (respond within 24 hours, not same-hour).

---

**Success criteria**: All customers responded to within 2 hours. No message goes unread and unreplied past the 20:00 UTC end-of-day wrap-up. All inquiry themes documented in the Day 0 qualitative notes section of the tracking log.

---

## Scenario 7: Distribution Infrastructure Failure

**Trigger conditions** (any time during pre-launch or launch window):
- Gist URL returns 404 or GitHub is unreachable
- Kit automation is confirmed down (Kit status page shows an outage)
- Zone card PDFs are missing or corrupted

**This is the highest-severity scenario. Act immediately.**

---

### Decision Tree

**Step A: Activate backup URL (10 minutes)**

All 8 zone card PDFs are backed up at `projects/seedwarden/assets/zone-cards/` on your local machine. The backup distribution path is a Google Drive shared folder.

If the Gist URL is down:
1. Create a Google Drive folder: New Folder > name it "Seedwarden Zone Cards"
2. Upload all 8 PDFs from `projects/seedwarden/assets/zone-cards/`
3. Right-click the folder > Share > "Anyone with the link" > Viewer access > Copy link
4. This becomes the backup URL. Replace all references to the Gist URL with this new URL.

**Total time**: 8–10 minutes if PDFs are locally accessible.

**After creating backup URL**:
- Update Instagram bio link-in-bio immediately
- Edit the Reddit post body (add "Edit: Updated link — [new URL]" to post body)
- Post one Instagram Story: "Link updated — grab it in bio" with link sticker pointing to new URL
- Update any remaining unposted social content
- Proceed with the launch — do not delay

**If Gist comes back up**: Keep both URLs live. The backup URL can serve as a redundant access point.

---

**Step B: If PDFs are corrupted or missing**

Check the local file sizes. All 8 PDFs should be 630–650 KB each. Any file under 100 KB is corrupted.

If corrupted: Run `uv run python scripts/generate_zone_cards.py` from the repo root to regenerate. Takes approximately 5 minutes. Regeneration procedure is documented in `ZONE_PDF_VERIFICATION_REPORT.md`.

If the generator fails: The source Canva files are the authoritative backup. Export each zone card from Canva as a PDF (high quality, PDF standard) and re-upload to the backup distribution URL.

---

**Success criteria**: Backup URL live and PDFs accessible within 15 minutes of detecting the Gist failure. All social bios and posts updated within 20 minutes.

---

## Escalation Protocol
### Use if More Than 2 Scenarios Trigger Simultaneously

**Trigger**: Two or more of Scenarios 1–7 are active at the same time.

**Immediate action (before executing any individual scenario)**: Pause all new initiatives. Do not start new posts, new DM batches, or any new distribution actions until the critical issues are resolved. Attempting to add channels under a simultaneous failure situation spreads attention and worsens outcomes.

---

**Prioritization framework**:

| Priority | Scenario | Reason |
|----------|---------|--------|
| 1 (resolve first) | Scenario 7 — Infrastructure failure | No distribution = no launch. Everything else is downstream of this. |
| 2 | Scenario 1 — Email delivery failure | Email is the highest-ROI channel for confirmed influencer activation. |
| 3 | Scenario 4 — Influencer underperformance | Influencer reach is the primary amplification mechanism. |
| 4 | Scenario 3 — Low traffic | Often resolves as Scenarios 1 and 4 are fixed. |
| 5 | Scenario 2 — Low social engagement | A secondary signal on Day 0; Day 7 is the real social threshold. |
| 6 | Scenario 5 — Etsy suppressed | Etsy is not the primary Day 0 channel. Do not prioritize over other failures. |
| 7 | Scenario 6 — High support volume | A positive problem. Address after infrastructure and distribution are stable. |

Work through priorities 1, 2, and 3 sequentially before returning to lower-priority scenarios.

---

**Communication protocol**:

If automated systems require intervention from external parties (Kit support, Etsy flagged a listing, GitHub Gist taken down by GitHub Trust and Safety):

- **Kit support**: support@kit.com. Include: account email (wanka95@gmail.com), description of the issue, your Kit account URL. Response time: typically 2–4 hours on weekdays.
- **Etsy support**: etsy.com/help (chat option available for active accounts). For a listing under review, do not contact support until 48 hours have passed — Etsy's automated review resolves most cases without intervention.
- **GitHub Gist**: If a Gist is taken down by GitHub Trust and Safety (rare and requires a policy violation), activate the backup URL (Step A, Scenario 7) immediately and do not attempt to recreate the Gist until you understand the reason for removal.

Document all escalation contacts, ticket numbers, and timestamps in the tracking log. Include in the Day 3 (June 2) review.

---

**If 4 or more scenarios trigger simultaneously**:

This is an infrastructure-level failure, not a content or distribution failure. Stop launch window activities. Fix the infrastructure (Scenario 7 first), then re-sequence the launch starting with Phase 2 Step 1 (Reddit post) as if it were now. A 1–2 hour delay on launch day does not materially affect Day 3 or Day 7 outcomes.

---

*Document version: 1.0 — May 27, 2026, Session 1691*
*Companion documents: TRACK_B_LAUNCH_DAY_RUNBOOK.md (launch sequence), DAY_3_AND_7_DECISION_GATES.md (post-launch decision framework), CONTINGENCY_DECISION_THRESHOLDS.md (numerical thresholds and weekly monitoring template)*
