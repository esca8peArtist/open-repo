---
title: "June 23-25 T+7 Checkpoint Execution Checklist"
subtitle: "Domains 51, 48, 59 — Daily task list with timing and decision gates"
created: "2026-06-22"
session: "3911"
status: "ready for use — print this page for June 23-25"
target_user_time: "15-20 minutes per day"
---

# June 23-25 T+7 Checkpoint Execution Checklist

*Session 3911 | June 22, 2026*

**Purpose**: Daily action checklist for June 23-25. Print this page or copy tasks to your calendar. Each day takes 15-20 minutes total (morning + afternoon).

---

## June 23 (Monday) — T+0 Checkpoint

**Morning (9:00–11:30 AM)**

- [ ] **9:00 AM**: Open `supremecourt.gov/opinions/slipopinion/25` in new browser tab
  - Search for: Case 24-38 (Little v. Hecox), Case 24-43 (West Virginia v. B.P.J.), Case 25-332 (Trump v. Slaughter), Case 25-365 (Trump v. Barbara)
  - If **Little v. Hecox or BPJ issued**: STOP. Execute Domain 50 immediate distribution (see CONTINGENCY ACTIVATION section below). This overrides all other June 23 tasks.
  - If **Trump v. Slaughter issued**: Note it. Continue with T+7 tasks. Update Domain 51 messaging if FEC implications are clear (see DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md for guidance).
  - If **Trump v. Barbara issued**: Verify at supremecourt.gov (do not rely on news alerts). If confirmed, see CONTINGENCY ACTIVATION section. Continue with T+7 tasks.
  - If **none of the above**: Continue to next task.

- [ ] **9:10 AM**: Check your sent folder for Domain 51 Wave 1 sends
  - Find emails to: Erin Chlopak (echlopak@campaignlegalcenter.org) and Issue One (info@issueone.org)
  - Mark: **[ ] Sent June 16-17** / **[ ] Not yet sent — SEND NOW**
  - If NOT sent: Use DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md. CLC first, Issue One 90 minutes later. Then T+7 checkpoint falls June 30 (not June 23-24). Mark new send date and adjust all June 23-25 tasks to June 30.

- [ ] **9:15 AM**: Check your sent folder for Domain 48 Wave 1 sends
  - Find email to: Nicole Porter (nporter@sentencingproject.org)
  - Mark: **[ ] Sent June 16-18** / **[ ] Not yet sent — SEND NOW**
  - If NOT sent: Use DOMAIN_48_EMAIL_TEMPLATE_SET.md Template A. Send Sentencing Project first. Then T+7 checkpoint falls June 30 (not June 23-25). Mark new send date.

- [ ] **9:20 AM**: Check inbox for Domain 51 replies (CLC and Issue One)
  - **For each reply received**, fill this table:
    
    | Contact | Sent date? | Reply received? | Reply date | Signal (S/M/W/B/--) | Notes |
    |---------|-----------|-----------------|------------|---------------------|-------|
    | CLC (Erin Chlopak) | | | | | |
    | Issue One | | | | | |

  - **Signal scoring** (apply to each reply — see Signal Classification section below):
    - **S (STRONG)**: Meeting request, named forwarding, citation in their work, substantive follow-up question
    - **M (MODERATE)**: Acknowledged receipt + expressed interest, forwarded to team, requested full document
    - **W (WEAK)**: Auto-acknowledgment, form response, no individual engagement
    - **B (BOUNCE)**: Hard bounce or OOO — re-verify address, log alternate if named
    - **--**: No reply yet (normal at T+7 for cold outreach)

- [ ] **9:30 AM**: Check inbox for Domain 48 replies (Sentencing Project and Prison Policy Initiative)
  - Find replies from: Nicole Porter (nporter@sentencingproject.org) or Peter Wagner (info@prisonpolicy.org)
  - Fill same table with signal scores

