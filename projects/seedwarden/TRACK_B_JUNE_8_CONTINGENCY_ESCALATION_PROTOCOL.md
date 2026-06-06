---
title: "Track B Day 3 Contingency Escalation Protocol — June 8, 2026"
created: 2026-06-06
status: pre-staged
execution-date: 2026-06-08
purpose: >
  User notification templates for Day 3 checkpoint contingencies. If CAUTION
  or NO-GO triggered after metrics collection, send the appropriate template
  to user. Includes: issue summary, impact assessment, recommended actions,
  and escalation criteria for orchestrator autonomous intervention.
---

# Track B Day 3 Contingency Escalation Protocol
**Checkpoint**: June 8, 2026 at 08:00 UTC  
**Escalation trigger**: CAUTION or NO-GO from TRACK_B_JUNE_8_DECISION_LOGIC_FLOWCHART.md  
**Recipient**: User (via CHECKIN.md or Discord)

---

## Template A: Email Open Rate CAUTION (10–19%)

**When to use**: Email open rate fell into 10–19% range at Day 3

---

### User Notification

```
🟡 TRACK B CHECKPOINT: Email open rate CAUTION (10–19%)

Date: June 8, 2026
Metric: Campaign Monitor open rate
Value: [____]%
Threshold: GO ≥20% | CAUTION 10–19% | NO-GO <10%

STATUS: CAUTION — Investigate but continue execution

DIAGNOSIS:
The launch email was delivered (bounce rate normal) but open rate is lower
than optimal. This typically indicates a subject line problem (recipients
chose not to open) rather than a deliverability issue.

IMMEDIATE ACTIONS (Execute today):
1. Review subject line: Was it personalized to zone/region?
   Current subject: _________________
   
2. Draft revised subject line using zone-specific framing:
   New subject: _________________
   
3. Send re-engagement campaign to non-openers:
   - Campaign Monitor: Campaigns > [Original campaign] > Create follow-up
   - Target: Non-openers (people who received but didn't open)
   - New subject: [Your revised subject from above]
   - Send timing: June 8 or June 9 (within 24h of original send)
   
4. Track: Original open rate vs re-engagement open rate
   - Original: [____]%
   - Re-engagement: _____% (fill in after second broadcast)

IMPACT:
- Phase 2 content and Day 7 checkpoint not affected
- Continue social calendar as planned
- Email re-engagement is an A/B test opportunity

NEXT CHECKPOINT: June 11 at 08:00 UTC (Day 7)
- At Day 7, email metrics include cumulative opens from both broadcasts
- Target: combined open rate ≥15% (strong signal for Phase 2 distribution)

Questions? Check CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 1 (Low Email Open Rate)
```

---

## Template B: Email Open Rate NO-GO (<10%)

**When to use**: Email open rate fell below 10% threshold at Day 3

---

### User Notification

