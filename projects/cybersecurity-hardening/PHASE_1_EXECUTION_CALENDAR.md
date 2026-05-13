---
title: "Phase 1 Execution Calendar — Week 1–3 Day-by-Day Operational Guide"
project: cybersecurity-hardening
created: 2026-05-13
revised: 2026-05-13
version: 2.0
status: production-ready
item: 29 — Phase 1 Execution Calendar & Contact Sequencing
launch-date: June 1, 2026
gate-checkpoint: June 15, 2026
decision-owner: Anya
depends-on:
  - TIER1_EXECUTION_RUNBOOK.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - TIER1_PHASE1_READINESS_SUMMARY.md
  - TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md
  - TIER_2_EXPANSION_ARCHITECTURE.md
  - TIER_2_PILOT_LAUNCH_READINESS.md
---

# Phase 1 Execution Calendar
## Week 1–3 Operational Guide: June 1–21, 2026

**Lead finding**: Everything in Phase 1 is subordinated to one conversion event — a scheduled 30-minute briefing call. Clicks confirm delivery; replies confirm interest; meetings are the metric. Every day in this calendar drives contacts toward that call. Do not improvise the sequence.

**Launch date**: June 1, 2026 (subject to user approval)
**Pre-launch window**: May 25–31 (contact verification, infrastructure setup)
**Gate 1 checkpoint**: June 7 (Wave 1 click-through review — go/no-go for Wave 2)
**Gate 2 checkpoint**: June 15 (Week 2 overall metrics — go/no-go for Tier 2 Group B)
**Tier 2 readiness gate**: June 19–21 (Week 3 summary, KPI capture)
**Executor**: Anya
**Decision owner**: Anya at every gate

**Reference corpus (canonical URL)**: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
**Short URL (create before Day 1)**: bit.ly/palantir-briefing (verify redirect before each wave)

---

## Section 1: Quick Reference — 3-Week Overview Table

> Use this table as your daily dashboard. Check it each morning before opening email.

| Week | Days | Phase | Daily Send Target | Contacts | Expected Reply Window | Critical Decision Point |
|------|------|-------|------------------|----------|-----------------------|------------------------|
| **Week 1** | June 1–7 | Introductory Wave | 3–5/day | Senate staff (8), think tanks (5) | 72h Senate, 48h think tanks | Gate 1 (June 7): <3 replies by Day 4 triggers Contingency A |
| **Week 2** | June 8–14 | Mid-Wave Follow-Up + Law School Intro | 3–5/day | Law schools (7), follow-ups, second-tier think tanks | 48–72h | Gate 2 (June 15): <8 substantive replies by Day 11 triggers Contingency B |
| **Week 3** | June 15–21 | Adoption Signals + Tier 2 Readiness | 0 new sends | Meetings, phone calls, KPI capture | N/A | Tier 2 gate (June 19): assess Phase 1 KPIs against thresholds; decide Aug 1 or proceed |

### Week-Level KPI Targets

| Week | Reply Rate Target | Substantive Engagement Target | Adoption Signal Target | Send Volume |
|------|------------------|-----------------------------|----------------------|-------------|
| Week 1 (Days 1–7) | 40%+ of Wave 1 (5+ of 13 sends) | 30%+ Stage 1+ replies | 0–1 early signals | 13 sends (Days 1–5) |
| Week 2 (Days 8–14) | 65%+ cumulative (16+ of 25 sends replied) | 40%+ Stage 1+ replies | 3+ adoption signals | 12 sends (Days 8–10) + follow-ups |
| Week 3 (Days 15–21) | 75%+ cumulative (19+ of 25) | 5+ organizations showing policy uptake | 2+ commitment signals | 0 new sends |

