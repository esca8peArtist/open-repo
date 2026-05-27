---
title: "Track B Launch Day Success Signal Checkpoints"
date: 2026-05-30
version: 1.0
status: production-ready
purpose: "6-hour monitoring framework with explicit success thresholds at each hour. Determines when to escalate vs. continue. Go/no-go decision at Hour 6."
---

# Track B Launch Day Success Signal Checkpoints
## 6-Hour Monitoring Framework — May 30 08:00–14:00 UTC

**How to use this document**: Refer to this at the END of each hour (09:00, 10:00, 11:00, 12:00, 13:00, 14:00 UTC). Record metrics. Compare against thresholds. Determine: Continue (all metrics green) or Escalate (metric below threshold). At Hour 6, make final go/no-go decision.

**Key principle**: Metrics below threshold do NOT automatically mean launch failed. They mean "investigate further" (via Decision Trees) or "proceed with awareness." Only after Hour 6 do you make a final success/failure determination.

---

## HOUR 0–1 CHECKPOINT (08:00–09:00 UTC)

**Activities during this hour**:
- Pre-launch verification (Gist, Kit, Etsy, social posts)
- Email influencer outreach begins

**Metrics to record at 09:00 UTC**:

| Metric | Target | Yellow (Investigate) | Red (Escalate) |
|--------|--------|----------------------|-----------------|
| Gist URL accessibility | Working in incognito | Working but with lag | 404 / not accessible |
| Kit broadcast "Scheduled" status | Confirmed | Confirmed but delayed | Still shows Draft |
| Etsy listings in Draft | All 21 confirmed | 18+ confirmed | <18 confirmed |
| Instagram bio link correct | Gist URL confirmed | Working but old URL | Placeholder URL |
| Social posts "Scheduled" in Buffer | IG, TT, Pinterest all scheduled | 2 of 3 platforms scheduled | <2 platforms scheduled |
| Baseline metrics recorded | All recorded (Etsy, Kit, IG, TK, Pinterest) | Most recorded | None recorded |

**Success Signal for Hour 0–1**:
- All 6 metrics show GREEN or YELLOW
- Zero REDS
- **Action**: Proceed to Hour 2

**Escalation Trigger for Hour 0–1**:
- Any 1 metric shows RED
- **Action**: Investigate using Common Issues Decision Tree > resolve within 15 minutes > record in WORKLOG > proceed to Hour 2

**Recording Template**:
```
HOUR 0–1 CHECKPOINT — 09:00 UTC

Gist URL:                    [WORKING / ISSUE: ___]
Kit broadcast status:        [SCHEDULED / ISSUE: ___]
Etsy listings confirmed:     [21 / 18 / <18]
Instagram bio link:          [GIST URL / PLACEHOLDER]
Social platforms scheduled:  [3/3 / 2/3 / <2/3]
Baseline metrics:            [ALL / SOME / NONE]

Overall status:              [GREEN / YELLOW / RED]
Actions taken:               [NONE / Describe corrections]
```

---

## HOUR 1–2 CHECKPOINT (09:00–10:00 UTC)

**Activities during this hour**:
- Social media posts are live (Instagram 08:30, TikTok 08:45, Pinterest 09:00)
- Email influencer outreach complete
- First 30 minutes of engagement beginning

**Metrics to record at 10:00 UTC**:

| Metric | Target | Yellow (Investigate) | Red (Escalate) |
|--------|--------|----------------------|-----------------|
| Instagram post visible | Post appears in feed within 2 min of 08:30 | Post visible but no caption | Post missing / error |
| TikTok video live | Video visible in profile, >0 views | Video visible, 0 views | Video not posted / deleted |
| Pinterest pins live | 3+ pins visible on board | 1–2 pins visible | 0 pins visible |
| Reddit post visible | Post on r/herbalism, >0 upvotes | Post visible, 0 upvotes | Post removed / missing |
| Email influencer outreach sent | 3–8 Tier 1 contacts reached | 1–2 contacts reached | 0 contacts reached |
| Platform connection status | All 3 connected (green in Buffer) | 2 connected | <2 connected |

**Success Signal for Hour 1–2**:
- 5 of 6 metrics GREEN
- 1 metric may be YELLOW (early engagement is slow)
- Zero REDS
- **Action**: Proceed to Hour 3

