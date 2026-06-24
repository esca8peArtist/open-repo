---
title: "Domains 51/48 — Wave 1 Response Tracking Template"
created: "2026-06-24"
status: "ACTIVE — fill daily beginning day of first send"
scope: "Domain 51 (Campaign Finance — 4 Tier 1 sends) + Domain 48 (Criminal Justice — 5 Tier 1 sends). Total: 9 sends."
baselines:
  open_rate_target: ">40% (prior SCOTUS rapid-response performance baseline)"
  click_rate_target: ">15% (prior SCOTUS rapid-response performance baseline)"
  reply_rate_minimum_threshold: "≥20% by Day 7 to authorize Wave 2 with current templates"
wave_2_trigger_conditions:
  green: "≥40% reply rate — Wave 2 launches current templates, July 1–2"
  yellow: "20–39% reply rate — Wave 2 launches with minor refinement, July 1–3"
  red: "<20% reply rate — Wave 2 held; template revision before launch, July 7+"
  hard_override: "Virginia July 15 — Domain 48 Wave 2 Virginia contacts (Sends 3, 6, 7) launch regardless of Wave 1 rate if July 7 is reached without activation"
---

# Domains 51/48 — Wave 1 Response Tracking Template
## Daily Monitoring June 24 – July 7, 2026

*Fill one row per day. Three-minute check-in format. All thresholds are numeric and time-anchored — no subjective assessment required.*

---

## SEND LOG — Complete Before Daily Tracking Begins

Fill these fields once, on the day each send occurs. Do not leave blank — log "NOT SENT" if not sent.

### Domain 51 Sends (Campaign Finance)

| Send # | Organization | Email | Send Date (UTC) | Send Time (UTC) | Bounced? | Gist URL Live at Send? |
|--------|---|---|---|---|---|---|
| D51-1 | Campaign Legal Center — Erin Chlopak | echlopak@campaignlegalcenter.org | | | | |
| D51-2 | Issue One | info@issueone.org | | | | |
| D51-3 | Common Cause California — Darius Kemp | dkemp@commoncause.org | | | | |
| D51-4 | Clean Money Action Fund | info@CAclean.org | | | | |

**Gist URL (Domain 51)**: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372

### Domain 48 Sends (Criminal Justice)

| Send # | Organization | Email | Send Date (UTC) | Send Time (UTC) | Bounced? | Gist URL Live at Send? |
|--------|---|---|---|---|---|---|
| D48-1 | Sentencing Project — Nicole Porter | nporter@sentencingproject.org | | | | |
| D48-2 | Prison Policy Initiative | info@prisonpolicy.org | | | | |
| D48-3 | Brennan Center — Sean Morales-Doyle | [web form] | | | | |
| D48-4 | Worth Rises — Bianca Tylek | info@worthrises.org | | | | |
| D48-5 | Movement for Black Lives | info@m4bl.org | | | | |

**Gist URL (Domain 48)**: https://gist.github.com/esca8peArtist/00c1423e3da7bb4693fa285ec87f18a8

**Note on CLC Restore Your Vote (Blair Bowie)**: Listed in DOMAIN_48_EMAIL_TEMPLATE_SET.md Wave 2, June 19. If that send has NOT occurred, add as D48-6 in the log above and in daily tracking below.

---

## REPLY LOG — Fill as Replies Arrive

| # | Reply Date (UTC) | From Org | From Email | Signal Level | Summary (1 sentence) | Action Taken |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |

**Signal level definitions**:
- STRONG: Named staff reply with substantive engagement (question, request, mention of sharing internally)
- MODERATE: Auto-acknowledgment or reply with named contact but no substantive engagement
- WEAK: Generic form response with no named contact; "unsubscribe" request
- NONE: No reply (default at Day 14 if nothing received)

---

## DAILY TRACKING — June 24 to July 7

### Day 1 — June 24, 2026

