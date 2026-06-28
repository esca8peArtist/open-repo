---
title: "Wave 2 Activation Decision Thresholds"
subtitle: "Deterministic contingency triggers — count to action, no subjective calls"
created: "2026-06-28"
session: "4467"
status: "PRODUCTION-READY"
hard_deadline: "2026-06-30 18:00 UTC"
decision_deadline: "2026-06-30 00:00 UTC (June 29 midnight = June 30 00:00 UTC)"
script_companion: "AUTOMATED_WAVE_2_CLASSIFICATION.py"
model_companion: "WAVE_2_OUTCOME_PROBABILITY_MODEL.md"
---

# Wave 2 Activation Decision Thresholds

**Domain 59 (EPI / Demos / NELP) | Domain 60**
**Session 4467 | June 28, 2026**

---

## Decision Architecture

This document provides deterministic contingency triggers. Each trigger is a count-to-action mapping with no subjective evaluation required. When you have a reply count, find the row, execute the action. The companion script (`AUTOMATED_WAVE_2_CLASSIFICATION.py`) automates this lookup.

**Decision deadline**: 2026-06-30 00:00 UTC (this is "June 29 midnight" — the end of the day June 29, expressed in UTC)

**Hard deadline**: 2026-06-30 18:00 UTC (final send window before advocacy window closes)

**Monitoring period**: Begins when Wave 2 sends are confirmed (expected June 24-27, 2026). Check inbox daily until June 30 00:00 UTC.

---

## Primary Decision Table — By Reply Count as of 2026-06-30 00:00 UTC

| Count | Classification | Trigger Condition | Mandatory Action |
|-------|---------------|-------------------|-----------------|
| 0 | ZERO | Zero replies by 2026-06-30 00:00 UTC | Activate Fallback Protocol (see Section 4) |
| 1 | LOW | Exactly 1 reply by 2026-06-30 00:00 UTC | Escalate Communication (see Section 3) |
| 2-3 | MODERATE | 2 or 3 replies by 2026-06-30 00:00 UTC | Continue Standard Timeline (see Section 2) |
| 4+ | HIGH | 4 or more replies by 2026-06-30 00:00 UTC | Accelerate Tier 3 (see Section 1) |

---

## Section 1 — HIGH: 4+ Replies by 2026-06-30 00:00 UTC

**Classification**: HIGH

**Trigger**: 4 or more substantive replies received across Wave 2 sends by 2026-06-30 00:00 UTC.

**What counts as a reply**: Any non-automated response from the recipient organization — including acknowledgment, forwarding notice, question, meeting request, or substantive engagement. Auto-reply OOO messages do NOT count. Bounces do NOT count.

**Mandatory actions (execute in order)**:

1. **Immediate (within 2h of classification)**: Log HIGH classification in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md with timestamp and total reply count.

2. **By 2026-06-30 12:00 UTC**: Send consolidated Tier 3 emails. Instead of the standard spaced send sequence (1 email per day), send all remaining Tier 3 contacts within a single 4-hour window (2026-06-30 09:00-13:00 UTC). The consolidated approach signals organizational momentum and allows each contact to see the framing while it is still live.

3. **By 2026-06-30 14:00 UTC**: Reply to each HIGH-classified contact individually with a brief acknowledgment and the Gist URL. Do not let HIGH-signal contacts go unacknowledged — they have opened a relationship thread.

4. **By 2026-06-30 18:00 UTC**: Final send window closes. All Tier 3 sends must be logged by this time.

**Expected reply count for HIGH**: 4-5 replies across Wave 2 (n=8-10 sends). Under the 60% base rate, this corresponds to approximately the 70th percentile of the reply distribution — a better-than-average outcome.

**Note on "consolidated 3-email" interpretation**: The task brief references "consolidated 3-email instead of spaced" — this refers to the Tier 3 send sequence. Where the standard Tier 3 plan calls for 3 emails spread over 3 days, HIGH classification compresses this to same-day sends.

---

## Section 2 — MODERATE: 2-3 Replies by 2026-06-30 00:00 UTC