```
🔴 TRACK B CHECKPOINT: Email open rate NO-GO (<10%)

Date: June 8, 2026
Metric: Campaign Monitor open rate
Value: [____]%
Threshold: GO ≥20% | CAUTION 10–19% | NO-GO <10%

STATUS: NO-GO — Immediate remediation required

DIAGNOSIS:
Email delivery rate is critically low. This indicates either:
A) Deliverability problem (bounces, spam folder, SPF/DKIM misconfiguration)
B) Launch broadcast was never sent (status = Draft, not Sent)

IMMEDIATE ACTIONS (Execute within 1–2 hours):

Step 1: Check broadcast status in Campaign Monitor
  - Log in to Campaign Monitor > Campaigns
  - Find the June 4 launch broadcast
  - Status: [ ] Sent  [ ] Draft  [ ] Scheduled  [ ] Failed
  
  IF DRAFT OR SCHEDULED: Send immediately. This is the most common cause.
  
Step 2: Check your own email spam folder
  - Log in to wanka95@gmail.com
  - Check Spam/Junk folder
  - Is the launch email there?
  
  IF YES: SPF or DKIM record misconfiguration. 
          See "SPF/DKIM Fix" below.
  
  IF NO: Proceed to Step 3.

Step 3: Verify email list quality
  - Campaign Monitor > Campaigns > [Original campaign] > View Report
  - Check bounce rate: _____% 
  
  If bounce rate > 5%: Email list quality issue.
    Recommended: Upload a cleaned list (remove hard bounces) 
                 and resend within 24 hours.
  
  If bounce rate < 5%: Proceed to Step 4.

Step 4: Manual outreach to Tier 1 contacts
  - Send the launch email manually from Gmail (wanka95@gmail.com)
  - To: The 15 influencer contacts from TRACK_B_HERBALIST_OUTREACH_MATRIX.md
  - Subject: [Use your best subject line]
  - Body: [Copy the launch email body]
  - Timing: Send within 1–2 hours of this checkpoint
  - Reason: Gmail has higher inbox placement than Campaign Monitor for outbound personal email

Step 5: SPF/DKIM Fix (if email is in spam folder)
  - Log in to your domain registrar ([your-domain].com)
  - Verify Campaign Monitor CNAME and TXT records are published:
    • CNAME: cname.createsend.com (or similar)
    • TXT: Campaign Monitor SPF record
  - If missing: Add them to your DNS
  - Wait 24–48 hours for DNS propagation
  - Test: Send a new Campaign Monitor test email to yourself
  - Once fixed: Resend launch email to full list (non-openers)

IMPACT:
- Phase 2 content activation at risk if email channel broken
- Day 7 checkpoint is critical: IF email issue is fixed and re-send 
  succeeds, Day 7 metrics may show recovery
- Continue social calendar as planned (social is independent of email)

ESCALATION CRITERIA:
- If email still NO-GO at Day 7: Escalate to orchestrator for 
  infrastructure audit
- If email fixed but still <15% open at Day 7: Pivot to Kit-gated 
  PDF as primary distribution channel

NEXT CHECKPOINT: June 11 at 08:00 UTC (Day 7)
- Email metric will show both original + any re-sends
- Target: ≥15% cumulative open rate (if fixes implemented)

Questions? Check CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 1 (Low Email Open Rate)
```

---

## Template C: Gist Views CAUTION (30–70)

**When to use**: Gist view count is in CAUTION range at Day 3

---

### User Notification

```
🟡 TRACK B CHECKPOINT: Gist view count CAUTION (30–70)

Date: June 8, 2026
Metric: GitHub Gist cumulative views
Value: [____] views
Threshold: GO >70 | CAUTION 30–70 | NO-GO <30

STATUS: CAUTION — Expected for Day 3. Monitor and amplify.

DIAGNOSIS:
This is the expected range for a new launch at 72 hours. Organic discovery
is still growing. No immediate action required, but amplification can 
accelerate growth.

EXPECTED RANGE:
- Reddit-only launch: 30–50 views typical
- Reddit + Instagram bio: 50–70 views typical
- Multi-channel launch: 70+ views expected

OPTIONAL AMPLIFICATION ACTIONS:
1. Cross-post to one new community (if not already done):
   [ ] r/homesteading (if r/herbalism was primary)
   [ ] r/foraging (if no prior foraging community)
   [ ] r/gardening (broad audience)
   
2. Create a Pinterest pin:
   - Take a screenshot of Zone 5 or your zone card
   - Add text overlay: "Free USDA Zone Quick-Start Guide"
   - Pin to a botanical/gardening board
   - Link to your Gist
   
3. Instagram Stories (if not already done):
   - Share a screenshot of the zone card
   - Use link sticker to direct to Gist

IMPACT:
- Not critical at Day 3. View count growth is expected to accelerate through Day 7
- Phase 2 content (additional zones) can proceed independently of Gist view count
- Social calendar continues normally

NEXT CHECKPOINT: June 11 at 08:00 UTC (Day 7)
- Target: >200 cumulative views (all channels combined)
- If Day 3 = 50 views, Day 7 target = 150–200+ (typical 3–4x growth)

Questions? Check CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 2 (Low Gist View Count)
```

---

## Template D: Gist Views NO-GO (<30)

