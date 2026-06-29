---
title: "Seedwarden Phase 3 Q3 Daily Email Monitoring Checklist"
date: 2026-06-29
version: 1.0
status: production-ready
sprint-window: June 29 – August 31, 2026
baseline-metrics: "Expected 22–28% open rate, 3–5% click rate (Q2 2026 construction-audience baseline)"
cross-references:
  - PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md (escalation decision trees)
  - PHASE_3_EXECUTION_LOG.md (metric recording location)
  - PHASE_3_LAUNCH_CALENDAR.md (bundle send schedule)
  - PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md (email content templates)
---

# Seedwarden Phase 3 Q3 Daily Email Monitoring Checklist

## Overview

This checklist provides actionable, daily monitoring procedures for the Seedwarden Phase 3 medicinal herbs bundle launch email campaign (June 29 – August 31, 2026). It pairs with PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md for escalation triggers and decision trees.

**All times in UTC unless otherwise stated.** Primary send time: 13:00 UTC (9:00 AM ET).

**Success baseline**: 22–28% email opens, 3–5% clicks (Q2 construction-audience benchmark).

---

## Part 1: Pre-Send Verification Procedures for Kit.com

### Step-by-Step Pre-Send Checklist (Run 1 hour before send time)

Run these verification steps at T-60 minutes (12:00 UTC / 8:00 AM ET) before each campaign send.

#### 1.1: Sender and List Verification

- [ ] **Sender email verified**: Confirm sender address in Kit.com > Settings > Email Sender. Must match previous sender domain (e.g., `hello@seedwarden.com`). No sudden domain changes within same campaign cycle.
- [ ] **List segment selected**: Navigate to Kit.com > Campaigns > [Campaign Name] > Recipients. Verify:
  - [ ] Correct subscriber segment selected (e.g., "All Subscribers" vs. "Openers of Email 1")
  - [ ] Subscriber count displayed matches expectation (±2% tolerance for recent unsubscribes)
  - [ ] No "Unconfirmed" subscribers included (suppress these before send if list has >5% unconfirmed)
  - [ ] "Bounced" subscribers excluded (automatic in Kit but verify manually on first send)
- [ ] **Unsubscribe link present**: Open email preview. Scroll to footer. Confirm unsubscribe link is visible and resolves (test link by clicking in preview, should show "[Unsubscribe]" or equivalent Kit language).

#### 1.2: Email Content Verification

- [ ] **Subject line review**:
  - [ ] No ALL CAPS words (except 1–2 acronyms if unavoidable)
  - [ ] No excessive punctuation (no more than one `!` or `?` per subject)
  - [ ] No spam trigger phrases: "FREE," "WINNER," "ACT NOW," "LIMITED TIME," "URGENT"
  - [ ] Subject length 40–60 characters (optimal for mobile preview)
  - [ ] Preview text (first 40–50 chars of body) differs from subject and sets context
- [ ] **Email body — HTML validation**:
  - [ ] All images hosted on public URL (not local drive, not private Dropbox)
  - [ ] Image-to-text ratio: no more than 60% of email body is images (Kit plaintext emails avoid this, but verify if using custom HTML)
  - [ ] All bundle images load in preview (bundle photo, cover mockup, etc.)
  - [ ] Text is readable: no tiny fonts (<11pt), no low-contrast colors
- [ ] **Links verification**:
  - [ ] All CTA links resolve to live Etsy listing (click each link, confirm 200 OK response, no 404)
  - [ ] No redirect chains (link should go directly to Etsy, not through a shortener like bit.ly unless required by analytics)
  - [ ] CTA button text is action-oriented: "Get the [Bundle Name]" or "Download Now" or "View Bundle" (not "Click Here" or "Learn More")
  - [ ] Only 1 primary CTA in email body (secondary CTA in footer is acceptable; no more than 2 total)
- [ ] **Brand consistency**:
  - [ ] Seedwarden branding (logo, colors, tone) matches previous emails in this series
  - [ ] Bundle name, price, and species list match the Etsy listing exactly
  - [ ] No typos in bundle description (spell-check entire email body)

#### 1.3: Delivery Settings Verification

- [ ] **Send time confirmed**: Navigate to Kit.com > Campaigns > [Campaign Name] > Schedule. Verify send time is set to 13:00 UTC.
- [ ] **Sending limits check**: Kit.com > Account > Settings > Sending Limits. Confirm:
  - [ ] No warning alerts or quota restrictions displayed
  - [ ] Account sending rate is normal (not throttled by Kit due to spam complaints)
  - [ ] IP reputation status is "Good" or "Normal" (no "Risky" flag)
- [ ] **Bounce list updated**: If any bounces detected since last send, Kit.com > Subscribers > filter "Bounced," export list, and suppress from this campaign (select campaign > Recipients > Exclude > upload bounced addresses).
- [ ] **Double opt-in confirmed**: All subscribers should have confirmed email (Kit auto-enforces this, but verify account setting is enabled at Kit.com > Account > Settings > Double Opt-In = ON).

#### 1.4: A/B Testing Setup (if applicable)

If A/B testing subject lines or send times:

- [ ] **Subject line A vs. B**: Both subject lines created and documented in PHASE_3_EXECUTION_LOG.md
  - [ ] Version A: [Subject line]
  - [ ] Version B: [Subject line]
  - [ ] Split: 50/50 by subscriber count (Kit auto-splits unless specified otherwise)
  - [ ] Winner declared at: T+24hr based on open rate (highest open% becomes control for next email)
- [ ] **Send time test** (if applicable): Confirm whether send is at standard 13:00 UTC or test time. Document test time in campaign notes.

#### 1.5: Final Sign-Off

- [ ] **Campaign summary approved**: Navigate to Kit.com > Campaigns > [Campaign Name] > Review. Confirm:
  - [ ] Campaign name: [Bundle name] — [Date]
  - [ ] Recipients: [Number] subscribers
  - [ ] Subject: [Display text]
  - [ ] Send time: 13:00 UTC on [Date]
- [ ] **Backup email saved**: Save email HTML or screenshot to local drive (for troubleshooting if needed).
- [ ] **Approval initials**: User initials and timestamp in PHASE_3_EXECUTION_LOG.md pre-send section.
- [ ] **Send button ready**: Email is in "Draft" or "Scheduled" state (not "Sent" yet). One click from sending.

**If any check fails: DO NOT SEND. Document the issue in PHASE_3_EXECUTION_LOG.md and defer to the next scheduled send time or escalate per PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md Procedure 1 (Delivery Rate).**

---

## Part 2: Post-Send Monitoring Checkpoints

Email send time: **13:00 UTC** (9:00 AM ET).

### Checkpoint 1: Delivery Rate Monitoring (T+1 hour = 14:00 UTC, same day)

**Procedure reference**: PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md — PROCEDURE 1

**Metric source**: Kit.com > Campaigns > [Campaign Name] > Delivery Stats

| Metric | Location in Kit | Action |
|--------|---|---|
| **Delivery Rate (%)** | Campaign > Delivery Stats > "Delivered" count / sent count × 100 | If <95%: escalate to YELLOW or RED per alert procedures |
| **Hard Bounces** | Subscribers > Bounces > filter "Hard" | If >1% of total sent: escalate |
| **Soft Bounces** | Subscribers > Bounces > filter "Soft" | Monitor only; Kit auto-retries soft bounces over 72 hours |
| **Spam Complaints** | Campaign > Delivery Stats > "Complaints" | If >0.1%: RED trigger — review email for spam markers |

**Action tree**:

```
IF delivery rate >95% AND spam complaints <0.05%:
  → GREEN status
  Log in PHASE_3_EXECUTION_LOG.md: date, campaign, delivery %, bounces count, time checked
  → Proceed to Open Rate monitoring (T+24hr)

IF delivery rate 90–95% OR spam complaints 0.05–0.1%:
  → YELLOW status
  Run: PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md PROCEDURE 1 steps 1–4
  Document action taken in PHASE_3_EXECUTION_LOG.md
  → Proceed with next send on schedule (no delay required for YELLOW)

IF delivery rate <90% OR spam complaints >0.1% OR hard bounces >2%:
  → RED status — HOLD FOR MANUAL REVIEW
  Run: PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md PROCEDURE 1 steps 1–6
  Do not send next email until escalation resolved
  → Escalate to user email + Kit support contact (see Section 6: Escalation Procedures)
```

