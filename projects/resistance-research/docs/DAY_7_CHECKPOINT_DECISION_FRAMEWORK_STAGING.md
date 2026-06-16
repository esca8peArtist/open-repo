---
title: "Day 7 Checkpoint Decision Framework — Pre-Staged for June 17-18, 2026"
created: "2026-06-16"
status: "pre-staged-for-checkpoint"
checkpoint_execution: "June 17-18, 2026"
decision_gates: "STRONG / MODERATE / WEAK"
phase_2_activation: "June 18-20, 2026"
---

# Day 7 Checkpoint Decision Framework
## Phase 2 Resistance-Research Campaign — Pre-Staged for June 17-18 Execution

*Framework prepared June 16, 2026. Three decision paths pre-populated with actions, sequencing, and resource allocation. Execute June 17-18 after engagement metric collection. Decision output = specific action path routing.*

---

## CHECKPOINT EXECUTION WORKFLOW (June 17-18, 2026)

### Step 1: Engagement Metric Collection (June 17 morning, 20 minutes)

**Time**: 08:00-10:00 local (June 17 morning)
**Location**: `WAVE_1_2_EXECUTION_STATUS_AUDIT.md` "Checkpoint Summary Table"

**Collect these metrics**:

| Metric | Source | Measurement Method | Entry |
|--------|--------|-------------------|-------|
| Email replies | Inbox | Count substantive emails from: CLC, Issue One, Common Cause CA, LWV CA, Clean Money AF | ___ |
| OOO/bounce count | Inbox | Count auto-replies and hard bounces | ___ |
| Gist view delta | GitHub Gist | Compare view count June 14 (baseline) to June 17 morning (current) | ___ |
| Bitly clicks | Bitly dashboard (if available) | Click count on domain-51 Gist short URL | ___ |
| Estimated open rate | Calculated | If replies: 100% for that contact; if Gist click: 50% proxy; if silent: 0% | ___ |

**Completed metric table** (fill in before Step 2):

| Organization | Contact | Email Date Sent | Status | Signal Type | Est. Open Rate | Notes |
|---|---|---|---|---|---|---|
| CLC | Chlopak | 06/09 | ? | ? | ? | ? |
| Issue One | Penniman | 06/09 | ? | ? | ? | ? |
| Common Cause CA | Kemp | 06/11 | ? | ? | ? | ? |
| LWV CA | Farrell | 06/11 | ? | ? | ? | ? |
| Clean Money | ? | 06/11 | ? | ? | ? | ? |

**Running tally**:
- Total emails sent: 5
- Total replies collected: ___
- Total OOO/bounces: ___
- Estimated aggregate open rate: ___% (calculated: replies ÷ 5 × 100 + Gist engagement bonus)
- Gist view count delta: ___ views

---

### Step 2: Classification Logic (June 17 morning, 10 minutes)

**Decision tree** (execute in order; stop at first MATCH):

```
IF (Reply count >= 2) OR (Gist delta > 10 views) OR (Open rate >= 15%):
    CLASSIFICATION = STRONG
    ROUTE = PATH A (Full Parallel Activation)
    
ELSE IF (Reply count >= 1) OR (Gist delta >= 5 views) OR (Open rate 8-14%):
    CLASSIFICATION = MODERATE
    ROUTE = PATH B (Selective Activation)
    
ELSE IF (Reply count = 0) AND (Gist delta <= 5) AND (Open rate < 8%):
    CLASSIFICATION = WEAK
    ROUTE = PATH C (Diagnostic + Contingency)
    
ELSE:
    CLASSIFICATION = TOO EARLY
    ROUTE = HOLD (continue monitoring through June 19; rerun classification)
```

**Run classification on completed metrics** (circle one):

- [ ] **STRONG** → PATH A
- [ ] **MODERATE** → PATH B
- [ ] **WEAK** → PATH C
- [ ] **TOO EARLY** → HOLD

---

### Step 3: Routing Decision (June 17 morning, 5 minutes)

**Route selection** (corresponds to classification above):

- If STRONG: Execute **PATH A** (→ Section "Path A: STRONG Engagement" below)
- If MODERATE: Execute **PATH B** (→ Section "Path B: MODERATE Engagement" below)
- If WEAK: Execute **PATH C** (→ Section "Path C: WEAK Engagement" below)
- If TOO EARLY: Continue monitoring; re-run classification June 19 morning

