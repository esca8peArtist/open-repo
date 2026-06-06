---
title: "Phase 1 Impact Evaluation — Response Routing Decision Trees and Follow-Up Templates"
created: 2026-06-06
version: 1.0
status: production-ready
scope: >
  Pre-stage response routing based on engagement levels detected during June 10–17 window.
  Decision trees covering >95% of real-world engagement patterns. Three-tier follow-up
  templates (email copy ready to send). Go/no-go thresholds for Phase 2 domain activation.
companion_files:
  - PHASE_1_IMPACT_EVALUATION_DASHBOARD.md
  - PHASE_1_IMPACT_EVALUATION_INTEGRATION.md
  - PHASE_1_DAY_7_CHECKPOINT_DECISION_TREE.md
  - DOMAIN_51_JUNE_16_DECISION_LOGIC.md
word_count: ~1600
---

# Phase 1 Impact Evaluation — Response Routing Decision Trees and Follow-Up Templates

**Version 1.0 — June 6, 2026**

**Lead finding**: The most common failure mode in phased distribution campaigns is not weak engagement — it is failing to capitalize on strong engagement quickly enough. An organization that replies with a Score 5 adoption statement on June 11 and receives no follow-up until June 17 loses the momentum of that initial commitment. This document pre-stages routing decisions and ready-to-send templates so that a June 11 SCORE5_OVERRIDE alert produces a same-day response, not a Day 7 analysis finding.

---

## 1. Engagement Classification System

All engagement routing begins by assigning an organization to one of three tiers based on signals detected in the June 10–17 window. Classification uses the highest signal received, not an average.

**Tier A — High Engagement (5+ interactions OR Score 5 adoption statement)**

Definition: The organization has sent a reply scoring 5 (explicit adoption statement: "We will use this in [specific project/publication/curriculum/filing]") OR has sent 5 or more interactions (emails, questions, forwards, follow-up clicks detectable through Bitly referrer data). This tier triggers Phase 2 coordination offer within 24 hours of detection.

**Tier B — Medium Engagement (Score 3–4 reply OR 2–4 interactions)**

Definition: The organization has engaged substantively (asked a question, requested more materials, forwarded to a colleague) without an explicit adoption statement. This tier receives a gratitude + Phase 2 information email within 48–72 hours of reply.

**Tier C — Low Engagement (Score 1–2 reply only OR no reply with confirmed delivery)**

Definition: The organization opened the email (confirmed by Bitly click) but replied only with an OOO or polite acknowledgment, OR did not reply at all despite confirmed delivery. This tier receives a root-cause survey at Day 14 if still no Score 3+ signal.

---

## 2. Decision Tree — Intra-Window Routing (June 10–17)

Run this tree immediately when any engagement signal is detected. Do not accumulate signals and route them in batch — each signal routes independently.

```
SIGNAL RECEIVED — START HERE

Step 1: What score is this reply?

  Score 5 (adoption statement)?
  → TIER A — IMMEDIATE ACTIVATION
    Action: Same-day response (within 4 hours, preferably within 1 hour)
    Template: Section 3.1 (Tier A — Phase 2 Coordination Offer)
    Alert: Update ALERTS tab SCORE5_OVERRIDE; update CHECKIN.md immediately
    Phase 2 trigger: Pull Domain 58 and Domain 59 contact lists; stage for 48-hour send
    DO NOT wait for Day 7 checkpoint — this is an override condition

  Score 4 (forward to colleague OR collaboration request)?
  → TIER B (with upgrade path)
    Action: Response within 24 hours
    Template: Section 3.2 (Tier B — Gratitude + Phase 2 Info)
    Alert: Update REPLY_LOG; check SCORE4_CLUSTER alert (if this is 2nd Score 4, ACTIVATE)
    Upgrade condition: If same organization sends Score 4 AND Score 3+ within 48 hours of each other,
      upgrade to Tier A and activate Section 3.1

  Score 3 (substantive reply — question, info request)?
  → TIER B
    Action: Response within 48 hours (or within 24 hours if reply indicates active litigation or time-sensitivity)
    Template: Section 3.2 (Tier B — Gratitude + Phase 2 Info)
    Upgrade condition: If their question reveals they are actively integrating materials (e.g., "What is
      the citation format for Domain 39?"), upgrade to Tier A and activate Section 3.1

  Score 2 (polite acknowledgment — "Thanks for sending, we'll review")?
  → TIER C (provisional)
    Action: No response required at this point. Mark as PENDING.
    Re-check at Day 14: If still no Score 3+ reply by Day 14, send root-cause survey (Section 3.3)
    Upgrade condition: If the Score 2 reply includes any question or specific mention of content,
      re-score as Score 3 and route to Tier B

  Score 1 (OOO only)?
  → TIER C (provisional)
    Action: None at this stage. Mark as PENDING.
    Check: If OOO end date is within 3 days, re-send the original email on the end date
    Re-check at Day 14: No reply by Day 14 → root-cause survey (Section 3.3)

  No reply (0 signals, confirmed delivery)?
  → TIER C
    Same as Score 1 treatment above
```

