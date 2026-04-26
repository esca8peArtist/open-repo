# Active Projects

> This is the single source of truth for autonomous orchestration.
> The orchestrator reads this file at the start of every session.
> Update priorities, status, and current focus as work progresses.
>
> **Last updated by**: orchestrator on 2026-04-25 (INBOX processing)

---

## Usage Budget

> Tracking is **token-based** (output tokens from `~/.claude/projects/.../  *.jsonl`).
> Plan resets every **Tuesday at 00:00 UTC**.
> To manually check: **claude.ai → Settings → Usage & billing**
> To recalibrate limits: `python3 scripts/usage-check.py --calibrate <sonnet_pct> <all_pct>`

**Calibrated limits** (back-calculated from UI — update after each weekly reset):
- **Sonnet token limit: 5,023,178**  ← calibrated 2026-04-26 (UI showed 42.0%)
- **All models token limit: 13,048,473**  ← calibrated 2026-04-26 (UI showed 34.0%)

**Alert thresholds** (handled by `scripts/usage-monitor.py`, runs every 30 min via cron):
- Every 10% crossed → Discord notification
- 80% → Orchestrator **paused** (`USAGE_PAUSE` file created); Discord alert with override command
- 80% override → `touch /home/awank/dev/SuperClaude_Framework/USAGE_PAUSE_OVERRIDE` (expires at 90% or Tuesday reset)
- 90% → Hard throttle, override revoked; sessions blocked until Tuesday

**Throttle rules (orchestrator must follow at session start):**
1. Run `python3 scripts/usage-check.py --check`
2. Exit 0 → proceed normally
3. Exit 1 (≥90%) → log "Usage throttled — idling." in WORKLOG.md, update CHECKIN.md, stop
4. Exit 2 (80% pause) → log "Usage paused at 80% — waiting for user override or Tuesday reset.", update CHECKIN.md, stop
5. Always update the usage line in CHECKIN.md with `python3 scripts/usage-check.py --checkin` before going idle

---

## Priority Order
1. resistance-research
2. stockbot
3. cybersecurity-hardening
4. mfg-farm
5. seedwarden
6. open-repo
7. off-grid-living
8. workout
9. resume
10. open-source-rideshare (Paused)

---

## Projects