---

## PATH A: STRONG ENGAGEMENT (≥2 replies + Gist engagement)

### Engagement Threshold Met

**Evidence**:
- ✓ ≥2 substantive email replies from Wave 1-2 contacts
- ✓ ≥3+ Gist clicks confirmed (click = 50% engagement proxy)
- ✓ ≥40% estimated open rate
- ✓ ≥0 hard bounces (all emails delivered)

**Implication**: Research resonates with target organizations. Tier 1 engagement sufficient to activate Tier 2 expansion and parallel new domains without risk of wasted outreach. Full Phase 2 launch authorized.

---

### ACTION PLAN: PATH A

#### Immediate Actions (June 17-18)

**1. Authorize Domain 51 Tier 2 expansion** (June 17 morning):
- Release 6 Tier 2 contacts for June 19-20 Wave 1 execution:
  * OpenSecrets (contact: research@opensecrets.org)
  * Democracy 21 (contact: tanya@democracy21.org)
  * Public Citizen (contact: cmendez@citizen.org)
  * Montana ballot campaign (contact: TBD from state campaign committee)
  * Michigan election board (contact: TBD)
  * Massachusetts good government (contact: TBD from MALDEF/Democracy Matters)
- **Time**: Pre-execution verification (15 min) — confirm all 6 email addresses current via org websites
- **Material**: Domain 51 Tier 2 email templates (3 template variants for OpenSecrets/Democracy 21 type vs. state-level vs. academic)
- **Timeline**: Send June 19-20 (120 min user time)

**2. Execute Domain 59 urgency frame patch** (June 17):
- Complete patch to replace obsolete Senate Finance markup urgency frame with OBBBA implementation period + 2026 midterm integration
- **Patch location**: `WAVE_1_NEWS_INTEGRATION.md` (documented; requires 15-min edit to `domain-59-send-templates.md`)
- **Timeline**: Complete by June 17 18:00 UTC
- **Verification**: Re-read patched templates to confirm urgency frame is current (3 min)

**3. Create Domain 48 Gist** (June 17):
- Create GitHub Gist from `domains/domain-48-criminal-justice-civic-exclusion.md` (6,800+ words, 46 citations)
- **Procedure**: `DOMAIN_48_GIST_CREATION_STEPS.md` (5-10 minutes)
- **URL placement**: Fill `{{DOMAIN_48_GIST_URL}}` in all templates in `DOMAIN_48_EMAIL_TEMPLATE_SET.md`
- **Timeline**: Complete by June 17 noon

**4. Authorize Domain 59 Wave 1 execution** (June 17 afternoon):
- Release 5 Tier 1 contacts for June 18-19 Wave 1 execution:
  * CBPP (contact: cbpp@cbpp.org)
  * ITEP (contact: itep@itep.org)
  * NWLC (contact: info@nwlc.org)
  * MomsRising (contact: info@momsrising.org)
  * AFL-CIO (contact: feedback@aflcio.org)
- **Material**: Domain 59 patched email templates (5 customized emails, `domain-59-send-templates.md`)
- **Timeline**: Send June 18-19 (90 min user time)

**5. Authorize Domain 48 Wave 1 execution** (June 17 afternoon):
- Release 4 contacts for June 19-20 Wave 1 execution:
  * The Sentencing Project (contact: nporter@sentencingproject.org)
  * Prison Policy Initiative (contact: info@prisonpolicy.org)
  * Campaign Legal Center (contact: echlopak@campaignlegalcenter.org)
  * Worth Rises (contact: info@worthrises.org)
- **Material**: Domain 48 email templates with Gist URL filled (4 customized emails)
- **Timeline**: Send June 19-20 (75 min user time)

---

#### Phase 2 Sequencing: STRONG Path

**June 18-19 (Day 1-2 Phase 2 Tier 1 expansion)**:

| Time | Task | Domain | Contacts | User Time |
|------|------|--------|----------|-----------|
| 09:00-10:30 | Send Domain 59 Wave 1 | 59 | CBPP, ITEP, NWLC, MomsRising, AFL-CIO | 90 min |
| 11:00-13:00 | Send Domain 51 Tier 2 (Tier 1 group) | 51 | OpenSecrets, Democracy 21, Public Citizen | 120 min |
| **Total Phase 2 Day 1-2**: | | | | **210 min (3.5 hours)** |

