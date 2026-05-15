---
title: "Tier 1 Day 1 Execution Checklist"
project: cybersecurity-hardening
created: 2026-05-15
status: user-ready
phase: Phase 1 — Tier 1 Launch
executor: Anya
launch-target: June 1, 2026
---

# Tier 1 Day 1 Execution Checklist

**Purpose**: One-page operational checklist for the day Tier 1 Phase 1 outreach begins. Run this on Day 0 (May 31) and again at Day 1 (June 1) morning before any sends.

**Estimated user time**: Day 0 prep = 90–120 minutes. Day 1 send session = 45–60 minutes.

**Corpus URL**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108  
**Short URL to create**: bit.ly/palantir-briefing (verify before Day 1)  
**Send target**: June 1, 2026 — 5 Senate/legislative staff contacts, 8:30–8:50 AM local time

---

## Day 0 (May 31) — Pre-Launch Setup (90–120 minutes)

### 1. Gist Accessibility Verification (15 min)
- [ ] Open the corpus URL in a private/incognito browser (not logged into GitHub)
- [ ] Confirm the page loads without a login wall
- [ ] Confirm all three documents are present and readable: `threat-model.md`, `opsec-playbook.md`, `implementation-guide.md`
- [ ] Confirm Part 0 (data broker opt-outs) is intact in implementation-guide.md
- [ ] Confirm California DELETE Act / DROP platform path is documented
- **STOP if Gist requires login**: Change GitHub Gist visibility to Public before proceeding

### 2. Short URL Setup (10 min)
- [ ] Log into bitly.com (create free account if needed — use project email, not personal)
- [ ] Shorten the Gist URL; assign back-half: `palantir-briefing`
- [ ] Test the short URL in a private browser — confirm it redirects correctly to the Gist
- [ ] Note short URL: `bit.ly/palantir-briefing`

### 3. Email Infrastructure (30 min)
- [ ] In Gmail, create parent label `Tier1-Policy` with nested labels: `Sent`, `Reply-Stage0`, `Reply-Stage1-Question`, `Reply-Stage1-MeetingRequest`, `Reply-Stage1-Routing`, `Reply-Declined`, `OOO-Active`, `Bounce-Unresolved`, `Follow-Up-Pending`, `Meeting-Scheduled`
- [ ] Enable Gmail Templates (Settings → Advanced → Enable Templates)
- [ ] Save all Week 1 templates as Gmail drafts: `Week1-Senator`, `Week1-ThinkTank`, `Week1-LawSchool`, `Week1-CivilRights`, `Week2-Followup`
- [ ] Set up Calendly (free tier): 20-minute and 30-minute slots, Mon–Thu availability; test booking link from a private browser

### 4. Tracking Spreadsheet (20 min)
- [ ] Create Google Sheet titled: "Phase 1 Policy Outreach Tracker — June 2026"
- [ ] Create 5 tabs: Contact Master List, Email Engagement Log, Meeting Schedule, Policy Uptake Signals, KPI Summary
- [ ] Pre-populate Tab 1 with all 25 contacts — at minimum the 5 Day 1 Wave 1 Senate contacts:
  - Senate Judiciary Subcommittee on Privacy, Technology & the Law — staff counsel
  - Senate Select Committee on Intelligence — commercial data brokers staff
  - Senate Homeland Security Committee — immigration technology staff
  - Senator Ron Wyden's office — privacy-focused staff
  - Senator Ed Markey's office — Digital Consumer Protection Caucus staff
- [ ] Add auto-calc formulas in Tab 1: reply rate, Stage 1+ ratio, meeting scheduled rate (see PHASE_1_EXECUTION_CALENDAR.md Section 8)
- [ ] Set calendar holds: Gate 1 (June 7, 9 AM), Gate 2 (June 15, 9 AM), Tier 2 gate (June 19, 9 AM), Day 8 follow-up (June 8, 8 AM)

### 5. Email Deliverability Test (10 min)
- [ ] Send test email from your outreach address to yourself at a personal Gmail and one non-Gmail account
- [ ] Confirm: Email lands in inbox, not spam
- [ ] Optional but recommended: go to mail-tester.com, send test, confirm score ≥ 8/10
- **STOP if score is below 6/10**: Diagnose deliverability (SPF/DKIM, spam trigger words) before any Day 1 sends

### 6. Contact Verification — Day 1 Wave 1 (15 min)
- [ ] Confirm all 5 Wave 1 (Senate) contact emails are current via official websites and LinkedIn
- [ ] Verify the named staff member is still in the same role (not transferred or departed)
- [ ] Flag any contact who is on leave as "deferred" — do not skip the organization
- [ ] For each contact, write 2–3 sentence personalization hook in Tab 1 Notes column (specific to recent committee work, bill, or hearing — not generic copy-paste)

### 7. Day 1 Drafts Final Review (15 min)
- [ ] Open all 5 Wave 1 email drafts in Gmail
- [ ] Confirm: All `[Your name]` and `[Contact Name]` placeholders replaced
- [ ] Confirm: Bitly short URL (bit.ly/palantir-briefing) is present in each draft
- [ ] Confirm: Subject line is under 50 characters and sector-specific
- [ ] Confirm: Opening 2–3 sentences are specific to that office's recent work
- [ ] Read each email as the intended recipient — does it make sense? Does it feel like targeted outreach or mass mail?

