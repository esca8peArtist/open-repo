---
title: "Phase 1 Launch Readiness Checklist"
project: cybersecurity-hardening
created: 2026-05-09
status: ready-for-user-execution
phase: Phase 1 — Tier 1 Institution Outreach
depends_on:
  - PHASE_1_FLAGS_ASSESSMENT.md
  - TIER1_PHASE1_READINESS_SUMMARY.md
  - TIER1_PREFLIGHT_CHECKLIST.md
  - TIER1_OUTREACH_EXECUTION_PLAN.md
  - TIER1_EXECUTION_RUNBOOK.md
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
---

# Phase 1 Launch Readiness Checklist

**Status**: All materials production-ready. Awaiting user execution.

**Purpose**: This is the consolidated go/no-go checklist before sending the first Tier 1 outreach email. Complete every section top-to-bottom. Estimated time: 90–120 minutes including corpus updates for Flags 1 and 3.

**Decision gate**: Do not send Day 1 emails until all sections in Part A (Corpus Accuracy) and Part B (Infrastructure) are checked. Parts C through E are reference sections to read before executing, not pre-launch gates.

---

## Part A — Threat Accuracy Verification (Complete Before Sending)

Three accuracy flags were identified in PHASE_1_FLAGS_ASSESSMENT.md during the Session 866 review. Status and required actions are documented below. Flag 2 is deferred per assessed risk level.

### Flag 1: ICE Mobile Fortify — Field Biometric Deployment (HIGH PRIORITY — Resolve Before Launch)

**Issue**: The corpus's biometric section frames collection as checkpoint-specific. Mobile Fortify (NEC-powered, deployed since early 2025, 100,000+ field uses confirmed) enables biometric collection at any public street encounter — no formal processing required. This is a material accuracy gap for Tier 1 readers.

**Required action**: Add a 100-word clarification paragraph to `opsec-playbook.md` in the existing biometric section. Suggested text from PHASE_1_FLAGS_ASSESSMENT.md:

> "Mobile Fortify Field Deployment (2026 Update): As of January 2026, ICE operates Mobile Fortify, a handheld facial recognition and fingerprint scanning app used by field agents. ICE has used this system more than 100,000 times in field operations. This enables biometric collection at any public encounter without a formal processing step. While this expands the threat surface, the countermeasures are unchanged: face masks, hats, and avoiding identification-enabling situations remain effective. Device-level hardening (GrapheneOS) is unaffected."

**Verification**: Confirmed accurate per EFF reporting (November 2025), Illinois/Chicago lawsuit (January 2026), and Biometric Update coverage (January 2026).

**Estimated effort**: 15 minutes.

- [ ] Paragraph added to `opsec-playbook.md` biometric section
- [ ] Gist updated with revision note: "Section 4 (Biometrics) updated 2026-05-09: Mobile Fortify field deployment scope clarified"
- [ ] Gist accessibility re-verified in private/incognito browser after update

---

### Flag 2: DOGE/SSA Court Ruling — Litigation Status (DEFERRED to July 26, 2026 Quarterly Review)

**Issue**: The corpus states "at least 15 federal lawsuits were challenging [DOGE data access] as of early 2026," implying ongoing legal constraint. The Fourth Circuit vacated the preliminary injunction in April 2026, and the Supreme Court had previously given DOGE access to proceed. SSA data is currently operationally accessible to DOGE-affiliated personnel.

**Decision**: Defer to July 26 quarterly review. The underlying countermeasures (financial compartmentalization, data minimization) are unchanged. This is a litigation-status update, not a countermeasure gap.

**Action item for July 26 review**: Update threat-model.md DOGE section with post-April 2026 litigation status. Suggested language in PHASE_1_FLAGS_ASSESSMENT.md is already drafted.

**Note for Week 1 outreach**: If any Tier 1 recipient asks specifically about DOGE data access litigation status, provide updated verbal context: "As of April 2026, the Fourth Circuit vacated the preliminary injunction; SSA data is operationally accessible to DOGE personnel pending final merits resolution. The countermeasures we recommend are unchanged."

- [ ] Flag 2 noted for July 26 quarterly review (no pre-launch action required)

---

### Flag 3: Cellebrite Device Seizure — BFU/AFU Distinction (HIGH PRIORITY — Resolve Before Launch)

**Issue**: The corpus accurately states Signal's server-side protection. It does not explain the BFU/AFU distinction: a device in AFU state (unlocked at least once, encryption keys in memory) is substantially more vulnerable to Cellebrite Physical Analyzer extraction than a device in BFU state (powered off, keys not in memory). For high-risk Tier 1 readers (immigration attorneys, activists with arrest risk), this is a meaningful gap.