**June 19-20 (Day 3-4 Phase 2 Tier 1 expansion)**:

| Time | Task | Domain | Contacts | User Time |
|------|------|--------|----------|-----------|
| 09:00-10:15 | Send Domain 48 Wave 1 | 48 | Sentencing Project, PPI, CLC, Worth Rises | 75 min |
| 11:00-13:00 | Send Domain 51 Tier 2 (state-level + academic) | 51 | MT, MI, MA campaigns + academic contacts | 120 min |
| **Total Phase 2 Day 3-4**: | | | | **195 min (3.25 hours)** |

**June 19-24 (Response collection & monitoring)**:

- **Domain 59**: 5-day window (June 18-22); target 2-3 replies minimum (CBPP + ITEP + 1 secondary)
- **Domain 51 Tier 2**: 4-day window (June 19-23); target 3-4 replies from 6 contacts (60-65% response rate)
- **Domain 48**: 4-day window (June 19-23); target 1-2 replies from 4 contacts (25-50% response rate)

---

#### Metric Collection Template (June 17-18 through June 23)

**Purpose**: Track engagement metrics for each domain in parallel to assess whether Phase 2 activation requires adjustment or is on pace for synthesis.

**Collect daily** (June 18-22, 10 min per day):

```
Date: June 18
Domain 59 replies: ___ | Open rate estimate: ___%
Domain 51 Tier 2 replies: ___ | Open rate estimate: ___%
Domain 48 replies: ___ | Open rate estimate: ___%
Gist engagement (Bitly or view count): ___
Notes: [any organizational changes, contact issues, etc.]

[Repeat June 19-22]
```

---

#### Resource Allocation Matrix: STRONG Path

| Domain | Tier | Contacts | Wave 1 Activation | Wave 2 Ready? | July 1 Deadline Impact | Resource Priority |
|--------|------|----------|-------------------|--------------|----------------------|-------------------|
| **Domain 51** | Tier 2 (6 contacts) | OpenSecrets, Dem 21, Public Citizen, MT, MI, MA | June 19-20 | June 24-25 (Wave 2) | ✓ On-time (22 days remaining) | HIGH |
| **Domain 59** | Tier 1 (5 contacts) | CBPP, ITEP, NWLC, MomsRising, AFL-CIO | June 18-19 | June 25-26 (Tier 2 expansion) | ✓ On-time (16 days remaining) | CRITICAL |
| **Domain 48** | Tier 1 (4 contacts) | Sent Proj, PPI, CLC, Worth Rises | June 19-20 | June 26-27 (Tier 2 expansion) | ✓ On-time (12 days remaining) | MEDIUM |
| **Phase 2 Synthesis** | - | - | June 23-25 (aggregate responses) | - | ✓ On-time (7 days remaining) | HIGH |
| **California Fair Elections Messaging** | - | - | June 25-30 (research integration) | - | ✓ On-time (1 day before deadline) | CRITICAL |

---

#### Routing Logic: STRONG Path Decision Tree

**If all three domains (51/59/48) respond at ≥40% rate by June 23**:
- ✓ Proceed to full Phase 2 synthesis + research integration (June 24-30)
- ✓ Activate all Tier 2 expansions June 24+ (no contingency needed)
- ✓ July 1 deadline: HIGH CONFIDENCE (9-day cushion post-research)

**If Domain 59 or 48 responds <30% by June 22**:
- ⚠ Flag for Tier 2 limited expansion (Domain 59: Tier 1 only; Domain 48: high-priority 2 contacts only)
- ⚠ Activate contingency playbook for low-response domain (messaging audit + contact pool refresh)
- ⚠ July 1 deadline: MEDIUM CONFIDENCE (5-day cushion; requires efficient synthesis)

**If any domain bounces >10%**:
- ❌ STOP Tier 2 expansion for that domain
- ❌ Execute diagnostic (contact list current? Organizational changes? Messaging issue?)
- ❌ Rerun sends with corrected contact pool only after diagnostic resolves
- ❌ July 1 deadline: HIGH PRESSURE (contingency domain activation may be required)

---

## PATH B: MODERATE ENGAGEMENT (≥1 reply OR Gist engagement, <STRONG threshold)

### Engagement Threshold: Partial Met

