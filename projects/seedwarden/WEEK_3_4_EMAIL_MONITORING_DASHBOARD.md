---
title: "Seedwarden Week 3-4 Email Monitoring Dashboard"
date: 2026-06-29
version: 1.0
status: production-ready
scope: "Jul 13 – Aug 3 (Sleep & Nervines + Immunity launches). Supersedes Week 1-2 baseline thresholds with Week 1-2 actuals."
cross-references:
  - SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md (Week 1-2 procedures)
  - PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md (escalation decision trees)
  - WEEK_3_4_CONTINGENCY_INCIDENT_PLAYBOOKS.md (incident response)
  - PHASE_3_EXECUTION_LOG.md (metric recording)
---

# Seedwarden Week 3-4 Email Monitoring Dashboard

**Sprint window**: July 13 – August 3, 2026  
**Emails in scope**: Email 3 (Sleep & Nervines, July 13) + Email 4 (Immunity Support, July 20) + Email 5 (Digestive Support, August 3)  
**Baseline**: Week 1-2 actuals replace Q2 construction-audience estimates from June 29 setup

---

## SECTION 1: THRESHOLD DEFINITIONS

### Week 3-4 Adjusted Thresholds

Week 1-2 data from June 29 – July 12 now provides Seedwarden-specific baselines. Populate after Email 2 (July 6) data closes.

**UPDATE THIS TABLE by July 8 (after Email 2 data is 48h final):**

| Metric | Q2 Estimate (Baseline) | Email 1 Actual | Email 2 Actual | Week 3-4 Adjusted | Notes |
|--------|----------------------|----------------|----------------|-------------------|-------|
| Open Rate (GREEN) | >22% | [FILL] | [FILL] | [FILL after wk 1-2] | Use lower of Email 1/2 as floor |
| Open Rate (YELLOW) | 15–22% | — | — | [FILL] | |
| Open Rate (RED) | <15% | — | — | <15% | Hard floor regardless of actuals |
| Click Rate (GREEN) | >3% | [FILL] | [FILL] | [FILL after wk 1-2] | |
| Click Rate (YELLOW) | 1–3% | — | — | [FILL] | |
| Click Rate (RED) | <1% | — | — | <1% | |
| Unsubscribe Rate (RED) | >0.5% | [FILL] | [FILL] | >0.5% | Holds regardless of list size |
| Delivery Rate (RED) | <90% | [FILL] | [FILL] | <90% | |
| Fatigue Signal (Email 3) | Email 3 < 15% | — | — | Email 3 <15% | Triggers re-engagement campaign |

**Adjustment rule**: If Email 1 AND Email 2 both exceeded GREEN threshold by 5+ points, raise GREEN threshold by 3 points for Emails 3–5. Example: if both returned 28%+ opens, set Email 3 GREEN floor to 25% (not 22%).

---

## SECTION 2: EMAIL SEND SCHEDULE — WEEKS 3-4

| Email # | Bundle | Target Send | Kit.com Name | Subject Line | CTA | List Size Estimate |
|---------|--------|-------------|-------------|--------------|-----|-------------------|
| 3 | Sleep & Nervines | Jul 13, 09:00 ET (13:00 UTC) | Sleep & Nervines Launch — Jul 13 | "Sleep & Nervines — The herbal foundation for deep rest" | Get the Sleep Guide | [Email 2 list count + new subscribers Jul 6-12] |
| 4 | Immunity Support | Jul 20, 09:00 ET (13:00 UTC) | Immunity Support Launch — Jul 20 | [Subject TBD; adjust based on Email 3 A/B results] | Get the Immunity Guide | [Email 3 list count + new subscribers Jul 13-19] |
| 5 | Digestive Support | Aug 3, 09:00 ET (13:00 UTC) | Digestive Support Launch — Aug 3 | [Subject TBD; adjust based on Email 4 performance] | Get the Digestive Guide | [Email 4 list count + new subscribers Jul 20-Aug 2] |

**Note**: Email 4 may shift to Jul 27 if Email 3 triggers fatigue protocol (open rate <15% at T+24hr). Update this table if date shifts.

