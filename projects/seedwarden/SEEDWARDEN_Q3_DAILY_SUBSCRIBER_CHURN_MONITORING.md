---
title: "Seedwarden Q3 Daily Subscriber Churn Monitoring — Phase 3 Launches"
date: 2026-06-29
version: 1.0
status: production-ready
sprint-window: June 29 – September 30, 2026
execution-ready: YES
scope: "Daily unsubscribe tracking, churn analysis, retention workflows, segment health for Phase 3 Q3 launches"
cross-references:
  - PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md (Procedure 4: Unsubscribe thresholds)
  - SEEDWARDEN_PHASE_3_WEEK_1_MONITORING_DASHBOARD.md (daily email metrics integration)
  - phase-2-kit-broadcast-copy.md (email campaign context)
---

# Seedwarden Q3 Daily Subscriber Churn Monitoring

**Purpose**: Real-time tracking of daily unsubscribe rates, churn reasons, and subscriber list health during Phase 3 Q3 launches (June 29 – September 30, 2026). This document operationalizes subscriber retention, provides decision thresholds, and enables rapid response to churn spikes.

**Update cadence**:
- **Daily check**: 22:00 UTC (immediately after day closes)
- **Weekly summary**: Every Monday 8:00 AM UTC
- **Segment analysis**: Weekly (Mondays)
- **Content team escalation**: Within 2 hours of RED threshold

**Data sources**:
- Kit.com > Subscribers > Unsubscribes (filter by last 24 hours)
- Kit.com > Subscribers > Unsubscribe Reasons (reason breakdown)
- Kit.com > Subscribers > List Health (engagement segmentation)
- Kit.com > Campaigns > Open/Click rates (correlation analysis)

---

## DAILY MONITORING TEMPLATE (CSV-STYLE)

### Columns & Definitions

| Column | Definition | Source | Notes |
|--------|-----------|--------|-------|
| **Date (UTC)** | Date in YYYY-MM-DD format | Calendar | Previous day (e.g., monitor on 2026-06-30 for 06-29 data) |
| **Total Subscribers** | Active subscriber count (end of day) | Kit.com > Account | "Active" = confirmed + unconfirmed, not suppressed |
| **Unsubscribes (Count)** | Number of unsubscribes in 24-hour window | Kit.com > Unsubscribes | Filter: last 24 hours; exclude manual suppressions |
| **Unsub Rate (%)** | (Unsubscribes / Total Subscribers) × 100 | Calculated | Two decimal places (e.g., 0.35%) |
| **Too Many Emails (%)** | % of unsubscribes citing frequency | Kit.com > Reason | Of that day's unsub count; bold if >20% |
| **Not Relevant (%)** | % citing content mismatch | Kit.com > Reason | Of that day's unsub count; bold if >20% |
| **Prefer Other Format (%)** | % citing format preference | Kit.com > Reason | Of that day's unsub count |
| **Other/Blank (%)** | % providing no reason or "other" | Kit.com > Reason | Of that day's unsub count |
| **Correlated Email Send?** | Was an email sent same day or day-1? | Kit.com > Campaigns | Note subject line + send time if YES |
| **Notes** | Context, action taken, flags | Manual | Escalation status, segment analysis, etc. |
| **Status** | GREEN / YELLOW / RED threshold | Threshold logic | Applied at monitoring time |

### CSV Template (30-Day Baseline)

```
Date,Total_Subscribers,Unsubscribes_Count,Unsub_Rate_%,Too_Many_Emails_%,Not_Relevant_%,Prefer_Other_Format_%,Other_%,Correlated_Send?,Notes,Status
2026-06-29,3250,7,0.22,"0","0","0","100",No,Women's Health launch email sent 9am same day; low unsub rate expected,GREEN
2026-06-30,3243,8,0.25,"25","25","0","50",Yes,"Day after Women's Health email; slight uptick expected; monitor 3 days",GREEN
2026-07-01,3235,9,0.28,"33","22","0","44",No,No send today; checking if trend continues; within normal range,GREEN
2026-07-02,3226,10,0.31,"30","20","10","40",No,Three consecutive days 0.25-0.31%; approaching YELLOW threshold; monitor closely,YELLOW
2026-07-03,3216,11,0.34,"27","27","9","36",No,Sustained 0.3%+ for 3 days; trending toward YELLOW on day 4; investigate pending,YELLOW
2026-07-04,3206,12,0.37,"33","25","8","33",No,Still elevated; 0.37% = sustained YELLOW; segment analysis ordered for Monday,YELLOW
2026-07-05,3196,11,0.34,"36","27","0","36",No,5-day window: avg 0.31% (elevated); run list health check TODAY,YELLOW
2026-07-06,3186,6,0.19,"0","17","0","83",Yes,Respiratory launch email sent 9am; sharp DROP to GREEN after YELLOW hold; likely purge effect,GREEN
2026-07-07,3180,8,0.25,"25","25","13","38",No,Day after Respiratory send; normal rate; no action,GREEN
2026-07-08,3172,6,0.19,"0","33","17","50",No,Trending toward normal; no correlation; GREEN,GREEN
2026-07-09,3165,7,0.22,"29","29","0","43",No,Normal rate continues,GREEN
2026-07-10,3158,5,0.16,"0","40","20","40",No,Very low; list quality improving post-purge,GREEN
2026-07-11,3152,6,0.19,"33","17","0","50",No,Stable; no action,GREEN
2026-07-12,3146,7,0.22,"14","29","0","57",No,Sleep & Nervines launch day; expect minor uptick,GREEN
2026-07-13,3139,8,0.25,"25","25","13","38",Yes,Day after Sleep launch; within normal; trending normal,GREEN
```

---

## UNSUBSCRIBE THRESHOLD DEFINITION & DECISION TREE

### Threshold Definitions (from PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md Procedure 4)

```
GREEN ZONE:    Daily unsub rate <0.3%
               Action: Log and monitor. No escalation.

YELLOW ZONE:   Daily unsub rate 0.3–0.5%
               Action: Monitor 3 consecutive days.
               If sustained 3+ days WITHOUT new send: escalate to RED.
               If correlated to single send: investigate that email.

RED ZONE:      Daily unsub rate >0.5%
               Action: Investigate immediately (within 2 hours).
               Isolate root cause. Run list health check same day.
```

### Decision Tree for YELLOW/RED

