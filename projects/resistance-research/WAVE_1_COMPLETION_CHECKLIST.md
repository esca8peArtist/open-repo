---
title: "Wave 1 Completion Checklist — Post-Send Verification Protocol"
created: 2026-05-18
status: ACTIVE — execute at 10:00 UTC May 18 when Wave 1 distribution closes
scope: "Full 40–45 Tier 1 organization Wave 1 verification, delivery confirmation, and signal baseline capture"
audience: "thorn — execute immediately at Wave 1 close (10:00 UTC)"
companion_files:
  - WAVE_1_RESPONSE_TRACKING_TEMPLATE.md
  - WAVE_1_CONTINGENCY_DECISION_TREE.md
  - WAVE_1_DAILY_MONITORING_TEMPLATE.md
  - PHASE_2_LAUNCH_DECISION_TRIGGERS.md
  - POST_WAVE_1_PHASE_1_MEASUREMENT_FRAMEWORK.md
---

# Wave 1 Completion Checklist

**Wave 1 window**: May 18 08:00–10:00 UTC  
**Execute this checklist**: Starting at 10:00 UTC May 18, immediately after final send  
**Time required**: 45–60 minutes  
**Output**: Completion status (FULLY_COMPLETE / PARTIAL_COMPLETE / BLOCKED) + baseline metrics snapshot

---

## PART 1: Organizational Send Verification (10:00–10:20 UTC)

Run through your send log and confirm each organization. Mark each row with one of: SENT / BOUNCE / SKIPPED / PENDING.

### 1.1 Law Schools and Academic Institutions

Record send status for each contact you attempted:

| Organization | Contact Name | Email Address Used | Status (SENT/BOUNCE/SKIPPED) | Time Sent (UTC) | Notes |
|---|---|---|---|---|---|
| NYU Law / Just Security | Ryan Goodman | ryan.goodman@nyu.edu | ___ | ___ | ___ |
| Harvard Kennedy School | Erica Chenoweth | erica_chenoweth@hks.harvard.edu | ___ | ___ | ___ |
| [Law school 3] | ___ | ___ | ___ | ___ | ___ |
| [Law school 4] | ___ | ___ | ___ | ___ | ___ |
| [Law school 5] | ___ | ___ | ___ | ___ | ___ |

**Law school subtotal**: ___ SENT / ___ BOUNCE / ___ SKIPPED

### 1.2 Immigration Legal Aid Organizations

| Organization | Contact Name | Email Address Used | Status | Time Sent (UTC) | Notes |
|---|---|---|---|---|---|
| [Immigration org 1] | ___ | ___ | ___ | ___ | ___ |
| [Immigration org 2] | ___ | ___ | ___ | ___ | ___ |
| [Immigration org 3] | ___ | ___ | ___ | ___ | ___ |

**Immigration legal aid subtotal**: ___ SENT / ___ BOUNCE / ___ SKIPPED

### 1.3 Think Tanks and Policy Organizations

| Organization | Contact Name | Email Address Used | Status | Time Sent (UTC) | Notes |
|---|---|---|---|---|---|
| Brennan Center for Justice | Wendy Weiser | wweiser@brennancenter.org | ___ | ___ | ___ |
| Protect Democracy | Ian Bassin | ian@protectdemocracy.org | ___ | ___ | ___ |
| Elias Law Group | Marc Elias | melias@elias.law | ___ | ___ | ___ |
| [Think tank 4] | ___ | ___ | ___ | ___ | ___ |
| [Think tank 5] | ___ | ___ | ___ | ___ | ___ |

**Think tank subtotal**: ___ SENT / ___ BOUNCE / ___ SKIPPED

### 1.4 Labor Unions

| Organization | Contact Name | Email Address Used | Status | Time Sent (UTC) | Notes |
|---|---|---|---|---|---|
| [Union 1] | ___ | ___ | ___ | ___ | ___ |
| [Union 2] | ___ | ___ | ___ | ___ | ___ |
| [Union 3] | ___ | ___ | ___ | ___ | ___ |

**Union subtotal**: ___ SENT / ___ BOUNCE / ___ SKIPPED

### 1.5 Other Academic and Civil Society