**Required action**: Add a new subsection to `implementation-guide.md` (Part 8 or Part 9: Device Seizure). Content to include:

1. BFU/AFU distinction (200 words): Encryption key availability, why it matters for Cellebrite extraction, practical implication: power off before any anticipated law enforcement encounter.
2. Wipe passphrase / duress PIN (150 words): How to configure in GrapheneOS Settings > Security > Wipe passphrase. Legal caveat: consult counsel on coercion/obstruction implications before relying on this.
3. Auto-reboot configuration (100 words): Settings > Security > Auto-reboot after inactivity. Recommended: 12–24 hours. Effect: device seized and left unsupervised overnight reverts to BFU state.
4. Cross-reference to existing content (50 words).

**Update note**: As of April 2025 (Android 16/Google Play Services), Android devices now auto-reboot to BFU after 72 hours of no successful unlock by default. The recommended 12–24 hour GrapheneOS auto-reboot setting is more protective than the default, and should still be documented as the recommended configuration.

**Estimated effort**: 45–60 minutes.

- [ ] BFU/AFU subsection added to `implementation-guide.md`
- [ ] Gist updated with revision note: "Section 8/9 (Device Seizure) added 2026-05-09: BFU/AFU distinction, wipe passphrase, auto-reboot configuration"
- [ ] Gist accessibility re-verified after update

---

### Part A Completion Gate

Do not proceed to Part B until both are checked:

- [ ] Flag 1 (Mobile Fortify) — paragraph added and Gist updated
- [ ] Flag 3 (Cellebrite/BFU) — subsection added and Gist updated

---

## Part B — Infrastructure Verification (Pre-Flight, 45–60 Minutes)

This is a condensed version of TIER1_PREFLIGHT_CHECKLIST.md for same-day use.

### Gist Accessibility

- [ ] Open Gist URL in private/incognito browser: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Confirm no login required
- [ ] All 7 corpus sections present and readable
- [ ] Mobile Fortify update visible in Section 4 (biometrics)
- [ ] BFU/AFU section visible in Section 8/9

### URL Tracking

- [ ] Bitly (or equivalent) short URL created and tested — redirects correctly to Gist
- [ ] Short URL confirmed to load without login in private browser

### Email Infrastructure

- [ ] 7 Gmail labels created under `Tier1-Outreach` (1A-National, 1A-Regional, 1B-National, 1B-Regional, 1C-National, 1C-Regional, Follow-up)
- [ ] 5 response templates saved as Gmail drafts (R1: Engagement, R2: Acknowledgment, R3: Declination, R4: Bounce, R5: OOO)
- [ ] BCC setup confirmed

### Tracking Spreadsheet

- [ ] Google Sheet or CSV tracking file created
- [ ] Column headers: Org Name / Contact / Email / Tier / Date Sent / Response Date / Response Type / Follow-up Date / Notes
- [ ] Day 1 organizations pre-populated: NILC, CLINIC, RAICES, ILRC, NLG

### Email Deliverability

- [ ] Send test email from sending account to yourself — confirm delivery to inbox (not spam)
- [ ] Subject line test: send a draft with Day 1 subject line to confirm no spam filter trigger

### Contact Verification (Day 1)

- [ ] NILC — info@nilc.org — confirm current on nilc.org contact page
- [ ] CLINIC — national@cliniclegal.org — confirm current on cliniclegal.org
- [ ] RAICES — communications@raicestexas.org — confirm current
- [ ] ILRC — kbello@ilrc.org — confirm current or find current contact on ilrc.org
- [ ] NLG — massdef@nlg.org — confirm current on nlg.org

---

## Part C — Gist Creation Steps (Reference — If Gist Needs to Be Republished)

The Gist is verified published and accessible as of 2026-04-29. These steps apply only if the Gist URL changes, is deleted, or requires republication.

**Gist creation procedure** (from `execution/domain-42-gist-creation-steps.md` methodology):

1. Go to gist.github.com and sign in as esca8peArtist
2. Click "+" to create a new gist
3. Set filename: `opsec-corpus-[version]-[date].md`
4. Paste corpus content (all 7 sections) in order
5. Set visibility: Public (not Secret)
6. Click "Create public gist"
7. Copy the resulting URL
8. Test in private/incognito browser (confirm no login required)
9. Update Bitly short link to point to new URL
10. Update all outreach templates with new Gist URL before sending

**If Gist is updated but URL is stable** (post-Flag-1 and Flag-3 edits): Click "Edit" on the existing Gist, make changes, click "Update public gist." The URL does not change. Bitly redirect does not need updating.

---

## Part D — Tier 1 Contact Outreach Templates Verification