**When to use**: Gist view count fell below 30 threshold at Day 3

---

### User Notification

```
🔴 TRACK B CHECKPOINT: Gist view count NO-GO (<30)

Date: June 8, 2026
Metric: GitHub Gist cumulative views
Value: [____] views
Threshold: GO >70 | CAUTION 30–70 | NO-GO <30

STATUS: NO-GO — Investigate URL and channel placement

DIAGNOSIS:
<30 views at 72 hours suggests either:
A) Gist URL is broken or missing from outreach materials
B) Social posts were removed by moderators or shadow-filtered
C) URL was miscopied in outreach

IMMEDIATE ACTIONS (Execute within 1–2 hours):

Step 1: Verify Gist is accessible
  - Open the Gist URL in incognito browser
  - Does it load and display full content?
  
  IF 404 NOT FOUND: Gist was deleted
    Action: Recreate immediately. Update all URLs in:
            • Instagram bio
            • Reddit posts
            • Kit landing page CTA
            • Launch email (if resending)
  
  IF LOADS NORMALLY: Proceed to Step 2.

Step 2: Audit URL placement across all channels
  [ ] Instagram bio: URL present and clickable?
  [ ] Reddit posts (all 3): URL in post body?
  [ ] Kit landing page: CTA button links to correct Gist?
  [ ] Launch email: [Launch email body] contains link?
  [ ] Twitter/X bio: URL present?
  
  For each missing placement: Add URL within 1 hour
  
Step 3: Check Reddit post status
  - Log in to Reddit > Your profile > Submitted posts
  - Are all June 4 posts visible?
  
  IF MISSING (removed by mods):
    Action: Do NOT repost identical content (likely shadow-filtered again)
    Instead: Create an IMAGE post (upload Zone 5 card as PNG)
             Post to r/foraging (less restrictive than r/herbalism)
             Use educational framing, not promotional
  
  IF VISIBLE but 0 UPVOTES:
    Action: Post was shadow-filtered
    Next: Message subreddit moderators asking for explicit approval 
          before next post (see HERBALIST_PARTNERSHIP_EMAIL_TEMPLATE.md)

IMPACT:
- Gist is the primary distribution endpoint for Zone Cards
- If Gist URL is broken, all outreach traffic is lost
- Rapid fix required to avoid Day 7 cascade failure

NEXT CHECKPOINT: June 11 at 08:00 UTC (Day 7)
- After fixes, expect 3–4x growth: 30 views Day 3 → 90–120 views Day 7
- If Day 7 still <50 views after fixes: activate alternate channels 
  (Etsy listing, Pinterest, new Reddit community)

Questions? Check CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 2 (Low Gist View Count)
```

---

## Template E: Influencer Activity CAUTION (Responses, No Shares)

**When to use**: Received responses from influencers but no public shares yet

---

### User Notification

```
🟡 TRACK B CHECKPOINT: Influencer activity CAUTION (Responses, no public shares yet)

Date: June 8, 2026
Metric: Influencer responses vs public shares
Responses received: [____] of 15 contacts
Public shares: [____] confirmed sharing
Threshold: GO ≥1 public share | CAUTION responses but no shares | NO-GO 0 responses

STATUS: CAUTION — Expected at 72h. Public shares likely coming.

DIAGNOSIS:
Influencers have engaged (responded to outreach) but not yet posted publicly.
This is normal — public shares often come Days 3–5. The response indicates 
interest; posts follow once influencers integrate content into their schedule.

ACTIONS (Execute today):
1. Follow up with each influencer who responded but hasn't shared:
   Template: "Thanks for your interest! When you're ready to share, 
   we'd love a mention on [Instagram/Twitter]. No rush — share on your timeline!"
   
2. Confirm which contacts committed to sharing this week:
   ☐ Contact 1: _______________ | Expected date: _____
   ☐ Contact 2: _______________ | Expected date: _____
   ☐ Contact 3: _______________ | Expected date: _____
   (Fill in actual names + expected share dates)
   
3. Set a reminder to check their social feeds on expected share dates
   (Pinterest, Instagram, Twitter)

EXPECTED OUTCOME:
- Public shares typically appear Days 3–5 from influencers who've engaged
- Do NOT re-contact if share doesn't happen within 5 days (may annoy them)
- Document expected shares in POST_LAUNCH_ANALYSIS_TEMPLATE.md

IMPACT:
- Not critical. Influencer shares are bonus amplification, not baseline requirement
- Phase 2 content proceeds independently
- Social calendar continues normally

NEXT CHECKPOINT: June 11 at 08:00 UTC (Day 7)
- If any influencer has shared by Day 7: Upgraded to GO
- If still no shares by Day 7 but responses active: Escalate to new outreach approach

Questions? Check CONTINGENCY_TRIGGER_DECISION_TREE.md Scenario 3 (Influencer Activity)
```