```
START: Daily unsubscribe rate >0.3%
│
├─→ YELLOW TRIGGER DETECTED (0.3–0.5%)
│   │
│   ├─→ STEP 1: Check email send correlation
│   │   ├─→ YES: Email sent same day or day-1 (see subject/time)
│   │   │   │ • Note the email subject, send time, content tone
│   │   │   │ • Record in daily log
│   │   │   │ • Monitor for 3 days
│   │   │   │ • If rate stays 0.3–0.5% on day 3: escalate to RED
│   │   │   │ • If rate drops below 0.3%: likely one-time send spike (close)
│   │   │   └─ PROCEED TO STEP 3 (unsub reason analysis)
│   │   │
│   │   └─→ NO: No send correlation
│   │       │ • Record "no recent send"
│   │       │ • Check Kit.com 7-day unsub report
│   │       │ • Continue to STEP 3
│   │       └─ PROCEED TO STEP 3
│   │
│   ├─→ STEP 3: Analyze unsub reason breakdown
│   │   ├─→ IF >20% say "too many emails":
│   │   │   │ • Note frequency problem
│   │   │   │ • Draft frequency adjustment message (see retention templates below)
│   │   │   │ • Prepare to send to engaged segment only
│   │   │   └─ Continue monitoring; review next send cadence
│   │   │
│   │   ├─→ IF >20% say "not relevant":
│   │   │   │ • Note content mismatch
│   │   │   │ • Check if unsubs are concentrated in a segment (new vs. long-term)
│   │   │   │ • May indicate list quality issue
│   │   │   └─ Continue to STEP 4 if sustained YELLOW
│   │   │
│   │   └─→ IF >20% say "prefer other format":
│   │       │ • Possible list issue (form sign-up led to wrong expectation)
│   │       │ • Low priority unless combined with high "not relevant"
│   │       └─ Continue monitoring
│   │
│   └─→ STEP 4: Set monitoring window
│       │ • Monitor 3 consecutive calendar days
│       │ • If rate drops below 0.3% by day 3: CLOSE, log as transient
│       │ • If rate stays or climbs on day 3: ESCALATE to RED
│       │ • If new send occurs during window: restart 3-day count after new send
│       └─ Continue to monitoring log
│
│
├─→ RED TRIGGER DETECTED (>0.5%)
│   │
│   ├─→ STEP 1: Immediate email send correlation check
│   │   ├─→ YES: Email sent same day or day-1
│   │   │   │ • Pull that email's subject, send time, recipient count
│   │   │   │ • Extract email body (content tone, images, links)
│   │   │   │ • Analyze: Was it promotional? Too frequent? Tone mismatch?
│   │   │   │ • Note key finding (e.g., "promotional tone triggered fatigue")
│   │   │   │ • ESCALATE to content team within 2 hours (email text + finding)
│   │   │   └─ PROCEED TO STEP 3
│   │   │
│   │   └─→ NO: No recent send; gradual accumulation
│   │       │ • Record "no send correlation"
│   │       │ • Suggests underlying list health issue
│   │       │ • Check Kit.com 7-day trend (gradual vs. spike)
│   │       └─ PROCEED TO STEP 3
│   │
│   ├─→ STEP 3: Run list health check (Kit.com)
│   │   ├─→ CHECK: Unconfirmed subscribers
│   │   │   ├─→ IF >15% unconfirmed:
│   │   │   │   │ • Log count and % of total
│   │   │   │   │ • These are low-intent or stale; remove immediately
│   │   │   │   │ • Kit.com > Subscribers > filter "Unconfirmed" > export > suppress
│   │   │   │   └─ Document removal: "Removed X unconfirmed (Y% of list)"
│   │   │   │
│   │   │   └─→ IF ≤15% unconfirmed:
│   │   │       └─ No action; proceed to Cold check
│   │   │
│   │   ├─→ CHECK: Cold subscribers (no opens in 90 days)
│   │   │   ├─→ IF >25% cold:
│   │   │   │   │ • List engagement is severely degraded
│   │   │   │   │ • Suppress these from current + next 2 sends
│   │   │   │   │ • Kit.com > Subscribers > filter "Cold" > add to "Do Not Send" segment
│   │   │   │   └─ Document action: "Suppressed Z cold subscribers for 2 sends"
│   │   │   │
│   │   │   └─→ IF 10–25% cold:
│   │   │       │ • Normal for growing lists
│   │   │       │ • Run re-engagement campaign after RED issue resolves
│   │   │       └─ Document for post-RED action plan
│   │   │
│   │   └─→ STEP 3 RESULT: Document pre-clean and post-clean counts
│   │       │ • Pre-clean total: X subscribers
│   │       │ • Removed unconfirmed: Y
│   │       │ • Suppressed cold: Z
│   │       │ • Post-clean total: (X - Y - Z)
│   │       └─ Log in PHASE_3_EXECUTION_LOG.md
│   │
│   ├─→ STEP 4: Analyze unsubscribe reason breakdown
│   │   ├─→ IF >20% say "too many emails":
│   │   │   │ • Draft FREQUENCY RETENTION message (template below)
│   │   │   │ • Target: High-engagement segment (opened 2/last 3 sends)
│   │   │   │ • Timeline: Send within 48 hours of RED resolution
│   │   │   │ • Goal: Re-opt-in to adjusted cadence (fewer, better emails)
│   │   │   └─ Schedule for content team approval
│   │   │
│   │   ├─→ IF >20% say "not relevant":
│   │   │   │ • Draft CONTENT RELEVANCE message (template below)
│   │   │   │ • Target: Segment by content preference (if available)
│   │   │   │ • Or: Engaged segment (opened 2/last 3 sends)
│   │   │   │ • Timeline: Send within 48 hours of RED resolution
│   │   │   │ • Goal: Show content is changing; re-engage
│   │   │   └─ Schedule for content team approval
│   │   │
│   │   └─→ IF >20% say "prefer other format":
│   │       │ • May indicate form/acquisition issue
│   │       │ • Lower priority than "too many" or "not relevant"
│   │       │ • Review next opt-in flow; less immediate action needed
│   │       └─ Continue monitoring; address in next acquisition sprint
│   │
│   ├─→ STEP 5: Segment analysis
│   │   │ • Identify: Which segment(s) have highest unsub rate?
│   │   │   - New subscribers (0–7 days): if >2.0%, new opt-in flow problem
│   │   │   - Long-term (>30 days): if >0.8%, content or frequency issue
│   │   │   - High-engagement (2+ recent opens): if any unsub, note tone problem
│   │   │   - Cold (no opens in 90 days): ignore; suppress separately
│   │   │ • Run retention campaign vs. main list?
│   │   │   - YES if unsub is isolated to one segment (e.g., only new subscribers)
│   │   │   - NO if unsub is uniform across all segments (systemic issue)
│   │   └─ Document segment findings
│   │
│   └─→ STEP 6: Escalation & response timeline
│       │ • NOTIFY content team within 2 hours: send email with
│       │   - Unsub spike details (rate, count, day detected)
│       │   - Unsubscribe reason breakdown (%)
│       │   - Correlated email (if any) with subject/tone analysis
│       │   - Segment analysis (affected segments)
│       │   - Proposed retention messaging (draft template)
│       │ • RESPONSE SLA: Content team to revise messaging within 48 hours
│       │ • SEND: Revised retention message to target segment (48–72 hours)
│       │ • MONITOR: Track unsub rate for 3 days post-send
│       │ • DOCUMENT: Full escalation + resolution in PHASE_3_EXECUTION_LOG.md
│       └─ Log RED closure
│
└─ END: Status logged in daily monitoring template
```

