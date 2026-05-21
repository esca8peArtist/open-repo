---
title: "Phase 3 Medicinal Herbs — Launch Risk Register"
date: 2026-05-21
version: 1.0
status: decision-ready
decision-deadline: May 30, 2026
execution-window: June 22 – July 13, 2026 (22 calendar days)
cross-references:
  - PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md (v6.0, Section 7)
  - PHASE_3_GANTT_TIMELINE.csv (contingency rows 66–71)
  - PHASE_3_SCOPE_DECISION_MATRIX.md
  - PHASE_3_RESOURCE_ALLOCATION_SCENARIOS.md
tags: [seedwarden, phase-3, risk-register, launch-risk, mitigation, kill-criteria]
---

# Phase 3 Launch Risk Register

**Prepared**: May 21, 2026
**Purpose**: Top risks per option with mitigation strategies, kill-criteria for further downscoping, and a go/no-go decision tree for the May 22–29 window. Grounded in the risk scoring matrix from PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md Section 7 and all six contingency rows in PHASE_3_GANTT_TIMELINE.csv.

**Risk scoring**: Probability 1 = Low (15–25%), 2 = Medium (30–45%), 3 = High (50%+). Impact 1 = Low, 2 = Medium, 3 = High. Score = P × I.

---

## Section 1: Top Risks — Option A (5 Bundles, Single Writer)

Option A carries the five highest-severity risks of any scope choice. All five are manageable through scope reduction — which is why Option C exists as the planned fallback.

### Risk A-1: Writing Pace Failure at June 24 Pace Gate

**Probability**: 2 (Medium — 35%). **Impact**: 2 (Medium). **Score**: 4.

**Description**: Women's Health writing falls below 2,500 words at EOD June 24 (sprint Day 3). The PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md pace targets require 5 focused hours of writing per day for Days 1–3 to reach this milestone. Any interruption — supplier coordination, photography setup, administrative tasks — cuts into writing time.

**Cascade if triggered**: Option A is no longer viable. Option C must be activated immediately. If activation is reactive (June 24) rather than proactive (May 30), three sprint days have already been run at Option A pace without the structural float that Option C preserves from Day 1. The pace gate protects the June 29, July 6–7, and July 13 upload dates — those dates remain intact after activation, but the writer enters Weeks 2–3 with higher accumulated fatigue than if Option C had been selected on May 30.

**Mitigation**:
- Primary: Select Option C on May 30. Eliminates pace pressure entirely.
- Secondary (if Option A is selected): Protect Days 1–3 writing time as non-negotiable. No supplier email, photography setup, or administrative tasks before 12pm on June 22–24. Writing sessions run 5 hours minimum before any other sprint activity.
- Tertiary: Reduce species per session. If Day 2 is running behind, compress Vitex (600 words) to 400 words and Red Clover to 250 words. Expand in v1.1 post-launch.

**Contingency trigger**: Women's Health below 2,500 words at EOD June 24. Log "Pace gate failed — Option C activated" in WORKLOG.md same day.

---

### Risk A-2: Week 1 Pace Unsustainable Beyond Day 3

**Probability**: 2 (Medium — 35%). **Impact**: 2 (Medium). **Score**: 4.

**Description**: Even if the June 24 pace gate is cleared, sustaining 5+ hours of focused writing per day through Days 4–7 (June 25–28) while Respiratory writing begins is the longest sustained writing push in Phase 3. Days 4–5 require Elderberry (800 words), Mullein (600 words), and Echinacea two-species comparison (600 words) — three of the most factually dense sections in Phase 3.

**Cascade if triggered**: Writing slips in Days 4–7 push the Respiratory self-edit and Women's Health PDF export into June 29–30, delaying the first upload from June 29 to July 1–2. A 2–3 day slip is recoverable (Respiratory still launches July 6–8; Sleep still launches July 13–16). A 5+ day slip compresses the Immunity writing window and pushes Sleep toward July 18–20.

**Mitigation**:
- Primary: Option C. Under Option C, Days 4–7 carry the same writing tasks but the writer knows Immunity and Digestive are explicitly not sprint-window bundles — no "must finish 5 bundles" pressure adds to the pace.
- Secondary: Day 6 (June 27) is designated the lighter day (4 hours, Thyme + WH self-edit). This is the natural recovery day in the sprint structure. Do not add writing tasks to Day 6 regardless of pace status.
- Tertiary: Women's Health PDF export can slip to June 29 morning (2-hour task) without impacting the June 29 upload. The upload checklist requires export complete before uploading, not the day before.

---

### Risk A-3: Canva Design Revision Loops

