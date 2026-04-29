---
title: "Distribution Tracking Dashboard Setup — Phase 1"
created: 2026-04-29
status: execution-ready
path_compatibility: "Path A, Path A+37 Hybrid, Path B — tracking structure is identical across all paths"
---

# Distribution Tracking Dashboard Setup

**Built April 29, 2026. Production-ready.**

This file specifies the complete tracking infrastructure for Phase 1 distribution. The goal is not data collection for its own sake — it is generating the feedback signal that enables course correction when outreach strategies are underperforming. Every metric listed has a defined decision threshold: what does an underperforming number mean, and what action does it trigger?

---

## Email Response Tracking Spreadsheet

### Setup

Create a spreadsheet (Google Sheets or equivalent) with one row per contact. The spreadsheet is the canonical record for all Phase 1 outreach. Update it within 24 hours of any interaction.

### Column Structure

| Column | Field | Format | Notes |
|--------|-------|--------|-------|
| A | Contact name | Text | Last name, First name for sort |
| B | Organization | Text | |
| C | Title | Text | |
| D | Tier | 1/2/3 | |
| E | Wave | 1/2/3 | Within Tier 1: waves 1, 2, 3 |
| F | Domain focus | Text | Which domains sent (e.g., "28, 29") |
| G | Email address | Text | Confirmed address |
| H | Date sent | Date | YYYY-MM-DD |
| I | Template used | Text | Which template variant |
| J | Subject line | Text | Record exact subject line for A/B analysis |
| K | BCC tracking address | Checkbox | Did you BCC the tracking address? |
| L | Opened (if tracked) | Y/N/Unknown | Only trackable if using email tracking service |
| M | Responded | Y/N | |
| N | Response date | Date | |
| O | Response type | Code | See response type codes below |
| P | Meeting scheduled | Y/N | |
| Q | Meeting date | Date | |
| R | Meeting outcome | Text | Brief notes |
| S | Follow-up sent | Y/N | |
| T | Follow-up date | Date | |
| U | Warm intro provided | Y/N | Did this contact provide any introduction to another contact? |
| V | Intro to whom | Text | Name and org of any warm intro |
| W | Citation produced | Y/N | Did this contact cite, publish, or share the framework? |
| X | Citation source | URL | Link to any public citation |
| Y | Notes | Text | Free-form notes on conversation content, specific feedback |

### Response Type Codes

| Code | Meaning |
|------|---------|
| SR | Substantive response — engaged with the content, asked questions, or provided feedback |
| ACK | Acknowledgment — received, thank you, will review |
| FWD | Forwarded to colleague — contact said they are routing to someone else |
| MTG | Meeting requested by contact |
| NEG | Negative — explicitly not interested or declined |
| OOO | Out of office — follow up after return date |
| NR | No response — 14+ days since send |
| CITE | Citation — contact publicly cited or shared the framework |

### Priority sort logic

Sort by: Wave ascending, then Response Type (SR, MTG, CITE at top; NR at bottom). This keeps the most productive conversations visible and flags the no-response contacts for follow-up evaluation.

### Email tracking setup

Use BCC to a dedicated tracking address (create a new Gmail or equivalent: democraticrenewal.tracking@gmail.com or similar) for all outreach. This creates a timestamped record of every email sent without requiring third-party tracking software.

For opened/clicked tracking (optional): services like MailTrack (free tier) or HubSpot (free tier) can embed a 1x1 pixel in outgoing emails that reports when the email is opened. This is useful for identifying whether NR contacts actually saw the email. Note that many email clients (especially government and law school addresses) block tracking pixels — treat open-rate data as a floor estimate, not an exact count.

---

## Substack Analytics Dashboard

### Key metrics to monitor

Substack provides analytics at substack.com/[publication]/dashboard. The relevant metrics and their targets:

**Open rate**
- Definition: Percentage of subscribers who open each email
- Target: Greater than 25% (policy newsletter baseline); greater than 35% is strong
- Check after: Every post, within 72 hours (open rate stabilizes by 72 hours)
- If below 25%: Test subject line variants in the next three posts; compare performance

**Subscriber growth**
- Definition: Net new subscribers per week (new subscribers minus unsubscribes)
- Target: 50+ per week during the 8-week launch window
- Check: Weekly (every Sunday)
- Growth rate benchmarks: Week 1-2: 100+ (launch spike); Weeks 3-6: 50-75 (sustained growth); Weeks 7-8: 30-50 (consolidation). Below 20/week after Week 3 indicates the cross-platform amplification is underperforming.

