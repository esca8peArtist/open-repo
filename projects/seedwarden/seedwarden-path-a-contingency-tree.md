---
title: "Seedwarden Path A — Contingency Decision Tree"
date: 2026-05-31
status: production-ready
scope: Common launch-day and post-launch issues
decision_framework: If X happens, do Y
---

# Seedwarden Path A — Contingency Decision Tree

**Purpose**: Quick-reference guide for common issues during June 1 execution and June 1–7 monitoring.

**How to use**: Find your issue in the left column. Follow the decision tree on the right.

---

## LAUNCH DAY (June 1, 08:00–09:00 UTC)

---

### Issue 1: Reddit Account Restrictions

**Symptom**: Reddit shows "You are not allowed to post in this community" when you try to submit to r/herbalism.

**Why it happens**: 
- Account is too new (< 30 days old)
- Insufficient karma in r/herbalism (need 50+ to post)
- Account was suspended or restricted

**Decision Tree**:

```
Is your account under 30 days old?
├─ YES → Send modmail instead (recommended)
│        └─ Go to r/herbalism sidebar → Click "Modmail"
│        └─ Use message template from seedwarden-path-a-execution-checklist.md
│        └─ Mods typically respond within 24–48 hours
│        └─ Continue with emails while waiting for mod response
│
├─ NO → Check karma
│        ├─ Have 50+ karma in r/herbalism?
│        │  ├─ YES → Contact Reddit support (likely shadowban)
│        │  │         └─ Continue to r/foraging instead (750K+ members, same reach)
│        │  │
│        │  └─ NO → Post in r/foraging instead (no karma requirement)
│        │          └─ Use same post title and body
│        │          └─ r/foraging is 6x larger than r/herbalism
```

**Action**:
1. If account is new: Send modmail to r/herbalism (see template below)
2. While waiting for modmail response: Proceed with Step 2 (emails)
3. Alternative if modmail rejected: Post to r/foraging, r/HerbalMedicine, or r/homesteading

**Modmail Template** (ready to copy-paste):

```
Subject: Educational Resource Post Request — Zone-Specific Herb Guides

Hi r/herbalism moderators,

I'd like to share an educational resource with your community: zone-specific 
growing guides for herbalists (Zones 3–10). 

These are free one-page PDFs covering frost dates, quick-start crops, storage 
timing, and heirloom varieties calibrated to each zone.

I'm not selling anything — the guides are freely available. I'd appreciate 
permission to post this resource in the community.

Thank you,
[Your name]
```

**Time impact**: +0 to +24 hours (can continue with emails while waiting)

---

### Issue 2: Email Client Rejects Batch Send

**Symptom**: Gmail warning "too many recipients" or "unusual activity detected" when you try to send to multiple contacts.

**Why it happens**: 
- You're hitting Gmail's daily send limit (~100–500 depends on account age)
- Account flagged for unusual activity
- BCC recipient limit reached

**Decision Tree**:

```
How many emails have you sent so far?
├─ Fewer than 10 → Likely a false flag
│                  └─ Wait 1 hour, try again
│                  └─ Or switch to individual send mode (slower, always works)
│
├─ 10 or more → You've hit daily send limit
│               └─ Switch to individual send mode immediately
│               └─ Instead of BCC all 5 contacts: send 5 separate emails
│               └─ Time: 25 min → 35 min (still within 60-min window)
│               └─ Do not delay — send the individual emails now
```

**Action**:
1. If false flag: Wait 30 min, refresh Gmail, try again
2. If real limit: Send each email individually (one at a time, one window per contact)
3. Use exact same customized message for each person (copy from templates)
4. Check "Sent" folder to confirm all 5 sent

**Time impact**: +10 minutes (25 min → 35 min for emails; still in window)

---

### Issue 3: Gist URL Broken or Inaccessible

**Symptom**: Test your Gist URL in incognito window (before sending outreach). You get 404, permission error, or blank page.

**Why it happens**:
- Gist was deleted or archived
- GitHub account locked
- Gist privacy settings changed to "private"
- Gist URL changed

**Decision Tree**:

