---
title: "Phase 3 Risk Assessment Update — May 26 Pre-Decision Window"
date: 2026-05-26
status: decision-ready — May 30 user gate
phase: Phase 3 pre-sprint risk review
purpose: >
  Updates the PHASE_3_LAUNCH_RISK_REGISTER.md (v1.0, May 21) for the May 26-30 decision
  window. Identifies the highest-risk items requiring user decision by May 30, flags any
  supplier risks that could impact the June 22 launch, and adds two new risks identified
  from the May 26 supplier verification pass. Intended as the risk input to the May 30
  scope decision.
source-documents:
  - PHASE_3_LAUNCH_RISK_REGISTER.md (v1.0, May 21 2026)
  - PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.md (v5.0, May 22 2026)
  - PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.csv (May 26 2026 update)
  - PHASE_3_PRODUCTION_TIMELINE_SKELETON.csv (May 26 2026)
decision-deadline: May 30, 2026
sprint-start: June 22, 2026
days-to-sprint-start: 27
tags: [seedwarden, phase-3, risk-assessment, risk-register, may-30, supplier, launch-risk]
---

# Phase 3 Risk Assessment Update
## May 26 Pre-Decision Window — For May 30 User Gate

**Prepared**: May 26, 2026
**Days to sprint start**: 27 (June 22)
**Purpose**: Identify and rank risks requiring user decision by May 30. The May 21 risk
register is incorporated by reference — this document focuses on delta items and updated
severity assessments based on May 22-26 supplier intelligence.

**Risk scoring unchanged from v1.0**: Probability: 1 = Low (15-25%), 2 = Medium (30-45%),
3 = High (50%+). Impact: 1 = Low, 2 = Medium, 3 = High. Score = P x I.

---

## Section 1: Highest-Risk Items for May 30 Decision Window

These are the items where a May 30 user decision materially reduces risk. Ordered by
combined score and time urgency.

---

### Risk Update 1 — AHG Peer Reviewer Not Secured (Unchanged from v1.0 — Priority Elevated)

**Original risk**: A-5 in PHASE_3_LAUNCH_RISK_REGISTER.md
**Current status as of May 26**: NO CHANGE — reviewer outreach not yet initiated
**Score**: P=2, I=3, Score=6. Highest-severity pre-sprint risk in the register.

**Why this requires May 30 action**:
The AHG outreach calendar in the risk register (June 8 first contact, June 15 follow-up)
assumes a 2-week response window. If the first outreach email is sent June 8, the earliest
any reviewer can confirm is June 22 — sprint Day 1 — with no margin for back-and-forth.
Moving the first outreach contact from June 8 to June 1 (or even May 30) adds 8 days of
response margin before the June 22 sprint start. This is the single change that most
improves the probability of having a reviewer quote on the Women's Health listing when it
goes live June 29.

**May 30 action required**:
Draft the AHG outreach email during the May 30 review session (template in
`PHASE_3_PEER_REVIEWER_RECRUITMENT_PLAYBOOK.md`). Send it no later than June 1.
Do not wait for June 8. Target: 8 AHG-directory RH practitioners with Women's Health
filter. Attach 400-word Black Cohosh excerpt. Request 15-minute review for listed credit.

**If no reviewer by June 22**: Sprint starts as planned. Women's Health lists June 29 without
reviewer quote. Continue outreach through July 13. Add quote retroactively before AHG
Symposium campaign activates July 28. Do not delay sprint.

**Score delta**: Unchanged at 6. Urgency elevated — action window is now.

---

### Risk Update 2 — Scope Decision Not Made by May 30 (NEW — Score: P=2, I=3, Score=6)

**Status**: NEW RISK identified May 26. Not in v1.0 register.

**Description**: The May 30 scope decision (Option A: 5 bundles, Option C: 3 bundles) is
the single biggest structural lever available before the June 22 sprint start. If this
decision is not made by May 30, it defaults to Option C (per the auto-lock provision in
`PHASE_3_IMPLEMENTATION_ROADMAPS_DETAILED.md`) on June 1. The auto-lock is the correct
fallback — the risk is that the user does not review the decision matrix before the auto-lock
activates, meaning the decision was made by default rather than by analysis.

**Impact of undecided scope entering June 1**:
- Option C (3 bundles) activates automatically and is the correct scope under most
  write-pace assumptions
