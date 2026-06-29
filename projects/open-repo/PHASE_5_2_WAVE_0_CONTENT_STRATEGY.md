---
title: "Phase 5.2 Wave 0 Content Strategy"
project: open-repo
phase: "5.2 Wave 0"
document_type: strategy
status: draft-for-review
date: 2026-06-28
confidence: 84%
word_count: ~2800
---

# Phase 5.2 Wave 0 Content Strategy

**Purpose**: Operational strategy for the first 8–12 weeks of open-repo's live public operation on GitHub Pages. Covers domain prioritization, contributor onboarding, platform mechanics, timeline with go/no-go gates, and pre-authorized risk rollbacks.

**Prerequisite state**: Phase 5 complete. GitHub Pages live at `https://esca8peArtist.github.io/open-repo/`. Five content schemas published at stable URLs. Schema documentation (879 lines) live. No server hosting required.

**Confidence level**: 84%. Domain gap analysis draws on search signal and comparable-project precedent. Contributor conversion estimates are based on open-source onboarding research (see Sources). Numeric thresholds are grounded assumptions, not measurement — treat as starting hypotheses, not targets carved in stone.

---

## Section 1 — Content Domains Assessment

### The Prioritization Problem

Open-repo already has schemas for five domains: Medical, Botanical Knowledge, Water Systems, Seed Preservation, and Food Preservation. The Wave 0 decision is not which schemas to build — those exist — but which domain gets the first real content, the first public contributor push, and the first ZIM file published to the OPDS catalog. Getting this wrong wastes the bootstrap window when initial community interest is highest.

Four criteria drive the recommendation:

1. **Gap in existing public repositories**: Content that Wikipedia, Wikimedia Commons, or Kiwix's existing library already covers well should not be Wave 0's focus. Open-repo adds value at the edges of that coverage.
2. **Community interest signal from comparable projects**: Domains where other open-knowledge projects (Practical Action, WHO, OpenStreetMap) have generated contributor momentum are likelier to recruit early contributors.
3. **Schema complexity and review overhead**: The lighter the required expert review, the faster Wave 0 can publish content. Domains requiring medical or legal sign-off gate publication on reviewer availability.
4. **Contributor recruitment feasibility**: Domains with active, identifiable online communities (Reddit, Discord, Signal groups) give a recruiting path. Domains without an online community require building one from scratch — a Wave 1 problem, not Wave 0.

### The Assessment

**Domain A — Water Systems (Recommended Priority 1)**

The gap here is specific and well-documented: Wikipedia's water-related articles cover the science of water treatment but are sparse on operational procedures ("how to build a slow sand filter from local materials," "how to test water for biological contamination without a lab"). Kiwix's offline library includes the Wikipedia Water article but not the WHO's practical field guidance (WASH manuals, Emergency Water Supply field guides). Practical Action's technical briefs on water systems are licensed CC BY and have no structured machine-readable form anywhere.

Community interest signal: WASH (Water, Sanitation, Hygiene) has active practitioner communities on ReliefWeb, the Humanitarian Data Exchange, and several NGO mailing lists. The global infrastructure for recruiting contributors — public health workers, humanitarian field staff, wilderness educators — is reachable within 2–3 outreach steps.

Schema complexity is moderate. Water systems procedures do not require licensed professional sign-off for most operational content (boiling, filtration, chemical treatment, rainwater harvesting) — they require accurate sourcing and plain-language clarity. Safety disclaimers are required; expert endorsement is not a hard gate for Wave 0.

Contributor recruitment feasibility: high. The audience includes wilderness first responders, disaster preparedness communities, permaculture designers, and international development practitioners — all with established online presences.

**Domain B — Food Preservation (Recommended Priority 2)**

The gap is narrower but deep. Ball canning guides and NCHFP (National Center for Home Food Preservation) publications are the authoritative sources for home preservation in the US context but are not available offline in structured form. The ZIM library has no food preservation archive. The content type — recipe + procedure hybrid — maps cleanly to schemas that already exist.

Community interest signal: home food preservation has experienced documented growth since 2020 (supply chain anxiety, homesteading movement) and has active communities on Reddit (/r/canning, /r/fermentation, /r/homestead) with 1M+ aggregate members. These communities regularly discuss wanting offline, authoritative reference material.

Schema complexity: low for most content. Canning safety does require following tested USDA/NCHFP procedures exactly (incorrect processing temperatures cause botulism). However, the expert review gate is already met for content sourced directly from NCHFP (US government, public domain) or Ball Blue Book (widely licensed for educational use). No individual physician reviewer is required.

