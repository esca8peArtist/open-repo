---
title: "Contingency Trigger Decision Tree — Track B Post-Launch June 4–18"
created: 2026-06-04
status: production-ready
purpose: >
  8-scenario decision tree with numeric thresholds, GO/CAUTION/NO-GO branches,
  and immediate-action runbooks for each failure mode in the June 4–18 tracking
  window. Executable without a Claude session in under 15 minutes per scenario.
references:
  - TRACK_B_MONITORING_AUTOMATION_FRAMEWORK.md (metric collection procedures)
  - POST_LAUNCH_ANALYSIS_TEMPLATE.md (metric log)
  - CONTINGENCY_DECISION_PLAYBOOK.md (predecessor — May 30 launch scenarios)
  - TRACK_B_HERBALIST_OUTREACH_MATRIX.md (influencer response log)
  - KIT_SETUP_NOTES.md (Kit automation reference)
---

# Contingency Trigger Decision Tree
## Track B — June 4, 2026 Launch | 8 Named Scenarios

**How to use**: When a Day 3, 7, or 14 checkpoint shows a problem, find the matching scenario by name. Confirm the trigger conditions match. Follow the decision tree steps in order. Each tree completes in 15 minutes or less.

**If two or more scenarios trigger simultaneously**: Jump to Scenario 8 (Multi-Failure Escalation Protocol) before executing any individual scenario.

---

## Threshold Master Table

All thresholds consolidated. See per-scenario trees below for the response to each range.

| Metric | Day 3 (June 7) | Day 7 (June 11) | Day 14 (June 18) |
|--------|---------------|----------------|-----------------|
| Email open rate | GO: ≥20% / CAUTION: 10–19% / NO-GO: <10% | — | GO: ≥20% / NO-GO: <20% cumulative |
| Email unsubscribe rate | CAUTION: 2–5% / NO-GO: >5% | NO-GO: >5% cumulative | NO-GO: >5% total |
| Gist views (cumulative) | GO: >70 / CAUTION: 30–70 / NO-GO: <30 | GO: >200 / CAUTION: 100–200 / NO-GO: <50 | GO: >400 / CAUTION: 150–400 / NO-GO: <150 |
| Influencer public shares | GO: ≥1 / CAUTION: 0 shares, responses rcvd / NO-GO: 0 responses from all 15 | GO: ≥3 / CAUTION: 1–2 / NO-GO: 0 | NO-GO: 0 (if email channel also failed) |
| Sales / orders | GO: ≥1 / CAUTION: views but 0 sales | GO: ≥1 / NO-GO: 0 AND listing not live | GO: ≥3 / CAUTION: 1–2 / NO-GO: 0 |
| Twitter/Instagram mentions | — | NO-GO: 0 mentions if 7+ days of posting | — |
| Kit new subscribers | GO: ≥5 / CAUTION: 1–4 / NO-GO: 0 | GO: ≥15 / CAUTION: 5–14 / NO-GO: <5 | GO: ≥30 / CAUTION: 10–29 / NO-GO: <10 |

---

## Scenario 1: Low Email Open Rate

**Trigger condition**: Campaign Monitor open rate below 20% on the June 4 launch broadcast.
- CAUTION range: 10–19% (investigate but do not halt)
- NO-GO trigger: below 10%

---

**Step A: Verify the broadcast was actually sent (1 minute)**

Log in to Campaign Monitor > Campaigns. Find the launch broadcast. Check status: Sent / Draft / Scheduled.

- If status is "Draft" or "Scheduled": it was not sent. Send immediately. This is the most common cause of unexpectedly low open data.
- If status is "Sent" with a delivery timestamp on June 4: proceed to Step B.

---

**Step B: Check deliverability signals (3 minutes)**

In Campaign Monitor, click the campaign > View Report. Look at:
- Bounce rate: if > 5%, list quality issue (see Scenario 4)
- Spam complaints: if > 0.1%, content is being flagged
- Open rate by domain: if Gmail open rate is normal but "others" is near zero, a specific provider is blocking delivery

If bounce rate < 2% and spam complaints = 0 and open rate is still below 10%: your domain has a deliverability issue. Open Kit or Gmail and check whether a test email sent to your own address landed in spam.

---

**Step C: Check the subject line and preview text (2 minutes)**