### mfg-farm
**Goal**: Build a fully automated manufacturing business centered on 3D printing, with a path to a full print farm. Sell products on Etsy, Amazon, and similar platforms. Develop a complete business plan: product selection driven by market demand and unique value proposition, pricing strategy, fulfillment workflow, and a scaling roadmap from single printer to multi-printer farm with multiple colors and material capabilities. Explore adjacent manufacturing (laser cutting, CNC, resin printing) and integrate where demand justifies it. The north star is maximizing income — product and machine decisions should be driven by data: what sells, what margins look like, and where automation creates the highest leverage.
**Priority**: High
**Status**: Active — ready to prototype
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/mfg-farm/`
**Current focus**: Session 291: **Business plan COMPLETE** (`business-plan.md`). **CadQuery parametric designs COMPLETE** (`cadquery/modrun_rail.py`, `cadquery/modrun_clip.py`). Market research + competitive analysis were already complete (`market-research.md`). Etsy and Amazon listing copy already complete (`etsy-listing-modrun.md`). **Lead product: ModRun cable management system** — original design, Etsy-compliant, 65–72% net margins. **BLOCKING GATE: test print required.** User needs to: (1) run `pip install cadquery` in mfg-farm env or system Python, (2) run `python modrun_clip.py --output-dir ./stl/` and `python modrun_rail.py --output-dir ./stl/` to generate STL files, (3) test print and tune tolerance parameters, (4) photograph finished set, (5) list on Etsy. All copy, pricing, tags, photo brief are ready in `etsy-listing-modrun.md`.
**Blocked on**: Test print (user action required — see focus above)
**Notes**: Automation is the core constraint — products and workflows must be designed for minimal human touchpoints per unit. Physical products mean real fulfillment costs (packaging, shipping, storage) — factor these in from the start. Etsy and Amazon have different fee structures and audiences; may want both. Scaling from 1→N printers requires thinking about file management, queue management, quality control, and packaging throughput — not just the printers themselves.

---

### resistance-research
**Goal**: Identify solutions to a failing democracy — if the current government could be replaced and rebuilt from a clean slate, what would it look like? How could it be structured to ensure justice, life, liberty, and the pursuit of happiness for all citizens? How could it be objectively efficient, equitable, and functional? This project addresses the full scope of government: voting systems, taxation, education, infrastructure, healthcare, law enforcement, housing, and everything in between. The government exists to serve its citizens — so how do we actually achieve that? A secondary goal is tracking and understanding the specific crises the United States is currently facing, finding actionable responses, and building a comprehensive integrated proposal for democratic renewal.
**Priority**: High
**Status**: Active — Phase 1 launched, Phase 2 live, **Phase 3 underway**
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: Phase 1 (monitoring) and Phase 2 (litigation tracking) LIVE and production-ready. **Phase 3 in progress (Session 485 — major completion):**

**✅ COMPLETED (Session 485)**:

1. **✅ Priority documents — all delivered and committed**:
   - ✅ `first-amendment-suppression.md` (3,400 words, 6 sections) — press crackdowns, protest restrictions, deplatforming, SLAPP litigation, legal landscape, current cases (2025-2026)
   - ✅ `environmental-rollbacks-tracker.md` (3,800 words, 5 agencies + cross-agency) — EPA/Interior/NOAA/DOE/DOT with Federal Register citations, litigation status, impact analysis (24 entries)
   - ✅ `police-brutality-consent-decree-tracker.md` (4,200 words, 8 major cities) — Chicago/Oakland/Minneapolis/Baltimore/Louisville/Cleveland/Ferguson/Newark with systemic defiance patterns

2. **✅ Format democratic renewal proposal — all infrastructure created**:
   - ✅ `democratic-renewal-executive-summary.md` (1,200-1,500 words, print-ready) — 2-page summary, 22-domain table, fiscal scope, call to action
   - ✅ `DISTRIBUTION_GUIDE.md` (1,000-1,200 words) — Platform strategy (Substack, Reddit, email, Twitter/X, institutional), audience segmentation, metrics
   - ✅ `published/README.md` (comprehensive hub) — Links to all documents, 5 use-case pathways, 22-domain quick-reference

3. **✅ Distribution setup — all templates drafted and ready**:
   - ✅ `distribution-substack-drafts.md` (4 posts: Launch, Electoral Reform, Accountability/Oversight, Trackers) — 800-1,000 words each
   - ✅ `distribution-reddit-templates.md` (5 posts: r/law, r/politics, r/Keep_Track, r/Ask_Politics, r/democracy) — native framing, 300-500+ words each
   - ✅ `distribution-institutional-outreach-templates.md` (8 templates: legal aid 2, digital rights 2, movement orgs 3) — personalization checklists, sequencing

**NEXT Phase 3 Work**:
4. Phase 3 research roadmap (international democratic renewal models, implementation timelines, constitutional design, adoption pathways)
5. (Exploration Queue) Seedwarden Phase 2-4 expansion + social media strategy

**Blocked on**: —
**Notes**: Phase 3 distribution infrastructure COMPLETE and READY for user execution. All trackers field-ready for ongoing updates. Gist remains live distribution channel. Next work is strategic deepening (Phase 3 research roadmap) and adjacent business/brand work (Seedwarden expansion).

---

### cybersecurity-hardening
**Goal**: Build a comprehensive, actionable guide to protecting communications and identity against government-level mass surveillance. Understand what Palantir and similar data brokers/intelligence platforms actually have access to — what data they ingest, how they link identities, and what their current government contracts cover. From that threat model, identify the best practical techniques for private and anonymous communication: encrypted messaging, metadata minimization, network anonymization (Tor/VPN tradeoffs), device hardening, operational security (OpSec), and identity compartmentalization. The output should be a personal OpSec playbook grounded in real threat modeling — not theoretical, but calibrated to the actual capabilities of the adversary.
**Priority**: High
**Status**: Active — **TIER 1 DISTRIBUTION PREP COMPLETE** (Session 465), ready for user execution
**Visibility**: Public — GitHub Gist (public) + private distribution to immigration legal aid organizations
**Working dir**: `projects/cybersecurity-hardening/`
**Current focus**: Session 465 (2026-04-26): **TIER 1 DISTRIBUTION PREP COMPLETE**. Agent-created TIER1_DISTRIBUTION_PREP.md (358 lines) consolidates all distribution materials: 8 Tier 1 organizations (5 legal aid + 3 community org networks), 3 email templates (legal aid, community orgs, mutual aid networks), 5-step execution process, pre-send checklist, FAQ, success metrics, and quarterly review schedule. All templates include Gist URL and are ready for personalization. TIER1_DISTRIBUTION_PREP.md committed to master. **Next**: User reviews and approves templates → execute Tier 1 outreach → track responses → Tier 2 (digital rights, security researchers, journalists) → Tier 3 (policy, academic, labor).
**Blocked on**: —
**Notes**: All distribution materials production-ready. Trilogy (Gist) published and accessible. TIER1_DISTRIBUTION_PREP.md provides step-by-step execution guide with email templates, contact list, tracking templates, and quarterly review schedule. User can begin Tier 1 outreach immediately after approval.

---

### stockbot
**Goal**: Build a full-stack model building and automated trading platform with both a web app and iOS app integration. The platform should allow creation, backtesting, and optimization of trading models across multiple model types (stock, options, rule-based, ensemble, multi-timeframe). The end goal is fully automated live trading — but only after models are rigorously vetted and confidence is established through paper trading. Model training and optimization costs must stay under $20/month. Once a model is sufficiently validated through paper trading performance, it graduates to live trading. Profit maximization is the north star, but capital preservation and risk management are non-negotiable constraints.
**Priority**: High
**Status**: Active — paper trading live, **pre-live-trading hardening underway**
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**Current focus**: Paper trading running (AAPL_h10_lgbm_ho stacker, session `33a4afe676cae12a`). Model graduation criteria framework complete (`model-graduation-criteria.md`). **Next tasks — work these in order:**

1. **Live trading guardrails** — implement before live trading is even considered. Write as `live-trading-guardrails.md` spec + implement in code:
   - Hard margin ban: cash-only account mode, never allow orders exceeding cash buying power
   - Max position size: no single position >15% of account balance
   - Max concurrent open positions: cap at N (determine appropriate number)
   - Daily loss kill switch: halt all new orders if account drops >X% intraday (user to approve threshold)
   - No short selling, no leveraged ETFs (2×/3× instruments banned)
   - Emergency halt command that closes all positions immediately

2. **Multi-strategy conflict resolution** — investigate and fix the issue where concurrent strategies cause Alpaca order conflicts (likely competing orders on same ticker, position double-counting, or rate limit collisions). Implement a shared position manager or strategy isolation layer.

3. **Strategy optimization** — once conflicts resolved, run backtests to evaluate which strategies perform best; eliminate underperformers; document findings in `strategy-evaluation.md`

4. **Live trading readiness checklist** — when paper trading shows consistent positive performance (per graduation criteria), produce a checklist of what the user needs to do: switch Alpaca API keys to funded live account, verify cash account type set (no margin), confirm guardrails active, set initial funding amount

**Blocked on**: —
**Notes**: User live trading criteria: strategies must open AND close positions autonomously with UI matching Alpaca exactly. Paper-to-live switch is just credential swap + URL change — but guardrails must be in place first. Initial live account will be funded with a very small amount to verify everything works. Margin is explicitly banned. Leveraged ETFs and short selling are explicitly banned.

---

### open-source-rideshare
**Goal**: Build a free, open-source alternative to Uber and Lyft that stops price-gouging both riders and drivers. The platform should be a web and mobile app that minimises deployment and maintenance costs, ideally using a model where the platform itself is non-profit or cooperative — the margin extracted by Uber/Lyft goes back to drivers and riders instead. Solve the real problems: regulatory compliance in different jurisdictions, driver and rider safety and security, insurance, payment processing, and trust. Also build a plan for bootstrapping the user and driver base — a rideshare app with no users is worthless, so growth strategy is part of the scope.
**Priority**: Low
**Status**: Paused — resume when user unpauses
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-source-rideshare/`
**Current focus**: Session 407: **Driver Document Expiry Status Endpoints COMPLETE** (commit `c8cd00f`, 20 new tests, branch `feature/driver-navigation`). `GET /drivers/me/document-expiry` (driver self-check with urgency labels) and `GET /admin/document-expiry` (fleet overview with expired_only filter). `get_expiring_documents_for_driver()` added to service layer. 6,154 tests passing. **Next**: open-repo data acquisition task (acquire OpenFarm data via Internet Archive and run import_openFarm.py), or further rideshare safety/compliance features.
**Blocked on**: —
**Notes**: This is the only public project. Higher standards for documentation, test coverage, and code quality since it's community-facing. Regulatory/safety/security solutions and growth strategy are in scope alongside the technical build.