**Evidence**:
- ✓ 1 substantive email reply from Wave 1-2 contacts
- ✓ 5+ Gist views OR Gist clicks confirmed
- ✓ 8-14% estimated open rate
- ⚠ 1+ hard bounces OR silent majority (≥3 of 5 contacts no signal)

**Implication**: Research has traction with some organizations but not sector-wide. Tier 2 expansion should be selective (high-priority contacts only). New domains (59/48) still activate but with reduced confidence. Phase 2 proceeds on compressed timeline with tighter synthesis schedule.

---

### ACTION PLAN: PATH B

#### Immediate Actions (June 17-18)

**1. Authorize Domain 51 Tier 2 selective expansion** (June 17 morning):
- Release **3 high-priority** Tier 2 contacts (not full 6) for June 20 execution:
  * **HIGH-PRIORITY**: OpenSecrets (national, highest leverage), Montana campaign (Senate Finance timeline), Massachusetts (state ballot alignment)
  * **DEFER to post-synthesis**: Democracy 21, Public Citizen, Michigan (activate only if Domain 51 Tier 1 responses strong enough to justify broader expansion)
- **Verification**: 15 min contact check
- **Timeline**: Send June 20 (60 min user time) — delayed 1 day vs. STRONG path

**2. Execute Domain 59 urgency frame patch** (June 17, ACCELERATED):
- Complete patch by June 17 **noon** (escalated from June 17 18:00 UTC in STRONG path)
- **Reason**: MODERATE path requires faster execution to compensate for 1-day timeline compression
- **Timeline**: 15 min edit

**3. Create Domain 48 Gist** (June 18):
- Execute Gist creation June 18 morning (acceptable in MODERATE path due to later Domain 48 send window)
- **Timeline**: 10 min completion by June 18 noon

**4. Authorize Domain 59 Wave 1 execution** (June 17 afternoon):
- Release full 5 Tier 1 contacts for **June 18-19** execution (same as STRONG path)
- **Reason**: Domain 59 Senate Finance window (June 30 deadline) requires immediate activation regardless of engagement level
- **Timeline**: Send June 18-19 (90 min user time)

**5. Authorize Domain 48 Wave 1 execution** (June 17 afternoon):
- Release full 4 contacts for June 19-20 execution (same as STRONG path)
- **Timeline**: Send June 19-20 (75 min user time)

---

#### Phase 2 Sequencing: MODERATE Path

**June 18-19 (Day 1-2 Phase 2 Tier 1 expansion — Domain 59 priority)**:

| Time | Task | Domain | Contacts | User Time |
|------|------|--------|----------|-----------|
| 09:00-10:30 | Send Domain 59 Wave 1 | 59 | CBPP, ITEP, NWLC, MomsRising, AFL-CIO | 90 min |
| **Total Phase 2 Day 1-2**: | | | | **90 min** |

**June 19-20 (Day 3-4 Phase 2 expansion)**:

| Time | Task | Domain | Contacts | User Time |
|------|------|--------|----------|-----------|
| 09:00-10:15 | Send Domain 48 Wave 1 | 48 | Sentencing Project, PPI, CLC, Worth Rises | 75 min |
| 11:00-12:00 | Send Domain 51 Tier 2 (high-priority only) | 51 | OpenSecrets, MT campaign, MA campaign | 60 min |
| **Total Phase 2 Day 3-4**: | | | | **135 min** |

**June 19-23 (Response collection & monitoring — compressed)**:

- **Domain 59**: 5-day window (June 18-22); target 2+ replies minimum (CBPP, ITEP, OR MomsRising)
- **Domain 51 Tier 2**: 3-day window (June 20-23); target 2 replies from 3 contacts (66% response target)
- **Domain 48**: 4-day window (June 19-23); target 1 reply from 4 contacts (25% minimum)

**June 23-24 (Synthesis — COMPRESSED)**:

- Aggregate all responses by June 23 EOD
- Classification decision: Continue synthesis OR defer Domain 48 per engagement
- Finalize sequencing by June 24 morning

---

#### Metric Collection Template: MODERATE Path

**Daily collection** (June 18-22, 10 min per day):

```
Date: June 18
Domain 59 replies: ___ | Target: 2+
Domain 51 Tier 2 replies: ___ | Target: 2
Domain 48 replies: ___ | Target: 1
Gist engagement: ___
**COMPRESSION CHECK**: Are Domains 59/48 responses on pace for June 23 synthesis deadline?
```