**First send date**: _________ (UTC)
**Sends completed today**: _____ / 9 total
**Domain 51 sends today**: _____ / 4 (D51-_ through D51-_)
**Domain 48 sends today**: _____ / 5 (D48-_ through D48-_)
**Gist D51 live**: [ ] Yes [ ] No
**Gist D48 live**: [ ] Yes [ ] No
**Bounces**: ___________________
**Replies received**: _____
**Day 1 status**: [ ] GREEN (any sends started) [ ] YELLOW (0 sends, ETA known) [ ] RED (0 sends, no ETA)

**June 24 Escalation Gate**:
- 18:00 UTC, 0 sends → Add to CHECKIN.md: "Domain 51/48 Wave 1 zero sends confirmed June 24 18:00 UTC — user ETA needed"

---

### Day 2 — June 25, 2026

**Running send total**: _____ / 9
**Domain 51**: _____ / 4 | **Domain 48**: _____ / 5
**Replies received (cumulative)**: _____
**Reply rate**: _____ / _____ sent = _____%

**June 25 Escalation Gate** (CRITICAL):
- 12:00 UTC, 0 sends → Execute BLOCKED.md entry (see DOMAINS_51_48_ESCALATION_THRESHOLDS.md Section A.1)
- 12:00 UTC → Flag Domain 59 Tier 2 as available independently (not gated on this)
- Status: [ ] GREEN [ ] YELLOW [ ] RED

---

### Day 3 — June 26, 2026

**Running send total**: _____ / 9
**Domain 51**: _____ / 4 | **Domain 48**: _____ / 5
**Replies received (cumulative)**: _____
**Reply rate (48h)**: _____ / _____ sent = _____%
**Response quality**: STRONG: ___  MODERATE: ___ WEAK: ___

**48h rate assessment** (apply only if ≥ 3 sends out):
- ≥ 20%: Normal — continue monitoring. No template change.
- < 20%: Early flag — continue to Day 4 before revision decision. Do not revise yet.

**Status**: [ ] GREEN [ ] YELLOW [ ] RED

---

### Day 4 — June 27, 2026 — FIRST THRESHOLD DAY

**Running send total**: _____ / 9
**Domain 51 reply rate (72–96h)**: _____ / _____ sent = _____%
**Domain 48 reply rate (72–96h)**: _____ / _____ sent = _____%
**Combined reply rate**: _____ / _____ sent = _____%
**Response quality**: STRONG: ___  MODERATE: ___ WEAK: ___

**June 27 Rate Threshold Decision** (first meaningful threshold):

| Combined Rate | Decision | Action |
|---|---|---|
| < 20% | REVISE before Wave 2 | Log: "Template revision scheduled [DATE/TIME]" |
| 20–39% | REFINE — minor edit | Log: "Template refinement scheduled [DATE/TIME]" |
| 40–59% | PROCEED as-is | Log: "Wave 2 authorized. Templates current. Target: July 1–2." |
| > 60% | ACCELERATE | Log: "Wave 2 expanded 20+ Tier B contacts. Target: June 29–30." |

**June 27 Decision logged**: _________________________________
**Wave 2 status after this decision**: _________________________________

**June 27 HARD DEADLINE CHECK — Domain 51 DISCLOSE Act**:
If the Senate Finance Committee markup on the DISCLOSE Act is scheduled for July 1 or earlier, accelerate any remaining Domain 51 sends immediately. Do not wait for T+7 checkpoint.
- Senate markup status: _________________________________

**Status**: [ ] GREEN [ ] YELLOW [ ] RED (wave 2 held for revision)

---

### Day 5 — June 28, 2026 — WAVE 2 PLANNING DAY

**All Wave 1 sends complete?**: [ ] Yes (9/9) [ ] No — remaining: _______
**Domain 51 reply rate**: _____ / 4 = _____%
**Domain 48 reply rate**: _____ / 5 = _____%

