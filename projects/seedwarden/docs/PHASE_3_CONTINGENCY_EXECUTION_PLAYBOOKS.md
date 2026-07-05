---
title: "Phase 3 Contingency Execution Playbooks"
subtitle: "5 Scenario Playbooks — Contractor Dropout, Supplier Delay, Scope Creep, Platform Outage, Image Sourcing Gap"
date: 2026-06-10
version: 1.0
status: activation-ready
scenarios: 1 (contractor dropout), 2 (supplier delay), 3 (scope creep), 4 (platform outage), 5 (image sourcing gap)
contractor-gate: June 17, 2026 EOD
sprint-start: June 22, 2026
cross-references:
  - PHASE_3_LAUNCH_DECISION_AUTOMATION_MATRIX.md (GO/CAUTION/NO-GO cells, auto-escalation triggers)
  - PHASE_3_RISK_DAILY_MONITORING_CHECKLIST.md (daily checks, escalation email templates)
  - PHASE_3_COMPREHENSIVE_RISK_REGISTER.md (risks 1–8, detection procedures)
  - CONTINGENCY_SOURCING_PLAYBOOK.md (contractor sourcing scenarios A–D)
  - PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md (9-week solo sprint details)
tags: [seedwarden, phase-3, contingency, playbooks, contractor, supplier, scope, platform, image-sourcing]
---

# Phase 3 Contingency Execution Playbooks
## 5 Scenario Playbooks — Step-by-Step Resolution with Escalation Templates

**Purpose**: Each playbook is a self-contained, step-by-step procedure for a specific failure mode. No open-ended judgment calls are required once a scenario triggers — every step is pre-decided. Copy the escalation templates directly; fill in the bracketed fields.

**Activation**: Scenarios trigger automatically per the thresholds in PHASE_3_LAUNCH_DECISION_AUTOMATION_MATRIX.md. Log every activation in WORKLOG.md within 1 hour.

---

## How to Use These Playbooks

1. A trigger condition fires (see matrix auto-escalation triggers T1–T9).
2. Open the corresponding playbook number.
3. Execute Step 1. Then Step 2. In order.
4. Copy any template in the playbook; fill in brackets; send.
5. Log the activation in WORKLOG.md using the format at the end of each playbook.

Do not improvise. These procedures were written pre-launch when reasoning was clear. Under the pressure of a sprint, the playbook is more reliable than in-the-moment judgment.

---

## Playbook 1: Contractor Dropout

**Applies to**: Pre-sprint dropout (no contract signed by June 17), mid-sprint dropout (contractor goes silent or withdraws after June 22)

**Triggers**:
- T2: 1–2 proposals by June 12, none pass Tier B screen → activate immediately
- T3: June 17 EOD, no contract signed → activate solo fallback
- T8: 3 consecutive days no contractor communication during sprint → assume dropout

---

### Step 1-A: Pre-Sprint Dropout (June 17 EOD — no contract signed)

Assess pipeline at June 17 5pm ET.

Count: How many candidates have completed all 5 screening criteria?
- Portfolio reviewed and confirms publication-quality line art: yes/no
- Botanical knowledge confirmed in portfolio or interview: yes/no
- Availability June 22–September 24 confirmed: yes/no
- Rate quoted at or below $1,350 ceiling (or $1,286 for Upwork after 5% fee): yes/no
- Contract offer made (or ready to make immediately): yes/no

**If at least 1 candidate has all 5 criteria**: Send contract offer immediately. Do not wait for comparison. The first candidate meeting all criteria gets the offer. If they decline, move to the next. You have until June 17 EOD.

**If zero candidates have all 5 criteria**: Solo fallback activates. Proceed to Step 1-B.

---

### Step 1-B: Solo Fallback Activation

Execute in order.

1. Stop all active contractor outreach immediately. Do not continue running parallel planning tracks.

2. Log the solo fallback activation in WORKLOG.md (use Template LOG-1 below).

