---
title: "Template Field Checklist — Phase 1 Batch 1 Email Templates"
created: 2026-05-15
source_template: "PHASE_1_EMAIL_TEMPLATES.md"
purpose: "Structured fill-in checklist for all {{placeholder}} fields across the five Batch 1 email templates. Complete all fields before Block 6 (send)."
status: pre-send-ready
---

# Template Field Checklist — Batch 1 Email Templates

Complete this checklist sequentially. Every field must be filled before any email is sent. No placeholder survives to the sent email.

---

## Part 1: Universal Fields (Same Value in All Five Emails)

These four fields appear in all five emails. Fill them once here, then apply across all templates.

---

### FIELD U-1: `{{YOUR_NAME}}`

**Description**: Your preferred outreach name — the signature on every email.
**Validation rule**: Must be a real name; no pseudonyms. The contact needs to be able to find you via Google, LinkedIn, or a website before they respond. A name that returns no results creates credibility risk.
**Example value**: `Anya Wank`
**Appears in**: All five emails (signature block of each)
**Your value**: _______________________________________________

---

### FIELD U-2: `{{YOUR_CONTACT_INFO}}`

**Description**: Email address (required) plus optionally Signal handle or personal website.
**Validation rule**: Must be a working email address you monitor. Do not use a generic contact-form URL here — this is a personal reply-to line. Signal handle is optional but increases trust for legal/security-aware contacts (Elias, Bassin).
**Example value**: `anya@yourdomain.com | Signal: @yourhandle | yourwebsite.com`
**Appears in**: All five emails (signature block of each)
**Your value**: _______________________________________________

---

### FIELD U-3: `{{DOMAIN_COUNT}}`

**Description**: The number of domains in the framework you are presenting.
**Validation rule**: Must match the path selected.
  - Path A or A+37: use `35` (core framework framing) or the current expanded count if you prefer to frame it as `47+`
  - Path B: use the count of domains being released in the initial wave
**Decision note**: The DISTRIBUTION_PATH_ANALYSIS.md (May 9) notes the framework is actually 47+ domains. Two defensible choices: use "35-domain core framework" (cleaner; matches Gist titles) or update all framing to "47-domain" (more accurate). Pick one and apply consistently across all five emails.
**Example value**: `35`
**Appears in**: All five emails (body paragraph 2)
**Your value**: _______________________________________________

---

### FIELD U-4: Path Selection Block

**Description**: Each email contains three mutually exclusive blocks labeled `[PATH A]`, `[PATH A+37]`, and `[PATH B]`. Exactly one is retained per email; the other two are deleted.
**Validation rule**: Only the block matching your selected path survives. The block is a single paragraph. Deleting the wrong two blocks is the most common pre-send error.
**Action**: After selecting your path, physically delete the two non-matching `[PATH X]` paragraphs from all five email drafts.
**Your path selection**: _______________ (A / A+37 / B)
**Applies to**: All five emails

---

### FIELD U-5: URL Placeholders (Block 1 Dependencies)

These three URL fields are filled after Gist creation (Block 1 in the execution checklist). If Gists are already live, fill immediately.

| Placeholder | What It Points To | Known URL | Status |
|-------------|------------------|-----------|--------|
| `{{PROPOSAL_URL}}` | Main 35-domain proposal Gist | https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261 | LIVE |
| `{{EXEC_SUMMARY_URL}}` | Executive summary Gist | https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4 | LIVE |
| `{{LITIGATION_TRACKER_URL}}` | Litigation Tracker 2026 Gist | https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0 | LIVE |

**Action**: Replace each placeholder with the corresponding URL. The three Gists above are confirmed live as of April 30, 2026. Verify they still load before inserting.
**Appears in**: Emails 1 (all three), 2 (Proposal + Exec Summary), 3 (Proposal + Exec Summary), 4 (Proposal + Exec Summary), 5 (all three + P.S.)

---

