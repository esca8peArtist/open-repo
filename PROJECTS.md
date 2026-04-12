# Active Projects

> This is the single source of truth for autonomous orchestration.
> The orchestrator reads this file at the start of every session.
> Update priorities, status, and current focus as work progresses.
>
> **Last updated by**: orchestrator on 2026-04-13 (Session 76)

---

## Priority Order
1. stockbot
2. resistance-research
3. open-source-rideshare
4. seedwarden
5. open-repo
6. off-grid-living
7. containerized-agents
8. workout
9. resume

---

## Projects

### resistance-research
**Goal**: Identify solutions to a failing democracy — if the current government could be replaced and rebuilt from a clean slate, what would it look like? How could it be structured to ensure justice, life, liberty, and the pursuit of happiness for all citizens? How could it be objectively efficient, equitable, and functional? This project addresses the full scope of government: voting systems, taxation, education, infrastructure, healthcare, law enforcement, housing, and everything in between. The government exists to serve its citizens — so how do we actually achieve that? A secondary goal is tracking and understanding the specific crises the United States is currently facing, finding actionable responses, and building a comprehensive integrated proposal for democratic renewal.
**Priority**: High
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/resistance-research/`
**Current focus**: Democratic renewal proposal at 22 domains / 2,544 lines / 13 feedback loops. Cross-domain quality pass COMPLETE. **Publication-ready format COMPLETE and CURRENT** — `published/` directory updated in Session 70 to include Sessions 68-69 content (Domains 10-15 fiscal estimates, subsections 10f/11f/14f; published copy now 2,595 lines). All 22 domains at full evidence depth. Session 76 monitoring pass: White House ballroom (April 17 deadline — National Trust "no national security emergency" filing, SCOTUS application window open); Abrego Garcia (Nashville case dismissal possible — removes admin's strongest argument); MSPB oral argument held April 9 awaiting ruling; CIT April 14 CBP status report due; mail voting EO clarification (EO 14399 vs EO 14248). Next: April 17 ballroom deadline monitoring pass critical.
**Blocked on**: —
**Notes**: Ongoing research and monitoring project. Existing files cover ICE detention, litigation tracking, case studies, civic action. When no specific task is queued, extend existing threads, find new angles, and monitor developments. Democratic renewal proposal is comprehensive at 22 domains; remaining work is quality deepening and publication preparation.

---

### stockbot
**Goal**: Build a full-stack model building and automated trading platform with both a web app and iOS app integration. The platform should allow creation, backtesting, and optimization of trading models across multiple model types (stock, options, rule-based, ensemble, multi-timeframe). The end goal is fully automated live trading — but only after models are rigorously vetted and confidence is established through paper trading. Model training and optimization costs must stay under $20/month. Once a model is sufficiently validated through paper trading performance, it graduates to live trading. Profit maximization is the north star, but capital preservation and risk management are non-negotiable constraints.
**Priority**: High
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/stockbot/`
**Current focus**: Paper trading LIVE as of 2026-04-13. 3 sessions running: momentum (SPY/QQQ/MSFT), rsi_mean_reversion (AAPL/NVDA), sma_crossover (AMZN/SPY). Sessions will fire first trades Monday 9:30 AM ET. Monitor via `http://127.0.0.1:8000` Trading page or curl `/api/paper-trading/cycle-log`. Next session: review Monday cycle logs and check for errors. iOS app deferred until paper trading stable.
**Blocked on**: —
**Notes**: Web app is in good shape. Model creation and most optimisation is operational. Paper trading has just started but has had issues — this is the current priority. iOS app is out of scope until paper trading is solid. All features must work across ALL model types (stock, options, rule-based, ensemble, MTF) — do not implement something for one type only.

---