---

### seedwarden
**Goal**: Build a profitable Etsy store and digital brand focused on farming, homesteading, and survival-related digital products, with the ability to expand into physical small products and seed packets. The business needs a full foundation: high-quality digital products that genuinely help people, a consistent social media presence across relevant platforms, and a reputation for real value. The goal is profit and a loyal customer base — not just a store. Grow the business systematically, identify what sells, double down on winners, and build a media presence that drives traffic organically.
**Priority**: Medium
**Status**: Active — Phase 1 upload pending user tag corrections; native plants guide on hold for image rebuild
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/seedwarden/`
**Current focus**: **Two parallel tracks:**

**Track A — Phase 1 launch (blocked on user)**: 3 tag corrections and Etsy account verification required before upload (documented in `UPLOAD_READY_CHECKLIST.md`). Once user completes those, the 8 text-heavy products below are ready to list immediately. Do NOT hold up these products waiting on the native plants guide.

**Phase 1 products ready to launch** (text-heavy, no photo dependency):
- Companion Planting Chart, Zone-by-Zone Seed Starting Calendar, Seed Saving Field Manual, Survival Garden Regional Plans, Apartment Seed Starting Kit, Container Growing Blueprint Pack, Food Sovereignty Starter Guide, 12-Month Urban Growing Planner

**Track B — Native plants guide image rebuild** (orchestrator can work this now): The current native-plants-regional-guide.pdf uses web-scraped photos that are unreliable for plant identification — wrong subjects, partial views, non-plant content in frame. **Rebuild the image pipeline:**
1. Source replacement images from USDA PLANTS Database (plants.usda.gov) and Wikimedia Commons botanical illustrations — both public domain, specifically designed for plant ID, show full plant with clear identification features
2. For each species in the guide, find a USDA or Wikimedia image showing: (a) whole plant habit, (b) key identifying features (leaf shape, flower, fruit/seed if applicable)
3. Update `scripts/main.py` image sourcing logic to pull from curated URLs rather than generic web search
4. Regenerate the PDF and verify quality before adding to Phase 1 upload queue

**Blocked on**: Tag corrections + Etsy account verification (user action, Track A only). Track B has no blockers.
**Notes**: User reviewed deliverables and found formatting issues in some PDFs and unreliable photos in native plants guide. Text-heavy products are solid and can launch. Native plants guide needs image rebuild — use authoritative botanical sources (USDA, Wikimedia) not web scraping. Phases 2–4 (phone mockups, lifestyle photography, printed page mockups) to be evaluated after Phase 1 conversion data is in.

---

### open-repo
**Goal**: An open-source library for all things under the sun — a distributed, free, one-stop shop to find and share information that benefits all of humanity. Link to Wikipedia for general information, schematics, building plans, 3D models, recipes/instructions, services to share, and more. The core principle: no single person or organization controls any of it. Everything is distributed and open source. This is about leveling the playing field — giving all people the best chance to not only survive but thrive.
**Priority**: Medium
**Status**: Active — Phase 4 COMPLETE, **PR #1 open, awaiting review/merge** (Session 486: 2026-04-26)
**Visibility**: Public — GitHub repo: `esca8peArtist/open-repo`. Use remote `open-repo` for all pushes. Use `git subtree push --prefix=projects/open-repo open-repo <branch>` — never push to `origin`.
**Working dir**: `projects/open-repo/`
**Current focus**: **PR #1 OPEN** (2026-04-26): https://github.com/esca8peArtist/open-repo/pull/1
- Title: "feat: Wave 4 Phase 2 — Federation Service Infrastructure"
- 194/198 tests passing (4 skipped), 0 failures
- Wave 4 federation complete: partner registration, service layer, admin routes, HTTP signature verification, request signing, conflict detection
- **Next**: Await PR merge review. After merge, begin Phase 5 (offline export/Kiwix integration).
**Blocked on**: —
**Notes**: All pushes to GitHub use `git subtree push --prefix=projects/open-repo open-repo <branch>` or `git subtree split` to keep the public repo clean. Never use `git push origin`. PR merge is awaiting maintainer review; no further blocking issues.

---

### off-grid-living
**Goal**: A comprehensive plan for off-grid, sustainable living. Define full plans for construction, implementation, operation, maintenance, and repair. Cover the complete operational architecture: food production, shelter, medicine, electricity generation, food preparation and storage, water, and general survival necessities. Include disaster scenarios up to and including nuclear disaster. Also cover community building, organization, and mutual support.
**Priority**: Medium
**Status**: Complete — **publication complete** (GitHub live, awaiting user execution of social media distribution)
**Visibility**: Public — GitHub repo: `https://github.com/esca8peArtist/off-grid-living-guide` (live as of 2026-04-26)
**Working dir**: `projects/off-grid-living/`
**Current focus**: **GitHub Publication COMPLETE (Session 486)**. All tasks executed:
  - ✅ Fixed file numbering: 01→03→... → 01-17 sequential with no gaps (shelter moved 11→02)
  - ✅ Updated all internal cross-references (17 files)
  - ✅ Wrote comprehensive README.md with structure, usage guide, CC BY-SA 4.0 license
  - ✅ Verified nuclear/radiological preparedness content (725 lines, complete)
  - ✅ Published to GitHub via git subtree push
  - ✅ Drafted social media posts (Reddit × 3, X/Twitter thread, email draft)