---

### Checkpoint 2: Open Rate Monitoring (T+24 hours = 13:00 UTC, next day)

**Procedure reference**: PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md — PROCEDURE 2

**Metric source**: Kit.com > Campaigns > [Campaign Name] > Open Rate

**Timing note**: Do not take action on open rates before T+24hr. Preliminary rates at T+3hr and T+8hr are tracking only. Open rates climb for up to 48 hours.

| Check Time | Metric | Expected Range | Action |
|---|---|---|---|
| **T+24hr** | Open rate (%) | >22% (GREEN) 15–22% (YELLOW) <15% (RED) | Escalate if <15% |
| **T+48hr** | Open rate (final) | >22% (GREEN) 15–22% (YELLOW) <15% (RED) | Final decision point for content/list changes |

**Field reference — Kit.com dashboard**:

- Navigate to: **Campaigns > [Campaign Name] > Analytics > Open Rate**
- Field: **"Open Rate (%)"** — shows percentage of delivered emails that recorded at least one open
- Context: "Opened: [Number] of [Total Delivered]"
- Unique opens: Opens counted once per subscriber (not multiple opens by same person)

**Action tree**:

```
IF open rate >22% at T+24hr:
  → GREEN status
  Log in PHASE_3_EXECUTION_LOG.md: date, campaign, open rate, clicks %
  Proceed to next bundle launch on standard schedule
  No content changes needed

IF open rate 15–22% at T+24hr:
  → YELLOW status
  Step 1: Identify subject line performance
    - If first campaign in series: proceed to Step 2 (baseline too low for A/B)
    - If second+ campaign: compare subject line to prior campaign's subject in PHASE_3_EXECUTION_LOG.md > Aggregate Metrics Summary
  Step 2: Draft A/B subject line for NEXT email (not this one)
    - Option A: Keep current subject line (measure if performance improves in next bundle)
    - Option B: Curiosity-hook variant (e.g., "Why [herb] is harvested wrong 90% of the time")
    - Decision rule: Choose Option B if this is the second+ campaign AND prior campaign was also YELLOW
    - Decision rule: Choose Option A if this is the first campaign (single data point insufficient)
  Step 3: Log YELLOW in PHASE_3_EXECUTION_LOG.md with subject A/B note
  Step 4: Wait for T+48hr data before further decision. No changes to current campaign.

IF open rate <15% at T+24hr:
  → RED status — IMMEDIATE ESCALATION REQUIRED
  Step 1: Run spam placement test (see Section 6: Escalation Procedures, "Spam Placement Test")
    - Send copy of email to 5 test addresses (Gmail, Outlook, Yahoo, Apple, Proton)
    - Check: inbox vs. spam folder placement
  Step 2: Interpret spam test results
    - If 2+ providers show spam folder: email has spam markers (subject, HTML, links)
      → Review Checklist A (PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md, Procedure 1)
      → Revise next email to remove triggers
      → Consider 24-hour delay before next send
    - If all inbox: issue is list engagement, not deliverability
      → Review recent subscriber source (giveaway? low-intent opt-in?)
      → Create segment: subscribers with zero opens in last 3 sends
      → Exclude this segment from next send if >500 subscribers
  Step 3: Log RED escalation in PHASE_3_EXECUTION_LOG.md with:
    - Spam test results (inbox/spam for each provider)
    - Root cause diagnosis
    - Action taken
    - Adjusted send date (if delayed)
  Step 4: Escalate to user per Section 6 (Escalation Procedures) if unable to resolve same-day
```

---

### Checkpoint 3: Click Rate Monitoring (T+24 hours, concurrent with Open Rate check)

**Procedure reference**: PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md — PROCEDURE 3

**Metric source**: Kit.com > Campaigns > [Campaign Name] > Click Rate

| Check Time | Metric | Expected Range | Action |
|---|---|---|---|
| **T+24hr** | Click rate (%) | >3% (GREEN) 1–3% (YELLOW) <1% (RED) | Escalate if <1% |

**Field reference — Kit.com dashboard**:

- Navigate to: **Campaigns > [Campaign Name] > Analytics > Click Rate**
- Field: **"Click Rate (%)"** — shows percentage of delivered emails with at least one click
- Context: "Clicked: [Number] of [Total Delivered]"
- Click rate = (total unique clicks / total delivered) × 100
- **Note**: Kit may also show "Click-Through Rate (CTR)" separately — use "Click Rate" metric (denominator = delivered, not opened)

**Action tree**:

```
IF click rate >3% at T+24hr:
  → GREEN status
  Log in PHASE_3_EXECUTION_LOG.md: date, campaign, click rate %, CTA text
  Proceed with next bundle launch
  No CTA changes needed

IF click rate 1–3% at T+24hr:
  → YELLOW status — CTA AUDIT REQUIRED (but no action on this email)
  Step 1: Review CTA text clarity
    - Acceptable: "Get the [Bundle Name]," "Download Now," "View Guide"
    - Unacceptable: "Click Here," "Learn More," generic verbs
    - Action: If unacceptable, revise for next email template
  Step 2: Test Etsy landing page on mobile
    - Open Etsy listing URL from email on phone (primary check device)
    - Confirm: page loads in <3 seconds, price visible above fold, bundle images loaded
    - If slow or broken: notify Etsy (check for listing issues) or revise link in next email
  Step 3: Count CTA instances in email body
    - If 1 primary CTA: acceptable
    - If >2 CTA links: remove secondary links for next email (concentrate click intent)
  Step 4: Log YELLOW in PHASE_3_EXECUTION_LOG.md with specific CTA audit finding
  Step 5: Apply finding to next email template. Do not change current email.

IF click rate <1% at T+24hr AND open rate is GREEN or YELLOW:
  → RED status — CTA PROBLEM CONFIRMED (opens happening, clicks not)
  Step 1: Deep CTA audit
    - CTA text: Copy it verbatim. Is it action-oriented?
      - Good: "Get," "Download," "View," "Claim"
      - Poor: "Click," "Here," generic verbs
    - CTA placement: Is CTA visible without scrolling (above fold)?
      - If no: add second CTA near top of email
    - CTA link: Does it resolve to LIVE Etsy listing (not 404, not wrong page)?
      - Test: click link in preview, confirm page loads
  Step 2: Image audit
    - Does bundle image (product photo) display in email?
    - If broken or missing: re-verify image URL is public (not local drive, not private Dropbox)
    - Test image URL in browser address bar (should display image, not 404)
  Step 3: Revise next email template with:
    - (1) CTA button text: change to action-oriented verb
    - (2) CTA moved to top half of email (above fold)
    - (3) Add second CTA in footer or post-PS section
  Step 4: Log RED in PHASE_3_EXECUTION_LOG.md with specific CTA change made
  Step 5: Escalate per Section 6 (Escalation Procedures) if CTA/link issues persist across 2+ sends
```

---

### Checkpoint 4: Unsubscribe Rate Monitoring (Daily at 22:00 UTC)

**Procedure reference**: PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md — PROCEDURE 4

**Metric source**: Kit.com > Subscribers > Unsubscribes (filter: last 24 hours)

**Calculation formula**: (Daily unsubscribes / total current subscriber count) × 100 = daily unsubscribe rate %

| Daily Rate | Status | Action |
|---|---|---|---|
| <0.3% | GREEN | Log in PHASE_3_EXECUTION_LOG.md daily unsubscribe count. No action. |
| 0.3–0.5% | YELLOW | Monitor for 3 consecutive days without send. If sustained >0.3%, escalate. |
| >0.5% | RED | Escalate same-day. Identify root cause (email-triggered vs. list fatigue). |

**Kit.com field navigation**:

- Navigate to: **Subscribers > Unsubscribes**
- Filter: Set date range to "Last 24 hours" (or "Custom" and select yesterday to today)
- View: **"Unsubscribes"** count displayed at top
- Optional: View reasons (Kit > Unsubscribes > "Reason" column)
- Calculation: Take unsubscribe count from filter, divide by total subscriber count (Kit > Subscribers > count at top), multiply by 100