**Referral sources**
- Definition: Where new subscribers are coming from (Reddit, Twitter/X, direct, other Substack, search)
- Target: No single source should exceed 60% of subscriber acquisition (over-concentration creates fragility)
- Check: Weekly
- Action: If Reddit is driving 70%+ of subscribers, invest more in Twitter/X and LinkedIn amplification; if Substack referrals are highest, invest in cross-newsletter promotion

**Top posts by open rate vs. click rate**
- Distinction: Open rate measures subject line effectiveness; click rate (percentage of openers who click through to the full proposal or a link) measures content effectiveness
- Target open rate: As above (25%+)
- Target click rate: 5%+ on posts that include a CTA to the full proposal
- Check: After each post

**Comment volume**
- Target: 5+ substantive comments per post
- High-value comment flag: Any comment from a Tier 1 or Tier 2 contact (a professor, a think tank staff member, a lawyer) — log in the email tracking spreadsheet under Notes for that contact if they commented publicly

**Unsubscribe rate**
- Target: Less than 1% per post (1-3% per month total)
- Red flag: Greater than 3% in any single post — indicates content misalignment with audience expectations; review that post's content and tone

### Weekly Substack Metrics Record

Maintain a second tab in the tracking spreadsheet:

| Week | Posts published | New subscribers | Total subscribers | Avg. open rate | Top post (open rate) | Reddit referrals | Twitter/X referrals | Unsubscribes | Notes |
|------|----------------|-----------------|-------------------|----------------|---------------------|-----------------|--------------------|-----------| ------|

---

## Reddit Tracking

Reddit does not have an API-accessible analytics dashboard for individual post authors; tracking must be manual.

### Per-post tracking record

Maintain a third tab in the tracking spreadsheet:

| Post date | Subreddit | Post title | Upvote count (24h) | Upvote count (72h) | Comment count | Gilded | Crosspost count | Notable comments (practitioner, academic, institutional) | Substack referrals in 48h window | Notes |
|-----------|-----------|------------|--------------------|--------------------|---------------|--------|-----------------|----------------------------------------------------------|----------------------------------|-------|

Check each post at 24 hours and 72 hours after posting. After 72 hours, Reddit engagement stabilizes.

**Performance thresholds:**

| Metric | Below target | On target | Strong |
|--------|-------------|-----------|--------|
| Upvote count (72h) | Less than 50 | 50-300 | 300+ |
| Upvote ratio | Below 80% | 80-90% | 90%+ |
| Comment count | Less than 10 | 10-30 | 30+ |
| Substack referrals from Reddit | Less than 5 | 5-20 | 20+ |

**Notable comments log**: When a practitioner (identified as a lawyer, academic, federal employee, etc.) leaves a substantive comment — especially a correction or an addition — log the comment text and any username (if they identified their affiliation) in the Notes column. These comments are valuable qualitative feedback even if they don't move the metrics.

**Cross-post sources**: Track if the post is crossposted to other subreddits organically. Crossposting indicates the content resonated with a community member enough to manually share it. Log the destination subreddit.

---

## Conversion Funnel

The conversion funnel maps the path from initial touchpoint to institutional impact. Track each stage.

**Stage 1: Initial exposure**
- Email sent / Reddit post published / Substack post published
- Tracked by: Spreadsheet send date / Reddit post record / Substack publication record

**Stage 2: Engagement**
- Email opened / Reddit upvote and click / Substack open
- Tracked by: Email open rate (estimated); Reddit upvote/comment count; Substack open rate

**Stage 3: Conversion to full proposal reader**
- Click to full proposal from email / Reddit post / Substack CTA
- Tracked by: Link click tracking (add ?utm_source=email or ?utm_source=reddit parameters to proposal links); Substack click rate

**Stage 4: Substack subscription**
- Reddit reader or email contact subscribes to Substack
- Tracked by: Substack referral sources

**Stage 5: Institutional action**
- Meeting scheduled (tracked in Column P of email spreadsheet)
- Citation produced (tracked in Column W/X)
- Media coverage (tracked separately in Notes)
- Policy adoption signal (tracked separately in Notes)

**Stage 6: Policy influence**
- Specific reform language appearing in introduced legislation
- Litigation strategy citing the framework
- Think tank publication incorporating the analysis
- Academic citation in published work

Stages 1-4 are trackable in real time. Stages 5-6 require active monitoring and cannot be tracked automatically — they require periodic review of news sources, legislative databases, and academic publication feeds.