Contributor recruitment feasibility: very high. The community already knows they want this — the challenge is discovery, not motivation.

**Domain C — Seed Preservation (Priority 3, begin community building in Week 6)**

The gap is real but more fragmented. Seed Savers Exchange and the Open Source Seed Initiative have valuable content, but it is not structured for offline use and is not uniformly open-licensed. iNaturalist covers species identification but not seed-saving methodology. Wikipedia's articles on seed saving are encyclopedic rather than procedural.

Schema complexity is moderate-high. Seed viability data, humidity and temperature storage parameters, and genetic isolation distances require domain-specific accuracy. Seed saving communities are expert-heavy; contributors are likelier to be skilled practitioners than first-time open-source contributors.

Community signal: active but smaller than water/food. Seed saving has a distinct culture of reciprocal sharing (seed swaps, community seed libraries) that is philosophically aligned with open-repo's values. This is a domain where federated institutional partners (community seed libraries, university extension programs) matter more than individual contributors.

**Recommendation**: Launch Wave 0 with Water Systems as Priority 1, Food Preservation as Priority 2 (weeks 4–8), and Seed Preservation as a community-building target for weeks 6–12 with a Phase 6 content gate. Medical and Botanical Knowledge remain in schema-ready standby; Medical requires reviewer outreach to complete (see `medical-reviewer-outreach-draft.md`) and should not be gated on Wave 0 timeline.

---

## Section 2 — Contributor Onboarding Strategy

### Contributor Profile

Wave 0 serves two contributor types simultaneously, and the onboarding path must not conflate them.

**Type A — Content Authors** are practitioners with domain knowledge who may have no GitHub experience. A wilderness first responder knows how to purify water by boiling; a home canner has made jam 200 times. They do not know what a pull request is. Target time from discovery to first contribution: 5 minutes. The mechanism is a Google Form or GitHub Issue template that accepts plain text and asks four questions: What is the procedure? What is your source? What domain is it in? Do you have any evidence this information is accurate?

**Type B — Technical Contributors** are developers or structured-content writers comfortable with JSON, Markdown, and GitHub. They can submit validated JSON-LD objects that conform to the published schemas. These contributors self-onboard via the existing schema documentation. Target time from discovery to first pull request: 30 minutes.

Wave 0 should invest disproportionately in Type A. Type B contributors will find their way once the project is visible. Type A contributors will not arrive unless the entry friction is actively removed.

### Onboarding Workflow

**Discovery path**: GitHub Pages landing page with a visible "Submit a procedure" button as the primary CTA. This button links to a pre-filled GitHub Issue template titled "Submit: [domain] procedure." The issue template is the contribution unit.

**Issue template contents** (full template in `WAVE_0_CONTRIBUTOR_ONBOARDING_TEMPLATE.md`):
- Procedure title (what is this for?)
- Domain (Water / Food Preservation / Seed Preservation / Other)
- Source (where does this information come from? URL or book citation)
- Content (the actual procedure, in plain language — 3 to 20 steps)
- License confirmation (checkbox: "I confirm this is my own work OR the source I cited is openly licensed")

Estimated completion time: 3–5 minutes for a practitioner who already knows the procedure.

**Review workflow**: A maintainer (initially the project owner) reviews each issue within 72 hours. Decision options:
1. Accept as-is — maintainer converts to JSON-LD, tags `content-ready`, pushes to content branch
2. Request clarification — maintainer asks one specific question in the issue thread
3. Decline with reason — clear explanation, invitation to revise

The conversion from plain-text issue to JSON-LD is done by the maintainer for Type A contributors. This is intentional: the contributor's job is knowledge, not schema compliance. Remove this burden entirely in Wave 0.

**Quality gates**: Two-stage. Stage 1 is source verification (is the cited source real and does the procedure match it?). Stage 2 is technical review (does the JSON-LD validate against the schema?). For Food Preservation content sourced from NCHFP or USDA, Stage 2 is the only gate since Stage 1 is pre-cleared by source authority. For practitioner-contributed Water Systems content, both stages apply. Stage 1 can be done by the maintainer or a domain reviewer; it does not require a licensed professional for non-medical content.

### Incentive Structure

Attribution is the primary incentive for Type A contributors. Every piece of content carries `author` metadata with the contributor's name (or pseudonym) and a link to their GitHub profile or chosen URL. This is surfaced in the JSON-LD, in the GitHub Pages article view, and in the ZIM file metadata. The contributor can link to their entry on the public site as evidence of their contribution.