**Classification**: MODERATE

**Trigger**: 2 or 3 substantive replies received across Wave 2 sends by 2026-06-30 00:00 UTC.

**Context**: This is the expected outcome based on Wave 1 data (Domain 59 Wave 1 delivered 2-3 MODERATE replies from 5 sends). MODERATE confirms the distribution strategy is functioning but has not achieved breakthrough organizational engagement.

**Mandatory actions**:

1. **Immediate**: Log MODERATE classification in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md.

2. **Continue standard timeline**: Do not accelerate or decelerate. The already-planned Tier 3 send schedule is the correct response to MODERATE.

3. **By 2026-06-30 18:00 UTC**: Complete any remaining Wave 2 sends that have not yet been executed (NELP if not yet sent; any Domain 60 contacts not yet sent).

4. **No new decision gates needed before June 30 18:00 UTC**: MODERATE is the baseline plan. Execute it.

**Note on Domain 60**: If Domain 60 produces MODERATE independently from Domain 59, treat the two domains as separate tracks — do not combine reply counts for classification purposes. Each domain has its own advocacy window and organizational contacts.

---

## Section 3 — LOW: 1 Reply by 2026-06-30 00:00 UTC

**Classification**: LOW

**Trigger**: Exactly 1 substantive reply received across all Wave 2 sends by 2026-06-30 00:00 UTC.

**Interpretation**: A single reply may indicate (a) the research framing is resonating selectively, (b) send timing was suboptimal (late in the week, conflicting with other organizational priorities), or (c) the contact profile requires a different approach. LOW does not mean the campaign has failed — it means the standard timeline needs adjustment before the hard deadline.

**Mandatory actions (execute in this order)**:

1. **Immediate**: Log LOW classification. Identify which organization replied and whether the reply is substantive or pro forma.

2. **By 2026-06-30 04:00 UTC**: Escalation check. Verify that all Wave 2 sends were actually delivered — check for bounces, SMTP rejections, or sends that were not completed. If any send failed, re-send immediately. A failed delivery explains a LOW classification without indicating a framing problem.

3. **By 2026-06-30 08:00 UTC (if sends were all confirmed delivered)**: Escalation option — send a short follow-up to the 2 highest-priority non-responding Wave 2 contacts. Subject line: "Brief follow-up — [original subject]." Body: 2-3 sentences maximum. Reference the June 30 advocacy window. Do not resend the full research document.

4. **By 2026-06-30 14:00 UTC**: Determine whether retry path or Gist-only path is more appropriate given response so far. If the follow-up escalation produced no additional response by 14:00 UTC, move to Gist-only distribution (see Section 4 — treat as ZERO for remaining contacts who have not responded).

5. **By 2026-06-30 18:00 UTC**: Final log entry. Record all attempts, responses, and path taken.

**What "escalate" means**: Direct subject-line clarification, shortened email body, or explicit request for the organization's preferred engagement format (e.g., "Would a 15-minute call be more useful than email for this?"). Escalation is not harassment — one follow-up within 5 business days of initial send is standard professional practice.

---

## Section 4 — ZERO: 0 Replies by 2026-06-30 00:00 UTC

**Classification**: ZERO

**Trigger**: Zero substantive replies received across all Wave 2 sends by 2026-06-30 00:00 UTC.