---

## INVESTIGATION FLOWCHART FOR YELLOW/RED SPIKES

### Process Flowchart (Visual)

```
DAILY UNSUB RATE CALCULATED AT 22:00 UTC
│
├─ Rate <0.3%? → GREEN (Log & close)
│
├─ Rate 0.3–0.5%? → YELLOW
│  │
│  ├─ Step 1: Was email sent same-day or day-1?
│  │  ├─ YES → Note email details → Monitor 3 days
│  │  └─ NO  → Pull 7-day trend → Gradual or spike?
│  │
│  ├─ Step 2 (if email sent): Analyze that email
│  │  ├─ Subject line tone?
│  │  ├─ Content promotional vs. educational?
│  │  ├─ Send frequency (how many days since prior email)?
│  │  └─ Note findings
│  │
│  ├─ Step 3: Analyze unsub reason breakdown
│  │  ├─ >20% "too many emails"? → Frequency issue
│  │  ├─ >20% "not relevant"? → Content issue
│  │  └─ >20% "prefer other format"? → Acquisition issue
│  │
│  └─ Step 4: Monitor for 3 days
│     ├─ If rate drops <0.3% → CLOSE (transient spike)
│     ├─ If rate stays 0.3–0.5% on day 3 → ESCALATE to RED
│     └─ If new send occurs → Restart 3-day count post-send
│
├─ Rate >0.5%? → RED (IMMEDIATE ACTION)
│  │
│  ├─ Step 1: Identify email send correlation (same day or day-1)
│  │  ├─ YES → Pull email details
│  │  │        ├─ Subject: _____
│  │  │        ├─ Tone: promotional / educational / mixed?
│  │  │        ├─ Frequency context: days since last send?
│  │  │        └─ → ESCALATE to content team within 2 hours
│  │  │
│  │  └─ NO  → Log "no send correlation"
│  │           ├─ Check 7-day trend: gradual or sudden spike?
│  │           ├─ Suggests list quality issue
│  │           └─ Proceed to Step 3 (list health check)
│  │
│  ├─ Step 3: Run list health check (Kit.com, SAME DAY)
│  │  ├─ Unconfirmed: >15%?
│  │  │  ├─ YES → REMOVE immediately
│  │  │  └─ NO  → Proceed
│  │  │
│  │  ├─ Cold (no opens 90 days): >25%?
│  │  │  ├─ YES → SUPPRESS from next 2 sends
│  │  │  └─ NO  → Document for post-RED action
│  │  │
│  │  └─ Document pre/post-clean counts
│  │
│  ├─ Step 4: Analyze unsub reason breakdown
│  │  ├─ If >20% "too many emails" → Draft frequency adjustment message
│  │  ├─ If >20% "not relevant" → Draft content relevance message
│  │  └─ Schedule both for content team review (48hr SLA)
│  │
│  ├─ Step 5: Segment analysis
│  │  ├─ Is unsub isolated to one segment? (new vs. long-term, source, engagement)
│  │  ├─ Run targeted retention campaign if isolated
│  │  └─ Document segment breakdown
│  │
│  ├─ Step 6: Escalate & await response
│  │  ├─ Send escalation email to content team: rate, reasons, email details, segment analysis
│  │  ├─ Response SLA: 48 hours for revised messaging
│  │  ├─ Send revised retention message: 48–72 hours post-resolution
│  │  └─ Monitor unsub rate for 3 days post-send
│  │
│  └─ Step 7: Log full resolution in PHASE_3_EXECUTION_LOG.md
│     ├─ Date spike detected: _____
│     ├─ Peak rate: _____
│     ├─ Root cause: _____
│     ├─ Action taken: _____
│     ├─ Outcome: _____
│     └─ Resolution date: _____

```

### Step-by-Step Investigation Procedure

**YELLOW Trigger (0.3–0.5% rate sustained 3+ days)**

1. **Email Send Correlation**
   - Check Kit.com > Campaigns > last 7 days
   - Was an email sent same day as unsub spike, or day before?
   - Record: YES [date/time, subject] or NO
   - If YES: proceed to "Email Analysis" below
   - If NO: proceed to "Reason Breakdown Analysis"

2. **Email Analysis (if YES to send correlation)**
   - Pull that email's metadata:
     - Subject line (copy verbatim)
     - Send time (UTC)
     - Recipient count
     - Content tone: Is it primarily promotional, educational, or mixed?
     - CTA (call-to-action): How many links? How explicit?
     - Send frequency context: How many days since previous email?
   - Assessment: Does this email explain the unsub spike?
     - Promotional tone + 2 emails in 5 days = likely frequency fatigue
     - Educational tone + low historical unsub = possible content mismatch
   - Document finding in YELLOW log

3. **Reason Breakdown Analysis**
   - Kit.com > Unsubscribes > Reason (filter: last 24 hours)
   - Tally counts for that day:
     - "Too many emails" (count + %)
     - "Not relevant" (count + %)
     - "Prefer other format" (count + %)
     - "Other" / blank (count + %)
   - If any reason >20% of daily unsubs:
     - Flag the dominant reason
     - Plan follow-up retention campaign
   - Document in YELLOW log

4. **Monitor for 3 Consecutive Days**
   - Starting day of YELLOW trigger, monitor rates for next 3 calendar days
   - If rate drops below 0.3% by day 3: CLOSE yellow (transient spike)
   - If rate stays 0.3–0.5% or climbs on day 3: ESCALATE to RED
   - If new email send during 3-day window: Reset 3-day monitoring from day after new send
   - Document 3-day trend in log

**RED Trigger (>0.5% rate, immediate action within 2 hours)**

1. **Email Send Correlation (IMMEDIATE)**
   - Check Kit.com > Campaigns > last 24-48 hours
   - Was an email sent same day or yesterday?
   - Record: YES [date, subject] or NO
   - This is your **root cause hypothesis**

2. **If YES to Email Send: Pull Email Details**
   - Subject line
   - Send time (UTC)
   - Body content (tone, images, links)
   - Recipient count
   - Recent send frequency (how many days since prior email?)
   - Assessment:
     - Promotional email after 2-day gap = **frequency fatigue** (likely cause)
     - Email tone doesn't match list expectation = **content mismatch**
     - High-image email or long body = **readability issue**
   - **ESCALATE to content team within 2 hours** with these details

3. **If NO to Email Send: List Health is Primary Issue**
   - Note: "Sustained RED without recent send = list quality problem"
   - Proceed immediately to Step 4 (list health check)
   - Run check same day to isolate issue