**Wave 2 Decision (confirm based on Day 4 threshold)**:
- [ ] REVISE templates — 1–2h revision scheduled: _______. Wave 2 launch: July 7
- [ ] REFINE templates — 30–45 min revision scheduled: _______. Wave 2 launch: July 1–2
- [ ] PROCEED as-is — Wave 2 launch authorized: _______. Templates: current
- [ ] ACCELERATE — Wave 2 expanded. Launch: _______. Additional contacts: _______

**Virginia override check**: Have any of Domain 48 Tier 2 Virginia contacts (Virginia Organizing, Progress Virginia, Virginia Interfaith Center — DOMAIN_48_WAVE_2_SEND_TEMPLATES.md Templates 3, 6, 7) been sent? If not sent AND combined rate < 40%: activate Virginia fast-track regardless. Virginia July 15 deadline overrides rate-based Wave 2 hold.

**Virginia override status**: [ ] Not applicable (VA contacts sent) [ ] Activated (rate hold overridden for VA contacts) [ ] N/A (rate ≥ 40%)

**Status**: [ ] GREEN (Wave 2 authorized) [ ] YELLOW (Wave 2 delayed but scheduled) [ ] RED (revision needed, Wave 2 held)

---

### Day 6 — June 29, 2026

**Remaining Wave 1 sends**: _____ (send today if any remain — last viable date for "rapid response" framing)
**Cumulative reply rate**: _____ / 9 = _____%
**Domain 59 Tier 2 status** (independent): EPI: _____ | Demos: _____ | NELP: _____
**Wave 2 preparation status**: _________________________________
**Status**: [ ] GREEN [ ] YELLOW [ ] RED

---

### Day 7 — June 30, 2026

**Final Wave 1 send count**: Domain 51: _____ / 4 | Domain 48: _____ / 5 | Total: _____ / 9
**7-day reply rate**: Domain 51: _____ / 4 = _____% | Domain 48: _____ / 5 = _____%
**Domain 59 Tier 2 complete?**: [ ] Yes (3/3) [ ] No — remaining: _______

**Wave 2 launch status**:
- Templates ready (revised/refined/current): [ ] Yes [ ] No
- Launch date confirmed: _______
- Contact expansion decision: _______

**July follow-up calendar** (fill in):
- [ ] Mark July 7: Domain 48 — M4BL and Fair Elections Center follow-up if no reply. Phone contact required for Virginia July 15 deadline. M4BL: info@m4bl.org. Fair Elections Center: fairelectionscenter.org/contact
- [ ] Mark July 10: Domain 51 — If CLC or Common Cause CA have not replied, escalate to: Sean McElwee (smcelwee@campaignlegalcenter.org) and Ben Barber (bbarber@commoncause.org) per DOMAINS_51_48_ESCALATION_THRESHOLDS.md
- [ ] Mark July 14: Domain 48 Wave 2 launch for non-Virginia Tier 2 contacts (FRRC, National Reentry Network, Legal Action Center, CSSNY) if launch delayed beyond July 7

**June 30 Closure Status**:

| Domain | Sends | Reply Rate | Threshold Crossed | Wave 2 Ready | Notes |
|--------|-------|-----------|-------------------|--------------|-------|
| Domain 51 | ___/4 | ___% | [ ] <20% [ ] 20-39% [ ] 40-59% [ ] >60% | [ ] Yes [ ] No | |
| Domain 48 | ___/5 | ___% | [ ] <20% [ ] 20-39% [ ] 40-59% [ ] >60% | [ ] Yes [ ] No | |
| Domain 59 T2 | ___/3 | N/A | N/A | N/A | |

**Overall June status**: [ ] GREEN (all Wave 1 complete, rate ≥ 20%, Wave 2 authorized) [ ] YELLOW (partial, scheduled) [ ] RED (significant slippage — July async path)

---

## WEEKS 2–3 TRACKING — July 1–14, 2026

### T+7 Checkpoint (7 days after first send date)

**First send date was**: _______. T+7 date: _______.