**Probability**: 2 (Medium — 30%). **Impact**: 2 (Medium). **Score**: 4.

**Description**: A cover session exceeds 2 hours on first attempt due to hero image selection, color correction, or template incompatibility. Under Option A, five covers must be complete by July 3 design lock. The Immunity cover (Goldenseal root or Ashwagandha hero, Deep Burgundy) has the highest revision risk — Goldenseal root images are less common in the CC library and may require multiple sourcing attempts.

**Cascade if triggered**: Each 2-hour cover overrun consumes float days that would otherwise absorb writing overruns. At 4 days of individual float per cover, a single overrun is absorbed easily. But concurrent overruns (cover overrun + writing overrun on the same day) stack and erode float from both tracks simultaneously.

**Mitigation**:
- Pre-stage 3–5 hero image candidates for each bundle before opening the Canva session. Select the hero offline (no Canva open) before starting the session.
- For Immunity cover specifically: pre-stage Ashwagandha root as the primary hero (superior CC library coverage vs. Goldenseal). Goldenseal becomes an optional accent image if a CC-licensed option is confirmed.
- If any cover exceeds 2 hours: switch immediately to Google Docs PDF fallback. Do not attempt a third revision cycle in-session. Guide content drives purchases, not cover design.
- Design lock July 3 EOD is absolute. No exceptions. Budget zero time for post-lock design changes.

---

### Risk A-4: FTC Compliance Gap Discovered in Review Pass (D18)

**Probability**: 1 (Low — 20%). **Impact**: 3 (High). **Score**: 3.

**Description**: The FTC compliance review pass on July 9 (D18) discovers an uncorrectable therapeutic claim in the Women's Health or Immunity bundle that was written under pace pressure. Under Option A, the high daily writing pace and strict word-count targets increase the probability of a compliant-sounding sentence slipping through that reads as a therapeutic claim without the required qualifying language.

**Cascade if triggered**: A confirmed non-compliant claim in Women's Health (which is already live by July 9) requires an immediate guide revision, PDF re-export, and Etsy listing re-upload. If the claim triggers an Etsy listing review or removal, the 72-hour discovery window for that listing is lost. Timeline impact: 24–48 hours to revise and re-upload. Revenue impact at 10 units/week: $22–$44 in lost sales during the correction window.

**Mitigation**:
- FTC Quick Reference table (PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md Appendix A) is open in a browser tab every writing session. Every therapeutic claim is reviewed against the table before the self-edit pass is complete.
- Women's Health and Immunity FTC passes are embedded in the writing schedule (D7 self-edit includes a mini FTC check). The D18 review is a final confirmation, not the first compliance pass.
- Defer D18 FTC review of Digestive and Respiratory (lowest-risk bundles) to post-launch v1.1 if Float Day 1 is consumed. Women's Health and Immunity cannot be deferred.
- The mandatory contraindication register (Vitex, Ashwagandha, Valerian, Passionflower, Lemon Balm) is pre-written in Appendix A of the critical path document and is pasted verbatim — not paraphrased — into each bundle.

---

### Risk A-5: AHG Peer Reviewer Not Secured (Practitioner Tier Revenue Ceiling)

**Probability**: 2 (Medium — 35%). **Impact**: 3 (High). **Score**: 6.

This is the highest-severity pre-sprint risk across all options (P=2, I=3, Score=6 — documented in PHASE_3_GANTT_TIMELINE.csv Row 19 and PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md Section 7).

**Description**: No AHG-credentialed reviewer confirms written accuracy review by June 21 (sprint Day 1). The Etsy listing for Women's Health goes live June 29 without a reviewer quote in the description.

**Cascade if triggered**: AHG directory cold outreach to $120–$150 practitioner tier converts at a fraction of the baseline rate without a named reviewer. The HERBALIST_NETWORK_ECOSYSTEM_MAPPING.md Section 7.3 documents the binary credibility filter: practitioners who scan the listing and do not see a reviewer credential skip immediately. This is not a sprint-window issue — it is a 6–12-week revenue ceiling that limits practitioner tier conversion from July 13 through the AHG Symposium (August 14–16) and beyond.

**This risk is equal across Options A and C.** Both options require the reviewer before June 22.

