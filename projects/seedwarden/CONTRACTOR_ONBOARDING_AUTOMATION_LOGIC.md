---
title: "Contractor Onboarding Automation Logic — Response Routing, Per-Track Workflows, and Payment Automation"
date: 2026-06-28
version: 1.0
status: production-ready
activation: June 28, 2026 (contractor responses due EOD)
response-deadline: June 28, 2026 EOD
onboarding-window: June 29–30, 2026 (upon ACCEPT confirmation)
sprint-start: June 29, 2026 (adjusted from June 22 slip)
finish-line: July 13, 2026 (best-case); July 15–17 (moderate); July 20+ (worst-case)
cross-references:
  - PHASE_3_CONTRACTOR_DECISION_TREE.md (original decision tree, solo fallback)
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo timeline, cascade logic)
  - PHASE_3_CONTRACTOR_ONBOARDING_WORKFLOW.md (6-phase lifecycle, onboarding kit)
  - PHASE_3_CONTRACTOR_ONBOARDING_INTEGRATION_CHECKLIST.md (marketing integration)
  - PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md (ready-to-send email templates)
  - PHASE_3_CONTRACTOR_SUCCESS_DASHBOARD.md (tracking grid, budget columns)
tags: [seedwarden, phase-3, contractor, onboarding, automation, routing, payment]
---

# Contractor Onboarding Automation Logic

**Prepared**: June 28, 2026
**Purpose**: Decision-automation playbook for processing contractor responses arriving today (June 28 EOD). Covers three response categories — ACCEPT, CONDITIONAL, ESCALATE — with per-contractor-type onboarding paths, weekly sync cadence, and payment automation specs. Every branch is deterministic: no "use judgment" nodes.

---

## Section 1 — Response Classification Decision Tree

When a contractor response arrives, classify it into one of three categories before taking any action. The classification must happen within 2 hours of message receipt.

```
RESPONSE ARRIVES (June 28, any time through EOD)
  |
  +-- Read the response and answer: Do they explicitly confirm availability for June 29 start?
          |
          YES, confirmed — "I can start [date on or before July 1]" or equivalent
          +-- ACCEPT pathway (Section 2)
          |
          MAYBE / CONDITIONAL — "I can start but need to confirm X" or "I'm interested but..."
          +-- CONDITIONAL pathway (Section 3)
          |
          NO / SILENCE — No response received by June 28 23:59 UTC, or explicit decline
          +-- ESCALATE pathway (Section 4)

ADDITIONAL CLASSIFICATION CHECK (for ACCEPT responses only):
  |
  +-- Does the acceptance include a rate confirmation at or below the agreed ceiling?
          |
          YES — rate confirmed within ceiling
          +-- Full ACCEPT: proceed directly to Day 1 onboarding
          |
          NO — rate not confirmed or requests adjustment
          +-- Treat as CONDITIONAL: clarification required before onboarding
```

**Classification log**: Record classification in WORKLOG.md within 2 hours of each response. Format:
```
[Contractor Name] — [Track] — Response received [DATE/TIME]
Classification: ACCEPT / CONDITIONAL / ESCALATE
Notes: [one sentence on the specific response content]
Action taken: [first action within the pathway]
```

---

## Section 2 — ACCEPT Pathway

### Trigger Condition
Contractor responds on or before June 28 EOD with unambiguous availability confirmation and rate agreement.

### Immediate Actions (within 4 hours of ACCEPT response)

1. **Reply confirmation email** — use Template 1 from `PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md`, customized with:
   - Specific first deliverable date (see per-track schedule below)
   - Onboarding kit delivery window ("You will receive the full onboarding kit within 24 hours")
   - Contract signature request ("Please reply to confirm you have received this and I will send the contract by [SAME DAY + 4hrs]")

2. **Send contract within 4 hours** — email contract PDF with:
   - Work-for-hire clause
   - Exact deliverable list and word counts / image counts / review scope
   - Milestone payment schedule (25% / 25% / 25% / 25%)
   - FTC and CITES compliance expectations in plain language
   - Target signature date: June 29 by 12:00 UTC (same day or next morning)