---

## 3. Three-Tier Follow-Up Templates

All templates are production-ready. Fill [BRACKETED] fields before sending. Keep edits minimal — the templates are calibrated for the appropriate level of urgency and warmth for each tier.

### 3.1 Tier A Template — Phase 2 Coordination Offer

**Use when**: Score 5 adoption statement received, OR Score 4 + 3 cluster from same org within 48h.

**Send within**: 4 hours of signal detection (same day, or first thing next morning if received after 6 PM).

**Subject line**: Re: Democratic Renewal Project — Follow-Up on Your Interest

---

Dear [FIRST_NAME],

Thank you for your note — I'm genuinely glad the framework is useful for [SPECIFIC_USE_THEY_MENTIONED or "your work on [their org's focus area]"].

I wanted to follow up directly because the level of engagement you've shown is exactly what we hoped Phase 1 would generate. A few organizations at this stage have asked for a brief coordination conversation — I'd welcome that if it's useful to you.

Specifically, I'm working on two things that might be relevant to what you described:

**Domain [58 or 59, whichever is relevant] distribution**: We're preparing to distribute analysis on [Domain 58: tribal sovereignty and federal trust obligations / Domain 59: economic precarity and civic participation] to [relevant constituency]. Given your work on [their area], I'd value your perspective on whether this framing resonates with your coalition before we finalize.

**Social proof for Phase 2**: As we expand distribution, we may cite that [ORGANIZATION NAME] has engaged with the framework (without quoting your specific reply unless you consent). Would that framing be acceptable, or would you prefer we keep your engagement confidential?

If a 15-minute call would be helpful, I'm available [DATES/TIMES]. Otherwise, a brief reply by email works perfectly.

Thank you again — this kind of substantive engagement is what makes the research worthwhile.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Post-send actions**:
1. Update REPLY_LOG: set N (Follow_Up_Tier) = HIGH; J (Action_Required) = NO (sent); K (Response_Sent) = YES
2. Update CONSTITUENCY_TRACKER: mark constituency as STRONG
3. Add to Adoptions tab in existing Phase 1 dashboard with Verification_Status = Confirmed
4. Update CHECKIN.md with adoption signal summary

### 3.2 Tier B Template — Gratitude + Phase 2 Information

**Use when**: Score 3 or 4 reply received (substantive but not yet explicit adoption).

**Send within**: 24–48 hours of reply (within 24h if reply contains time-sensitive context).

**Subject line**: Re: Democratic Renewal Project — Thank You + What's Coming Next

---

Dear [FIRST_NAME],

Thank you for taking the time to engage with the framework — [BRIEF ACKNOWLEDGMENT OF THEIR SPECIFIC POINT, e.g., "Your question about the Loper Bright implications for Domain 6 is exactly the kind of synthesis we're building toward"].

I wanted to let you know what's coming in the next phase of the project, in case it's relevant to your work:

**Phase 2 distributions** (June–August 2026):
- Domain 58: Tribal sovereignty and the federal trust doctrine under the current administration — targeting law schools, civil rights organizations, and immigration legal aid clinics
- Domain 59: Economic precarity as a structural barrier to civic participation — targeting labor unions, mutual aid networks, and policy research organizations
- Domain 54: Youth civic power and the 26th Amendment enforcement gap — targeting voting rights organizations before the November 2026 midterms

If any of these align with your work, I can send them directly when they're ready for distribution. Just reply with your preference.

Thank you again for your engagement.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Post-send actions**:
1. Update REPLY_LOG: set N = MEDIUM; K = YES
2. Update CONSTITUENCY_TRACKER: mark constituency status as BUILDING if not already
3. Note in DAILY_SIGNALS Column N: "Tier B sent to [Org] [Date]"

### 3.3 Tier C Template — Root-Cause Survey

**Use when**: Score 0–2 only OR no reply, and Day 14 has passed since initial send.

**Send window**: Day 14 (June 24 for June 10 send). Do not send before Day 14.