```
Is the Gist currently public and accessible?
├─ YES (you can download PDFs) → Proceed with outreach immediately
│                                └─ No action needed
│
└─ NO (404, permission error, blank) → STOP. Do not send outreach yet.
   ├─ Can you fix the Gist?
   │  ├─ YES → Fix it now, test the link, then send all outreach
   │  │
   │  └─ NO (Gist deleted, GitHub account issues) → 
   │      ├─ Use Google Drive backup immediately
   │      │  └─ Upload all 8 PDFs to Google Drive
   │      │  └─ Right-click folder > Share > "Anyone with link"
   │      │  └─ Copy the Google Drive folder URL
   │      │  └─ Replace [GIST_URL] with Google Drive URL in all messages
   │      │  └─ Proceed with outreach (no delay)
   │      │
   │      └─ Alternative: Use Gumroad free product
   │           └─ Create Gumroad account (free)
   │           └─ Upload 8 PDFs as one free product
   │           └─ Share the Gumroad URL instead
   │           └─ Proceed with outreach
```

**Action**:
1. Test Gist URL in incognito window: `https://gist.github.com/[your_username]/[gist_id]`
2. If working: Proceed with outreach
3. If broken: Use Google Drive or Gumroad immediately, update all messages, send

**Time impact**: 0 minutes (if working) or +15 minutes (if need to switch to Google Drive/Gumroad)

---

### Issue 4: Running Out of Time (T+30 and Still Not Done)

**Symptom**: It's 08:30 UTC and you've only completed Reddit and 3 emails. You're behind schedule.

**Why it happens**: 
- Customizing emails took longer than expected
- Technical issues with sending
- Distractions or interruptions

**Decision Tree**:

```
How many of the 19 items have you sent?
├─ 15+ (Reddit + 5 emails + most DMs) → You're almost done
│                                       └─ Finish DMs now (5 min)
│                                       └─ Complete monitoring setup
│                                       └─ You will finish by 08:50 UTC (fine)
│
├─ 8–15 (Reddit + emails + some DMs) → You're on track
│                                       └─ Continue. Finish by 08:55 UTC is acceptable
│
├─ Less than 8 → You're behind schedule
│                └─ Reduce customization effort
│                └─ Use template messages with minimal changes
│                └─ Skip nice-to-have customizations
│                └─ Prioritize: Reddit + 5 emails + Tier 1 DMs (4 highest-reach contacts)
│                └─ Defer: Lower-tier DMs to June 1 afternoon (less urgent)
```

**Action** (if behind schedule):
1. Reduce email customization to 1–2 lines per email (keep it short)
2. Send all 5 emails in next 10 minutes (no fancy customization)
3. Send Reddit modmail messages (3) quickly (2 min)
4. Send Discord DMs (3) quickly (3 min)
5. Skip Facebook and lower-tier DMs — send June 1, 14:00–15:00 UTC instead
6. You will have reached 130K+ Reddit members + 5 top contacts + 3 communities by 08:55 UTC
7. Follow-up DMs can be sent June 1 afternoon with no loss of effectiveness (DM audience is more forgiving of timing)

**Time impact**: Finish by 08:55 UTC instead of 08:45 UTC (acceptable)

---

## POST-LAUNCH (June 1–7)

---

### Issue 5: Zero Email Responses by June 2 18:00 UTC

**Symptom**: You sent 5 emails on June 1 at 08:10–08:22 UTC. By June 2 18:00 UTC (40+ hours later), you have 0 responses.

**Why it happens**:
- Emails landed in spam folder
- Contacts are busy or on vacation
- Subject line didn't convey urgency
- Normal for cold outreach (typical response time is 2–7 days)

**Decision Tree**:

```
Have you checked spam/promotions folders?
├─ YES, emails landed in spam → 
│  ├─ Forward emails to inbox (filter rule to prevent future spam)
│  └─ Consider "no response" status expected (contacts may not see spam folder)
│  └─ Send gentle follow-up from different email address if available
│
└─ NO, still in inbox → 
   ├─ Did any contact respond? (Check inbox)
   │  ├─ YES, 1+ responses → Send follow-up to remaining non-responders
   │  │                      └─ See Issue 6 (Selective follow-up)
   │  │
   │  └─ NO responses → Send follow-up email to all 5
   │                     └─ This is expected at 24 hours; push toward response
   │                     └─ Use follow-up template below
```

**Follow-up Email Template** (June 2, 18:00 UTC):

```
Subject: Quick follow-up — zone guides launched today

Hi [CONTACT_NAME],

Sent you a note yesterday about the Seedwarden zone guides launching today. 
Wanted to make sure it landed.

Free download: [GIST_URL]

Happy to chat if you have questions or if you'd like to feature these with 
your community.

Best,
[YOUR_NAME]
Seedwarden
```