3. **Log in WORKLOG.md**:
   ```
   [Contractor Name] — ACCEPT received [DATE/TIME]
   Contract sent: [TIME]
   Contract signature target: June 29 12:00 UTC
   Deposit amount: $[X] due on signature
   ```

### Contract Signature + Deposit Gate

**No onboarding kit is delivered until contract is signed and deposit is confirmed.** This is a hard gate — not a soft preference. The deposit protects both parties and confirms contractor commitment before onboarding overhead is invested.

If contractor does not return signed contract within 24 hours of sending:
- Send a single follow-up: "Following up on the contract I sent [DATE]. Please confirm receipt. Looking forward to working with you."
- If no response within 48 hours of original send: reclassify to CONDITIONAL (awaiting clarification) and route accordingly.

### Per-Track Onboarding Paths (post-signature)

#### Photographers

**Onboarding kit delivery** (within 24 hours of deposit confirmed):
- Shot list for Session 1 bundle (specify which bundle is first — Respiratory, Immunity, or Digestive based on manuscript readiness)
- Phase 3 Canva brand guidelines (hex codes, surface standards, lighting spec) from `PHASE_3_CANVA_DESIGN_SYSTEM.md`
- Technical specs: 2000×2000px minimum, sRGB, JPEG 80%+, 3-day edit turnaround
- File naming convention: `[bundle-slug]-[image-type]-[sequence].jpg`
- Etsy attribution protocol: photographer credited as "Photography by [Name] — [portfolio link]" in Etsy listing and any social posts using the images
- Session 1 scheduling: target shoot date within 5 days of contract signing (by July 4 latest for July 6 Respiratory launch window)

**Submission specs**:
- 5 approved images per session (not 5 submitted — 5 approved after any rounds)
- Shot types required per session: top-down flat-lay, 45-degree flat-lay, lifestyle-in-use, close-up botanical detail, inside-spread mockup
- Delivery method: shared Google Drive folder (`Seedwarden-Phase3-Photography/[Photographer-Name]/`)
- Edit turnaround: 3 calendar days from shoot to delivered edits
- Approval response from user: within 48 hours of delivery
- Reshoots: 1 reshoot per session included in flat rate; additional reshoots billed at 25% of session rate

**First milestone trigger**: Session 1 photos approved (user signs off in WORKLOG.md entry: "Session 1 — APPROVED [DATE]")

#### Writers

**Onboarding kit delivery** (within 24 hours of deposit confirmed):
- Content outline Google Doc (per-bundle section breakdown with word counts, species, and mandatory content elements)
- FTC Quick Reference one-pager (evidence-tier language standards, mandatory disclaimer positions, never-use claim list)
- CITES sidebar verbatim text for Goldenseal / Immunity bundle (paste-ready, do-not-paraphrase)
- Bundle/species clarification memo: which writer covers which bundles (clarifies Adrian White vs. Rebecca Lexa Immunity assignment ambiguity flagged in Item 132 audit — must be resolved before kickoff call)
- Word count reminders per bundle:
  - Respiratory Health: 3,600 words (Elderberry, Mullein, Echinacea ×2 species, Thyme; Introduction, Preparation Methods, Cross-Reference, Contraindications)
  - Immunity Support: 3,800 words (Echinacea condensed reference, Ashwagandha, Elderberry condensed reference, Goldenseal; Introduction, Preparation Methods, CITES sidebar, Contraindications)
  - Digestive Support: 3,600 words (Dandelion, Calendula, Lemon Balm, Ginger; Introduction, Preparation Methods, Cross-Reference, Contraindications)
- Delivery format: Google Doc, shared to user's Google account before writing begins

**Word count enforcement**:
- First draft minimum: 85% of bundle word count target (e.g., Respiratory minimum 3,060 words)
- Drafts below 85% returned for completion before user review begins — this is not a revision round, it is a delivery shortfall
- Each milestone payment is contingent on delivery above the 85% threshold AND FTC compliance review pass