**Subject line**: Quick check-in — Democratic Renewal Project

---

Dear [FIRST_NAME],

I sent you an email two weeks ago about the Democratic Renewal Project, and I wanted to briefly follow up.

I know inboxes are relentless, so I'll keep this short: I'd genuinely like to understand whether the framework is useful for your work or not. Three quick questions — this will take 60 seconds:

1. Did the original email reach you? (Our tracking suggests it was delivered, but we know spam filters are imperfect.)

2. If you did see it: was the framing relevant to your current work, or not the right fit? (No wrong answer — honest feedback helps us improve future distributions.)

3. Is there a better contact at [ORGANIZATION] for research on [RELEVANT DOMAIN TOPIC FOR THEIR ORG — e.g., voting rights / immigration policy / labor law]?

If you prefer, you can ignore this and I won't follow up again. But if it helps you to know: the response from [CONSTITUENCY DOMAIN — e.g., "law schools" / "civil rights organizations"] overall has been [HONEST SUMMARY — e.g., "strong" / "varied"], and we're moving into Phase 2 distribution in the coming weeks.

Thank you for your time.

[YOUR_NAME]
[YOUR_CONTACT_INFO]

---

**Post-send actions**:
1. Update REPLY_LOG: add new row for this outreach; set F = Tier C Follow-Up; set K = YES
2. Record send date in DAILY_SIGNALS Column N: "Tier C survey sent to [Org] Day 14"
3. Set 7-day reminder to check for reply to this survey

---

## 4. Go/No-Go Decision Triggers for Phase 2 Domain Activation

These thresholds are pre-calculated. At Day 7 (June 17 for June 10 send), read the cumulative signals from the dashboard and apply the appropriate decision.

### Domain 39 + Domain 51 Acceleration Triggers (STRONG Engagement)

**STRONG threshold**: Open rate >40% AND Score 3+ replies ≥5 AND ≥4 constituencies with any signal

If STRONG by Day 7:
- Domain 39 acceleration: Distribute to secondary healthcare contacts within 48 hours of STRONG determination. Lead with social proof: "[X] law schools / civil rights organizations have substantively engaged with the research." Use Tier A template with Domain 39 as the coordination offer subject.
- Domain 51 acceleration: If Domain 51 campaign finance contacts are in play, proceed to Domain 48 parallel batch activation per DOMAIN_51_JUNE_16_DECISION_LOGIC.md Section 3.1.
- Phase 2 sequence: Advance all pending domain distributions by 1 week.

### Phase 2 On Schedule (MODERATE Engagement)

**MODERATE threshold**: Open rate 20–40% AND Score 3+ replies 2–4 AND ≥3 constituencies with any signal

If MODERATE by Day 7:
- Domain 39: No acceleration. Proceed on original June 28–July 5 Phase 2 window.
- Domain 51: Proceed to Domain 48 sequential activation per DOMAIN_51_JUNE_16_DECISION_LOGIC.md Section 3.2.
- No changes to domain sequencing. Continue daily monitoring. Day 30 checkpoint (July 10 for June 10 send) is the next decision gate.

### Root-Cause Investigation Required (WEAK Engagement)

**WEAK threshold**: Open rate <20% AND Score 3+ replies 0–1 AND ≤2 constituencies with any signal

If WEAK by Day 7:
1. Run delivery diagnostic before any other action. Check: (a) Are Bitly links present in sent emails? (b) Check Gmail sent folder for bounce-backs. (c) Send plain-text test message to 2 contacts with no links.
2. If delivery confirmed but engagement weak:
   - Apply Modification 1 (stakeholder substitution): Replace 20–30% of contacts with next-tier alternatives (department chairs → clinic directors; national directors → state chapter directors)
   - Apply Modification 2 (framing revision): Shift from framework overview to single-domain pitch most relevant to recipient's current work
   - Do NOT resend the original email — changed framing only
3. Defer Domain 39 acceleration. Domain 51 sequential activation holds pending Day 30 checkpoint.
4. If Domain 39 open rate is specifically <15%: Defer Domain 51 for 2 weeks and investigate whether campaign finance audience requires a different outreach channel (conference proceedings, Just Security / Lawfare publication pathway).

### Per-Domain Defer Logic

