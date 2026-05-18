---
title: "Wave 1 Synthesis Framework Prep — May 21 Item 61 Staging Notes"
created: 2026-05-18
status: PREP — for use by May 21 10:30 UTC session agent
scope: "Pre-analysis for Item 61 synthesis: contingency path likelihood, synthesis deliverable structure, risks, recommended May 21 session actions"
monitoring_window: "May 18 10:32 UTC — May 21 10:30 UTC"
decision_gate: "May 21 14:00 UTC (user confirmation)"
primary_decision_doc: "WAVE_1_SYNTHESIS_FRAMEWORK.md (Item 61)"
companion_files:
  - WAVE_1_SYNTHESIS_FRAMEWORK.md
  - MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md
  - PHASE_2_OUTCOME_LAUNCH_ROADMAP.md
  - WAVE_1_MONITORING_DASHBOARD.md
  - DOMAIN_42_AMPLIFICATION_STRATEGY.md
---

# Wave 1 Synthesis Framework Prep — Item 61 Staging Notes

*Prepared: May 18, 2026 (post-send). For use by the May 21 10:30 UTC synthesis session.*

---

## 1. MONITORING STATUS AS OF MAY 18 20:00 UTC

**Monitoring window**: May 18 10:32 UTC — May 21 10:30 UTC (72 hours total)  
**Elapsed at this prep document's creation**: ~10 hours (first hours post-send)

### What Can Be Observed Right Now

The monitoring infrastructure is **manual** — the orchestrator has no direct inbox or Bitly access. The WAVE_1_MONITORING_DASHBOARD.md reflects a single agent pass at 09:09 UTC on May 18, during active send execution. Status at that pass: all 5 emails sent, no replies received (within expected norms), no anomalies detected.

**Observable signals at this stage (without inbox access)**:
- No delivery failure reports in WORKLOG.md or ORCHESTRATOR_STATE.md
- No bounce notifications flagged in CHECKIN.md
- WAVE_1_COMPLETION_CHECKLIST.md records 5/5 sends complete
- ORCHESTRATOR_STATE.md confirms monitoring window is ACTIVE

**What cannot be observed without user inbox + Bitly access**:
- Reply count and quality scores
- Hard bounces or soft bounces
- OOO autoreplies (Weiser/Bassin/Elias are in their primary window)
- Gist view delta

**Early signal confidence**: LOW at this stage — 10 hours is too early for any policy org contact. The earliest possible substantive reply would be from Marc Elias (fastest expected responder, 48-hour cycle), meaning the first actionable signal arrives May 19 08:00–10:00 UTC at the earliest.

**Monitoring WAVE_1_MONITORING_LOG.md**: This file did not exist prior to this prep session. Recommend creating it as a running daily log during the monitoring window, distinct from the structured dashboard. The dashboard (WAVE_1_MONITORING_DASHBOARD.md) has pre-populated update blocks for each day — the log would capture ad-hoc signals, provisional assessments, and day-by-day notes.

---

## 2. CONTINGENCY PATH LIKELIHOOD ASSESSMENT

This is a base-rate analysis using sector norms, framing alignment, and contact characteristics — not actual observed data.

### Most Likely Classification at May 21 10:30 UTC: MODERATE

**Reasoning**:

The three contacts in their primary window (Weiser, Bassin, Elias) have these characteristics:

| Contact | Sector | Expected Cycle | Framing Alignment | Likelihood of Score 3+ Reply by 72h |
|---------|--------|---------------|-------------------|--------------------------------------|
| Marc Elias | Litigation | 48h | HIGH — Callais cascade is directly relevant to Democracy Docket docket | ~30-40% |
| Wendy Weiser | Policy Org | 2-5 days | HIGH — Domain 1/37 SAVE Act framing is core Brennan Center terrain | ~15-20% at 72h (full reply likely by Day 5) |
| Ian Bassin | Policy Org | 2-5 days | HIGH — implementation/constitutional focus matches Protect Democracy mission | ~15-20% at 72h |

**Combined probability estimate for at least 1 substantive reply within 72h**: ~50-60%

**Combined probability estimate for 2+ substantive replies within 72h**: ~20-30%