**T+7 rate assessment**:
- Domain 51 total replies by T+7: _____ / 4 = _____%
- Domain 48 total replies by T+7: _____ / 5 = _____%
- Composite T+7 rate: _____ / 9 = _____%

**T+7 composite rate decision table**:

| Rate | Wave 2 Decision | Template Status | Timeline |
|---|---|---|---|
| < 20% | REVISE + RE-TEST | Revise Domain 51 and 48 templates independently. Test 1 contact each before full Wave 2. | Revision: July 1–3. Re-test: July 7. Wave 2: July 14 if re-test succeeds. |
| 20–39% | REFINE + PROCEED | Adopt framing from any replies that worked. Minor edit — 30–45 min. | Wave 2 launch: July 1–2. |
| 40–59% | PROCEED AS-IS | Templates proven. | Wave 2 launch: July 1–2. |
| > 60% | ACCELERATE | Add 20+ Tier B contacts per domain. | Wave 2 launch: June 29–30 (already past — launch immediately). |

**T+7 Decision**: _________________________________
**T+7 Wave 2 authorization date**: _________________________________

---

### T+14 Checkpoint (14 days after first send date)

**T+14 date**: _______

**Final Wave 1 reply rate**:
- Domain 51: _____ / 4 = _____%
- Domain 48: _____ / 5 = _____%

**Contacts with no reply by T+14** (mark NO RESPONSE, do not follow up unless specific escalation triggered):

| Send | Org | Reply Status |
|------|-----|-------------|
| D51-1 | CLC | [ ] Replied [ ] NO RESPONSE |
| D51-2 | Issue One | [ ] Replied [ ] NO RESPONSE |
| D51-3 | Common Cause CA | [ ] Replied [ ] NO RESPONSE |
| D51-4 | Clean Money Action Fund | [ ] Replied [ ] NO RESPONSE |
| D48-1 | Sentencing Project | [ ] Replied [ ] NO RESPONSE |
| D48-2 | Prison Policy Initiative | [ ] Replied [ ] NO RESPONSE |
| D48-3 | Brennan Center | [ ] Replied [ ] NO RESPONSE |
| D48-4 | Worth Rises | [ ] Replied [ ] NO RESPONSE |
| D48-5 | M4BL | [ ] Replied [ ] NO RESPONSE |

**T+14 escalation actions** (trigger only if no response from specific contacts):

| Condition | Action |
|---|---|
| CLC has not replied | Send brief follow-up to echlopak@campaignlegalcenter.org — 3 sentences max. Subject: "Following up — Citizens United research, Hawaii/Montana charter model" |
| Common Cause CA has not replied | Send brief follow-up to dkemp@commoncause.org — 3 sentences max. Subject: "Following up — CA Fair Elections Act research" |
| Sentencing Project has not replied | Escalate to info@sentencingproject.org general inbox (not Nicole Porter directly). Include "Virginia July 15" in subject if before July 15. |
| M4BL has not replied AND July 7 has passed | Activate Virginia contingency path via ACLU of Virginia (acluva@acluva.org — Mary Bauer). Do not follow up M4BL directly. |
| Issue One, PPI, Worth Rises, Brennan Center not replied | Do NOT send follow-up. One contact per organization per wave cycle. |

---

## WAVE 2 TRIGGER CONDITIONS

*Copy the applicable trigger condition to your calendar or task manager on the date of your first Wave 1 send.*

### Trigger Condition A — ACCELERATE (rate > 60%)

**Condition**: ≥ 6 of 9 Wave 1 contacts reply with any signal (STRONG, MODERATE, or WEAK) by Day 7.
**Trigger date**: Day 7 from first send = _______ (fill in)
**Action if triggered**: Launch Wave 2 immediately using DOMAIN_51_WAVE_2_SEND_TEMPLATES.md and DOMAIN_48_WAVE_2_SEND_TEMPLATES.md without modification. Expand contact list: add 20+ Tier B contacts for Domain 51 (Arizona Prop 130 campaign, Massachusetts Fair Elections Act campaign — see DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md Tier 2 list). Activate NAACP LDF and Fines and Fees Justice Center for Domain 48 immediately.

