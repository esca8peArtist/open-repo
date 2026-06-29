---
title: "Item 33: Phase 2 Contingency Decision Tree (Mechanical Triggers)"
created: "2026-06-29"
status: "production-ready"
purpose: "Deterministic branch routing based on verifiable send timestamps; no subjective judgment"
trigger_source: "DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md send date/time columns"
decision_points: "June 30 EOD, July 1 EOD, July 7 EOD, July 8 (Congress return), July 5 response assessment (Branch B)"
---

# Phase 2 Contingency Decision Tree — Mechanical Triggers

**Use this tree to route to correct branch. All decisions are based on grep timestamps in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md — no subjective assessment.**

---

## How to Use This Tree

1. **Check current date and time** (UTC)
2. **Look up today in the timeline below**
3. **Run the corresponding verification command** (copy-paste into terminal)
4. **Match result to decision logic**
5. **Execute the indicated branch** (see ITEM_33_PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md Section 2, 3, or 4)

**Critical rule**: Do not jump ahead. If today is June 29, do NOT check "What if we're on July 5?" — check only the June 29 decision point.

---

## Decision Timeline

### TODAY: June 29, 2026

**Decision Point**: Has Wave 1 been sent yet?

**Command to run**:
```bash
grep "^### Send 1:\|^### Send 2:" /home/awank/dev/SuperClaude_Framework/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | grep -E "Send Date/Time.*June 29" | wc -l
```

**Result interpretation**:
- **Result = 0**: Wave 1 NOT sent yet. DECISION: Send today (Branch A path). Proceed to DOMAIN_51_URGENT_JUNE29_EXECUTION_SUMMARY.md immediately.
- **Result ≥1**: Wave 1 sent. DECISION: Proceed to Wave 2 sends. Continue on June 29 or June 30.

**Action**: Execute Wave 1 NOW if not sent (Copy-paste templates from DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md). Log send times immediately.

---

### TODAY: June 30, 2026

**Decision Point**: Have both Wave 1 AND Wave 2 been sent?

**Command to run**:
```bash
grep "^### Send [1-5]:" /home/awank/dev/SuperClaude_Framework/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | grep -E "Send Date/Time.*(June 29|June 30)" | wc -l
```

**Result interpretation**:
- **Result = 5**: ALL 5 sends completed (Wave 1 + Wave 2). DECISION: **BRANCH A** (Success path).
  - Action: Deploy measurement infrastructure immediately. Proceed to Section 2 of ITEM_33_PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md
  - Measurement window: 30 days (June 29 - July 28)
  - Value recovery: 100%
  
- **Result = 2**: Only Wave 1 sent. DECISION: Proceed to Wave 2 sends today or tomorrow.
  - Action: Execute Wave 2 (3 remaining emails) today if time permits, or first thing June 30
  - Log all send times
  
- **Result = 0**: No sends by June 30. DECISION: Move to July 1 decision point.
  - Action: Do NOT delay further. Execute Wave 1 on July 1 morning. Proceed to Branch B procedures (ITEM_33_PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md Section 3).

**Action**: If 2 sends logged, complete Wave 2 today or June 30 morning. If 0 sends, execute Wave 1 immediately on July 1.

---

### TODAY: July 1, 2026

**Decision Point**: What is the current send status?

**Command to run**:
```bash
grep "Send Date/Time" /home/awank/dev/SuperClaude_Framework/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | grep -E "June 29|June 30|July 1" | wc -l
```

**Result interpretation**:
- **Result ≥5**: All 5 Wave 1-2 sends completed. DECISION: **BRANCH A** (Success path).
  - Action: Deploy measurement infrastructure. Proceed to Section 2.
  - Value recovery: 100%
  
- **Result = 2-4**: Partial sends completed (some Wave 1-2 sent). DECISION: **BRANCH A (Partial)**.
  - Action: Complete any remaining Wave 1 sends immediately (July 1 morning). Execute any unsent Wave 2 sends (90 min spacing). Deploy measurement infrastructure by July 2.
  - Value recovery: 95-100% (on-time or within 24 hours of deadline)
  
- **Result = 1**: Only 1 send logged. DECISION: Execute Wave 1 Send 2 immediately (July 1 morning). Assess on July 2.
  - Action: Send second Wave 1 email (Issue One) today
  
- **Result = 0**: NO sends by July 1. DECISION: **BRANCH B** (1-7 day delay).
  - Action: Execute Wave 1 immediately (July 1 09:00 ET). Proceed to Branch B procedures (Section 3).
  - Value recovery: 60-75% (message reaches campaign-active period post-integration cutoff)