The MODERATE classification (30-59% reply rate = 1 of 3 adjusted contacts) is the most probable outcome at the 72-hour gate, driven by the expectation that Elias or one of the two policy org contacts produces a Score 3+ reply.

STRONG (60%+ rate = 2+ of 3 adjusted contacts at Score 3+) requires both Elias AND one of Weiser/Bassin to respond substantively within 72h. Possible, but this requires two independent fast responders hitting within the same tight window — lower probability (~15-25%).

WEAK (<30% = 0 of 3 adjusted contacts) requires all three policy org and litigation contacts to be silent at 72 hours. Given the strength of domain alignment and framing specificity, this outcome most likely indicates a delivery problem, not a content failure. Delivery check (WAVE_1_SYNTHESIS_FRAMEWORK.md Section 3.3) is mandatory before confirming WEAK.

### Who Replies First (Fastest to Slowest Projection)

1. **Marc Elias (Democracy Docket)** — fastest. The Callais cascade framing and Watson v. RNC relevance is operationally time-sensitive for his team. If any reply arrives before May 20 09:00 UTC, it is almost certainly Elias.

2. **Ian Bassin (Protect Democracy)** — second fastest. Protect Democracy is a litigation organization; their staff have faster document-review cycles than academic institutions. The implementation/constitutional focus of the Batch 1 email aligns directly with their current active work.

3. **Wendy Weiser (Brennan Center)** — third. Brennan Center has institutional review layers. Weiser's role as VP of Democracy Program means her outbound reply rate may be filtered through staff. A reply by Day 5 (May 23) is most probable.

4. **Ryan Goodman (Just Security / NYU Law)** — fourth. Academic and editorial cycle. 5-10 days is the sector norm. Any reply before May 25 is a positive early signal.

5. **Erica Chenoweth (Harvard Kennedy School)** — slowest. End-of-semester academic calendar. Response cycle may extend to May 28 (Day 10) or beyond.

### Special Notes

- **If Elias does NOT reply by May 21 10:30 UTC**: This is a moderate negative signal for the litigation framing specifically, but does NOT indicate WEAK for the overall classification. The Domain 37/Callais framing may be operationally useful to Elias but arrive at a busy litigation moment. Do not over-index on Elias silence.

- **If a law school contact (Goodman or Chenoweth) replies before May 21**: This is an anomaly-level positive signal. Early academic replies indicate high domain salience — score normally and adjust institutional rate calculation to include all responding contacts.

- **OOO risk**: If Bassin or Weiser are OOO through the 72-hour window (conference travel, late-semester), the adjusted contact count drops to 2 (Elias + 1 remaining), making STRONG mathematically harder. Watch for OOO notifications May 18-19.

---

## 3. BATCH 2 CONTACTS THAT SHOULD BE PREPPED/RESEARCHED NOW

These contacts are best positioned to move from prep to execution on May 21, and some pre-work can reduce friction at the May 21 launch window.

### Priority Group 1 — Pre-Prep Justified Now (Regardless of Outcome)

**Marc Elias / Democracy Docket (if he replies with a specific case reference)**  
If Elias's reply names a case or docket number, Batch 2 pre-contact should identify 2-3 Democracy Docket staff researchers to receive the Domain 37 Section 3 extract formatted for litigation support. Checking the Democracy Docket docket page (democracydocket.com) before May 21 for any new Watson v. RNC or Callais-related filings would allow the May 21 session to personalize Batch 2 immigration legal aid emails with current case references.

**Richard Hasen (UCLA Law)** — designated "fastest academic responder" in the framework. His Batch 2 email (Domain 1/33/37) requires minimal customization. Pre-drafting the subject line referencing his most recent Election Law Blog post (check electionlawblog.org before May 21) would sharpen the hook.

**Nicholas Stephanopoulos (Harvard Law School)** — election law expert; Batch 2 Priority Group 1. His recent work on the efficiency gap connects directly to Domain 1. Pre-identifying his most recent publication (SSRN or Harvard Law Review search) before May 21 allows immediate subject line customization under Strong.

**Olatunde Johnson and Gillian Metzger (Columbia Law)** — both on the May 21 Moderate path send list. Their contact emails are pre-verified. The only prep needed is confirming their emails are still current at Columbia's law faculty directory — a 5-minute task.