- The user loses the option to select Option A (5 bundles) without re-opening the decision
  after June 1, which compresses the pre-sprint setup window
- The AHG outreach and Canva brand kit setup cannot be optimally scoped without knowing
  whether 3 or 5 bundle covers are being produced

**May 30 action required**:
Review `PHASE_3_DECISION_MATRIX_V2.md` (Option A vs. C comparison, cost and revenue by
scope). Select one option. Log the decision in WORKLOG.md using the decision record template
in `PHASE_3_DECISION_MATRIX_V2.md` Section 5. This takes approximately 20-30 minutes.

**Score**: P=2 (decision may slip given other May 30 launch priorities), I=3 (a non-decision
defaults to Option C, which is correct — but the user loses the structured analysis window).

---

### Risk Update 3 — Mountain Rose Herbs Dried Herbs — Individual SKU Status Unconfirmed (UPDATED — Score: P=2, I=2, Score=4)

**Original risk**: C-1 in PHASE_3_LAUNCH_RISK_REGISTER.md (MRH order delay)
**Status update**: Risk scope widened. The May 21 register addressed delivery delay (MRH
order ships but arrives late). The May 26 supplier verification found that while Goldenseal
root and Black Cohosh root are confirmed out of stock, individual SKU status for the seven
sprint herbs has NOT been phone-verified or email-confirmed as of May 26.

**Specific gap**: The PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.csv shows `[CONFIRM stock before
ordering]` on each of the seven sprint herbs at Mountain Rose Herbs. The May 22 stockout
check was scoped to Goldenseal and Black Cohosh. Lavender, Mullein, Lemon Balm, and
Passionflower at MRH have not been individually confirmed in stock.

**Why this matters for May 30 window**:
If any sprint herb at MRH is also out of stock (low probability, but possible for Mullein
leaf and Passionflower herb, which are lower-volume products), the June 15 order cannot be
placed without a backup plan. Frontier Co-op is the confirmed fallback for all species, but
the Frontier Co-op backup order deadline would be June 13 (not June 15) due to slightly
longer transit times.

**May 30 action required**:
Email mountainroseherbs.com customer service or call to confirm in-stock status on these
seven SKUs: Elderberry (dried whole), Echinacea purpurea root, Lavender flower, Lemon Balm
leaf, Mullein leaf, Passionflower herb, Valerian root. Record responses in
PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.csv (Verification Timestamp column). This takes
approximately 15 minutes (website check) or 30 minutes (phone confirmation).

**Score delta**: Unchanged at 4. Urgency increased because individual SKU confirmation has
not been done and the June 15 order window is 20 days away.

---

### Risk Update 4 — Canva Palette Not Confirmed in WORKLOG.md (UPDATED — Score: P=2, I=1, Score=2)

**Original risk**: C-3 in PHASE_3_LAUNCH_RISK_REGISTER.md
**Status update**: Confirmation has NOT been logged in WORKLOG.md as of May 26. The auto-lock
provision means this is not a blocking risk — palette locks to the six production hex codes
on June 15 regardless. But the May 30 window is when the user has context to review the
palette alongside the scope decision, making it the most efficient moment to confirm or modify.

**Impact if not confirmed by May 30**:
Zero on sprint execution (auto-lock covers it). Low impact on design quality (production
hex codes are the designed Phase 3 palette). The only lost opportunity is a palette
customization if the user had a preference.

**May 30 action required**: 5-minute entry in WORKLOG.md (see `PHASE_3_CANVA_STAGING_CHECKLIST.md`
Section 1 for exact template text). Confirm or modify the six hex codes.

**Score**: P=2 (low urgency, easy action, often deferred), I=1 (auto-lock covers the gap).

---

### Risk Update 5 — Strictly Medicinal Seeds Outreach Not Sent (NEW — Score: P=2, I=2, Score=4)

**Status**: NEW RISK identified May 26. Not in v1.0 register.

**Description**: Per `PHASE_3_SUPPLIER_CONFIRMATION_EXECUTION_SUMMARY.md` (May 26), the
inquiry email to Strictly Medicinal Seeds (info@strictlymedicinalseeds.com) for Echinacea,
Passionflower, and Valerian transplant availability was listed as a May 26 action item. As
of the current session, the email status in the tracker shows `[FILL]` — not confirmed sent.