For Type B contributors: GitHub contributor graph credit, listed in the repository's `CONTRIBUTORS.md`, and an optional "Verified Domain Expert" badge (manual, granted by maintainer after 3+ accepted contributions in a domain). This badge is surfaced on the contributor's GitHub profile via repository topic tagging.

Community recognition: A monthly "New contributors" note in the repository's release notes and a pinned GitHub Discussions post listing all contributors from the prior month. No leaderboard (gamification creates gaming behavior); recognition is qualitative, not competitive.

---

## Section 3 — Platform Mechanics for GitHub Pages

### Static Site Publishing Workflow

The publishing mechanism is already in place (see `GITHUB_PAGES_SETUP.md`). Content flows as follows:

1. Maintainer accepts a contribution issue and converts it to JSON-LD
2. JSON-LD file is placed in `docs/content/{domain}/{slug}.json`
3. A corresponding Markdown human-readable page is generated and placed in `docs/content/{domain}/{slug}.md`
4. Commit pushed to `main` branch triggers GitHub Pages rebuild (typically 1–3 minutes)
5. New content is live at `https://esca8peArtist.github.io/open-repo/content/{domain}/{slug}`

No CI/CD workflow file is required for Wave 0 — GitHub Pages rebuilds automatically on push to `main`. A GitHub Actions workflow can be added in Week 4 to automate JSON-LD schema validation on every PR (prevents malformed content reaching `main`).

### Content Organization (Folder Structure)

```
docs/
├── index.md                    # Landing page (existing)
├── schemas/                    # Published schemas (existing)
├── content/
│   ├── water/                  # Wave 0 Priority 1
│   │   ├── index.md            # Domain overview + list of articles
│   │   └── {slug}.md           # Individual procedure page
│   ├── food-preservation/      # Wave 0 Priority 2
│   │   ├── index.md
│   │   └── {slug}.md
│   └── seed-preservation/      # Community building target
│       └── index.md
├── contributing/
│   ├── index.md                # Contribution guide
│   └── submit.md               # Links to issue template
└── contributors.md             # Attribution page
```

JSON-LD source files live in a parallel `content/` directory outside `docs/` for machine consumption; the `docs/content/` Markdown files are the human-readable rendered forms.

### A/B Testing Framework

GitHub Pages cannot natively split-test because it serves static HTML with no server-side logic. The pragmatic Wave 0 A/B approach uses GoatCounter (free, no cookies, no GDPR banner, no server required) with manual page variant tracking.

Implementation: Create two versions of the landing page CTA section:
- Variant A: Primary CTA = "Submit a procedure" (action-first)
- Variant B: Primary CTA = "Browse procedures" (browse-first)
- Variant C: Primary CTA = "Join the community" (identity-first)

Mechanics: Deploy Variant A for Weeks 1–3. Switch to Variant B for Weeks 4–6. Track which variant produces more clicks to the Issue template submission form (GoatCounter tracks clicks on the CTA link). Decision: whichever variant produces the higher click-through rate to the submission form is the Wave 1 homepage CTA.

Note: this is sequential, not parallel, A/B testing — "A/A/B in sequence." True parallel A/B testing on a static GitHub Pages site requires JavaScript-based client-side random assignment (Posthog free tier supports this). If click volume is too low in Weeks 1–6 to reach statistical significance (likely), treat the test as directional signal only, not a controlled experiment.

### Analytics Pre-Configuration

Add GoatCounter tracking to `docs/_config.yml` via a Jekyll `_includes/head.html` partial. GoatCounter script is under 3KB, no cookies, and GDPR-exempt.

Track:
- Page views by domain content page (which procedures are most viewed)
- CTA click-through rate (landing page to Issue template)
- Contributor conversion rate (Issue submissions per 1,000 unique visitors)
- Mobile vs. desktop split (GoatCounter provides this automatically by user agent)
- Geographic distribution (country-level, no IP stored)

Set up three saved reports in GoatCounter dashboard:
1. "Content popularity" — sorted by page views, filtered to `/content/` paths
2. "Funnel" — landing page views vs. issue template clicks vs. new issue submissions
3. "Domain comparison" — page views split by `/water/` vs. `/food-preservation/` vs. `/seed-preservation/`

---

## Section 4 — Timeline and Milestones

All dates assume Wave 0 launch in the week of 2026-06-28 (current date). Adjust proportionally if delayed.

