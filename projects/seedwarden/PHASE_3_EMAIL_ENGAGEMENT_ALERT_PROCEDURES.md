---
title: "Phase 3 Email Engagement Alert Procedures — Decision Tree"
date: 2026-06-29
version: 1.0
status: active
sprint-window: June 29 – August 3, 2026
cross-references:
  - PHASE_3_EXECUTION_LOG.md (where metrics are recorded)
  - PHASE_3_WEEK_1_2_ALERT_THRESHOLDS.md (numeric gate definitions)
  - PHASE_3_BUNDLE_LAUNCH_EMAIL_SEQUENCES.md (source email templates)
  - PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md (feedback and course-correction templates)
---

# Phase 3 Email Engagement Alert Procedures

**How to use**: Read left-to-right. Each gate is triggered by a specific metric at a specific time. Follow the listed steps in order. Do not skip steps. Log all YELLOW and RED triggers in `PHASE_3_EXECUTION_LOG.md` Escalation Log with timestamp.

**All times UTC. Email send time = 13:00 UTC. Monitoring checkpoints are relative to send.**

---

## PROCEDURE 1 — DELIVERY RATE (Check at T+1hr = 14:00 UTC, day of send)

**Metric source**: Kit.com dashboard > Campaign > Delivery Stats.

```
IF delivery rate >95% AND hard bounces <1%:
  → Status: GREEN. No action. Continue to open rate monitoring.

IF delivery rate 90–95% OR hard bounces 1–2%:
  → Status: YELLOW.
  Step 1: Open Kit.com > Account > Sending Limits. Check for warnings or quota alerts.
  Step 2: Open Kit.com > Subscribers > Bounces. Identify: hard bounce vs. soft bounce.
    - Hard bounce = invalid address. Remove from list: Kit.com > Subscribers > filter "Bounced" > export > manually suppress.
    - Soft bounce = temporary failure. Take no action — Kit retries automatically.
  Step 3: Log in PHASE_3_EXECUTION_LOG.md: date, delivery rate, bounce count, action taken.
  Step 4: Proceed with next send on schedule. No delay required for YELLOW delivery.

IF delivery rate <90% OR hard bounces >2% OR spam complaints >0.1%:
  → Status: RED.
  Step 1: Pause any sends currently in draft or scheduled for the next 24 hours in Kit.
  Step 2: Log in to Kit.com > Account > Deliverability. Check for: suspension flag, IP reputation warning, spam complaint report.
  Step 3: If account suspended: email Kit support at support@kit.com. Subject: "Account suspension — active campaign." Include account email and campaign name. Response SLA: 1 business day.
  Step 4: If no suspension found: review the email HTML for spam trigger patterns (see Checklist A below).
  Step 5: Do not send next email until delivery rate returns to >95% on a test send.
  Step 6: Log full escalation in PHASE_3_EXECUTION_LOG.md with resolution status.
```

**Checklist A — Spam Trigger Review** (run when delivery RED):
- [ ] Subject line: no ALL CAPS words, no excessive punctuation (!!!), no "FREE" or "WINNER"
- [ ] Body: image-to-text ratio not >60% images (Kit plain-text emails avoid this)
- [ ] Links: all links resolve to the same domain (etsy.com); no redirect chains
- [ ] Unsubscribe link: present and functional in footer
- [ ] Sender address: matches domain used previously (no sudden domain change)

---

## PROCEDURE 2 — OPEN RATE (Check at T+24hr)

**Metric source**: Kit.com dashboard > Campaign > Open Rate.
**Check times**: T+24hr = 13:00 UTC next day. T+48hr = 13:00 UTC two days after send.

**Note**: Do not trigger YELLOW/RED response until the T+24hr checkpoint. Preliminary rates at T+3hr and T+8hr are for tracking only — open rates climb for up to 48 hours.