**First milestone trigger**: Respiratory first draft delivered, at 3,060+ words, FTC compliance reviewed and passed

#### Habitat Specialists

**Onboarding kit delivery** (within 24 hours of deposit confirmed):
- Field schedule proposal request: "Please send your available field survey dates for July 1–20. We need habitat observation notes for [SPECIES LIST — confirm against PHASE_3_CONTRACTOR_SELECTION_SCORECARD.md]."
- Permission forms checklist:
  - USDA Forest Service permit (if applicable for field collection in national forest)
  - State natural heritage program notification (if species is state-listed)
  - Private land access form (if scouted locations require landowner consent)
  - United Plant Savers At-Risk species protocol acknowledgment (mandatory for Echinacea angustifolia and Goldenseal observations)
- Regional accuracy scope: specify exact bundles and species sections requiring habitat review (e.g., "You are reviewing the habitat and range accuracy sections for Echinacea purpurea and E. angustifolia across the Respiratory and Immunity bundles")
- Source citation protocol: each habitat claim cites one of: USDA PLANTS database, NatureServe, iNaturalist verified observations, or UpS At-Risk species documentation
- Delivery format: annotated Google Doc comments on the writer's draft, or separate habitat notes document (user preference: comments on draft)

**First milestone trigger**: First scoped section delivered with primary source citations confirmed

---

## Section 3 — CONDITIONAL Pathway

### Trigger Condition
Contractor responds on or before June 28 EOD but includes a condition, question, or scheduling ambiguity that must be resolved before onboarding can begin.

### Common CONDITIONAL patterns

| Response type | Example | Resolution action |
|---|---|---|
| Date uncertainty | "I can probably start June 29 but need to confirm one other project" | Schedule a 15-minute clarification call within 24 hours |
| Rate question | "I'd like to discuss the per-bundle rate vs. flat rate" | Send rate clarification email; cap negotiation to 1 round |
| Scope question | "Can you confirm which bundles I would be covering?" | Send scope clarification email within 2 hours |
| Tool access request | "I'd need access to the content outlines before I can confirm" | Send outlines + offer conditional contract within 24 hours |
| Partial availability | "I can cover Respiratory and Immunity but not Digestive" | Evaluate partial engagement; see Partial Acceptance sub-section |

### Clarification Call Protocol

**Trigger**: Any CONDITIONAL response that cannot be resolved in 1 email exchange.

**Format**: 15-minute video or phone call. No written call agenda required — clarification calls are focused on one decision.

**Scheduling**: Offer 3 time slots within the next 36 hours. Do not let clarification calls push past June 30 — if a contractor cannot confirm by June 30, reclassify to ESCALATE.

**Call objective**: Exit the call with a yes or no. If the contractor's condition is something you can meet (minor scope adjustment, tool access, payment method change): agree on the call and confirm via email immediately after. If the condition is something you cannot meet (rate above ceiling, unavailable for July launch): politely decline on the call and activate backup options.

**Post-call log** (WORKLOG.md):
```
[Contractor Name] — Clarification call [DATE/TIME]
Condition: [What they needed clarified]
Resolution: ACCEPTED with [adjustment] / DECLINED — condition unmeetable
Next action: [Send contract / Activate ESCALATE pathway]
```

### Partial Acceptance Sub-Section

If a photographer or writer accepts part of the scope but not the full engagement:

**Photographer accepts 1–2 sessions, not 3**: This is viable. Assign Session 1 and Session 2 to the accepting photographer; source a second photographer for Session 3 via Upwork with a compressed brief (same specs, 3-day turnaround, single session). Adjust the flat rate contract to reflect the reduced session count.