## Part 2: Contact-Specific Fields

These fields are unique per email. Each requires 5–10 minutes of current research.

---

### EMAIL 1: Ryan Goodman (Just Security / NYU Law)

**Send order**: FIRST — send before any other email

#### FIELD G-1: `{{RECENT_JUST_SECURITY_ARTICLE}}`

**Description**: The title and approximate date of Goodman's most recent published piece at Just Security. This is the specific "I read your work" signal — it must be a real, recent article, not a generic reference.
**Where to find it**: https://www.justsecurity.org/author/goodmanryan/ — look for his most recent piece (within the last 30–60 days)
**Validation rule**: Must be a real article title. Do not use a category name ("your war powers coverage") or a vague descriptor ("your recent work"). If the page does not clearly list author-specific articles, use the site's tag search for ryan-goodman.
**Format**: `[Article title], Just Security, [Month Year]`
**Example value**: `"The OLC Memo That Could Nullify the War Powers Resolution," Just Security, April 2026`
**In the template**: The sentence reads: "your recent work at Just Security on {{RECENT_JUST_SECURITY_ARTICLE}} connects directly..."
**Your value**: _______________________________________________

#### FIELD G-2: Subject Line Selection

**Description**: Exactly one of three subject line options must be selected. The other two are deleted.
**Options**:
  - Option A: `Domain 28 / Operation Absolute Resolve — OLC memo analysis + statutory gap — Just Security forum piece?`
  - Option B: `Independent research: prosecutorial weaponization (Domain 29, SPLC indictment) + war powers — seeking Just Security feedback`
  - Option C: `Framework + FISA 702 analysis: judicial independence and surveillance accountability — for Just Security review`
**Recommended**: Option A (most specific; strongest curiosity gap)
**Validation rule**: Only one survives. The other two subject line lines are deleted from the draft.
**Your selection**: _______________________________________________

---

### EMAIL 2: Wendy Weiser (Brennan Center for Justice)

**Send order**: SECOND — send 30 minutes after Goodman

#### FIELD W-1: `{{RECENT_BRENNAN_CENTER_PUBLICATION}}`

**Description**: The title of the most recent Brennan Center publication that Weiser personally authored or that her Democracy Program produced. This establishes that you have read their specific recent output.
**Where to find it**: https://www.brennancenter.org/our-work — filter by "Democracy Program" or by Weiser's author page at https://www.brennancenter.org/about/leadership/wendy-r-weiser
**Validation rule**: Must be a real publication with a real title. Citing a Brennan Center report that is 12+ months old signals you are not current with their work — check the date.
**Format**: `[Publication title], Brennan Center, [Month Year]`
**Example value**: `"Protecting the Vote in 2026," Brennan Center for Justice, May 2026`
**In the template**: The sentence reads: "your work at the Brennan Center on {{RECENT_BRENNAN_CENTER_PUBLICATION}} connects directly..."
**Your value**: _______________________________________________

#### FIELD W-2: Subject Line Selection

**Options**:
  - Option A: `Framework + April 2026 voting rights crisis: four-state SAVE Act wave + ballot initiative suppression — Brennan Center feedback`
  - Option B: `Independent research on voting rights and federalism — builds on Brennan Center work — seeking feedback`
  - Option C: `35-domain democratic reform framework — Domain 1 (electoral reform) — academic review requested`
**Recommended**: Option A (most current; references April 2026 events she is actively tracking)
**Validation rule**: One selected; two deleted.
**Your selection**: _______________________________________________

---

### EMAIL 3: Erica Chenoweth (Harvard Kennedy School)

**Send order**: THIRD — send 60 minutes after Goodman

**ROLE UPDATE — REQUIRED REVIEW BEFORE SENDING** (see contact verification section below): Chenoweth is now serving as Academic Dean for Faculty Development in addition to her professorship. Her inbox volume has increased substantially. Consider acknowledging her expanded role in the salutation or opening line.