**Escalation Trigger for Hour 1–2**:
- 2+ metrics RED
- Example: Instagram post missing AND TikTok video not posted AND Reddit post removed = 3 RED = escalate
- **Action**: Investigate each RED metric using Common Issues Decision Tree > resolve within 15 minutes > document > proceed to Hour 3

**Recording Template**:
```
HOUR 1–2 CHECKPOINT — 10:00 UTC

Instagram post:        [LIVE / MISSING / ERROR: ___]
TikTok video:          [LIVE, ___ views / MISSING / 0 VIEWS]
Pinterest pins:        [___ of 3 live / MISSING]
Reddit post:           [LIVE, ___ upvotes / REMOVED / 0 UPVOTES]
Email outreach:        [___ contacts sent / INCOMPLETE]
Platform connections:  [___ of 3 green]

Overall status:        [GREEN / YELLOW / RED]
Actions taken:         [NONE / Describe corrections]
```

---

## HOUR 2–3 CHECKPOINT (10:00–11:00 UTC)

**Activities during this hour**:
- First engagement check: upvotes, impressions, views visible
- Influencer email responses begin arriving
- Monitoring and response to social comments

**Metrics to record at 11:00 UTC**:

| Metric | Target | Yellow (Investigate) | Red (Escalate) |
|--------|--------|----------------------|-----------------|
| Instagram impressions (1 hr) | 20+ impressions | 10–19 impressions | <10 impressions |
| TikTok views (1 hr) | 30+ views | 15–29 views | <15 views |
| Reddit upvotes (1 hr) | 5+ upvotes | 2–4 upvotes | 0 upvotes |
| Email influencer responses | 1+ positive reply received | Replies still coming | 0 replies yet |
| Social post errors | No errors, no removals | Minor text error | Post removed / flagged |
| Any buyer DMs | Not expected yet, but 0 is normal | — | — |

**Success Signal for Hour 2–3**:
- All 4 main metrics (IG, TT, Reddit, Influencer) show GREEN or YELLOW
- Zero REDS on post health
- **Action**: Proceed to Hour 4