**Daily monitoring template** (see Part 4 for CSV template):

```
Date: [YYYY-MM-DD]
Time checked: 22:00 UTC
Total subscribers (beginning of day): [NUMBER]
Unsubscribes (last 24 hours): [NUMBER]
Daily unsubscribe rate: [NUMBER%]
Status: [GREEN / YELLOW / RED]
Notes: [Any spikes, reasons, actions taken]
```

**Action tree**:

```
IF daily unsubscribe rate <0.3%:
  → GREEN status
  Log in PHASE_3_EXECUTION_LOG.md daily unsubscribe count
  No action required

IF daily unsubscribe rate 0.3–0.5% for 1 day:
  → YELLOW status (expected for launch week sends)
  Step 1: This rate is within normal range for high-frequency periods
  Step 2: Monitor for 3 consecutive days without send
    - If rate drops below 0.3% within 3 days: return to GREEN, no escalation
    - If rate sustained >0.3% for 3 days: escalate to RED
  Step 3: Review unsubscribe feedback (Kit > Unsubscribes > "Reason" column)
    - If >20% cite "too many emails": add frequency preference option to next welcome sequence
  Step 4: Log YELLOW in PHASE_3_EXECUTION_LOG.md with daily counts

IF daily unsubscribe rate >0.5% on any day:
  → RED status — SAME-DAY ESCALATION
  Step 1: Identify root cause (email-triggered vs. organic list churn)
    - Pull unsubscribe report: Kit > Unsubscribes > filter "last 7 days"
    - Question: Is spike same-day or day-after a recent email send?
    - If YES (spike correlated with send): email triggered list fatigue
    - If NO (gradual accumulation): list health issue
  Step 2: If spike correlates with a specific send
    - Increase gap between next two sends
    - Example: if Email 2 was within 5 days of Email 1 and Email 1 caused spike: move Email 2 to 10+ days out
    - Review email tone: does it feel too promotional vs. educational?
    - Revise next email to increase educational content (target 80% educational / 20% promotional)
  Step 3: If no specific send correlation (list health issue)
    - Run Kit list health check:
      - Subscribers > filter "Unconfirmed": remove if >15% of list
      - Subscribers > filter "Cold" (no opens in 90 days): suppress from next send
    - Log count before/after cleanup
  Step 4: Full RED escalation log in PHASE_3_EXECUTION_LOG.md with:
    - Pre-clean subscriber count
    - Post-clean subscriber count
    - Root cause (send-triggered vs. list issue)
    - Action taken (send delay, list clean, tone revision)
    - Escalation status
  Step 5: Escalate to user per Section 6 (Escalation Procedures) if rate does not drop below 0.5% by next day
```

---

### Checkpoint 5: Second-Bundle Fatigue Check (Email 3 only: July 13)

**Procedure reference**: PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md — PROCEDURE 5

Run this check when Email 3 (Sleep bundle, scheduled July 13) is sent. Compare open rate to Email 1 and Email 2.

**Fatigue trigger**: Email 3 open rate <15%.

**Context**: By Email 3, subscribers have received 2 launch emails in 15 days (June 29 + July 6). Fatigue typically shows as <15% open rate on the third email.

| Email 3 Open Rate | Status | Action |
|---|---|---|---|
| >20% | GREEN — No fatigue | Proceed with Email 4 on standard Week 3 schedule |
| 15–20% | YELLOW — Minor decline | Increase educational content in Email 4 (80% educational / 20% promotional) |
| <15% | RED — Fatigue confirmed | Extend gap before Email 4 to Week 4 (+7 days). Send re-engagement email to cold segment. |

**Action tree**:

```
IF Email 3 open rate >20%:
  → No fatigue signal detected
  Log in PHASE_3_EXECUTION_LOG.md
  Proceed with Email 4 (Immunity bundle) on standard Week 3 schedule (July 20)

IF Email 3 open rate 15–20%:
  → Minor decline detected
  Step 1: Increase educational content ratio in Email 4
    - Target: 80% educational / 20% promotional (up from standard 60% / 40%)
    - Example: Add "how to dry [herb]" section, "why [herb] works" deep dive
  Step 2: Add teaser section to Email 4 subject line and preview text
    - Example subject: "The [herb] question I get every fall (answered)"
    - Preview: "Plus: why [herb] works better than [alternative]"
  Step 3: Log YELLOW in PHASE_3_EXECUTION_LOG.md with Email 4 content ratio note

IF Email 3 open rate <15%:
  → Fatigue signal confirmed — ACTION REQUIRED
  Step 1: Extend gap before Email 4 by 7 days
    - Move Email 4 (Immunity) from July 20 → July 27
    - Notify any automation sequences to reflect new date
  Step 2: Send re-engagement email to "Cold" segment
    - Define: subscribers who did NOT open Email 1, Email 2, or Email 3
    - Create segment in Kit: Subscribers > Segmentation > "Has not opened" > select all 3 campaigns
    - Send: "We've been launching guides — did you miss them?"
    - Content: brief summary of all 3 bundles with direct Etsy links (no new pitch)
  Step 3: Revise Email 4 subject line
    - Shift from bundle-announcement framing to value-delivery framing
    - Before: "Immunity Support — Herbs for respiratory defense and immune resilience"
    - After: "The elderberry question I get every fall (answered)"
  Step 4: Revise Email 4 body
    - Increase educational content to 80% (see Step 1 above)
    - Reduce promotional language and pitch
  Step 5: Log RED + action taken in PHASE_3_EXECUTION_LOG.md with new send date for Email 4
```

---

## Part 3: Engagement Rate Thresholds & Trigger Conditions

### Quick Reference Table

| Metric | GREEN | YELLOW | RED | Check Time | Escalation Path |
|---|---|---|---|---|---|
| **Delivery Rate** | >95% | 90–95% | <90% | T+1hr (14:00 UTC) | PROC1: Review spam markers, check IP reputation, pause future sends |
| **Open Rate (24hr)** | >22% | 15–22% | <15% | T+24hr (13:00 UTC +1day) | PROC2: Spam test, segment cold subscribers, A/B subject line |
| **Click Rate (24hr)** | >3% | 1–3% | <1% | T+24hr (13:00 UTC +1day) | PROC3: CTA text audit, link verification, CTA repositioning |
| **Unsubscribe Rate** | <0.3% | 0.3–0.5% | >0.5% | Daily 22:00 UTC | PROC4: Identify trigger email, increase send gap, list health clean |
| **Spam Complaints** | <0.05% | 0.05–0.1% | >0.1% | T+1hr (14:00 UTC) | PROC1: Spam marker review, IP reputation escalation |
| **Email 3 Fatigue (July 13)** | >20% | 15–20% | <15% | T+24hr, July 14 | PROC5: Extend send gaps, re-engagement email, content shift |

---

### RED Escalation Triggers & Response Timeline

**RED = Immediate action required within 4 hours**

| Trigger | Threshold | Response | Timeline |
|---|---|---|---|
| Delivery Rate drops <90% | Any decrease below 90% | Pause sends. Review IP reputation. Escalate to Kit support if account flagged. | T+2 hours (within 4 hours of send) |
| Open Rate <15% at T+24hr | Single campaign <15% opens | Run spam placement test. Diagnose list quality vs. deliverability. Segment cold subscribers. | T+24 to T+48 hours (next day morning) |
| Click Rate <1% AND opens are GREEN | Clicks <1% despite >22% opens | CTA is broken or unclear. Revise next email template. Test Etsy link. | Within 24 hours of T+24 checkpoint |
| Unsubscribe Rate >0.5% daily | >0.5% on any 24-hour period | Identify if send-triggered. If yes: extend next send by 7 days. If list fatigue: clean "cold" subscribers. | Same day at 22:00 UTC check |
| Spam Complaints >0.1% | >0.1% by T+1hr | Review email HTML for spam markers. Escalate to Kit support. Do not send next email until resolved. | Within 4 hours of send |
| Email 3 fatigue confirmed | Open rate <15% on July 13 send | Extend Email 4 to July 27. Send re-engagement to cold segment. Pivot Email 4 content to educational frame. | Within 24 hours of T+24 checkpoint |

---

## Part 4: Daily Email Tracking Template (CSV-Style Format)

### Master Tracking Sheet