```
IF open rate >22% at T+24hr:
  → Status: GREEN. No action.
  Log in PHASE_3_EXECUTION_LOG.md: date, campaign, open rate.
  Proceed to next bundle launch on schedule.

IF open rate 15–22% at T+24hr:
  → Status: YELLOW.
  Step 1: Compare subject line against any prior campaign. If this is the first send, proceed to Step 2.
    - Prior campaign data location: PHASE_3_EXECUTION_LOG.md > Aggregate Metrics Summary.
  Step 2: Draft an A/B subject line for the next email. Two options:
    Option A: Current subject line (keep as-is, measure if performance improves next bundle).
    Option B: Curiosity-hook variant (example: "Why [herb] is harvested wrong 90% of the time").
    Decision: pick Option B if current campaign is second or later AND first campaign was also YELLOW.
    Decision: pick Option A if this is the first campaign (single data point is insufficient for A/B pivot).
  Step 3: Log YELLOW in PHASE_3_EXECUTION_LOG.md. Note which option was chosen for next send.
  Step 4: No changes to current campaign. Wait for T+48hr rate before any further decision.

IF open rate <15% at T+24hr:
  → Status: RED.
  Step 1: Run spam placement test. Send a copy of the most recent email to these five addresses:
    - Gmail (personal)
    - Outlook (personal)
    - Yahoo Mail (create test account if needed)
    - Apple Mail (test via iCloud address)
    - Proton Mail (free account)
    Check: does the email land in inbox or spam folder on each provider?
  Step 2: If spam placement confirmed on 2+ providers:
    - Review subject line for spam trigger phrases (see Checklist A above).
    - Review body copy: excessive link density (>3 links), image-heavy HTML, misleading preview text.
    - Revise next email to remove triggers before next send.
    - Consider 24-hour delay to next send if spam issue not resolved.
  Step 3: If spam placement not confirmed (all inbox):
    - Issue is likely list engagement, not deliverability.
    - Review recent subscriber acquisition source — are new subscribers low-engagement (e.g., from a giveaway, low-intent opt-in)?
    - Segment: create a segment of subscribers who have NOT opened in the last 3 sends. Exclude from next send if list is >500 subscribers.
  Step 4: Log full RED in PHASE_3_EXECUTION_LOG.md. Record: spam test results, action taken, next send adjusted (yes/no).
```

---

## PROCEDURE 3 — CLICK RATE (Check at T+24hr, same time as open rate)

**Metric source**: Kit.com dashboard > Campaign > Click Rate.

```
IF click rate >3% at T+24hr:
  → Status: GREEN. No action.
  Log in PHASE_3_EXECUTION_LOG.md.

IF click rate 1–3% at T+24hr:
  → Status: YELLOW.
  Step 1: Check: is the CTA link text clear and specific? ("Get the Women's Health Bundle" vs. "click here" or "learn more").
  Step 2: Check: does the Etsy listing page load quickly and show the correct bundle at the correct price?
    - Open listing URL from email on mobile (primary check device). Confirm: loads in <3 seconds, price visible above fold, images loaded.
  Step 3: Check: is there only ONE primary CTA in the email, or are there competing links?
    - If >2 CTA links: consider removing secondary links for the next email to concentrate click intent.
  Step 4: Log YELLOW in PHASE_3_EXECUTION_LOG.md with specific finding.
  Step 5: No changes to current campaign. Apply findings to next email template.

IF click rate <1% at T+24hr (AND open rate is GREEN or YELLOW — meaning people opened but did not click):
  → Status: RED.
  Step 1: CTA problem confirmed (opens are happening, clicks are not). Audit the email CTA:
    - CTA text: copy it verbatim. Is it action-oriented? ("Get" / "Download" / "View" > "Click" / "Here").
    - CTA placement: is the CTA above the fold (visible without scrolling)? If not, add a second CTA near top of email.
    - CTA link: confirm it resolves to the live Etsy listing, not a 404 or wrong page.
  Step 2: Check: does the bundle image show in the email? If image is broken, click intent drops sharply.
    - Re-verify: all images in email are hosted on a public URL (not local drive or private Dropbox).
  Step 3: Revise the next email template with: (1) CTA button text updated, (2) CTA moved above fold, (3) second CTA added at bottom of email.
  Step 4: Log RED in PHASE_3_EXECUTION_LOG.md with specific CTA change made.
```

---

## PROCEDURE 4 — UNSUBSCRIBE RATE (Check daily at 22:00 UTC)

**Metric source**: Kit.com dashboard > Subscribers > Unsubscribes (filter: last 24 hours).
**Calculation**: (daily unsubscribes / total subscriber count) × 100 = daily rate %.