The Strictly Medicinal supplier confirmation is the input to two June 22 Tier 3 orders:
Echinacea purpurea transplant and Passionflower transplant (for post-launch v1.1 photography).
These are not sprint-blocking — Wikimedia CC covers both species for v1.0 launch. But if the
June 22 order is placed without a stock confirmation, there is a 20-30% chance of a backorder
or unavailability response, which delays the v1.1 photography upgrade to August-September.

**May 30 action required**:
Send the inquiry email to info@strictlymedicinalseeds.com. Template is in
`PHASE_3_SUPPLIER_OUTREACH_LOG.md`. Key questions: (1) Echinacea purpurea transplant stock
for June 22 order? (2) Passionflower transplant stock for June 22 order? (3) Valerian
transplant stock for June 22 order? Expected response time: 2-3 business days.

**Score**: P=2, I=2, Score=4. Urgency: send by May 27 to get a response before June 1.

---

### Risk Update 6 — Prairie Moon Elderberry Summer Stock Unconfirmed (UPDATED — Score: P=2, I=2, Score=4)

**Original risk**: C-1 variant in v1.0 register (general supplier delay)
**Status update**: Prairie Moon Elderberry summer availability is flagged as `UNCERTAIN`
in `PHASE_3_SUPPLIER_CONFIRMATION_TRACKER.csv` because Prairie Moon's spring shipping season
closed. Elderberry is a different species from Goldenseal and Black Cohosh (not in the
confirmed stockout list), but summer availability for Sambucus shrubs has not been confirmed
by phone or website check as of May 26. The June 15 Elderberry order deadline depends on
this confirmation.

**Why this matters more now**:
The local nursery fallback is the most reliable Elderberry source (2-gallon potted Sambucus
shrubs are standard inventory at garden centers spring through July). But Elderberry for the
studio photography session (June 17-21) needs to be ordered by June 15 regardless of source.
If Prairie Moon's website does not confirm summer stock by June 1, the local nursery path
must be activated without waiting for Prairie Moon to respond.

**May 30 action required**:
Add a June 1 calendar reminder: check prairiemoon.com for Sambucus nigra or S. canadensis
2-gallon availability. If not showing in-stock by June 1: pivot to local nursery immediately.
No further decision needed now — just confirm the June 1 check is scheduled.

**Score**: Unchanged at 4 (local nursery fallback is highly reliable). Urgency: June 1
is the decision point, not May 30. Log the June 1 check as a calendar item during May 30 review.

---

## Section 2: Risk Items That Have Resolved Since v1.0

These risks from the May 21 register have been resolved by May 26 intelligence:

### Resolved — Path 1 Live Goldenseal Ambiguity

**Original risk status** (May 21): Path 1 was "preferred" with uncertainty about supplier
availability.
**Resolved**: May 22 stockout confirmation eliminated Prairie Moon and Crimson Sage as Path 1
sources. Path 2 (Wikimedia CC) is now confirmed as the only zero-risk path. Decision is
pre-selected — user need only log "Goldenseal Path 2 confirmed" in WORKLOG.md by June 8.
NativeWildflowers.net is available if Path 1 is desired, but the financial and schedule
case for Path 2 is conclusive.

**Action remaining**: Log Path 2 confirmation in WORKLOG.md before June 8 (zero float).
This is a 2-minute action, not a decision.

### Resolved — Black Cohosh Source Ambiguity

**Original risk status** (May 21): No confirmed NOW-shipping source for Black Cohosh.
**Resolved**: NativeWildflowers.net confirmed in-stock bareroot at $5.99, ships immediately.
May 25 order = June 1-7 arrival. iNaturalist CC-BY confirmed as zero-cost fallback with
excellent Appalachian population coverage.

**Action remaining**: Place order at NativeWildflowers.net by May 27 if live specimen is
desired for pre-sprint photography window. This is optional — iNaturalist CC-BY is
sufficient for v1.0 launch without any live plant.

### Resolved — Canva Design System Palette Discrepancy

**Original risk status** (implied in prior Canva docs): A palette discrepancy was noted
between older documents and the authoritative May 19 adaptation guide.
**Resolved**: `PHASE_3_CANVA_DESIGN_SYSTEM.md` (May 20) explicitly declares the May 19
adaptation guide as authoritative and notes all older documents are superseded. The six
production hex codes are unambiguous. No design decision remains except user confirmation
in WORKLOG.md.