### Priority Group 2 — Domain Hook Research for Batch 2-3

**Think tank contacts (Brookings, Roosevelt, EPI)** — the think tank Tier 2 email templates require confirming which specific researchers are currently active. Before May 21, spot-check Brookings Governance Studies (Molly Reynolds is listed in the coordination framework — verify current affiliation), Roosevelt Institute, and EPI staff pages. Personnel turnover in think tanks is common; emails sent to departed researchers bounce.

**Domain 42 Sub-Batch Follow-Up (May 20-21)** — the Domain 42 sub-batch (Drug Policy Alliance, NORML, ACLU Criminal Law Reform, Sentencing Project, LEAP) was supposed to send by May 21 per BATCH_1_CONTACT_LOG.md. The follow-up protocol (Day 7-10 post-send, May 20-23) is entering its window. Regardless of overall Wave 1 classification, the Domain 42 state AG sub-batch (5 state AGs: Mayes/Arizona, Bonta/California, Phil Weiser/Colorado, Nessel/Michigan, Brown/Washington) sends May 21 under ALL classification paths. The AG contact portal links need a live-check before May 21 send:
  - azag.gov contact form
  - oag.ca.gov contact form
  - coag.gov contact form
  - michigan.gov/ag
  - atg.wa.gov

---

## 4. MAY 21 ITEM 61 SYNTHESIS DELIVERABLES — DRAFT STRUCTURE

The May 21 session (10:30-14:00 UTC) produces one primary output: the confirmed classification and activated path, logged in CHECKIN.md and WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv.

### Required Deliverables at the May 21 Session

**1. Signal Classification Record** (fill in WAVE_1_SYNTHESIS_FRAMEWORK.md Section 3.5 template)
- Hard bounce count
- OOO count
- Adjusted contact count (5 − bounces − OOOs)
- Substantive replies (Score 3+)
- Integration signals (Score 4-5)
- Institutional reply rate
- Gist delta
- Law school window status
- Final classification: STRONG / MODERATE / WEAK

**2. Batch 2-3 Path Activation**
Per classification:
- STRONG: Queue ~20 sends, Priority Groups 1-2 + Domain 42 state AGs. Use social proof framing. Phase 2 research authorization flag for user at 14:00.
- MODERATE: Queue ~10 sends today (Priority Group 1 + Domain 42 AGs). Use policy urgency framing. Phase 2 standard timeline flag for user.
- WEAK: HOLD Batch 2. Send Domain 42 AGs only. Post-mortem protocol initiated. Flag "Needs Your Input" in CHECKIN.md.

**3. Domain 42 Sends (Path-Independent)**
5 state AG contacts send regardless of classification (May 28 DEA deadline is 7 days from May 21). Template source: DOMAIN_42_AMPLIFICATION_STRATEGY.md. Use urgency framing only — do not bundle with broader research framework under WEAK.

**4. CHECKIN.md Update**
Classification result, path recommendation, Phase 2 start date recommendation, and "awaiting 14:00 UTC user confirmation" note.

**5. Phase 2 Research Authorization Request (for user at 14:00)**
Frame the 14:00 gate clearly:
- STRONG: "Approve Domain 57 + Domain 59 research beginning May 25? Yes/No."
- MODERATE: "Approve Domain 39 pre-distribution package (3 hours, June 1 anchor) + Domain 57 beginning June 8? Yes/No."
- WEAK: "Domain 37 supplement + Domain 39 no later than June 8 are non-negotiable. Approve post-mortem review before any Batch 2 send? Yes/No."

### Signal Classification Thresholds (Quick Reference)

Current framework thresholds (from WAVE_1_SYNTHESIS_FRAMEWORK.md Section 3.1):

| Outcome | Institutional Reply Rate | Integration Signals (Score 4-5) | Override |
|---------|-------------------------|--------------------------------|---------|
| STRONG | ≥60% (3 of adjusted) | ≥3 by May 21 10:30 UTC | Any Score 5 = STRONG regardless |
| MODERATE | 30-59% OR 1-2 integration signals | 1-2 (either/or with rate) | None |
| WEAK | <30% AND 0 integration signals | 0 | None — run delivery check first |