**Action**:
1. Check spam folder first
2. Send the follow-up email to all non-responsive contacts on June 2, 18:00 UTC
3. Do not panic — 24-hour zero response is normal for cold outreach
4. Better response signal comes on June 3–5 as contacts check email

**Expected response timeline**:
- Day 1 (0–24 hours): 0–5% response (rare)
- Day 2–3 (24–72 hours): 5–15% response (typical)
- Day 4–7 (72+ hours): 10–20% cumulative response (goal)

**Time impact**: +5 minutes (sending follow-up email)

---

### Issue 6: One or Two Top Contacts Responded Positively

**Symptom**: Sabrena Gwin (AHG) replied "Great resource. I'll feature in the June newsletter." Or Susan Leopold replied "Love the FGV angle. Let's discuss partnership."

**Why it matters**: Early positive responses are your highest-value signal. They require action.

**Decision Tree**:

```
What type of response did you get?
├─ YES, they want to feature it
│  └─ What did they ask?
│     ├─ No specific asks → Thank them, ask for timing/placement
│     │                   └─ Example: "Thanks! Would June 3 or June 10 work for the newsletter? 
│     │                              And should I send any graphics or just the link?"
│     │
│     ├─ They want specific format (image, description, etc.) → Provide within 2 hours
│     │                                                        └─ Ask clarifying questions
│     │                                                        └─ Turn around fast (this is your biggest win)
│     │
│     └─ They want to discuss partnership/affiliate → Reply within 1 hour
│                                                    └─ Confirm interest
│                                                    └─ Propose next call/meeting time (June 2–3)
│                                                    └─ Share affiliate terms if ready
│
├─ They have questions or concerns
│  └─ What question?
│     ├─ "Is this for sale?" → See Response Template 1 in monitoring dashboard
│     │                        └─ Clarify free vs. paid plan
│     │
│     ├─ "Who are you?" / Credibility question → Reply with credentials
│     │                                          └─ Keep it short: "2-year research project on bioregional herbalism"
│     │                                          └─ Link to LinkedIn or personal website (if available)
│     │
│     ├─ "Can I feature this?" → YES, absolutely
│     │                           └─ See Response Template in monitoring dashboard
│     │                           └─ Provide any assets they need
│     │
│     └─ Domain-specific question (e.g., "Why didn't you include Zone 2?") → 
│        └─ Answer honestly and briefly
│        └─ Offer to create Zone 2 as a follow-up if there's demand
```

**Action**:
1. Reply to positive responses within 2 hours (fast response = serious signal)
2. For feature requests: provide any assets/descriptions they ask for
3. For partnership interest: schedule call for June 2–3
4. Forward email to your monitoring spreadsheet for tracking

**Time impact**: +15 minutes per positive response (email reply + light follow-up work)

---

### Issue 7: Reddit Post Removed or Suppressed

**Symptom**: June 2, you check your Reddit post and it's gone (or it has 0 upvotes after 24 hours and you suspect it was shadowbanned).

**Why it happens**:
- Subreddit spam filter or promotional content rules
- New account restrictions
- Keyword filter triggered (e.g., "free" or external links)
- Moderators removed it

**Decision Tree**:

```
Can you still see your post in your Reddit history?
├─ YES, post is live (you can see it in your profile)
│  └─ But it has 0 upvotes and 0 comments after 24 hours?
│     └─ Your post was likely shadowbanned by the subreddit filter
│     └─ It's visible to you but not to other users
│     └─ Modmail r/herbalism and ask: "Is my post visible? It's not getting traction."
│     └─ If no response: Repost in r/foraging or r/HerbalMedicine
│
└─ NO, post is gone (not in your history)
   └─ It was removed by moderators
   └─ Check your messages for removal reason (usually a comment on the post)
   └─ Decision:
      ├─ Was it removed for "promotional content"?
      │  └─ Do NOT repost the same post to r/herbalism
      │  └─ Instead: Post to r/gardening, r/foraging, or r/homesteading
      │  └─ These communities have different mod rules
      │
      ├─ Was it removed for "new account"?
      │  └─ Send modmail asking: "Can I share this resource as an established community member?"
      │  └─ While waiting: Post to r/foraging (no new account restrictions)
      │
      └─ Was it removed for "external links"?
         └─ Post to r/foraging instead (allows Gist links)
         └─ r/foraging is 750K+ members (much larger than r/herbalism anyway)
```