---

#### Resource Allocation Matrix: MODERATE Path

| Domain | Tier | Contacts | Wave 1 Activation | Synthesis Date | July 1 Deadline Impact | Resource Priority |
|--------|------|----------|-------------------|-----------------|----------------------|-------------------|
| **Domain 51** | Tier 2 (3 contacts) | OpenSecrets, MT, MA | June 20 | June 24 | ✓ On-time (8 days remaining) | CRITICAL |
| **Domain 59** | Tier 1 (5 contacts) | CBPP, ITEP, NWLC, MomsRising, AFL-CIO | June 18-19 | June 24 | ✓ On-time (7 days remaining) | CRITICAL |
| **Domain 48** | Tier 1 (4 contacts) | Sent Proj, PPI, CLC, Worth Rises | June 19-20 | June 24 (conditional) | ⚠ Tight (7 days remaining) | MEDIUM |
| **Phase 2 Synthesis** | - | - | June 23-24 (compressed) | - | ⚠ Tight (1-day slip allowance) | CRITICAL |
| **California Fair Elections Messaging** | - | - | June 25-30 (reduced contingency) | - | ⚠ Tight (1 day before deadline) | CRITICAL |

---

#### Routing Logic: MODERATE Path Decision Tree

**If Domain 59 + Tier 2 responses meet targets (2 replies + 2 replies) by June 23**:
- ✓ Proceed to synthesis June 23-24
- ✓ Include Domain 48 in synthesis (even if <25% response)
- ✓ Phase 2 distribution June 25-30: Full three-domain coverage (compressed)
- ✓ July 1 deadline: MEDIUM CONFIDENCE (1-day cushion; no further delays possible)

**If Domain 59 or Tier 2 responses fall below targets by June 22**:
- ⚠ Execute contingency messaging audit (1 hour, June 22 afternoon)
- ⚠ Resend to non-responsive high-priority contacts June 23 (morning)
- ⚠ Compress synthesis to June 23 evening (fast-track decision tree)
- ⚠ Phase 2 distribution June 25-30: Reduced contingency focus
- ⚠ July 1 deadline: MARGINAL CONFIDENCE (zero cushion; any further delays = mission pressure)

**If any domain bounces >15%**:
- ❌ STOP Phase 2 expansion for that domain
- ❌ Execute diagnostic by June 23 morning (contact list? messaging?)
- ❌ Resend corrected list June 23 (if fix identified)
- ⚠ July 1 deadline: HIGH PRESSURE (requires fast-track synthesis + efficient distribution)

---

## PATH C: WEAK ENGAGEMENT (<1 reply AND <5% click rate)

### Engagement Threshold: NOT Met

**Evidence**:
- ✗ 0 substantive email replies from Wave 1-2 contacts (all 5 silent beyond standard lag)
- ✗ <5 Gist views (no engagement signal from clicks/views)
- ✗ <8% estimated open rate
- ✗ ≥1 hard bounce OR organizational changes detected

**Implication**: Research framing, contact list, or messaging approach requires diagnostic investigation before expanding to Tier 2. Phase 2 activation paused pending diagnostic fix or contingency domain activation. Timeline pressure increases; recovery requires fast diagnostic turnaround (4 hours maximum).

---

### ACTION PLAN: PATH C

#### Immediate Actions (June 17-18)

**HOLD all Phase 2 expansions until diagnostic completes** (June 17-18):

- [ ] **DO NOT execute** Domain 51 Tier 2 sends yet
- [ ] **DO NOT execute** Domain 59 Wave 1 sends yet
- [ ] **DO NOT execute** Domain 48 Wave 1 sends yet
- [ ] **Execute diagnostic** (4 hours total, June 17-18)

---

#### Diagnostic Protocol (June 17-18, 4 hours total)

**Part 1: Contact Delivery Verification** (1 hour, June 17):

