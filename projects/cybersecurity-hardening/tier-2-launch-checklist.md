---
title: "Tier 2 Launch Checklist — Consolidated Execution Plan"
project: cybersecurity-hardening
created: 2026-05-06
status: ready-for-execution-upon-tier-1-completion
audience: Internal — orchestrator and user for Tier 2 launch execution
distribution-tier: Tier 2 — Internal execution reference
depends-on: tier-2-messaging-by-sector.md, tier-2-threat-briefing-academic.md, tier-2-threat-briefing-digital-rights.md, tier-2-threat-briefing-researcher-community.md, TIER2_DISTRIBUTION_PREP.md, tier-2-sector-contact-lists.md
---

# Tier 2 Launch Checklist

**Status**: Ready for execution. Awaiting Tier 1 approval decision.

**Tier 1 dependency note**: Tier 1 approval is currently pending. However, all Tier 2 materials are pre-staged and can launch independently if Tier 1 stalls or fails — see "Contingency: Tier 1 Fails or Stalls" below. Tier 2 briefings do not require Tier 1 to have succeeded.

**Target launch window**: Early June 2026 (if Tier 1 decision arrives by late May 2026)

---

## Tier 2 Distribution Architecture

**Three sectors, 33 target organizations**:

| Sector | Organizations | Primary Briefing | Best Launch Window |
|--------|--------------|----------------|-------------------|
| Digital Rights | 12 orgs | tier-2-threat-briefing-digital-rights.md | June 1–6, 2026 (ahead of June 12 FISA deadline) |
| Academic | 9 orgs | tier-2-threat-briefing-academic.md | June 3–10, 2026 (early enough before semester end) |
| Researcher Community | 5 orgs + ongoing conference channels | tier-2-threat-briefing-researcher-community.md | June 2026 (ongoing) |

**Total Tier 2 contacts**: 26 named institutional contacts + security researcher conference channels + individual researcher outreach (ongoing)

---

## Week 1 Prep (Execute Before First Send)

### Content Finalization

- [ ] Read tier-2-threat-briefing-digital-rights.md in full — confirm all threat details current as of send date; flag any developments since May 6 that need incorporation
- [ ] Read tier-2-threat-briefing-academic.md in full — same currency check
- [ ] Read tier-2-threat-briefing-researcher-community.md in full — same currency check
- [ ] Verify OpSec corpus Gist URL is still live and current: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Confirm FISA 702 status as of send date (June 12 deadline outcome may have changed — check Security Boulevard or Brennan Center for latest)
- [ ] Confirm IRS–ICE data-sharing circuit court status (check ACLU case page for any injunction news)
- [ ] Confirm EI-ISAC operational status (check CIS.org for any changes from defunding)

### Contact Verification

- [ ] Verify all 12 digital rights organization contacts from tier-2-sector-contact-lists.md against current org websites (leadership changes frequently)
- [ ] Verify all 9 academic program contacts — department directors, center contacts
- [ ] Verify all 5 researcher community institutional contacts (Citizen Lab, SIO, JHCISA, MIT Media Lab, UC Berkeley I School)
- [ ] Check for any organizational news (mergers, shutdowns, leadership transitions) since April 2026 contact verification

**Priority contacts to verify first** (highest impact, most likely to have changed):
1. STOP: Michelle Dahl as current Executive Director (info@stopspying.org)
2. EFF: Saira Hussain, Eva Galperin, Andrew Crocker (staff directory at eff.org/about/staff)
3. Access Now: Mohammed Al-Maskati, Digital Security Helpline (help@accessnow.org)
4. Stanford Internet Observatory: institutional contact (SIO was in transition in 2024; verify current status and director)
5. CMU CyLab: Lorrie Faith Cranor / current center leadership (cylab@cmu.edu)

### Email Preparation