**Writer accepts 1–2 bundles, not 3**: This is viable if the covered bundles are Respiratory and Immunity (highest-risk content). Digestive is the lowest-risk bundle — if uncovered, it can be moved to solo fallback (user writes Digestive at a later date per the solo fallback schedule in `PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md`). If a writer only accepts Digestive: evaluate whether a single-bundle contract for Digestive is worth the onboarding cost; usually it is not.

**Habitat specialist accepts partial species coverage**: Acceptable if the critical species are covered (Echinacea angustifolia At-Risk status, Goldenseal CITES notes). Log uncovered species in WORKLOG.md; user reviews those sections with primary sources before upload.

### CONDITIONAL to ACCEPT Conversion

Once the clarification condition is resolved and the contractor confirms:
- Log reclassification: "[Contractor Name] — CONDITIONAL converted to ACCEPT [DATE/TIME]. Condition resolved: [what changed]."
- Proceed immediately to ACCEPT pathway (Section 2). Do not delay — every day between confirmation and contract signing is a day the contractor has no commitment to the project.

### CONDITIONAL Deadline: June 30 EOD

If a CONDITIONAL contractor has not confirmed or declined by June 30 EOD:
- Send a single final prompt: "We need to confirm our contractor team by June 30 EOD to maintain our July 6 first deliverable date. Are you able to confirm your participation today?"
- If no response by June 30 23:59 UTC: reclassify to ESCALATE. Log in WORKLOG.md.

---

## Section 4 — ESCALATE Pathway

### Trigger Conditions

ESCALATE activates under any of these conditions:
1. Zero responses received by June 28 23:59 UTC (full-team no-response)
2. All respondents declined explicitly
3. All respondents are CONDITIONAL and have not converted to ACCEPT by June 30 EOD
4. Responses received but no candidate clears the vetting floor (rate above ceiling AND score below 60 AND no negotiation route)

### ESCALATE does not mean failure. It means the primary roster is insufficient and the backup activation sequence fires.

### Escalation Sequence (activate in order; do not skip steps)

**Step 1 — Toptal intake (June 28 EOD or June 29 first hour)**

- Open Toptal intake at toptal.com
- Complete the talent request form specifying:
  - Role type: Freelance botanical content writer (or photographer — specify per gap)
  - Timeline: Start available July 1; first deliverable July 8
  - Scope: 3 medicinal herb bundle manuscripts, 11,000 words total, FTC compliance required
  - Budget ceiling: $1,350 for writer, $1,050 for photographer (3 sessions)
- Toptal match turnaround: 48–72 hours. This means a match by July 1–2 if intake submitted June 28–29.
- Log: "Toptal intake submitted [DATE/TIME]. Expect match by [DATE]."

**Step 2 — Upwork emergency listing (June 29, within 4 hours of ESCALATE classification)**

- Post a secondary Upwork listing with revised framing:
  - Title: "Experienced Botanical / Herbal Medicine Writer — 3 Digital Guide Bundles, July Start"
  - Description: More specific than the original listing — name the exact bundles (Respiratory, Immunity, Digestive), word counts (3,600 / 3,800 / 3,600), and first delivery date (July 8)
  - Budget: "Fixed price, $1,000–$1,350 for full scope; milestone-based payment"
  - Availability filter: Must confirm July 1 availability in their proposal
- Second Upwork photographer listing (if photographer track is unresolved):
  - Title: "Botanical Flat-Lay Photographer — 3 Sessions, Medical Herb Guides, July"
  - Budget: $150–$350/session, 3 sessions
  - Location: No restriction — remote delivery (shipped specimens) is acceptable for flat-lay sessions

**Step 3 — Activate solo fallback track (June 29, parallel to Steps 1 and 2)**

Per `PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md` Section 6:
- Log in WORKLOG.md: "ESCALATE pathway active [DATE]. Contractor responses insufficient. Solo fallback track activating alongside external search. If no contractor confirmed by July 3 EOD, solo fallback is the operative plan."
- The July 3 EOD gate replaces the original June 17 hard deadline — it is recalibrated because the sprint has already slipped from June 22 to June 29. A contractor signed by July 3 still has 3 days before the July 6 Respiratory writing deadline.
- Begin solo writing preparation immediately: Women's Health upload (which has zero flex) still targets July 6 launch window regardless of contractor outcome.