**Escalation Trigger for Hour 2–3**:
- 2+ metrics below target (YELLOW or RED)
- Example: IG <10 impressions AND Reddit 0 upvotes AND no influencer response = possible algorithmic suppression
- **Action**: Investigate platform-specific issue (shadowban, spam filter, etc.) using Common Issues Decision Tree > proceed to Hour 4 regardless (can't fix algo suppression in real-time) > continue monitoring

**Interpretation notes**:
- New Instagram accounts typically see 10–20 impressions on first posts (normal)
- TikTok's "For You" algorithm is slow on Day 1 for new accounts (expect <50 views on first 6 hours, normal)
- Reddit upvotes are slow until early responders engage (0 upvotes at 1 hour is normal; check again at Hour 3)
- Influencer responses may trickle in over 24 hours (do not expect all at Hour 2)

**Recording Template**:
```
HOUR 2–3 CHECKPOINT — 11:00 UTC

Instagram impressions:    [___ / target: 20+ / status: GREEN / YELLOW / RED]
TikTok views:             [___ / target: 30+ / status: GREEN / YELLOW / RED]
Reddit upvotes:           [___ / target: 5+ / status: GREEN / YELLOW / RED]
Email influencer replies: [___ received / status: GREEN / YELLOW / RED]
Post errors:              [NONE / MINOR ERROR / FLAGGED / REMOVED]
Buyer DMs:                [___ received]

Overall status:           [GREEN / YELLOW / RED]
Actions taken:            [NONE / Describe]
Next checkpoint:          Hour 4 (12:00 UTC)
```

---

## HOUR 3–4 CHECKPOINT (11:00–12:00 UTC)

**Activities during this hour**:
- Final verification before email broadcast sends
- Continued social media monitoring
- Influencer outreach responses continuing

**Metrics to record at 12:00 UTC** (just before email sends):

| Metric | Target | Yellow | Red |
|--------|--------|--------|-----|
| Kit broadcast status | "Scheduled" for 12:00 UTC | "Draft" | "Scheduled" for wrong time |
| Email test send | Test email received cleanly | Test email in Spam | Test email not delivered |
| Email subject finalized | Confirmed final, not placeholder | Minor text issue | Placeholder text |
| Social engagement trend | Upvotes/views increasing | Flat (no growth) | Decreasing |
| Influencer response count | 2+ responded | 1 responded | 0 responded |
| Platform outages | No outages reported | Minor slowness | Major platform down |

**Success Signal for Hour 3–4**:
- Kit broadcast shows "Scheduled" for 12:00 UTC (confirmed)
- Email test send succeeds
- 5 of 6 metrics GREEN
- **Action**: Proceed to Hour 5 (email broadcast send)

**Escalation Trigger for Hour 3–4**:
- Kit broadcast shows "Draft" instead of "Scheduled"
- Email test did not deliver
- Major platform outage detected
- **Action**: Fix immediately (resolve Kit scheduling issue, troubleshoot email delivery, monitor platform status) > proceed to Hour 5 once resolved > document all actions

**Recording Template**:
```
HOUR 3–4 CHECKPOINT — 12:00 UTC (Pre-Email-Send)

Kit broadcast status:         [SCHEDULED / DRAFT / WRONG TIME]
Email test send:              [SUCCESS / SPAM / NOT DELIVERED]
Email subject:                [FINAL / PLACEHOLDER]
Social engagement trend:       [INCREASING / FLAT / DECREASING]
Influencer responses:          [___ received / status: GREEN / YELLOW / RED]
Platform status:              [ALL OK / SLOWNESS / MAJOR OUTAGE]

Kit broadcast ready to send?  [YES / NO — describe issue]
Overall status:               [GREEN / YELLOW / RED]
Actions taken:                [NONE / Describe corrections]
```

---

## HOUR 4–5 CHECKPOINT (12:00–13:00 UTC)

**Activities during this hour**:
- Email broadcast SENDS at 12:00 UTC
- Email delivery, open rate, click rate begin appearing
- Monitor for Etsy orders from email traffic
- Social engagement continues

**Metrics to record at 13:00 UTC** (1 hour after email send):

| Metric | Target | Yellow | Red |
|--------|--------|--------|-----|
| Email delivery rate | >90% delivered | 80–90% delivered | <80% delivered |
| Email bounce rate | <2% | 2–5% | >5% |
| Email open rate (1 hr) | 15%+ | 5–14% | <5% |
| Email click rate (1 hr) | 3%+ | 1–2% | <1% |
| Etsy orders received | 1–3 orders | 0 orders | — (not concerning yet) |
| Etsy shop views | 30%+ above baseline | 0–30% above | Negative (views decreased) |

**Success Signal for Hour 4–5**:
- Email delivery >90%
- Email bounce <2%
- Email open rate >15% at 1 hour (strong signal)
- Email click rate >3%
- **Action**: Proceed to Hour 6 (final checkpoint)

**Escalation Trigger for Hour 4–5**:
- Email delivery <80% (delivery/auth issue)
- Email bounce >5% (list quality or auth problem)
- Email open rate <5% (subject line or deliverability issue)
- Email click rate <1% (CTA button broken or weak)
- **Action**: Investigate using Common Issues Decision Tree > log in WORKLOG > proceed to Hour 6 regardless (cannot fix email metrics in real-time)

**Interpretation notes**:
- Email open rate can be inflated by Apple Mail Privacy Protection (users' mail servers opening emails automatically). Real engaged opens may be 20–30% vs. reported 40%+.
- Email click rate is more reliable than open rate for measuring true engagement
- Zero orders at 1 hour post-send is normal; orders typically trickle in Hours 2–6
- Etsy shop views spike typically lags email open rate by 15–30 minutes

**Recording Template**:
```
HOUR 4–5 CHECKPOINT — 13:00 UTC (1 Hour After Email Send)

Email delivery:               [___% / target: >90% / status: GREEN / YELLOW / RED]
Email bounce rate:            [___% / target: <2% / status: GREEN / YELLOW / RED]
Email open rate (1 hr):       [___% / target: 15%+ / status: GREEN / YELLOW / RED]
Email click rate (1 hr):      [___% / target: 3%+ / status: GREEN / YELLOW / RED]
Etsy orders:                  [___ received]
Etsy shop views:              [___ today (compare to baseline: ___)]

Social metrics at 1 hr:
  Reddit upvotes:             [___]
  Instagram impressions:      [___]
  TikTok views:               [___]

Overall email performance:    [GREEN / YELLOW / RED]
Overall social performance:   [GREEN / YELLOW / RED]
Actions taken:                [NONE / Describe]
```

---

## HOUR 5–6 CHECKPOINT (13:00–14:00 UTC)

**Activities during this hour**:
- Final metrics collection
- Email open rate and click rate finalization (6 hours post-send)
- Social engagement continues
- Final go/no-go success determination

**Metrics to record at 14:00 UTC** (6 hours after email send, END OF LAUNCH WINDOW):

| Metric | Target | Yellow | Red |
|--------|--------|--------|-----|
| Email open rate (6 hrs) | 30%+ | 20–29% | <20% |
| Email click rate (6 hrs) | 8%+ | 5–7% | <5% |
| Etsy orders (cumulative) | 2–5 orders | 1 order | 0 orders |
| Reddit post engagement | 10+ upvotes | 5–9 upvotes | <5 upvotes |
| Instagram reach (6 hrs) | 100+ impressions | 50–99 | <50 |
| TikTok views (6 hrs) | 100+ views | 50–99 views | <50 views |
| Total followers gained | 3–5 new followers across platforms | 1–2 followers | 0 followers |
| Influencer shares | 1+ influencer shared publicly | 0 shares but responses | 0 responses, no shares |

---

### FINAL GO/NO-GO DECISION (At 14:00 UTC)

**Count green metrics**: How many of 8 metrics are GREEN (at or above target)?

| Green Count | Decision | Reason | Next Action |
|-------------|----------|--------|-------------|
| 7–8 green | **GO** | Launch successful across all channels | Proceed to Day 1 monitoring (May 31) |
| 5–6 green | **GO with Adjustments** | Strong performance but some channels underperforming | Proceed to Day 1; adjust Day 2 content per below |
| 3–4 green | **PROCEED** | Mixed results; some channels working | Document findings; proceed; prepare contingency adjustments for Day 3 |
| <3 green | **CONDITIONAL** | Multiple channels underperforming | Proceed but activate escalation procedures on Day 3 |

---

### Success Threshold Interpretation

**What "SUCCESS" means at Hour 6**:

1. **Email delivery and engagement good** (delivery >90%, open >20%, click >5%)
   - Indicates: Email list is healthy, subject line resonated, CTA is compelling
   - Implication: Email channel is the strongest distribution lever; use it again Days 2–3

2. **Etsy orders received** (1+ order by Hour 6)
   - Indicates: Product is compelling, pricing is acceptable, purchase path works
   - Implication: Email → Etsy conversion is functioning; not an accident

3. **Social engagement visible** (IG 50+ impressions, TT 50+ views, Reddit 5+ upvotes)
   - Indicates: Content resonates with audience; algorithm is not suppressing
   - Implication: Social channel is contributing; continue posting to same cadence

4. **Influencer responses** (1+ responded, 0 public shares yet is normal)
   - Indicates: Pre-launch outreach worked; influencers are aware
   - Implication: Track Day 3–7 for actual shares (takes time for influencers to incorporate into newsletters/posts)

**What "BELOW TARGET" means (but is NOT a failure)**:

- Email open <20%: Not unusual for first launch. Subject line weak? Test different angle on Day 2.
- Etsy orders = 0 at Hour 6: Email opens lag behind send. Orders typically arrive Hours 2–6 post-email. Check again at Hour 8 (16:00 UTC).
- Social engagement <50: Expected for new accounts. Algorithm visibility improves Days 2–3 as engagement builds.
- No influencer responses yet: Normal. Most responses come 24–48 hours after outreach. Check Day 2.

---

### Day 3 Escalation Decision (June 2, Day 3)

Use THESE thresholds at Hour 6 to determine if Day 3 escalation is needed:

**If cumulative by Hour 6**:
- Email open rate <15% AND click rate <3%: Prepare Day 3 contingency (revise email copy, send follow-up with different angle)
- Etsy orders still = 0 by Hour 6: Check email spam folder; verify landing page links; consider paid promotion on Day 3
- Social engagement <30 total (IG + TT + Reddit combined impressions/views/upvotes): Prepare Reddit repost with image format on Day 3

---

## Recording Template — Full Hour 6 Summary

```
═══════════════════════════════════════════════════════════════════
HOUR 5–6 CHECKPOINT — 14:00 UTC (6 Hours After Email Send — FINAL)
═══════════════════════════════════════════════════════════════════

EMAIL METRICS
  Delivery rate:               ___% (target: >90%) [GREEN / YELLOW / RED]
  Bounce rate:                 ___% (target: <2%) [GREEN / YELLOW / RED]
  Open rate (6 hrs):           ___% (target: 30%+) [GREEN / YELLOW / RED]
  Click rate (6 hrs):          ___% (target: 8%+) [GREEN / YELLOW / RED]
  Unsubscribe rate:            ___% (watch if >0.5%)

SALES METRICS
  Etsy orders:                 ___ (target: 2–5)
  Etsy shop views:             ___ today
  Average order value:         $___

SOCIAL METRICS
  Reddit upvotes:              ___ (target: 10+)
  Instagram impressions:       ___ (target: 100+)
  TikTok views:                ___ (target: 100+)
  Pinterest saves:             ___ (expected: low Day 1)
  Total followers gained:      ___ (target: 3+)

INFLUENCER METRICS
  Tier 1 contacts responded:   ___ of [X] (expected: 20–30%)
  Public shares received:      ___ (expected: 0–1 Day 1, grows Day 2+)

OVERALL LAUNCH STATUS
  Green metrics:               ___ of 8 (see decision matrix above)
  DECISION:                    [GO / GO WITH ADJUSTMENTS / PROCEED / CONDITIONAL]
  
IF NOT FULLY GREEN, DIAGNOSE:
  [ ] Email: Low open? Check subject line. Low click? Check CTA button.
  [ ] Sales: 0 orders? Check email spam folder. Check Etsy listing visibility.
  [ ] Social: Low engagement? Check platform algorithm (new account = expected). Check for flags.
  [ ] Influencers: No response? 24–48 hour lag is normal. Check Day 2.

DAY 3 CONTINGENCY TRIGGERS (if below threshold):
  [ ] Email open <15%: Prepare revised follow-up email for Day 2
  [ ] Email click <3%: Review CTA button design / copy
  [ ] Etsy orders = 0: Prepare paid promo test for Day 3 ($20–50 budget)
  [ ] Social engagement <30: Prepare Reddit repost (image format) for Day 3
  [ ] No influencer responses by Day 3: Send one gentle follow-up (Day 3 only)

WORKLOG NOTES
  Any issues encountered:      [Describe]
  Manual interventions taken:  [Describe]
  Lessons for Day 2 content:   [Describe]
  Next checkpoint:             June 2, 08:00 UTC (Day 3 threshold decision)
```

---

## Quick Reference — Green / Yellow / Red Summary

**LAUNCH SUCCESSFUL (GREEN)**
- Email: delivery >90%, bounce <2%, open >30%, click >8%
- Sales: 2–5 orders by Hour 6
- Social: Reddit 10+, IG 100+, TT 100+ by Hour 6
- Influencers: 1+ responded by Hour 6
- Overall: 7+ of 8 metrics GREEN

**LAUNCH STRONG BUT NEEDS MONITORING (YELLOW)**
- Email: delivery 80–90%, bounce 2–5%, open 20–29%, click 5–7%
- Sales: 1 order by Hour 6
- Social: 50–99 engagement on each platform
- Influencers: 0 responses yet (normal, 24–48 hour lag)
- Overall: 5–6 of 8 metrics GREEN

**LAUNCH PROCEEDING WITH AWARENESS (YELLOW-RED MIXED)**
- Email: below targets but not critical
- Sales: 0 orders yet (can arrive Hours 6–12)
- Social: very low engagement (< 50 on new accounts is expected)
- Influencers: no responses yet (normal)
- Overall: 3–4 of 8 metrics GREEN

**LAUNCH REQUIRES ESCALATION (RED)**
- Email: delivery <80%, bounce >5%, or zero opens/clicks
- Sales: may follow, but email problem indicates deeper issue
- Social: no engagement across any platform (possible algorithmic suppression or spam flag)
- Influencers: zero responses AND zero social engagement together
- Overall: <3 of 8 metrics GREEN
- Action: Investigate via Common Issues Decision Trees; prepare Day 3 contingencies

---

*Document status: Production-ready. May 30, 2026.*
*Use this to monitor progress and determine success/escalation at each hour.*
*Final decision gate: 14:00 UTC. All metrics recorded. Go/no-go logged in WORKLOG.md.*