---

## SECTION 3: DAILY TRACKING TEMPLATE — WEEKS 3-4

### Email 3: Sleep & Nervines (Launch Jul 13)

#### Pre-Send Verification (Jul 12, 5pm ET)

- [ ] Kit.com campaign created: "Sleep & Nervines Launch — Jul 13"
- [ ] Subject line loaded: "Sleep & Nervines — The herbal foundation for deep rest"
- [ ] Preview text loaded (differs from subject, sets context — 40–50 chars)
- [ ] Etsy Sleep bundle link verified: live URL, not draft, loads in <3 seconds on mobile
- [ ] Bundle cover image loads in email preview
- [ ] Unsubscribe link visible and functional in footer
- [ ] Recipient list count logged: [NUMBER] (compare to Email 2 count; alert if <95% of Email 2 count due to unusual unsub spike)
- [ ] Send time confirmed: 09:00 ET (13:00 UTC) July 13
- [ ] Test email sent to personal inbox: subject, image, CTA link, unsubscribe all verified
- [ ] A/B subject line configured (if Email 2 was YELLOW): Version A + Version B in Kit scheduler

#### T+1 Hour Check (Jul 13, 14:00 UTC)

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| Delivery Rate | >95% | [FILL] | GREEN/YELLOW/RED |
| Hard Bounces | <1% of sent | [FILL] | |
| Spam Complaints | <0.05% | [FILL] | |

**If RED**: Do not send Email 4 until delivery issue resolved. Execute WEEK_3_4_CONTINGENCY_INCIDENT_PLAYBOOKS.md Playbook 1.

#### T+24 Hour Check (Jul 14, 13:00 UTC)

| Metric | Email 1 Actual | Email 2 Actual | Email 3 Expected | Email 3 Actual | Status |
|--------|---------------|----------------|-----------------|----------------|--------|
| Open Rate | [FILL] | [FILL] | ≥(Email 2 - 3%) | [FILL] | |
| Click Rate | [FILL] | [FILL] | ≥(Email 2 click rate) | [FILL] | |
| Fatigue Signal | — | — | <15% = RED | [FILL] | |

**Fatigue assessment**: Email 3 is the critical fatigue checkpoint. Subscribers have received 2 launch emails in 15 days.

```
IF Email 3 open rate >20%:
  → No fatigue signal. Proceed with Email 4 on Jul 20 as planned.
  Log: GREEN, no change.

IF Email 3 open rate 15–20% (YELLOW):
  → Minor decline. Increase educational content in Email 4 body (80% educational / 20% promotional).
  Update Email 4 subject to curiosity-hook format.
  Log: YELLOW, Email 4 content adjustment noted.

IF Email 3 open rate <15% (RED):
  → Fatigue confirmed. Move Email 4 from Jul 20 to Jul 27 (+7 days).
  Send re-engagement email to cold segment (definition: no opens on Emails 1, 2, or 3).
  Log: RED, Email 4 delayed, re-engagement campaign activated.
```

#### T+48 Hour Final Baseline (Jul 15, 13:00 UTC)

| Metric | T+24 Rate | T+48 Final | Trend | Action |
|--------|-----------|------------|-------|--------|
| Open Rate | [FILL] | [FILL] | ↑/→/↓ | [FILL] |
| Click Rate | [FILL] | [FILL] | ↑/→/↓ | [FILL] |
| Unsubscribes | [COUNT] | [COUNT] | ↑/→/↓ | [FILL] |

**Log line for PHASE_3_EXECUTION_LOG.md**:
```
Jul 15 — Email 3 (Sleep & Nervines) 48hr Final
Open: ___% | Click: ___% | Delivery: ___% | Unsub: ___% | Fatigue: [YES/NO]
Status: [GREEN/YELLOW/RED] | Action: [None / Email 4 adjusted / Fatigue protocol activated]
```

---

### Email 4: Immunity Support (Target Jul 20; may shift to Jul 27 if fatigue)

