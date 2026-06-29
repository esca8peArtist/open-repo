---
title: "Phase 3 Week 1-2 Alert Thresholds — Automated Go/No-Go Gates"
date: 2026-06-29
version: 1.0
status: active
sprint-window: June 29 – July 13, 2026
cross-references:
  - PHASE_3_WEEK_1_2_DAILY_EXECUTION_CHECKLIST.md (where thresholds are checked)
  - PHASE_3_WEEK_1_2_VERIFICATION_TEMPLATES.md (measurement templates)
  - PHASE_3_LAUNCH_CONTINGENCY_ROUTING.md (contingency procedures)
  - PHASE_3_LAUNCH_MARKETING_CALENDAR.md (source expected ranges)
---

# Phase 3 Week 1-2 Alert Thresholds

**How to use**: Check each gate at the specified checkpoint time. All thresholds are numeric — no interpretation required. When a metric triggers a YELLOW or RED level, execute the listed response steps in order. Log all escalations in WORKLOG.md.

---

## GATE 1 — EMAIL DELIVERABILITY (Check at 10am ET, day of each send)

**Gate**: Email delivery rate at 1 hour post-send.

| Level | Threshold | Response |
|-------|-----------|----------|
| GREEN | Delivery rate >95% AND bounces <1% | No action. Continue monitoring. |
| YELLOW | Delivery rate 90-95% OR bounces 1-2% | Step 1: Check Kit account status for sending limit warnings. Step 2: Review bounce log — identify whether bounces are hard (invalid address) or soft (temporary). Step 3: Remove hard bounces from list before next send. No delay to next send required. |
| RED | Delivery rate <90% OR bounces >2% OR spam complaints >0.1% | Step 1: Pause any pending sends. Step 2: Log in to Kit support — check for account suspension or IP reputation flag. Step 3: If account suspended, contact Kit support immediately (support@kit.com). Do not send Email 2 until delivery issue resolved. Log in WORKLOG.md with timestamp. |

---

## GATE 2 — EMAIL OPEN RATE, WOMEN'S HEALTH (Check at 9am ET, Jun 30 — 24hr mark)