**Action**: If no sends logged, execute Wave 1 immediately on July 1. If partial sends, complete within 24 hours. Move to Branch B if Wave 1 not sent by July 1 20:00 UTC.

---

### TODAY: July 2-3, 2026

**Decision Point**: Are sends still pending? If yes, which branch applies?

**Command to run**:
```bash
grep "Send Date/Time" /home/awank/dev/SuperClaude_Framework/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | grep -E "July 1" | wc -l
```

**Result interpretation**:
- **Result ≥2**: Wave 1 sent on July 1. DECISION: **BRANCH B** (1-7 day delay).
  - Action: Execute Tier 2 Send 1 on July 2 (True North Research, Lisa Graves). Proceed to Section 3, Day 2-4 procedures.
  - Spacing: If this is July 2, send today. If this is July 3, execute Tier 2 Send 1 today, then Tier 2 Send 2 on July 4.
  
- **Result = 0**: No sends logged by July 1. DECISION: **BRANCH B** (Will activate July 1-7 delay path).
  - Action: Send Wave 1 immediately (if not already sent on July 1 EOD). Execute Tier 2 on July 2 (if Wave 1 sent July 1).
  - Timeline: Day 2 of Branch B = July 2 Tier 2 Send 1

**Action**: Send Tier 2 Contact 1 on July 2 (copy-paste from ITEM_33_PHASE_2_CONTINGENCY_CONTACT_MATRIX.md). Do not delay further.

---

### TODAY: July 4-5, 2026

**Decision Point**: Have Tier 2 sends executed? What is response status?

**Command to run**:
```bash
grep "Tier 2 Send" /home/awank/dev/SuperClaude_Framework/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | grep -E "July 2|July 4" | wc -l
```

**Result interpretation**:
- **Result = 0**: No Tier 2 sends logged. DECISION: Execute immediately.
  - Action: Send Tier 2 Contact 1 today (July 4). Then Tier 2 Contact 2 on July 6.
  
- **Result ≥1**: Tier 2 sends have started. DECISION: Continue to response assessment.
  - Action: Proceed to July 5 response assessment decision (see July 5 section below).

**Action**: If Tier 2 not sent, send Contact 1 today. By July 5 EOD, prepare response count for decision trigger.

---

### TODAY: July 5, 2026 — CRITICAL DECISION POINT (Branch B Response Assessment)

**Decision Point**: Based on Wave 1-2 responses received, should Tier 3 be accelerated (July 5-6) or wait (July 8)?

**Command to run**:
```bash
echo "Count substantive replies (Score 3+) from Wave 1-2 contacts."
echo "Search Gmail: from:(@campaignlegalcenter.org OR @issueone.org OR @commoncause.org OR @lwvc.org OR @CAclean.org)"
echo "Exclude: auto-acknowledges, form responses, OOO"
echo "Count: Score 3+ replies only (substantive content, requests for more info, forward to colleague, adoption signal)"
```

**Manual assessment** (not automated — requires inbox review):
- **Response count HIGH (4+ Score 3+ replies by July 5 19:00 UTC)**: Strong engagement signal
- **Response count MEDIUM (2-3 Score 3+ replies by July 5 19:00 UTC)**: Moderate signal
- **Response count LOW (0-1 Score 3+ replies by July 5 19:00 UTC)**: Weak signal

**Decision by July 5 20:00 UTC**:

| Response Count | Decision | Action |
|---|---|---|
| **HIGH (4+)** | Continue normal Phase 2 timeline | Do NOT accelerate Tier 3. Proceed to Day 30 checkpoint July 11. |
| **MEDIUM (2-3)** | **CHOOSE**: Accelerate OR Wait | **Option A**: Send Tier 3 Contact 1 on July 5-6 (momentum signal). **Option B**: Send Tier 3 on July 8-10 when Congress returns (coordination signal). Recommendation: If 2+ replies within 5 days of Wave 1 send, momentum likely — wait for response window to settle. If 1 reply, accelerate to July 5-6. **MAKE DECISION BY 20:00 UTC AND LOG IN EXECUTION LOG.** |
| **LOW (0-1)** | Prepare for Branch C activation (July 8+) | Do NOT accelerate Tier 3. Stage for possible July 8+ rapid-response if sends continue to slip. No sends July 6-7. Monitor for Congressional re-entry impact July 8. |

**Action**: By July 5 20:00 UTC, determine response count and log ACCELERATION DECISION in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md. If accelerating, send Tier 3 Contact 1 on July 5 or 6. If waiting, proceed to July 8.

---

### TODAY: July 6-7, 2026

**Decision Point**: What was the July 5 response assessment decision? Execute accordingly.