#### Pre-Send Context (Fill before Jul 18)

- [ ] Fatigue decision made from Email 3: Send Jul 20 (no fatigue) or Jul 27 (fatigue detected)
- [ ] Email 4 subject line finalized based on Email 3 A/B winner
- [ ] Email 4 content ratio confirmed: standard 60/40 (no fatigue) or educational-heavy 80/20 (fatigue YELLOW)
- [ ] List size: [EMAIL 3 COUNT minus unsubscribes Jul 14-19]
- [ ] Re-engagement email sent (if fatigue RED from Email 3): cold segment targeted, separate campaign, measured separately

#### Pre-Send Verification (Day before send, 5pm ET)

Same checklist as Email 3 above. Fill CTA link with live Etsy Immunity bundle URL.

- [ ] Immunity bundle Etsy URL verified live (not Sleep bundle URL — common copy-paste error)
- [ ] If Email 3 fatigue was YELLOW: opening paragraph revised to 80% educational
- [ ] If Email 3 fatigue was RED: send date is Jul 27, not Jul 20 (confirm before scheduling)

#### T+24 Hour Check

| Metric | Email 3 Actual | Email 4 Expected | Email 4 Actual | Status |
|--------|---------------|-----------------|----------------|--------|
| Open Rate | [FILL] | ≥Email 3 (or ≥15% if fatigue adjusted) | [FILL] | |
| Click Rate | [FILL] | ≥Email 3 click rate | [FILL] | |
| Unsubscribes | [FILL] | <0.5%/day | [FILL] | |

**Log line**:
```
Email 4 (Immunity) 24hr check — [DATE]
Open: ___% | Click: ___% | Delivery: ___% | Unsub: ___%
Compared to Email 3: [better/same/worse by X%]
Status: [GREEN/YELLOW/RED] | Action: [None / Adjust Email 5 / Escalate]
```

---

### Email 5: Digestive Support (Aug 3)

#### Pre-Send Context (Fill before Aug 1)

- [ ] Email 4 data final (T+48 closed Jul 22 for Jul 20 send; Jul 29 for Jul 27 send)
- [ ] Email 5 subject line finalized based on Email 4 A/B winner or performance data
- [ ] Re-engagement email for cold segment (if not already sent): segment defined as no opens on any of Emails 1–4
- [ ] List size: [EMAIL 4 COUNT minus Jul 20-Aug 2 unsubscribes]

#### T+24 Hour Check (Aug 4, 13:00 UTC)

| Metric | Email 4 Actual | Email 5 Expected | Email 5 Actual | Status |
|--------|---------------|-----------------|----------------|--------|
| Open Rate | [FILL] | ≥Email 4 | [FILL] | |
| Click Rate | [FILL] | ≥Email 4 click rate | [FILL] | |
| Revenue signal | — | Etsy orders Aug 3-4 | [FILL] | |

---

## SECTION 4: ESCALATION TRIGGERS (WEEKS 3-4)

### Priority 1: Email 3 Fatigue Confirmed (<15% opens)

**What**: Subscribers have received 3 launch emails in 22 days (Jun 29, Jul 6, Jul 13). Open rate below 15% confirms fatigue.

**Response timeline**: Within 4 hours of T+24 check

**Immediate actions**:
1. Log RED in PHASE_3_EXECUTION_LOG.md
2. Move Email 4 send date from Jul 20 → Jul 27 in Kit.com scheduler
3. Define cold segment: Kit.com > Subscribers > filter "Did not open" > select Emails 1, 2, 3
4. Prep re-engagement email (see WEEK_3_4_CONTINGENCY_INCIDENT_PLAYBOOKS.md, Playbook 5)
5. Revise Email 4 subject to value-frame: "The elderberry question I get every fall (answered)"
6. Revise Email 4 opening to 80% educational / 20% promotional

**Escalation contact**: No external escalation needed (self-managed). Log decision in PHASE_3_EXECUTION_LOG.md with timestamp.

---

### Priority 2: Unsubscribe Rate >0.5% on Any Day