A low open rate with good deliverability signals is almost always a subject line problem (email arrived, recipients chose not to open).

- Was the subject line personalized to the recipient's zone or region? Zone-specific subject lines outperform generic ones by 15–30% for botanical/herbalism audiences.
- Did the subject line contain spam trigger words (free, download, claim, limited time)? These reduce inbox placement.

**If subject line is the likely cause**: draft a new subject and send a re-engagement broadcast to non-openers. Campaign Monitor supports sending a follow-up to non-openers with a different subject line. Use it. Target: send re-engagement within 48 hours of the original broadcast.

---

**Step D: CAUTION response (open rate 10–19%)**

Continue monitoring. Send re-engagement broadcast with revised subject to non-openers (2-line subject line that references the zone card by number rather than by name). Log the original and revised subject lines and open rates in the POST_LAUNCH_ANALYSIS_TEMPLATE.md for A/B learning.

No other action required at Day 3.

---

**Step E: NO-GO response (open rate < 10%)**

1. Check spam folder of your own email address — did the launch broadcast arrive in spam?
2. If yes: SPF or DKIM record may be missing or incorrect. Log in to your domain registrar and verify the Campaign Monitor CNAME/TXT records are published. Allow 24–48h for DNS propagation after any fix.
3. Temporary workaround: send the launch email manually from Gmail (wanka95@gmail.com) to the Tier 1 influencer contacts (the 15 from TRACK_B_HERBALIST_OUTREACH_MATRIX.md). Gmail has high inbox placement for outbound personal email.
4. For the subscriber list: do not resend to the full list via Gmail. Wait for SPF/DKIM fix, then resend via Campaign Monitor to non-openers.
5. Log the incident in WORKLOG.md: date, open rate, diagnosis, resolution steps.

---

## Scenario 2: Low Gist View Count

**Trigger condition**: Gist views below threshold at any checkpoint.
- Day 3 NO-GO: < 30 views at 72h
- Day 7 NO-GO: < 50 views cumulative at 7 days
- Day 14 NO-GO: < 150 views cumulative

---

**Step A: Verify the Gist URL is accessible (1 minute)**

Open the Gist URL in an incognito/private browser window. Does it load? Is the full content visible?

- If "Page not found": the Gist was deleted or the URL was incorrect in all outreach. Recreate immediately. Check the URL in every social bio and replace.
- If it loads correctly: proceed to Step B.

---

**Step B: Audit URL placement across all channels (3 minutes)**

Check each of the following for the correct Gist URL:
1. Instagram bio link
2. Instagram posts and Stories (any link sticker or swipe-up)
3. Reddit post body (each post submitted)
4. Kit landing page CTA button
5. Launch email body (click the link in a sent email)
6. Twitter/X bio and any pinned tweet

If the URL is missing or broken in any of these: fix immediately. Each missing placement is a direct reduction in view count.

---

**Step C: Reddit post removal check (2 minutes)**

Navigate to your Reddit profile > submitted posts. Are your June 4 posts still visible?

- If posts are missing: they were removed by moderators. Do not repost the same content. Post in r/foraging (750K+ members) using an image post format (upload Zone 5 card as PNG). Image posts bypass most subreddit promotional filters.
- If posts are visible but have 0 upvotes: the post was likely shadow-filtered. Message the subreddit moderators with educational framing from HERBALIST_PARTNERSHIP_EMAIL_TEMPLATE.md Template E. Ask for explicit mod approval before your next post.

---

**Step D: CAUTION response (Day 3: 30–70 views)**

Expected range for a new account with no prior audience. Do not panic. Continue executing the social calendar as planned. The Day 7 checkpoint has more meaningful baseline data. One key action: cross-post to one new community not yet reached (r/homesteading if r/herbalism was primary, or r/foraging if neither was used).

---

**Step E: NO-GO response (Day 7: < 50 views despite correct URL placement and Reddit posts live)**

This means the content itself is not generating organic discovery. Test an alternate distribution format before Day 14:

1. Create a free Etsy listing for one zone card (Zone 5 or the most popular zone in your region). Etsy has organic search discovery that Gist lacks.
2. Pin a Pinterest image post linking to the Gist. Pinterest has long-tail botanical search traffic.
3. Do not invest further in the current Gist-only distribution strategy until one of these alternatives shows traction. Day 14 threshold remains at 150 views — the alternate channel can contribute to that total.