**Mitigation**:
- June 8: Email 8 AHG-directory RH practitioners (Women's Health filter). Attach 400-word Black Cohosh excerpt. Request 15-minute review for credit.
- June 15: Follow-up non-respondents. Expand to UpS practitioner network and Herbal Academy affiliate contact.
- June 21: If no reviewer confirmed, begin sprint as planned. Upload Women's Health June 29 without reviewer quote. Add retroactively when secured. Continue outreach through July 13 — at minimum, add reviewer quote before AHG Symposium campaign activates July 28.
- Do not delay sprint start for reviewer confirmation. This risk is a revenue ceiling, not a launch blocker.

---

## Section 2: Top Risks — Option C (3-Bundle Focus)

Option C has a substantially lower risk profile than Option A. The risks below apply to all options (AHG reviewer) or are specific to Option C's slightly extended Phase 4 handoff.

### Risk C-1: Supplier Delay — Mountain Rose Herbs Dried Herbs

**Probability**: 1 (Low — 20%). **Impact**: 2 (Medium). **Score**: 2.

**Description**: Mountain Rose Herbs order placed June 15 does not ship within 3–5 business days, missing the June 17–21 dried herb studio photography window.

**Cascade if triggered**: The dried herb flat-lay session (June 17–21) is delayed. Etsy listing image slots 2–4 use Wikimedia Commons CC-BY-SA images as primary content (already planned as fallback). The flat-lay session is rescheduled to sprint Week 1 (June 23–25). Writing takes priority over photography on any constrained day — photography is skipped if writing falls behind pace.

**Mitigation**:
- Place Mountain Rose Herbs order June 15 with standard shipping (3–5 business days).
- If not shipped by June 20: place Frontier Co-op emergency order same day (3–5 business day ship, comparable species coverage). Log in WORKLOG.md.
- Confirm Mountain Rose Herbs order status by email or phone on June 18 (3 days after order). Do not wait for automatic tracking update.

---

### Risk C-2: Goldenseal Photo License Delay (Path 2 Only)

**Probability**: 1 (Low — 20%). **Impact**: 1 (Low). **Score**: 1.

**Description**: NC Botanical Garden and Missouri Botanical Garden do not respond to photo license requests by the June 21 sprint start. Under Path 2 (Option C default), this is the planned free photo source for Goldenseal.

**Cascade if triggered**: Zero. Wikimedia Commons CC-BY-SA has direct Goldenseal coverage without institutional license. The botanical garden outreach is a quality upgrade, not a critical path dependency. Confirm fallback Wikimedia filenames before June 8 outreach is sent.

**Mitigation**: Confirm 3 Wikimedia Commons CC-BY-SA Goldenseal filenames in PHOTO_ATTRIBUTION_LOG.md before sending the June 7 botanical garden outreach emails. If garden responds with licensed images, use those — they are higher resolution. If no response, the pre-confirmed Wikimedia images are the primary source. Zero sprint impact.

---

### Risk C-3: Canva Palette Not Confirmed by June 15 (Auto-Lock Activates)

**Probability**: 2 (Medium — 40%). **Impact**: 1 (Low). **Score**: 2.

**Description**: No palette decision is recorded in WORKLOG.md by June 15. The production hex codes auto-lock to the six codes in PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md Section 4.

**Cascade if triggered**: None in terms of sprint execution — the production hex codes are the designed Phase 3 palette. The auto-lock provision exists precisely to avoid a non-decision creating a launch blocker. Impact: the user loses the opportunity to customize the palette if they had a specific palette preference they had not communicated.

**Mitigation**: Review the six production hex codes in Section 4 of the critical path document during the May 22–30 review window. If no changes are desired, record "Palette confirmed — production hex codes approved" in WORKLOG.md on May 30. If a change is desired, record the specific revised hex codes. No further action required.

---

### Risk C-4: Phase 4 Tea Blends July 15 Launch Date Slips (Post-Sprint Handoff)

**Probability**: 2 (Medium — 35%). **Impact**: 1 (Low). **Score**: 2.

**Description**: Phase 3 sprint closes July 13. Phase 4 Tea Blends target launch is July 15 (PHASE_4_MARKET_RESEARCH.md Section 6, Wave 1). The 2-day gap between sprint close and Tea Blends launch is insufficient for full product preparation if the sprint consumes all float days.

**Cascade if triggered**: Tea Blends launch slips from July 15 to July 22–28. Each week of slip costs approximately $450–$600 in Tea Blends revenue at baseline rates (40 units/week × $13 × 4 weeks / 4 weeks = $520/week average). A 1-week slip costs approximately $520 in Tea revenue.

**This risk applies to Option A more than Option C** — Option A ends the sprint with higher fatigue and less remaining capacity for Phase 4 prep. Option C's 4 float days include 2 days available for Phase 4 Tea Blends briefing starting July 14.

**Mitigation**:
- Tea Blends supplier order (Mountain Rose Herbs wholesale, $200 minimum) can be placed concurrently with the June 15 Phase 3 MRH order — add tea blend ingredients to the same order (add ~$100–$150 for tea ingredient quantities). This eliminates the supplier lead time from the post-sprint critical path.
- Etsy listing drafts for 4 Tea SKUs can be written in 3–4 hours on July 14–15 using the Phase 3 listing format as a template.
- Canva label template for Tea Blends can be produced on July 14 (1 hour) using the Phase 3 design system as the base.
- Realistic Tea Blends launch date under Option C: July 18–22 (not July 15). The 3-7 day slip is acceptable given the sprint close workload.

---

## Section 3: Kill Criteria — When to Downscope Further

These are the explicit conditions under which Option C (3 bundles) should be downscoped to a 2-bundle or 1-bundle launch — or the launch date should slip to July 1.

### Kill Criterion 1: Writing Pace Gate Failure at June 24 + June 28

If Women's Health is below 2,500 words at EOD June 24 AND below 3,400 words at EOD June 28 (2-gate failure):
- Respiratory writing has not yet begun in full
- The June 29 upload target is no longer achievable
- **Action**: Slip Women's Health upload to July 6. Respiratory upload slips to July 13. Sleep slips to July 20. Sprint close becomes July 20.
- This is not a launch cancellation — it is a 7-day slip across all three bundles with full recovery achievable before the August practitioner tier targets.

### Kill Criterion 2: Both Phase 2 Gates Drop Below Threshold by June 20

If forager cohort drops below 18% AND native plants conversion drops below 1.2% simultaneously at the June 20 pre-sprint gate check:
- The demand signal for Phase 3 medicinal herbs is weakened but not eliminated
- **Action**: Continue all pre-sprint photography and sourcing (sunk cost under $233 even at Path 2 minimum). Hold writing sprint until July 1 gate re-check. If both gates have not recovered by July 1, defer first upload to July 13 (Women's Health). Sprint content is complete — only the upload authorization is held.
- Both gates are currently cleared with meaningful margin (21.3% vs. 20% threshold; 2.24% vs. 1.5% threshold). This kill criterion is low-probability but worth having on record.

### Kill Criterion 3: AHG Reviewer Rejects Content on Accuracy Grounds

If an AHG-credentialed reviewer returns a material accuracy objection (not a minor edit) on the Black Cohosh conservation sidebar or Vitex invasive-species note — meaning they identify a factual error that, if published, could cause harm or misidentification:
- **Action**: Pause Women's Health writing to resolve the objection. Consult the specific authoritative source cited by the reviewer. Apply correction. If correction requires more than 4 hours, slip the June 29 upload by 2 days to June 30 (maximum 1-day Etsy algorithmic impact).
- This is not a launch cancellation. A reviewer-identified correction improves the product. Accept it, correct it, thank the reviewer, and add their name to the listing with the corrected text.

### Kill Criterion 4: Supplier Fraud — Non-Cultivated Goldenseal or Black Cohosh

If the supplier page for Black Cohosh (Strictly Medicinal Seeds) or Goldenseal (Prairie Moon or Strictly Medicinal, if Path 1) does not explicitly state "nursery-propagated" or "cultivated" stock:
- **Action**: Do not order from that supplier. Switch to Path 2 (Wikimedia CC) for the photo. Do not cite that supplier in the guide. Log the finding in WORKLOG.md.
- This is not a launch cancellation — photo fallback is pre-staged for both species. The kill criterion applies only to supplier citation in the guide text, not to photography.

---

## Section 4: Go/No-Go Decision Tree (May 22–29 Window)

This decision tree covers the early warning window before May 30. Each node is a question answerable from current data.

```
May 22: Phase 2 launched. First 24-hour sales data available.
       |
       +-- Q1: Forager cohort conversion rate above 18%?
               |
               YES --> Continue to Q2
               NO  --> Not yet a kill signal. Monitor daily. Kill criterion 2 
                       requires BOTH gates below threshold simultaneously. 
                       Native plants conversion still above 1.5%? Continue to Q2.
       |
       +-- Q2: Native plants guide conversion above 1.2%?
               |
               YES --> Both gates above floor. Phase 3 proceed.
               NO (both below) --> Activate Kill Criterion 2 protocol.
                                    Continue pre-sprint prep. Hold upload auth.
       |
May 25: Black Cohosh optimal order window.
       |
       +-- Q3: Black Cohosh ordered from Strictly Medicinal Seeds?
               |
               YES --> Log order confirmation in WORKLOG.md. June 21–28 arrival window.
               NO  --> Order now if available. Latest order date June 8.
                        iNaturalist CC-BY Appalachian fallback is pre-staged.
       |
May 30: Phase 2 launch data (48-hour read). DECISION DAY.
       |
       +-- Q4: Writing pace available — 5+ focused hours/day confirmed?
               |
               YES, explicitly confirmed --> Option A is viable. Select A.
               NO or Uncertain          --> Select Option C. Log in WORKLOG.md.
       |
       +-- Q5: Contractor confirmed by May 30 for Option B?
               |
               YES, contractor confirmed and test section pending June 1 --> Option B.
               NO                                                        --> Option B not viable.
       |
       +-- Q6: Palette decision recorded?
               |
               YES --> Hex codes confirmed or revised. Done.
               NO  --> Auto-lock activates June 15. No action needed now.
       |
       +-- Q7: Goldenseal decision recorded?
               |
               Path 1 (Option A/B) --> Order by June 8 hard deadline.
               Path 2 (Option C)   --> Email NC Botanical Garden by June 7.
                                       Confirm Wikimedia filenames now.
```

### Early Warning Signals to Monitor May 22–29

| Signal | Data Source | Re-planning Trigger |
|---|---|---|
| Forager cohort conversion drops below 18% | Etsy analytics (daily) | Monitor without action until both gates simultaneously fail |
| Native plants conversion drops below 1.2% | Etsy analytics (daily) | Same — both gates required to trigger Kill Criterion 2 |
| Black Cohosh not available at Strictly Medicinal Seeds by May 25 | Strictly Medicinal website / email | Order from Prairie Moon Nursery same day; log fallback |
| Phase 2 revenue below 5 units in first 48 hours | Etsy order notifications | Reassess audience targeting before Phase 3 launch; does not delay sprint |
| Contractor not identified by May 28 | Internal | Option B is rejected; select Option C May 30 |

### Decision Confidence Check (Fill Out May 30)

Rate confidence (1–5) on each dimension before finalizing the Option selection:

| Dimension | Confidence 1–5 | Notes |
|---|---|---|
| Writing pace — 5 hrs/day for 14 days (Option A) | — | 5 = certain; 3 = uncertain; 1 = unlikely |
| Contractor quality (Option B only) | — | N/A if not pursuing Option B |
| Supplier lead times confirmed | — | Have contacted Strictly Medicinal? Prairie Moon? |
| AHG peer reviewer outreach sent June 8 | — | 5 = outreach drafted and ready to send |
| Phase 2 gate margins holding | — | Current: 21.3% and 2.24% — both well above floor |

If any confidence score is 2 or below for a factor that is required for your chosen option, reconsider the option choice before logging the May 30 decision.

---

## Section 5: Mitigation Effort Summary

| Risk | Option Affected | Hours to Mitigate | Cost to Mitigate | Mitigation Status |
|---|---|---|---|---|
| Writing pace failure (A-1) | Option A | 0 (select Option C instead) | $0 | Preemptable with May 30 decision |
| Week 1 pace unsustainable (A-2) | Option A | 0 (select Option C instead) | $0 | Preemptable with May 30 decision |
| Canva revision loops (A-3) | All options | 2 hrs pre-staging per cover | $0 | Pre-stage heroes before June 22 |
| FTC compliance gap (A-4) | All options | 3 hrs review pass D18 | $0 | Appendix A table already compiled |
| AHG reviewer not secured (A-5) | All options | 4 hrs outreach prep | $0 | Begin June 8 |
| MRH delivery delay (C-1) | All options | 1 hr Frontier Co-op backup order | ~$120 | Frontier Co-op account creation |
| Goldenseal photo delay (C-2) | Option C | 1 hr Wikimedia pre-staging | $0 | Pre-stage before June 7 outreach |
| Palette auto-lock (C-3) | All options | 0.25 hrs (record decision) | $0 | Record on May 30 |
| Phase 4 Tea slip (C-4) | Option C | 3–4 hrs post-sprint prep | ~$150 (MRH tea order) | Add tea ingredients to June 15 MRH order |

**Total mitigation effort**: 15–17 hours of pre-sprint and in-sprint effort eliminates or substantially reduces all 9 identified risks. The highest-leverage single action is selecting Option C on May 30 — it eliminates Risks A-1, A-2, and reduces A-3 through lower sprint density.

---

*Document version 1.0 — May 21, 2026.*
*Risk scoring sourced from: PHASE_3_MEDICINAL_HERBS_CRITICAL_PATH.md (v6.0, Section 7), PHASE_3_GANTT_TIMELINE.csv (contingency rows 66–71).*
*Companion documents: `PHASE_3_SCOPE_DECISION_MATRIX.md`, `PHASE_3_RESOURCE_ALLOCATION_SCENARIOS.md`.*
*Next review: May 30 (decision gate), June 20 (pre-sprint gate check), June 24 (D3 pace gate).*