3. Open PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md Section 6. Verify all pre-sprint checklist items are complete:
   - CC images pre-staged (all 14 species confirmed in assets/)
   - Canva palette loaded
   - Attribution log complete
   - Content outlines finalized for all 6 bundles

4. Set Phase 4 start date to October 1, 2026. Wave 1 launch: November 1, 2026.

5. Confirm June 22 sprint start. User writes all 6 bundles at 12 hrs/week. Women's Health is the first bundle (zero-float — upload June 29).

**Template LOG-1: Solo Fallback Activation Log**
```
WORKLOG.md entry — [Date]

SCENARIO: Contractor dropout / no-go — solo fallback activated.
Pipeline status at gate: [X] candidates reviewed, [Y] interviewed, [Z] offers made.
Reason for no confirmed contract: [brief — no Tier B+ candidates / all over budget / no responses].
Solo fallback activated per PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md.
Sprint: June 22 – September 24, 12 hrs/week, 6 bundles.
Phase 4 adjusted: start October 1, Wave 1 November 1, Phase 5 February 1, 2027.
Pre-sprint checklist status: [all complete / items pending: list them].
```

---

### Step 1-C: Mid-Sprint Dropout Detection

This step applies during the sprint (June 22 – August 3 for contractor model). Monitor daily.

**Daily check**: Is there a contractor communication entry in WORKLOG.md from today or yesterday?

**Day 1 of silence**: Send Template MSG-1 (below). Log: "Day 1 contractor silence. Check-in sent."

**Day 2 of silence**: Send Template MSG-1 again AND attempt phone contact if number is in the contract. Log: "Day 2 contractor silence. Second contact attempt."

**Day 3 of silence**: Do not wait for further response. Assume dropout. Proceed to Step 1-D.

**Delivery date missed with no communication**: Count as Day 1 of silence from the moment the deadline passes. If the contractor was already at Day 1 or Day 2 of silence, you may already be at Day 2 or Day 3.

**Template MSG-1: Contractor Check-In (Missed Milestone or Silence)**
```
Subject: Checking in — [bundle name] delivery

Hi [Name],

I noticed we haven't connected since [date]. I wanted to check in directly — are you okay, and is there anything blocking the [bundle name] delivery?

If you need a short extension (1–3 days), please let me know today and I can adjust the schedule. If there's a larger issue affecting your availability, I'd rather know now so we can work through it together.

Please reply here or reach me at [phone number] if that's easier. I'll follow up again tomorrow morning if I haven't heard from you.

Thank you,
[Name]
Seedwarden
```

---

### Step 1-D: Mid-Sprint Dropout Response

Activate immediately at Day 3 silence. Do not delay.

**Determine dropout stage**:

Stage A (dropout before any delivery — before first draft received):
- Full solo fallback. No partial contractor work to salvage.
- Cascade all bundle upload dates per solo fallback architecture.
- All remaining content: user-written.
- Preserve contract records for Upwork dispute process (if deposit was paid through Upwork escrow).

Stage B (dropout after partial delivery — 1–8 plates or drafts delivered):
- Assess quality of delivered work. If publishable after user revision: retain it.
- Remaining bundles shift to solo pace.
- Payment: release only for delivered and accepted work. Log what was accepted.
- Draft upload schedule for remaining bundles based on solo model timing.

Stage C (dropout after substantial delivery — 9 or more plates or most bundles complete):
- Minimal disruption. Attempt to complete remaining scope via one of:
  1. Urgent Upwork replacement: post Template JOB-1 (below) for small remaining scope.
  2. Contact Upwork proposal pool runners-up from original search: one may accept urgent small scope.
  3. User absorbs remaining content.