---

## Scenario 3: Zero Sales

**Trigger condition**: 0 orders/revenue at any checkpoint after launch.
- Day 3: Note but do not escalate (Day 3 revenue is not expected if no paid listing exists)
- Day 7 NO-GO: 0 sales AND Etsy listing is still Draft or not created
- Day 14 NO-GO: 0 sales AND Etsy listing has been Active for at least 5 days

---

**Step A: Check Etsy listing status (1 minute)**

Log in to etsy.com/your/shops > Listings. Is the Zone Card bundle listing:
- Active: visible to buyers and searchable
- Draft: saved but not published (invisible to buyers)
- Deactivated: was active, manually deactivated
- Not created: no listing exists

If the listing is Draft, Deactivated, or does not exist: publish immediately. A free Gist does not generate Etsy sales. The paid bundle listing must be Active.

---

**Step B: Check Etsy listing impressions vs views (2 minutes)**

In Etsy Shop Manager > Stats:
- Impressions: how many times the listing appeared in search results
- Views: how many times someone clicked to see the listing
- Orders: how many completed purchases

If impressions are low (< 50 at Day 7): SEO issue. The listing title and tags are not matching buyer search queries. Update the listing title to include "wild edibles guide," "zone quick-start," "USDA hardiness zone," and "native plants identification."

If impressions are high (> 200) but views are low (< 10): the listing thumbnail is not compelling enough to click. Update the primary photo to show the most visually appealing zone card spread.

If views are moderate (> 10) but orders are 0: pricing or trust issue. Ensure the listing has at least 3–5 photos, a complete description, and at least 1 review (if possible, ask a beta user to leave an honest review).

---

**Step C: NO-GO response at Day 14 (0 sales, listing Active for 5+ days)**

1. Lower price by $2 as a test (if currently at $7–9, test at $4.99).
2. Add a free download incentive in the listing description: "Download Zone 5 card free at [Gist URL] before buying — try before you buy."
3. Run a 10% off sale via Etsy's Sale & Discounts tool (no extra cost, creates an "On Sale" badge on the listing).
4. If still 0 sales after Day 14: the Etsy channel is not working for this product. Pivot to Kit-gated PDF (subscribe to download) as the primary monetization path. Etsy becomes secondary.

---

## Scenario 4: Influencer Silence

**Trigger condition**: 0 responses from all 15 influencer contacts after the specified time window.
- CAUTION: 0 responses at Day 3 (72h — outreach emails may not have been read yet)
- NO-GO: 0 responses from all 15 contacts at Day 7 (7 days after outreach)

---

**Step A: Verify outreach was sent (1 minute)**

Check your Gmail sent folder. Search for messages sent to the addresses in TRACK_B_HERBALIST_OUTREACH_MATRIX.md between June 1–4. Count how many were actually sent.

- If fewer than 15 emails were sent: send the remaining contacts immediately. This is the most common cause of influencer silence — the outreach was not fully executed at launch.
- If all 15 were sent: proceed to Step B.

---

**Step B: Check for email bounces (1 minute)**

In your Gmail sent folder, look for any bounce-back messages from the addresses you contacted. A bounced email address means the contact never received the outreach.

For any bounced contact: find an alternate contact method (Instagram DM, their website contact form, or Twitter/X DM). Re-send the outreach via the alternate channel with a one-line subject: "Re: zone card resource — bounced from [original email]."

---

**Step C: CAUTION response (Day 3, 72h, 0 responses)**

No action required at Day 3. Influencer email response time is typically 3–7 days. Continue monitoring. Send no follow-up before Day 5.

---

**Step D: Send one follow-up to the top 5 contacts (Day 7, if 0 responses)**

By Day 7 with 0 responses, one follow-up to the highest-priority contacts is appropriate. Send to the 5 contacts with the best audience fit (see TRACK_B_HERBALIST_OUTREACH_MATRIX.md Tier 1 column).

Follow-up email:

```
Subject: Quick follow-up — [X] downloads in week 1

Hi [NAME],

Following up on my note from last week about the Seedwarden Zone
Quick-Start Cards. The resource has gotten [X] views in the first
week and I wanted to share that in case it's useful context.

No pressure — if the timing isn't right or it's not a fit for your
audience, completely understood.

If you'd like a PDF preview of any specific zone card, happy to send
one directly.

Best,
[YOUR_NAME]
```