### Trigger Condition B — PROCEED (rate 40–59%)

**Condition**: 4–5 of 9 Wave 1 contacts reply by Day 7.
**Trigger date**: Day 7 = _______
**Action if triggered**: Authorize Wave 2 with current templates. Target launch: July 1–2. No modification needed.

### Trigger Condition C — REFINE (rate 20–39%)

**Condition**: 2–3 of 9 Wave 1 contacts reply by Day 7.
**Trigger date**: Day 7 = _______
**Action if triggered**: Minor template refinement (30–45 min). Adopt the subject line or opening framing from any replies that worked. Wave 2 launch: July 1–3.

### Trigger Condition D — REVISE (rate < 20%)

**Condition**: 0–1 of 9 Wave 1 contacts reply by Day 7.
**Trigger date**: Day 7 = _______
**Action if triggered**: Hold Wave 2. Template revision: 1–2 hours. Focus revision on: (1) shorter email (reduce from ~480w to ~300w), (2) more specific advocacy ask tied to concrete deadline, (3) different subject line (test "urgent research" framing vs. current "analysis" framing). Re-test with 1 contact per domain on July 7–8 before full Wave 2 launch on July 14.

### Trigger Condition E — VIRGINIA OVERRIDE (July 7 deadline)

**Condition**: July 7 is reached and no Domain 48 Wave 2 Virginia contacts (Virginia Organizing, Progress Virginia, Virginia Interfaith Center) have been sent.
**Trigger date**: July 7, 2026 — HARD DATE
**Action**: Send Virginia fast-track immediately regardless of Wave 1 rate. See DOMAIN_48_WAVE_2_SEND_TEMPLATES.md "Virginia-Urgency Fast Track" section. Three sends (Templates 3, 6, 7) execute July 7 regardless of any other gate status. Virginia July 15 deadline does not move.

### Trigger Condition F — STALL ACCELERATION (June 27 12:00 UTC)

**Condition**: Wave 1 sends still incomplete (< 4 total sends) on June 27 12:00 UTC.
**Trigger date**: June 27, 12:00 UTC
**Action**: Execute catch-up compressed timeline per WAVE1_CATCH_UP_PROCEDURES.md. Remaining Domain 51 and 48 sends proceed on compressed same-day schedule. "Rapid response" framing language in Domain 51 templates modified to remove Senate markup urgency if markup has concluded. Domain 48 Virginia framing remains fully valid through July 14.

---

## RESPONSE RATE BASELINES

These baselines are derived from prior SCOTUS rapid-response distribution performance and adjusted for the current organizational targets.

| Metric | Target | Source Baseline | Notes |
|--------|--------|----------------|-------|
| Open rate | > 40% | Prior SCOTUS rapid-response sends | Gmail/Outlook do not track opens for individual sends without tracking pixel; approximate via reply-as-proxy |
| Reply rate by Day 7 | > 15% | Prior organizational outreach rounds | 15% = 1–2 of 9 sends; "floor" threshold for template validity |
| Reply rate minimum for Wave 2 without revision | ≥ 20% | Prior rapid-response performance | 20% = 2 of 9 sends |
| STRONG signal target | ≥ 2 across both domains | Phase 2 activation minimum | 2 STRONG signals from Tier 1 = conditional Phase 2 approval |
| STRONG signal for full Wave 2 | ≥ 4 across both domains | Phase 2 full activation | 4 STRONG signals = full Tier 2 expansion authorized |
| Virginia deadline | July 15, 2026 | Right to Vote Coalition integration window | Non-recoverable; Virginia coalition Tier 2 contacts activate July 7 if not reached earlier |