Use this template to record metrics for every campaign send. **Create a new row for each email send.** Columns align with Kit.com dashboard fields.

```
Date Sent,Campaign Name,Send Time ET,Recipient Count,Delivery Rate %,Hard Bounces,Soft Bounces,Spam Complaints,T+1hr Delivery Status,T+24hr Open Rate %,T+24hr Click Rate %,T+24hr Click Count,Unsubscribe Count (24hr),Unsubscribe Rate %,Email 3 Fatigue Signal,A/B Test (Y/N),Subject Line A,Subject Line B,Open Rate Winner,CTA Text,Etsy Link,Notes / Actions Taken

06-29-2026,Women's Health Bundle,08:00,8000,97.2%,2,12,0,GREEN,24.1%,4.2%,336,18,0.23%,N/A,Y,Women's Health — An 8-week herbal series starts today,Why women skip cycle support (and 3 herbs that fix it),A,Get the Women's Health Bundle,https://www.etsy.com/listing/xxxxx,Baseline campaign; opens above threshold; proceeding to Email 2

07-06-2026,Respiratory Health Bundle,08:00,8165,96.8%,3,10,0,GREEN,22.7%,3.8%,310,16,0.20%,N/A,Y,Respiratory Health — Herbs for clear airways,The 1 mistake that kills mullein potency (how to fix it),A,Get the Respiratory Guide,https://www.etsy.com/listing/xxxxx,Green on all metrics; Email 2 on schedule

07-13-2026,Sleep and Nervines Bundle,08:00,8249,95.5%,4,18,0,YELLOW,19.3%,3.1%,256,22,0.27%,YELLOW (15-20%),N,Sleep and Nervines — Rest the herbal way,N/A,N/A,Get the Sleep Guide,https://www.etsy.com/listing/xxxxx,Slight decline from Email 1/2; YELLOW on opens (19% is 15-22% range); minor fatigue signal emerging

07-20-2026,Immunity Support Bundle,08:00,8271,94.2%,5,22,0,YELLOW,18.1%,2.4%,198,28,0.34%,RED (<15%) for Email 3,Y,Immunity Support — Elderberry and beyond,The immune herb nobody talks about (and why),B,Download the Immunity Guide,https://www.etsy.com/listing/xxxxx,"RED fatigue on Email 3 (18% < 20%); extended gap to Email 5 per PROC5; sent re-engagement to cold segment (412 subscribers); switched subject to value-frame 'The immune herb...'; monitoring for recovery"

08-03-2026,Digestive Support Bundle,08:00,8299,96.1%,2,8,0,GREEN,25.2%,4.6%,381,12,0.14%,GREEN (>20%),N,Digestive Support — Gut health from the garden,N/A,N/A,Get the Digestive Guide,https://www.etsy.com/listing/xxxxx,"Recovery to GREEN after 10-day gap and content pivot; opens recovered to 25%; extended send interval appears to have worked; returned to standard pacing for future cycles"
```

### Daily Unsubscribe Log (Separate Sheet)

Run at 22:00 UTC daily. Track unsubscribe trends across all send windows.

```
Date,Day,Unsubscribe Count (Last 24h),Total Subscribers (EOD),Daily Rate %,Status,Reason Summary (if >20% cite one reason),Escalation Notes

06-29-2026,Friday,18,8000,0.23%,GREEN,N/A,N/A
06-30-2026,Saturday,12,7982,0.15%,GREEN,N/A,N/A
07-01-2026,Sunday,8,7974,0.10%,GREEN,N/A,N/A
07-02-2026,Monday,14,7966,0.18%,GREEN,N/A,N/A
07-03-2026,Tuesday,16,7950,0.20%,GREEN,N/A,N/A
07-04-2026,Wednesday,22,7934,0.28%,YELLOW,Too many emails (45%),Monitor for 3 days; if sustained >0.3% escalate to RED
07-05-2026,Thursday,19,7915,0.24%,YELLOW,Too many emails (48%),Continued elevated rate; planning frequency preference in next welcome
07-06-2026,Friday,28,7887,0.35%,YELLOW,Too many emails (52%),Email 2 sent; rate elevated but within YELLOW range; monitor through 07-09
07-07-2026,Saturday,18,7859,0.23%,GREEN,N/A,Rate dropping; Email 2 spike contained
07-08-2026,Sunday,12,7847,0.15%,GREEN,N/A,Trending back to normal
```

---

## Part 5: Decision Tree for 4 Engagement Scenarios

### Scenario 1: Opens Low (<20%) but Clicks Good (>3%)

**Diagnosis**: Content clarity issue — subscribers opened but didn't immediately recognize value in CTA.

**Root causes**:
- Email body doesn't clearly explain why they should click
- Bundle description is vague or uses internal jargon
- Bundle price is surprising (higher than expected)
- CTA link text doesn't match bundle content stated in body

**Diagnostic steps**:

1. **Compare subject line to email body**: Does the subject promise match the bundle description in body?
   - If mismatch: subject overpromises (e.g., subject says "5 herbs," body only lists 3)
   - Fix: Revise next subject to match body or expand body to match subject
2. **Review bundle description copy**: Is it clear WHY this bundle matters?
   - Weak: "Learn about sleep herbs"
   - Strong: "Why your sleep herbs aren't working (and the 3-herb combo that fixes it)"
   - Fix: Rewrite opening paragraph of next email to lead with benefit/problem solved
3. **Check CTA placement**: Is CTA button visible without scrolling (above the fold)?
   - If below fold: add second CTA near top of email body
   - Fix: Top CTA should appear after first 2–3 paragraphs max
4. **Verify bundle image displays**: Does product image (cover, flat-lay) show in email?
   - If missing/broken: subscribers can't visualize bundle
   - Fix: Re-verify image URL is public (test by opening URL in browser)

**Actions to take**:

- **For THIS email**: No changes. Done.
- **For NEXT email**: 
  - Rewrite opening paragraph to lead with problem/benefit (not feature list)
  - Move CTA button above fold
  - Add 1–2 images of bundle / herb close-ups for visual appeal
  - Test email on mobile (primary view device) — CTA must be tappable and visible

**Example revision**:

```
Before:
"Hi [Name],
This month we're launching the Sleep Bundle. Inside you'll find information about:
- Passionflower
- Valerian
- Skullcap
And more. Get the bundle here: [LINK]"

After:
"Hi [Name],
Why do sleep herbal blends fail? Because they mix fast-acting nervines (valerian) with slow-acting adaptogens (ashwagandha).
Our Sleep Bundle teaches you WHEN to use each herb across your night. You'll discover:
- The timing mistake that kills passionflower's effect
- Why valerian works in tea form but not as a powder
- The 3-herb combo for falling asleep vs. staying asleep
[GET THE SLEEP GUIDE]
[LINK displayed here, at fold]
[Rest of content below]"
```

---

### Scenario 2: Opens Good (>22%) but Clicks Low (<2%)

**Diagnosis**: CTA problem — subscribers read email but didn't click through to Etsy.

**Root causes**:
- CTA text is vague ("Click Here," "Learn More") instead of action-oriented
- CTA button is buried below fold (requires scrolling to find)
- CTA link is broken or points to wrong Etsy listing
- Bundle image doesn't load, reducing click intent
- Etsy page loads slowly or doesn't display price (friction on landing)

**Diagnostic steps**:

1. **Audit CTA text**: Copy the exact CTA text from email.
   - Weak: "Click here," "Learn more," "Read guide," "View now"
   - Strong: "Get the Sleep Bundle," "Download Now," "View on Etsy," "Claim Yours"
   - If weak: replace with action-oriented verb + bundle name
2. **Test CTA link**: Click link in email preview or Kit.com preview.
   - Does it resolve to correct Etsy listing?
   - Does page load in <3 seconds?
   - Is bundle price visible above fold on mobile?
   - If any fail: fix link or notify Etsy of listing issues
3. **Check CTA placement**: Is CTA visible without scrolling?
   - Count lines to CTA from email top. If >5 paragraphs: move CTA up or add second CTA.
   - Mobile device: Does CTA appear on first screen?
   - Fix: Add CTA within first 2–3 paragraphs AND in footer