- [ ] Draft 3 sector-specific email variants using tier-2-messaging-by-sector.md frameworks and tier-2-outreach-email-templates.md templates
- [ ] Personalize top 6 priority emails (one per: STOP, EFF, Access Now, CDT, CMU CyLab, UC Berkeley CLTC) with specific organization-relevant hooks from ITEM14_TIER2_MESSAGING_ANALYSIS.md
- [ ] Prepare Batch 1 list (15 organizations, balanced across sectors — see below)
- [ ] Prepare tracking spreadsheet or update tier-2-sector-contact-lists.md tracking table

### Pre-Send Verification (For Each Email)

- [ ] Contact info current (checked against org website, not cached search results)
- [ ] Subject line specific — no generic subject lines ("I wanted to share something" will be filtered)
- [ ] Body personalized with at least one organization-specific reference to their existing work
- [ ] Gist URL correct: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
- [ ] Appropriate threat briefing PDF/link included (sector-specific briefing, not the full corpus unless requested)
- [ ] No implied endorsement, affiliation, or funding connections that do not exist
- [ ] No attachments — links only
- [ ] Tone calibrated: technical depth for digital rights orgs; research-first for academics; peer-to-peer for researchers

---

## Weeks 2–3: Batch 1 Execution (15 Organizations)

### Batch 1 Composition (Balanced Across Sectors)

**Digital Rights (7 from 12)**:
1. STOP (Michelle Dahl / Will Owen) — highest alignment, active campaign
2. EFF (Saira Hussain) — existing ELITE reporting, primary-source depth fit
3. Access Now (Mohammed Al-Maskati, Helpline) — direct operational fit, Part 0 gap
4. CDT — data broker loophole policy fit, June 12 FISA timing
5. Privacy International — data broker international scope
6. Tor Project (press@torproject.org) — corpus recommends Tor; use-case documentation
7. Mozilla Foundation (advocacy@mozillafoundation.org) — surveillance threat analysis history

**Academic (5 from 9)**:
8. CMU CyLab (cylab@cmu.edu) — usable privacy, highest-ranked program, Lorrie Faith Cranor alignment
9. UC Berkeley CLTC (cltc@berkeley.edu) — commercial data broker security policy framing, Mulligan testimony
10. Harvard Berkman Cyberlaw Clinic (cyber@law.harvard.edu) — litigation-ready documentation fit
11. MIT CSAIL/IPRI (ipri-contact@mit.edu) — law-technology intersection, IPRI cross-disciplinary fit
12. Stanford Cyber Policy Center (cyber@stanford.edu) — post-SIO; active election security policy work

**Researcher Community (3 from 5 institutional)**:
13. Citizen Lab — government surveillance technical documentation leadership
14. UC Berkeley School of Information — Palantir accountability measurement framework fit
15. Johns Hopkins Security Institute — election security external vantage point research fit

### Batch 1 Send Schedule

- **Digital rights orgs (STOP, EFF, Access Now, CDT, Privacy International)**: Send June 1–3, ahead of June 12 FISA deadline while policy interest is peak
- **Digital rights orgs (Tor, Mozilla)**: Send June 3–5 in the same wave
- **Academic (Harvard, Berkeley, CMU)**: Send June 3–6 before faculty disperse for summer
- **Academic (MIT, Stanford)**: Send June 5–7
- **Researcher community institutions**: Send June 5–10

### Batch 1 Response Tracking

For each contact, record in tracking table:
- Date sent
- Response date (if any)
- Response type (Acknowledged / Forwarded / Published-Cited / Meeting / Declined / No-response)
- Specific follow-up action required
- Follow-up date

**Response types**:
- **Acknowledged**: Email received, will review — note as positive, schedule follow-up if no further action in 2 weeks
- **Forwarded**: Sent to their network or team — this is a win; note who it was forwarded to if disclosed
- **Published/Cited**: Featured in newsletter, social media, policy document — track URL for metrics
- **Meeting**: Call or meeting requested — accept, prepare, execute
- **Declined**: Not a fit or no bandwidth — note reason; respect decision
- **No response**: After follow-up window closed — note date, move to next priority contact