#### FIELD C-1: `{{RECENT_CHENOWETH_WORK}}`

**Description**: The title of her most recent published work. A default is pre-filled in the template ("Why Gen-Z Is Rising, Journal of Democracy, January 2026") but it must be verified — she may have published more recently.
**Where to find it**: https://www.hks.harvard.edu/faculty/erica-chenoweth or https://scholar.harvard.edu/ericheno
**Validation rule**: If the default ("Why Gen-Z Is Rising") is still her most recent piece as of your send date, keep it. If she has published since January 2026, update to the newer piece. Do not use the book-in-progress ("End of People Power") as a substitute — it is not yet published.
**Default (confirmed as of April 2026)**: `Why Gen-Z Is Rising, Journal of Democracy, January 2026`
**Your verification date**: _______________ | **Still current?**: Y / N
**Updated value if needed**: _______________________________________________

#### FIELD C-2: Subject Line Selection

**Options**:
  - Option A: `Research builds on your 3.5% threshold — seeking correction on nonviolent action application to current U.S. context`
  - Option B: `35-domain democratic renewal framework — theory of change grounded in Chenoweth nonviolent action research — academic feedback`
  - Option C: `Harvard Kennedy School research collaboration: democratic renewal diagnostic & mobilization strategy`
**Recommended**: Option A (strongest — frames the ask as a correction, not an endorsement; specifically names her threshold finding)
**Note**: Option C may be less effective given her Administrative Dean role (she may be routing non-faculty-contact emails differently now)
**Your selection**: _______________________________________________

---

### EMAIL 4: Ian Bassin (Protect Democracy)

**Send order**: FOURTH — send 90 minutes after Goodman

#### FIELD B-1: `{{RECENT_PROTECT_DEMOCRACY_FILING}}`

**Description**: The name, court, and filing date of Protect Democracy's most recent case activity or publication. This signals you are tracking their active docket.
**Where to find it**: https://protectdemocracy.org/work/ — look for their most recent case or analysis (within 30 days)
**Validation rule**: Must be a specific case name and court, or a specific publication title. Do not use "your recent litigation work" — Bassin will not know which matter you mean, and it signals you did not actually look it up.
**Format**: `[Case name], [Court], [Filing type], [Date]` or `[Publication title], [Date]`
**Example value**: `Widakuswara v. Lake, D.D.C., preliminary injunction brief, May 2026`
**In the template**: The sentence reads: "your ongoing litigation — particularly {{RECENT_PROTECT_DEMOCRACY_FILING}} — connects directly to two domains..."
**Your value**: _______________________________________________

#### FIELD B-2: `{{YOUR_AVAILABILITY}}`

**Description**: Two or three specific time windows in the next two weeks when you are available for a 20-minute call. This is unique to the Bassin email (the only Batch 1 email that proposes a call).
**Validation rule**: Must be specific — day, time, and timezone. "This week or next" is not a valid response here; it forces Bassin's assistant to ask a follow-up question before scheduling.
**Example value**: `Tuesday May 20, 10–11 AM EDT; Wednesday May 21, 2–3 PM EDT; or Thursday May 22, 9–10 AM EDT`
**In the template**: The sentence reads: "Would you be willing to take a 20-minute call at your convenience? I'm available {{YOUR_AVAILABILITY}}."
**Your value**: _______________________________________________

#### FIELD B-3: Subject Line Selection

**Options**:
  - Option A: `Framework + prosecutorial weaponization: domain-29 SPLC analysis and domain-06 judicial threat documentation — Protect Democracy input`
  - Option B: `Litigation & implementation strategy: democratic renewal framework (judicial independence + constitutional reform) — brief call?`
  - Option C: `Independent research on DOJ capture and judicial independence — builds on Protect Democracy litigation — seeking 20 minutes`
**Recommended**: Option B (cleanest for a meeting request; names both domains and the call ask in the subject line)
**Your selection**: _______________________________________________