**Template JOB-1: Urgent Replacement Upwork Posting**
```
Title: URGENT — Botanical Illustrator, [X] Plates Remaining, 2-Week Turnaround

We have [X] botanical illustration plates remaining from a larger project where our original illustrator became unavailable. We need a botanical illustrator to complete [X] plates at publication-quality line art within 2 weeks.

Plants remaining: [list species names and Latin binomials]
Style: Match provided samples — existing plates from the project will be shared with the selected illustrator
Format: 300 DPI, TIFF or PNG
Timeline: Delivery within 14 days of contract signing

Budget: $[X] fixed price for [X] plates.

If you can start within 48 hours and have medicinal plant illustration experience, please apply immediately with portfolio examples. This is time-sensitive.
```

**Template LOG-2: Mid-Sprint Dropout Log**
```
WORKLOG.md entry — [Date]

SCENARIO: Contractor mid-sprint dropout.
Dropout stage: [A: pre-delivery / B: partial delivery: X plates / C: substantial delivery: X plates].
Last confirmed contact: [date and method].
Plates or drafts confirmed received: [X of Y]. Files verified: [yes/no].
Recovery action: [full solo conversion / urgent Upwork replacement / partial mixed set].
Financial recovery: [Upwork dispute filed / partial payment released / full payment released for delivered work].
Sprint impact: [minimal / moderate / full solo conversion — adjusted upload dates: list].
Phase 4 timeline: [unaffected / adjusted by X days].
```

---

## Playbook 2: Supplier Delay

**Applies to**: Mountain Rose Herbs (MRH) delivery delayed; botanical garden contact unresponsive; Frontier Co-op backup order needed

**Triggers**:
- June 18: MRH shipping confirmation not received
- June 15: Botanical garden contact has not responded to outreach
- June 19: MRH has no tracking number and supplier has not shipped

---

### Step 2-A: MRH Non-Shipment (June 18 — No Tracking)

1. Email MRH order support with order number. Request tracking within 24 hours. Use Template MSG-2 (below).
2. Simultaneously: log the check in WORKLOG.md: "June 18 — MRH order: no tracking confirmed. Follow-up sent."
3. Place a Frontier Co-op account order the same day as insurance. Frontier Co-op is free to set up (no minimum order). Estimated delivery June 24–26 if ordered June 18. This is the pre-authorized backup supplier — no approval needed to place this order.

**If MRH confirms shipping June 18 or June 19**: Cancel Frontier Co-op order or retain as backup for photography.

**If MRH does not ship by June 19**: Frontier Co-op order is now the primary. Photography shifts to Sprint Days 2–4 (June 23–25). Zero impact on June 29 Women's Health upload.

**Template MSG-2: MRH Order Follow-Up**
```
Subject: Order [ORDER NUMBER] — Shipping Status Request

Hello Mountain Rose Herbs team,

I placed order [ORDER NUMBER] on [date]. I have not yet received a shipping confirmation or tracking number. The order is needed by June 21 for a production deadline.

Could you confirm the current status of my order and provide a tracking number if it has shipped? If there is a delay or stock issue, please let me know today so I can make arrangements.

Thank you,
[Name]
```

---

### Step 2-B: Both MRH and Frontier Co-op Delayed Past June 25

Activate full CC-only mode immediately.

1. Open PHOTO_ATTRIBUTION_LOG.md. If fewer than 1 CC image per bundle is confirmed: run Wikimedia Commons sourcing sprint (30 minutes per bundle). All 14 sprint species have verified CC BY-SA sources on Wikimedia.

2. Wikimedia sourcing procedure per bundle:
   - Go to commons.wikimedia.org/wiki/Special:Search
   - Search: "[Species name] medicinal" or "[Species common name] plant"
   - Filter: CC-BY-SA license
   - Confirm at least 1 full-plant habit photo
   - Log: filename, source URL, photographer name, license, attribution text

3. iNaturalist procedure (if Wikimedia is thin for a species):
   - Go to inaturalist.org/observations
   - Search species name, filter Research Grade
   - Check license on individual observation page
   - Acceptable: CC0, CC BY, CC BY-SA only
   - Log same fields as Wikimedia

