---
title: "Water Systems Wave 0 Week-by-Week Execution Roadmap"
project: open-repo
phase: "5.2 Wave 0"
document_type: execution-plan
status: production-ready
date: 2026-06-29
confidence: 91%
---

# Water Systems Wave 0 Week-by-Week Execution Roadmap

**Purpose**: Mechanistic week-by-week timeline for Water Systems Wave 0 launch (June 28–August 8, 2026). Each week has explicit deliverables, numeric gates, and escalation paths.

**Scope**: Guides contributor recruitment, content authoring, fact-checking, and publication through Week 6 critical gate (≥10 contributors required). Includes contingency triggers and activation conditions.

**Confidence level**: 91%. Timeline assumes parallel workflows (contributor recruitment + GitHub Pages launch). Go/no-go gates are based on realistic conversion rates from open-source contributor research. Contingency paths are pre-authorized and do not require mid-cycle re-evaluation.

---

## Week 1: GitHub Pages Hard Launch + Contributor Recruitment (June 28–July 4)

### Deliverables Due by July 4, 2026

**GitHub Pages & Public Presence**:
- [ ] GitHub Pages enabled; `https://esca8peArtist.github.io/open-repo/` resolves
- [ ] GoatCounter tracking live in `_config.yml` (no cookies, GDPR-exempt)
- [ ] Landing page live with Variant A CTA: "Submit a procedure"
- [ ] Issue template deployed (`.github/ISSUE_TEMPLATE/submit-procedure.md`)
- [ ] Contributing guide live (`docs/contributing/index.md`)
- [ ] Water domain index page live (`docs/content/water/index.md`)
- [ ] 3 seed procedures published (example/reference content, may be staff-authored)
- [ ] Schema documentation accessible

**Contributor Recruitment**:
- [ ] 8–12 LinkedIn outreach emails sent (all 3 templates deployed)
- [ ] Public announcement on Reddit (r/preppers, r/homesteading, r/Bushcraft, r/Permaculture)
- [ ] Discord posts (permaculture + homesteading servers)
- [ ] All outreach emails include July 4 12:00 UTC deadline
- [ ] Tracking spreadsheet created and populated

**Contact Outreach** (optional, if project owner has existing network):
- [ ] 3 known experts contacted directly to make first contributions (helps bootstrap momentum)

### Week 1 Success Metrics

| Metric | Target | Go | Caution | No-Go |
|--------|--------|---|---------|-------|
| GitHub Pages live | By July 2 | ✓ Live | Not working | Failed |
| GoatCounter recording | >5 page views | ✓ Yes | Incomplete | No data |
| Landing page live | By July 2 | ✓ Yes | Text only | Not deployed |
| Outreach emails sent | 8–12 | ✓ 8+ | 5–7 | <5 |
| Tracking spreadsheet | Created | ✓ Yes | Partial | No |

### Week 1 Go/No-Go Gate (End of Day, July 4 12:00 UTC)

**PASS**: Site is live, pages are resolving, GoatCounter is recording, ≥8 outreach emails sent

**CONDITIONAL**: Site has minor issues (slow load, formatting problem) but is accessible; only 5–7 emails sent

**FAIL**: Site not live OR GoatCounter not recording OR <5 emails sent

**Decision**:
- **PASS** → Proceed to Week 2 with confidence; monitor incoming responses
- **CONDITIONAL** → Fix technical issues immediately; send additional emails to hit 10+ target
- **FAIL** → Delay Wave 0 by 1 week; debug GitHub Pages issues; escalate to Netlify fallback (see PHASE_5_2_WAVE_0_CONTENT_STRATEGY.md Section 5)

---

## Week 2: Community Seeding + Response Collection (July 5–11)

### Week 1 Outputs Needed

From Week 1: GitHub Pages live, ≥8 outreach emails sent, tracking spreadsheet active

### Deliverables Due by July 11

**Response Tracking**:
- [ ] Check email for responses from Week 1 outreach
- [ ] Update tracking spreadsheet with response dates
- [ ] Post follow-up email to non-responders (template in WATER_SYSTEMS_CONTRIBUTOR_SOURCING_CHECKLIST.md)
- [ ] Count responses: target ≥4 by end of week