**Step 4 — Herbalist Academy + AHG direct contact (June 29–30)**

- Email Herbal Academy partnerships inbox: request referral to certified herbalists available for July freelance content work
- Email AHG member services directly: same referral request, framing as "we are looking for RH or AHG-credentialed writers for a 6-week digital guide project starting July 1"
- Log both outreach attempts in WORKLOG.md with date and contact email used

**Step 5 — Hard decision gate (July 3 EOD)**

If no contractor is confirmed by July 3 EOD (contract signed + deposit paid):
- Solo fallback is the confirmed operative plan
- Stop all contractor search activity
- Log: "July 3 EOD — No contractor confirmed. Solo fallback confirmed. Per PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md. No contractor engagement after this date."
- Do not attempt to engage a contractor after July 3 — the onboarding cost and alignment risk on a July 3+ start contractor exceeds the benefit.

---

## Section 5 — Weekly Sync Cadence

### Full Team Sync — Mondays, 14:00–15:00 UTC

**Frequency**: Weekly, every Monday starting the first week after onboarding (Week 1 = June 30 – July 6)

**Participants**: All active contractors across all tracks (photographer, writer, habitat specialist)

**Format**: Video call (Google Meet or Zoom). Maximum 60 minutes. Not optional — if a contractor cannot attend, they send a written update by Sunday 20:00 UTC (format: status, blockers, next-week plan).

**Agenda structure** (fixed, do not deviate):

| Segment | Duration | Owner |
|---|---|---|
| Week review — each contractor shares status in 3 min or less | 15 min | Each contractor |
| Blockers round — anything preventing delivery this week | 10 min | All |
| Cross-track dependencies — do any photo needs block writers? | 10 min | User moderates |
| FTC / quality flags from last week's reviews | 10 min | User |
| Next week priorities — each contractor confirms their week's delivery target | 10 min | Each contractor |
| Close | 5 min | User |

**What gets logged after each Monday sync** (WORKLOG.md):
```
## Monday Sync — [DATE]
Attendees: [list]
Status summary:
  - [Photographer Name]: [deliverable status]
  - [Writer Name]: [word count / bundle status]
  - [Specialist Name]: [section status]
Blockers raised:
  - [List any]
Resolutions:
  - [List actions taken or committed]
Next week's delivery targets:
  - [Per contractor]
```

### Specialty Group Check-Ins — Thursdays, 30 minutes per group

**Purpose**: Shorter, track-specific working session. No cross-track presence needed.

**Photographer slot**: Thursday 13:00–13:30 UTC
- Agenda: Image delivery review, reshoot flagging, Canva integration questions, brand guideline clarifications
- Decision authority: user approves or flags images during this call; approved images immediately available for Etsy listing integration

**Writer slot**: Thursday 14:00–14:30 UTC
- Agenda: Section progress check, FTC language review of any flagged passages, species accuracy questions, cross-bundle reference coordination (Echinacea treatment across Respiratory and Immunity, Lemon Balm treatment across Sleep and Digestive)
- Decision authority: user resolves any FTC framing questions; mandatory contraindication language is confirmed verbatim

**Habitat Specialist slot**: Thursday 15:00–15:30 UTC
- Agenda: Field observation status, source citation review, annotation delivery on writer drafts
- Decision authority: user confirms regional accuracy additions are incorporated before upload

**Thursday no-show protocol**: If a contractor misses a Thursday slot without advance notice:
- Email same day: "We missed you today — please send a written update by [Thursday + 24 hours]"
- If second consecutive Thursday no-show without notice: treat as a dropout signal; activate dropout recovery procedure from `PHASE_3_CONTRACTOR_DECISION_TREE.md` (Mid-Sprint Dropout Procedure)

---

## Section 6 — Payment Automation Specs

### Milestone Architecture