---

## Template F: Multi-Failure Escalation (2+ metrics NO-GO)

**When to use**: Two or more metrics triggered NO-GO simultaneously

---

### User Notification

```
🔴🔴 TRACK B CHECKPOINT: MULTI-FAILURE ESCALATION (2+ NO-GO metrics)

Date: June 8, 2026
Failures:
  [ ] Email open rate <10%
  [ ] Gist views <30
  [ ] Influencers: 0 responses
  [ ] Sales: 0 orders + Etsy Draft

STATUS: MULTI-FAILURE — Requires immediate user decision

DIAGNOSIS:
Multiple channels failing simultaneously suggests either:
A) Critical platform issue (Campaign Monitor / GitHub / Etsy misconfiguration)
B) Core messaging or targeting problem (outreach not reaching intended audience)
C) Timing issue (launch materials sent to wrong list or at wrong time)

ORCHESTRATOR CANNOT AUTO-REMEDIATE MULTI-FAILURE.
Requires user investigation of root cause.

IMMEDIATE ACTIONS (User required):

1. Answer diagnostic questions:
   [ ] Was the launch email actually sent? (Check Campaign Monitor status)
   [ ] Are social post URLs correct? (Check Gist, Instagram bio, Reddit links)
   [ ] Did you receive any inquiries or feedback (email, DM, comments)?
   [ ] Is Etsy listing published (Active, not Draft)?

2. If all basic checks pass:
   Root cause may be messaging or audience mismatch. 
   Request user decision:
   "Track B launch experienced multi-channel failure. 
    Possible causes: messaging issue, audience mismatch, or platform misconfiguration.
    
    Options:
    A) Retry launch with revised messaging (1–2 hours prep)
    B) Pivot to Phase 1.5 outreach (direct email to herbalist community)
    C) Defer Phase 1 execution, troubleshoot platform integrations, relaunch Day 10+
    D) Other?"

ESCALATION TO ORCHESTRATOR:
This condition triggers Scenario 8 in CONTINGENCY_TRIGGER_DECISION_TREE.md
(Multi-Failure Escalation Protocol). 

Do not attempt individual scenario fixes. Escalate immediately.

Questions? Request multi-failure analysis session.
```

---

## How to Route Escalations

**If GO**: Log in CHECKIN.md "Track B Day 3: GO. Continue execution."

**If CAUTION**: 
1. Send Template A, B, C, D, or E (whichever matches the metric)
2. Log in CHECKIN.md: "Track B Day 3: CAUTION on [metric]. Executing [action]."
3. Schedule Day 7 re-check for June 11

**If NO-GO (single metric)**:
1. Send Template B, D, or similar (whichever matches the metric)
2. Log in CHECKIN.md: "Track B Day 3: NO-GO on [metric]. Executing [remediation]."
3. Execute recommended actions immediately (within 1–2 hours)
4. Schedule Day 7 re-check for June 11

**If NO-GO (multiple metrics — Template F)**:
1. Send Template F
2. Log in CHECKIN.md: "Track B Day 3: MULTI-FAILURE. Escalating for user decision."
3. Request user input on root cause and next steps
4. Suspend normal execution until user provides guidance

---

**Escalation initiated by**: ___________ | **Date/Time**: ___________ | **Template used**: [A/B/C/D/E/F]