**Important pre-classification check**: Before classifying as ZERO, verify all of the following:
- [ ] All sends were confirmed delivered (no bounces logged in send log)
- [ ] No replies are sitting in spam or promotions folder
- [ ] The Gist URL (https://gist.github.com/esca8peArtist/70b18a6f26dc879e3399c6d147d882ba) still resolves HTTP 200

If any of the above fail, correct the failure first and do not classify as ZERO yet.

**Mandatory actions (if ZERO confirmed)**:

1. **Immediate (by 2026-06-30 02:00 UTC)**: Log ZERO classification. Record total sends, delivery confirmations, and any anomalies.

2. **Activate Gist-only distribution**: The research document remains available at the Gist URL regardless of organizational response. Treat the Gist as the primary artifact. Share it on any applicable social or professional networks (LinkedIn, Twitter/X, professional Slack channels or listservs where policy researchers congregate).

3. **Retroactive protocol activation**: Record all contacts as "Wave 2 attempted, no reply." Do not delete or modify original emails. These contacts remain on the list for future waves — ZERO in a single window does not mean the contact is disqualified.

4. **By 2026-06-30 12:00 UTC**: Complete any remaining sends that have not yet been attempted. ZERO classification applies only to contacts who have been sent to and not replied. If NELP or Domain 60 contacts have not been sent to by 2026-06-30 00:00 UTC, send them anyway — the advocacy window remains open until 18:00 UTC.

5. **Log for future reference**: A ZERO outcome with confirmed delivery is meaningful research data — it indicates either a framing problem, a contact-type mismatch, or normal variance in unsolicited policy research response rates. Document it explicitly so future waves can adjust.

**Gist-only fallback path**: Even if zero organizational replies are received, the Gist URL distributes the research publicly. Any search engine index, any social share, any secondary forwarding by any reader constitutes distribution. ZERO in email does not mean zero impact.

---

## Decision Timeline Summary (All UTC)

| Timestamp (UTC) | Decision Point | Action |
|-----------------|----------------|--------|
| 2026-06-25 09:00 | Wave 2 sends begin (if not already sent) | Send EPI, Demos per DOMAIN_59_WAVE_2_EMAIL_EXECUTION_PACKAGE.md |
| 2026-06-26 09:00 | NELP send window opens | Send NELP (info@nelp.org) |
| 2026-06-27 09:00 | Domain 60 sends begin | Send Domain 60 contacts per Domain 60 execution package |
| 2026-06-28 18:00 | First monitoring checkpoint | Check inbox; log any replies; update DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md |
| 2026-06-29 18:00 | Pre-deadline monitoring | Final inbox check before classification deadline |
| 2026-06-30 00:00 | CLASSIFICATION DEADLINE | Count replies; classify HIGH/MODERATE/LOW/ZERO; execute corresponding section |
| 2026-06-30 04:00 | LOW escalation window opens | If LOW: verify delivery, prep follow-up |
| 2026-06-30 08:00 | LOW follow-up send (if applicable) | 2-3 sentence follow-up to 2 non-responding contacts |
| 2026-06-30 09:00 | HIGH consolidated send window opens | If HIGH: begin Tier 3 consolidated sends |
| 2026-06-30 12:00 | HIGH/ZERO actions due | HIGH: Tier 3 sends underway; ZERO: Gist-only activated |
| 2026-06-30 14:00 | LOW retry assessment | If LOW with no follow-up response: move to Gist-only for remaining |
| 2026-06-30 18:00 | HARD DEADLINE | All sends logged; all paths executed; advocacy window closes |

---

## Classification Rules — Edge Cases

**Mixed signal (one domain HIGH, one MODERATE)**: Classify each domain independently. Run HIGH protocol for the HIGH domain, MODERATE protocol for the MODERATE domain simultaneously.

**Reply received AFTER 2026-06-30 00:00 UTC but BEFORE 18:00 UTC**: Do not retroactively reclassify. Continue executing the path determined at 00:00 UTC. Log the late reply for future planning.

**OOO reply with a return date before June 30**: Treat as pending, not as a reply. Set a calendar reminder to follow up when the contact returns. Do not include in the count toward classification.

**Reply from a different person at the same organization (e.g., "Dr. X asked me to follow up")**: Count as a substantive reply. Organizational engagement is the target — the specific individual is secondary.

**Bounce with no delivery confirmation**: Re-verify the email address against the organization's website. Re-send to verified address. Do not count the original bounced send in the denominator until delivery is confirmed.

---

*All timestamps in UTC. "June 29 midnight" = 2026-06-30 00:00 UTC. Hard deadline = 2026-06-30 18:00 UTC.*
*Cross-reference: WAVE_2_OUTCOME_PROBABILITY_MODEL.md (statistical basis) | AUTOMATED_WAVE_2_CLASSIFICATION.py (executable lookup)*