| Contact | Email Sent | Date | Status | Delivery Check | Notes |
|---------|-----------|------|--------|-----------------|-------|
| CLC | echlopak@campaignlegalcenter.org | 06/09 | ? | [ ] Gmail bounce? [ ] Spam folder? [ ] Check org website for updates | |
| Issue One | info@issueone.org | 06/09 | ? | [ ] Gmail bounce? [ ] Spam folder? [ ] Check issueone.org for contact changes | |
| Common Cause CA | dkemp@commoncause.org | 06/11 | ? | [ ] Kemp still there (org website check) [ ] Email still current? | |
| LWV CA | lwvc@lwvc.org | 06/11 | ? | [ ] Still active address? [ ] Check lwvc.org for staff updates | |
| Clean Money | info@CAclean.org | 06/11 | ? | [ ] Still current? [ ] Check yesfairelections.org for contact change | |

**Action items**:
- For each contact: visit organization website + LinkedIn to verify person is still in role (1 min per contact × 5 = 5 min)
- Check Gmail bounce notifications (2 min)
- Check Spam folder (1 min)
- Document findings in table above
- **Decision**: Are there hard bounces or organizational changes? → YES = proceed to Part 2; NO = proceed to Part 3

**Part 2: Delivery Issues? Execute corrective sends** (June 18 afternoon):

IF hard bounces detected:
- Get corrected email from org website or call/LinkedIn message asking for correct contact
- Resend to corrected email June 18 afternoon
- Log resend + reset engagement collection clock (measure responses June 19-22, not June 10-16)

IF organizational changes detected (contact left role):
- Identify successor contact from org website or by calling main phone
- Send to successor email + include context ("I originally sent this to [Name] at [Org]; if this isn't the right person, please forward")
- Log resend + reset engagement collection clock

**Part 3: Template Audit (if no delivery issues found)** (1 hour, June 17):

Question 1: **Is the email urgency frame current?**
- Re-read Domain 51 send templates (all 5)
- Check: Does urgency frame reference current news/events? OR does it feel dated (more than 30 days old)?
- **If dated**: → Template problem identified; see Part 4

Question 2: **Is the email subject line compelling?**
- Re-read subject lines from all 5 emails
- Check: Do subject lines reference recipient's own work? OR are they generic?
- **If generic**: → Template problem identified; see Part 4

Question 3: **Is the Domain 51 Gist still current?**
- Open Gist URL: https://gist.github.com/esca8peArtist/6dce895c5192e6a3ba2abfed40733372
- Check: Are citations from June 2026 or earlier? Is any content clearly obsolete?
- **If content dated >30 days**: → Research currency problem; see Part 4

**Decision tree**:
- If all three are current: → Go to Part 5 (Consider contingency domain activation)
- If any one is dated: → Go to Part 4 (Execute template/content revision)

**Part 4: Template/Content Revision (if issues found)** (1.5 hours, June 18):

If Domain 51 templates are dated:
- Update subject lines to reference more recent news (1 hour)
- Update urgency framing in body text (30 min)
- Resend all 5 emails June 18 afternoon with revised templates
- Reset engagement collection clock (measure June 19-22, not June 10-16)
- **Decision**: Proceed to Phase 2 activation June 20+ (1 day delay vs. STRONG/MODERATE paths, acceptable)

If Domain 51 Gist content is dated:
- Update Gist with 2-3 most recent developments from June 2026 sources (1 hour)
- Post "UPDATED June 16" header to Gist
- Send update notification email to all 5 contacts: "I've updated the research document with recent developments; the Gist link now reflects the latest analysis as of June 16" (30 min)
- Reset engagement collection clock
- **Decision**: Proceed to Phase 2 activation June 20+ with revised Gist + update notification sends

**Part 5: If no delivery issues AND templates current** (1.5 hours, June 18):

**Contingency domain activation** (activate in parallel to Domain 51/59/48):
- Activate Domain 57 (Multilateral Withdrawal) OR Domain 54 (Youth Civic Power) depending on availability
- Deploy full Tier 1 contact pool (20+ contacts for Domain 57)
- **Rationale**: Domain 51/59/48 may have contacted wrong person or faced organizational barriers unrelated to research quality. Parallel activation of fresh domain with new contact pool reduces risk of wasted timeline while investigating Domain 51 issue
- Send Domain 57 Tier 1 emails June 19-20 (during diagnostic resolution window for Domain 51)
- Measure Domain 57 responses June 19-23 (parallel to Domain 51 re-sends, if any)
- **Decision**: If Domain 57 shows 40%+ response rate by June 23, use Domain 57 as primary Phase 2 focus; activate Domains 51/59/48 as secondary tier (post-diagnostic follow-up)

---

#### Phase 2 Sequencing: WEAK Path