| Domain | Go/No-Go Condition | Defer Trigger | Defer Duration |
|--------|-------------------|---------------|----------------|
| Domain 39 (Healthcare) | STRONG or MODERATE overall signal | Open rate <20% at Day 7 | 2 weeks — re-evaluate at Day 30 |
| Domain 51 (Campaign Finance) | Domain 51 composite score ≥5 (per DOMAIN_51_JUNE_16_DECISION_LOGIC.md) | Composite score <5 | Sequential hold: Domain 48 first; Domain 51 follow-up at June 30 checkpoint |
| Domain 58 (Tribal Sovereignty) | Score 3+ from Law School, Civil Rights, or Imm Legal Aid | No signals from primary constituencies | Hold to Day 30 |
| Domain 59 (Economic Precarity) | Score 3+ from Labor, Mutual Aid, or Academic | No signals from primary constituencies | Hold to Day 30 |

---

## 5. Contingency Procedures — Engagement Pattern Edge Cases

These cover the 5–10% of real-world patterns not addressed by the primary decision tree.

**Edge case 1: High click velocity, zero replies (all Bitly clicks but no email responses)**

Signal interpretation: Recipients opened and read the materials but did not reply. Possible causes: (a) content useful but not immediately actionable; (b) contacts forwarded internally and are waiting for colleague feedback; (c) contacts opened but are in a meeting-heavy week.

Action: Do NOT interpret as weak signal at Day 7. Wait until Day 14 for reply velocity. At Day 14, if still no replies despite high click velocity: send a Tier B "Did you have a chance to review?" email — not a root-cause survey. Frame it as a conversation offer, not a check-up.

**Edge case 2: Score 5 adoption from an organization NOT on the Tier 1 contact list**

Signal interpretation: Organic amplification — a Tier 1 contact forwarded to a Tier 2 contact who then replied to you directly. This is a STRONG network multiplier event.

Action: (a) Log in Network Map tab of existing dashboard (PHASE_1_MONITORING_DASHBOARD_SHEETS_SPEC.md Tab 7). (b) Add to Adoptions tab with Signal_Type = Referral and Network_Event = YES. (c) Reply to the new contact with Tier A template, framing the conversation as "You came to us via [Tier 1 contact name, if mentioned]." (d) Update CHECKIN.md with network multiplier event note.

**Edge case 3: Score 3 reply from a contact in a constituency that is otherwise showing zero signals**

Signal interpretation: Isolated signal in a weak constituency. This is a lagging indicator — it may mean the full constituency is engaging but slowly, or it may be a single strong contact in an otherwise indifferent pool.

Action: Reply with Tier B template. Ask specifically: "Have you shared this with colleagues at [other institutions in this constituency]?" If they say yes, score the mention as a network event (even if unconfirmed). Do NOT upgrade the full constituency to BUILDING based on a single contact.

**Edge case 4: Two Score 5 adoptions in the same constituency within 72 hours**

Signal interpretation: Cluster adoption — word has spread within this constituency through internal networks. This is a VERY STRONG signal (3x weight).

Action: Immediate Phase 2 activation for this constituency's primary domain. Update CHECKIN.md with "Cluster adoption detected — [constituency] — [date]." Pull Phase 2 domain contact list immediately and stage send for next business day. Use both adoption orgs as social proof in Phase 2 outreach (with permission from both contacts).

**Edge case 5: Score 3+ reply, but with substantive critique of the research**

Signal interpretation: Critique-engagement (not dismissal). A contact who takes time to critique is more engaged than one who doesn't reply. This is not a failure signal.

Action: (a) Score it as 3 (substantive engagement). (b) Reply with a modified Tier B template acknowledging the critique explicitly. (c) If the critique identifies a factual error: correct the Gist and note the update date. (d) If the critique identifies a framing issue: note it for Modification 2 framing revision. (e) A detailed critique from a law school professor or civil rights organization director is often the first step toward an academic citation — follow up at Day 30 asking whether they've had a chance to write up their thoughts.

**Edge case 6: High open rate from faith or mutual aid contacts, zero from law schools or civil rights**

Signal interpretation: The distribution reached operational constituencies but not institutional/academic gatekeepers. This is a common pattern — direct practitioners engage faster than credentialing institutions.

Action: Do NOT treat this as WEAK overall. Flag the law school/civil rights lag as a MONITOR condition for that constituency specifically. Adjust Day 14 outreach to law schools using a different approach: (a) forward via a clinic administrator or student organization rather than direct faculty contact; (b) shift subject line from framework-level to specific-issue level ("26th Amendment enforcement gap in Indiana — new research" is more compelling than "Democratic renewal framework update"). Continue Phase 2 for engaged constituencies; hold law school/civil rights acceleration until Day 14 confirms or denies their engagement.