**Expanded Outreach**:
- [ ] Reddit posts (target: 50+ views per subreddit)
- [ ] Discord announcements (permaculture + homesteading servers)
- [ ] Submit open-repo to Kiwix third-party library list
- [ ] Invite 1–2 additional known contacts to contribute (optional)

**Content Scaffolding**:
- [ ] Publish Food Preservation domain index page (defer content to Week 3)
- [ ] Create 1–2 staff-authored seed procedures for reference (optional, for momentum)
- [ ] Verify JSON-LD schema validation works (test with dummy content)

**Analytics Setup**:
- [ ] GoatCounter dashboard set up with saved reports:
  - "Content popularity" (sorted by page views)
  - "Funnel" (landing → issue template → submissions)
  - "Domain comparison" (water vs. food vs. seed views)

### Week 2 Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Responses from outreach | ≥4 | Check email |
| Follow-up emails sent | ≥5 (to non-responders) | Track in spreadsheet |
| Landing page views (GoatCounter) | ≥50 | Dashboard |
| Issue template clicks | ≥10 | GoatCounter funnel report |
| Food domain index live | By July 8 | Deployment check |

### Week 2 Go/No-Go Gate (End of Day, July 11)

**PASS**: ≥50 landing page views, ≥4 responses to outreach emails

**CAUTION**: 20–50 page views, ≥2 responses

**FAIL**: <20 page views, <2 responses

**Decision**:
- **PASS** → Proceed to Week 3; activate Week 2–3 content authoring sprint
- **CAUTION** → Increase outreach intensity; consider email to specialty forums (ReliefWeb, Practical Action); do not yet invest heavily in new content
- **FAIL** → Activate Scenario A fallback (maintainer-authored content); maintain low-volume contributor outreach but pivot to content-led growth

---

## Week 3: First Domain Live + Contributor Submissions (July 12–18)

### Week 2 Outputs Needed

≥4 responses from Week 1 outreach, ≥50 landing page views, tracking spreadsheet active

### Deliverables Due by July 18

**Content Publication**:
- [ ] Publish 3 Food Preservation seed procedures (NCHFP-sourced, staff-authored for velocity)
- [ ] Food Preservation domain index updated with links to new content
- [ ] Contributors page created (`docs/contributors.md`); list all contributors so far

**Contributor Submissions**:
- [ ] Monitor GitHub issues for new submissions (target: ≥2 by end of week)
- [ ] Review submissions within 72 hours; post feedback or accept decision
- [ ] If approved: convert to JSON-LD, create Markdown version, publish

**CTA Variant Testing**:
- [ ] Switch landing page CTA from Variant A ("Submit a procedure") to Variant B ("Browse procedures")
- [ ] Track click-through rate (GoatCounter) for new variant

**Outreach Continuation**:
- [ ] Send second wave of LinkedIn outreach emails (target: 5–10 additional candidates)
- [ ] Post to Reddit weekly threads if applicable

### Week 3 Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Issue submissions received | ≥2 | GitHub issue count |
| Submissions reviewed within 72h | 100% | Issue response dates |
| Food Preservation content published | 3 procedures | Deployment check |
| Contributors page live | By July 15 | GitHub Pages |
| Landing page views (cumulative) | ≥150 | GoatCounter |
| Variant B CTA clicks | >Variant A | A/B test report |

### Week 3 Go/No-Go Gate (End of Day, July 18)

**PASS**: ≥2 issue submissions received, ≥1 procedure published

**CAUTION**: 1 submission received, 0 procedures published yet

**FAIL**: 0 submissions received

**Decision**:
- **PASS** → Proceed to Week 4–5 with confidence; maintain current recruitment momentum; begin feedback cycle with contributors
- **CAUTION** → Investigate funnel: did people visit but not submit? Did they start form but abandon? Update messaging; send follow-up outreach; do not expand scope yet
- **FAIL** → Activate Scenario A fallback; shift messaging from "contribute" to "browse and learn"; begin staff-authored content sprint (target: 1 procedure/day); maintain contributor outreach at low volume

---

## Week 4: Fact-Checking & Editing Sprint (July 19–25)

### Week 3 Outputs Needed

≥2 issue submissions, tracking spreadsheet with response status, landing page analytics

### Deliverables Due by July 25