### 8. Google Alerts Setup (5 min)
- [ ] Create Google Alerts for: "ELITE address confidence score", "Palantir ICE ELITE", "DROP platform immigration"
- [ ] These catch downstream citations if the corpus begins to spread

### Day 0 Go/No-Go Gate
Do not proceed to Day 1 sends if ANY of these remain true:
- [ ] Gist URL requires login
- [ ] Bitly short URL does not redirect correctly
- [ ] Mail-tester score below 6/10
- [ ] Any Day 1 contact email has bounced in a test send
- [ ] Fewer than 23 of 25 contacts have verified, current email addresses
- [ ] Any Day 1 email draft still contains placeholder text

---

## Day 1 (June 1, Monday) — Launch Morning (45–60 minutes)

### 9. Pre-Send Final Verification (10 min)
- [ ] Re-open Gist in incognito browser — confirm it still loads publicly
- [ ] Re-check Bitly redirect — test in private browser
- [ ] Open tracking spreadsheet — confirm it is accessible and Tab 1 is pre-filled
- [ ] Open Calendly — confirm booking link is live

### 10. Send Wave 1 — Senate Staff (25 min, 8:30–8:50 AM)

Send in this order, 5 minutes apart:

| Time | Contact | Organization | Template |
|------|---------|-------------|----------|
| 8:30 AM | Staff counsel, Subcommittee on Privacy, Technology & the Law | Senate Judiciary | `Week1-Senator` (oversight jurisdiction variant) |
| 8:35 AM | Staff member, commercial data brokers | Senate Select Committee on Intelligence | `Week1-Senator` (intelligence oversight variant) |
| 8:40 AM | Staff member, immigration technology | Senate Homeland Security | `Week1-Senator` (DHS jurisdiction variant) |
| 8:45 AM | Privacy-focused staff | Senator Ron Wyden's office | `Week1-Senator` (Wyden variant) |
| 8:50 AM | Digital Consumer Protection Caucus staff | Senator Ed Markey's office | `Week1-Senator` (Markey variant) |

**Per-email pre-send check (before each send)**:
- [ ] Gist URL correct in body: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] BCC to yourself enabled
- [ ] Subject line correct and specific
- [ ] Opening hook is personalized to THIS office's specific recent work
- [ ] No placeholder text remaining

### 11. Post-Send Logging (10 min, 9:00–9:10 AM)
- [ ] Update Tab 1 and Tab 2 in tracking spreadsheet with send timestamps for all 5 contacts
- [ ] Apply `Tier1-Policy/Sent` Gmail label to BCC copies of each send
- [ ] Note Bitly baseline click count in Tab 5 (will be 0 at send time; first clicks typically arrive within 3–4 hours)
- [ ] Set Tab 1 follow-up dates: June 8 (Day 8 follow-up if no reply by June 7)

### 12. Day 1 Monitoring (5 min, 3:00–5:00 PM)
- [ ] Check Bitly dashboard — any clicks? Log in Tab 5.
- [ ] Check Gmail for any rapid replies — classify and respond within 24 hours if Stage 1+
- [ ] Check for bounces in sent mail — if any, research alternate contact immediately

---

## Days 2–5 Reminder — Week 1 Send Schedule

| Day | Contacts | Send Time |
|-----|---------|-----------|
| Day 2 (Tue, June 2) | 3 Senate/CRS (Commerce, House Judiciary, CRS) | 8:30 AM |
| Day 3 (Wed, June 3) | 5 Think Tanks Part 1 (Brennan, Georgetown CPT, EPIC, R Street, Cato) | 9:00 AM |
| Day 4 (Thu, June 4) | 5 Think Tanks Part 2 (New America, CAP, Just Security, Lawfare, CDT) | 9:00 AM |
| Day 5 (Fri, June 5) | 5 Law Schools Part 1 (Georgetown Law, Yale MFIA, Harvard, Stanford, NYU) | 10:00 AM |
| Day 6 (Sat, June 6) | No sends — reply processing and Day 8 draft prep | — |
| Day 7 (Sun, June 7) | GATE 1 CHECKPOINT — run by 10:00 AM | — |

**Gate 1 thresholds (June 7)**:
- Greater than 30% click rate (8+ clicks from 25 sends) = GO
- 20–30% click rate = CAUTION (revise subject lines before Day 8 follow-ups)
- Less than 20% click rate = STOP (Contingency A — deliverability diagnostic, 48-hour max)

---

## Quick Reference: File Locations

| File | Purpose |
|------|---------|
| `PHASE_1_EXECUTION_CALENDAR.md` | Full day-by-day calendar, templates, contingency trees |
| `TIER1_OUTREACH_PREPARED.md` | Personalized drafts for 1A national organizations (NILC, CLINIC, RAICES, ILRC, NLG) |
| `TIER1_PREFLIGHT_CHECKLIST.md` | Detailed infrastructure pre-flight (Gist, Bitly, Gmail, tracker) |
| `TIER1_OUTREACH_EXECUTION_PLAN.md` | Full response templates (R1–R5) and response handling |
| `PHASE_1_FLAGS_ASSESSMENT.md` | Three pre-launch accuracy flags (Mobile Fortify, DOGE, Cellebrite) |

---

*Created: 2026-05-15. Launch target: June 1, 2026. Coordinates with: PHASE_1_EXECUTION_CALENDAR.md, TIER1_OUTREACH_PREPARED.md, TIER1_PREFLIGHT_CHECKLIST.md.*