4. All 14 species should be resolvable within 3–4 hours total via this procedure.

5. Log: "Supplier delay — full CC-only mode activated. MRH/Frontier not confirmed. Wikimedia sourcing sprint complete. [N] of 6 bundles confirmed."

**Goldenseal special handling**: Do not use photos of wild Goldenseal specimens. Source exclusively from: University of Michigan Herbarium records, USDA PLANTS database, or cultivated-specimen Wikimedia images. Verify "cultivated" in the image description before logging.

---

### Step 2-C: Botanical Garden Contact Unresponsive by June 15

1. Remove botanical garden from sourcing plan immediately. Do not follow up after June 15 — the timeline has no slack for a delayed institutional response.

2. Treat all image sourcing as Wikimedia + iNaturalist only.

3. Run the pre-sprint image audit described in Step 2-B for any bundle that was depending on botanical garden photography.

4. Log: "Botanical garden contact: no response by June 15 cutoff. Removed from sourcing plan. Wikimedia/iNaturalist only."

**Pre-validated fallback supplier chain (in priority order)**:
1. Wikimedia Commons CC BY-SA (primary — all 14 species documented available)
2. iNaturalist CC BY or CC BY-SA observations (secondary — high volume, verify license per observation)
3. USDA PLANTS database images (free, public domain, high botanical accuracy)
4. Stock photo purchase up to $75 per bundle (pre-authorized; Shutterstock, Adobe Stock, or Alamy)

---

## Playbook 3: Scope Creep

**Applies to**: Women's Health bundle expanding past daily word targets; any bundle exceeding time budget by 10% or more; mid-sprint requests for new content not in the original 6-bundle scope

**Triggers**:
- T6: Bundle time exceeds budget by 10% after Day 5
- T-immediate: Any new bundle concept raised during June 22–July 13 sprint window
- Risk 3 from register: Women's Health section word count exceeds 110% of target at any session

---

### Step 3-A: Real-Time Section Scope Freeze

When any section exceeds 110% of its word target:

1. Stop writing the section at the 110% word count.
2. Open a new document section titled "[bundle name] v1.1 expansion notes."
3. Paste the excess content into that section.
4. Note what the excess content covers (topic, 1 sentence).
5. Continue the main document from the next section.
6. Do not attempt to integrate the excess content during the current session.

This is the scope freeze. The discomfort of cutting is the mitigation working as designed.