**What**: Daily unsub rate exceeds RED threshold.

**Response timeline**: Same-day investigation, within 2 hours

**Steps**:
1. Check email send correlation (was an email sent same-day or day-1?)
2. Pull unsubscribe reasons from Kit.com > Subscribers > Unsubscribes
3. Run list health check (unconfirmed >15%? cold >25%?)
4. Draft retention message (frequency adjustment or content relevance — see SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md templates)
5. Log RED in PHASE_3_EXECUTION_LOG.md

---

### Priority 3: Open Rate RED on Email 4 or 5 (<15%)

**What**: Fatigue not resolved after email gap extension, or new content issue.

**Steps**:
1. Run spam placement test (send to 5 test addresses: Gmail, Outlook, Yahoo, Apple, Proton)
2. If spam found: revise subject line and HTML before Email 5 send
3. If all inbox: list quality issue; segment cold subscribers and exclude from Email 5
4. Move Email 5 by additional 7 days if needed (to Aug 10)

---

### Priority 4: Delivery Rate <90%

**What**: Email platform issue, IP reputation problem, or sender authentication failure.

**Response**: Within 2 hours of T+1hr check

**Contact**: Kit.com support (support@kit.com) — include account email, campaign name, delivery rate actual, send date.

---

## SECTION 5: AGGREGATE PERFORMANCE TRACKER (WEEKS 1-4)

### Campaign Performance Comparison Table

Update this table after each email's T+48hr close.

| Email | Bundle | Send Date | List Size | Delivery % | Open % | Click % | Unsub % | Status | Notes |
|-------|--------|-----------|-----------|------------|--------|---------|---------|--------|-------|
| 1 | Women's Health | Jun 29 | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [G/Y/R] | Baseline |
| 2 | Respiratory | Jul 6 | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [G/Y/R] | |
| 3 | Sleep & Nervines | Jul 13 | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [G/Y/R] | Fatigue check |
| 4 | Immunity | Jul 20/27 | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [G/Y/R] | |
| 5 | Digestive | Aug 3 | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [G/Y/R] | |
| Re-eng | Cold segment | [If activated] | [FILL] | [FILL] | [FILL] | [FILL] | [FILL] | [G/Y/R] | Cold revival |

### Trend Analysis (Fill after each email)

```
Open Rate Trend:
Email 1: ___% → Email 2: ___% → Email 3: ___% → Email 4: ___% → Email 5: ___%
Trend line: [Stable / Declining / Recovering] by [X%] average per campaign

Click Rate Trend:
Email 1: ___% → Email 2: ___% → Email 3: ___% → Email 4: ___% → Email 5: ___%
Trend line: [Stable / Declining / Recovering]

Unsubscribe Accumulation:
Total lost: ___ subscribers (Email 1 list → Email 5 list delta)
Attrition rate: ___% of original list
New subscribers gained: ___ (offset from social/Etsy referral)
Net list change: [+/–] [COUNT]
```

### A/B Subject Line Record

| Email | Version A | Version B | A Open % | B Open % | Winner | Applied To |
|-------|-----------|-----------|----------|----------|--------|-----------|
| 3 | [FILL if A/B run] | [FILL] | [FILL] | [FILL] | [A/B] | Email 4 subject |
| 4 | [FILL] | [FILL] | [FILL] | [FILL] | [A/B] | Email 5 subject |

---

## SECTION 6: SUBJECT LINE DECISION MATRIX (WEEKS 3-4)

### Week 3 Email 3 (Sleep) — Subject Candidates

**Default (if Email 2 was GREEN)**: "Sleep & Nervines — The herbal foundation for deep rest"

**A/B Variant (if Email 2 was YELLOW)**: Test against curiosity-hook:
- Version B: "Why your sleep herbs aren't working (here's why)"
- Winner at T+24hr by ≥2% → use for Email 4 frame

**If Email 2 was RED**: Use value-frame only:
- "The 3-herb combination for falling asleep vs. staying asleep"

---

### Week 4 Email 4 (Immunity) — Subject Candidates