### Week 1 (June 28 – July 4): GitHub Pages Hard Launch

- Day 1: Enable GitHub Pages, verify `https://esca8peArtist.github.io/open-repo/` resolves
- Day 1: Add GoatCounter tracking snippet to `_config.yml`
- Day 2: Publish Variant A of landing page (CTA: "Submit a procedure")
- Day 2: Create GitHub Issue template for contributions (see WAVE_0_CONTRIBUTOR_ONBOARDING_TEMPLATE.md)
- Day 3: Publish `docs/contributing/index.md` with 5-minute contribution guide
- Day 4: Publish Water domain index page (`docs/content/water/index.md`)
- Day 5: Publish 3 seed content items (Water Systems) as first example articles
- Day 7: Confirm GitHub Pages is serving all pages, schemas are accessible, GoatCounter is recording

**Go/no-go gate**: Site is live and GoatCounter is recording page views by end of Week 1. If Pages build fails or domain is inaccessible, escalate to Netlify fallback (see Section 5).

### Week 2 (July 5–11): Community Seeding

- Announce on Reddit: /r/preppers, /r/homesteading, /r/Permaculture, /r/CERT (with subreddit-appropriate framing — "offline reference resource," not "my project")
- Post to 2 relevant Discord servers (emergency preparedness, permaculture)
- Submit to Kiwix's third-party library list (process documented at kiwix.org/en/contribute/)
- Invite 3 specific individuals known to the project owner to make first contributions

**Go/no-go gate**: At least 50 unique page views by end of Week 2. Below 50: increase outreach, do not yet invest in more content. Above 50: proceed to Week 3 as planned.

### Week 3 (July 12–18): First Domain Goes Live

- Publish Food Preservation domain index and 3 seed procedures (NCHFP sources, public domain)
- Publish `CONTRIBUTORS.md` (even if the contributor list is only the project owner at this stage)
- Switch landing page to Variant B CTA ("Browse procedures") for A/B tracking
- Respond to any contributor-submitted issues (target: 72-hour response time maintained)

**Milestone**: First external contributor submission received, OR confirmation that issue template has been viewed >10 times without submissions (latter indicates discovery problem, not motivation problem).

### Week 6 (July 19 – August 1): 10-Contributor Gate

**Target**: 10 unique contributor submissions received (issues opened using the template), of which at least 3 have been reviewed and published.

This is the first decision gate:
- If >=10 submissions: continue Wave 0 domains, begin Seed Preservation community seeding
- If 5–9 submissions: investigate funnel (is the issue template being found? are people starting it and abandoning?). Consider switching CTA to Variant C ("Join the community") to shift emphasis from contribution to belonging
- If <5 submissions: activate rollback scenario A (see Section 5). Do not expand to new domains until input funnel is working

### Week 8 (August 9–15): ZIM File Published

- Generate first ZIM export covering Water + Food Preservation content
- Submit ZIM to OPDS catalog (self-hosted endpoint already implemented in Phase 5)
- Update `docs/index.md` with ZIM download link and Kiwix instructions
- Switch landing page to Variant C CTA ("Join the community") to test third variant

### Week 12 (September 6): Wave 0 Decision Point

**Metrics to review**:
- Total unique contributors (target: 10+)
- Total published procedures (target: 20+)
- GoatCounter: page views/month (target: 500+)
- Domain coverage: are Water and Food Preservation both producing regular new content?

**Decision tree**:
- All three targets met: expand to Seed Preservation as Wave 0 Priority 3; begin Phase 6 (federation node) planning
- Two of three targets met: maintain current domains, double outreach for one more month, do not expand domains
- One or zero targets met: activate rollback scenario A or B (see Section 5); reassess Wave 0 mission scope before any expansion

---

## Section 5 — Risk Mitigation

All three scenarios below are **pre-authorized**: no mid-wave analysis is required. If the trigger condition is met, the rollback activates within 48 hours.

### Scenario A — Low Contributor Signup

**Trigger**: <5 external contribution submissions by Week 6 (not counting maintainer-authored content).

**Root cause analysis (automated)**: Check GoatCounter funnel. If landing page views >200 and issue template clicks <20, the CTA is failing. If issue template clicks >20 and submissions <5, the template is too complex. If landing page views <200, the discovery problem precedes the conversion problem.