**Command to run**:
```bash
grep "Tier 3\|ACCELERATION\|Branch B Response Assessment" /home/awank/dev/SuperClaude_Framework/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | tail -1
```

**Result interpretation**:
- **Result contains "Accelerate"**: Execute Tier 3 Contact 1 today (July 5 or 6) and Tier 3 Contact 2 tomorrow (July 6 or 7).
  - Action: Copy-paste Tier 3 Contact 1 email from contact matrix, send today.
  - Log: Send time in execution log.
  
- **Result contains "Wait" or "Normal timeline"**: Do NOT send additional emails July 6-7.
  - Action: Close response window July 7 23:59 UTC. Move to Phase 2 measurement phase.
  - Timeline: T+7 checkpoint shifts to July 8-14 (7 days from Wave 1 send).

**Action**: Execute the decision logged on July 5. If accelerating, send Tier 3 Contact 1 today. If waiting, proceed to measurement phase.

---

### TODAY: July 8, 2026 — Congress Returns

**Decision Point**: Has Wave 1 been sent? If not, Branch C is now active.

**Command to run**:
```bash
grep "Send Date/Time" /home/awank/dev/SuperClaude_Framework/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | grep -E "June 29|June 30|July [1-7]" | wc -l
```

**Result interpretation**:
- **Result ≥1**: Wave 1 sent within June 29 - July 7. DECISION: **BRANCH B still active** (continue monitoring, not Branch C).
  - Action: Continue measurement phase initiated earlier. T+7 checkpoint = 7 days from Wave 1 send date.
  
- **Result = 0**: No sends by July 7. DECISION: **BRANCH C activated** (>7 day delay, rapid-response timeline).
  - Action: Send Wave 1 immediately (July 8 09:00 ET). Include Congressional return context in email. Proceed to Section 4, Day 1 procedures.
  - Timeline: Tier 2 send on July 9. Tier 3 sends on July 11-14 (conditional).
  - Measurement window: July 15-31 ONLY (2 weeks, no extension).

**Action**: If Wave 1 not sent by July 7, execute immediately on July 8. Proceed to Branch C (Section 4).

---

### TODAY: July 9, 2026

**Decision Point**: Branch C Day 2 — Tier 2 rapid-response send

**Command to run**:
```bash
grep "Tier 2 Send 1\|July 9" /home/awank/dev/SuperClaude_Framework/projects/resistance-research/DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md | wc -l
```

**Result interpretation**:
- **Result = 0**: Tier 2 Send 1 not yet sent. DECISION: Execute today.
  - Action: Send Tier 2 Contact 1 (True North Research, Lisa Graves) at 09:00 ET (14:00 UTC). Proceed to Section 4, Day 2 procedures.
  - Log: Send time in execution log.

**Action**: Send Tier 2 Contact 1 (copy-paste from contact matrix). Log time.

---

### TODAY: July 11-14, 2026

**Decision Point**: Branch C Day 3-6 — Tier 3 rapid-response sends (conditional)

**Command to run**:
```bash
echo "Check: Did Tier 2 send (July 9) generate any Bitly clicks or email reply by July 13 20:00 UTC?"
echo "Login: bitly.com → d51-research link → check clicks last 5 days"
echo "Gmail: Search from:true* north* research* or similar for reply"
```

**Result interpretation**:
- **Bitly clicks ≥1 OR email reply received**: Signal present.
  - Decision: Execute Tier 3 sends on schedule (July 11 Contact 1, July 14 Contact 2).
  - Action: Send Tier 3 Contact 1 on July 11. Send Tier 3 Contact 2 on July 14 (copy-paste from contact matrix).
  - Log: Both send times.
  
- **Bitly clicks = 0 AND no reply by July 13 20:00 UTC**: No signal.
  - Decision: Execute Tier 3 Contact 1 on July 11 (required), SKIP Tier 3 Contact 2 on July 14 (conserve outreach).
  - Action: Send Tier 3 Contact 1 on July 11. Log as "Tier 3 Contact 2 SKIPPED (no Tier 2 signal)" on July 14.

**Action**: Send Tier 3 Contact 1 on July 11. Check signal before July 14 Tier 3 Contact 2 send.

---

### TODAY: July 15, 2026

**Decision Point**: Abbreviated measurement window begins (2-week only)

**Command to run**:
```bash
echo "Initialize measurement: July 15-31 ONLY (no extension past July 31)"
echo "Create dashboard sheet with columns: Date, Event_Type, Contact_Org, Click_Count, Reply_Score"
echo "Begin daily monitoring: Bitly clicks, Gmail replies from all Wave 1-2-Tier 2-3 contacts"
```