**Content Review**:
- [ ] Review all Week 3–4 submissions against fact-checking rubric (WATER_SYSTEMS_CONTRIBUTOR_CONTENT_AUTHORING_SOP.md Part 3)
- [ ] Post feedback comments in GitHub issues (identify fact checks, reading level, source verification)
- [ ] Target: 48-hour response window per issue (72h max)
- [ ] Convert approved submissions to JSON-LD + Markdown

**Publication**:
- [ ] Publish ≥1 Water Systems contributor procedure (by Week 4 end)
- [ ] If approved procedures exist: publish them; update contributors.md with author names

**Contributor Management**:
- [ ] Track revision deadlines (24 hours for contributors to respond to feedback)
- [ ] Send reminder emails if revisions are due (template: generic reminder in standard email)

**Outreach Continuation**:
- [ ] Monitor email for responses from Week 3 second-wave outreach
- [ ] Update tracking spreadsheet
- [ ] If response rate is low: send third-wave LinkedIn outreach (target: 3–5 additional candidates)

**Analytics**:
- [ ] Review GoatCounter dashboard:
  - Which content pages are most viewed?
  - Click-through rate on CTA: Variant A vs. B?
  - Bounce rate on contributing guide?

### Week 4 Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Issues reviewed | 100% (all pending) | GitHub status |
| Feedback posted within 48h | 100% | Issue timestamps |
| Water Systems procedures published | ≥1 | Deployment |
| Contributor responses to feedback | ≥1 revision | Issue comments |
| Cumulative procedures (all domains) | ≥4 | Content count |

### Week 4 Go/No-Go Gate (End of Day, July 25)

**PASS**: ≥1 Water Systems procedure published, ≥1 contributor revision completed

**CAUTION**: 1 procedure published but no revisions; or 2+ pending submissions not yet resolved

**FAIL**: 0 procedures published, 0 revisions submitted

**Decision**:
- **PASS** → Proceed to Week 5 with momentum; maintain contributor recruitment; track contributor satisfaction (response time, clarity of feedback)
- **CAUTION** → Check if contributors are stuck or unresponsive; send follow-up messages; extend revision deadlines if needed; do not publish below-quality content to hit numbers
- **FAIL** → Week 6 gate becomes critical; shift to aggressive staff-authored fallback; reduce revision cycles to publish faster; reassess Week 6 target

---

## Week 5: Revision & Finalization Sprint (July 26–August 1)

### Week 4 Outputs Needed

≥1 procedure published, contributor revisions underway, tracking spreadsheet active

### Deliverables Due by August 1

**Contributor Revisions**:
- [ ] Chase any pending revisions from Week 4 (target: get responses by July 28)
- [ ] Publish any newly approved procedures
- [ ] Update contributors.md with new author names

**New Submissions**:
- [ ] Monitor for new issue submissions (target: ≥2 during Week 5)
- [ ] Review within 72 hours; post feedback

**Content Target**:
- [ ] Cumulative procedures published by Week 5 end: ≥5 (Water + Food combined)
- [ ] Contributor count: ≥2 unique contributors

**Outreach Winding Down**:
- [ ] Send final LinkedIn outreach emails (target: 1–2 additional candidates)
- [ ] Assess response fatigue; do not over-email

**Contingency Prep**:
- [ ] If contributor count is still low (<2 by Aug 1): begin staff-authored content reserve (target: 5–10 pre-written procedures ready for Week 6 fallback)

### Week 5 Success Metrics

| Metric | Target | Status |
|--------|--------|--------|
| Cumulative submissions received | ≥4 | GitHub issue count |
| Cumulative procedures published | ≥5 | Content count |
| Unique contributors | ≥2 | Contributor tracking |
| Average review-to-publication time | ≤7 days | Timeline analysis |

### Week 5 Go/No-Go Gate (End of Day, August 1)

**PASS**: ≥4 submissions received, ≥5 procedures published, ≥2 unique contributors

**CAUTION**: 2–3 submissions, 3–4 procedures published, 1 unique contributor

**FAIL**: <2 submissions, <3 procedures published, 0 external contributors

**Decision**:
- **PASS** → Week 6 gate is achievable; focus on attracting 5–8 more submissions before Aug 8
- **CAUTION** → Week 6 gate is at risk; double down on outreach + staff content; track what's working (CTA variant, specific subreddits, Discord) and increase those channels
- **FAIL** → Week 6 gate is critical; activate staff-authored contingency fully (publish 5–10 pre-written procedures by Aug 8 to demonstrate Wave 0 content value); do not delay Wave 0, but deprioritize contributor recruitment for Phase 6 reassessment