Fill in [X] with the actual Day 7 Gist view count. Real numbers are more persuasive than vague claims.

---

**Step E: NO-GO response (0 responses after follow-up, by Day 10)**

The influencer email channel is not working for this outreach batch. Pivot to direct platform engagement:

1. Comment thoughtfully on 3–5 recent posts from each of the top 5 influencer accounts on Instagram. Do not pitch — add value to their existing conversation. This builds recognition before a second DM outreach.
2. Share the zone card content in communities those influencers participate in (herbalism forums, Discord servers, Facebook groups where they are members).
3. For Phase 2: the influencer channel should be de-emphasized. Reddit and Pinterest organic search are stronger distribution levers for this product type at zero follower count.

---

## Scenario 5: High Unsubscribe Rate

**Trigger condition**: Email unsubscribe rate exceeds threshold.
- CAUTION: 2–5% of total broadcast recipients unsubscribe
- NO-GO: > 5% unsubscribe rate on any single broadcast or cumulatively across the welcome sequence

---

**Step A: Identify which email triggered the spike (1 minute)**

In Campaign Monitor, check unsubscribe counts per broadcast and per Kit automation step. A spike on a specific email (rather than gradual decay across the sequence) indicates that email's content was misaligned with subscriber expectations.

---

**Step B: Audit the problematic email (3 minutes)**