**Gate**: Open rate at 24 hours post-send for Email 1 (Women's Health, sent Jun 29).

| Level | Threshold | Response |
|-------|-----------|----------|
| GREEN | Open rate >22% | No action. Log final baseline. Proceed to Email 2 at standard 9am ET Jul 6. |
| YELLOW | Open rate 15-22% | Step 1: Check subject line — "Women's Health — An 8-week herbal series starts today" — compare against any prior campaigns for subject line performance. Step 2: Segment clickers (anyone who opened) for retargeting before Email 2. Step 3: Draft A/B subject line test for Email 2 (Respiratory). Option A: "Respiratory Health — Herbs for clear airways and strong immunity" (existing). Option B: "Why you're harvesting thyme at the wrong time" (curiosity hook). Pick based on list behavior. Log YELLOW in WORKLOG.md. |
| RED | Open rate <15% | Step 1: Check Kit deliverability log — is the email landing in spam folders? Step 2: Send a manual test of Email 1 to 5 different email providers (Gmail, Outlook, Yahoo, Apple Mail, Proton Mail) and check spam placement. Step 3: If spam placement confirmed: review email content for spam-trigger phrases (excessive caps, "FREE," excessive exclamation marks, or image-heavy HTML). Revise Email 2 to remove triggers before Jul 6 send. Log RED in WORKLOG.md. Consider delaying Email 2 by 24 hours if spam issue not resolved. |

**Note on 48-hour window**: Open rates continue to climb for 48 hours. Do not trigger YELLOW/RED response until the 24-hour check. If open rate is 20% at 24 hours and climbs to 23% at 48 hours, retroactively reclassify as GREEN. Decisions should reference 24-hour minimum, not preliminary 3-hour rates.

---

## GATE 3 — EMAIL OPEN RATE, RESPIRATORY HEALTH (Check at 9am ET, Jul 7 — 24hr mark)

**Gate**: Open rate at 24 hours post-send for Email 2 (Respiratory, sent Jul 6).

| Level | Threshold | Response |
|-------|-----------|----------|
| GREEN | Open rate >22% | No action. Log final baseline. Track cross-campaign delta vs. Email 1. |
| YELLOW | Open rate 15-22% | Same as Gate 2 YELLOW. Additionally: if Email 1 was also YELLOW, this is a pattern — the list may have deliverability or engagement issues that need to be resolved before Email 3 (Jul 13). Contact Kit support and review list health (unsubscribes, bounce accumulation, engagement scoring). |
| RED | Open rate <15% | Same as Gate 2 RED. Additionally: if both Email 1 and Email 2 are RED, the issue is structural (deliverability, list health, or content). Consider: (1) cleaning the list before Email 3, (2) testing a re-engagement sequence instead of Email 3, (3) consulting Kit deliverability documentation. Log RED in WORKLOG.md. Escalate if unable to diagnose within 24 hours. |

---

## GATE 4 — SOCIAL ENGAGEMENT ZERO-CHECK (Check at 8-hour mark for each post)

**Gate**: Any post showing zero engagement (0 likes, 0 comments) at 8 hours post-publish.

| Level | Threshold | Response |
|-------|-----------|----------|
| GREEN | Any engagement (1+ likes or comments at 8hrs) on each platform | No action. |
| YELLOW | 0 engagement on ONE platform for 3+ hours | Step 1: Confirm the post is actually live on that platform — view natively (not through scheduler). Step 2: If post is live but 0 engagement: check if the account has been throttled or shadow-restricted (new accounts or accounts with recent policy warnings may experience reduced reach). Step 3: Manually engage with the post yourself (like it, leave a comment) to signal to the algorithm that the account is active. Note: 0 engagement at 3 hours is normal for YouTube Shorts on new channels. Only trigger YELLOW for LinkedIn or Instagram zero at 3+ hours. |
| RED | 0 engagement on ALL platforms at 8 hours, OR post confirmed not live | Step 1: If not live — post manually immediately from `PHASE_3_WEEK_1_2_CONTENT_BLOCKS_READY_TO_SHIP.md`. Step 2: If live but no engagement on all platforms — account may be restricted. Check platform notifications and emails. Step 3: Log in WORKLOG.md. Switch to native posting (not scheduler) for remaining posts until root cause identified. |

---

## GATE 5 — CONTRACTOR PHOTO DELIVERY (Check at 5pm ET, Jul 5 — Session 1 due)

**Gate**: Photographer Session 1 delivery by 5pm ET, Saturday July 5.

| Level | Threshold | Response |
|-------|-----------|----------|
| GREEN | All 5 images received AND pass quality gate by 5pm ET Jul 5 | Send Template 3A (Praise Email). Schedule Milestone 2 payment for Jul 8 upon review approval. |
| YELLOW | Images received but 1-2 fail quality gate (reshoot needed) | Step 1: Send Template 3B (Course Correction) with specific reshoot items within 48 hours of receipt. Step 2: Set reshoot deadline for Jul 9 (3 business days). Step 3: Confirm whether failing images can be temporarily substituted with Wikimedia CC alternatives for the Jul 6 social launch — if yes, Respiratory launch proceeds on schedule. Log in WORKLOG.md. |
| RED | No images received by 5pm ET Jul 5, OR entire Session 1 fails quality gate | Step 1: Send follow-up message to photographer immediately: "Session 1 was due today. Please confirm status." Step 2: If no response by 9am ET Jul 6: activate Wikimedia CC image fallback for Respiratory bundle (per `PHASE_3_LAUNCH_CONTINGENCY_ROUTING.md`). Step 3: Respiratory launch (Jul 6) proceeds using fallback images. Photographer contract reviewed for breach clause. Log RED in WORKLOG.md. |

---

## GATE 6 — CONTRACTOR WRITER FIRST DRAFT (Check at 5pm ET, Jul 8)

**Gate**: Writer first draft (Respiratory bundle, 3,600 words) delivery by 5pm ET, Wednesday July 8.

| Level | Threshold | Response |
|-------|-----------|----------|
| GREEN | Draft received AND passes quality gate (word count, FTC pass, citations present) | Send Template 3A (Praise Email). Begin 48-hour review. Schedule Milestone 2 payment contingent on clean revision round. |
| YELLOW | Draft received with revision items (FTC issues, word count <10% under target, missing section) | Step 1: Send Template 3B (Course Correction) within 48 hours with specific, numbered revision items. Step 2: Set revision deadline for Jul 11 (3 days). Step 3: Confirm whether revision round can complete before Sleep & Nervines launch (Jul 13) — this is likely with a Jul 11 revision due date. Log in WORKLOG.md. |
| RED | No draft received by 5pm ET Jul 8, OR draft received with structural failure (under 2,500 words, no citations, missing FTC framing throughout) | Step 1: Send follow-up immediately: "Respiratory draft was due today. Please confirm status." Step 2: If no response by 9am ET Jul 9: assess solo fallback path per `PHASE_3_LAUNCH_CONTINGENCY_ROUTING.md` (PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md). Step 3: Determine whether Respiratory bundle content can be completed using existing draft notes + self-written sections. Step 4: Log RED in WORKLOG.md. Consider contract review for non-delivery. |

---

## GATE 7 — WEEK 1 COMBINED GO/NO-GO (Check EOD Jul 10 — end of Week 1)

**Gate**: Three combined signals must show viability for Week 2 normal pacing.

### Signal 1: Email Performance

| Metric | GREEN | YELLOW | RED |
|--------|-------|--------|-----|
| Combined opens (Email 1 + Email 2) | >250 total opens | 150-250 total opens | <150 total opens |
| Minimum open rate (either email) | Both >22% | Either 15-22% | Either <15% |

### Signal 2: Social Performance

| Metric | GREEN | YELLOW | RED |
|--------|-------|--------|-----|
| Total combined engagements (all posts, all platforms) | >500 | 250-500 | <250 |
| Zero-engagement posts | None | 1-2 posts had 0 engagement | 3+ posts had 0 engagement |

### Signal 3: Contractor Performance

| Metric | GREEN | YELLOW | RED |
|--------|-------|--------|-----|
| Handoffs on schedule (of 4 primary: 6x onboarding, Session 1, writer draft) | 3 of 4+ | 2 of 4 | 1 or fewer of 4 |
| Any handoff completely missing (no delivery, no response) | None | — | 1+ missing |

### Week 2 Pacing Decision

| Combined Status | Decision |
|----------------|----------|
| All 3 GREEN | Proceed to Week 2 at normal pace. Sleep & Nervines launch Jul 13 confirmed. |
| Any 1 YELLOW | Review compressed timeline option: consider accelerating Sleep launch to Jul 12 if Etsy bundle is ready. Increase social post frequency by 1 additional post in Week 2. No other changes required. |
| Any 1 RED | Log in WORKLOG.md. Contact `PHASE_3_LAUNCH_CONTINGENCY_ROUTING.md` decision tree. Email-specific RED: consider 24-hour delay on Email 3 and re-test. Contractor-specific RED: activate solo fallback for affected bundle. |
| Multiple RED | Escalate immediately. Review whether Q3 launch timeline is achievable at original scope. Consider scope reduction (3 bundles instead of 5 in Q3 sprint) per `PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md`. Log in WORKLOG.md with full context. |

---

## GATE 8 — WEEK 2 COMBINED GO/NO-GO (Check EOD Jul 13)

Run the same three-signal gate as Gate 7 with Week 2 actuals.

**Week 2 email performance**:
- Email 2 (Respiratory) 24hr open rate: _____ % (>22% = GREEN)
- Email 3 (Sleep & Nervines) 24hr open rate: _____ % (>22% = GREEN; check at 9am Jul 14)
- Combined Week 1-2 total opens: _____ (>500 cumulative = GREEN)

**Week 2 social performance**:
- Posts 6-9 combined engagements: _____ (>300 for Week 2 posts = GREEN)
- Any zero-engagement posts: [ ] None [ ] _____ posts (>1 = YELLOW)

**Week 2 contractor performance**:
- Session 2 received (due Jul 12): [ ] Yes [ ] No
- Writer revision/draft complete (Respiratory approved): [ ] Yes [ ] No
- Week 3 (Sleep) contractor handoff: on track for Jul 13 launch: [ ] Yes [ ] No

**Week 3 pacing decision** (record result):
- Status: [ ] All GREEN — normal pace [ ] YELLOW — review adjustments [ ] RED — escalate
- Decision logged in WORKLOG.md: [ ] Yes

---

## REFERENCE: THRESHOLD SUMMARY TABLE

| Gate | Checkpoint | GREEN Floor | YELLOW Range | RED Ceiling |
|------|-----------|-------------|-------------|-------------|
| 1 — Email deliverability | 10am ET, send day | >95% delivery | 90-95% | <90% |
| 2 — Women's Health open rate | 9am ET, Jun 30 | >22% | 15-22% | <15% |
| 3 — Respiratory open rate | 9am ET, Jul 7 | >22% | 15-22% | <15% |
| 4 — Social zero-check | 8hr mark per post | Any engagement | 0 on 1 platform, 3hr | 0 on all platforms, 8hr |
| 5 — Photo Session 1 delivery | 5pm ET, Jul 5 | 5 images, pass gate | Images with reshoot needed | Not received OR full failure |
| 6 — Writer first draft | 5pm ET, Jul 8 | Received + pass gate | Received with revisions | Not received OR structural failure |
| 7 — Week 1 combined | EOD Jul 10 | All 3 signal GREEN | Any signal YELLOW | Any signal RED |
| 8 — Week 2 combined | EOD Jul 13 | All 3 signal GREEN | Any signal YELLOW | Any signal RED |

---

## ESCALATION LOG TEMPLATE (Copy into WORKLOG.md when any YELLOW or RED fires)

```
DATE: [DATE]
TIME: [TIME ET]
GATE: [Gate number and name]
LEVEL: [ ] YELLOW [ ] RED
METRIC: [Exact metric and value — e.g., "Email 1 open rate: 14.2% at 24hr"]
THRESHOLD CROSSED: [e.g., "<15% triggers RED"]
STEPS TAKEN:
  1. [Action taken]
  2. [Action taken]
  3. [Action taken, or "pending"]
RESOLUTION: [ ] Resolved — [describe] [ ] Pending [ ] Escalated to contingency
IMPACT ON SCHEDULE: [ ] None [ ] [Describe impact]
```

---

*Prepared: June 29, 2026. All thresholds calibrated against PHASE_3_LAUNCH_MARKETING_CALENDAR.md expected ranges. Email targets (22-28% open) are based on engaged-list baseline for a niche product launch. Social engagement targets are conservative Week 1-2 baselines for first-launch algorithm build. Contractor gates are hard deadlines derived from PHASE_3_CRITICAL_PATH_ANALYSIS_JUNE22_JULY13.md.*