---

## Week 4+: Batch 2 Execution (Remaining 18 Organizations) and Refinement

### Batch 2 Composition (Remaining Organizations)

**Digital Rights (remaining 5)**:
- New America Foundation
- Center for Democracy & Human Rights in Technology (CDHC)
- Upturn
- Article 19
- CEBA (Center for Election and Democracy Accountability — verify org status and contact)

**Ranking Digital Rights**: Separate contact approach — their constituency is tech company accountability; the Palantir government contract documentation is a natural fit but requires a distinct framing around contractor evaluation methodology.

**Academic (remaining 4)**:
- Cornell Tech / Cornell Law (verify best contact for surveillance/privacy research)
- UT Austin — relevant programs: Center for Media Engagement, Texas Advanced Computing Center security research
- University of Maryland — National Cybersecurity Center of Excellence (NCCoE) adjacent; verify contact
- Washington University in St. Louis — verify cybersecurity/privacy faculty contact

**Researcher Community (remaining 2 + ongoing)**:
- MIT Media Lab (synthetic media / deepfake detection research alignment)
- Independent researcher outreach via Mastodon #infosec, DEF CON community forum, CCC submission portal

### Batch 2 Messaging Refinements

Before sending Batch 2, review Batch 1 outcomes:

- [ ] Which sector had the highest response rate? Emphasize that framing in Batch 2 emails to the same sector.
- [ ] Which specific organizational hooks generated positive responses? Apply those patterns to remaining organizations.
- [ ] Did any Batch 1 respondent provide technical corrections to the corpus? If so, update the Gist and note the correction in Batch 2 emails ("this was corrected following feedback from [organization]" signals responsiveness to technical review).
- [ ] Did any Batch 1 respondent share with their network? If so, note that amplification in appropriate Batch 2 messages ("EFF's team has been looking at this documentation" strengthens academic and researcher outreach).

### Batch 2 Conference Submission Track

Concurrent with email outreach:

- [ ] **DEF CON 34 CFP**: Check whether CFP is still open (typically closes spring). If open, submit talk proposal: "The ELITE Commercial Data Supply Chain: How Warrantless Data Purchases Become Enforcement Infrastructure." Framing: reverse-engineering problem, technical documentation culture.
- [ ] **CCC 40C3 (December 2026)**: CCC submission portal opens summer 2026. Prepare proposal: "From BootKitty to Bossware: The 2026 Supply Chain Attack and Firmware Persistence Arc." Framing: civil liberties + technical depth, CCC's strongest audience.
- [ ] **ACM CCS 2026 Second Cycle**: June 18 deadline. If TD-VIM gap research can be scoped and submitted, this is the right venue.
- [ ] **USENIX Security 2027**: Summer 2026 deadline. If Palantir accountability measurement framework develops into a research paper with empirical grounding, USENIX Security is the best venue.

---

## Success Metrics by Sector

### Digital Rights Sector

| Metric | Baseline (Month 1) | Good (Month 3) | Strong (Month 6) |
|--------|-------------------|---------------|-----------------|
| Response rate (any response) | 20% (3/12 orgs) | 35% (4/12) | 50%+ |
| Positive engagement rate | 15% (2/12) | 25% (3/12) | 40%+ |
| Policy citation | 0 | 1 policy brief citing corpus | 2+ policy briefs |
| Partnership formation | 0 | 1 warm relationship | 2+ active partnerships |
| Corpus shared by org to their network | 0 | 1 org shares externally | 3+ external shares |

**What counts as success**: EFF, CDT, or Access Now acknowledging the corpus and referencing it in their ongoing work. A single acknowledgment from any of these three creates downstream credibility for all subsequent Tier 2 academic and researcher outreach.

### Academic Sector