**Backup Subreddits** (in priority order):

| Subreddit | Members | Best for | Posting Requirements |
|-----------|---------|----------|----------------------|
| r/foraging | 750K+ | Educational resources | None; no new account restrictions |
| r/HerbalMedicine | 20K–40K | Clinical practitioner audience | May need approval; send modmail |
| r/homesteading | 500K+ | Gardening & growing guides | None |
| r/gardening | 3.5M+ | Gardening audience | May need approval; send modmail |

**Action**:
1. If shadowbanned: Modmail r/herbalism asking if post is visible
2. If removed: Do not repost to same subreddit; post to r/foraging instead
3. Use exact same post title and body in backup subreddit
4. r/foraging is actually the highest-reach herbalist community (750K vs 130K)

**Time impact**: +5–10 minutes (reposting to backup subreddit)

---

### Issue 8: Gist View Count Stuck Below Target on June 6

**Symptom**: It's June 6 (Day 5). You have:
- Gist views: 20 (target was 70+)
- Reddit upvotes: 8 (target was 25+)
- Email responses: 0

**Why it happens**:
- Reddit post underperformed (most likely cause)
- Gist link was not inserted in all messages (check your sent emails)
- Audience didn't find the content valuable
- Technical issue (URL broken, Gist private)

**Decision Tree**:

```
Diagnose the problem first (15 minutes). Do not take action without diagnosis.

Step 1: Check if Gist URL was in all messages
├─ YES → Proceed to Step 2
└─ NO → Add URL to messages now; update DMs/modmail with corrected link

Step 2: Check Reddit post status
├─ Post is still live? 
│  ├─ YES, but 0 upvotes → Post was shadowbanned
│  │                       └─ Repost in r/foraging immediately
│  │
│  └─ NO, removed → Already covered in Issue 7
│                   └─ Post in r/foraging if not already done

Step 3: Check if emails were actually sent
├─ Check Gmail Sent folder
├─ All 5 emails present?
│  ├─ YES → Proceed to Step 4
│  └─ NO → Send unsent emails immediately (this is your biggest miss)

Step 4: Is this just Week 1 underperformance?
├─ YES, this is normal for new products → Proceed with Day 10 re-check (June 11)
│                                        └─ Do not panic. More content and time will show trajectory.
│
└─ NO, emails were sent, Reddit worked → Consider that audience may not find it valuable
                                        └─ Proceed with Day 10 re-check
                                        └─ Plan content adjustments for Phase 2 based on feedback
```

**Action** (in priority order):
1. Verify all 5 emails were sent (check Sent folder)
2. If unsent: Send immediately
3. Repost to r/foraging if Reddit post failed
4. Update Gist with a call-to-action (e.g., "Please leave feedback in the comments")
5. Do not panic. Week 1 low performance is normal. Day 10 check (June 11) will show real trajectory.

**Time impact**: +30 minutes (diagnosis + fixes)

---

### Issue 9: One Contact Asks "What's Your Track Record?" or "Prove Credibility"

**Symptom**: John Gallagher (LearningHerbs) replies: "Interesting. Can you tell me more about Seedwarden's background? Who's behind this?"

**Why it happens**: Influencers with large audiences need confidence that you're legitimate.

**Decision Tree**:

```
What credibility signals do you have?
├─ Established herbalism credentials (RH, NAMA, AHG, etc.)
│  └─ Mention in reply immediately
│  └─ Example: "I'm a registered herbalist with 5 years clinical practice."
│
├─ Prior published work or education
│  └─ Link to website, LinkedIn, or publications
│  └─ Keep it brief: "You can find background here: [link]"
│
├─ Research/consultation background
│  └─ Share research process: "2-year research project collaborating with [organizations]"
│  └─ Mention collaborators/advisors if applicable
│
└─ None / Early-stage / Solo project
   └─ Be honest and lean into the "grassroots" angle
   └─ Example: "This started as a personal research project because I couldn't find 
                zone-specific guides for my practice. I've tested all content with 
                my own growing seasons and consulted with [1–2 practitioners you've worked with]."
   └─ Honesty and transparency > false credibility
```

**Example Response** (if you have limited formal credentials):