**Next Phase**: User execution of social media distribution per `social-media-launch-posts.md`:
  - Post to r/offgrid, r/preppers, r/homesteading (slightly different angle for each)
  - Post X/Twitter thread (7 tweets)
  - Optional: email announcement to mailing list
  - Timing: stagger Reddit posts Tue–Fri, X thread over 2–3 days

**Blocked on**: —
**Notes**: Instagram and TikTok require separate visual/video production — defer until GitHub traction established and user decides to invest in visual content. All 17 domains production-ready. Repo live and accessible.

---

### containerized-agents
**Goal**: Archived — goal TBD if reactivated.
**Priority**: Low
**Status**: Archived
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/containerized-agents/`
**Current focus**: —
**Blocked on**: —
**Notes**: Archived per user direction on 2026-04-12.

---

### workout
**Goal**: Create comprehensive workout plans that blend athleticism, strength training, mobility, and calisthenics into unified programs. Produce plans for three equipment tiers: no equipment, resistance bands only, and full gym. Provide proposals for different training frequencies (days/week), exercise variety, and formats to build the best all-in-one plan maximizing strength growth while addressing athleticism, mobility, and bodyweight mastery.
**Priority**: Low
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/workout/`
**Current focus**: `comprehensive-plan.md` (1,053 lines) complete — covers all 3 equipment tiers (no equipment, bands, full gym) × multiple frequencies (3/4/5/6 days), with full exercise libraries, progression systems, calisthenics skill ladders, and mobility protocols. Awaiting user review and selection.
**Blocked on**: —
**Notes**: Content/planning project, not a software build. Goal defined by user on 2026-04-12. Existing `proposals_v2.md` covers the 6-day gym PPL in detail (referenced from comprehensive plan). `requirements.md` has baseline info and calisthenics skill levels.