**Critical adjustment**: The adjusted contact count at 72h is 3, not 5 — law school contacts (Goodman, Chenoweth) are in secondary window through May 28. STRONG = 2 of 3 policy/litigation contacts at Score 3+. MODERATE = 1 of 3. WEAK = 0 of 3.

### Path Decision Matrices — Domain Activation by Classification

| Domain | STRONG | MODERATE | WEAK |
|--------|--------|----------|------|
| Domain 56 (Civil Service) | Distribute May 28 | Distribute May 28 | Distribute May 28 |
| Domain 39 (Healthcare) | Pre-distribution package by June 1 | Pre-distribution package by June 1 | Pre-distribution package — no later than June 8 |
| Domain 58 (Tribal Sovereignty) | Distribute by June 15 | Distribute by June 15 | Distribute by June 15 |
| Domain 57 (Multilateral Withdrawal) | Research begins May 25 | Research begins June 8 | Research begins August 1 |
| Domain 59 (Economic Precarity) | Research begins May 25 (parallel with D57) | Research begins July 1 | Research begins July 15 |
| Domain 38 (AI Regulatory Capture) | Production June 8 | Production July 1 | Immediate — production by June 30 |
| Domain 40 (Surveillance Capitalism) | Production Q3 | Production July 1 | Production June 22 |
| Domains 41-43 | Hold — scope Week 5+ only | Hold | Hold indefinitely |

Note: Under WEAK, D38 and D40 are ACCELERATED (fast-turn external deadlines create independent audience activation). Under STRONG, they are deferred because D57/D59 consume research bandwidth.

### Batch 2-3 Activation Timing Per Classification

| Classification | Batch 2 First Send | Batch 2 Framing | Batch 3 Gate |
|---------------|-------------------|-----------------|-------------|
| STRONG | May 21 (today) | Social proof — name institution, describe engagement type | May 24 (no gate needed) |
| MODERATE | May 21-22 (standard) | Policy urgency — June 1 HHS, August 10 UNGA 81, November 3 | June 1-3 (Batch 2 Day 5 signal check) |
| WEAK | June 1 minimum (post-mortem) | Domain utility only — no social proof | No Batch 3 until Batch 2 ≥1 quality reply |

---

## 5. RISKS AND EARLY ADJUSTMENTS

### Risk 1: Domain 56 May 28 Distribution Timing Conflict

Domain 56 is supposed to distribute May 28. Domain 42 DEA deadline is also May 28. Under STRONG, the May 21 session also launches Batch 2 and begins Domain 57 pre-production. May 28 will be a high-activity day. Risk: Domain 56 distribution execution is crowded out.

**Mitigation**: Domain 56 distribution prep (DOMAIN_56_EXECUTION_CHECKLIST.md) should be completed in the Week 1 May 18-24 window, so May 28 execution is mechanical only. The May 21 session should flag Domain 56 as a "pre-complete before May 26" task.

### Risk 2: Domain 42 Sub-Batch Status Unclear

The BATCH_1_CONTACT_LOG.md shows Domain 42 sub-batch (DPA, NORML, ACLU, Sentencing Project, LEAP) with status "DRAFTED — ready to send" with send dates listed as "—" (not yet sent). It is unclear from available files whether these 5 organizations received their Domain 42 emails before May 21. If they have NOT been sent yet, May 21 is the hard deadline — the domain 42 participation notice emails must reach organizations by May 22 to allow adequate preparation before the May 28 DEA deadline.

**Action required at May 21 session**: Confirm whether Domain 42 sub-batch (DPA, NORML, ACLU, Sentencing Project, LEAP) emails were sent. If not, send them today, May 21, before any other Batch 2 work.

### Risk 3: State AG Domain 42 Contact Portals May Require User Navigation

The 5 state AG contacts (Mayes/AZ, Bonta/CA, Phil Weiser/CO, Nessel/MI, Brown/WA) use web contact portals, not direct email addresses. These portals often have character limits, form fields, and CAPTCHA — making them more time-intensive than a standard email send. Under STRONG, the May 21 session is already handling ~20 Batch 2 sends; adding 5 portal submissions may exceed available session time.