```
Great question. Seedwarden started as a personal research project — I noticed 
there was a gap between general zone guides and what actually works for 
practitioners in specific bioregions.

I've spent 2 years testing growing timing and heirloom varieties with my own 
herbalism practice, and I've had these guides reviewed by practitioners in 
[Zone X] and [Zone Y] to ensure regional accuracy.

I'm not a nationally-known figure, but these guides are built on real growing 
experience and feedback from practitioners in each zone.

If you'd like to discuss further, I'm happy to hop on a call and answer any 
questions about the research or content.

Best,
[YOUR_NAME]
```

**Action**:
1. Reply honestly with whatever credibility you have
2. Focus on the guides' quality and real-world testing, not your fame
3. Offer to discuss in more detail (call, email, etc.)
4. If asked for testimonials: You may not have them yet (new product), so offer to get feedback from early users

**Time impact**: +10 minutes (email reply)

---

### Issue 10: Commission Rate Question or Affiliate Terms Discussion

**Symptom**: John Gallagher or another high-value contact replies: "Interested in affiliate. What terms are you offering?"

**Why it matters**: This is a major win. You need to respond quickly with clear terms.

**Decision Tree**:

```
Do you have affiliate terms already decided?
├─ YES → Reply immediately with numbers
│        └─ Example: "15% commission per sale. Tracking URL: [link]. Payout monthly."
│        └─ Attach any affiliate agreement if you have one
│        └─ Offer to schedule call to discuss
│
└─ NO → Decide NOW based on your business model
   ├─ What's your plan?
   │  ├─ Free Gist + Etsy paid bundle ($5–9 price point)
   │  │  └─ Offer: 20–25% commission on Etsy sales only
   │  │  └─ Explain: "Etsy bundles launching June 10. You'll get affiliate link."
   │  │
   │  ├─ Free Gist only (no paid option yet)
   │  │  └─ Offer: Newsletter feature + revenue share on future paid product
   │  │  └─ Explain: "Free guides first. Paid bundles launching June 10. We'll offer affiliate terms then."
   │  │
   │  └─ Unsure about business model
   │     └─ Reply honestly: "Great question. I'm deciding between free/paid model this week.
   │                         Can we schedule a call June 2–3 to discuss partnership structure?
   │                         I want to make sure terms work for both of us."
   ```

**Safe Default Terms** (if unsure):

```
For the free Gist version: We'll feature your recommendation in our acknowledgments 
and offer first access to any paid products launching later.

For future paid products: 15–20% affiliate commission per sale from your link, 
tracked and paid monthly.

Does that work as a starting point?
```

**Action**:
1. If you have terms ready: Reply immediately (same day)
2. If you don't: Decide within 24 hours and follow up
3. Schedule call to discuss details (don't negotiate 5 back-and-forth emails)
4. Move fast. Influencer interest cools quickly if you delay.

**Time impact**: +15 minutes (email + decision-making)

---

## DECISION TREE SUMMARY

| Issue | First Step | Second Step | Time to Resolve |
|-------|-----------|-------------|-----------------|
| 1. Reddit restrictions | Check account age | Send modmail or post to r/foraging | 5–10 min |
| 2. Email batch send rejected | Wait 30 min or switch individual send | Send emails one-by-one | 10 min |
| 3. Gist URL broken | Test URL in incognito | Switch to Google Drive or Gumroad | 15 min |
| 4. Running out of time | Reduce customization | Prioritize top contacts, defer lower-tier | 0 min |
| 5. Zero email responses by Day 2 | Check spam folder | Send follow-up email to all 5 | 5 min |
| 6. Positive response from top contact | Reply within 2 hours | Provide any requested assets | 10 min |
| 7. Reddit post removed/suppressed | Check post status | Repost to r/foraging | 10 min |
| 8. Low Gist views on Day 5 | Diagnose (15 min) | Fix root cause (send emails, repost Reddit) | 30 min |
| 9. Credibility question | Reply with honest background | Offer to discuss further | 10 min |
| 10. Affiliate terms question | Decide commission rate | Reply with numbers | 15 min |

---

## WHEN TO ESCALATE / ASK FOR HELP

**Do not panic if any of these happen.** They are all recoverable within a few minutes.

**Escalate to user if**:
- Gist URL completely broken and no Google Drive backup available (stop and request backup from user)
- Email account locked or suspended (stop and request account access)
- All 3 backup subreddits (r/foraging, r/HerbalMedicine, r/homesteading) reject post (stop and reassess messaging)

**Do not escalate if**: Anything in the decision tree above. Those are all recoverable.

---

**Document version**: 1.0  
**Last updated**: 2026-05-31  
**Status**: Ready for June 1–7 troubleshooting