```
IF daily unsubscribe rate <0.3%:
  → Status: GREEN. No action. Log in PHASE_3_EXECUTION_LOG.md.

IF daily unsubscribe rate 0.3–0.5%:
  → Status: YELLOW (elevated, typical for launch week sends).
  Step 1: This rate is within expected range for launch-week sends (high-frequency period).
  Step 2: Monitor for 3 consecutive days. If rate stays 0.3–0.5% for 3 days without send, escalate to RED.
  Step 3: Review unsubscribe feedback (Kit.com > Unsubscribes > Reason). If >20% say "too many emails": consider adding a frequency preference option to the next welcome sequence.
  Step 4: Log YELLOW in PHASE_3_EXECUTION_LOG.md with daily counts.

IF daily unsubscribe rate >0.5%:
  → Status: RED.
  Step 1: Pull the Kit.com unsubscribe report for the last 7 days. Identify: is the spike correlated with a specific email send?
    - If yes (spike same day or day after a send): the email triggered list fatigue or mismatched expectations. Review that email's tone, frequency, and content.
    - If no (gradual accumulation): list health issue. Proceed to Step 3.
  Step 2: If spike correlates with a send:
    - Increase gap between next two sends. If Email 2 is scheduled within 5 days of Email 1 and Email 1 caused the spike: increase gap to 10 days minimum.
    - Review email content for tone mismatch — does it feel too promotional vs. educational?
  Step 3: Run list health check in Kit.com:
    - Subscribers > filter "Unconfirmed" — remove if >15% of list (indicates cold or unqualified opt-ins).
    - Subscribers > filter "Cold" (no opens in 90 days) — suppress from sends until re-engagement sequence run.
  Step 4: Log full RED in PHASE_3_EXECUTION_LOG.md with: pre-clean subscriber count, post-clean count, reason, and date.
```

---

## PROCEDURE 5 — SECOND-BUNDLE FATIGUE CHECK (Email 3: Sleep, July 13)

Run this check when Email 3 is sent. Compare open rate to Email 1 and Email 2.

**Fatigue trigger**: Email 3 open rate <15%.

```
IF Email 3 open rate >20%:
  → No fatigue signal. Proceed with Email 4 (Immunity, planned Week 3) on standard schedule.

IF Email 3 open rate 15–20%:
  → Minor decline. Acceptable.
  Step 1: Increase educational content ratio in Email 4 (from ~60% educational / 40% promotional to ~80% / 20%).
  Step 2: Consider adding a "here's what's inside" teaser section to Email 4 subject line and preview text.
  Log in PHASE_3_EXECUTION_LOG.md.

IF Email 3 open rate <15%:
  → Fatigue signal confirmed.
  Step 1: Extend gap before Email 4 by 7 days (from Week 3 to Week 4 timing).
  Step 2: Send a re-engagement email to the "Cold" segment (subscribers who did not open Email 1, 2, or 3).
    Subject line: "We've been launching guides — did you miss them?"
    Content: brief summary of all 3 bundles with direct Etsy links. No new pitch.
  Step 3: Review Email 4 subject line. Shift from bundle-announcement framing to value-delivery framing:
    Before: "Immunity Support — Herbs for respiratory defense and immune resilience"
    After: "The elderberry question I get every fall (answered)"
  Step 4: Log in PHASE_3_EXECUTION_LOG.md with adjusted send date for Email 4.
```

---

## QUICK REFERENCE — THRESHOLD SUMMARY

| Metric | GREEN | YELLOW | RED | Check Time |
|--------|-------|--------|-----|------------|
| Delivery rate | >95% | 90–95% | <90% | T+1hr (14:00 UTC) |
| Open rate (24hr) | >22% | 15–22% | <15% | T+24hr (13:00 UTC +1 day) |
| Click rate (24hr) | >3% | 1–3% | <1% | T+24hr (13:00 UTC +1 day) |
| Daily unsubscribe rate | <0.3% | 0.3–0.5% | >0.5% | 22:00 UTC daily |
| Spam complaints | <0.05% | 0.05–0.1% | >0.1% | T+1hr (14:00 UTC) |
| Email 3 fatigue check | >20% | 15–20% | <15% | T+24hr, July 14 |

---

*Prepared: June 29, 2026. All thresholds based on Q2 2026 construction-audience baseline (22–28% open rate, 3–5% click rate). Update thresholds after Week 1 if actual baseline differs significantly from Q2 data.*