| Organization | Contact Name | Email Address Used | Status | Time Sent (UTC) | Notes |
|---|---|---|---|---|---|
| [Academic 1] | ___ | ___ | ___ | ___ | ___ |
| [Academic 2] | ___ | ___ | ___ | ___ | ___ |
| [Civil society 1] | ___ | ___ | ___ | ___ | ___ |

**Other subtotal**: ___ SENT / ___ BOUNCE / ___ SKIPPED

---

## PART 2: Aggregate Send Count Summary (10:20–10:25 UTC)

Complete immediately after table verification above.

| Metric | Count |
|---|---|
| Total organizations targeted | ___ (expected: 40–45) |
| Total emails sent (confirmed in sent folder) | ___ |
| Total hard bounces (550/mailbox not found) | ___ |
| Total soft bounces (452/temp failure) | ___ |
| Total skipped (contact not found / not attempted) | ___ |
| Out-of-office autoreplies received (confirms live delivery) | ___ |
| Immediate substantive replies (within 2 hrs of send) | ___ |

**Overall delivery rate**: ___ / ___ = ___%  
**Wave 1 completion status**: [ ] FULLY_COMPLETE (≥38 of 40 sent, <3 hard bounces)  
[ ] PARTIAL_COMPLETE (25–37 sent OR 3–5 bounces)  
[ ] BLOCKED (<25 sent OR >5 hard bounces OR user reported unable to continue)

---

## PART 3: Gist Baseline Snapshot (10:25–10:35 UTC)

Open each Gist in a fresh incognito window and record view count before any contact clicks links.

**Time of snapshot (UTC)**: ___

| Gist Title | URL | Baseline View Count (H+0) | Notes |
|---|---|---|---|
| Main 40-Domain Proposal | ___ | ___ | ___ |
| Executive Summary | ___ | ___ | ___ |
| Litigation Tracker | ___ | ___ | ___ |
| Domain 37 (Electoral Security) | ___ | ___ | ___ |
| Domain 42 (DEA Briefing) | ___ | ___ | ___ |
| Domain 56 (Civil Service) | ___ | ___ | ___ |
| Domain 57 (Multilateral) | ___ | ___ | ___ |
| Domain 58 (Tribal Sovereignty) | ___ | ___ | ___ |

**Why this matters**: Gist view counts are your primary real-time signal. GitHub does not expose view-count APIs for unauthenticated users, so manual incognito checks every 2–4 hours are the only measurement method. The H+0 baseline prevents false positives from your own pre-send checks.

---

## PART 4: Bounce Investigation Protocol (10:35–10:45 UTC)

For any hard bounces received, execute the following before logging final send status:

**Step 1**: Confirm the bounce is a hard bounce (550 Mailbox Not Found) vs. soft bounce (452 Temp Failure / greylisting). Soft bounces usually self-resolve within 24 hours — log as PENDING, not BOUNCE.

**Step 2**: For each hard bounce, check:
- Was the email address verified in PHASE_1_CONTACT_VERIFICATION.json prior to send?
- Is there an alternate contact address for this organization in DISTRIBUTION_OUTREACH_CONTACTS.md?
- Is this a Tier 1 priority organization (law school, major think tank, union federation) or secondary?

**Step 3**: Log each hard bounce with resolution path:

| Organization | Bounced Address | Alternate Address | Action Required | Priority |
|---|---|---|---|---|
| ___ | ___ | ___ | RESEND / SKIP / FIND-ADDRESS | HIGH / MED / LOW |

**Hard bounce threshold**: If ≥3 hard bounces for Tier 1 priority organizations, flag in Wave 1 completion status as PARTIAL_COMPLETE and notify orchestrator.

---

## PART 5: Response Signal Collection Protocol (10:45–11:00 UTC)

Where to monitor and how often:

### Primary Signal Channels

**Email inbox** — Check every 2 hours Day 0, every 4 hours Day 1–3, once daily Day 4–7.  
What to look for: Direct replies, out-of-office messages (confirms live delivery), automated acknowledgments. Log each in WAVE_1_RESPONSE_TRACKING_TEMPLATE.md immediately upon receipt.

**GitHub Gists (manual incognito check)** — Check every 2–4 hours Day 0, twice daily Day 1–3.  
Record view counts in WAVE_1_DAILY_MONITORING_TEMPLATE.md at each check. View count delta from H+0 baseline is your primary engagement proxy for contacts who clicked links but have not yet replied.