**Expected response windows by sector:**
- Senate offices: 72 hours (staff review legislative mail on Monday–Thursday; Friday afternoon sends go dark)
- Think tanks: 48 hours (fellows check personal email; contact the fellow directly, not the press office)
- Law school clinics: 48–96 hours (supervising attorneys have case deadlines; clinic schedule affects availability)
- Civil rights organizations (ACLU, Lawyers' Committee): 48 hours (policy teams move fast; communications teams move slow — avoid the communications office)

---

## Section 2: Pre-Launch Window — Days -7 to 0 (May 25–31)

> This window is non-negotiable. Do not send any Week 1 email until every pre-launch item is complete.

### Days -7 to -4 (May 25–28): Contact Verification

**Goal**: Confirm all 25 contact emails are current and organizational affiliations are accurate.

**Daily contact verification routine (30–45 min/day, 5 contacts/day):**

1. Open the organization's official website staff page. Find the named contact. Verify their title has not changed.
2. Cross-check via LinkedIn (confirm current employer and title).
3. If a named individual has left the organization: identify their replacement in the same function (legislative counsel, not press; senior fellow, not communications). Note the update in Tab 1 of the tracking spreadsheet.
4. Verify email deliverability: if the organization uses a known format (firstname.lastname@domain.org), confirm the format via a published press release or staff directory. Do not guess.
5. Flag any contact who has publicly stated they are on sabbatical, parental leave, or extended travel — this is a "deferred" contact (see Contingency C), not a skip.

**Prioritize verification order**: Wave 1 contacts first (Senate staff, Days 1–2 sends), then think tanks (Days 3–4), then law schools (Days 5+).

**Public statement scan (15 min/day):**
For each contact verified, do a 5-minute Google search for recent public statements related to cybersecurity, surveillance, or national security. Purpose: personalization hooks. Note any of the following in Tab 1:
- Recent published report, testimony, or op-ed
- Committee hearing they participated in
- Bill or amendment they introduced or co-sponsored
- Recent interview or public speech

### Days -3 to 0 (May 29–31): Infrastructure + Warm Introduction Outreach

**May 29–30 (2 hours total): Infrastructure setup**

**Corpus accessibility (15 min):**
- [ ] Open https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108 in a private/incognito browser window not logged into GitHub. Confirm it loads without a login wall.
- [ ] Confirm all three core documents are present: threat-model.md, opsec-playbook.md, implementation-guide.md.
- [ ] Create Bitly short URL: log into bitly.com, shorten the Gist URL, assign the back-half `palantir-briefing`. Test in a private window. Note in tracking spreadsheet.

**Email infrastructure (30 min):**
- [ ] In Gmail, create nested labels under parent `Tier1-Policy`: `Sent`, `Reply-Stage0-Acknowledgment`, `Reply-Stage1-Question`, `Reply-Stage1-MeetingRequest`, `Reply-Stage1-Routing`, `Reply-Declined`, `OOO-Active`, `Bounce-Unresolved`, `Follow-Up-Pending`, `Meeting-Scheduled`, `Meeting-Completed`.
- [ ] Enable Gmail Templates (Settings → Advanced → Enable Templates). Save all response templates from this document as named Gmail drafts: `Week1-Senator`, `Week1-ThinkTank`, `Week1-LawSchool`, `Week1-CivilRights`, `Week2-Followup`, `Meeting-Request`, `Phone-Script-Notes`.
- [ ] Set up Calendly (free tier) with 20-minute and 30-minute slots, Monday–Thursday availability. Test the booking link from a private browser. You will paste this into follow-up emails.

**Tracking spreadsheet (30 min):**
- [ ] Create Google Sheet titled "Phase 1 Policy Outreach Tracker — June 2026". Structure per Section 8 of this document.
- [ ] Pre-populate Tab 1 with all 25 contacts (name, organization, email, sector, send wave, verification status).

**Google Alerts (5 min):**
- [ ] Set Google Alerts for: "ELITE address confidence score", "Palantir ICE ELITE", "DROP platform immigration". These catch downstream citations of the corpus.

**Calendar holds (10 min):**
- [ ] Place calendar holds for: Gate 1 check (June 7, 9 AM), Gate 2 check (June 15, 9 AM), Week 3 summary session (June 19, 9 AM), Day 8 follow-up reminder (June 8, 8 AM).
- [ ] Set send-day reminders 30 minutes before each scheduled send window (7:30 AM reminders for Days 1–5 and Days 8–10).

**May 31 (45–60 min): Final verification sweep**

**Contact re-verification for Day 1 sends:**
- [ ] For the 5 Wave 1 (Senate) contacts: re-verify email, confirm draft is complete, verify opening 2–3 sentences are specific to that office's current work.
- [ ] Read each Wave 1 draft as the intended recipient. Is the Bitly URL present? Is your name substituted? Is the subject line below 50 characters?
- [ ] Send a test email from your outreach address to yourself at a personal Gmail and a non-Gmail account. Confirm it does not land in spam. Check mail-tester.com — aim for 8/10 or above.

**Decision gate — do not launch if any of these are true:**
- [ ] Gist URL requires login
- [ ] Bitly short URL does not redirect correctly
- [ ] Mail-tester score below 6/10
- [ ] Any Day 1 contact email has bounced in a previous test send
- [ ] Fewer than 23 of 25 contacts have a verified, current email address

**Warm introduction outreach (optional — if available, increases Week 1 reply rate by ~15%):**

If you have a mutual contact with any of the 25 institutional contacts, send a 1-sentence note via that mutual contact on May 29–30:

> "I'm sharing an important cybersecurity resource with a small group of institutional leaders next week — [Contact Name] at [Organization] is one of them. Wanted to give you a heads-up in case they mention it."

This is not mandatory. Only do this if (a) the mutual contact relationship is genuine and strong, and (b) the mutual contact would not find it unusual. Do not manufacture a mutual contact that does not exist.

---

## Section 3: Week 1 — Day-by-Day Calendar (June 1–7)

> Maximum 5 new sends per day. Allow 3–5 minutes between each send to avoid Gmail rate-limit flags. All sends: 7:00–9:00 AM local time.

---

### Day 0 (Sunday, May 31): Pre-Launch Final Prep

**2 hours total**

- 9:00–9:45 AM: Complete contact re-verification sweep (see Section 2 above). Log any address changes in Tab 1.
- 9:45–10:15 AM: Compose and finalize all 5 Wave 1 email drafts (Senate/legislative cohort). Save as Gmail drafts — do not send yet.
- 10:15–10:30 AM: Send deliverability test to personal accounts. Check mail-tester.com.
- 10:30–10:45 AM: Confirm Calendly link is working. Confirm Bitly dashboard is accessible.
- 10:45–11:00 AM: Final checklist review. All items in Section 2 Pre-Launch Checklist must be checked.

**Go/no-go**: If all pre-launch checklist items are checked, you are cleared to launch June 1.

---

### Day 1 (Monday, June 1): Wave 1 — Senate/Legislative Staff (5 sends)

**Time estimate: 45–60 min total**

**Send window: 8:30–10:00 AM** (Senate staff read email in morning; avoid before 8 AM and after noon)

| # | Contact | Organization | Send Time | Template | Personalization Hook | Expected Reply |
|---|---------|-------------|-----------|----------|---------------------|----------------|
| 1 | Staff counsel, Subcommittee on Privacy, Technology & the Law | Senate Judiciary Committee | 8:30 AM | `Week1-Senator` (oversight jurisdiction variant) | Committee's June 12 Section 702 FISA deadline; reference the subcommittee's 2024 data broker report | 72h (by June 4) |
| 2 | Staff member handling commercial data brokers | Senate Select Committee on Intelligence | 8:35 AM | `Week1-Senator` (intelligence oversight variant) | SSCI's 2024 report on commercial data broker industry; lead with FOIA documentation gap | 72h (by June 4) |
| 3 | Staff member, immigration technology | Senate Homeland Security Committee | 8:40 AM | `Week1-Senator` (DHS jurisdiction variant) | DHS Palantir contracts (ELITE is a DHS-ICE contract); committee's recent DHS oversight hearings | 72h (by June 4) |
| 4 | Privacy-focused staff | Senator Ron Wyden's office | 8:45 AM | `Week1-Senator` (Wyden variant) | Wyden's published privacy letters to data brokers; corpus's FOIA documentation extends that work | 72h (by June 4) |
| 5 | Digital Consumer Protection Caucus staff | Senator Ed Markey's office | 8:50 AM | `Week1-Senator` (Markey variant) | Markey's data broker regulation bills; corpus's data broker opt-out documentation is directly relevant | 72h (by June 4) |

**Post-send (8:55–9:30 AM):**
- Update Tab 1 and Tab 2 in tracking spreadsheet with send timestamps.
- Apply `Tier1-Policy/Sent` label to BCC copies.
- Note Bitly baseline (0 clicks immediately post-send; first clicks typically arrive within 3–4 hours for engaged contacts).
- Set Tab 1 follow-up date for each: June 8 (Day 8 follow-up if no reply by June 7).

**End-of-day checkpoint:** 5 sends complete, tracking updated, Day 8 reminder set.

**Fallback — if contact has changed positions or left:**
If pre-launch verification reveals a named contact has departed, do not skip the organization. Identify the replacement in the same function (the new legislative counsel handling digital policy, not the chief of staff). If no named replacement is findable, send to the committee's public staff inquiry email with "Attention: Staff counsel handling digital surveillance/privacy policy" in the subject line. Log this as a degraded send in Tab 1.

---

### Day 2 (Tuesday, June 2): Wave 1 Continued — Senate/House Staff + CRS (3 sends)

**Send window: 8:30–10:00 AM**

| # | Contact | Organization | Send Time | Template | Personalization Hook | Expected Reply |
|---|---------|-------------|-----------|----------|---------------------|----------------|
| 6 | Counsel, AI and surveillance technology | Senate Commerce Committee | 8:30 AM | `Week1-Senator` (Commerce variant) | Commerce Committee's AI oversight work; lead with commercial data pipeline as the AI surveillance mechanism | 72h (by June 5) |
| 7 | Staff on surveillance and intelligence | House Judiciary Committee | 8:35 AM | `Week1-Senator` (House oversight variant) | House Judiciary's civil rights and immigration enforcement jurisdiction; ELITE system as Judiciary matter | 72h (by June 5) |
| 8 | Digital privacy analyst | Congressional Research Service | 8:40 AM | `Week1-Senator` (CRS variant — research frame, not oversight frame) | CRS analysts produce reports cited in legislation; lead with primary-source documentation for policy analysis; offer the corpus as a citable resource | 72h (by June 5) |

**Also at 8:00–8:30 AM:** Check Bitly dashboard from Day 1 sends. Any clicks? Log in Tab 5. If zero clicks after 24 hours, verify the Bitly redirect (test in private browser). Zero clicks at 24 hours is not alarming — Senate offices often have delayed email review — but verify the link is working.

**Post-send: same protocol as Day 1.**

**Day 2 secondary check:** If Day 1 shows any Stage 1+ replies (questions, forwarding signals), respond within 24 hours using the appropriate response template. Do not let warm contacts wait.

---

### Day 3 (Wednesday, June 3): Wave 2 — Think Tanks Part 1 (5 sends)

**Send window: 9:00–11:00 AM** (think tank fellows read email mid-morning; avoid Monday morning when inboxes are fullest)

| # | Contact | Organization | Send Time | Template | Personalization Hook | Expected Reply |
|---|---------|-------------|-----------|----------|---------------------|----------------|
| 9 | Michael Price, Senior Counsel, Liberty & National Security | Brennan Center for Justice | 9:00 AM | `Week1-ThinkTank` (Brennan variant) | Brennan Center's *America's Surveillance State* (2023); corpus extends with ELITE-specific FOIA documentation from 2025–2026 | 48h (by June 5) |
| 10 | Laura Moy (verify current), Executive Director | Georgetown Center on Privacy & Technology | 9:05 AM | `Week1-ThinkTank` (Georgetown CPT variant) | Georgetown CPT's *American Dragnet* (2022); corpus is a methodological extension with 2025–2026 ELITE system data | 48h (by June 5) |
| 11 | Surveillance policy team (verify named staff) | EPIC | 9:10 AM | `Week1-ThinkTank` (EPIC variant) | EPIC's amicus brief practice; corpus designed for brief-compatible citation structure (all claims tied to FOIA disclosures and court filings with direct URLs) | 48h (by June 5) |
| 12 | Technology and civil liberties program | R Street Institute | 9:15 AM | `Week1-ThinkTank` (R Street variant — bipartisan frame) | R Street's center-right positioning; framing is institutional oversight and constitutional limits, not partisan | 48h (by June 5) |
| 13 | Center for Constitutional Studies | Cato Institute | 9:20 AM | `Week1-ThinkTank` (Cato variant) | Cato's published work on NSA Section 702 and commercial surveillance; corpus's Section 702 documentation maps directly | 48h (by June 5) |

**Post-send:** same protocol. Note Bitly cumulative clicks from Days 1–3.

---

### Day 4 (Thursday, June 4): Wave 2 Continued — Think Tanks Part 2 (5 sends)

**Send window: 9:00–11:00 AM**

| # | Contact | Organization | Send Time | Template | Personalization Hook | Expected Reply |
|---|---------|-------------|-----------|----------|---------------------|----------------|
| 14 | Named staff (verify via website) | New America — Open Technology Institute | 9:00 AM | `Week1-ThinkTank` (OTI variant) | OTI's encryption and domestic surveillance policy work; lead with how corpus fills gap between OTI's encryption research and live ELITE documentation | 48h (by June 6) |
| 15 | Technology policy team | Center for American Progress | 9:05 AM | `Week1-ThinkTank` (CAP variant) | CAP's immigration enforcement accountability work; frame as tech-contracts-to-enforcement-patterns connection | 48h (by June 6) |
| 16 | Senior editors or contributing scholars | Just Security | 9:10 AM | `Week1-ThinkTank` (Just Security variant) | Just Security's national security and surveillance law focus; lead with FOIA/contract sourcing designed to their citation standards | 48h (by June 6) |
| 17 | Senior editor or affiliated scholar | Lawfare Institute | 9:15 AM | `Week1-ThinkTank` (Lawfare variant) | Lawfare's published ICE data practices and FISA reporting; corpus extends with ELITE-specific technical detail | 48h (by June 6) |
| 18 | AI and surveillance program | CDT (Center for Democracy and Technology) | 9:20 AM | `Week1-ThinkTank` (CDT variant) | CDT's legislative relationships; lead with how corpus documentation supports their congressional engagement work | 48h (by June 6) |

**Day 4 cumulative check:** 20 of 25 sends complete by end of Day 4. Check Bitly for cumulative clicks. If below 20% (fewer than 4 clicks from 20 sends), run subject line review before Day 5. If 3+ bounces have occurred: stop Wave 3 sends and validate remaining contact emails before proceeding.

---

### Day 5 (Friday, June 5): Wave 3 Launch — Law School Clinics Part 1 (5 sends)

**Send window: 10:00 AM–12:00 PM** (law school contacts — clinic directors and supervising attorneys — have better Friday morning availability than Senate staff; avoid Friday afternoon, lowest read rate of the week)

| # | Contact | Organization | Send Time | Template | Personalization Hook | Expected Reply |
|---|---------|-------------|-----------|----------|---------------------|----------------|
| 19 | Current director (verify via website) | Georgetown Law — Institute for Technology Law and Policy | 10:00 AM | `Week1-LawSchool` (Georgetown Law variant) | Georgetown CPT's *American Dragnet* as shared intellectual foundation; corpus adds operational countermeasures directly applicable to clinic litigation | 48–96h (by June 9) |
| 20 | Supervising attorney (verify via website) | Yale Law — Media Freedom and Information Access Clinic | 10:05 AM | `Week1-LawSchool` (MFIA variant) | MFIA's First Amendment and surveillance litigation; corpus's FOIA documentation is brief-compatible with direct URLs | 48–96h (by June 9) |
| 21 | Current clinic director (verify via HLS website) | Harvard Law — Cyberlaw Clinic | 10:10 AM | `Week1-LawSchool` (Harvard variant) | Cyberlaw Clinic's digital rights and surveillance work; lead with primary-source citability | 48–96h (by June 9) |
| 22 | Supervising attorney (verify via Stanford website) | Stanford Law — Immigrants' Rights Clinic | 10:15 AM | `Week1-LawSchool` (Stanford variant) | ELITE documentation directly relevant to active immigration clinic dockets; California-specific DROP platform documentation adds client-usable value | 48–96h (by June 9) |
| 23 | Supervising attorney (verify via NYU website) | NYU Law — Immigrant Rights Clinic | 10:20 AM | `Week1-LawSchool` (NYU variant) | NYU's active immigration litigation docket; corpus designed to be citable from primary documents in removal proceedings | 48–96h (by June 9) |

**Send timing note for Friday:** Space sends at 10-minute intervals rather than 5-minute intervals. Friday mid-morning is higher read-rate than afternoon. Do not send after 12:30 PM on Fridays — emails landing in inboxes Friday afternoon are consistently deprioritized until Monday.

**End of Week 1 preview:** 25 sends complete after Day 5 (all waves dispatched). Days 6–7 are monitoring, reply processing, and Gate 1 decision.

---

### Day 6 (Saturday, June 6): Reply Processing + Wave 4 Prep

**Time estimate: 30–45 min — no new sends**

- Check Gmail for replies received Days 1–5. Classify each using Stage 0 / Stage 1 system (see Section 8 for definitions). Apply Gmail label. Reply to any Stage 1+ responses within 24 hours using template from Section 7.
- Check Bitly dashboard. Log cumulative click count in Tab 5. Any spike (more than 3 clicks in a single hour) may indicate internal forwarding — note the time and organization.
- Pre-compose Day 8 follow-up drafts for Wave 1 contacts (Senate staff) who have not yet replied. Use Week 2 follow-up template from Section 7.
- Review Gate 1 criteria so you know exactly what to check Sunday morning.

---

### Day 7 (Sunday, June 7): GATE 1 CHECKPOINT

**Time estimate: 45–60 min — no sends**

**Gate 1 decision (run by 10:00 AM):**

Open Tab 5 of the tracking spreadsheet. Calculate: Total Bitly clicks from Days 1–5 ÷ 25 sends × 100 = click rate.

| Result | Decision | Action |
|--------|----------|--------|
| >30% click rate (8+ clicks) | GO | Proceed with Day 8 follow-ups as scheduled. No adjustments needed. |
| 20–30% click rate (5–7 clicks) | CAUTION | Proceed, but revise subject line before Day 8 follow-ups. Test one alternate subject line variant. |
| <20% click rate (fewer than 5 clicks) | STOP | Do not send follow-ups until deliverability diagnostic complete. Run mail-tester.com from the outreach address. Check for spam folder landing. 48-hour maximum resolution window. Activate Contingency A. |

**Gate 1 secondary check:**
- How many Stage 1+ replies received? Target: at least 1 by Day 7. Zero Stage 1+ replies from 25 sends by Day 7 is a weak signal — verify sends reached named individuals, not press@ or info@ inboxes.
- Any bounces? Log in Tab 1. Research alternate contacts for bounced organizations before Day 8.

**If STOP triggered:** Run Contingency A protocol from Section 9. Resolution window is 48 hours. Do not send follow-ups until resolved.

**Prepare Day 8 sends (if Gate 1 is GO or CAUTION):**
- Review all 25 contacts. Identify which have not replied and have no Bitly click. These are priority follow-up targets.
- Draft warm follow-up emails using the Week 2 follow-up template (Section 7). Different subject line from the initial send.

---

## Section 4: Week 2 — Day-by-Day Calendar (June 8–14)

> Week 2 runs two parallel tracks: (1) follow-up to Week 1 silent contacts, (2) introduction wave to law schools not yet reached. Maximum 5 sends/day across both tracks combined.

---

### Day 8 (Monday, June 8): Wave 1 Follow-Up + Remaining Law School Intros

**Time estimate: 60–75 min**

**7:00–8:00 AM — Law school completion sends (2 sends):**

| # | Contact | Organization | Send Time | Template | Personalization Hook |
|---|---------|-------------|-----------|----------|---------------------|
| 24 | Immigration unit lead (verify via UC Chicago website) | University of Chicago Law — Mandel Legal Aid Clinic | 7:00 AM | `Week1-LawSchool` | UC Chicago's client population directly affected by ELITE targeting; lead with geographic relevance (Chicago is a significant ELITE deployment zone) |
| 25 | Supervising attorney (verify via CUNY website) | CUNY School of Law — Main Street Legal Services | 7:10 AM | `Week1-LawSchool` | CUNY Law's practice-oriented mission; corpus designed to be actionable in real client matters without technical expertise |

**8:00–9:00 AM — Wave 1 follow-ups (Senate staff from Days 1–2, 8 days elapsed):**

Send Template R2 (soft follow-up) to any Day 1–2 Senate contact who has not replied and has not Bitly-clicked. Use a different subject line from the initial send. Maximum 3–4 follow-up sends this morning.

---

### Day 9 (Tuesday, June 9): Think Tank Follow-Ups + Wave 2 Law School Follow-Up Prep

**Time estimate: 45–60 min**

**7:00–7:30 AM:** Check Bitly and Gmail. Log new clicks and replies. Update Tab 5.

**7:30–8:30 AM — Think tank follow-ups (Days 3–4 sends, 6 days elapsed):**

Send Template R2 to think tank contacts (Waves 2a and 2b) who have not replied. Subject line variant: "Re: [original subject] — one concrete application for your work." Open with one sentence naming a specific aspect of the corpus directly applicable to their most recent published work. This demonstrates you read their material. Maximum 4 follow-up sends.

**Day 9 decision:** If any Stage 1+ replies have come in from Weeks 1 sends, send the Calendly link within 24 hours. Do not let warm leads go cold.

---

### Day 10 (Wednesday, June 10): Mid-Point KPI Check + Law School Follow-Ups

**Time estimate: 45–60 min**

**7:00–7:30 AM — Mid-point KPI check (four questions before proceeding):**

1. Bitly click rate: Total clicks ÷ 25 × 100. Above 30%? Above 40%? Below 30% at Day 10 triggers subject line diagnostic.
2. Reply rate: Total substantive replies (excluding OOO) ÷ 25 × 100. Target by Day 10: at least 10% (2–3 replies). Zero replies by Day 10 means email routing is the issue — verify all sends went to named individuals, not general inboxes.
3. Meetings scheduled: How many briefing calls are on the calendar? Target by Day 15: at least 3 confirmed meetings.
4. Reply quality: Of replies received, what percentage are Stage 1+ (substantive question, meeting request, forwarding signal)? Target: 60%+ of replies are Stage 1+.

**7:30–9:00 AM — Law school clinic follow-ups (Days 5 sends, 5 days elapsed):**

Send Template R2 to law school contacts from Wave 3 who have not replied within 5 days. Subject line: "Re: [original subject] — usable in active immigration dockets." Lead with one sentence naming the type of case the clinic handles and a specific corpus section relevant to it.

---

### Days 11–12 (Thursday–Friday, June 11–12): Civil Rights Org Intros + Senate Escalation

**Note: Days 11–12 are send days for civil rights organizations if they are in the 25-contact cohort, and escalated Senate follow-ups otherwise. The Section 702 FISA reauthorization deadline is June 12 — use this as a time-peg for Senate follow-ups.**

**Day 11 (Thursday, June 11) — Law school follow-ups + civil rights sends:**

If ACLU and Lawyers' Committee for Civil Rights Under Law are in the 25-contact cohort, send initial introductions now (they were reserved from Week 1 to avoid inbox clumping and to allow Week 1 reply processing to complete).

| # | Contact | Organization | Send Time | Template | Personalization Hook |
|---|---------|-------------|-----------|----------|---------------------|
| — | Policy counsel, surveillance and privacy team | ACLU — National (if in cohort) | 9:00 AM | `Week1-CivilRights` | ACLU's ongoing Section 702 litigation and commercial surveillance advocacy; equity angle on ELITE's differential impact |
| — | Staff attorney (verify current) | Lawyers' Committee for Civil Rights Under Law (if in cohort) | 9:05 AM | `Week1-CivilRights` | Lawyers' Committee's civil rights litigation angle; corpus's documentation of differential targeting of Black and brown communities in ELITE enforcement zones |

**Reply rate milestone target (end Day 11):** 8+ substantive replies from the first 25 sends. If below 8: activate the Day 12 escalated Senate follow-up regardless of click rate.

**Day 12 (Friday, June 12) — Section 702 deadline anchor + Senate escalation:**

Use the June 12 Section 702 FISA reauthorization deadline as a natural re-engagement peg for Senate contacts who have not replied.

```
Subject: FISA reauthorization today — the ELITE documentation may be relevant

One follow-up on the briefing I sent June 1st.

With the Section 702 reauthorization deadline today, I wanted to resurface the commercial data broker pipeline documentation in the corpus — specifically how Venntel and Babel Street data is acquired under Section 702 interfaces and sold to ICE without a warrant requirement.

The FOIA documentation in Part 2 of the threat model is structured to be citable in oversight letters or hearing prep.

Happy to do 20 minutes at any point this week — [Calendly link] — or send a briefing memo if that format is more useful.

[Your name]
```

---

### Days 13–14 (Saturday–Sunday, June 13–14): Reply Processing + Gate 2 Prep

**Day 13 (Saturday) — 30 min:**
No new sends. Check Gmail and Bitly. Process replies. Book any meetings requested. Log all activity in tracking spreadsheet.

**Day 14 (Sunday) — 45 min:**
Finalize all KPI data for Gate 2 check Monday morning.

**Gate 2 prep — calculate these numbers:**

| Metric | Target | Your Actual | Above/Below |
|--------|--------|-------------|-------------|
| Bitly cumulative click rate | >40% (10+ clicks) | ____% | |
| Meetings scheduled by Day 14 | ≥3 confirmed | ____ | |
| Reply rate (any substantive reply) | >20% (5+ of 25) | ____% | |
| Stage 1+ reply ratio | >60% of replies | ____% | |

---

## Section 5: Week 3 — Day-by-Day Calendar (June 15–21)

> Week 3 is not a send week. It is a meeting completion week and an adoption signal collection week. No new outreach — focus entirely on converting scheduled meetings and capturing KPI data.

---

### Day 15 (Monday, June 15): GATE 2 CHECKPOINT + Week 3 Launch

**Time estimate: 60–75 min**

**9:00–9:45 AM — Gate 2 decision:**

| Result | Decision | Tier 2 Impact |
|--------|----------|---------------|
| >40% clicks + ≥3 meetings | GO | Authorize Tier 2 Group B timeline. Begin Group B prep this week (July 15–28 window). |
| 30–40% clicks + 1–2 meetings | CAUTION | Proceed Phase 1 follow-ups. Group B approval contingent on Week 4 adoption signals. |
| <30% clicks + 0 meetings | STOP | Pause Tier 2 prep. Phase 1 diagnostic only. Redirect all capacity to Phase 1 recovery. Activate Contingency B. |

**9:45–10:30 AM — If Gate 2 is GO or CAUTION:**
Review all scheduled meetings. Confirm calls scheduled for this week. For Stage 1+ contacts who have not yet scheduled: send a specific time offer with Calendly link. Do not leave it open-ended.

---

### Days 16–17 (Tuesday–Wednesday, June 16–17): Policy Uptake Signal Monitoring

**Time estimate: 30–45 min/day**

**Daily structure:**
- Morning (20 min): Check Bitly, Gmail, and Google Alerts. Process any replies. Update tracking spreadsheet.
- Meetings: Hold briefing calls as scheduled. Write post-meeting notes in Tab 3 within 24 hours.
- End-of-day: Log meeting completion status (Completed / Rescheduled / Cancelled).

**Key priority — identify 3–5 organizations showing adoption interest:**

After each completed call, assess whether the contact shows any of these adoption signals and log in Tab 4:
- Mentioned forwarding the corpus to a colleague, committee, or team
- Referenced a specific corpus section in the context of current work (testimony prep, litigation, policy brief)
- Asked for sector-specific variant or additional documentation
- Expressed intent to implement a practice from the guide
- Offered to introduce you to another contact in their network

**Phone calls to top 3 adoption signals:**

If you have 3+ contacts who have shown adoption signals but have not yet scheduled a briefing call, shift to phone outreach. One call attempt per contact to the organization's main line. Ask for the named staff member. Use the phone script from Section 7. Do not leave a voicemail unless you have a specific message that adds value over the email.

---

### Days 18–19 (Thursday–Friday, June 19–20): Tier 2 Readiness Decision Point

**Day 18 (Thursday, June 19) — Tier 2 assessment (60 min):**

Assess Phase 1 Week 1–3 performance against KPI thresholds:

| KPI | Threshold for Tier 2 Proceed | Threshold for Tier 2 Defer | Your Actual |
|-----|------------------------------|---------------------------|-------------|
| Click rate (cumulative) | ≥40% | <30% | ____% |
| Reply rate | ≥20% | <15% | ____% |
| Meetings completed | ≥3 | 0 | ____ |
| Stage 1+ ratio | ≥60% | <40% | ____% |
| Adoption signals (Tab 4) | ≥3 | 0–1 | ____ |

**Decision tree:**
- If 4–5 metrics meet "proceed" threshold: Tier 2 Group B launches on July 15 as scheduled. Begin Group B contact verification and material customization this week.
- If 2–3 metrics meet "proceed" threshold: Extend Phase 1 follow-up to July 1. Re-assess Tier 2 readiness July 5. Group B slides to August 1.
- If 0–1 metrics meet "proceed" threshold: Full Phase 1 diagnostic (see Contingency B). Group B deferred minimum to August 1 pending diagnostic findings.

**Day 19 (Friday, June 20):**
Complete any remaining briefing calls scheduled for Week 3. Log all outcomes in Tab 3. Begin assembling Week 3 summary report data (see Days 20–21).

---

### Days 20–21 (Saturday–Monday, June 20–21): Week 3 Summary Report

**Time estimate: 2 hours total across both days**

Capture all data for the Week 3 summary. This report becomes the authoritative record for the Phase 1 execution and the input document for any Tier 2 decision.

**Summary report structure (write into WORKLOG.md and CHECKIN.md):**

1. **Contact coverage**: Total sends, bounce rate, unique organizations reached
2. **Engagement metrics**: Click rate, reply rate, Stage 1+ ratio (with breakdown by sector)
3. **Meeting metrics**: Meetings scheduled, meetings completed, meeting completion rate
4. **Adoption signals**: All signals from Tab 4, categorized by type and organization
5. **Decision outcomes**: Gate 1 result (GO/CAUTION/STOP), Gate 2 result, Tier 2 readiness gate result
6. **Notable responses**: Any responses that merit follow-up action in Months 2–3
7. **Contingencies activated**: Which contingency protocols were triggered and what action was taken
8. **Recommendation**: Proceed to Tier 2 Group B on [date] / Extend Phase 1 follow-up to [date] / Full diagnostic before proceeding

---

## Section 6: Message Customization Matrix by Contact Type

> Use this matrix to customize the templates in Section 7. Do not send identical copy to different contact types. Each sector has different institutional incentives and different language that signals you understand their world.

---

### Senate Committee Staff (8 contacts — SSCI, HPSCI, Judiciary, Homeland, Commerce, House Judiciary, Wyden, Markey)

**Frame**: Institutional authority, oversight jurisdiction, legislative tool.

**Opening hook — what resonates:**
- Reference a specific committee hearing, published report, or recent bill from that office
- Connect the corpus directly to their oversight jurisdiction (not a generic "important resource")
- Name the concrete legislative tool the corpus enables: oversight letters, hearing prep, constituent briefings, bill language

**June 12 Section 702 FISA deadline anchor (Days 1–12):**
```
As the [Committee name] prepares for the Section 702 reauthorization deadline, we're sharing a resource on the commercial data broker pipeline that underlies NSA's FISA acquisition — specifically how location data sold by Venntel and Babel Street enters the Section 702 data supply chain without a separate warrant requirement.
```

**Avoid**: Technical implementation language. These contacts do not implement; they legislate. Stay at the policy and oversight layer.

**Domain emphasis**: Domains 1, 25 (FISA/Section 702 angle), 33 (surveillance state architecture), 6 (constitutional limits)

**5 subject line variants (Senate):**
1. `FISA reauthorization — primary-sourced ELITE briefing`
2. `Palantir ELITE briefing for [Committee] oversight staff`
3. `Commercial data broker pipeline — primary-source documentation`
4. `OpSec corpus for Senate privacy/surveillance staff`
5. `FOIA-sourced surveillance briefing — [Committee] jurisdiction`

---

### Think Tanks and Policy Organizations (10 contacts — Heritage, CAP, CSIS, Brookings, Atlantic Council, Brennan, Georgetown CPT, EPIC, R Street, Cato)

**Frame**: Research quality, citability, primary-source documentation that fills a gap in published policy literature.

**Opening hook — what resonates:**
- Reference a specific published report by that organization and explain exactly what the corpus adds
- Lead with the FOIA/contract sourcing (think tanks want citable documentation, not advocacy)
- Name the governance or precedent angle (international systems, comparative policy design)

**Sample opening:**
```
Georgetown CPT's *American Dragnet* (2022) remains the most comprehensive mapping of commercial data broker resale to immigration enforcement. The corpus I'm sharing updates that documentation with the ELITE system's 2025–2026 operational parameters — all drawn from FOIA disclosures and DHS contracts on USASpending.gov — and adds a technical countermeasures layer that *Dragnet* did not address.
```

**Avoid**: Framing the corpus as an advocacy document. Think tank fellows want research, not campaigns. The corpus is primary-source documentation — present it that way.

**Domain emphasis**: Domains 1, 6, 25, 33, 37 (governance structure, precedent from international systems)

**5 subject line variants (Think tank):**
1. `Primary-sourced ELITE documentation — extends [Organization's recent report]`
2. `FOIA-backed surveillance corpus — citable for policy work`
3. `Palantir ELITE 2025–2026: primary documentation + countermeasures`
4. `Surveillance infrastructure documentation — policy research resource`
5. `OpSec corpus for [Organization] policy team`

---

### Law Schools — Civil Liberties and Surveillance Law Clinics (7 contacts — Cornell, Yale, Columbia, Stanford, Georgetown Law, Harvard, NYU)

**Frame**: Legal citability, direct application to active dockets, primary-source structure compatible with brief writing.

**Opening hook — what resonates:**
- Name a specific type of case the clinic handles (removal proceedings, DV-immigration, FOIA litigation) and connect a specific corpus section to it
- Lead with citability: all corpus claims are tied to primary documents (FOIA disclosures, DHS contracts, court filings) with direct URLs
- Mention student research opportunities or clinic coursework integration

**Sample opening:**
```
The ELITE system documentation in Section 2 of the threat model is drawn entirely from primary sources — Palantir's DHS contracts on USASpending.gov, FOIA-disclosed ELITE operational specifications, and court filings in active immigration cases. It is structured to be citable in removal proceedings briefs and does not rely on secondary characterizations.
```

**Avoid**: Operational security implementation detail. Clinic directors want brief-ready documentation, not step-by-step device hardening instructions. Reserve the implementation guide as a secondary offer after the initial call.

**Domain emphasis**: Domains 6 (constitutional limits on surveillance), 25 (FISA interface with immigration enforcement)

**5 subject line variants (Law school):**
1. `FOIA-sourced ELITE documentation — briefable in immigration dockets`
2. `Palantir ELITE briefing — primary-source corpus for clinic work`
3. `Surveillance law resource — primary-source documentation for [Clinic name]`
4. `ELITE system FOIA documentation — clinic-applicable`
5. `Immigration enforcement surveillance corpus — citable primary sources`

---

### Civil Rights Organizations (2 contacts — ACLU, Lawyers' Committee)

**Frame**: Equity angle, differential impact, litigation readiness, community protection.

**Opening hook — what resonates:**
- Lead with the disparate impact data (ELITE's geographic and demographic concentration in majority-minority communities)
- Connect to ongoing litigation (ACLU's Section 702 suits; Lawyers' Committee's redistricting and enforcement work)
- Frame the corpus as litigation-support documentation, not just advocacy material

**Sample opening:**
```
ELITE's address confidence scoring disproportionately targets residents of majority-Black and Latino neighborhoods in ICE enforcement priority zones — a product of the underlying training data's geographic concentration and the commercial data broker inputs. The FOIA documentation in Section 3 of the threat model provides primary-source evidence of this targeting architecture, structured to support civil rights litigation challenging discriminatory enforcement patterns.
```

**Domain emphasis**: Domains 1, 33 (surveillance and its impact on democratic participation and minority communities)

**5 subject line variants (Civil rights):**
1. `ELITE targeting documentation — civil rights litigation resource`
2. `Differential surveillance impact — primary-sourced ELITE corpus`
3. `Palantir ELITE briefing — ACLU/Lawyers' Committee relevance`
4. `ICE surveillance equity documentation — FOIA-sourced`
5. `Civil rights lens on ELITE targeting — primary documentation`

---

## Section 7: Email Templates with Customization Fields

> Use these templates as starting points. Every email sent must have a customized opening of 2–3 sentences specific to the recipient's recent work. Never send a template without customization. Bracketed fields [like this] must be replaced before sending.

---

### Template: Week 1 Intro Email — Senate Staff Version

**Subject** (choose 1 of 5 variants from Section 6):

**Body:**
```
[Contact Name],

[CUSTOM OPENING — 2–3 sentences. Reference a specific committee hearing, report, or recent action from this office. Connect it directly to why the corpus is relevant NOW. Example: "As the Judiciary Subcommittee on Privacy prepares for the June 12 Section 702 deadline, the commercial data broker pipeline documentation in the corpus may be directly useful for oversight letter drafting or hearing prep."]

I'm sharing a primary-source documentation corpus on the federal government's surveillance infrastructure — specifically Palantir's ELITE system, the NSA Section 702 commercial data interface, and the commercial data broker pipeline that underlies both.

The corpus is three documents:
- Threat model: What government systems can see (Palantir ELITE targeting parameters, Venntel/Babel Street data pipeline, DOGE database consolidation), all drawn from FOIA disclosures and DHS contracts on USASpending.gov
- Countermeasures playbook: Specific responses by threat level
- Implementation guide: Exact steps with verification checkpoints

All claims are tied to primary documents with direct URLs — designed to be citable in oversight letters, hearing prep, and constituent briefings without requiring secondary verification.

[SHORT URL — bit.ly/palantir-briefing]

I'd welcome a 20-minute call to walk through the sections most relevant to [Committee]'s jurisdiction. [Calendly link — optional at initial send; include if space permits]

[Your name]
[Title/affiliation if applicable]
```

---

### Template: Week 1 Intro Email — Think Tank Version

**Subject** (choose 1 of 5 variants from Section 6):

**Body:**
```
[Contact Name],

[CUSTOM OPENING — 2–3 sentences. Reference a specific report, policy brief, or research area from this organization. Explain exactly what the corpus adds to their existing documentation. Example: "Your organization's 2024 work on commercial surveillance infrastructure identified the data broker resale mechanism as the primary gap in legislative oversight. The corpus I'm sharing documents that pipeline in primary-source detail — Palantir contracts, FOIA-disclosed ELITE specifications, and Venntel resale agreements — with a technical layer not present in policy briefings."]

The corpus is primary-source documentation on the federal surveillance infrastructure that intersects most directly with [Organization]'s current work on [relevant policy area]:

- Threat model: Palantir ELITE targeting system, NSA Section 702 commercial data interface, commercial data broker pipeline — all FOIA-sourced with direct document URLs
- Countermeasures playbook: Technical and administrative responses, tiered by exposure level
- Implementation guide: Practical steps with verification checkpoints

The sourcing is structured to meet academic citation standards — every substantive claim points to a FOIA disclosure, government contract, or court filing. It is designed to be incorporated into published policy work without additional verification.

[SHORT URL — bit.ly/palantir-briefing]

Happy to discuss the documentation or answer questions about any section. A 20–30 minute call would let me walk through the sections most relevant to [Organization's current project or recent publication].

[Your name]
```

---

### Template: Week 1 Intro Email — Law School Clinic Version

**Subject** (choose 1 of 5 variants from Section 6):

**Body:**
```
[Contact Name / Clinic Director],

[CUSTOM OPENING — 2–3 sentences. Name a specific type of case the clinic handles and connect a specific corpus section to it. Example: "The ELITE system documentation in Section 2 of the threat model maps directly to active removal proceedings — specifically how address confidence scores are generated from commercial data broker inputs without a warrant, and how that scoring influences prioritization decisions. For clinics handling removal cases in [state], this primary-source documentation is structured to be citable in briefs."]

The corpus is three documents:

- Threat model: Palantir ELITE system targeting architecture, NSA Section 702 commercial data pipeline, Venntel and Babel Street data resale — all drawn from FOIA disclosures, DHS contracts, and court filings with direct URLs
- Countermeasures playbook: Tiered responses for clients at different risk levels
- Implementation guide: Step-by-step actions, no technical expertise required

All substantive claims are tied to primary documents with direct URLs — designed to be citable in briefs and FOIA litigation without requiring additional sourcing. The California DROP platform documentation (Section 3.4) is particularly relevant for clinics serving clients without government-issued ID.

[SHORT URL — bit.ly/palantir-briefing]

I'd welcome a 20-minute call to discuss how specific sections apply to [Clinic]'s current docket. [Calendly link]

[Your name]
```

---

### Template: Week 1 Intro Email — Civil Rights Organization Version

**Subject** (choose 1 of 5 variants from Section 6):

**Body:**
```
[Contact Name],

[CUSTOM OPENING — 2–3 sentences. Reference a specific ACLU or Lawyers' Committee litigation or policy initiative. Connect the corpus to the equity angle. Example: "The ACLU's ongoing Section 702 challenge has focused on the warrant requirement gap in NSA collection. The corpus I'm sharing documents the commercial data broker interface that allows location data from Venntel and Babel Street to enter the surveillance supply chain without a Section 702 authorization — a parallel gap the documentation may help support."]

The corpus documents the federal surveillance infrastructure that most directly affects Black and Latino communities:

- Threat model: Palantir ELITE targeting system (address confidence scoring concentrates in majority-minority enforcement zones), NSA Section 702 commercial interface, commercial data broker pipeline — all FOIA-sourced
- Countermeasures playbook: Community-level responses, tiered by risk
- Implementation guide: Client-facing actions (including data broker opt-outs that directly degrade ELITE targeting inputs)

The equity documentation — specifically the geographic and demographic concentration of ELITE enforcement prioritization — is structured to support civil rights litigation challenging discriminatory enforcement patterns.

[SHORT URL — bit.ly/palantir-briefing]

Happy to discuss the litigation-support applications in a 20-minute call. [Calendly link]

[Your name]
```

---

### Template: Week 2 Follow-Up Email (Soft Tone — Non-Replies)

**Subject**: `Following up — [one-phrase reference to corpus relevance for this contact]`

**Body:**
```
[Contact Name],

Circling back briefly on the [corpus/briefing] I sent [date].

[ONE SENTENCE — reference a recent development relevant to that contact's work since the initial send. Example: "Given the June 12 Section 702 reauthorization vote, the commercial data broker pipeline documentation may be immediately useful for your oversight work." Or: "Your organization's [recent report/testimony/op-ed] published this week maps closely to the ELITE documentation in the corpus."]

I wanted to make sure the resource reached you — [one sentence on why it's specifically relevant to their function, not a generic restatement].

Happy to do a quick 20-minute call — [Calendly link] — or answer any questions by email.

[Your name]
```

**Note on tone:** This follow-up must feel like a genuine check-in, not a marketing sequence. The one-sentence current-events hook is what distinguishes it from a mass follow-up. Do not send this template without customizing that sentence.

---

### Template: Phone Call Script — Top 3 Senators (If Email Silent at Day 12+)

**Preparation before calling:**
- Know the named staff member's name and exact title
- Have a one-sentence value proposition ready
- Have the Calendly link ready to give verbally or follow up via email immediately

**30-second introduction:**
```
"Hi, my name is [Your name] — I'm trying to reach [Staff Name] who handles digital surveillance policy for Senator [X]'s office. I sent a briefing document on June 1st on Palantir's ELITE system and the commercial data broker pipeline — I wanted to make sure it reached [Staff Name] directly."
```

**2-minute value proposition (if connected to staff member):**
```
"Thank you for taking my call. I'll be brief. I've prepared a primary-source documentation corpus on the federal surveillance infrastructure — specifically Palantir's ELITE system, which uses commercial data broker inputs without a warrant to generate address confidence scores for ICE enforcement targeting.

The documentation is all drawn from FOIA disclosures and DHS contracts — structured to be citable in oversight letters, hearing prep, or constituent briefings. Given the Section 702 reauthorization timeline and [Senator]'s work on [relevant issue], I thought this might be directly useful for your office.

The corpus is published at a public link — I can send it again with a two-paragraph summary if that's easier to review than the full document."
```

**1-minute next steps:**
```
"Would it be useful to schedule a 20-minute call? I can walk through the sections most relevant to [Committee/office]'s current jurisdiction. Or if you'd prefer, I can send a one-page briefing memo. Which would be more useful?"
```

**Common objections + response templates:**

*"We already have our own research on surveillance."*
> "I understand — the corpus is specifically designed to complement existing research, not replace it. The value is the primary-source FOIA documentation layer — every claim is tied to a government contract or disclosure with a direct URL. Happy to send just the two-paragraph executive summary and you can assess whether it adds anything."

*"Please send your information to our general inbox."*
> "Understood — I'll send a brief summary to [office general contact email] with your name in the subject line. Is [staff name] the right person to address it to for digital surveillance policy?"

*"We don't have time right now."*
> "Completely understood. The briefing is available any time at [short URL] — if it becomes relevant to a hearing or oversight project in the next few weeks, I'm happy to do a quick call on short notice. I'll follow up by email."

---

### Template: Meeting Request Email (After Positive Reply)

**Subject**: `20-min call — [specific topic relevant to this contact]`

**Body:**
```
[Contact Name],

Thank you for your reply — glad the [corpus / briefing] is useful.

I'd welcome a 20–30 minute call to walk through the sections most directly applicable to your work, specifically [one or two corpus sections most relevant to this contact's stated interest].

Here's my Calendly link for scheduling: [Calendly link]

Alternatively, here are three specific times that work on my end:
- [Day, Date, Time] [Timezone]
- [Day, Date, Time] [Timezone]
- [Day, Date, Time] [Timezone]

Before the call, I'll send a one-paragraph agenda so we can focus the time.

[Your name]
```

---

## Section 8: Success Metrics Tracking

### Daily KPIs (tracked in Google Sheets Tab 5, updated every morning)

| KPI | How Measured | Target by Day 7 | Target by Day 14 | Target by Day 21 |
|-----|-------------|-----------------|------------------|------------------|
| Emails sent cumulative | Tab 2 count | 25 | 25 + follow-ups | Same |
| Bitly click rate | Clicks ÷ sends × 100 | >30% (8+ clicks) | >40% (10+ clicks) | >45% |
| Reply rate (any substantive) | Replies ÷ sends × 100 | 20%+ (5+ replies) | 28%+ (7+) | 35%+ (9+) |
| Stage 1+ reply ratio | Stage1+ ÷ all replies | 50%+ | 60%+ | 60%+ |
| Meetings scheduled | Tab 3 count | 1+ | 3+ | 5+ |
| Bounce rate | Bounces ÷ sends | <5% | <5% | <5% |

### Wave-Level KPIs

| Wave | Trigger | Reply Target | Adoption Signal Target | Decision Point |
|------|---------|-------------|----------------------|----------------|
| Week 1 (25 sends) | June 1–5 | 5+ substantive replies by Day 7 | 0–1 early interest signals | Gate 1 (June 7) |
| Week 2 (follow-ups + law schools) | June 8–12 | 8+ cumulative substantive replies by Day 11 | 3+ adoption signals | Gate 2 (June 15) |
| Week 3 (meetings) | June 15–21 | — | 2+ commitment signals (implement or distribute) | Tier 2 readiness gate (June 19) |

**Reply type definitions (for Stage classification):**
- **Stage 0 — Acknowledgment**: Generic "thank you, received" or "will review" — no substantive content. No further action until Day +10 follow-up.
- **Stage 1-Question**: Contact asks a substantive question about a specific corpus section, sourcing, or use case. Reply within 24 hours using R1 template. Attach Calendly link.
- **Stage 1-MeetingRequest**: Contact explicitly requests a call or meeting. Book within 48 hours.
- **Stage 1-Routing**: Contact forwards to a colleague or says "you should contact [name]." Log the referral. Engage the referred contact within 24 hours — this is a warm lead.
- **Declined**: Contact explicitly says not interested or asks to be removed. Remove immediately. Mark closed. Do not follow up.
- **OOO (Out of Office)**: Auto-responder. Do NOT count as a response. Note the return date in Tab 1. Set a calendar reminder to follow up when they return.
- **Bounce**: Delivery failure. Research alternate contact immediately. Do not count as a send in your metrics until re-sent to a valid address.

---

### Google Sheets Template Structure

**Tab 1: Contact Master List**

| Column | Content |
|--------|---------|
| A | Contact Name |
| B | Organization |
| C | Title/Function |
| D | Email Address |
| E | Sector (Senate/Think Tank/Law School/Civil Rights) |
| F | Wave (1/2/3) |
| G | Send Date |
| H | Send Time |
| I | Bitly Click (Y/N) |
| J | Click Date |
| K | Reply Received (Y/N) |
| L | Reply Date |
| M | Reply Type (Stage0/Stage1-Q/Stage1-MR/Stage1-R/Declined/OOO/Bounce) |
| N | Days-to-Reply (formula: =IF(L2="","",L2-G2)) |
| O | Follow-Up Sent (Y/N) |
| P | Follow-Up Date |
| Q | Meeting Scheduled (Y/N) |
| R | Meeting Date |
| S | Meeting Status (Scheduled/Completed/Rescheduled/Cancelled) |
| T | Next Action |
| U | Notes |

**Auto-calc formulas (add to bottom of each column):**
- Reply rate: `=COUNTIF(K:K,"Y")/COUNTA(A2:A26)*100`
- Stage 1+ ratio: `=COUNTIFS(M:M,"Stage1-*")/COUNTIF(K:K,"Y")*100`
- Avg days-to-reply: `=AVERAGEIF(N:N,"<>")`
- Meeting scheduled rate: `=COUNTIF(Q:Q,"Y")/COUNTA(A2:A26)*100`

---

**Tab 2: Email Engagement Log**

| Column | Content |
|--------|---------|
| A | Date |
| B | Contact Name |
| C | Organization |
| D | Email Type (Initial/Follow-up/Meeting Request) |
| E | Subject Line Used |
| F | Bitly Clicks at 24h |
| G | Bitly Clicks at 72h |
| H | Reply Received |
| I | Reply Content Summary |
| J | Reply Classification |

---

**Tab 3: Meeting Schedule**

| Column | Content |
|--------|---------|
| A | Contact Name |
| B | Organization |
| C | Meeting Date |
| D | Meeting Time |
| E | Format (Phone/Video/In-Person) |
| F | Attendees |
| G | Status (Scheduled/Completed/Rescheduled/Cancelled) |
| H | Key Outcomes |
| I | Follow-Up Committed |
| J | Next Steps |
| K | Adoption Signal (Y/N/Partial) |
| L | Tier 2 Candidate (Y/N) |

---

**Tab 4: Policy Uptake Signals**

| Column | Content |
|--------|---------|
| A | Organization |
| B | Contact Name |
| C | Signal Type (Internal Share / Practice Implementation / Referral / Media Mention / Policy Cite / Distribution Request) |
| D | Signal Description |
| E | Date Detected |
| F | Confidence Level (High/Medium/Low) |
| G | Escalation Path |
| H | Follow-Up Action |

---

**Tab 5: KPI Summary (update every Friday)**

| Row | Metric | Week 1 Actual | Week 2 Actual | Week 3 Actual | Final |
|-----|--------|--------------|--------------|--------------|-------|
| 1 | Total sends | | | | |
| 2 | Total Bitly clicks | | | | |
| 3 | Click rate % | | | | |
| 4 | Total replies | | | | |
| 5 | Reply rate % | | | | |
| 6 | Stage 1+ replies | | | | |
| 7 | Stage 1+ ratio % | | | | |
| 8 | Meetings scheduled | | | | |
| 9 | Meetings completed | | | | |
| 10 | Meeting completion rate % | | | | |
| 11 | Adoption signals logged | | | | |
| 12 | Bounces | | | | |
| 13 | Bounce rate % | | | | |
| 14 | Gate 1 result | | N/A | N/A | |
| 15 | Gate 2 result | N/A | | N/A | |
| 16 | Tier 2 readiness result | N/A | N/A | | |

---

## Section 9: Contingency Decision Trees

> All contingency protocols are pre-committed. Do not improvise under pressure. Activate the relevant protocol and follow it in order.

---

### Contingency A — Week 1 Low Reply Rate

**Trigger**: Fewer than 3 substantive (Stage 1+) replies by end of Day 4 (June 4) — or Gate 1 click rate below 20% on Day 7.

**Response sequence (execute in order — do not skip ahead):**

1. **Check email deliverability (Day 5 morning, 20 min)**
   - Open mail-tester.com. Send a test from your outreach address to the mail-tester address. Check the score.
   - If score is below 6/10: diagnose the deliverability issue before any further sends. Common causes: missing SPF/DKIM authentication, sending from a free Gmail with no custom domain, subject line triggering spam filters. Resolve before proceeding.
   - Check your own Sent folder: do the emails appear in your sent mail? If not, they may have failed silently.
   - Check if any Day 1–4 sends show as bounced in your outbox but were not logged.

2. **Verify contact routing (Day 5, 15 min)**
   - Were the emails sent to named individuals (legislative counsel, named fellow, supervising attorney)? Or to general inboxes (info@, press@, general@)?
   - If any were sent to general inboxes: re-send to a named individual at that organization. Flag this as a "corrected send" in Tab 1.

3. **Warm follow-up phone calls to 5 top senators (Day 8–9, if Day 4 trigger met)**
   - Use the Phone Call Script from Section 7.
   - One call attempt per office. Ask for the named staff member. Do not leave a detailed voicemail — say only "I'm following up on a briefing I sent June 1st on Palantir's ELITE system — I wanted to make sure it reached [name]."

4. **Ask existing contacts for referrals (Day 8, 10 min)**
   - If you have any existing contacts in the policy space (outside the 25-contact list), email one or two asking if they know anyone at the organizations you are targeting. Warm referrals convert at significantly higher rates than cold outreach.

5. **Activate media amplification strategy (if Day 7 Gate 1 STOP triggered)**
   - Consider whether a single substantive op-ed or public post about the corpus would generate inbound interest from contacts on the list. This is a secondary strategy — do not use it as a substitute for the outreach but as a parallel amplification.
   - If a political trigger (congressional hearing, news story, executive order about ICE surveillance or Palantir) occurs during the contingency period: reference it in remaining outreach. Political triggers accelerate think tank and Senate cohort response rates.

---

### Contingency B — Week 2 Policy Uptake Low

**Trigger**: Fewer than 2 policy uptake signals (adoption indicators) by end of Day 14 (June 14) — or Gate 2 click rate below 30% and fewer than 2 meetings scheduled.

**Diagnostic sequence:**

1. **Click-through analysis by sector (30 min)**
   Open Bitly. Which sector — Senate, think tank, law school — has the lowest click rate? If the underperformance is sector-specific, the subject line is not resonating for that sector. Test a sector-specific variant on remaining follow-up sends.

2. **Meeting no-show rate (15 min)**
   Of scheduled meetings, how many completed vs. cancelled? If no-show rate is above 25%, the scheduling process is not qualifying intent. Before the next meeting confirmation, add one qualification question: "To make the call most useful — are you focused primarily on legislative oversight, civil liberties litigation, or operational security for your team?"

3. **Feedback quality assessment (20 min)**
   Are replies generic ("looks interesting") or specific ("the Part 0 opt-outs would be useful for our intake forms")? Generic-only replies indicate framing is too abstract. Add a concrete use-case statement to remaining follow-ups.

**Response levers (apply in sequence):**

- **Lever 1 — Pivot to secondary sector**: If think tanks are underperforming, shift emphasis to law school clinics (faster adoption signals; clinic directors are closer to active dockets). If Senate is silent, shift emphasis to think tanks (intermediary step toward Senate adoption).
- **Lever 2 — Extend timeline to July 1**: Announce internally (in WORKLOG.md) that Phase 1 follow-up extends to July 1. No new contacts — extend the follow-up loop for the existing 25.
- **Lever 3 — Defer Tier 2 readiness gate**: If extending to July 1, the Tier 2 readiness gate slides to July 5. Group B launch slides to August 1. Log this decision in WORKLOG.md with the data that warranted it.
- **Lever 4 — Assess content resonance**: If all three levers applied and adoption is still below 35% by Day 28, pause Tier 2 and schedule diagnostic sessions with 3 early adopters. Ask directly: what would make this corpus more useful for your specific work?

---

### Contingency C — Contact Unavailable (OOO / Position Change / Extended Leave)

**Trigger**: Contact replies "not available until [date]" OR pre-launch verification reveals a contact has departed the organization.

**Response:**

1. **Note the return date** in Tab 1, column "Notes." Set a calendar reminder for the day after their stated return to follow up. Do not skip this contact.
2. **Identify a backup contact** at the same organization in the same function. If no backup is findable, note "deferred — no backup identified" in Tab 1. Do not replace them with a contact from a different organization.
3. **Mark as "deferred"** not "unresponsive." Deferred contacts are in the follow-up queue; unresponsive contacts are not.
4. **Do not count deferred contacts** in your denominator for reply rate calculations until they have been reached (either on return from OOO or via backup contact). A contact who never received your email cannot be counted as a non-reply.

---

### Contingency D — Email Delivery Issues (Bounce Rate Exceeds 5%)

**Trigger**: More than 1–2 bounces from 25 sends (>5% bounce rate). Hard bounces only — soft bounces (full inbox) are not the same as hard bounces (invalid address).

**Response:**

1. **Stop the current wave** (do not send remaining emails until the list is validated).
2. **Re-verify all remaining contact emails** against official organization websites and LinkedIn. Do not accept an email address that cannot be confirmed from a primary source.
3. **Re-send bounced emails** to corrected addresses. Log the correction in Tab 1.
4. **For contacts with persistent bounces** (no valid email findable): call the organization's main line and ask to speak with the named staff member. Explain you sent an email that bounced and ask for the correct address.
5. **Check your outreach address** for any spam blacklist flags (check at mxtoolbox.com). If your sending address is on a blacklist, you will need to resolve this before resuming sends.
6. **After resolving**: check mail-tester.com score before resuming. Do not resume if score is below 7/10.

---

## Section 10: Pre-Launch Checklist (Day 0 = June 1, Day -1 = May 31)

> Work through this list top-to-bottom on May 31. Do not launch on June 1 if any item is unchecked.

**Infrastructure:**
- [ ] All 25 contact emails verified and current — spot-check 5 random contacts against official websites (not just the list)
- [ ] Google Sheets monitoring dashboard complete: 5 tabs created, formulas entered, auto-calc rows populated
- [ ] Email templates finalized, spell-checked, and saved as Gmail drafts — test delivery to personal Gmail account and one non-Gmail account (no spam landing)
- [ ] Calendly link live and tested — booking works from a private browser, time zone is correct
- [ ] Gist URL loads without login in a private browser — all 3 documents present
- [ ] Bitly short URL (bit.ly/palantir-briefing) redirects correctly — tested in private browser
- [ ] Mail-tester.com score ≥ 8/10 from the outreach address

**Scheduling:**
- [ ] Calendar holds placed for: Gate 1 (June 7, 9 AM), Gate 2 (June 15, 9 AM), Tier 2 gate (June 19, 9 AM), Day 8 follow-up reminder (June 8, 8 AM)
- [ ] Send-day reminders set for 7:30 AM on Days 1–5 and Days 8–10
- [ ] 30-minute daily time blocks reserved for reply processing throughout June 1–21

**Content:**
- [ ] All 5 Wave 1 email drafts (Senate contacts) complete in Gmail drafts — personalized opening sentences verified for each
- [ ] Wave 2 and Wave 3 drafts at least outlined — final personalization can happen day-of for Days 3–5
- [ ] Phone call script reviewed and practiced (if phone outreach needed at Day 12+)
- [ ] Domain materials accessible (Gist URL bookmarked on device you will use for outreach)

**Operational:**
- [ ] Google Alerts active: "ELITE address confidence score", "Palantir ICE ELITE", "DROP platform immigration"
- [ ] Backup contact list created in Tab 1 Notes column: for each primary contact, at least one backup function noted (not necessarily a named individual, but a function — "privacy counsel" or "senior immigration fellow")
- [ ] User availability confirmed: able to review and respond to replies within 24 hours throughout June 1–21 (Stage 1+ replies require same-day response)
- [ ] Escalation path confirmed: if user is unavailable for more than 48 hours during Week 1, who has authority to send follow-ups? Note this.

---

## Section 11: Implementation Notes

### Send Time Optimization

Send times are based on government and nonprofit email engagement patterns.

| Contact Type | Best Send Window | Avoid |
|-------------|-----------------|-------|
| Senate offices | 8:30–10:00 AM Mon–Thu | Friday afternoon (very low); Monday morning (inbox clutter from weekend); before 8 AM |
| Think tanks | 9:00–11:00 AM Tue–Fri | Monday (full inbox); Friday afternoon |
| Law school clinics | 10:00 AM–12:00 PM Tue–Thu | Monday (faculty/clinic schedule); Friday afternoon; exam periods if detectable |
| Civil rights organizations | 9:00–11:00 AM Tue–Thu | Monday; Friday afternoon |

### Email Frequency Rules

- Maximum 1 email per contact per day (never send two emails to the same contact on the same day, even if one is a response)
- Maximum 5 new contact emails per day (to avoid spam filter triggers and allow personalization quality)
- Maximum 2 contacts to the same organization per wave (to avoid appearing coordinated or bulk)
- Total outreach per contact: 1 initial + 1 follow-up only. No third email unless you made an explicit commitment during a previous interaction.

### Reply Handling Protocol

| Reply Type | Response Time | Action |
|-----------|--------------|--------|
| Stage 1-Question | 24 hours | Use R1 template; attach Calendly link |
| Stage 1-MeetingRequest | 48 hours | Book meeting; send confirmation + agenda |
| Stage 1-Routing | 24 hours | Log referral; contact the referred person within 24h |
| Stage 0-Acknowledgment | 10 days (follow-up) | No immediate response; add to Day 10+ follow-up queue |
| Declined | Immediate | Remove from list; mark closed |
| OOO | When contact returns | Note return date; set reminder |
| Bounce | Immediate | Research alternate contact; re-validate list |

Log all replies in Tab 1 within 2 hours of receipt. Do not let replies sit unclassified.

### Escalation to Phone Call

Escalate a contact to phone outreach if ALL of the following are true:
- The contact is one of the top 5 highest-priority organizations (Senate offices, Brennan Center, Georgetown CPT, EPIC, CDT)
- You have sent the initial email AND the Day 8 follow-up
- No Bitly click detected AND no reply (confirming the contact has not seen the email — not that they declined)
- At least 12 days have elapsed since the initial send

Do not phone contacts who have clicked the Bitly link but not replied — they have seen the email and are making a choice. Respect that.

### Tier 2 Trigger Assessment

A contact is a strong Tier 2 pilot candidate if they show 2 or more of the following signals during Phase 1:

| Signal | Weight |
|--------|--------|
| Replied within 24 hours of initial send | High |
| Asked 2+ clarifying questions | High |
| Mentioned potential implementation or distribution | High |
| Scheduled and completed a briefing call | High |
| Generated a warm referral to another contact | Medium |
| Mentioned the corpus in public context (media, hearing, brief) | Very High — immediate Tier 2 flag |

Log all Tier 2 signals in Tab 4 as they occur. The Tier 2 pilot cohort selection on June 19 draws from this log.

---

## Appendix: Quick Reference Card

```
PHASE 1 EXECUTION QUICK REFERENCE — JUNE 2026
=========================================================

LAUNCH: June 1, 2026 | GATE 1: June 7 | GATE 2: June 15 | TIER 2 GATE: June 19
EXECUTOR: Anya | CORPUS: bit.ly/palantir-briefing (verify before Day 1)
TRACKING: Google Sheets "Phase 1 Policy Outreach Tracker — June 2026"

DAILY SEND SCHEDULE:
  Day -1 (May 31): Final prep. No sends. Go/no-go.
  Day 1 (June 1): 5 Senate staff (Judiciary, Intel, Homeland, Wyden, Markey) — 8:30 AM
  Day 2 (June 2): 3 Senate/CRS (Commerce, House Judiciary, CRS) — 8:30 AM
  Day 3 (June 3): 5 think tanks Part 1 (Brennan, Georgetown CPT, EPIC, R Street, Cato) — 9 AM
  Day 4 (June 4): 5 think tanks Part 2 (New America, CAP, Just Security, Lawfare, CDT) — 9 AM
  Day 5 (June 5): 5 law schools Part 1 (Georgetown Law, Yale MFIA, Harvard, Stanford, NYU) — 10 AM
  Day 6 (June 6): No sends. Reply processing. Day 8 draft prep.
  Day 7 (June 7): GATE 1 checkpoint. Day 8 follow-up prep.
  Day 8 (June 8): 2 law schools (Chicago Law, CUNY) + Wave 1 follow-ups (Senate staff)
  Days 9–12:      Follow-up loop, meeting scheduling, law school follow-ups
  Day 12 (June 12): Section 702 deadline anchor — Senate escalation emails
  Day 13–14:      Reply processing. Gate 2 prep.
  Day 15 (June 15): GATE 2 checkpoint
  Days 16–19:     Meeting completion, adoption signal collection, phone calls
  Day 19 (June 19): Tier 2 readiness gate
  Days 20–21:     Week 3 summary report. Log all data.

GATE 1 (June 7):
  >30% clicks AND 1+ Stage 1+ reply → GO
  20–30% clicks → CAUTION (revise subject lines)
  <20% clicks → STOP (Contingency A — deliverability diagnostic, 48h max)

GATE 2 (June 15):
  >40% clicks + ≥3 meetings → GO (authorize Tier 2 Group B — July 15)
  30–40% clicks + 1–2 meetings → CAUTION (extend to July 1)
  <30% clicks + 0 meetings → STOP (Contingency B — diagnostic only)

TIER 2 GATE (June 19):
  4–5 KPIs met → Tier 2 proceeds July 15
  2–3 KPIs met → Extend to July 1, re-assess July 5; Group B slides to Aug 1
  0–1 KPIs met → Full diagnostic. Group B deferred minimum to Aug 1.

RESPONSE CLASSIFICATION:
  Stage 0 = Generic acknowledgment (R2 follow-up at Day +10)
  Stage 1-Q = Substantive question (R1 within 24h + Calendly)
  Stage 1-MR = Meeting request (book within 48h)
  Stage 1-R = Routing to colleague (engage referral within 24h)
  Declined = Mark closed. Do not follow up.
  OOO = Note return date. Follow up when back.
  Bounce = Validate list immediately.

CONTINGENCY TRIGGERS:
  Contingency A: <3 Stage 1+ replies by Day 4 → deliverability check, phone calls, referral ask
  Contingency B: <2 uptake signals by Day 14 → sector pivot, extend timeline, defer Tier 2
  Contingency C: Contact unavailable → mark deferred, find backup, do not skip
  Contingency D: >5% bounce rate → stop wave, validate list, check sending address

THREE THINGS THAT MATTER MOST:
  1. Meetings scheduled — not clicks, not replies, meetings
  2. Correct function targeted — legislative counsel not press; clinic director not admin
  3. One follow-up maximum per contact, with a different subject line and a fresh hook
=========================================================
```

---

*Version 2.0 — Created 2026-05-13. Phase 1 launch target: June 1, 2026. Gate checkpoints: June 7 (Gate 1), June 15 (Gate 2), June 19 (Tier 2 readiness). All thresholds pre-committed — do not adjust during execution without logging the data that warranted the adjustment. Coordinates with: `TIER1_EXECUTION_RUNBOOK.md`, `TIER1_OUTREACH_EXECUTION_PLAN.md`, `TIER_1_SUCCESS_MEASUREMENT_FRAMEWORK.md`, `TIER_2_EXPANSION_ARCHITECTURE.md`, `TIER_2_PILOT_LAUNCH_READINESS.md`.*