All personalized templates are documented in TIER1_OUTREACH_PREPARED.md (Tier 1A national) and TIER1_DISTRIBUTION_PREP.md (Tier 1B and 1C). Review these before Day 1.

### Tier 1A: Immigration Legal Aid (Days 1–7)

**25 organizations targeted**: 5 national (Day 1) + 20 regional (Days 2–5)

**Day 1 national contacts** with personalized templates ready:

| Organization | Contact | Personalization Hook |
|-------------|---------|---------------------|
| NILC | info@nilc.org | Lead with Part 0 actionability + primary-source citation structure for legal advocacy |
| CLINIC | national@cliniclegal.org | Lead with 400+ affiliates distribution channel; California path (AB 60/AB 1766) |
| RAICES | communications@raicestexas.org | Lead with regional chapter structure; Part 0 workshop format |
| ILRC | kbello@ilrc.org | Lead with legal-citability; implementation verification |
| NLG | massdef@nlg.org | Lead with Part 0 for members + legal observer dimension |

**Day 2–5 regional research**: Research pattern documented in TIER1_EXECUTION_LOG.md: "[state] immigration legal aid," "[state] law school immigration clinic," "[state] public defender immigration unit." Target 5 per day for Days 2–5.

### Tier 1B: Community-Based Organizations (Days 8–14)

**Day 8 national contacts**:
- We Are CASA — wearecasa.org/contact/
- Make the Road — mediacontact@maketheroadny.org
- United We Dream — info@unitedwedream.org
- Centro de los Derechos del Migrante — info@cdmigrante.org
- [Local sanctuary network — research before Day 8]

**Personalization hook for 1B**: "Part 0 is workshoppable — a 2-hour community session can walk through opt-outs together. No technical background required." Lead with accessibility and harm reduction framing; avoid corporate language.

### Tier 1C: Mutual Aid Networks (Days 15–21)

**Day 15 national contacts**:
- National Bail Fund Network — info@nationalbailfund.org
- Community Justice Exchange — network@communityjusticeexchange.org
- Food Not Bombs (varies by chapter — research regional contact)
- Anarchist Black Cross (varies by region)
- [Local mutual aid hub — research before Day 15]

**Personalization hook for 1C**: "Part 0 is the highest-leverage action for the broadest population. Tier 2/3 are for people with specific reason to believe they're under active investigation." Assume audience knows Signal/Tor/GrapheneOS; lead with harm reduction and immediate action.

---

## Part E — Email Scheduling and Batching Strategy

### Send Volume and Timing

- **Maximum**: 5 emails per day (avoids Gmail rate-limit flags, maintains quality per personalization)
- **Optimal send time**: 7:00–9:00 AM local time (highest open rates for professional email; organizational contacts check morning email)
- **Avoid**: Friday afternoon and weekend sends (organizational contacts less likely to action before Monday)

### Week-by-Week Schedule

| Week | Days | Activity | Volume |
|------|------|----------|--------|
| Week 1 | Days 1–7 | Tier 1A (Immigration Legal Aid) active send + research Days 2–5 contacts | 25 emails |
| Week 2 | Days 8–14 | Tier 1B (Community Organizations) active send | 25 emails |
| Week 3 | Days 15–21 | Tier 1C (Mutual Aid) active send | 15–20 emails |
| Week 4 | Days 22–28 | Follow-up loop: R1 engagement replies, R2 acknowledgment follow-ups | ~15 follow-ups |
| Weeks 5–7 | Days 29–49 | Second follow-up wave for non-responses; response handling | Ongoing |

### Batch Composition Rule

Each day's 5 emails should be from the same tier (1A, 1B, or 1C) but can mix national and regional contacts after Day 1. Do not mix tiers within a send day — tone and personalization differ significantly enough to increase error risk.

### Response Handling (Do Immediately Upon Receipt)

All response templates in TIER1_OUTREACH_EXECUTION_PLAN.md Section 1.4:

| Template | Trigger | Timeline |
|----------|---------|----------|
| R1: Engagement | Questions, interest, intent to share | Reply within 24 hours |
| R2: Acknowledgment | "Will review" / "passed to team" | Follow up after 10 days if no further engagement |
| R3: Declination | "Not for us" / "remove" | Acknowledge, do not follow up |
| R4: Bounce | Permanent delivery failure | Research alternate contact immediately |
| R5: OOO | Auto-reply with return date | Log return date; follow up 2 days after return |

---

## Part F — Expected Outcomes and Timeline

### Phase 1 Active Campaign: Weeks 1–7