### open-source-rideshare
**Goal**: Build a free, open-source alternative to Uber and Lyft that stops price-gouging both riders and drivers. The platform should be a web and mobile app that minimises deployment and maintenance costs, ideally using a model where the platform itself is non-profit or cooperative — the margin extracted by Uber/Lyft goes back to drivers and riders instead. Solve the real problems: regulatory compliance in different jurisdictions, driver and rider safety and security, insurance, payment processing, and trust. Also build a plan for bootstrapping the user and driver base — a rideshare app with no users is worthless, so growth strategy is part of the scope.
**Priority**: Medium
**Status**: Active — early stage
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-source-rideshare/`
**Current focus**: Backend comprehensive — 1,809 unit tests passing. Features include: matching engine, WebSocket (heartbeat, health), payments (Stripe, cancellation fees), pricing (demand-aware, time-of-day), geocoding, auth, admin API, Alembic migrations, ride history, profile endpoints, safety service (SOS, trip sharing, emergency contacts), admin SOS monitoring, cancellation policy, notification service (Twilio SMS + SendGrid email + Firebase FCM push), driver rating aggregation, rate limiting, admin SOS WebSocket, scheduled rides, dispatch scheduler + retry logic, admin cancellation stats, driver earnings, promo codes & referral system, ride receipts, service areas/geofencing, admin feedback & disputes, ride & driver metrics dashboard, ride pooling/shared rides, vehicle management & WAV matching, in-app chat, transparent demand pricing, driver ETA estimation, saved locations, admin document verification, recurring rides/commute scheduling, multi-stop rides/waypoints, fare splitting, driver payout & settlement (Stripe Connect), SMS/email notification integration, audit logging & compliance reporting, **background check integration (Checkr API), device token management (FCM)**. Session 70: feature/background-checks-firebase-push committed locally (101 new tests, 1,708 → 1,809). Both Flutter apps have full user flows. Pending: git identity on Pi to commit/push.
**Blocked on**: —
**Notes**: This is the only public project. Higher standards for documentation, test coverage, and code quality since it's community-facing. Regulatory/safety/security solutions and growth strategy are in scope alongside the technical build.

---

### seedwarden
**Goal**: Build a profitable Etsy store and digital brand focused on farming, homesteading, and survival-related digital products, with the ability to expand into physical small products and seed packets. The business needs a full foundation: high-quality digital products that genuinely help people, a consistent social media presence across relevant platforms, and a reputation for real value. The goal is profit and a loyal customer base — not just a store. Grow the business systematically, identify what sells, double down on winners, and build a media presence that drives traffic organically.
**Priority**: Medium
**Status**: Active
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/seedwarden/`
**Current focus**: 19 products total (14 Tier 1, 3 Tier 2, 1 Tier 3, 1 new). Companion Planting Chart complete (382 lines, $5, listing copy done, cross-links referencing actual products). Survival Garden updated to 7 regions (1363 lines, $22, listing copy updated, caloric tables for all regions). Product audit updated with launch sequence (companion planting chart added to Phase 1). **Biggest blocker**: PDF mockup images needed for all listings — #1 conversion factor on Etsy, requires Canva or mockup generator. Also: PDF regeneration needed after content edits. Photo sourcing for Native Plants guide. Download habit photos for wild edibles (Stellaria and Taraxacum have Wikimedia leads ready).
**Blocked on**: —
**Notes**: Etsy store exists with some products started but not yet quality to sell. Social media has plans but nothing executed. Need to fix quality before promoting. Plant images: all 120 native-plants images already downloaded and cached (verified Session 74) — "0/18" note in prior session was stale.

---

### open-repo
**Goal**: An open-source library for all things under the sun — a distributed, free, one-stop shop to find and share information that benefits all of humanity. Link to Wikipedia for general information, schematics, building plans, 3D models, recipes/instructions, services to share, and more. The core principle: no single person or organization controls any of it. Everything is distributed and open source. This is about leveling the playing field — giving all people the best chance to not only survive but thrive.
**Priority**: Medium
**Status**: Active — research phase
**Visibility**: Public — push to feature branches on GitHub freely. Hold on main push for user approval.
**Working dir**: `projects/open-repo/`
**Current focus**: Research phase — survey what already exists (Wikipedia, Internet Archive, OpenStreetMap, LibreTexts, Wikidata, Open Library, Thingiverse, etc.), identify gaps, and define architecture. Key questions: federated vs. centralized, content taxonomy, contribution model, discovery/search, and governance.
**Blocked on**: —
**Notes**: Start with landscape research before any building. The goal is ambitious — don't reinvent what already exists well. Identify the missing layer that ties it all together or fills the gaps nobody else is filling.

---

### off-grid-living
**Goal**: A comprehensive plan for off-grid, sustainable living. Define full plans for construction, implementation, operation, maintenance, and repair. Cover the complete operational architecture: food production, shelter, medicine, electricity generation, food preparation and storage, water, and general survival necessities. Include disaster scenarios up to and including nuclear disaster. Also cover community building, organization, and mutual support.
**Priority**: Medium
**Status**: Active — research phase
**Visibility**: Private — local only, no GitHub push
**Working dir**: `projects/off-grid-living/`
**Current focus**: Master outline complete (`master-outline.md`, 752 lines, 16 domains). `03-water.md` complete (~850 lines, Session 76) — full technical reference: source selection (well/spring/rainwater/surface), water rights law, pumping systems, cistern storage, treatment decision tree, distribution, greywater reuse, emergency protocols, nuclear fallout water, cost tables. Next: `06-energy-power.md` (solar sizing, battery chemistry, micro-hydro).
**Blocked on**: —
**Notes**: This is a planning and research project, not a software build. Practical and actionable plans over theory. Include real costs, sourcing, and skill requirements where possible. Nuclear disaster scenario is in scope — treat it seriously.

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

---

## Completed (Archive)

<!-- Move completed projects here with a completion date -->