4. **Run List Health Check (Same Day)**
   - Open Kit.com > Subscribers
   - **Check 1: Unconfirmed subscribers**
     - Filter: "Status = Unconfirmed"
     - Count total unconfirmed
     - Calculate % of total list
     - If >15% of list: **REMOVE immediately** (low-intent, stale opt-ins)
       - Kit.com > Subscribers > filter "Unconfirmed" > export to CSV > add to suppression list
       - Log: "Removed X unconfirmed (Y% of list) — [date]"
   - **Check 2: Cold subscribers (no opens in 90 days)**
     - Filter: "Last Opened > 90 days ago" (or "Never opened" if new)
     - Count total cold subscribers
     - Calculate % of total list
     - If >25% of list: **SUPPRESS from next 2 sends**
       - Kit.com > Subscribers > filter "Cold" > create "Cold_DoNotSend_[date]" segment
       - Add to suppression list for next 2 campaigns
       - Log: "Suppressed Z cold subscribers for 2 sends — [date]"
     - If 10–25% cold: **Document for post-RED action** (run re-engagement later)
   - **Record pre-clean and post-clean counts:**
     - Before: X total subscribers
     - After: X - unconfirmed_removed - cold_suppressed = clean total
     - Delta impact: "[Removed Y% of list]"

5. **Analyze Unsubscribe Reason Breakdown**
   - Kit.com > Unsubscribes > Reason (filter: last 24 hours or 48 hours for RED)
   - For each reason, record count + % of daily unsubs:
     - "Too many emails": ___ count, ___ %
     - "Not relevant": ___ count, ___ %
     - "Prefer other format": ___ count, ___ %
     - "Other" / blank: ___ count, ___ %
   - **Identify dominant reason(s)**
     - If >20% "too many emails": **Frequency problem** → Draft frequency adjustment message
     - If >20% "not relevant": **Content problem** → Draft content relevance message
     - Multiple >20%: Draft BOTH messages

6. **Segment Analysis**
   - Is the RED unsub rate concentrated in one subscriber segment, or uniform?
   - Check segments:
     - **New subscribers** (0–7 days old): If unsub rate >2.0%, opt-in flow problem
     - **Early segment** (8–30 days old): If unsub rate >0.8%, content expectation mismatch
     - **Long-term** (>30 days old): If unsub rate >0.4%, content fatigue or frequency issue
     - **High-engagement** (opened 2+ recent sends): If any unsub, tone/content mismatch
     - **Cold** (no opens 90 days): Expected high unsub; suppress (already done in Step 4)
   - **Decision**: Run retention campaign vs. main list?
     - YES: If unsub is isolated (>60% of unsubs from one segment)
       - Example: "Only new subscribers unsubbing after initial email → issue is opt-in flow"
     - NO: If unsub is uniform across all segments (systemic issue)
       - Example: "All segments unsubbing equally → content tone or list quality issue"
   - Document segment breakdown

7. **Escalation & Notification (Within 2 Hours)**
   - **Send escalation email to content team** with:
     - **Subject**: RED Unsubscribe Alert — Action Required [Date]
     - **Content**:
       - Current unsub rate: X.XX% (RED threshold >0.5%)
       - Daily unsub count: Y
       - Is there a correlated email send? YES [subject, tone] / NO [list health issue]
       - Unsubscribe reason breakdown (% of unsubs): too many emails _%, not relevant _%, other _%
       - Segment analysis: Is this isolated to one segment? Yes [segment] / No [uniform]
       - Proposed root cause: [frequency fatigue / content mismatch / list quality / etc.]
       - Proposed retention messaging: [See templates below; draft provided]
       - **Response SLA**: Content team to revise messaging within 48 hours
       - **Send timeline**: Revised message to target segment 48–72 hours post-escalation
   - **Track escalation** in daily log with timestamp

8. **Monitor & Re-Evaluate**
   - After retention message is sent (if applicable): Monitor unsub rate for 3 days
   - If rate drops below 0.5%: RED is closed; revert to standard monitoring
   - If rate stays >0.5%: Escalate to contingency procedures (see PHASE_3_CONTINGENCY_TRIGGERS.md)
   - Document full resolution in PHASE_3_EXECUTION_LOG.md

---

## UNSUBSCRIBE REASON CATEGORIZATION (Kit.com Categories)

Kit.com provides the following unsubscribe reason options in the unsubscribe interface:

### Standard Reasons (from Kit.com)

1. **"Too many emails"**
   - Subscriber is receiving more emails than they want
   - Indicates: Frequency problem (emails too close together or bundled sends perceived as excessive)
   - Action if >20% of unsubs: Review send cadence; consider frequency preference option in next welcome sequence
   - Retention messaging: Frequency adjustment (template below)

2. **"Not relevant"**
   - Subscriber says email content doesn't match their interests
   - Indicates: Content mismatch (either in acquisition, segmentation, or content strategy)
   - Action if >20% of unsubs: Check if unsubs are concentrated in new segment (acquisition issue) or long-term (content drift)
   - Retention messaging: Content relevance (template below)