- [ ] **9:40 AM**: Count STRONG signals and run routing decision

  **Domain 51 routing** (count your S signals from CLC / Issue One):
  - [ ] >= 2 STRONG: Activate all 5 Tier 2 contacts (Montana Plan, Michigan Clean Elections, New Mexico Common Cause, Issue One Advisory Board, OpenSecrets). **Send within 48 hours**. Use DOMAIN_51_WAVE_2_EMAIL_EXECUTION_PACKAGE.md. Jump to "Afternoon" section.
  - [ ] = 1 STRONG: Activate Issue One Advisory Board + OpenSecrets only. Hold remaining Tier 2 for June 30. Jump to "Afternoon" section.
  - [ ] 0 STRONG / >= 2 MODERATE: Activate Issue One Advisory Board only. Jump to "Afternoon" section. July 1 is hard deadline — prioritize CA contacts (Common Cause CA, LWV CA, Clean Money Action Fund) on June 30 regardless of signal.
  - [ ] 0 STRONG / 0-1 MODERATE: Run delivery diagnostic (Step 5 below).

  **Domain 48 routing** (count your S signals from Sentencing Project / Prison Policy Initiative):
  - [ ] >= 1 STRONG: Activate all Wave 2 contacts immediately (NAACP LDF, Fines and Fees Justice Center, ACLU of Virginia). **Send within 48 hours**. Use DOMAIN_48_EMAIL_TEMPLATE_SET.md. Jump to "Afternoon" section.
  - [ ] 0 STRONG / >= 1 MODERATE: Activate NAACP LDF only. Hold others until June 30. Jump to "Afternoon" section.
  - [ ] 0 STRONG / 0 MODERATE: If sends were < 72 hours old, re-check June 25. If sends were >= 72 hours old, run delivery diagnostic (Step 5 below).

- [ ] **9:50 AM (conditional)**: Delivery diagnostic — only if 0 STRONG / 0 MODERATE for either domain
  1. Load Gist URLs:
     - Domain 51: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
     - Domain 48: https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8
  2. Confirm HTTP 200 (page loads). If 404: recreate using contingency procedures (DOMAIN_51_CONTINGENCY_SB_299_FALLBACK.md or DOMAIN_48_GIST_CREATION_STEPS.md). Resend affected emails.
  3. Send test email to yourself from the same sending account. Confirm it reaches inbox, not spam.
  4. If delivery confirmed: Consider subject line improvement. Re-assess June 25.

**Afternoon (3:00–4:00 PM)**

- [ ] **3:00 PM**: Send Domain 51 Tier 2 emails (if routing triggered)
  - If Domain 51 routing activated >= 1 STRONG: Send Issue One Advisory Board email (DOMAIN_51_WAVE_2_EMAIL_EXECUTION_PACKAGE.md). If >= 2 STRONG, send all 5 Tier 2 emails.
  - Use template as-is; only fill [YOUR_NAME] and [YOUR_CONTACT_INFO] fields.
  - Log send in DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md.

- [ ] **3:15 PM**: Send Domain 48 Wave 2 emails (if routing triggered)
  - If Domain 48 routing activated >= 1 STRONG: Send NAACP LDF email (DOMAIN_48_EMAIL_TEMPLATE_SET.md). If >= 2 MODERATE, note that July 15 Virginia deadline justifies urgency flag even at MODERATE.
  - Log send in DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md.

- [ ] **3:30 PM**: Update DISTRIBUTION_EXECUTION_LOG.md with June 23 outcomes
  - Record: Which domains had Wave 1 sent, signal counts, routing decisions, any Tier 2 sends

---

## June 24 (Tuesday) — Domain 59 Wave 2 Forced Activation Decision

**Morning (9:00–11:00 AM)**

- [ ] **9:00 AM**: Check supremecourt.gov again (same case numbers as June 23)
  - If any opinions issued: follow CONTINGENCY ACTIVATION section below

- [ ] **9:05 AM**: Check Domain 59 inbox for replies since June 18
  - Look for: CBPP, MomsRising, AFL-CIO, ITEP, NWLC
  - Fill table:
    
    | Contact | New reply since June 18? | Signal (upgrade/same/new) | Notes |
    |---------|--------------------------|---------------------------|-------|
    | CBPP | [ ] | Prior: MODERATE | |
    | MomsRising | [ ] | Prior: MODERATE | |
    | AFL-CIO | [ ] | Prior: -- | |
    | ITEP | [ ] | Prior: -- | |
    | NWLC | [ ] | Prior: -- | |

- [ ] **9:15 AM**: Run Domain 59 Wave 2 forced activation decision
  - [ ] **If CBPP or MomsRising sent any additional communication since June 17** (even a follow-up question): Treat as upgrade to STRONG. Activate all 3 Wave 2 contacts (EPI, Demos, NELP) within 24 hours. Jump to "Send Wave 2" below.
  - [ ] **If any new STRONG signal from AFL-CIO, ITEP, or NWLC**: Same — activate all 3 Wave 2 contacts immediately.
  - [ ] **If signal remains at 2 MODERATE / 0 STRONG (expected scenario)**: Force Wave 2 activation regardless. Jump to "Send Wave 2" below.