All contractors operate on the same 4-milestone payment structure regardless of track. Milestones are tied to deliverable acceptance, not calendar dates.

| Milestone | Trigger | Amount (standard) | Method | Timeline |
|---|---|---|---|---|
| M1 — Deposit | Contract signed | 25% of flat rate | PayPal / Wise / Venmo | Within 3 days of signature (on or before July 1) |
| M2 — First deliverable | First deliverable accepted | 25% of flat rate | Same as M1 | Within 3 business days of acceptance |
| M3 — Second deliverable | Second deliverable accepted | 25% of flat rate | Same as M1 | Within 3 business days of acceptance |
| M4 — Final handoff | All deliverables accepted, revisions complete | 25% of flat rate | Same as M1 | Within 3 business days of final acceptance |

### Milestone Alignment to Bundle Upload Schedule

The milestone dates below are tied to the bundle upload schedule. They are not independent contractor deadlines — they are the upstream gates for each bundle going live.

| Milestone | Date | Photographer trigger | Writer trigger | Specialist trigger |
|---|---|---|---|---|
| M1 (Deposit) | July 1, 2026 | Contract signed | Contract signed | Contract signed |
| M2 (First deliverable) | July 8, 2026 | Session 1 approved | Respiratory draft approved | First species sections approved |
| M3 (Second deliverable) | July 15, 2026 | Session 2 approved | Immunity draft approved | Second species sections approved |
| M4 (Final handoff) | July 27, 2026 | Session 3 approved + reshoots clear | Digestive final + all revisions | All annotations complete |

**Note**: July 27 M4 date for all tracks provides a 7-day buffer before the August 3 Digestive listing goes live on Etsy. Do not compress this buffer — it accommodates final PDF QA, Etsy listing draft, and upload scheduling.

### Payment Execution Checklist (per milestone)

Before releasing any milestone payment:
- [ ] Deliverable received and logged in WORKLOG.md
- [ ] FTC compliance review passed (writers and specialists only — photographers: brand compliance check)
- [ ] Word count / image count at or above threshold
- [ ] CITES sidebar present and unedited (Immunity bundle only)
- [ ] User has signed off: "[Deliverable] approved. Payment releasing [DATE]."
- [ ] Payment sent via agreed method
- [ ] Payment confirmed received by contractor (reply email or platform confirmation)
- [ ] WORKLOG.md updated: "M[X] payment — $[amount] — sent [DATE] — confirmed received [DATE]"

### International Payment Protocol

For contractors based outside the US (common for AHG-credentialed herbalists in Canada, UK, and Australia):
- Preferred method: Wise (lower fees than PayPal for international transfers under $1,000)
- Acceptable: PayPal international, Upwork platform payment
- Not used: Wire transfer for amounts below $500 (fees erode project economics)
- Log currency if non-USD: "M1 payment — [USD amount] / [local currency equivalent at send date]"

### Dispute / Withholding Protocol

If a contractor delivers work that fails the FTC compliance review or is below the 85% word count minimum:
- Do not release the milestone payment
- Send within 24 hours: "Thank you for the delivery. Before I release this milestone, we need [specific correction]. Here is what is missing: [list]. Please return a revised draft by [DATE — 72 hours maximum]."
- If the contractor disputes the revision request: do not argue; send a copy of the FTC Quick Reference and the content outline showing the mandatory element. The mandatory element is a contractual deliverable.
- If the contractor delivers a compliant revision within 72 hours: release payment immediately.
- If the contractor does not respond within 72 hours: treat as a dropout signal. Activate mid-sprint dropout procedure.

---

*Prepared: June 28, 2026. Cross-references: PHASE_3_CONTRACTOR_DECISION_TREE.md (original decision logic), PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (solo fallback activation and cascade logic), PHASE_3_CONTRACTOR_ONBOARDING_WORKFLOW.md (6-phase lifecycle), PHASE_3_CONTRACTOR_COMMUNICATION_TEMPLATES.md (email templates). Version 1.0.*