| Milestone | Timeline | Trigger |
|-----------|----------|---------|
| Day 1 emails sent | Week 1 Day 1 | Part A and B checks complete |
| Tier 1A complete | End of Week 1 | 25 emails sent to immigration legal aid |
| Tier 1B complete | End of Week 2 | 25 emails sent to community orgs |
| Tier 1C complete | End of Week 3 | 15–20 emails sent to mutual aid |
| First response window | Weeks 2–4 | 2–4 weeks for organizational response |
| Adoption signal window | Weeks 4–6 | 4–6 weeks for adoption indicators |
| Phase 1 gate decision | Week 7 | Pass/fail on success metrics |

### Response Timeline Expectations by Tier

- **Tier 1A (Legal Aid)**: National organizations respond in 3–10 business days. Regional organizations are slower — 10–21 days. Legal aid staff are high-volume; assume 2 weeks before follow-up.
- **Tier 1B (Community)**: Faster than 1A — 3–7 days for national. Community staff are responsive but communications routing varies by organization structure.
- **Tier 1C (Mutual Aid)**: Fastest — 1–5 days. Mutual aid networks operate with high urgency; a relevant resource gets shared quickly or not at all.

### Adoption Signal Timeline

- **2–4 weeks**: First responses (acknowledgment, questions, forwarding intent)
- **4–6 weeks**: Adoption signals (forwarding confirmed, sharing with network, workshop integration)
- **6–8 weeks**: Secondary amplification (Bitly click spikes not from your sends, referral contacts reaching out)

---

## Part G — Success Metrics

### Primary Success Metric

**Campaign success = Response rate >10% by end of Week 2** (2.5+ responses from 25 Day-1-to-Day-14 sends)

### Secondary Indicators

| Metric | Minimum (Week 4) | Good (Week 6) | Strong (Week 8) |
|--------|-----------------|--------------|----------------|
| Overall response rate | >10% | >20% | >30% |
| Engagement responses (R1 class) | >5% | >10% | >15% |
| Bitly click rate | >15% | >25% | >35% |
| Meeting acceptance (if applicable) | 1 | 2–3 | 5+ |
| Amplification signals (sharing, referrals) | 1 | 3 | 5+ |

### Amplification Signals to Track Actively

1. Contact explicitly says they forwarded to their network — ask about reach
2. Bitly click spike not correlated with your send date (someone else shared the link)
3. New organization contacts you via referral from a Tier 1 recipient
4. A Tier 2 amplifier (EFF, Freedom of the Press Foundation, 404 Media, The Intercept) mentions or cites the corpus

### Pivot Triggers

If by Day 14 (end of Week 2):
- Response rate is <5%: Review subject lines and opening sentences; A/B test alternative framing
- A specific category (e.g., law school clinics) is at 0% response: Adjust framing for that sub-sector
- No Bitly clicks: Verify Gist URL is correct in sent emails; check email deliverability

Pivot protocols documented in TIER1_OUTREACH_EXECUTION_PLAN.md Section 5.3.

---

## Part H — Next-Step Callouts Requiring User Approval or Action

**Before launching (user action required)**:

1. CORPUS UPDATE — Flag 1 (Mobile Fortify): User or agent must add the Mobile Fortify paragraph to `opsec-playbook.md` and update the Gist. Estimated: 15 minutes. If user wants agent to draft exact text, confirm and agent will execute.

2. CORPUS UPDATE — Flag 3 (Cellebrite/BFU): User or agent must add BFU/AFU subsection to `implementation-guide.md` and update the Gist. Estimated: 45–60 minutes. If user wants agent to draft the full subsection, confirm and agent will execute.

3. CONTACT RESEARCH — Days 2–5 regional contacts: 20 regional immigration legal aid contacts need to be identified before Day 5. Research pattern is documented. User can research or assign to agent for Sunday pre-launch batch.

4. AUTHORIZATION — Day 1 email send: User must authorize the first email batch. Day 1 target: NILC, CLINIC, RAICES, ILRC, NLG. Ready to send upon authorization.

**Decisions user can make now to accelerate**:
- [ ] Authorize agent to complete Flag 1 and Flag 3 updates (yes/no)
- [ ] Authorize agent to research Days 2–5 regional contacts (yes/no)
- [ ] Confirm intended launch date for Day 1 emails
- [ ] Review Day 1 email templates in TIER1_OUTREACH_PREPARED.md and approve messaging

---

**Document status**: Complete — ready for user execution  
**Prepared**: 2026-05-09  
**Flag assessment basis**: PHASE_1_FLAGS_ASSESSMENT.md (2026-05-07)  
**Primary sources verified**: EFF Mobile Fortify reporting (2025-11), Illinois/Chicago lawsuit (2026-01), Cellebrite BFU/AFU documentation (confirmed), Fourth Circuit DOGE ruling (2026-04)