---

## Success Threshold Definitions

These are the thresholds that define "Phase 1 is working" vs. "Phase 1 needs adjustment."

**Email open rate: target greater than 25%**
- Meaning: More than 1 in 4 recipients is opening the email. This is the baseline for a well-targeted, well-subject-lined cold outreach to a professional audience.
- If below 25%: The subject lines may be too generic, too long, or not sufficiently relevant to the recipient's current work. Re-examine the three subject line variants per template and test a different variant in the next wave.
- If above 40%: The outreach is performing strongly; the contact list is well-targeted and the subject lines are landing.

**Meeting conversion: target greater than 5%**
- Meaning: At least 1 in 20 email contacts agrees to a call or meeting.
- At 25 Tier 1 contacts, 5% = 1-2 meetings. This is the minimum floor.
- Target: 10-15% = 2-4 meetings from the 25-contact Phase 1 list.
- If below 5%: The outreach is generating interest but not action. Consider whether the CTA is unclear, whether the meeting request is calibrated to the right ask (some contacts will prefer an email exchange to a call), or whether the opening paragraph is not sufficiently personalized.

**Substack subscriber growth: target greater than 50/week**
- Weeks 1-2: 100+ (launch spike expected from post 1 share momentum)
- Weeks 3-6: 50+ (sustained growth from series publication and cross-platform amplification)
- Weeks 7-8: 30+ (consolidation)
- If below 30/week after Week 3: Cross-platform amplification is underperforming. Identify which platform is driving the most subscribers (Substack referral sources) and invest more effort there.

**Reddit upvote ratio: target above 80%**
- Meaning: Posts that land below 80% upvote ratio are encountering significant negative engagement — either the community finds them off-topic, promotional, or politically disagreeable.
- If below 80%: Review the post for framing that reads as advocacy or self-promotion. Adjust the next post's opening to be more analytical and less prescriptive.

**Tier 1 citation production (60-day target): 2+ external citations**
- Meaning: At least two Tier 1 contacts publicly cite, share, or incorporate the framework within 60 days of distribution
- If zero citations by Day 45: The follow-up sequence should be deployed; consider whether the framework is reaching the right people or whether a different angle (a one-page domain brief rather than the full document) would be more effective.

---

## Weekly Check-In Template

Run this check-in every Sunday during the 8-week launch window. It takes approximately 30 minutes.

**Email outreach review:**
1. How many emails sent this week? (Target: Wave 1 complete by Week 1, Wave 2 by Week 2, Wave 3 by Week 3)
2. Response rate so far: \_\_\_ responses / \_\_\_ sent = \_\_\_%
3. Any SR (substantive response) or MTG (meeting request) codes logged this week?
4. Any contacts still in NR status after 14+ days? List them — consider follow-up.
5. Any warm introductions provided? Log in Column V.

**Substack review:**
1. Posts published this week: \_\_\_
2. New subscribers this week: \_\_\_ (target: 50+)
3. Open rate for each post: \_\_\_% (target: 25%+)
4. Top referral source this week: \_\_\_
5. Any notable comments from institutional contacts?

**Reddit review:**
1. Posts published this week: \_\_\_ subreddit(s)
2. Upvote count and ratio at 72h for each post: \_\_\_
3. New Substack subscribers attributable to Reddit: \_\_\_
4. Any crossposting or notable practitioner comments?

**Citation and media monitoring:**
1. Any mentions of the framework in news, blog posts, academic papers, or social media from non-direct contacts?
2. Any legislative or litigation activity that references the framework's analysis?

**Decision points for this week:**
- Does Phase 1 outreach stay on schedule, or does any wave need adjustment?
- Does any domain need updating based on practitioner feedback?
- Does the Substack publication schedule stay on track?
- Is there a flag condition (see below) that needs to be escalated?

**Flag conditions** (escalate to CHECKIN.md if any of these occur):
- A Tier 1 contact provides a substantive objection to a specific factual claim — the claim needs to be reviewed before further distribution
- A response indicates the framework is being mischaracterized in a way that could damage future distribution (e.g., being described as a specific organization's product when it is independent research)
- A media outlet requests an interview or comment — this is positive, but requires a response strategy
- A hostile contact or organization publicly attacks the framework's accuracy — requires a documented response
- A legislative event (bill introduction, committee hearing, court ruling) directly overlaps with a domain claim — update the domain and send a follow-up to relevant contacts