**Pre-authorized rollback**:
- Remove the contribution-first framing from landing page
- Switch mission framing to "browse offline reference" — position open-repo as a content product, not a contributor network, for Wave 0
- Maintainer authors 20+ additional procedures solo (target: 1 per day for 3 weeks) using NCHFP, WHO WASH, and Practical Action CC-licensed sources
- Contributor onboarding is deprioritized until Week 12; do not abandon it, but do not invest further energy in it during this period
- Measure whether content-led growth (SEO via GitHub Pages indexing, Kiwix catalog discovery) eventually produces inbound contributor interest

**Rollback does not mean failure**: A curated solo library with 50+ high-quality offline procedures is still a valuable Phase 5.2 output. Contributors may arrive later after the content base proves the project's value.

### Scenario B — Content Quality Issues

**Trigger**: Two or more published procedures receive factual error reports (GitHub issues or comments citing incorrect information), OR one procedure receives a safety-related error report.

**Pre-authorized rollback**:
- Immediately unpublish the flagged content (move to `docs/content/_review/` folder, inaccessible from navigation)
- Add a visible review status badge to all contributor-submitted content ("Under review" / "Verified")
- Increase Stage 1 review to require a second reviewer sign-off (two-person rule) before any practitioner-contributed content goes live
- Medical and safety-adjacent content (anything involving chemical dosing, temperature ranges for food safety, or treatment of illness) requires sign-off from the medical reviewers already identified in `medical-reviewer-outreach-draft.md`
- Reduce publication velocity: switch from "publish when schema-valid" to "publish when source-verified + 24-hour hold for final check"

**Recovery criterion**: No further factual error reports for 4 consecutive weeks.

### Scenario C — GitHub Pages Limitations

**Trigger**: Any of the following: (a) GitHub Pages build fails for more than 24 hours with no resolution path, (b) site is flagged or taken down by GitHub for any reason, (c) Jekyll dependency breaks GitHub Pages build on a new Ruby version push.

**Pre-authorized fallback**: Netlify free tier. Netlify supports Jekyll natively, deploys from the same GitHub repository, and provides 100GB/month bandwidth free. Migration steps:
1. Connect `esca8peArtist/open-repo` repo to Netlify
2. Set build command: `jekyll build`, publish directory: `_site`
3. Netlify provides a `*.netlify.app` subdomain within 5 minutes of connection
4. Update `_config.yml` `baseurl` and `url` fields for Netlify domain
5. Point custom domain (if configured) to Netlify DNS

**Time to migrate**: 30 minutes. No content changes required. The fallback is always available — do not wait for GitHub Pages to fail before verifying Netlify deployment works (test it in Week 2 as a shadow deploy, even if GitHub Pages is working).

**Note on Netlify's September 2025 credit-based pricing**: At Wave 0 traffic volumes (<10GB/month), the Netlify free tier is adequate. Monitor monthly bandwidth usage via Netlify dashboard; if it approaches 50GB/month, the project is growing faster than expected and a $19/month Pro plan is the appropriate upgrade, not a hosting change.

---

## Sources

- [GitHub readme: Contributor Onboarding best practices](https://github.com/readme/featured/contributor-onboarding)
- [Let Me In: Guidelines for Successful Onboarding of Newcomers to OSS (ResearchGate)](https://www.researchgate.net/publication/322414294_Let_Me_In_Guidelines_for_the_Successful_Onboarding_of_Newcomers_to_Open_Source_Projects)
- [Good First Issues increase contributor jumps 13% (arXiv)](https://arxiv.org/pdf/2302.05058)
- [GoatCounter: Easy web analytics, no tracking](https://github.com/arp242/goatcounter)
- [Plausible Analytics: Open source privacy-first analytics](https://github.com/plausible/analytics)
- [GoatCounter for GitHub Pages (DEV Community)](https://dev.to/iam_pbk/why-i-chose-goatcounter-for-my-github-pages-site-7k8)
- [Netlify vs GitHub Pages comparison 2025](https://www.freetiers.com/blog/netlify-vs-github-pages-comparison)
- [Kiwix offline knowledge platform](https://albertoroura.com/offline-knowledge-with-kiwix-zim-and-docker-model-runner/)
- [Seed preservation knowledge gaps (Frontiers)](https://www.frontiersin.org/journals/sustainability/articles/10.3389/frsus.2025.1453170/full)
- [Community engagement in open source projects (DEV Community)](https://dev.to/vitalisorenko/community-engagement-strategies-in-open-source-projects-a-comprehensive-guide-2m83)

---

*Prepared 2026-06-28. For review by project owner. Confidence: 84%.*