- [ ] **9:30 AM (conditional)**: Senate Finance markup check
  - Visit: https://www.finance.senate.gov/imo/media/doc/Markup%20Schedule.pdf or check Senate Finance homepage
  - If Senate Finance is marking up OBBBA-related legislation June 24-25: This confirms forced activation decision. Proceed with Wave 2 sends.

- [ ] **9:40 AM**: Send EPI email (Domain 59 Wave 2)
  - **CRITICAL**: Verify EPI research director email address against epi.org staff directory (listed as "UNCONFIRMED" in prior session notes)
  - Address: researchdept@epi.org (verify before sending)
  - Template: DOMAIN_59_WAVE_2_EMAIL_EXECUTION_PACKAGE.md
  - Only fill: [YOUR_NAME] and [YOUR_CONTACT_INFO]
  - Log send in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md with note: "Forced Wave 2 activation June 24. Signal at T+15: 2 MODERATE (CBPP + MomsRising). 0 STRONG. Activation rationale: June 30 OBBBA midterm framing lock. EPI address verified [confirmed/unconfirmed]."

- [ ] **9:50 AM**: Send Demos email (Domain 59 Wave 2)
  - Address: info@demos.org
  - Template: DOMAIN_59_WAVE_2_EMAIL_EXECUTION_PACKAGE.md
  - Log send in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md

- [ ] **10:00 AM**: Hold NELP for July 7 send
  - Document in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md: "NELP (info@nelp.org) held as July 7 send (post-July 4 holiday, still within advocacy window)"
  - If Senate Finance markup activity accelerates, consider moving NELP send to June 27-30 window

**Afternoon (2:00–3:00 PM)**

- [ ] **2:00 PM**: Check for any new Domain 51 or Domain 48 replies from June 23 sends
  - Any new replies since your June 23 morning check? Update signal logs. If any upgrade to STRONG, re-run routing decisions.

- [ ] **2:10 PM**: Log Domain 59 Wave 2 decision in DISTRIBUTION_EXECUTION_LOG.md
  - Record: Prior signal status (June 17), current assessment (June 24), decision rationale, Wave 2 sends (EPI + Demos), NELP hold

---

## June 25 (Wednesday) — Final T+7 & Close-Out

**Morning (9:00–10:30 AM)**

- [ ] **9:00 AM**: Check supremecourt.gov one final time (same case numbers)
  - This is likely the last opinion day before summer recess announcement. If Little v. Hecox / BPJ has not issued by June 25, check daily thereafter through late June/early July.

- [ ] **9:10 AM**: Domain 48 final T+7 check (if Wave 1 was sent June 18)
  - If Wave 1 sent June 18, June 25 is Day 7. Check inbox for:
    - Brennan Center (if Wave 2 sent June 23)
    - Worth Rises (if Wave 2 sent June 23)
  - Fill signal table, update routing decision using June 23 decision tree

- [ ] **9:20 AM**: Confirm Domain 59 Wave 2 sends from June 24
  - Check sent folder:
    - [ ] EPI (researchdept@epi.org) — sent June 24
    - [ ] Demos (info@demos.org) — sent June 24
  - If not sent June 24: Send today. June 30 deadline is 5 days away.

- [ ] **9:30 AM**: Assess NELP send timing (default July 7)
  - Decision: July 7 (post-July 4 holiday) OR June 27-30 if Senate Finance markup accelerated
  - Check Senate Finance schedule again if unclear
  - Document decision in DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md

**Afternoon (3:00–4:00 PM)**

- [ ] **3:00 PM**: Final close-out log
  - Fill this summary table:
    
    | Domain | Wave 1 sent? | STRONG count at T+7 | MODERATE count at T+7 | Routing action taken | Next milestone |
    |--------|-------------|---------------------|-----------------------|---------------------|----------------|
    | Domain 51 | [ ] Yes / [ ] No | | | | July 1 CA deadline; Day 14 June 30 |
    | Domain 48 | [ ] Yes / [ ] No | | | | July 15 Virginia deadline; Day 14 June 30 |
    | Domain 59 | Wave 1 COMPLETE | 0 | 2 | Wave 2 forced activation June 24 | NELP July 7; Day 14 June 30 |

- [ ] **3:15 PM**: Update DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md and DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md with final June 23-25 outcomes

---

## Contingency Activation — Any Day (June 23-25 and Beyond)

### If Little v. Hecox or West Virginia v. B.P.J. Issued

**When**: The moment you see this decision on supremecourt.gov

**Timeline**: ~30 minutes total