**Default (no fatigue)**: [TBD based on Email 3 A/B results]

**Curiosity-hook options**:
- "The elderberry question I get every fall (answered)"
- "Goldenseal is CITES-listed — here's why that matters for your immune routine"
- "Why your immunity routine fails in month 2 (3 herbs that fix it)"

**Educational-heavy (if fatigue YELLOW from Email 3)**:
- "The ashwagandha timing mistake most growers make"
- "Immune herbs don't work the way most people think"

---

## SECTION 7: QUICK-REFERENCE DAILY CHECKLIST (WEEKS 3-4)

### Email Send Days (Jul 13, Jul 20 or 27, Aug 3)

**Morning (8:00 AM ET)**:
- [ ] Verify Kit.com email is scheduled for 09:00 ET
- [ ] Confirm Etsy bundle link in email body is live (click it now)
- [ ] Check subscriber count matches expected range

**T+1hr (14:00 UTC)**:
- [ ] Delivery rate: >95%? If <90%, execute Playbook 1

**T+24hr (13:00 UTC next day)**:
- [ ] Open rate: >GREEN threshold? Log and continue
- [ ] Open rate <15% (Email 3 only): Activate fatigue protocol — shift Email 4 to Jul 27
- [ ] Click rate: >GREEN? Log and continue. <1% with GREEN opens: fix CTA for next email
- [ ] Log in PHASE_3_EXECUTION_LOG.md

**Daily (22:00 UTC)**:
- [ ] Unsubscribe count and rate logged
- [ ] >0.5%: execute churn investigation (SEEDWARDEN_Q3_DAILY_SUBSCRIBER_CHURN_MONITORING.md)

### Non-Send Days (All Other Days)

**22:00 UTC daily**:
- [ ] Unsubscribes for day: [count] / [total subscribers] × 100 = [rate%]
- [ ] Status: GREEN (<0.3%) / YELLOW (0.3–0.5%) / RED (>0.5%)
- [ ] Log in PHASE_3_EXECUTION_LOG.md

---

## SECTION 8: CONTENT ADJUSTMENT RULES (WEEKS 3-4)

### If Email 3 Performance is Below Email 2

Apply these content adjustments before Email 4 drafting:

| Email 3 vs. Email 2 | Adjustment |
|---------------------|-----------|
| Opens down 3–5 points | A/B test subject line for Email 4 |
| Opens down 5+ points | Shift subject to curiosity-hook; increase educational ratio to 80/20 |
| Clicks down 2+ points | Move CTA above fold; strengthen CTA verb ("Get" not "View") |
| Unsubs up 0.2+ points | Increase send gap to 10 days (Jul 20 → Jul 23 instead) |
| All metrics stable | No changes; keep Email 4 format identical to Email 3 structure |

### Body Content Ratio Adjustment Guide

| Open Rate Status | Click Rate Status | Email 4-5 Content Ratio |
|-----------------|-------------------|------------------------|
| GREEN (>threshold) | GREEN (>3%) | 60% educational / 40% promotional (standard) |
| YELLOW (15–threshold) | GREEN | 70% educational / 30% promotional |
| YELLOW | YELLOW (1–3%) | 75% educational / 25% promotional; strengthen CTA |
| RED (<15%) | Any | 80% educational / 20% promotional; shift framing to value delivery |
| GREEN | RED (<1%) | Standard ratio OK; CTA rewrite required; test button text |

---

## Version Control

**Document version**: 1.0  
**Created**: 2026-06-29  
**Update required by**: July 8, 2026 (after Email 1 + Email 2 data in) — populate Section 1 adjusted thresholds  
**Next update**: After Email 3 T+48hr close (July 15)  
**Owner**: Seedwarden Q3 Project Lead

*This document is the Week 3-4 extension of SEEDWARDEN_Q3_DAILY_EMAIL_MONITORING_CHECKLIST.md. That document governs operational procedure; this document governs thresholds, aggregation, and adjustment decisions specific to the Week 3-4 window where list fatigue, multi-send accumulation, and campaign-learning inform real-time pivots.*