**Action**: Deploy DOMAIN_51_RESPONSE_MONITORING_PROTOCOL.md for July 15-31 abbreviated window. Initialize dashboard. Begin daily logging.

---

### TODAY: July 31, 2026

**Decision Point**: Measurement window CLOSES (no extension)

**Command to run**:
```bash
echo "FINAL: Close measurement window. No extension past July 31 regardless of response count."
echo "Summarize: Total replies, Bitly clicks, forward detection, value recovery %"
echo "Log: Final outcome in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md"
```

**Action**: 
- 23:59 UTC: Stop all measurement tracking
- Close Bitly link monitoring
- Summarize final outcomes: Reply count, click count, forwarding events
- Calculate value recovery: 35-50% baseline + multipliers for responses received
- Log final outcome in execution log: Branch C complete

**Important**: DO NOT extend measurement past July 31. Window closes regardless of pending replies.

---

## Escalation Triggers (All Dates)

### If Any Wave 1-2 Send Bounces (Hard Bounce Within 2 Hours)

**Trigger**: Mail Delivery Failure notification in inbox

**Immediate action** (same day):
1. Identify bounced email address
2. Refer to ITEM_33_PHASE_2_CONTINGENCY_CONTACT_MATRIX.md for backup contact
3. Resend to backup email or phone
4. Log bounce + resend in execution log immediately
5. Continue with normal timeline (do not pause for resend)

**Time to recover**: ~5 minutes

---

### If Gist URL Returns 404 or 403 (Any Date)

**Trigger**: Test Gist URL in browser or check if recipients report broken link

**Immediate action** (within 1 hour):
1. Retrieve Domain 51 document from local backup
2. Re-upload to GitHub as new public Gist
3. Update Bitly link to point to new Gist URL
4. For unsent emails: Replace Gist URL in templates
5. For sent emails: Send follow-up with corrected URL (subject: "Gist URL Correction — Domain 51")
6. Log Gist recovery in execution log

**Time to recover**: ~10 minutes

---

### If No Response by Branch Endpoint

**Branch A endpoint (July 28)**: 0 substantive replies after 30 days
- Outcome: Delivery confirmed, engagement low
- Action: Document outcome, do not retry, proceed to Phase 2 analysis phase
- Log: "Branch A complete, 0 replies, delivery confirmed"

**Branch B endpoint (July 7 or +30 from Wave 1)**: 0-1 substantive replies
- Outcome: Partial contingency success (Tier 2 extended reach)
- Action: Continue monitoring if Tier 3 sends occurred; close measurement at +30 days or July 31
- Log: "Branch B complete, [N] replies, [X]% value recovery"

**Branch C endpoint (July 31)**: 0 substantive replies by window close
- Outcome: Contingency unsuccessful due to delay + short window
- Action: Document as "delayed-distribution, low-engagement," do not extend, close measurement
- Log: "Branch C complete, 0 replies, 35-40% value recovery estimate"

---

## Summary Decision Matrix (Quick Reference)

| Date | Trigger Command | Branch | Action |
|---|---|---|---|
| **June 29** | `grep June 29 ...` | A or Execute | Send Wave 1 if not sent. (Branch A path) |
| **June 30** | `grep June 29-30 ...` | A or B | Complete Wave 1-2 by EOD (Branch A) or move to Branch B July 1 |
| **July 1** | `grep June 29 - July 1 ...` | A or B | Complete sends if on-time (A), else Branch B |
| **July 2-3** | `grep July 1 ...` | B | Execute Tier 2 Send 1 (July 2) |
| **July 4** | Tier 2 status check | B | Execute Tier 2 Send 2 (July 4) |
| **July 5** | Gmail reply count + Bitly | B | Response assessment; decide Tier 3 acceleration YES/NO |
| **July 6-7** | July 5 decision log | B | Execute Tier 3 acceleration if decided (or close response window) |
| **July 8** | `grep June 29 - July 7 ...` | B or C | If no sends by July 7, Branch C activated; send Wave 1 today |
| **July 9** | Tier 2 status | C | Execute Tier 2 Send 1 (True North Research) |
| **July 11-14** | Tier 2 signal check | C | Execute Tier 3 sends (conditional on Tier 2 signal) |
| **July 15** | Initialize measurement | C | Begin 2-week abbreviated window (July 15-31 only) |
| **July 31** | CLOSE measurement | C | Stop tracking; document outcome; no extension |

---

**All decisions are deterministic. No subjective judgment required. Match current date to timeline, run verification command, follow indicated branch. All branches are pre-proceduralized in ITEM_33_PHASE_2_POST_DEADLINE_CONTINGENCY_ACTIVATION.md Sections 2-4.**