**Action sequence**:
1. Verify decision at supremecourt.gov/opinions/slipopinion/25 (do NOT rely on news alerts)
2. Open DOMAIN_50_GIST_PREP.md (5-10 min to create Gist)
3. Copy Gist URL
4. Send Template A from DOMAIN_50_EMAIL_TEMPLATE_SET.md to:
   - Lambda Legal: info@lambdalegal.org — "Lambda Legal specifically" variant
   - ACLU LGBTQ+ Rights Project: (use aclu.org/contact; specify LGBTQ+ Rights Project)
   - HRC: hrc@hrc.org
5. Do NOT wait for August 1. Do NOT do anything else first.

**Post-ruling framing**: If Court upholds trans sports bans, lead with Kalarchik state constitutional strict scrutiny model (Montana, April 14, 2026) in Lambda Legal email.

**Log in CHECKIN.md**: Domain 50 immediate distribution triggered by [Case name] decision [date]

---

### If Trump v. Slaughter Issued (FTC / Independent Agencies)

**When**: Decision issued (expected before July 1)

**Action**: If Humphrey's Executor is overruled or substantially narrowed:
1. Add "June 2026 Update" note to Domain 51 Gist or append to distribution emails: "SCOTUS [date] ruling in Trump v. Slaughter: FEC structural independence now constitutionally uncertain. Cascade agencies include NLRB, MSPB, FEC, EEOC, FERC."
2. This strengthens the Domain 51 campaign finance argument.
3. Flag for Domain K research scope expansion (if scheduling Phase 3 work).
4. Log in CHECKIN.md: Domain 51 messaging updated based on Trump v. Slaughter [date]

---

### If Trump v. Barbara Issued (Birthright Citizenship)

**When**: Decision issued (expected before July 1)

**Verification**: Verify at supremecourt.gov/opinions/slipopinion/25 before executing (do NOT rely on news alerts; prior June 2 alert was false positive). Case number: 25-365.

**Action**: If ruling against government:
1. Open DOMAIN_58_TRUMP_V_BARBARA_RAPID_RESPONSE.md
2. Execute per protocol

**Log in CHECKIN.md**: Domain 58 rapid response executed following Trump v. Barbara [date]

---

## Signal Classification Quick Reference

*Use this for any reply you receive June 23-25*

| Signal | Score | Definition | Example |
|--------|-------|-----------|---------|
| **STRONG (S)** | 4-5 | Specific engagement action; decision-maker reply with substantive question or forwarding offer | "Can we set up a call to discuss?" or "I'm forwarding this to our research team who works on this directly" |
| **MODERATE (M)** | 3 | Receipt acknowledged + expressed interest; forwarded to team (no specific action); requested full document | "Thank you for sharing, this is very relevant to our work" or "I've sent this to our research director" |
| **WEAK (W)** | 1-2 | Auto-acknowledgment, form response, no individual name or content engagement | "We received your message" or "Thanks for contacting us" |
| **BOUNCE (B)** | 0 | Hard bounce or OOO — not a signal; requires action | Re-verify address and resend within 48 hours; log alternate if named |
| **No reply (--)**  | 0 | Normal at T+7 for cold outreach; not a failure signal | Check again on Day 14 (June 30) |

---

## Resources & Templates

- **T_PLUS_7_CHECKPOINT_MONITORING_FRAMEWORK.md** — Full signal rubric and routing logic (reference)
- **DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md** — CLC and Issue One Wave 1 templates
- **DOMAIN_51_WAVE_2_EMAIL_EXECUTION_PACKAGE.md** — Montana Plan, Michigan, New Mexico, Issue One Advisory Board, OpenSecrets
- **DOMAIN_48_EMAIL_TEMPLATE_SET.md** — All Wave 1-2 templates for Sentencing Project, PPI, Brennan Center, Worth Rises, etc.
- **DOMAIN_59_WAVE_2_EMAIL_EXECUTION_PACKAGE.md** — EPI, Demos, NELP templates (verified addresses)
- **DOMAIN_50_EMAIL_TEMPLATE_SET.md** — Lambda Legal, ACLU LGBTQ+, HRC (for contingency activation)
- **DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md** — Log all Domain 51 sends and signal data
- **DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md** — Log all Domain 48 sends and signal data
- **DOMAIN_59_DISTRIBUTION_EXECUTION_LOG.md** — Log all Domain 59 sends and signal data
- **DISTRIBUTION_EXECUTION_LOG.md** — Master log for all three domains

---

*Prepared June 22, 2026 (Session 3911). Print this page before June 23. Bookmark supremecourt.gov/opinions/slipopinion/25 and check it daily morning of June 23-25. All decision trees and templates staged and ready for use.*