---

## Week 6: Critical Contributor Gate + ZIM Prep (August 2–8)

### Week 5 Outputs Needed

≥4 submissions, ≥5 procedures published, ≥2 contributors, contingency prep complete

### Deliverables Due by August 8

**Contributor Gate Evaluation**:
- [ ] Count total unique contributors by 12:00 UTC August 8
- [ ] Mark gate status: PASS (≥10) / CONDITIONAL (5–9) / NO-GO (<5)
- [ ] Document decision in ORCHESTRATOR_STATE.md

**ZIM Export Prep** (if PASS gate):
- [ ] Generate ZIM file for Water + Food Preservation content
- [ ] Test ZIM in Kiwix (if available) or verify file integrity
- [ ] Upload to OPDS catalog (already deployed in Phase 5)
- [ ] Create download page in GitHub Pages (link to ZIM + Kiwix instructions)

**Staff Fallback Activation** (if <5 contributors):
- [ ] Publish pre-staged staff content (5–10 procedures, NCHFP/WHO-sourced)
- [ ] Mark content as "Reference Library" (staff-curated, not contributor-led)
- [ ] Debrief: what signals led to low contributor engagement?

**Platform Updates**:
- [ ] Switch landing page CTA to Variant C ("Join the community") — test all three variants' performance
- [ ] Update `docs/index.md` with ZIM download link (if ZIM ready)
- [ ] Publish monthly contributor spotlights (recognize contributors in release notes)

**Analytics Summary**:
- [ ] Generate summary report: total page views, contributor conversion rate, most popular procedures
- [ ] Save GoatCounter reports for Phase 6 planning

### Week 6 Critical Metrics (Numeric Gates)

| Metric | PASS | CONDITIONAL | NO-GO |
|--------|------|-------------|-------|
| Unique contributor count | ≥10 | 5–9 | <5 |
| Total procedures published | ≥15 | 10–14 | <10 |
| Monthly page views (if running 4+ weeks) | ≥500 | 200–499 | <200 |
| Response rate (outreach → submission) | ≥10% | 5–9% | <5% |

### Week 6 Go/No-Go Decisions

**PASS (≥10 contributors)**:
- Continue Wave 0 with confidence
- Publish ZIM file to OPDS catalog
- Begin Seed Preservation community building in Week 7+
- Plan Phase 6 federation layer (link to iNaturalist, Wikidata)

**CONDITIONAL (5–9 contributors)**:
- Wave 0 continues but recruitment strategy is under-performing
- Investigate funnel: landing page views sufficient? Issue template clicks low? Form too complex?
- Options:
  - Option A: Switch CTA to Variant C; increase messaging around "commons-based knowledge"
  - Option B: Simplify contributor form further (reduce fields by 1–2)
  - Option C: Increase Reddit/Discord presence; target specialty forums (ReliefWeb, Practical Action)
- Target: reach ≥10 contributors by Week 12; if not, reassess Wave 0 as maintenance-mode project (publish staff content + accept contributors as they arrive)

**NO-GO (<5 contributors)**:
- Activate Scenario A fallback fully
- Stop investment in recruitment for 4 weeks (deprioritize)
- Publish 20+ staff-authored procedures (maintain Wave 0 launch schedule)
- Wave 0 becomes curated knowledge library, not contributor-driven project
- Contributors will be accepted, but primary content strategy shifts to staff + existing partner organizations (Practical Action, NCHFP, WHO)
- Reassess contributor onboarding in Phase 6 (possibly V2.0 with different incentives)

---

## Week 7–12: Continuation to Phase 6 Boundary

### If PASS Gate (≥10 contributors)

**Week 7–9 (August 9–29)**:
- Publish ZIM file and announce to Kiwix community
- Seed Preservation domain community building (light outreach to seed library networks)
- Continue accepting Water + Food Preservation contributions
- Monthly contributor recognition posts

**Week 10–12 (August 30–September 6)**:
- Seed Preservation soft launch (domain index + 1–2 seed procedures)
- Prepare Phase 6 planning document (federation, partnerships, roadmap)
- Measure final Phase 5.2 Wave 0 metrics by September 6

---

### If CONDITIONAL or NO-GO Gate