**Mitigation**: Prioritize Domain 42 state AG portal sends FIRST on May 21, before any Batch 2 sends, since their deadline is hard. Allow 30-45 minutes for 5 portal submissions.

### Risk 4: Law School Secondary Window Ends May 28 — Coincides With D56 Distribution

Goodman (NYU) and Chenoweth (Harvard Kennedy) have their secondary classification window through May 28. If either replies May 21-25 with Score 4-5, the classification upgrades from MODERATE to STRONG and the Phase 2 research timeline accelerates. This upgrade can be handled at the May 25 secondary gate — but if a Score 5 signal arrives between May 21 and May 25 (e.g., Goodman mentions the framework in a Just Security editorial piece), STRONG override activates immediately without waiting for May 25.

**Mitigation**: Monitor inbox between May 21 and May 25 for any law school signals. If Score 5 signal arrives, flag immediately in CHECKIN.md and upgrade Phase 2 timeline.

### Risk 5: OBBBA / HHS Interim Rule Pre-Emption

The HHS interim final rule on Medicaid work requirements is expected June 1 without notice-and-comment. If there is any early release of rule text before June 1, Domain 39 should be pre-distributed immediately — this is a policy window pre-emption event (PHASE_2_OUTCOME_LAUNCH_ROADMAP.md Section 6.4). This risk is low before May 21 but worth noting as a contingency.

### Risk 6: May 28 DEA Deadline Is 7 Days From May 21 — Hard Stop

The DEA-1362 participation notice deadline is May 28. Organizations receiving Domain 42 materials need materials by May 22 to have 6 days to draft and file notices. If the Domain 42 sub-batch organizations (DPA, NORML, etc.) have NOT yet received their emails, May 21 is effectively the last viable send date. This is the most time-critical task of the May 21 session.

**Assessment**: At the time of this prep document (May 18), the sub-batch appears unsent per BATCH_1_CONTACT_LOG.md. If confirmed unsent at May 21, these sends must execute before any other work.

---

## 6. IS DOMAIN 42 DEA HEARING (MAY 28) STILL ON TRACK?

**Status**: Uncertain — requires confirmation that either (a) sub-batch emails were already sent in the May 14-20 window, or (b) they execute on May 21.

**Current known state from available files**:
- Domain 42 research: COMPLETE (6,860 words, 54 citations, last updated April 2026)
- Email templates: 5 emails drafted and ready (in `execution/DOMAIN_42_WAVE_1_EMAIL_PACKAGE.md` per BATCH_1_CONTACT_LOG.md)
- Gist URL: Pre-verified (`https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab` — spot-check this URL before sending)
- Sub-batch status: "DRAFTED — ready to send" as of May 13, send dates blank

**State AG sub-batch** (Mayes/AZ, Bonta/CA, Phil Weiser/CO, Nessel/MI, Brown/WA): Listed in WAVE_1_SYNTHESIS_FRAMEWORK.md Appendix B as "path-independent — send today regardless of classification" on May 21. These are separate from the DPA/NORML/ACLU sub-batch.

**Conclusion**: Domain 42 May 28 deadline is ACHIEVABLE if sub-batch sends execute May 21. Risk is MODERATE (time pressure but not yet critical failure). May 21 session must confirm sub-batch send status and execute if not yet done.

---

## 7. NEXT AUTONOMOUS WORK RECOMMENDATION FOR MAY 21 ITEM 61 SESSION

### Pre-Session (Before 10:30 UTC)

The orchestrator cannot act on inbox or Bitly data — the user needs to populate WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv before the 10:30 UTC gate. Prompt:

> "Before 10:30 UTC: Check your email inbox and log any replies, bounces, or OOO notifications in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv. Check your Bitly dashboard for Gist view delta since May 18 baseline. WAVE_1_SYNTHESIS_FRAMEWORK.md Section 2.1 is the data collection table."

### 10:30-11:15 UTC Session Actions (Orchestrator-Executable)

1. **Read user-provided signal data** from WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv
2. **Run Section 3.2 decision table** — identify classification
3. **Apply law school silence adjustment** — explicitly note Goodman/Chenoweth silence is within sector norms if neither has replied
4. **Complete Section 3.5 classification record** — fill all fields
5. **Log classification** in WAVE_1_ENGAGEMENT_SCORING_CALCULATOR.csv row 61
6. **Update CHECKIN.md** — classification result, path activated, 14:00 user gate flag