**Word target reference by bundle (derived from risk register)**:
- Black Cohosh (Women's Health): 700 words per entry
- Vitex: 600 words per entry
- Red Clover: 400 words per entry
- Black Cohosh conservation sidebar: 150 words — hard stop at 165 regardless of incomplete thoughts

---

### Step 3-B: Day 2 Pace Check (June 23 EOD)

Women's Health Day 2 target: 1,200 words minimum.

**If Women's Health is below 900 words at June 23 EOD**:
1. Remove all non-writing tasks from June 24 schedule. No supplier coordination, no photography, no email before writing is complete.
2. Apply scope compression: Vitex 600w → 400w (remove invasive-species regional detail to a single sentence); Red Clover 400w → 250w (limit to isoflavone framing and forager edibility crossover note).
3. Write Black Cohosh conservation sidebar in a separate document section; hard stop at 165 words; paste into main document.

---

### Step 3-C: Day 3 Pace Gate Failure (June 24 EOD — Women's Health below 2,500 words)

1. Log immediately: "D3 pace gate FAILED — Women's Health [X] words at June 24 EOD. Option C activated." (see Template LOG-3 below)

2. Activate Option C scope reduction:
   - Women's Health, Respiratory, and Sleep proceed on original schedule.
   - Immunity and Digestive defer to post-sprint (post-August 3 if contractor model; post-September 24 if solo).
   - This is a scope correction. The June 29 Women's Health upload date is unaffected.

3. Do not attempt a pace recovery that would require compressing FTC review. The D18 FTC compliance review (July 9) is mandatory — never reduce below 48 hours per bundle for FTC review.

**Template LOG-3: Pace Gate Failure Log**
```
WORKLOG.md entry — [Date]

SCENARIO: Day 3 pace gate failure — Option C activated.
Bundle affected: Women's Health.
Word count at gate: [X] words (target: 2,500).
Scope correction: Immunity and Digestive deferred to post-sprint.
Bundles proceeding: Women's Health (upload June 29), Respiratory (upload July 6), Sleep (upload July 13).
FTC review maintained: yes — Women's Health FTC review remains July 9.
Phase 4 timing impact: [none / adjusted by X weeks].
```

---

### Step 3-D: New Bundle Request During Sprint (June 22–July 13)

Any new bundle concept raised during the active sprint window is automatically deferred.

1. Log the concept in WORKLOG.md under "Phase 4 exploration queue."
2. Respond: "Logged for Phase 4 evaluation. Current sprint is scope-frozen."
3. Do not open research tabs, draft outlines, or allocate writing time to new concepts during the sprint window.

**Template MSG-3: Contractor Scope Expansion Request (Contractor Model Only)**
```
Subject: [Bundle name] — sprint request

Hi [Name],

The [bundle name] outline is complete. We've had [brief description of delay or scope expansion situation] that has shifted [deferred bundle] to a later date in the sprint.

I'd like to check your availability for a focused writing sprint on [bundle name] in the [date range] window. The scope is [word count] words, structured per the outline I'm attaching. Budget: [amount].

Can you confirm your availability and turnaround time for this scope?

Thank you,
[Name]
Seedwarden
```

---

## Playbook 4: Platform Outage

**Applies to**: Kit (email platform) unavailable June 22; Etsy store suspended or inaccessible June 22; both platforms unavailable simultaneously

**Triggers**:
- T9: Kit or Etsy inaccessible at launch window June 22

---

### Step 4-A: Kit Outage — Email Platform Unavailable

1. Do not delay the content sprint. Continue writing Women's Health bundle on schedule regardless of platform status.

2. Attempt Kit login via kit.com/login. If login fails: check kit.com status page or @kitdotcom on X for known outage. Log what you see.

3. If outage is confirmed and Kit support has not responded within 4 hours:
   - Export subscriber list from last available Kit CSV backup.
   - Import to Mailchimp Free account (free for up to 500 contacts, available at mailchimp.com with no setup delay).
   - Reconstruct the 3-email welcome sequence in Mailchimp using existing copy from KIT_EMAIL_LAUNCH_SEQUENCE.md.

4. For launch-day email announcement: send via Gmail with BCC list of all subscribers. Subject: "Seedwarden is live — Women's Health Bundle now available." Body: 2 sentences + Etsy listing link.

5. Log the platform status and actions taken (Template LOG-4A below).

**Template LOG-4A: Kit Outage Log**
```
WORKLOG.md entry — [Date/Time]

SCENARIO: Kit platform outage — email launch fallback activated.
Kit status: [login failed / outage confirmed on status page / support ticket submitted at HH:MM].
Fallback activated: [Gmail BCC announcement / Mailchimp migration].
Subscriber count in fallback list: [X].
Launch email sent: [yes/no, time].
Kit resolution timeline: [estimated / unknown].
Content sprint status: [unaffected — writing on schedule].
```

---

### Step 4-B: Etsy Outage or Suspension

1. Do not delay the content sprint.

2. If Etsy store is suspended (not a platform-wide outage): open Etsy resolution center at etsy.com/your/shops/me/resolution-center. Submit a reinstatement request with a description of the store and all products (digital educational guides, no physical inventory). Etsy reinstatement typically takes 2–7 business days. Document the suspension notice text in WORKLOG.md.

3. If Etsy platform is down (site-wide outage): check etsy.com status. Wait up to 2 hours for routine outages. If unresolved:
   - Create Gumroad account at gumroad.com (free; 10% fee per sale — acceptable for temporary operations).
   - Upload all 6 bundle PDFs as separate products at identical prices.
   - Send launch email to subscriber list with Gumroad links substituted for Etsy links.

4. Log all actions (Template LOG-4B below).

**Template LOG-4B: Etsy Outage or Suspension Log**
```
WORKLOG.md entry — [Date/Time]

SCENARIO: Etsy [outage / suspension].
Status: [store suspended [reason if known] / platform outage — down since HH:MM].
Action: [reinstatement request submitted at HH:MM / Gumroad account created / platform outage — waiting].
Gumroad listings live: [yes/no, URLs if applicable].
Email subscribers notified of alternate purchase link: [yes/no, time sent].
Content sprint status: [unaffected — writing on schedule].
Etsy reinstatement ETA: [X business days / unknown].
```

---

### Step 4-C: Both Platforms Unavailable Simultaneously

1. Gumroad is the immediate fallback for both.

2. Content sprint continues on schedule. Platform issues do not delay writing.

3. Email list announcement goes out on schedule via Gmail BCC.

4. Monitor Etsy and Kit status every 4 hours on launch day. Restore primary platform links in email list and any social posts when the platform is confirmed restored.

5. Log both outage events with timestamps and recovery actions.

---

## Playbook 5: Image Sourcing Gap

**Applies to**: Wikimedia Commons images insufficient for one or more bundles by June 19; iNaturalist search returns no usable CC images for a species; Goldenseal image sourcing complications

**Triggers**:
- T4: Any bundle with 0 CC images at June 19 EOD
- T5: 3 or more bundles with 0 images at June 21 EOD

---

### Step 5-A: Single Bundle Image Gap (June 19 — 1–2 bundles unresolved)

For each unresolved bundle, execute the 4-source protocol in order. Stop when 1 image is confirmed per bundle.

**Source 1 — Wikimedia Commons (30 minutes per bundle)**:
- URL: commons.wikimedia.org/wiki/Special:Search
- Search: "[Scientific name] medicinal" or "[Common name] plant"
- Filter: CC BY-SA license
- Target: 1 full-plant habit photo + 1 detail (leaf, flower, or fruit)
- Log: filename, URL, photographer, license, attribution text in PHOTO_ATTRIBUTION_LOG.md

**Source 2 — iNaturalist (20 minutes per bundle)**:
- URL: inaturalist.org/observations
- Search species, filter Research Grade
- Click individual observation; verify License field in right sidebar
- Acceptable: CC0, CC BY, CC BY-SA only
- Log same fields as Wikimedia

**Source 3 — USDA PLANTS Database (15 minutes per bundle)**:
- URL: plants.usda.gov
- Search species name; check Photo Gallery tab
- USDA images are public domain (no attribution required, but log source URL)
- Note: USDA images tend to be herbarium specimens, not habit photos — useful for botanical accuracy, less useful for visual appeal in listings

**Source 4 — Stock photo purchase (pre-authorized, $75 per bundle maximum)**:
- Preferred sources: Shutterstock, Adobe Stock, Alamy
- Search: "[scientific name]" OR "[common name] medicinal plant" OR "[common name] herb"
- Verify license: editorial license is acceptable for educational PDF use; standard commercial license preferred
- Download highest-resolution available
- Log: purchase receipt URL, license type, permitted uses

---

### Step 5-B: Full Sourcing Bottleneck (June 21 — 3+ bundles unresolved)

Activate the rapid-licensing protocol. This is pre-authorized — no approval required.

1. Allocate stock photo budget: $75 per unresolved bundle. Maximum total: $450 (6 bundles × $75). If budget is not fully used, the remainder is not carried over.

2. Assign sourcing order by bundle upload date (most urgent first):
   - Women's Health (upload June 29): source first
   - Respiratory (upload July 6): source second
   - Sleep (upload July 13): source third
   - Immunity, Digestive, Integrative: source in parallel with writing

3. Stock photo sourcing sprint: 24-hour window June 21–22. By June 22 9am ET: all 6 bundles must have at least 1 confirmed image (CC or licensed stock).

4. If a bundle's image is not confirmed by June 22 9am ET: launch that bundle's listing with a public-domain botanical illustration from a pre-1900 source (no copyright applies). Biodiversity Heritage Library (biodiversitylibrary.org) and the Botanical Illustrations database at Missouri Botanical Garden are the best sources. These are public domain and historically accurate.

**Biodiversity Heritage Library procedure**:
- URL: biodiversitylibrary.org
- Search: "[species name]" or genus name
- Filter to illustrated works
- Download highest-resolution plate available
- Log: source URL, publication name, publication year, illustrator if named
- Attribution: "Public domain — [Publication Title], [Year]"

5. Log the full sourcing sprint completion (Template LOG-5 below).

**Template LOG-5: Image Sourcing Sprint Log**
```
WORKLOG.md entry — [Date]

SCENARIO: Image sourcing gap — rapid-licensing sprint activated.
Total bundles confirmed at June 21 EOD: [X of 6].
Bundles requiring sourcing action: [list bundle names].
Stock photo budget allocated: $[X].
Sourcing actions taken by bundle:
  - Women's Health: [Wikimedia confirmed / iNaturalist confirmed / Stock purchased at $X / BHL public domain used]
  - Respiratory: [same format]
  - Sleep: [same format]
  - Immunity: [same format]
  - Digestive: [same format]
  - Integrative: [same format]
All bundles confirmed: [yes / no — [X] still unresolved at June 22 EOD].
```

---

### Step 5-C: Goldenseal-Specific Image Protocol

Goldenseal (Hydrastis canadensis) is CITES Appendix II listed. Wild specimen photos require handling documentation. Follow this protocol for all Goldenseal images regardless of the image's stated source.

1. Acceptable sources for Goldenseal images:
   - Cultivated specimen photos on Wikimedia Commons (verify "cultivated" in image description)
   - University of Michigan Herbarium records
   - USDA PLANTS database (herbarium specimen)
   - Botanical illustrations from Biodiversity Heritage Library (public domain)

2. Not acceptable: photos tagged "wild" or with unclear cultivation status, photos from foraging or field identification contexts.

3. Attribution for Goldenseal images must include: "Hydrastis canadensis (Goldenseal) — cultivated specimen." Never label a listing image with "wild Goldenseal."

---

## Playbook Summary Reference

| Playbook | Trigger | First Action | Time to Resolution |
|----------|---------|--------------|-------------------|
| 1 — Contractor dropout | T2/T3/T8 | Assess pipeline; activate solo fallback or check-in message | 30 min (pre-sprint) / 48 hrs (mid-sprint) |
| 2 — Supplier delay | June 18 no tracking / June 15 no garden response | MRH follow-up + Frontier Co-op order; or full CC-only mode | 24 hrs (MRH) / immediate (CC-only) |
| 3 — Scope creep | 110% section overrun / T6 / new bundle request | Scope freeze; paste excess to v1.1 notes; continue | Immediate (real-time) |
| 4 — Platform outage | T9 — Kit or Etsy down June 22 | Kit: Gmail BCC + Mailchimp; Etsy: Gumroad | 4 hrs (Kit) / 2–4 hrs (Etsy) |
| 5 — Image sourcing gap | T4/T5 — bundles without CC images | 4-source protocol; stock photo budget; BHL public domain | 24-hr sourcing sprint |

---

*Prepared: June 10, 2026. Foundation references: PHASE_3_COMPREHENSIVE_RISK_REGISTER.md (risks 1–8), CONTINGENCY_SOURCING_PLAYBOOK.md (contractor scenarios A–D), PHASE_3_LAUNCH_DECISION_AUTOMATION_MATRIX.md (auto-escalation triggers T1–T9), PHASE_3_SOLO_FALLBACK_ARCHITECTURE.md.*