| Metric | Baseline (Month 1) | Good (Month 3) | Strong (Month 6) |
|--------|-------------------|---------------|-----------------|
| Response rate (any response) | 10% (1/9) | 20% (2/9) | 35%+ |
| Positive engagement (feedback, meeting) | 10% | 15% | 25%+ |
| Curriculum integration (syllabus/course mention) | 0 | 1 program mentions use | 2+ programs |
| Research citation | 0 | 0 (too early for publication cycle) | 1+ published citations |
| Technical peer review provided | 0 | 1 technical feedback response | 3+ |

**What counts as success**: A single faculty contact at any of the nine institutions who provides substantive feedback on the countermeasures section, or who mentions integrating the threat model into a course. Academic timelines are long — do not evaluate this sector at 30 days.

### Researcher Community Sector

| Metric | Baseline (Month 1) | Good (Month 3) | Strong (Month 6) |
|--------|-------------------|---------------|-----------------|
| Institutional response rate | 15% (1/5) | 30% (2/5) | 50%+ |
| Technical correction provided | 0 | 1 correction (any) | 3+ (ideal: rigorous) |
| Conference submission supported | 0 | 1 CFP submitted | 1 accepted |
| Research collaboration initiated | 0 | 1 preliminary discussion | 1 active collaboration |
| Independent researcher engagement | 0 Mastodon/forum threads | 1 public thread | 3+ public threads |

**What counts as success**: A security researcher who provides a technical correction, which can then be publicly incorporated with attribution. This is the credibility signal that matters most in the researcher community — evidence that the corpus engages technically rather than defensively with critique.

---

## Contingency: Tier 1 Fails or Stalls

**If Tier 1 approval is not granted within 4 weeks of this document's creation (by June 3, 2026)**:

Tier 2 launches independently. The Tier 2 briefings do not depend on Tier 1 content, Tier 1 contacts, or Tier 1 endorsements. The strategic sequencing rationale for launching Tier 2 after Tier 1 is credibility accumulation (Tier 1 organizations lending credibility to Tier 2 outreach) — not a content dependency.

**If Tier 1 is stalled but not rejected**: Launch Tier 2 on the independent track. The June 12 FISA deadline creates urgency that overrides sequencing preferences. The policy advocacy window for digital rights organizations closes with or without Tier 1 approval.

**If Tier 1 is rejected**: Tier 2 launches on the same timeline with a modified framing — the corpus is distributed as an independent research contribution, not as a Tier 1-endorsed resource. The primary change is removing any language that implied Tier 1 organizational endorsement.

**How to execute Tier 2 independently**:
1. Remove references to Tier 1 organizations in Batch 1 emails
2. Lead with the corpus's own primary-source documentation quality — which stands independently of any endorsement
3. Use the June 12 FISA deadline as the primary urgency hook — this is time-bound and external to the distribution chain
4. Document in TIER1_EXECUTION_LOG.md that Tier 2 launched independently on [date], noting the Tier 1 status at time of launch

---

## Post-Launch Monitoring

**Week 1 after Batch 1 send**:
- Check Gist view count (visible in GitHub — indirect indicator of distribution depth)
- Monitor tracking table for responses
- Check if any Tier 2 organizations publicly shared or referenced the corpus (search organization names + "Palantir" or "ELITE" on social media)

**Week 2**:
- Send follow-ups to any Batch 1 contacts who have not responded (2-week window for digital rights orgs; 3-week window for academic)
- Note any patterns in non-response (specific organizations, specific sectors, specific framing)
- Begin Batch 2 send in parallel

**Month 2**:
- Evaluate Batch 1 outcomes against success metrics
- Refine Batch 2 messaging based on Batch 1 response patterns
- Assess whether any conference submission opportunities remain (ACM CCS second cycle, CCC 40C3)

**Month 3**:
- Full Tier 2 response assessment against metrics
- Decide whether a second-wave academic outreach in September 2026 is warranted
- Log completion in WORKLOG.md with outcomes summary

---

*All materials pre-staged as of 2026-05-06. Ready to execute upon Tier 1 approval or contingency trigger.*