4. **Verify bundle image**: Does product image display (not broken)?
   - Test: Open image URL directly in browser address bar
   - If 404 or broken: re-upload image to public host
5. **Count total links**: Are there competing CTAs (multiple links)?
   - If >2 CTA links: remove secondary links. Keep ONE primary CTA.
   - This prevents decision fatigue (subscribers click non-CTA link instead)

**Actions to take**:

- **For THIS email**: 
  - If CTA link is broken: add note in PHASE_3_EXECUTION_LOG.md, manually note the issue
  - If Etsy listing is slow: escalate to Etsy shop owner
  - Do NOT re-send email unless critical error (broken link)
- **For NEXT email**:
  - Revise CTA text to action-oriented verb + bundle name
  - Position CTA within first 3 paragraphs (above fold on mobile)
  - Add second CTA in footer (PS section or sign-off)
  - Re-test image URL before sending
  - Limit total links in email to 1 primary CTA + unsubscribe/footer links only

**Example revision**:

```
Before:
"Hi [Name],
The Sleep Bundle is ready. Check out the Sleep Bundle. [LEARN MORE]"

After:
"Hi [Name],
Why do sleep herbal blends fail? Because they mix fast-acting nervines with slow-acting adaptogens.
Our Sleep Bundle teaches you WHEN to use each herb across your night.
[GET THE SLEEP BUNDLE — $20]
[LINK displayed here at fold]
---
Here's what's inside:
[Bundle description, herbs, recipes]
---
Ready to sleep better? [GET THE GUIDE]
[LINK repeated in footer]
Seedwarden"
```

---

### Scenario 3: Both Opens and Clicks Low (<20% opens AND <2% clicks)

**Diagnosis**: List quality or deliverability issue — email isn't reaching engaged subscribers or list has stale addresses.

**Root causes**:
- Email landed in spam folder for many subscribers (deliverability problem)
- List contains many cold/inactive subscribers (list hygiene problem)
- Recent subscriber cohort came from low-intent source (giveaway, low opt-in bar)
- Subject line or sender domain changed abruptly (trust issue)

**Diagnostic steps**:

1. **Run spam placement test** (mandatory for this scenario):
   - Send copy of email to 5 test addresses:
     - Gmail personal account
     - Outlook.com personal account
     - Yahoo Mail personal account
     - Apple iCloud personal account
     - Proton Mail free account
   - Check: which folder does email land in (inbox vs. spam)?
   - If 2+ providers show spam folder: email has spam markers (subject, HTML, links)
   - If all inbox: issue is list quality, not deliverability
2. **If spam placement confirmed** (2+ providers = spam):
   - Review Checklist A (PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md, Procedure 1)
   - Identify spam triggers: subject line, image/text ratio, link density, unsubscribe link missing
   - Example: subject line has "FREE," "WINNER," "ACT NOW" → remove
   - Example: 80% of email is images, <20% text → rebalance to 40% images / 60% text
3. **If spam test shows inbox** (list quality issue):
   - Pull subscriber acquisition sources: Kit.com > Subscribers > Source report
   - Identify: which sources have lowest opens? (Giveaway? Landing page? Facebook ad?)
   - Create cold segment: Kit.com > Subscribers > filter "no opens in last 90 days"
   - Count cold segment. If >20% of list: this is the problem
   - Exclude cold segment from next send (isolate issue)
4. **Review recent subscriber cohorts**:
   - If large cohort joined 1–2 months ago: they may not be engaged yet
   - If large cohort came from single source (e.g., giveaway): low intent
   - Option: suppress giveaway cohort from next send, measure performance of core subscribers only

**Actions to take**:

- **For THIS email**: Document findings in PHASE_3_EXECUTION_LOG.md. Do NOT re-send.
- **For NEXT email**:
  - If spam trigger found: revise subject line and HTML per Checklist A
  - If list quality issue: exclude cold segment (no opens in 90 days)
  - Consider 7–10 day gap before next send (allows time for re-engagement attempt)
  - Send re-engagement email to cold segment before next bundle launch
- **Long-term** (post-Phase 3):
  - Implement monthly "cold subscriber" cleanup (suppress >90 days no-open)
  - Track subscription source performance; de-prioritize low-intent sources

**Example diagnostics**:

```
Email 3 performance: 14% opens, 0.8% clicks
→ Run spam test:
   Gmail: INBOX ✓
   Outlook: INBOX ✓
   Yahoo: INBOX ✓
   Apple: INBOX ✓
   Proton: INBOX ✓
→ Verdict: Email delivered to inbox. List quality issue.
→ Investigate: 8,249 total subscribers
   - Cold segment (no opens last 90 days): 1,247 subscribers (15%)
   - New giveaway cohort (joined 30 days ago): 612 subscribers (7.4%)
   - Core subscribers (>1 open in 90 days): 6,390 subscribers (77%)
→ Segment analysis: If we exclude cold + giveaway, core open rate would be ~18-19%
→ Action: Next email send only to core 6,390 subscribers. Measure opens separately.
→ If core segment shows >22% opens: confirm list quality is root cause.
→ Then clean cold segment from main list and re-baseline engagement metrics.
```

---

### Scenario 4: Unsubscribe Spike (>0.5% daily)

**Diagnosis**: Email triggered frequency fatigue or content mismatch expectations.

**Root causes**:
- Email 2 sent too close to Email 1 (subscribers feel overwhelmed by frequency)
- Email tone is too promotional vs. educational (content mismatch)
- Subject line overpromised; email body didn't deliver
- Unsubscribe link prominent, and subscribers used it due to frequency regret

**Diagnostic steps**:

1. **Identify if spike is send-triggered**:
   - Pull Kit.com unsubscribe report: 7-day view
   - Question: Did spike occur same-day or day-after a recent email send?
   - If YES: the email caused the spike (frequency/content issue)
   - If NO (gradual, no correlation to send): list health issue
2. **Review sending frequency**:
   - Check: How many days between Email 1 and Email 2?
   - Standard: 7–10 days between emails (Phase 3: June 29 + July 6 = 7 days ✓)
   - If <5 days apart: subscribers perceive as too frequent
   - If >3 sends within 21 days: cumulative fatigue triggers unsubscribes
3. **Review email tone**:
   - Count sales-focused sentences vs. educational sentences
   - Benchmark: 60% educational / 40% promotional (or 80% / 20% in retention phases)
   - If email is >60% promotional: rebalance for next send
4. **Check unsubscribe reasons**:
   - Kit.com > Unsubscribes > "Reason" column
   - If >20% say "too many emails": frequency is the issue
   - If >20% say "not relevant": content mismatch
   - If split reasons: unclear issue; proceed to Step 5
5. **Review subscriber list health**:
   - Kit.com > Subscribers > filter "Cold" (no opens 90 days)
   - If >15% of list is cold: cold subscribers are unsubscribing at baseline rate
   - This may not be email-triggered; organic churn is normal

**Actions to take**:

- **If spike is send-triggered** (>0.5% unsubscribe same-day or day-after send):
  - Increase gap before next send by 7 days
  - Example: Email 2 on July 6, Email 3 was July 13 → move Email 3 to July 20
  - Rewrite next email to increase educational content (target 80% / 20%)
  - Log change in PHASE_3_EXECUTION_LOG.md with new send date
- **If spike is NOT send-triggered** (gradual, no correlation to send):
  - Clean "cold" subscribers from main list: Kit.com > Subscribers > export "Cold," suppress from future sends
  - Count before/after (pre-clean: 8,249, post-clean: 7,002)
  - Baseline unsubscribe rate will drop after cleanup
- **Long-term** (post-Phase 3):
  - Add frequency preference to welcome sequence: "How often would you like to hear from us? [Daily] [Weekly] [Monthly]"
  - Segment by preference; don't send to [Monthly] subscribers if they're in [Weekly] frequency bucket

**Example escalation**:

```
July 4 unsubscribe spike: 0.6% (56 subscribers from 9,342 total)
→ Identify trigger: Email 2 (Respiratory) sent July 6
→ Timeline: Spike occurred July 4 (2 days before send) — NOT send-triggered
→ Diagnosis: Organic churn from cold segment
→ Review unsubscribe reasons:
   - "Too many emails": 12 (21%)
   - "Not relevant": 18 (32%)
   - No reason given: 26 (46%)
→ Action: Clean list
   - Cold segment (no opens 90 days): 987 subscribers
   - Export, suppress from future sends
   - New total: 8,355 active subscribers
   - Rebaseline unsubscribe rate using new denominator
→ Monitor: Next 3 days unsubscribe rate; if drops to <0.3%, cleanup was effective.
→ Future: Add frequency preference to next welcome sequence.
```