---

### EMAIL 5: Marc Elias (Democracy Docket / Elias Law Group)

**Send order**: FIFTH — send 120 minutes after Goodman

**EMAIL ADDRESS UPDATE — CRITICAL** (see contact verification section): The PHASE_1_CONTACT_VERIFICATION.json lists `melias@perkinscoie.com` as primary. This is stale — Elias left Perkins Coie in 2021. The BATCH_1_CONTACT_VERIFICATION.md (updated 2026-05-14) corrects this to `melias@elias.law`. Use `melias@elias.law` as primary.

#### FIELD E-1: Case Status Verification for Watson v. RNC and Louisiana v. Callais

**Description**: The email references these two active cases. Their status must be verified before sending — if either has been decided (or substantially developed), the template references need updating.
**Where to find it**: https://www.democracydocket.com — search for Watson v. RNC and Louisiana v. Callais
**Validation rule**: If either case has been resolved since the template was drafted (April 30, 2026), update the reference to reflect the current status. If both are still pending (expected June–July 2026 decisions), the template references stand as written.
**Check date**: _______________ | **Watson v. RNC status**: _______________
**Louisiana v. Callais status**: _______________ | **Template changes needed?**: Y / N

#### FIELD E-2: Subject Line Selection

**Options**:
  - Option A: `Democracy Docket collaboration: electoral reform framework + litigation tracker alignment`
  - Option B: `Framework + Watson v. RNC / Louisiana v. Callais analysis — domain 1 litigation tracker — Democracy Docket feedback`
  - Option C: `Independent research on electoral reform and voter suppression — builds on Democracy Docket tracking — seeking input`
**Recommended**: Option B (names specific active cases; signals you read Democracy Docket's tracking)
**Your selection**: _______________________________________________

---

## Part 3: Follow-Up Template Fields

For follow-up emails sent 14 days after initial send (one follow-up only; no further contact after that).

#### FIELD F-1: `{{SEND_DATE}}`
**Description**: The date the original email was sent. Fill when you send each email.
**Format**: `[Month Day, Year]` — e.g., `May 16, 2026`

#### FIELD F-2: `{{NEW_DEVELOPMENT}}`
**Description**: A specific new development since the original email that is relevant to this contact's domain. Must be new information — not a restatement of the original email.
**Validation rule**: This must be a real, recent development — a court ruling, a new filing, a published piece, or a data update. Do not restate the original email's points as "new developments."
**Contact-specific suggestions**: See `PHASE_1_EMAIL_TEMPLATES.md` section "New development examples for each contact."

---

## Pre-Send Validation Checklist

Run this check on each draft before hitting send.

- [ ] `{{YOUR_NAME}}` filled — no placeholder text remains
- [ ] `{{YOUR_CONTACT_INFO}}` filled — working email address visible
- [ ] `{{DOMAIN_COUNT}}` filled — consistent value across all five drafts
- [ ] `{{PROPOSAL_URL}}` — real Gist URL inserted (not a placeholder)
- [ ] `{{EXEC_SUMMARY_URL}}` — real Gist URL inserted
- [ ] `{{LITIGATION_TRACKER_URL}}` — real Gist URL inserted (Emails 1 and 5 only)
- [ ] Contact-specific content placeholder filled (RECENT_JUST_SECURITY_ARTICLE etc.)
- [ ] Exactly one subject line in the subject field; other two options deleted from draft
- [ ] Exactly one path block `[PATH X]` retained; other two deleted
- [ ] Verified email address in To: field (see contact verification section below for corrections)
- [ ] No raw `{{` or `}}` characters remain anywhere in the email body

---

*Source: `PHASE_1_EMAIL_TEMPLATES.md` (created 2026-04-30). Contact verification corrections from `BATCH_1_CONTACT_VERIFICATION.md` (updated 2026-05-14) and web verification 2026-05-15.*