**Note on open rate tracking**: Without a tracking pixel (not recommended for advocacy emails), open rate cannot be measured directly. Use reply rate as the functional proxy. A reply rate ≥ 20% implies an open rate substantially higher (typically 3–5x reply rate in organizational advocacy outreach). If your email client provides open data (some clients show "message read" receipts), log those in the Reply Log above with "READ (no reply)" as the signal level.

---

## DECISION TREE — JUNE 28 WAVE 2 GO/NO-GO

```
June 28 assessment:

Combined Wave 1 reply rate (by June 28)?

  > 60% ─────────────────────────────────────────────┐
                                                      │
  40–59% ───────────────────────────────────────────┐ │
                                                    │ │
  20–39% ─────────────────────────────────────────┐ │ │
                                                  │ │ │
  < 20% ─────────────────────────────────────────┐│ │ │
                                                 ││ │ │
                                                 ▼▼ ▼ ▼
                                                REVISE  REFINE  PROCEED  ACCELERATE
                                                  │       │        │         │
                                         Rev: 1-2h  Rev:30m  No rev    No rev
                                         July 7+    July 1-2  July 1-2  June 29-30
                                             │       │        │         │
                                             ▼       ▼        ▼         ▼
                                        Re-test  Full     Full      Expanded
                                        1 each   Wave 2   Wave 2    Wave 2 +
                                        July 7-8 templates templates 20+ contacts
                                                 unchanged unchanged per domain

REGARDLESS OF ABOVE ─────────────────────────────────────────────────────────────┐
                                                                                  │
July 7 reached with no VA contacts sent?                                          │
  YES: Execute DOMAIN_48_WAVE_2_SEND_TEMPLATES.md Virginia Fast Track immediately │
  NO: Continue on rate-based decision above                                       │
                                                                                  ▼
                                                              All decisions subordinate to
                                                              Virginia July 15 hard deadline
```

---

## CROSS-REFERENCES

- Wave 1 execution checklist: `projects/resistance-research/execution/domain-51-48-wave-1-execution-checklist.md`
- Domain 51 Wave 1 package (10 Tier 1 contacts): `DOMAIN_51_WAVE_1_EMAIL_EXECUTION_PACKAGE.md`
- Domain 48 email templates (Wave 1): `DOMAIN_48_EMAIL_TEMPLATE_SET.md`
- Domain 48 contact stratification: `DOMAIN_48_CONTACT_LIST_AND_STRATIFICATION.md`
- Domain 51 Wave 2 Tier 2 (NEW — this session): `DOMAIN_51_WAVE_2_SEND_TEMPLATES.md`
- Domain 48 Wave 2 Tier 2 (NEW — this session): `DOMAIN_48_WAVE_2_SEND_TEMPLATES.md`
- Escalation thresholds with pre-written BLOCKED.md entries: `DOMAINS_51_48_ESCALATION_THRESHOLDS.md`
- Daily monitoring checklist (parallel document): `DOMAINS_51_48_WAVE1_DAILY_MONITORING_CHECKLIST.md`
- Catch-up procedures: `WAVE1_CATCH_UP_PROCEDURES.md`
- Execution status tracker: `DOMAINS_51_48_WAVE1_EXECUTION_STATUS_TRACKER.md`
- Domain 51 distribution log: `DOMAIN_51_DISTRIBUTION_EXECUTION_LOG.md`
- Domain 48 distribution log: `DOMAIN_48_DISTRIBUTION_SEND_LOG_TEMPLATE.md`
- T+7 decision automation: `T7_CHECKPOINT_DECISION_AUTOMATION.md`

---

*Created June 24, 2026. Daily tracking template for June 24 – July 7 with numeric baselines (>40% open rate / >15% reply rate targets), exact UTC trigger times, Wave 2 decision tree, and Virginia July 15 override conditions. Companion documents: DOMAIN_51_WAVE_2_SEND_TEMPLATES.md and DOMAIN_48_WAVE_2_SEND_TEMPLATES.md (created same session).*