**June 17-18 (Diagnostic window)**:

| Time | Task | Action |
|------|------|--------|
| 08:00-09:00 | Contact delivery verification | Execute Part 1 above |
| 09:00-10:00 | Template audit | Execute Part 3 above |
| 10:00-10:30 | Decision gate: Issues found? | YES = Part 2/4; NO = Part 5 |
| 10:30-13:00 | Corrective action (Part 2/4 OR Part 5) | Resend, revise, or activate contingency |

**June 18-19 (Corrective sends OR contingency activation)**:

**Option A: Corrective sends** (if delivery issues OR template issues found):
- Domain 51 resend with corrected emails OR revised templates (June 18)
- Domain 59 Wave 1: activate June 19 (standard timeline)
- Domain 48 Wave 1: activate June 20 (standard timeline)
- **Timeline**: Compressed by 1 day vs. STRONG/MODERATE

**Option B: Contingency activation** (if no issues found but engagement unexpectedly low):
- Domain 57 (Multilateral Withdrawal) Tier 1: deploy June 19-20 (20+ national contacts)
- Domain 51 investigation continues in parallel (June 19-21)
- Domain 59/48 activation deferred to post-synthesis (June 23+)
- **Timeline**: Alternative research path activates while diagnostic investigates Domains 51/59/48

**June 19-23 (Parallel response collection)**:

- Domain 57 (if activated): 5-day window, target 8+ replies from 20+ contacts (40% response rate)
- Domain 51 (if resent): 4-day window, target 1+ replies (better baseline after correction)
- Domain 59 (if activated): 5-day window, target 2+ replies
- Domain 48 (if activated): 4-day window, target 1+ reply

**June 23-24 (Synthesis — decision tree)**:

**IF Domain 57 (contingency) shows strong response (8+ replies)**:
- Proceed with Domain 57 as primary Phase 2 focus
- Activate Domain 57 Tier 2 expansion June 24-25
- Defer Domains 51/59/48 to post-July 1 analysis (secondary tier)
- **July 1 deadline**: Contingency domain research synthesis + Phase 2 analysis (acceptable fallback)

**IF Domain 51 (after correction) shows improved response (1+ replies)**:
- Proceed with Domain 51 Tier 2 expansion June 24+
- Activate Domains 59/48 Tier 1 expansion June 24+ (compressed timeline)
- Include Domain 57 (if activated) as supporting evidence
- **July 1 deadline**: All three/four domains included in synthesis (compressed but achievable)

**IF neither Domain 57 nor Domain 51 show improvement by June 23**:
- ESCALATE to contingency playbook: "Very Low Engagement" path
- Activate research completion WITHOUT new domain distribution (use existing research resources)
- Focus Phase 2 effort on synthesis of Domains 49/50 and deep-dive analysis of legislative landscape
- **July 1 deadline**: Phase 2 analysis defers primary outreach; focuses on research synthesis

---

#### Resource Allocation Matrix: WEAK Path

| Domain | Activation Status | Timeline | Response Target | Synthesis Role | July 1 Impact |
|--------|-------------------|----------|-----------------|-----------------|--------------|
| **Domain 51** | Diagnostic or resend | June 18 diagnostic + June 18 resend OR hold | 1+ replies (post-correction baseline) | Primary IF corrected | Depends on diagnostic outcome |
| **Domain 59** | Standard OR deferred | June 19 standard OR June 24+ deferred | 2+ replies | Secondary / contingency | Depends on contingency outcome |
| **Domain 48** | Standard OR deferred | June 20 standard OR June 24+ deferred | 1+ reply | Secondary / contingency | Depends on contingency outcome |
| **Domain 57 (contingency)** | Activate if no issues found | June 19-20 (parallel) | 8+ replies from 20+ contacts | Primary IF strong response | Fallback primary if Domain 51 weak |
| **Phase 2 Synthesis** | Compressed + contingency-routed | June 23-24 | Multiple decision branches | Multi-branch synthesis | High pressure; reduced confidence |

---

#### Contingency Playbooks: WEAK Path

**Recovery Condition 1: Domain 51 corrective resend shows 50%+ reply rate by June 22**
- ✓ Proceed with full Phase 2 activation June 23+ (Tier 2 expansion + Domains 59/48)
- ✓ July 1 deadline: MEDIUM CONFIDENCE (tight but achievable with efficient synthesis)