---

## Part 6: Escalation Procedures

### Escalation Contact Matrix

| Issue | Primary Contact | Secondary Contact | Turnaround | Info to Include |
|---|---|---|---|---|
| **Delivery rate RED** (<90%) or **spam complaints** (>0.1%) | Kit support (support@kit.com) | User (wanka95@gmail.com) | 1 business day | Account email, campaign name, metric value, affected send date, error message (if any) |
| **Unsubscribe spike RED** (>0.5%) or **fatigue confirmed** (Email 3 <15%) | User decision required | N/A | Same day | Spike date, magnitude (e.g., "0.6%"), root cause diagnosis (send-triggered vs. list health), recommended action |
| **CTA / click rate RED** (<1% clicks) | User decision required | N/A | Within 24 hours | Open rate, click count, CTA text audited, Etsy link tested, image status |
| **Open rate RED** (<15%) + **spam test confirming spam folder** | Kit support + Email revision needed | User | 1 business day | Spam test results (5 providers, inbox/spam for each), subject line, email HTML, recommend action (revise vs. resend) |
| **Open rate RED** (<15%) + **spam test clear** (all inbox) | User decision required | N/A | Within 24 hours | Spam test results (all inbox), list quality findings (% cold, recent cohort sources), segment recommendation |

### Escalation Email Template

Use this template to escalate RED issues to user or Kit support.

**To**: [Primary Contact]  
**Subject**: [Status] Phase 3 Email Campaign Escalation — [Bundle Name] — [Metric Name] [Date]  
**Body**:

```
Hello [Recipient],

I am escalating a RED-status issue from the Seedwarden Phase 3 email campaign.

CAMPAIGN DETAILS:
- Bundle: [Name]
- Send date: [Date] at [Time] UTC
- Recipients: [Number]
- Delivery rate: [%] (expected >95%)

ISSUE SUMMARY:
- Metric: [Delivery Rate / Open Rate / Click Rate / Unsubscribe Rate]
- Status: RED (threshold exceeded)
- Value: [Number] (threshold: [Threshold])
- Discovered: [Date] at [Time] UTC (T+[Hours]hr)

ROOT CAUSE ANALYSIS:
[Describe diagnosis: Spam marker found? List quality issue? CTA broken? Deliverability issue?]

EVIDENCE:
- Spam placement test result: [If applicable — inbox on all 5 providers / spam on 2 providers]
- Kit.com diagnostic: [Specific finding from dashboard]
- List segment analysis: [If applicable — % cold, recent cohort source, etc.]

RECOMMENDED ACTION:
[Option 1]: [Action A] — Timeline: [Duration]
[Option 2]: [Action B] — Timeline: [Duration]
[My recommendation]: [Option X] because [reason].

NEXT STEPS:
- Please approve Action [X] by [Time] [Date] so I can proceed with [Email Name] send
- If you need clarification, I'm available at [Phone/Email]
- Log this escalation in PHASE_3_EXECUTION_LOG.md

Thank you,
[Name]
```

### Spam Placement Test Procedure

**When to run**: RED trigger on delivery rate OR open rate <15%  
**Duration**: 15 minutes  
**Tools needed**: Email access to 5 providers or ability to create test accounts

**Step 1: Create/access test email accounts** (5 total)

```
Provider 1: Gmail
- Account: [create new or use existing test account]
- Address: example.seedwarden.test@gmail.com

Provider 2: Outlook
- Account: [create new or use existing test account]
- Address: example.seedwarden.test@outlook.com

Provider 3: Yahoo Mail
- Account: [create or use existing]
- Address: example.seedwarden.test@yahoo.com

Provider 4: Apple iCloud
- Account: [create or use existing]
- Address: [name]@icloud.com

Provider 5: Proton Mail
- Account: [create new free account — no phone number required]
- Address: seedwarden.test@protonmail.com
```

**Step 2: Send test email**

- Open the RED-status campaign in Kit.com
- Click "Send Test Email"
- Enter the 5 test email addresses (one per line)
- Click "Send"
- Wait 2–3 minutes for emails to arrive

**Step 3: Check inbox vs. spam folder**

| Provider | Inbox | Spam | Notes |
|---|---|---|---|
| Gmail | ✓ or ✗ | ✓ or ✗ | [Any visible markers?] |
| Outlook | ✓ or ✗ | ✓ or ✗ | [Any visible markers?] |
| Yahoo | ✓ or ✗ | ✓ or ✗ | [Any visible markers?] |
| Apple | ✓ or ✗ | ✓ or ✗ | [Any visible markers?] |
| Proton | ✓ or ✗ | ✓ or ✗ | [Any visible markers?] |

**Step 4: Interpret results**

```
IF all 5 show INBOX:
  → Email is deliverable (no spam markers detected)
  → Issue is NOT deliverability, but list quality
  → Diagnosis: proceed to list health analysis (Scenario 3)

IF 2–3 show SPAM:
  → Email has weak spam markers (subjective filters from those providers)
  → Review subject line and HTML for borderline phrases

IF 4+ show SPAM:
  → Email has strong spam markers (authentication, content, or HTML issue)
  → Diagnosis: urgent revision needed before next send
  → Review Checklist A (PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md)
```

**Step 5: Document result**

Log in PHASE_3_EXECUTION_LOG.md:

```
SPAM PLACEMENT TEST — [Date] [Campaign Name]
Performed: [Time] UTC by [Name]
Test addresses: 5 (Gmail, Outlook, Yahoo, Apple, Proton)

RESULTS:
- Inbox: [Number / 5]
- Spam: [Number / 5]

DETAILED:
- Gmail: [INBOX or SPAM]
- Outlook: [INBOX or SPAM]
- Yahoo: [INBOX or SPAM]
- Apple: [INBOX or SPAM]
- Proton: [INBOX or SPAM]

VERDICT: [Email is deliverable / Email has weak spam markers / Email has strong spam markers]

NEXT ACTION: [No action needed / Monitor list quality / Revise email and retest]
```

---

### Kit Support Contact Information

**Email**: support@kit.com  
**Subject line template**: "Account issue — [Campaign Name] — [Issue type]"  
**Response SLA**: 1 business day (typically 4–24 hours)

**Information to include in every support ticket**:

```
1. Account email: [Your Kit login email]
2. Campaign name: [Exact name from Kit > Campaigns]
3. Issue: [Delivery rate dropped below 90% / Spam complaints exceeded threshold / Account suspended / etc.]
4. Metric affected: [Delivery rate: 87% / Bounce rate: 3.2% / etc.]
5. Send date: [Date] at [Time] UTC
6. Recipients count: [Number]
7. Error message (if any): [Copy exact error text]
8. Steps you've taken: [Reviewed account settings / Checked sender domain / etc.]
9. Desired outcome: [Resume sends / Whitelist domain / etc.]
```

---

## Part 7: Kit.com Dashboard Fields to Monitor Daily

### Required Daily Fields (Check at specified times)