---

## Section 3: Impact on June 22 Launch if May 30 Decisions Are Delayed

| Decision | May 30 Deadline | Impact if Delayed to June 1-5 | Impact if Delayed Past June 5 |
|---|---|---|---|
| Option A vs. C scope selection | May 30 | Option C auto-locks June 1 — correct default but user loses analysis window | No impact on sprint execution; Option C is the plan |
| AHG reviewer outreach initiated | May 30 (ideally) | Outreach sent June 8 — reviewer response arrives June 22, no pre-launch confirmation margin | Reviewer secured after Women's Health goes live July 29 — practitioner tier revenue ceiling through August |
| Palette confirmed in WORKLOG.md | May 30 (ideally) | Auto-lock June 15 — no sprint impact | Auto-lock June 15 — no sprint impact |
| Strictly Medicinal email sent | May 27 | Response arrives June 1-3 — June 22 order still viable | Response arrives after June 22 order deadline — order placed without confirmation (backorder risk) |
| Prairie Moon June 1 check scheduled | May 30 calendar item | No impact if check is still done June 1 | Elderberry order decision slips to June 5 — 10-day lead time puts arrival at June 15-19 (tight for June 17-21 studio) |
| MRH individual SKU confirmation | June 1-5 | Order can still be placed by June 15 | June 13 Frontier fallback order needed — adds $10-15 premium |

---

## Section 4: Risk Scorecard — May 26 Snapshot

| Risk | Score | Status | May 30 Action | Time to Act |
|---|---|---|---|---|
| AHG reviewer not secured (A-5) | 6 | OPEN — not initiated | Draft AHG outreach; send by June 1 | NOW |
| Scope decision not logged (NEW) | 6 | OPEN — not decided | Review decision matrix; log in WORKLOG.md | May 30 |
| MRH individual SKU unconfirmed (NEW) | 4 | OPEN | Email or call MRH to confirm 7 sprint herb SKUs in stock | May 30 or June 1 |
| SM outreach not sent (NEW) | 4 | OPEN | Send email to info@strictlymedicinalseeds.com | May 27 |
| Prairie Moon Elderberry (UPDATED) | 4 | OPEN | Schedule June 1 calendar check; pivot to local nursery if no confirmation | June 1 |
| Canva palette not confirmed (C-3) | 2 | OPEN — auto-lock June 15 covers it | Log palette confirmation in WORKLOG.md | May 30 (5 min) |
| Goldenseal path ambiguity | RESOLVED | Path 2 confirmed; log in WORKLOG.md by June 8 | 2-minute WORKLOG.md entry | Before June 8 |
| Black Cohosh source ambiguity | RESOLVED | NativeWildflowers.net confirmed; optional order by May 27 | Optional live specimen order | By May 27 if desired |
| Canva palette discrepancy | RESOLVED | May 19 guide is authoritative | None | Complete |

---

## Section 5: Recommended May 30 Action Sequence (30-45 minutes total)

In priority order:

1. **Scope decision** (20 min): Review `PHASE_3_DECISION_MATRIX_V2.md`. Select Option A
   or C. Log in WORKLOG.md using the decision record template. This unlocks all downstream
   sprint planning.

2. **Palette confirmation** (5 min): Open WORKLOG.md. Add one line confirming or modifying
   the six Phase 3 hex codes. Done.

3. **AHG outreach initiation** (10 min): Open `PHASE_3_PEER_REVIEWER_RECRUITMENT_PLAYBOOK.md`.
   Identify 8 target practitioners. Draft outreach email or schedule it as a June 1 calendar
   action. Do not wait for June 8.

4. **Calendar item: June 1 Prairie Moon check** (2 min): Add a June 1 reminder to check
   prairiemoon.com Elderberry availability.

5. **MRH SKU confirmation** (15 min, can be done June 1): Email mountainroseherbs.com
   or check individual product pages for all 7 sprint herb SKUs. Note any out-of-stock
   items and activate Frontier Co-op order for those items by June 13.

6. **Goldenseal Path 2 log** (2 min): Log in WORKLOG.md: "Goldenseal Path 2 confirmed —
   Wikimedia CC images to download by June 8." This is the zero-float June 8 deadline item.

**Total time**: 30-45 minutes for all six actions. All of them are executable during the
May 30 decision session alongside the main Phase 2 launch review.