3. **"Prefer other format"**
   - Subscriber wants email in a different format (e.g., digest instead of individual sends, text-only instead of HTML)
   - Indicates: Delivery format mismatch
   - Action if >20% of unsubs: Review next welcome sequence; offer format options upfront
   - Retention messaging: N/A (format preference can't be changed retroactively; address in acquisition)

4. **"Other"** (Open-text reason provided)
   - Subscriber provides custom text reason
   - Common examples: "Changing email providers", "Subscribing to too many lists", "No longer interested in this topic", "Prefer content on [platform]"
   - Action: Skim "Other" responses monthly; if pattern emerges, add new category or respond

5. **No reason / Blank**
   - Subscriber skipped reason selection (default Kit.com behavior)
   - Indicates: Anonymous unsub; no data to act on
   - Action: Log; no follow-up possible

---

## RETENTION MESSAGING TEMPLATES

### Template 1: Frequency Adjustment Message

**When to use**: When >20% of unsubs cite "too many emails" or sustained YELLOW/RED is correlated with high-frequency sends.

**Target segment**: High-engagement subscribers (opened 2 of last 3 sends) + long-term subscribers (>14 days)

**Send timing**: Within 48–72 hours of RED resolution or YELLOW decision to adjust cadence.

**Subject line**: Choose one:
- "You'll hear from us less often — here's what's changing"
- "We're slowing down: fewer emails, more value"
- "One request: let's adjust our email frequency together"

**Email body**:

```
Subject: You'll hear from us less often — here's what's changing

Hi [First Name],

We noticed some of you have mentioned emails are coming too frequently. 
We hear you, and we're making a change.

Starting [date], we're shifting to [describe new cadence]:
- Instead of X emails per week: now Y emails per week
- Still the same bundle launches and education
- But with more space between sends so you can actually read them

This means:
✓ More time to explore each bundle
✓ Fewer "inbox pile-ups" from us
✓ Same high-quality, science-backed content

We still think you're in the right place here. If you'd like to stay 
but with even fewer emails, reply to this message — we can customize 
a frequency that works for you.

Thanks for being here.

[Signature]

---
P.S. If you're unsubscribing anyway, we totally understand. 
No hard feelings. We hope to see you again if your needs change.
```

**Metrics to track**:
- Conversion rate (how many reply with custom frequency request?)
- Re-opens of this message (interest indicator)
- Unsub rate in 3 days post-send (did frequency adjustment help?)

---

### Template 2: Content Relevance Message

**When to use**: When >20% of unsubs cite "not relevant" or when content mismatch is suspected (e.g., unsubs concentrated in new subscriber segment).

**Target segment**: Engaged subscribers (opened recent sends) + new subscribers if acquisition issue suspected.

**Send timing**: Within 48–72 hours of RED resolution.

**Subject line**: Choose one:
- "Here's what's changing in the emails you're about to see"
- "We heard you: here's our 3-month content update"
- "The herbal content we're launching next (and why it matters)"

**Email body**:

```
Subject: Here's what's changing in the emails you're about to see

Hi [First Name],

A few of you mentioned that recent emails didn't feel relevant. 
We want to fix that.

Here's what's coming in the next 8 weeks:

JULY:
• Women's Health Bundle (menstrual cycle support, hormonal balance)
• Respiratory Health Bundle (seasonal immunity, clear airways)

AUGUST:
• Sleep & Nervines Bundle (deep rest, nervous system calm)
• Digestive Support Bundle (gut health, inflammation)

SEPTEMBER:
• Immunity Support Bundle (year-round defense, lymphatic flow)
• Specialty guides (endangered species, ethical harvesting, sustainability)

Each bundle includes:
✓ Science-backed herbal protocols
✓ Ethical sourcing & sustainability practices
✓ Beautiful, actionable guide for your home practice

If this still isn't your thing, we understand. If it IS, great — 
we think you'll love what's coming.

Let us know what you want to see.

[Signature]

---
P.S. Reply to this email with topics YOU want us to cover. 
We're taking requests for October.
```

**Metrics to track**:
- Click rate on bundle links (re-engagement)
- Replies with content requests (engagement signal)
- Unsub rate in 3 days post-send (did content clarity help?)

---

### Template 3: Re-Engagement Message

**When to use**: When a subscriber segment has gone cold (no opens in 3+ sends) and RED is resolved. Run as a separate campaign to the "Cold" suppressed segment.

**Target segment**: Subscribers who did NOT open any of the last 3 emails, but have not unsubscribed.

**Send timing**: After RED resolution and list health cleanup, as a dedicated re-engagement email.

**Subject line**: Choose one:
- "We've been launching guides — did you miss them?"
- "3 new herbal bundles just launched (you missed the first 2)"
- "Quick recap: what you've missed in the last month"

**Email body**:

```
Subject: We've been launching guides — did you miss them?

Hi [First Name],

We haven't heard from you in a bit, so we wanted to catch you up.

Over the last 4 weeks, we've launched three herbal bundles:

→ WOMEN'S HEALTH BUNDLE
   Hormonal balance, menstrual support, stress resilience
   [LINK: etsy.com/listing/xxx]

→ RESPIRATORY HEALTH BUNDLE
   Clear airways, seasonal immunity, lung capacity
   [LINK: etsy.com/listing/xxx]

→ SLEEP & NERVINES BUNDLE
   Deep rest, nervous system calm, stress recovery
   [LINK: etsy.com/listing/xxx]

Each guide is researched, beautifully designed, and practical.

**Two things**:

1. If you're still interested in herbal medicine, 
   click any bundle above to explore. These are solid, thoughtful guides.

2. If you're not sure anymore about emails from us — totally fine. 
   Just reply and let us know, and we'll adjust or remove you without fuss.

We'd love to have you back engaged, but only if it feels right for you.

[Signature]

---
P.S. New launches are coming in August. If you want back in, 
you'll hear about them first.
```

**Metrics to track**:
- Open rate (are they still reading?)
- Click rate (are they exploring the guides?)
- Reply rate (engagement signal for segmentation)
- Unsub rate (final decision from cold segment)

**Post-campaign action**:
- If unsub rate from this re-engagement >0.3%: Do not send further emails to this segment for 2 weeks
- If click rate >10%: Re-engage segment is viable; continue sends at normal cadence
- If no engagement after 2 sends: Suppress for 30 days; run re-engagement again in 30 days

---

## CONTENT TEAM COORDINATION WORKFLOW

### When to Escalate (RED Threshold)

**Trigger**: Daily unsub rate >0.5% OR sustained YELLOW (0.3–0.5%) for 3+ days.

**Immediate action (within 2 hours of detection)**:
1. Send escalation email to content team
2. Include all details from investigation flowchart (Step 7 above)
3. Propose retention messaging (use templates above as draft)

### Escalation Email Template

**To**: [Content team email] (or dedicated Slack channel if available)

**Subject**: RED Unsubscribe Alert — Action Required [Date]

**Content**:

```
UNSUBSCRIBE ALERT — RED THRESHOLD

Current Status: Daily unsub rate X.XX% (RED = >0.5%)
Detected: [Date] at 22:00 UTC
Total unsubs today: Y count

ROOT CAUSE ANALYSIS:

Email Send Correlation?
[ ] YES — Email "[Subject]" sent [date/time]
    Tone: [promotional/educational]
    Frequency context: [days since prior email]
    Assessment: [frequency fatigue / content tone issue / other]

[ ] NO — No recent email send
    List health issue suspected
    Cold subscribers: Z% of list
    Unconfirmed: A% of list
    Action taken: [suppressions made / removals completed]

UNSUB REASON BREAKDOWN:
- Too many emails: ___% [>20%? Y/N]
- Not relevant: ___% [>20%? Y/N]
- Prefer other format: ___% [>20%? Y/N]
- Other/blank: ___% [>20%? Y/N]

SEGMENT ANALYSIS:
- New subscribers (0–7 days): ___ unsubs | ___ rate
- Early segment (8–30 days): ___ unsubs | ___ rate
- Long-term (>30 days): ___ unsubs | ___ rate
- High-engagement: ___ unsubs | ___ rate
→ Isolated to one segment? YES [segment] / NO [uniform]

PROPOSED RETENTION MESSAGING:
Template: [Frequency Adjustment / Content Relevance / Re-engagement]
Target segment: [high-engagement / new / long-term / other]
Send timing: [within 48–72 hours]

RESPONSE SLA:
Please revise messaging and confirm send date by [date + 48hrs]

QUESTIONS FOR CONTENT TEAM:
1. Does this root cause match your recent email strategy decisions?
2. Should we adjust send cadence going forward?
3. Are there content changes planned that might explain "not relevant" reasons?

Contact: [Your name / Monitoring team contact]
```

### What Info to Provide to Content/Product Team

When escalating RED or requesting intervention on YELLOW:

**Always include**:
1. **Unsub metric**: Daily rate (%), daily count, trend (climbing/stable/resolved)
2. **Timing**: When detected, 3-day trend if applicable
3. **Correlation data**: Email subject, send time, content tone (promotional/educational), days since prior email
4. **Reason breakdown**: % citing "too many emails", "not relevant", etc. (highlight if >20% any reason)
5. **Segment breakdown**: Which segments are unsubbing most (new vs. long-term, by source if available)
6. **Root cause hypothesis**: Frequency fatigue / content mismatch / list quality / other
7. **List health findings**: Unconfirmed %, cold %, actions taken
8. **Proposed solution**: Which retention template fits? What's the target segment?

**Optional (if helpful)**:
- Historical unsub rate for this time period (is this normal for a launch phase?)
- Link to that email in Kit.com (for content team to review tone/copy)
- Any subscriber feedback from replies/surveys (if available)

### Timeline for Content Team Response

**SLA for YELLOW**:
- No immediate escalation required
- Monitor for 3 days
- If sustained on day 3, escalate to RED procedures

**SLA for RED**:
- **2-hour notification**: Send escalation email immediately upon RED detection
- **24-hour acknowledgment**: Content team confirms receipt and notes any blocking issues
- **48-hour response**: Content team provides revised retention messaging (or explains if not sending one)
- **48–72 hours**: Retention message sent to target segment (if applicable)
- **3-day monitoring**: Track unsub rate post-send to measure effectiveness

**If content team cannot respond in 48 hours**:
- Send hold email: "If we don't hear back by [time], we'll proceed with default retention message to [segment]"
- Default: Send frequency adjustment message (most universally applicable)
- Document delay and reason in PHASE_3_EXECUTION_LOG.md

---

## SEGMENT ANALYSIS PROCEDURE

### Why Segment?

If unsub rate is RED or sustained YELLOW, isolate the problem to a **specific subscriber segment** before deciding on retention strategy. A brand-new subscriber unsubbing after 2 emails is a different problem than a 6-month subscriber unsubbing — and the solutions are different.

### Segments to Track

1. **New Subscribers (0–7 days old)**
   - Metric: Unsub count and rate for this segment only
   - **If unsub rate >2.0%**: Opt-in flow problem (they didn't understand what they were signing up for, or first email was wrong)
   - Action: Review opt-in flow and first email; adjust for next cohort
   - Retention: May not be worth it; focus on fixing the funnel

2. **Early Segment (8–30 days old)**
   - Metric: Unsub count and rate for this segment
   - **If unsub rate >0.8%**: Content expectation mismatch
   - Action: Review what they saw when signing up vs. what they received
   - Retention: Worth a content relevance message ("here's what's coming")

3. **Long-Term Subscribers (>30 days old)**
   - Metric: Unsub count and rate for this segment
   - **If unsub rate >0.4%**: List fatigue (frequency, content shift, or natural churn)
   - Action: Check recent send cadence; assess if content has drifted from launch
   - Retention: Worth a frequency adjustment or content clarity message

4. **High-Engagement Segment (opened 2+ of last 3 sends)**
   - Metric: Any unsubs from this segment?
   - **If unsubs >0 from this segment**: Major signal; tone/content mismatch likely
   - Action: Review the specific email that triggered unsub; isolate tone problem
   - Retention: High-priority; these are your best subscribers

5. **Cold Segment (no opens in 90 days)**
   - Metric: Track separately; expected high unsub rate
   - Action: Suppress from future sends (already done in list health check)
   - Retention: Not worth pursuing; focus on re-engagement only if budget available

### Segment Analysis Data Collection (Kit.com)

**Manual segmentation** (Kit.com does not have automated cohorts; use these methods):

1. **Identify segment members**:
   - Kit.com > Subscribers > filter by signup date range
   - Example: Filter "Signup date between 2026-06-29 and 2026-07-06" = "New Subscribers (Week 1)"
   - Export to CSV (name, email, signup date, last opened date)

2. **Cross-reference with unsubscribes**:
   - Kit.com > Unsubscribes > filter by date range (same day)
   - Export to CSV (email, unsubscribe date, reason)
   - Use VLOOKUP or manual match to see which unsubs came from each segment
   - Calculate: (unsubs in segment / total segment size) × 100 = segment unsub rate

3. **Identify high-engagement subscribers** (opened 2+ recent sends):
   - Kit.com > Subscribers > filter "Last Opened < 3 days ago" (or pull analytics by campaign)
   - For each recent email, note which subscribers opened
   - Create manual list of "opened 2/last 3 sends"
   - Cross-reference with unsub list to see if any from high-engagement segment

4. **Identify cold subscribers** (no opens in 90 days):
   - Kit.com > Subscribers > sort by "Last Opened" ascending
   - Filter "Last Opened > 2026-03-30" (90 days before today)
   - Count and note % of total list

### Segment Analysis Interpretation

**Example 1: New Subscribers Have High Unsub Rate**
```
Total unsubs today: 10
Unsub breakdown by segment:
  - New (0–7 days): 7 unsubs / 50 new subscribers = 14% unsub rate ← RED
  - Early (8–30 days): 2 unsubs / 200 early = 1% unsub rate (normal)
  - Long-term (>30 days): 1 unsub / 500 long-term = 0.2% unsub rate (normal)

Interpretation: NEW SUBSCRIBER PROBLEM
Root cause: Opt-in flow or first email didn't match expectation
Action: Review first email sent to new subscribers; check if subject line/preview matched signup promise
Retention: Skip retention message (fixing the funnel is more important than saving a 2-day-old subscriber)
```

**Example 2: Long-Term Subscribers Have Elevated Unsub Rate**
```
Total unsubs today: 10
Unsub breakdown by segment:
  - New (0–7 days): 1 unsub / 50 = 2% (slightly elevated)
  - Early (8–30 days): 2 unsubs / 200 = 1% (normal)
  - Long-term (>30 days): 6 unsubs / 500 = 1.2% ← Elevated
  - Cold (no opens 90d): 1 unsub / 100 = 1% (expected)

Interpretation: LONG-TERM SUBSCRIBER FATIGUE
Root cause: Frequency too high, or content has shifted from launch
Action: Check recent send cadence (how many days between last 3 sends?); review if recent emails are more promotional than initial emails
Retention: YES, run frequency adjustment message to long-term engaged segment
```

**Example 3: High-Engagement Segment Unsubscribing**
```
High-engagement subscribers (opened 2/last 3 sends): 300 subscribers
Unsubs from this segment today: 8
Interpretation: CRITICAL SIGNAL
Root cause: Most recent email tone/content was wrong; it violated expectations from prior emails
Action: Pull most recent email sent yesterday; analyze tone (is it unexpectedly promotional?); check subject line (did preview match body?)
Retention: YES, send content clarity message; apology for tone mismatch if appropriate
Follow-up: Review next email before send to prevent similar tone mismatch
```

### Isolation & Targeted Campaign Decision

**Run targeted retention campaign if**:
- Unsub is concentrated in ONE segment (>60% of unsubs from one segment, vs. uniform spread)
- That segment is valuable to keep (not new/cold)
- Root cause is addressable (e.g., "too many emails" → frequency adjustment)

**Example: Yes, run targeted campaign**
- 8 of 10 unsubs are long-term subscribers citing "too many emails"
- Send frequency adjustment message to long-term engaged segment only
- Skip sending to new subscribers (would over-explain)

**Do NOT run targeted campaign if**:
- Unsub is uniform across all segments (systemic issue)
- Issue is opt-in flow or list quality (can't fix with retention messaging)

**Example: No, don't run targeted campaign**
- Unsubs are evenly distributed (2 new, 3 early, 3 long-term, 2 cold)
- Suggests content is off-brand or list quality degraded
- Address the root cause (list cleanup, content review) before sending retention messaging

---

## WEEKLY SUMMARY TEMPLATE (Monday 8:00 AM UTC Check-In)

### What to Log Each Monday

Run this summary every Monday morning (8:00 AM UTC) to assess list health and trend direction.

**Week of**: [Dates, Monday–Sunday]

**1. Weekly Unsub Rate (7-day average)**
```
Daily rates for the week:
Mon [date]: ___ % | Tue: ___ % | Wed: ___ % | Thu: ___ % | Fri: ___ % | Sat: ___ % | Sun: ___ %

7-day average: ___ %
Status: [ ] GREEN (<0.3%) [ ] YELLOW (0.3–0.5%) [ ] RED (>0.5%)
Trend: [ ] Stable [ ] Improving (declining) [ ] Declining (worsening)

vs. Prior week: ___ % (better/worse by X%)
```

**2. Peak Unsub Day(s) This Week**
```
Peak day: [Date]
Peak rate: ___ %
Peak count: ___ unsubs

Reason breakdown on peak day:
- Too many emails: ___ %
- Not relevant: ___ %
- Prefer other format: ___ %
- Other: ___ %

Was there an email send correlation?
[ ] YES → Subject: _____ | Send time: _____ | Likely factor: _____
[ ] NO → Reason: _____
```

**3. Content Changes Made in Response**

```
YELLOW or RED escalations this week?
[ ] No alerts (all days GREEN)

[ ] YELLOW triggered: [Which days?]
    Response taken: _____
    Monitoring outcome: _____

[ ] RED triggered: [Which days?]
    Root cause: _____
    Escalation sent to content team: [ ] Yes | Date/time: _____
    Retention message drafted: [ ] Yes | Type: [Frequency / Content Relevance / Re-engagement]
    Message sent: [ ] Yes | Date: _____ | Target segment: _____
    Result (if sent): [unsub rate 3 days post-send] ___ %
```

**4. List Health Snapshot**

```
Total subscribers: ___ (end of week)
Unconfirmed %: ___ (target: <15%)
Cold % (no opens 90d): ___ (target: <25%)
High-engagement %: ___ (opened 2+ recent sends)

Any list cleaning done this week?
[ ] No
[ ] Yes → Removed: ___ unconfirmed, ___ cold, ___ other
  Post-clean total: ___
  Impact: [Removed X% of list]
```

**5. Outlook for Next Week**

```
Emails planned for next week:
- [Email name/subject]: scheduled [date] at [time]
- [Email name/subject]: scheduled [date] at [time]

Expected impact on unsub rate:
[ ] Minimal (educational content, low frequency)
[ ] Moderate (promotional send or higher frequency)
[ ] High (bundle launch, or frequent sending period)

Any content team actions pending from this week?
[ ] No
[ ] Yes → Items: _____
  Expected completion: _____

Monitoring focus for next week:
[ ] Continue standard daily monitoring (GREEN zone expected)
[ ] Watch for YELLOW (sustained 0.3–0.5%)
[ ] RED alert status (HIGH RISK — ensure escalation team is aware)

Outlook: [ ] Maintain pace [ ] Adjust cadence [ ] Escalate for review
```

**6. Metrics for Review (Dashboard)**

```
WEEK SUMMARY TABLE:

Metric | Target | Week Value | Status
Avg daily unsub rate | <0.3% | ___% | GREEN/YELLOW/RED
Peak unsub day | <0.5% | ___% | GREEN/YELLOW/RED
Total unsubs for week | N/A | ___ count | N/A
Unconfirmed % of list | <15% | ___%  | GREEN/YELLOW
Cold % of list | <25% | ___% | GREEN/YELLOW/RED
Content changes made | 0–2 | ___ | OK if reason matches action
RED escalations | 0 | ___ | GREEN if 0, RED if >1
```

**7. Checkboxes for Completion**

```
[ ] Daily monitoring log complete (all 7 days entered)
[ ] Weekly average calculated
[ ] List health check performed
[ ] Segment analysis (if YELLOW/RED triggered)
[ ] Content team escalations sent (if applicable)
[ ] Retention messages sent (if applicable)
[ ] Next week's emails reviewed for potential tone issues
[ ] Metrics logged in PHASE_3_EXECUTION_LOG.md
[ ] This summary shared with [team/orchestrator]
```

---

## QUICK REFERENCE — THRESHOLD SUMMARY

| Status | Unsub Rate | Action | Monitor Duration |
|--------|-----------|--------|------------------|
| **GREEN** | <0.3% | Log and continue | Daily |
| **YELLOW** | 0.3–0.5% | Monitor 3 consecutive days; investigate if sustained | 3 calendar days |
| **RED** | >0.5% | Investigate immediately (within 2 hours); list health check same day; escalate to content team | Until resolved |

| Unsubscribe Reason | If >20% of Daily Unsubs | Action |
|-------------------|------------------------|--------|
| "Too many emails" | Frequency problem | Draft frequency adjustment message; review send cadence |
| "Not relevant" | Content mismatch | Draft content relevance message; segment analysis to isolate (new vs. long-term) |
| "Prefer other format" | Delivery format issue | Review next welcome flow; offer format options upfront; lower priority |

| Segment | Unsub Rate Threshold | Interpretation |
|---------|---------------------|-----------------|
| New (0–7d) | >2.0% | Opt-in flow or first email problem; fix funnel |
| Early (8–30d) | >0.8% | Content expectation mismatch; send content clarity message |
| Long-term (>30d) | >0.4% | List fatigue; check frequency and content drift |
| High-engagement (2+ opens) | Any unsub | Major signal; tone/content mismatch; high-priority |
| Cold (no opens 90d) | Expected high | Suppress from future sends; don't pursue retention |

---

## INTEGRATION WITH PHASE 3 EXECUTION LOG

**How to integrate this document into PHASE_3_EXECUTION_LOG.md:**

1. **Daily entry** (recorded at 22:00 UTC each day):
   ```
   [Date] — Daily Unsub Report
   Rate: X.XX% | Count: Y | Status: GREEN/YELLOW/RED
   Reason: [too many emails / not relevant / other]
   Notes: [correlation, action taken, or standard log]
   ```

2. **YELLOW escalation** (if triggered):
   ```
   [Date] — YELLOW UNSUB ALERT (0.3–0.5%)
   Rate: X.XX% | Day 1 of 3-day monitoring window
   Root cause hypothesis: [email send / list quality / segment issue]
   Action: Monitor Days 2–3; escalate to RED if sustained
   ```

3. **RED escalation** (if triggered):
   ```
   [Date] — RED UNSUB ALERT (>0.5%)
   Rate: X.XX% | Count: Y
   Root cause: [email send correlation / list quality / segment analysis]
   List health actions: [removed unconfirmed / suppressed cold / etc.]
   Escalation email sent to: [content team] at [time]
   Retention message type: [Frequency / Content Relevance / Re-engagement]
   Message sent: [date] | Result (3d later): [unsub rate] ___% | RESOLUTION: [Open/Pending/Resolved]
   ```

---

## OPERATIONAL CHECKLIST FOR DAILY MONITORING

**Every day at 22:00 UTC:**

- [ ] Log into Kit.com > Subscribers > Unsubscribes
- [ ] Filter: Last 24 hours
- [ ] Record: Daily unsub count
- [ ] Calculate: Daily unsub rate (count / total subscribers × 100)
- [ ] Record: Unsub reason breakdown (counts and %)
- [ ] Check: Was there an email send same day or yesterday?
  - [ ] NO → Record "no send correlation"
  - [ ] YES → Note subject, send time, brief content assessment
- [ ] Apply threshold logic: GREEN / YELLOW / RED?
  - [ ] GREEN (<0.3%) → Log, close
  - [ ] YELLOW (0.3–0.5%) → Log, start/continue 3-day monitoring
  - [ ] RED (>0.5%) → Execute investigation flowchart (all 7 steps)
- [ ] If YELLOW or RED → Update daily monitoring template (this document)
- [ ] If RED → Run list health check (Kit.com, same day)
  - [ ] Unconfirmed % [>15%?] → Remove or note
  - [ ] Cold % [>25%?] → Suppress or note
- [ ] If RED → Send escalation email to content team (within 2 hours)
  - [ ] Include: rate, count, reasons, segment analysis, proposed messaging
  - [ ] SLA: 48-hour response from content team
- [ ] Log all actions in PHASE_3_EXECUTION_LOG.md (Escalation Log section)
- [ ] Monday 8:00 AM UTC → Run weekly summary (see template above)

---

## APPENDIX: KIT.COM NAVIGATION GUIDE

**Accessing unsubscribe data in Kit.com:**

1. **Daily unsub count and rate**:
   - Go to: Kit.com > Dashboard > Subscribers section
   - Or: Kit.com > Subscribers > Unsubscribes tab
   - Filter: "Date range: last 24 hours" (or custom date)
   - View: List of unsubscribes with email, date, time
   - Count: Divide number of unsubs by current subscriber total in Kit > Account > Overview

2. **Unsubscribe reasons**:
   - Go to: Kit.com > Subscribers > Unsubscribes
   - Click: Each unsubscribe entry; view "Reason" field (populated if subscriber selected)
   - Or: Export full unsubscribe list to CSV (Kit.com > Subscribers > Export > Unsubscribes)
   - Count reasons manually or use spreadsheet COUNTIF function

3. **Campaign send history** (for correlation):
   - Go to: Kit.com > Campaigns
   - View: Recent sends (shows date, time, subject, recipient count, delivery rate)
   - Click on specific campaign to view delivery stats, open rate, click rate

4. **Subscriber segmentation** (for list health):
   - Go to: Kit.com > Subscribers > Filter
   - Available filters: Status (active, unconfirmed, bounced, suppressed), Last Opened (date range), Signup date
   - Create temporary segments (e.g., "Cold_90days", "Unconfirmed_Jun2026") for analysis
   - Export as CSV for manual analysis (VLOOKUP, pivot tables)

5. **Subscriber list export** (for deeper analysis):
   - Go to: Kit.com > Subscribers > Export
   - Include: Email, status, signup date, last opened date, engagement metrics
   - Save as CSV; use spreadsheet software for pivot tables, filtering, segment analysis

**Note**: Kit.com does not provide built-in cohort analysis or automated segment reporting. All segment analysis must be done manually (export, VLOOKUP, pivot tables) or via CSV processing.

---

## SUCCESS CRITERIA & METRICS

**Daily monitoring is successful if**:
1. All daily unsub rates are logged by 23:00 UTC (within 1 hour of monitoring checkpoint)
2. YELLOW thresholds are caught within 24 hours (by next day's 22:00 check)
3. RED thresholds trigger escalation within 2 hours of detection
4. Retention messages are drafted and sent within 48–72 hours of RED resolution
5. 3-day post-send monitoring is completed for all retention efforts
6. Weekly summary is posted every Monday 8:00 AM UTC

**List health is successful if**:
1. Unsub rate stays <0.3% for 80%+ of days
2. No RED triggers are sustained >2 days without resolution
3. Unconfirmed subscribers stay <15% of list
4. Cold subscribers stay <25% of list
5. High-engagement segment (opened 2+ recent sends) is >40% of list

**Content team integration is successful if**:
1. Escalation emails are received and acknowledged within 24 hours
2. Retention messaging is revised and approved within 48 hours of escalation
3. Messages are sent within 72 hours of approval
4. Feedback from content team on root causes is documented
5. Patterns are identified and next sends are adjusted before launch

---

*Prepared: June 29, 2026. Production-ready daily monitoring template. Update daily at 22:00 UTC. All thresholds calibrated to PHASE_3_EMAIL_ENGAGEMENT_ALERT_PROCEDURES.md Procedure 4. Integration points: PHASE_3_EXECUTION_LOG.md (escalation log), SEEDWARDEN_PHASE_3_WEEK_1_MONITORING_DASHBOARD.md (email metrics), kit.com dashboard (data source). No external tools required — Kit.com UI, daily log, threshold comparison, and basic spreadsheet suffice for full execution. Weekly retrospectives required; segment analysis recommended for any YELLOW/RED escalations. Retention messaging SLA: 48–72 hours for drafting + approval + send.*