| Kit Dashboard Section | Field Name | Location Path | Purpose | Check Frequency |
|---|---|---|---|---|
| **Campaigns** | Campaign name | Campaigns > [Campaign Name] > Details | Verify correct campaign is monitored | Pre-send |
| **Campaigns** | Recipient count | Campaigns > [Campaign Name] > Recipients | Confirm list size; alert if <expected | Pre-send |
| **Campaigns** | Delivery rate | Campaigns > [Campaign Name] > Delivery Stats | T+1hr: ensure >95% | T+1hr |
| **Campaigns** | Delivered count | Campaigns > [Campaign Name] > Delivery Stats | T+1hr: raw count for validation | T+1hr |
| **Campaigns** | Bounce rate | Campaigns > [Campaign Name] > Delivery Stats | T+1hr: hard bounces should be <1% | T+1hr |
| **Campaigns** | Hard bounces (count) | Subscribers > Bounces > filter "Hard" | T+1hr: identify invalid addresses | T+1hr |
| **Campaigns** | Spam complaints | Campaigns > [Campaign Name] > Delivery Stats | T+1hr: should be <0.05% | T+1hr |
| **Analytics** | Open rate | Campaigns > [Campaign Name] > Analytics > Open Rate | T+24hr: >22% is GREEN | T+24hr |
| **Analytics** | Opened count | Campaigns > [Campaign Name] > Analytics | T+24hr: raw count for calculations | T+24hr |
| **Analytics** | Click rate | Campaigns > [Campaign Name] > Analytics > Click Rate | T+24hr: >3% is GREEN | T+24hr |
| **Analytics** | Click count | Campaigns > [Campaign Name] > Analytics | T+24hr: raw count for calculations | T+24hr |
| **Analytics** | Clicked links (by URL) | Campaigns > [Campaign Name] > Analytics > Clicks > By Link | T+24hr: identify which links drove clicks | T+24hr |
| **Subscribers** | Total count | Subscribers > top of page | Daily at 22:00 UTC: baseline for rate calculations | Daily 22:00 UTC |
| **Subscribers** | Unsubscribes (24hr) | Subscribers > Unsubscribes > filter "Last 24 hours" | Daily 22:00 UTC: calculate daily rate % | Daily 22:00 UTC |
| **Subscribers** | Unsubscribe reasons | Subscribers > Unsubscribes > "Reason" column | Daily 22:00 UTC: identify trends (too many emails, not relevant, etc.) | Daily 22:00 UTC |
| **Subscribers** | Cold segment | Subscribers > filter "Last opened" > set "90 days ago" | Daily 22:00 UTC: identify inactive subscribers for potential removal | Daily 22:00 UTC |
| **Account** | Sending limits | Account > Settings > Sending Limits | Pre-send: check for quota warnings | Pre-send |
| **Account** | Deliverability status | Account > Deliverability > "Your IP reputation" | Pre-send: confirm "Good" or "Normal" | Pre-send |
| **Account** | Domain DKIM/SPF | Account > Sending Domain > DKIM & SPF | Pre-send: verify authentication is enabled | Pre-send |
| **Account** | Bounce settings | Account > Settings > List Cleaning > Auto-remove bounces | Pre-send: confirm hard bounces auto-suppressed | Pre-send |

---

## Part 8: Content Adjustment Decision Tree Based on Open Rates

### How to Read This Tree

Start at the top with your T+24hr open rate. Follow branches left or right based on each condition. Each endpoint gives a specific content recommendation.

```
OPEN RATE AT T+24hr
│
├─ >25% (EXCELLENT)
│  ├─ AND clicks >4%: No changes. Subject/content resonating well. Keep template.
│  └─ AND clicks 1–4%: Clicks lag behind opens. CTA/link may be issue (see Part 5, Scenario 2).
│
├─ 22–25% (GREEN)
│  ├─ AND clicks >3%: Perfect. Maintain this subject line and content structure.
│  └─ AND clicks 1–3%: Clicks underperforming. Audit CTA (see Part 5, Scenario 2).
│
├─ 18–22% (YELLOW — acceptable but trending down)
│  ├─ AND this is email 2+: Compare to prior email
│  │  ├─ If prior email was >22%: Subject line may have regressed. A/B test (see PROC2, Step 2).
│  │  └─ If prior email was also 18–22%: Consistent performance. Monitor next email; may indicate list engagement plateau.
│  └─ AND this is email 1: Baseline acceptable. Keep subject; monitor email 2 for trend.
│
├─ 15–18% (YELLOW — concerning trend)
│  ├─ AND list >6,000 subscribers: List likely contains cold segment. Run list cleanup (cold >90 days no-open).
│  └─ AND list <6,000 subscribers: Small list means fewer data points. A/B test subject line (see PROC2).
│
├─ <15% (RED — action required)
│  ├─ Run spam placement test (mandatory)
│  │  ├─ IF spam: Review Checklist A (PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md). Revise subject/HTML.
│  │  └─ IF inbox on all: List quality issue. Segment cold subscribers and re-test. See Part 5, Scenario 3.
│  └─ For next email: Shift subject line to curiosity-hook or value-frame ("The X question I get Y" style).
│
└─ IF opens LOW but clicks GOOD: Content clarity issue. Email body doesn't explain WHY to click. Revise opening paragraph (see Part 5, Scenario 1).
```

---

### Subject Line Adjustment Framework

Use this table to adjust subject lines based on open rate performance.

| Prior Open Rate | Status | Recommendation for Next Email |
|---|---|---|
| >25% | Excellent | Keep subject line structure. Test minor variations if curious (different hook word, adjusted length). |
| 22–25% | Green | Keep subject line. Performance stable. |
| 18–22% | Yellow | A/B test. Version A: same subject structure. Version B: curiosity hook ("Why [thing] [problem]..."). |
| 15–18% | Yellow → Red | A/B test required. Version A: major subject reframe (value-based instead of announcement-based). Version B: curiosity hook. |
| <15% | Red | Mandatory reframe. Shift from announcement ("Immunity Bundle launched") to value ("The [herb] question I get every [season]"). |

---

### Body Content Adjustment Framework

| Open Rate | Click Rate | Content Adjustment |
|---|---|---|
| >22% | >3% | No changes. Baseline content works. |
| >22% | 1–3% | Add visual breaks (bold headers, short paragraphs). Clarify CTA. Move CTA above fold. |
| >22% | <1% | Increase educational content. Add why-to-buy section. Improve CTA visibility. |
| 15–22% | >3% | Strengthen opening paragraph. Make benefit clear in first 2 sentences. Keep rest same. |
| 15–22% | 1–3% | Increase educational ratio (target 80% / 20% promotional). Simplify copy. Strengthen CTA. |
| 15–22% | <1% | Rewrite opening 3 paragraphs for benefit clarity. Fix CTA (text, placement, link). Add images. |
| <15% | Any | If spam placement positive: revise subject line, reduce image density, check for trigger phrases. If inbox delivery positive: increase educational content, reframe from promotional to educational. |

---

## Part 9: A/B Testing Guidelines for Subject Lines and Send Times

### Subject Line A/B Testing

**When to test**: After Email 1 baseline is established OR if Email N open rate enters YELLOW (15–22%) or RED (<15%)

**Test structure**: 50/50 split by subscriber count (Kit auto-splits unless specified)

| Element | Version A (Control) | Version B (Test) | Evaluate |
|---|---|---|---|
| **Announcement frame** | "Women's Health — An 8-week series" | "Why you're doing cycle support wrong (and 3 herbs that fix it)" | Curiosity > announcement |
| **Benefit frame** | "Sleep Bundle — 6 restful herbs" | "The sleep herb nobody talks about (and why)" | Specific benefit > generic benefit |
| **Problem frame** | "Immunity support from herbs" | "Your immunity herbs aren't working — here's why" | Problem identification > feature listing |
| **Question frame** | "Respiratory health guide inside" | "Which respiratory herb works best for your cough?" | Question > statement |

**Success metric**: Version B should have ≥2% higher open rate than Version A

**Decision rule**:
```
IF Version B open rate > Version A by ≥2%:
  → Use Version B for next email (Version B becomes new control)
  → Document winner in PHASE_3_EXECUTION_LOG.md
  → Archive loser for future reference

IF Version B and Version A within 2% of each other:
  → Use Version A (control is safest when unclear)
  → Note "inconclusive" in log
  → Try different A/B in next email (change a different element)

IF Version A > Version B:
  → Keep Version A as control
  → Test different variant next time
  → Example: last test was Curiosity vs. Announcement; next test: Benefit vs. Problem
```

**Example A/B test campaign**:

```
Email 3 (Sleep Bundle) A/B Test Results:
- Subject A: "Sleep and Nervines — Rest the herbal way" (control)
- Subject B: "Why your sleep herbs aren't working (here's why)" (test)
- A sent to: 4,125 subscribers
- B sent to: 4,124 subscribers
- A open rate: 18.2% (757 opens)
- B open rate: 21.3% (876 opens)
- Difference: +3.1% favor B
- **DECISION**: B is winner. Use "Why your X..." frame for Email 4.
- Logged: PHASE_3_EXECUTION_LOG.md, Email 3 A/B section
```