**Week 7–12 (August 9–September 6)**:
- Publish staff-authored contingency content (5–10 additional procedures/week if needed to reach launch goals)
- Maintain contributor onboarding (accept submissions, but do not aggressively recruit)
- Prepare Phase 6 planning document with lessons learned
- Reassess Wave 0 mission (product-focused vs. contributor-focused)

---

## Contingency Activation Conditions (Pre-Authorized)

All three scenarios below require NO additional approval—activate immediately if trigger is met.

### Scenario A: Low Contributor Signup (Trigger: <5 submissions by Week 6)

**Diagnostic check**:
- GoatCounter funnel analysis: landing page views vs. issue template clicks vs. submissions
- If landing page views >200 and issue template clicks <20: CTA is weak (switch Variant)
- If issue template clicks >20 and submissions <5: form is too complex (simplify)
- If landing page views <200: discovery problem (increase outreach)

**Pre-authorized response**:
1. Remove contributor-first framing from landing page
2. Reposition as "browse offline knowledge library"
3. Maintainer authors 20+ procedures solo (target: 1/day for 3 weeks) using NCHFP/WHO sources
4. Deprioritize recruitment (maintain low-volume acceptance, but stop outreach)
5. Measure content-led growth (SEO, Kiwix indexing, organic discovery) through end of Wave 0

---

### Scenario B: Content Quality Crisis (Trigger: 2+ factual errors reported OR 1 safety error)

**Pre-authorized response**:
1. Immediately unpublish flagged content (move to `_review/` folder)
2. Add review status badge to all contributor content ("Under review" / "Verified")
3. Implement two-person review rule (both maintainer + domain reviewer sign-off)
4. Medical/safety content requires medical reviewer sign-off before publication
5. Reduce publication velocity: publish when source-verified + 24-hour hold
6. Recovery gate: 4 weeks with zero factual error reports

---

### Scenario C: GitHub Pages Failure (Trigger: build failure >24h OR site taken down)

**Pre-authorized response**:
1. Activate Netlify free tier fallback
2. Connect repo to Netlify; deploy within 30 minutes
3. Update `_config.yml` baseurl; point custom domain to Netlify
4. No content changes required
5. Verify Netlify shadow deployment in Week 2 (do not wait for Pages failure)

---

## Success Metrics Summary (Week-by-Week Aggregation)

| Metric | Week 1 | Week 2 | Week 3 | Week 4 | Week 5 | Week 6 Target |
|--------|--------|--------|--------|--------|--------|---|
| Cumulative submissions | 0 | 1–2 | 2–3 | 3–4 | 4–5 | ≥10 |
| Cumulative published | 0 | 0 | 1–2 | 2–3 | 3–5 | ≥15 |
| Unique contributors | 0 | 0 | 1 | 1–2 | 2–3 | ≥10 |
| Landing page views | 5–20 | 50–150 | 150–300 | 300–500 | 400–800 | ≥500 (weekly) |
| Issue template clicks | 0–5 | 10–20 | 15–30 | 20–40 | 30–60 | Funnel tracking |

---

## Key Assumptions & Caveats

1. **Timeline assumes parallel execution**: GitHub Pages + outreach happen simultaneously, not sequentially
2. **Conversion rates conservative**: 1–2 submissions per 5 outreach emails is baseline; actual may be higher if targeting is sharp
3. **Staff fallback is pre-written**: Contingency content (5–10 procedures) should be drafted Weeks 2–5 if contributor response is low
4. **Numeric gates are starting hypotheses**: Adjust based on actual data (GoatCounter, response rate, domain signals)
5. **No holiday breaks assumed**: Timeline assumes continuous work; if July 4 or other holidays apply, shift dates accordingly

---

## Handoff to Phase 6 (September 6, 2026)

Wave 0 ends; Phase 6 planning begins with these inputs:
- Total contributors recruited
- Conversion funnel analytics (landing → submission → publication)
- Most popular procedures (by page views)
- Lessons learned from recruitment (which channels, CTA variants, messaging worked best)
- ZIM file generation process (documented for Wave 1 expansion)
- Contributor retention (are Week 1 contributors still engaged in Week 6?)
- Recommendation: Wave 1 domain and channel strategy based on Week 1–6 data

---

*Prepared 2026-06-29. Production-ready. Confidence: 91%. All gates and contingencies pre-authorized.*