---

### resume
**Goal**: Maintain and improve Anya's professional resume and any associated portfolio materials.
**Priority**: Low
**Status**: Paused
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resume/`
**Current focus**: —
**Blocked on**: —
**Notes**: Only gets attention when explicitly requested.

---

## Exploration Queue

Topics fair game when no higher-priority task is active. Log findings to the relevant project or resistance-research.

- ~~Cryptographic voting systems and democratic resistance — extend the remote-voting research into the democratic renewal proposal~~ — **Done** (Session 24: Section 4 expanded to 8 subsections covering E2E-V protocols, deployed systems, coercion resistance, RLAs, post-quantum crypto, formal verification, maturity spectrum; Domain 1e updated with three-layer verification model)
- ~~Legal landscape of algorithmic decision-making in ICE detention — recent case law, civil rights angles~~ — **Done** (Session 24: `algorithmic-decision-making-immigration.md`, 270 lines — ICM/FALCON/ImmigrationOS systems, NIST bias data, Gonzalez v. ICE, EU AI Act/Canada AIA models, 6 reform recommendations; Domain 16d expanded)
- ~~Cooperative/platform cooperative business models — relevant to rideshare's ownership structure~~ — **Done** (Session 22: `cooperative-models-research.md`, 744 lines in open-source-rideshare/)
- ~~Regulatory landscape for rideshare in major US cities~~ — **Done** (Session 23: `regulatory-compliance-research.md`, 1,002 lines)
- ~~Etsy SEO and digital product market research — what sells in the homesteading/survival niche?~~ — **Done** (Session 24: `etsy-seo-market-research.md` in seedwarden/, 402 lines — Etsy algorithm mechanics, keyword strategy, competitive landscape, price positioning, title optimization, growth strategy, seasonal planning, bundle strategy, social media, metrics)

- ~~**Palantir and government surveillance infrastructure**~~ — **Done** (Session 484: `palantir-threat-model.md` complete — Gotham/Foundry/AIP architecture, confirmed federal contracts (ICE/ELITE/ImmigrationOS, CBP/AFI, FBI, NSA, DHS), data sources, entity resolution methodology, real-world implications, capability gaps)

- ~~**off-grid-living: nuclear and radiological preparedness**~~ — moved to project Current focus (Step 3 of publication prep)

- ~~**Stockbot: model evaluation framework**~~ — **Done** (Session 484: `model-graduation-criteria.md` complete — four-gate framework for paper-to-live graduation: statistical sufficiency, performance quality, robustness validation, operational readiness)

- ~~**resistance-research: post-launch Phase 2 prep**~~ — **Done** (Phase 2 litigation tracking COMPLETE and production-ready per Session 462)

- ~~**Resistance-research: Phase 3 research roadmap**~~ — moved to project Current focus (Phase 3 priority documents + proposal formatting + distribution setup)

- ~~**Seedwarden: Phase 2-4 expansion & social media strategy**~~ — moved to project Current focus (native plants image rebuild is the priority; Phase 2-4 deferred until Phase 1 conversion data in)

- **workout: nutrition and tracking companion** — comprehensive-plan.md is complete but lacks nutrition guidance and progress tracking. Add: a nutrition framework (macros by goal + equipment tier), a weekly tracking template (lifts, bodyweight, energy), and a progress milestone chart. Write to `projects/workout/nutrition-and-tracking.md`. This extends the plan without requiring user review of the existing document.

- **cybersecurity-hardening: device hardening deep-dive** — the Palantir threat model is complete. Next gap: practical device hardening for iPhone and Android against government-level surveillance. Research: aeroplane mode vs. full-power-off for RF silence, locked bootloader implications, GrapheneOS vs. CalyxOS tradeoffs, iCloud vs. local backup security, location data brokers and how to opt out, and SIM swapping as an attack vector. Write to `projects/cybersecurity-hardening/device-hardening-guide.md`.

---

## Completed (Archive)

<!-- Move completed projects here with a completion date -->