---

### Send Time A/B Testing

**When to test**: If delivery rate is RED or if opens are consistently YELLOW/RED

**Standard send time**: 13:00 UTC (9:00 AM ET)

**Test send times**:

| Time | Timezone | Logic | Best for |
|---|---|---|---|
| **09:00 UTC** | 4:00 AM ET | Very early | Not recommended (too early in US time) |
| **11:00 UTC** | 6:00 AM ET | Early morning | Europe/early risers |
| **13:00 UTC (control)** | 8:00 AM ET | Standard coffee check-in | Broad US audience |
| **14:00 UTC** | 9:00 AM ET | Mid-morning | US business/professional audience |
| **16:00 UTC** | 11:00 AM ET | Late morning | Lunch-break checking |
| **18:00 UTC** | 1:00 PM ET | Afternoon | Alternative US time |
| **20:00 UTC** | 3:00 PM ET | Afternoon/evening | Evening leisure reading |

**Test structure**: Send 50/50 split at Time A vs. Time B (Kit auto-splits)

**Decision rule**:
```
IF Time B has ≥2% higher open rate than Time A:
  → Switch to Time B for next email
  → Document new send time in PHASE_3_EXECUTION_LOG.md
  → Use Time B as new control

IF Time A and Time B within 2%:
  → Continue with 13:00 UTC (control)
  → Send time may not be primary lever; focus on subject line / content instead

IF Time A > Time B:
  → Confirm 13:00 UTC is optimal
  → Do not continue time-based A/B testing unless opens drop below 15%
```

**Note**: Send time testing is secondary to subject line testing. Prioritize subject line A/B first.

---

## Part 10: Integration with PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md

This checklist is the **daily operational manual**. PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md is the **escalation decision tree**. They work together as follows:

| Task | Use This Doc | Then Use Alert Procedures Doc |
|---|---|---|
| **Pre-send verification** | Part 1 checklist | N/A (alert only if issue found) |
| **T+1hr delivery check** | Part 2, Checkpoint 1 action tree | PROCEDURE 1 if RED |
| **T+24hr open rate check** | Part 2, Checkpoint 2 action tree | PROCEDURE 2 if RED |
| **T+24hr click rate check** | Part 2, Checkpoint 3 action tree | PROCEDURE 3 if RED |
| **Daily unsubscribe check** | Part 2, Checkpoint 4 action tree | PROCEDURE 4 if RED |
| **Email 3 fatigue decision** | Part 2, Checkpoint 5 action tree | PROCEDURE 5 if fatigue confirmed |
| **Scenario diagnosis** | Part 5 (4 engagement scenarios) | Alert Procedures for specific steps |
| **Escalation procedures** | Part 6 contact matrix | Alert Procedures for step-by-step instructions |
| **A/B testing framework** | Part 9 | Alert Procedures PROCEDURE 2 (subject line decision) |

### Cross-Reference Examples

**Example 1: Opens are 19% at T+24hr (YELLOW)**
- Use this doc: Part 2, Checkpoint 2 → leads to YELLOW branch
- Use Alert Procedures: PROCEDURE 2, step 2 → A/B subject line recommendation
- Use this doc: Part 9 to execute the A/B test

**Example 2: Clicks are <1% (RED) despite 24% opens**
- Use this doc: Part 2, Checkpoint 3 → leads to RED branch
- Use Alert Procedures: PROCEDURE 3, step 1 → CTA audit checklist
- Use this doc: Part 5, Scenario 2 → detailed CTA audit framework
- Use Part 6 to document escalation

**Example 3: Unsubscribe rate spikes to 0.7% (RED)**
- Use this doc: Part 2, Checkpoint 4 → leads to RED branch
- Use Alert Procedures: PROCEDURE 4, steps 1–2 → identify trigger
- Use this doc: Part 5, Scenario 4 → detailed root cause and actions
- Use Part 6 to escalate to user

---

## Quick Reference: Daily Checklist (Abbreviated)

Print or bookmark this abbreviated version for daily use.

### Pre-Send (1 hour before 13:00 UTC send)

- [ ] Sender email verified (domain matches prior sends)
- [ ] Recipient list confirmed (count ±2%)
- [ ] Subject line: no ALL CAPS, no spam phrases
- [ ] Email images: all public URLs, all load in preview
- [ ] CTA text: action-oriented (Get, Download, View)
- [ ] CTA link: resolves to live Etsy, no 404
- [ ] Unsubscribe link: present and functional
- [ ] Send time: 13:00 UTC confirmed
- [ ] Backup email saved locally
- [ ] Approval initials logged in EXECUTION_LOG.md

### T+1hr (14:00 UTC)

- [ ] Delivery rate >95%? → GREEN. Proceed.
- [ ] Delivery rate 90–95%? → YELLOW. Log action. Continue.
- [ ] Delivery rate <90%? → RED. Escalate (PROCEDURE 1).

### T+24hr (13:00 UTC next day)

- [ ] Open rate >22%? → GREEN. Log. Proceed.
- [ ] Open rate 15–22%? → YELLOW. A/B subject line for next email.
- [ ] Open rate <15%? → RED. Run spam test. Escalate.
- [ ] Click rate >3%? → GREEN. Log. Proceed.
- [ ] Click rate 1–3%? → YELLOW. Audit CTA (Part 5, Scenario 2).
- [ ] Click rate <1% (AND opens GREEN)? → RED. Fix CTA (Part 5, Scenario 2).
- [ ] Both opens & clicks low? → RED. Spam test + list analysis (Part 5, Scenario 3).

### Daily at 22:00 UTC

- [ ] Unsubscribe count (last 24hr): [NUMBER]
- [ ] Daily rate % = [COUNT] / [TOTAL SUBSCRIBERS] × 100
- [ ] <0.3%? → GREEN. Log. No action.
- [ ] 0.3–0.5%? → YELLOW. Monitor 3 days. Log reasons.
- [ ] >0.5%? → RED. Identify trigger. Escalate (PROCEDURE 4).

### Every Email

- [ ] Log in PHASE_3_EXECUTION_LOG.md: date, campaign name, send time, recipient count, delivery %, open %, click %, unsubscribe %, status (GREEN/YELLOW/RED), actions taken, notes
- [ ] If RED: complete escalation form (Part 6) and contact primary owner

---

## Appendix: Phase 3 Q3 Bundle Send Schedule

| Email # | Bundle | Launch Date | Send Time ET | Kit.com Send Time UTC | Expected Recipients | Baseline Open % | Baseline Click % | A/B Test Needed? |
|---|---|---|---|---|---|---|---|---|
| 1 | Women's Health | Jun 29 | 08:00 AM | 13:00 (12:00 PT) | 8,000 | 24% | 4% | N |
| 2 | Respiratory Health | Jul 6 | 08:00 AM | 13:00 | 8,165 | 23% | 3.5% | Y |
| 3 | Sleep and Nervines | Jul 13 | 08:00 AM | 13:00 | 8,249 | 22% | 3.2% | Y (fatigue check) |
| 4 | Immunity Support | Jul 20 (or adjusted +7d if fatigue) | 08:00 AM | 13:00 | 8,271 | 23% | 3.5% | Y |
| 5 | Digestive Support | Aug 3 | 08:00 AM | 13:00 | 8,299 | 25% | 4% | N |
| 6 | Re-engagement (if fatigue) | Per PROC5 (between Email 3–4) | 08:00 AM | 13:00 | Variable (cold segment) | 15–18% | 2% | N |

---

## Version Control & Updates

**Document version**: 1.0  
**Created**: 2026-06-29  
**Last updated**: 2026-06-29  
**Next review**: 2026-07-15 (after Email 2 data in)  
**Owner**: Seedwarden Phase 3 Project Lead  

**Change log**:
- 2026-06-29: Initial version created. All 10 sections complete, actionable, no placeholders.

---

*This document is production-ready. Use it daily during Phase 3 Q3 launches (June 29 – August 3 and post-launch monitoring through August 31). All thresholds are based on Q2 2026 construction-audience baseline (22–28% expected opens, 3–5% expected clicks). After Week 1 data arrives, compare actual metrics to baseline and update thresholds in Part 3 if needed.*