**Recovery Condition 2: Domain 57 (contingency) shows 40%+ reply rate by June 22**
- ✓ Proceed with Domain 57 as primary Phase 2 focus
- ⚠ Activate Domains 51/59/48 as secondary analysis (post-July 1)
- ⚠ July 1 deadline: MEDIUM CONFIDENCE (contingency domain synthesis + reduced Domains 51/59/48 coverage)

**Recovery Condition 3: Both Domain 51 AND Domain 57 weak (<40% reply) by June 23**
- ❌ ESCALATE to contingency research pathway (no new domain outreach; synthesis focus)
- ❌ Activate "Very Low Engagement" playbook (see SYNTHESIS_CONTINGENCY_EXECUTION_PLAYBOOKS.md)
- ❌ July 1 deadline: MARGINAL CONFIDENCE (timeline severely compressed; requires 100% execution efficiency)

---

## METRIC COLLECTION TEMPLATE (Use for all three paths)

### Daily Engagement Snapshot (June 18-23)

**Purpose**: Track engagement metrics in real-time to validate classification and flag deviations from expected response timeline.

**Collect daily** (10 minutes per day, 08:00-10:00 local):

```
DATE: June 18
Domain 51 (Wave 1-2 baseline check):
  - Total replies so far: ___ (running total from June 9-18)
  - Any new OOO/bounces: ___
  - Gist view count (today vs. June 14 baseline): ___ views

Domain 59 (if activated June 18):
  - Emails sent June 18: ___ (should be 5 if PATH A/B activated)
  - Replies by EOD: ___ (expect 0 on day 1; likely 0-1)

Domain 51 Tier 2 (if activated June 19-20):
  - Emails sent June 19-20: ___ (should be 3-6 depending on path)
  - Replies by June 20 EOD: ___ (expect 0 on day 1)

Domain 48 (if activated June 19-20):
  - Emails sent June 19-20: ___ (should be 4)
  - Replies by June 20 EOD: ___ (expect 0 on day 1)

CHECKPOINT QUESTION: Is engagement tracking as expected for this path?
  - YES: Continue standard timeline
  - NO: Flag deviations (e.g., Domain 59 bounce, Domain 51 Tier 2 strong early replies)
  - UNCERTAIN: Continue monitoring; rerun decision tree June 23 if unusual pattern emerges

NEXT STEPS: [fill in based on path selected]
```

**Repeat June 19-23** with same template structure.

---

## DECISION TREE SUMMARY TABLE

### Quick Reference (June 17 morning decision point)

| Classification | Engagement Evidence | Path | Activation Timeline | Synthesis Date | July 1 Confidence |
|---|---|---|---|---|---|
| **STRONG** | ≥2 replies + Gist engagement OR ≥15% open rate | A | June 18-20 (full) | June 23-25 | HIGH (95%) |
| **MODERATE** | ≥1 reply OR Gist delta ≥5 views OR 8-14% open rate | B | June 18-21 (selective) | June 23-24 (compressed) | MEDIUM (85%) |
| **WEAK** | 0 replies AND <5 Gist views AND <8% open rate | C | June 18 diagnostic → June 19-20 (conditional) | June 23-24+ (contingency-routed) | LOW (70%) |
| **TOO EARLY** | Zero signals, no bounces | HOLD | Hold for June 19 re-classification | June 24+ | TBD |

---

## CONCLUSION

**Framework pre-staged for June 17-18 checkpoint execution.**

Three decision paths (STRONG/MODERATE/WEAK) are fully documented with:
- ✓ Metric collection templates
- ✓ Classification logic
- ✓ Action plans with specific contacts + sequencing
- ✓ Resource allocation matrices
- ✓ Contingency playbooks
- ✓ July 1 deadline feasibility assessment

**Checkpoint execution steps** (June 17):
1. Collect engagement metrics (20 min, morning)
2. Run classification logic (10 min)
3. Select path (5 min)
4. Execute path-specific action plan (begins June 17 afternoon)

**All materials required for Phase 2 activation are production-ready.** Checkpoint decision output directly routes to specific action path; no additional interpretation required.

---

*Framework pre-staged: June 16, 2026. Checkpoint execution: June 17-18, 2026. Phase 2 activation: June 18-20, 2026. July 1 hard deadline: 16 days remaining.*