**Email Bitly/tracking links (if implemented)** — If outreach emails included Bitly-shortened links, check Bitly dashboard for click counts by link. Each click = confirmed link-follow from a recipient's device. Note: some institutional email clients auto-click links for security scanning — a single Bitly click within 30 seconds of send is likely a security scanner, not a human click.

### Secondary Signal Channels

**Social media (Twitter/X, LinkedIn, Bluesky)** — Check once daily. Search for:
- "democratic renewal" + your name or organization
- "40-domain" + proposal language
- Domain-specific terminology (e.g., "electoral security framework," "civil service depoliticization")
- Retweets or shares of any Gist URLs

**Institutional websites** — Check weekly, not daily. Signs to watch for: Organizations that list your proposal in resources pages, syllabi, or reading lists. This is a Week 2–4 signal, not a Day 0 signal.

**Google Alerts (set up now if not already)** — Configure alerts for:
- "democratic renewal proposal" (exact phrase)
- The Gist URL slug (if unique enough to search)
- Your name + "proposal" if public attribution applies

---

## PART 6: First-Response Wait-Time Baseline

What to expect by time window — calibrated to academic and policy sector reply norms.

### Hours 0–2 (10:00–12:00 UTC May 18)
**Expected**: Out-of-office autoreplies only, or silence. This is normal. Policy org contacts (Bassin, Elias) are most likely to reply within 2 hours if they are in their inbox, but a 2-hour non-reply is meaningless. Do not interpret silence as negative signal.  
**Actionable if you see**: Any hard-bounce notifications not already captured in Part 4. Any substantive reply (score this as extraordinary — less than 5% of contacts reply within 2 hours of cold outreach).

### Hours 2–6 (12:00–16:00 UTC May 18)
**Expected**: Still mostly silence or OOO autoreplies. If contacts are US-based, 10:00–14:00 UTC corresponds to 05:00–09:00 US Pacific / 06:00–10:00 US Mountain / 08:00–12:00 US Eastern. Early eastern US work hours. A reply from an east-coast contact within this window is possible but not expected.  
**Actionable if you see**: Gist view count rising above H+0 baseline — this means at least one recipient clicked a link. Log the delta; this is a positive engagement signal even without a reply.

### Hours 6–24 (16:00 UTC May 18 – 10:00 UTC May 19)
**Expected**: Most early replies will arrive in this window if they come in Day 0. Policy org contacts (3–5 day cycles) are most likely to reply first. Academic contacts (5–10 day cycles) are unlikely to reply within 24 hours.  
**Actionable if you see**: Any substantive reply — log immediately in WAVE_1_RESPONSE_TRACKING_TEMPLATE.md and score per engagement taxonomy. A Day 0 reply from any contact is a strong signal regardless of content. An OOO reply confirming a return date after May 25 means that contact should not be counted in the 72-hour window.

### Days 2–7 (May 19–25)
**Expected**: The primary reply window. Most engaged contacts will reply in this range. This is where response rate becomes meaningful. Track daily in WAVE_1_DAILY_MONITORING_TEMPLATE.md.  
**Decision gate**: May 25 week-1 checkpoint. By this date, classify Wave 1 as STRONG / MODERATE / WEAK using thresholds in WAVE_1_CONTINGENCY_DECISION_TREE.md and make Phase 2 launch decision.

---

## PART 7: Completion Log Entry

After completing Parts 1–6, copy and complete the following entry into DISTRIBUTION_EXECUTION_LOG.md:

```
WAVE 1 COMPLETION LOG — May 18, 2026
Time completed: ___ UTC
Total sent: ___
Total bounced (hard): ___
Total bounced (soft): ___
Completion status: FULLY_COMPLETE / PARTIAL_COMPLETE / BLOCKED
Gist baseline recorded: YES / NO
First reply received: YES (from: ___, at: ___ UTC) / NO
Immediate anomalies: ___
Next monitoring checkpoint: ___ UTC (H+2)
Notify orchestrator: [paste this entry or summarize status]
```

**Notify orchestrator of Wave 1 completion status once this entry is complete.**