Read the email that triggered the spike. Ask:
- Did the email's content match what subscribers opted in to receive?
- Did the email contain a sales pitch if subscribers expected purely educational content?
- Was the subject line misleading (promised something the email didn't deliver)?

---

**Step C: CAUTION response (2–5% unsubscribe)**

Pause any additional broadcast emails for 48 hours. Do not pause the Kit automation sequence (automation emails have lower unsubscribe risk than broadcasts because they are triggered by subscriber action). Review and revise the next scheduled broadcast before sending. Aim for: one clear value-deliver per email, no more than one CTA per email.

---

**Step D: NO-GO response (> 5% unsubscribe)**

1. Immediately pause all broadcast emails (do not pause automation).
2. Audit the subscriber source: how did these subscribers join? If a large batch joined from a Reddit post that described the product differently than the emails deliver, there is an audience mismatch. The solution is to align email content with what the subscriber expects based on the channel they came from.
3. If unsubscribe rate is > 10% on any single email: that email should not be resent. Archive it. Rewrite the entire email.
4. Log in WORKLOG.md with the unsubscribe rate, email that triggered it, and diagnosis.

---

## Scenario 6: Social Media Zero Traction

**Trigger condition**: No meaningful organic engagement on social channels.
- Day 7 NO-GO: < 200 Instagram reach total AND 0 Twitter mentions AND Reddit posts removed or 0 upvotes

---

**Step A: Check account standing (1 minute)**

- Instagram: go to Settings > Account Status. Is the account under any restrictions or shadowban?
- Reddit: check your account karma and post history for any removals
- Twitter/X: check whether the account is in "limited distribution" mode (visible in Settings > Your Account > Account information)

A new account with zero prior history is at elevated risk of algorithmic downranking on all platforms. This is normal and not a permanent failure state.

---

**Step B: Shift to community participation (highest-ROI action)**

Rather than broadcasting to an empty follower list, participate in existing conversations:

1. Reddit: search r/herbalism for recent threads about zone-specific planting or wild edibles. Comment with helpful information. Include the Gist URL only where it genuinely answers the question ("I made a free zone quick-start card for this — [URL] if helpful").
2. Instagram: find posts tagged #zonegardening, #wildedibles, #herbalism with recent high engagement. Leave substantive comments (not "great post!"). Do not pitch.
3. This builds discovery and follower count organically. Results appear within 3–5 days of consistent participation.

---

**Step C: Test one paid post if organic is confirmed failing at Day 7**

If Day 7 shows < 200 Instagram reach despite 5+ posts and 3+ days of community participation: run a $10–20 test on Instagram. Target: gardening interests + herbalism interests + United States. Use the highest-performing organic post as the ad creative. Measure cost per link click. If cost per click is < $1.50, scale to $50. If cost per click is > $2.50, the creative or audience targeting needs adjustment.

---

## Scenario 7: Sales/Revenue Channel Mismatch

**Trigger condition**: Revenue is present but concentrated in one unexpected channel (or absent from the expected channel).

Example: Day 7 shows 5 sales, all from direct search — but email and social show zero conversion. Or: 0 Etsy sales despite strong email open rate and Gist views.

---

**Step A: Map revenue to acquisition source (3 minutes)**

If UTM parameters or Bitly links are tracking referral sources: check the breakdown in Google Analytics (Acquisition > Traffic Acquisition) or Bitly dashboard.

If no UTM tracking was set up: estimate by timing. A sale within 4 hours of the launch email send is email-attributed. A cluster of sales on June 5–6 after a Reddit post that spiked upvotes is Reddit-attributed.

---

**Step B: Double down on the working channel**

If email is converting but social is not: send an additional email broadcast to non-openers of the launch email (with a revised subject line). Do not invest more time in social content for the rest of the 14-day window.

If Reddit is converting but email is not: add the Gist URL and Etsy bundle link to every Reddit comment and post going forward. Convert any social media posting time into Reddit community participation time.

If no channel is converting but Gist views are present: the product landing experience (Gist) is not converting browsers to buyers. Add a clearer call-to-action at the top of the Gist: "Want the full bundle? Available on Etsy at [URL]." A single above-the-fold CTA can meaningfully improve conversion from a content page.

---

## Scenario 8: Multi-Failure Escalation Protocol

**Trigger condition**: Two or more of the following are in NO-GO state simultaneously at any checkpoint:
- Email open rate < 10%
- Gist views < 30 at Day 3 or < 50 at Day 7
- 0 influencer responses at Day 7
- 0 sales at Day 7 (listing Active for 3+ days)
- High unsubscribe rate > 5%

---

**Multi-failure triage (complete before executing any individual scenario)**

When multiple signals fail simultaneously, the root cause is almost always one of three things. Diagnose the root cause first, then the individual scenarios resolve faster.

**Root cause A: Launch did not execute**

Check: Were the launch emails sent? Was the Kit automation active on June 4? Were the social posts published? Were the Reddit posts submitted?

If any of these were not executed: this is not a product failure. It is a launch execution gap. Execute the missing items immediately (email outreach, Reddit posts, social posts). Give the campaign 72 additional hours before re-evaluating against thresholds.

**Root cause B: Distribution infrastructure broken**

Check: Does the Gist URL work in an incognito window? Is the Kit landing page accessible? Is the email domain on a blocklist?

If any of these are broken: fix the infrastructure first. All downstream metrics will improve once the plumbing works. See Scenario 2 (Gist) and Scenario 1 (Email) for infrastructure repair steps.

**Root cause C: Audience mismatch**

If all infrastructure is working and all outreach was sent but engagement is near zero across all channels: the product positioning does not match the audience. Indicators: normal email deliverability, normal open rate for a cold list (15–20%), but near-zero click rate and zero conversion.

Response:
1. Do not send more emails or posts until the positioning is revised.
2. Ask 1–2 people in your personal network who match the target audience to review the Gist and the Etsy listing. What do they think the product is? If their answer differs from your intent, revise the positioning before the Day 14 checkpoint.
3. The Day 14 checkpoint remains the evaluation gate. A revised positioning launched on Day 8–10 gives 4–6 days of data before the Day 14 decision.

---

## GO / CAUTION / NO-GO Summary

| Status | Meaning | Action |
|--------|---------|--------|
| GO | All thresholds met or exceeded | Continue executing launch plan as designed. Consider activating amplification actions (Track A holdouts, affiliate outreach, paid test). |
| CAUTION | Some metrics below threshold but not catastrophically low | Continue current plan. Investigate the specific gap. Do not expand scope until the gap is understood. |
| NO-GO | One or more critical metrics failed | Execute the matching scenario tree above. Stabilize before committing to Phase 2 expansion. |

---

*Document version: 1.0 — June 4, 2026*
*References: TRACK_B_MONITORING_AUTOMATION_FRAMEWORK.md (metric collection), POST_LAUNCH_ANALYSIS_TEMPLATE.md (log), CONTINGENCY_DECISION_PLAYBOOK.md (predecessor)*