### 11:00-13:30 UTC Session Actions (User-Executable, Orchestrator-Staged)

1. **Confirm Domain 42 sub-batch status** — have DPA/NORML/ACLU/Sentencing Project/LEAP received their emails? If not, execute now.
2. **Execute Domain 42 state AG sends** (5 contacts, portal submissions — allow 30-45 min)
3. **Queue appropriate Batch 2 sends** per classification:
   - STRONG: Pull Priority Group 1 from MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md Section 3A
   - MODERATE: Pull Priority Group 1 from Section 3B
   - WEAK: Hold — do NOT send Batch 2
4. **Personalize templates** — fill [PROPOSAL_URL], [YOUR NAME], all placeholders before any send
5. **Stagger sends 30 minutes apart**

### 14:00 UTC User Gate

The session should surface exactly these three questions for user decision:

**Q1 — Classification confirmed?**  
"Wave 1 classification: [STRONG / MODERATE / WEAK]. Reply rate: X%. Integration signals: N. Law school window: still open through May 28. Recommend proceeding on [path]."

**Q2 — Phase 2 research authorization:**
- STRONG: "Approve Domain 57 + Domain 59 beginning May 25?"
- MODERATE: "Approve Domain 39 pre-distribution (June 1) + Domain 57 beginning June 8?"
- WEAK: "Domain 39 by June 8 is non-negotiable. Approve post-mortem first?"

**Q3 — Domain 42 confirmed active:**
"Domain 42 state AG sends: [executed / pending]. Sub-batch (DPA/NORML/ACLU/Sentencing Project/LEAP): [sent / not yet sent — execute now]."

### May 25 Secondary Gate

The Item 61 session does NOT close the loop — the May 25 secondary gate is where law school signals (Goodman, Chenoweth) are incorporated, the classification is finalized, and Phase 2 research officially begins. The May 21 session prepares and stages; the May 25 session authorizes.

Key May 25 tasks (from WAVE_1_SYNTHESIS_FRAMEWORK.md Section 8):
- Re-populate Section 2.1 with any new signals received May 21-25
- Re-run Section 3.2 decision table with full 7-day data
- Upgrade classification if law school signals arrive
- Run 12-item May 25 checklist in WAVE_1_SYNTHESIS_AND_PHASE_2_DECISION_FRAMEWORK.md Section 5
- Get user approval for Phase 2 research start

---

## 8. SUMMARY TABLE

| Question | Current Answer |
|---------|---------------|
| Early signals observed so far? | None observable — inbox/Bitly not accessible to agent; Day 1 is too early for any reply |
| Most likely classification at May 21? | MODERATE (probability ~50-60%) |
| Most likely to reply first? | Marc Elias (Democracy Docket) — litigation urgency, 48h cycle |
| Domain 42 May 28 deadline on track? | UNCERTAIN — sub-batch status unclear; must confirm and send May 21 if not yet executed |
| D56 May 28 distribution on track? | YES — research complete; execution checklist prep needed this week |
| Batch 2 contacts to prep now? | Stephanopoulos, Hasen (law school), domain 42 sub-batch confirmation, state AG portal spot-check |
| Biggest risk? | Domain 42 sub-batch unsent; must execute May 21 before any other work |
| May 21 session priority order? | (1) Signal collection + classification, (2) Domain 42 sub-batch if unsent, (3) Domain 42 state AG portal sends, (4) Batch 2 queue per classification, (5) Phase 2 authorization at 14:00 |

---

*Prepared May 18, 2026 (post-send monitoring session). Sources: WAVE_1_SYNTHESIS_FRAMEWORK.md (Item 61), MAY_21_31_BATCH_2_3_COORDINATION_FRAMEWORK.md, PHASE_2_OUTCOME_LAUNCH_ROADMAP.md, BATCH_1_CONTACT_LOG.md, DOMAIN_42_MAY_28_EXECUTION_PREP.md, WAVE_1_MONITORING_DASHBOARD.md, ORCHESTRATOR_STATE.md.*
