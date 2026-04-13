# Check-in Briefing

> This file is updated by the orchestrator before going idle.
> When you drop in, read this first. It's designed to get you up to speed in under 5 minutes.
> After reviewing, clear the "Since Last Check-in" section and leave notes in "Your Notes" for the orchestrator to pick up.

---

## Since Last Check-in

**Period**: April 13, 2026
**Sessions run**: 75–81

### Accomplished (Session 81)

#### resistance-research — April 13 Monday monitoring
New file: `monitoring/2026-04-13-monday.md`. All five threads confirmed:
- **White House ballroom**: Leon has not acted on D.C. Circuit remand. No SCOTUS application on docket. National Trust filed separability argument (above-ground ballroom vs. underground security work). April 17 stay expiry is the hard deadline — cranes running April 18 = contempt.
- **SCOTUS application**: Not filed. Administration strategically constrained — filing before Leon acts loses the factual record; filing after Leon narrows loses national security framing.
- **Section 122 tariff (CIT)**: Panel sharply skeptical at April 10 oral argument. No ruling yet. April 14 noon EDT: CBP Phase 1 status declaration (IEEPA refund implementation).
- **Abrego Garcia**: April 17 pressure defused by Xinis ruling; April 28 hearing is the next line. Liberia deportation template still active if admin wins.
- **Nashville (Crenshaw/Blanche)**: CNN April 11 report confirms Crenshaw found Blanche's comments linked Maryland case to investigation — meets vindictive prosecution threshold. Subpoena path being weighed. Extended silence suggests Crenshaw going beyond simple dismissal.

#### open-source-rideshare — Push notification preferences
Per-user opt-in/out by notification type and channel. 51 new tests. Full suite: 1,918 passing (no regressions).
- `models/notification_preference.py` — `NotificationPreference` (table `notification_preferences_v2`), unique constraint on `(user_id, notification_type, channel)`, enabled=True default (opt-out model)
- `schemas/notification_preference.py` — validates type+channel against known enums; `SetPreferenceRequest`, `BulkSetPreferenceRequest`, `UserPreferencesResponse`
- `services/notification_preferences.py` — `get_user_preferences` (full 15×3 map), `set_preference`, `bulk_set_preferences`, `is_channel_enabled`, `reset_preference`
- `api/v1/notification_preferences.py` — GET full map, PUT /bulk, PUT /{type}/{channel}, DELETE /{type}/{channel} (204)
- Migration: `a8e1f5b03c92_add_notification_preferences.py`
- `services/notifications.py` updated: checks preference before each channel dispatch; SOS_ALERT always bypasses; DB failures are non-fatal

#### off-grid-living — `08-medical-health.md` (1,139 lines)
Domain 8 complete. 14 sections covering: treat-vs-evacuate decision framework, MARCH first aid protocol (wound irrigation physics: 18g needle = 8 PSI, closure hierarchy, Ottawa ankle rules), 3-tier supply tables ($350–550 basic, $900–1,400 advanced) with specific sources, 18 medicinal plants with evidence levels (St. John's Wort CYP3A4 interactions and comfrey hepatotoxicity flagged explicitly), empiric antibiotics + fish antibiotic legality confirmed (2018 CID study), full dental section (Cavit, abscess I&D, Ludwig's angina warning, extraction), prescription management (SLEP data, ReliOn insulin OTC $25/vial, ivermectin horse paste dosing math), childbirth (all 5 P's, McRoberts for shoulder dystocia, improvised Bakri balloon), mental health (Antarctic winterover research cited, exercise=SSRI equivalent evidence), trauma (tourniquet timing physiology, conservative appendicitis antibiotics 70% RCT success), CBRN (ARS dose table by Gy, 7/10 rule, KI dosing by age group, nerve agent SLUDGE signs with atropine dosing), training stack (WFR $700–900 recommended), 25-row cost table (~$4,000–5,000 total investment). Next: `09-waste-sanitation.md`.

---

### Stockbot Note
STOCKBOT_API_KEY not available in this orchestrator session — unable to check Monday trading cycle logs. Check manually:
```
curl -H "Authorization: Bearer $STOCKBOT_API_KEY" http://127.0.0.1:8000/api/paper-trading/cycle-log?limit=20
```
Or visit `http://127.0.0.1:8000` → Trading page. First trades should have fired Monday 9:30 AM ET.

---

### Accomplished (Session 80)

#### resistance-research — Pre-April-17 scenario analysis

New file: `monitoring/2026-04-17-preview.md` (359 lines). Decision-tree analysis of all four April 17 ballroom scenarios:

- **Scenario A (40%)**: Leon narrows order before April 17 — SCOTUS application loses national security framing; above-ground work halts; Appropriations Clause preserved
- **Scenario B (20%)**: No action, stay expires — injunction fully reinstated; contempt territory if admin continued building
- **Scenario C (50% base)**: SCOTUS application filed — blended ~30% SCOTUS grants if Leon narrowed, ~70% if security framing intact
- **Scenario D (15%)**: Leon expands injunction (includes underground/bomb-shelter work) — near-certain solo Roberts administrative stay
- **Roberts posture synthesis**: 50–55% probability SCOTUS grants if application filed; key variable is Leon remand outcome
- **April 14 events**: CIT conference on IEEPA refund; Section 122 ruling probability 25% this week (panel posture against admin)
- **Civic action**: How each scenario affects May Day calculus and AFL-CIO endorsement threshold; full tool inventory if courts fold
- Branching decision tree + hour-by-hour watch items through April 17

#### open-source-rideshare — Rider rating system (mutual accountability)

New feature: 6 files, 2 updated, 36 tests (18 passing service-layer, 18 skipped integration).

- `models/rider_rating.py` — `RiderRating` with `UniqueConstraint("ride_id", "driver_id")` and `CheckConstraint("rating >= 1 AND rating <= 5")`
- `services/rider_ratings.py` — submit, summary (avg/count/distribution), per-ride lookup, low-rated list (30-day avg < 3.0 with > 5 ratings)
- `api/v1/rider_ratings.py` — 4 endpoints: driver submits, public summary, per-ride lookup, admin low-rated list
- Migration `f1a3c7e92d05_add_rider_ratings.py`; `models/__init__.py` + `main.py` updated

#### off-grid-living — `05-food-preservation.md` complete (1,522 lines)

Domain 5 complete. Master outline updated. 13 sections: root cellaring, canning (water bath + pressure), lacto-fermentation, dehydration (solar dehydrator design + 17-crop table), freezing (solar sizing math), smoking/curing (nitrite chemistry, UDS smoker build), vinegar pickling, oil preservation (botulism warnings), grain/dry storage (17-commodity duration table), preservation calendar (Zone 5 month-by-month), disaster scenarios (nuclear Cs-137 note), cost/ROI (18-item equipment table, 5-household cooperative math).

---

### Accomplished (Session 79)

#### resistance-research — April 13 evening monitoring + CRITICAL CORRECTION

New file: `monitoring/2026-04-13-evening.md`. Litigation tracker corrected.

1. **White House ballroom**: No SCOTUS application filed as of evening. No Judge Leon response to D.C. Circuit remand. The remand asked Leon to clarify whether his injunction covers the underground infrastructure (bomb shelters, missile-resistant steel, "Top Secret Military installations") — if Leon narrows his order to exclude underground work, the administration's SCOTUS narrative collapses before any application is filed. These two events (Leon response + SCOTUS filing) could break simultaneously before April 17.

2. **Maryland/Abrego Garcia — CORRECTION**: The April 17 DOJ deadline in Maryland is MOOT. Judge Xinis disposed of it on April 12: rejected the government's self-imposed schedule, new briefings April 20, hearing April 28. The "double April 17 deadline" scenario no longer exists. Watch: April 28 hearing — if govt wins, Liberia-deportation model becomes usable template for routing around withholding-of-removal orders.

3. **Nashville**: No Crenshaw ruling. Continued silence may indicate he's weighing subpoenaing Blanche rather than simply dismissing.

4. **CRITICAL CORRECTION — IEEPA tariffs**: Prior tracking was wrong. **SCOTUS struck down IEEPA tariffs 6-3 on February 20, 2026** (*Learning Resources v. Trump*, No. 24-1287, Roberts opinion: "IEEPA contains no reference to tariffs or duties"). The April 14 CIT conference is about REFUND IMPLEMENTATION (CBP Phase 1 system, April 20 launch). The live tariff legality fight is the **Section 122 challenge** (10% global tariff, separate legal theory), argued April 10 before CIT three-judge panel — ruling pending. Tracker has been corrected.

5. **May Day**: No AFL-CIO national endorsement. Coalition unchanged from afternoon pass.

#### off-grid-living — `04-food-production.md` complete (1,301 lines)

Domain 4 complete. Master outline updated to mark it done. Comprehensive coverage:
- **Caloric math**: 1,800–4,000 cal/day by activity; calories/acre by crop (sweet potato 4.875M/acre leads); annual targets for 4-person household (3.5M cal/year with specific pound targets per crop); sq-ft caloric density ranking table
- **Annual vegetables**: Zone 3–10 planting calendar; 15-crop spec table (days-to-maturity, yield/sq ft, storage life); succession planting with specific sq footage; allocation tables for 1/4-acre / 1/2-acre / 1-acre
- **Perennial systems**: 12 fruit tree species table (zones, years to first fruit, mature yields); nut tree calorie density (pecan 3,100 cal/lb, 465,000 cal/tree mature); 7-layer food forest design; berry yield by row foot
- **Livestock**: Chicken egg math (8 hens = 1,920 eggs/year, winter production); rabbit (3:1–4:1 FCR, 160 lb dressed/year from trio); goat milk math (400–600 gal/year/doe); pig; duck vs. chicken table; IBC tote aquaponics (tilapia/bluegill/catfish)
- **Seed saving**: Isolation distances by family (corn requires 1,000 ft+, tomato 10–35 ft); viability table for 18 crops; wet/dry processing; seed bank quantity targets
- **Soil systems**: Hot pile compost (3×3×3 min, 131–160°F target); C:N ratios; cover crop calendar; no-till vs. till comparison; hugelkultur decision guide; biochar retort method
- **Food preservation**: Root cellar parameters; 9-method comparison; storage duration matrix by crop × method
- **Water for food**: 1/2-acre needs ~163,000 gal/season (reduced to ~80k with mulch + drip); rainwater sizing math (~1,375 sq ft roof per 1/4-acre garden); drip vs. overhead table
- **Cost tables**: Startup $1,200–$10,500; annual $190–$2,100; livestock startup/annual by species; payback 0.5–2.5 years
- **Disaster scenarios**: Crop failure math; drought protocol; IPM + 4-bed rotation; post-nuclear food safety (zeolite 50 lb/100 sq ft, deep till, potassium for Cs-137 displacement), pre-positioning checklist

#### open-source-rideshare — Driver incentive/bonus program system

New feature: 6 files, 2 updated, 36 tests (0 failures).

- `models/incentive.py` — `IncentiveProgram` (quest / peak_hours / streak / earnings_guarantee types) + `DriverIncentiveProgress` (active / completed / paid / expired)
- `services/incentives.py` — `record_trip_completion` evaluates all active programs per trip; time-window + day-of-week guards; streak expiry on any cancellation; peak_hours accumulates per-trip; earnings_guarantee floor logic
- `api/v1/incentives.py` — 3 driver endpoints (view programs + progress + pending earnings), 5 admin endpoints (CRUD + leaderboard)
- `schemas/incentive.py`, migration `e2f5a9c81d47`, `models/__init__.py` + `main.py` updated
- Admin soft-deletes preserve historical progress for audit

---

### Accomplished (Sessions 75–78 Archive)

#### stockbot — Critical bug fixes + paper trading LIVE

Session persistence bug fixed. All 3 sessions running: momentum (SPY/QQQ/MSFT), rsi_mean_reversion (AAPL/NVDA), sma_crossover (AMZN/SPY). First trades fire Monday 9:30 AM ET. Commit: `025f06a`.

#### resistance-research — April 13 morning monitoring pass

Roberts solo SCOTUS stay of MSPB/NLRB reinstatement (critical signal for Trump v. Slaughter June 2026). Ballroom April 17 deadline: National Trust "no national security emergency" brief. Nashville dismissal imminent. Birthright citizenship oral argument: Roberts called admin argument "quirky." May Day general strike build.

#### off-grid-living — `06-energy-power.md` (997 lines) + `03-water.md` (850 lines)

Both complete. Full technical references covering all major systems.

#### open-source-rideshare — Driver tipping system

37 new tests, full tipping system: TipRecord model, Stripe, 48-hour window, $0.50–$50 range, notifications. Branch: `feature/background-checks-firebase-push` (local, push still blocked by missing SSH key).

#### open-repo — NEW project bootstrapped

`landscape-research.md` (16-platform survey) + `architecture-notes.md`. Federated instances + IPFS + ActivityPub architecture.

#### seedwarden — Image audit, content review

120 images confirmed cached. Region 5 (Southwest/Desert) content gap flagged: only 14 species vs 27–46 in other regions.

---

### Accomplished (Session 76)

#### resistance-research — April 13 morning monitoring pass

5 threads updated in `litigation-tracker-2026.md`:

1. **White House ballroom (CRITICAL — April 17 deadline)**: National Trust filed April 13 response arguing "no national security emergency" — directly contests the D.C. Circuit majority's factual predicate. No SCOTUS emergency application yet as of Sunday AM; window open (would go to Roberts or Kavanaugh).

2. **Abrego Garcia**: Nashville criminal case — Judge Crenshaw "poised to decide at any time" on dismissing human smuggling charges due to Blanche's public vindictive-prosecution statements. If dismissed, removes admin's strongest argument for dissolving the Maryland injunction. DHS still maintaining Liberia theory despite Costa Rica confirming willingness.

3. **MSPB / Federal Circuit**: Oral argument in Oguntade v. MSPB held April 9 — awaiting ruling. Now a decided-argument-awaiting-ruling case.

4. **CIT tariff / IEEPA**: April 14 CBP status report due. April 20 Phase 1 IEEPA refund rollout on track. Section 122 ruling still pending.

5. **Mail voting EO clarification**: Current litigation targets EO 14399 (March 31, 2026) — the October 2025 "show your papers" injunction was against EO 14248 (a different order).

#### off-grid-living — `03-water.md` complete (~850 lines)

First domain deep-dive document, full technical reference:
- **Source selection**: Well depth/cost tables by region ($25–85/ft, $8–40k complete system), spring box construction sequence, rainwater formula (0.623 gal/sq ft/inch) with 4-climate examples, water rights law (prior appropriation vs riparian, rainwater legality by state incl. Colorado's 110-gal limit)
- **Pumping**: Simple Pump (to 325 ft) vs Bison Pump comparison, Grundfos SQFlex solar sizing (100W per 100 ft head per GPM), pump sizing worksheet with livestock demand table
- **Storage**: Cistern sizing (30-day reserve math), materials table (poly, IBC, ferro-cement, concrete, fiberglass) with per-gallon costs
- **Treatment decision tree** by source type: sequential sediment filtration, carbon, UV (note: 30 mJ/cm² not reliable against Cryptosporidium), RO, distillation
- **Distribution**: Pressure tank sizing, PEX vs CPVC vs copper freeze-resistance table, frost depths by region
- **Greywater**: L2L/branched drain/constructed wetland, legal status by state
- **Emergency**: FEMA 1-gal/day myth corrected, bleach ratios, SODIS protocol, nuclear fallout water (I-131 half-life, sealed cistern safety, RO for dissolved radionuclides)
- **Cost tables**: 5 system configurations from minimal cabin to full redundant homestead

#### stockbot — Health check

Backend confirmed running, all 3 sessions cycling every 3 seconds, `market_open: false` (expected Sunday). Ready for Monday 9:30 AM ET.

---

### Accomplished (Session 75)

#### stockbot — Paper trading sessions LIVE

All 3 paper trading sessions are now running and will begin active trading at Monday's market open (9:30 AM ET, April 14):

| Strategy | Tickers | Session ID |
|---|---|---|
| `momentum` | SPY, QQQ, MSFT | 8fd082bf9782737b |
| `rsi_mean_reversion` | AAPL, NVDA | eb4bcbab870baa6b |
| `sma_crossover` | AMZN, SPY | d6b116ddee054524 |

- Backend already running from previous session — health check passed
- Alpaca paper account: PA38Z548DIRR — $99,335.35 cash, ACTIVE, trading unblocked
- Cycle logs returning `market_open: false` (correct — Sunday, market closed)
- Web UI at `http://127.0.0.1:8000/` — confirmed accessible
- **No action needed from you Monday morning** — sessions are live and will fire automatically

---

### Accomplished (Session 74)

#### off-grid-living — Initial master outline (752 lines, 16 domains)

Created `projects/off-grid-living/master-outline.md` from scratch (project directory was empty). Covers every major domain with key questions, subsections, and cost estimates:

1. Site selection (evaluation checklist, water rights, zoning by state)
2. Shelter (7 structure types, owner-built cost estimates)
3. Water (source → treatment chain → distribution → storage; daily needs math)
4. Food production (caloric math: 0.5–1 acre feeds 2 adults; annual/perennial/livestock/aquaculture)
5. Food preservation (per-person-per-year targets, root cellar specs)
6. Energy (solar sizing, battery chemistry, micro-hydro, cost estimates)
7. Heating/cooling (wood supply math: 1–4 cords/year, passive cooling)
8. Waste/sanitation (composting toilet, greywater, solid waste)
9. Medicine (pharmaceutical stockpile list, herbal garden, equipment, skills priorities)
10. Tools (3-tier inventory from founding tools through blacksmithing)
11. Communications (GMRS, ham radio, satellite, analog fallback)
12. Security (animal/human threats, firearms, legal framing)
13. Community/governance (labor specialization, decision-making)
14. Finances (transition phases, homestead revenue streams, barter)
15. **Disaster scenarios** — power outage, storm, pandemic, economic collapse, civil unrest, **nuclear event** (fallout shelter design for root cellar retrofit, 7-10 rule, KI dosing, post-fallout farming guidance)
16. Skills (table with time-to-competence and learning paths)

Includes cross-domain dependency map and phased development roadmap. Commit: `b420466`.

#### resistance-research — April 12/13 monitoring pass

4 new developments added to `litigation-tracker-2026.md`:

1. **Abrego Garcia v. Noem** — DOJ demanded Judge Xinis dissolve injunction by April 17 or "seek relief from a court not having the same views." Xinis refused. April 20 briefing + April 28 hearing set. DOJ's "third-country deportation" theory (Liberia) is a live template.

2. **NPR/PBS defunding EO** — Judge Moss (D.D.C.) permanent injunction March 31 — First Amendment viewpoint discrimination. Doctrinal record now exists against viewpoint-based executive defunding.

3. **MSPB immigration judges ruling** — MSPB held fired IJs lack appeal rights (inferior officers); Federal Circuit appeal filed. **Key**: rationale is identical to Schedule Policy/Career "policy-influencing function" language — if affirmed, ~50k Schedule F employees may lose all MSPB appeal access.

4. **CIT Section 122 detail** — Panel (Barnett/Kelly/Stanceu) "sharply probed" government; post-argument analysis mirrors SCOTUS IEEPA skepticism.

#### seedwarden — image audit
All 120 native-plants images already cached. Stale "0/18 complete" note corrected in PROJECTS.md.

---

### Accomplished (Session 73)

#### open-source-rideshare — Flutter FCM notification routing

Both Flutter apps now have full notification tap routing. When a user taps a push notification:

**Rider app routing:**
- `ride_matched`, `driver_en_route`, `driver_arrived` → `/ride/:id` (RideTrackingScreen)
- `ride_completed` → `/ride/:id/rate` (RideRatingScreen)
- `ride_cancelled` → `/` (HomeScreen)
- `payment_received`, `fare_split_request` → `/ride/:id` or `/history`

**Driver app routing:**
- `ride_matched` → `/ride/:id` (ActiveRideScreen)
- `background_check_approved`, `background_check_action_required` → `/profile`
- `payout_completed`, `payment_received` → `/earnings`
- `ride_completed`, `rating_received` → `/history`

Terminated-app taps are handled via `consumePendingDeepLink()` called in `HomeScreen.initState`.

Also: **fixed a `.gitignore` bug** — root `lib/` rule was blocking the Flutter `lib/` directories from being tracked. Added `!projects/**/lib/` override. Flutter apps are now committed (45 files, first-time commit).

Commit: `6f4f946` on `feature/background-checks-firebase-push`. Branch now has 4 commits beyond master. Backend: 1,817 tests passing.

#### resistance-research — April 12 second monitoring pass

6 significant developments captured (not in first pass):
1. **White House ballroom remand (April 12)** — D.C. Circuit majority sends case back to Judge Leon for fact-finding; April 17 deadline likely forces SCOTUS shadow-docket application
2. **DHS shutdown resolved** — 48-day partial shutdown ended via executive memo + CR through May 22; fund-redirection authority contested under ICA
3. **Mail voting EO — second lawsuit** — Lawyers' Committee + NAACP + Common Cause + Black Voters Matter adds 15th Amendment theory; no TRO yet
4. **Schedule F (Schedule Policy/Career) in effect** — March 9, strips civil-service protections from ~50,000 employees
5. **No Kings electoral pivot** — June 14 next national mobilization; Eyes on ICE civilian monitoring program building
6. **Ramirez Ovando — Tenth Circuit appeal filed** — jurisdictional squeeze risk

---

### Accomplished (Session 72) — STOCKBOT PAPER TRADING READY FOR MONDAY

**Stockbot is now ready for paper trading at Monday's market open (9:30 AM ET, April 14).**

#### Bugs found and fixed

1. **Web UI auth broken (critical)** — Every frontend API call was returning HTTP 401. Root cause: `web/.env` was missing, so `VITE_API_KEY` compiled as an empty string in the React bundle. Fixed: created `web/.env` with the correct API key, rebuilt the frontend bundle.

2. **`ib_insync` crash on every trading cycle (critical)** — `src/brokers/__init__.py` imported `IBKRBroker` at module level. When `TradingSession` ran its trade cycle in a `ThreadPoolExecutor` thread, Python processed the brokers package, `asyncio.get_event_loop()` raised `RuntimeError` (threads have no default event loop), and every single cycle failed immediately. Fixed: made IBKR/TDA imports lazy in both `src/brokers/__init__.py` and `src/brokers/broker_factory.py`.

3. **Cycle log endpoint returned empty** — `GET /api/paper-trading/cycle-log` was reading from the deprecated `app.state.active_trading_session` instead of the current `app.state.paper_trading_sessions` dict. Fixed to aggregate across all running sessions.

#### End-to-end verification
- Started backend, started a momentum session (SPY/QQQ/AAPL), polled status: `running`, `error: null`, `market_open: false` (expected on Sunday)
- Cycle logs returned correctly
- Session stopped cleanly

#### Strategy choices for Monday
| Strategy | Tickers | Logic |
|---|---|---|
| `momentum` | SPY, QQQ, MSFT | 21-day return threshold — trend-following, best for liquid ETFs |
| `rsi_mean_reversion` | AAPL, NVDA | RSI-14 — counter-trend, rare triggers, good complement |
| `sma_crossover` | AMZN, SPY | 10/50 SMA cross — classic confirmation, very low frequency |

See `PAPER_TRADING_MONDAY.md` in the stockbot directory for exact startup commands.

---

### Accomplished (Session 71)

1. **Resistance-research — April 12 monitoring pass** (commit `94589a0`):
   - Gonzalez v. CBP: compliance violation confirmed (Sacramento Home Depot sweep, pre-printed forms, U.S. citizen arrested)
   - Mail voting EO + 23-state suit: USPS blocking mail ballots for anyone not on DHS/SSA list
   - White House ballroom D.C. Circuit stay — expires April 17, SCOTUS shadow-docket imminent
   - CIT tariff hearing (April 10): no ruling yet
   - No Kings protests: 8-9M participants, largest in U.S. history

2. **Open-source-rideshare**: Live driver ETA push + background check notifications (8 new tests, 1,809 → 1,817). Branch: `feature/background-checks-firebase-push`.

### In Progress
- **Stockbot**: 3 paper trading sessions live and cycling. First market-open trades fire Monday 9:30 AM ET (April 14, 13:30 UTC). Monitor: `curl -H "Authorization: Bearer $STOCKBOT_API_KEY" http://127.0.0.1:8000/api/paper-trading/session-results`
- **Open-source-rideshare**: `feature/background-checks-firebase-push` has 7+ commits beyond `master` (incentive system added Session 79). Push to GitHub still blocked — needs SSH key or credential helper.
- **Seedwarden**: 19 products ready. PDF mockup images still needed. Region 5 (Southwest) content gap (14 species).
- **off-grid-living**: Domains 3, 4, 6, 7 complete. Next: `05-food-preservation.md` or `08-medical-health.md`.
- **open-repo**: Landscape research, architecture notes, MVP protocol design complete. Next: content import pipeline (OpenFarm extraction script).

### Needs Your Input

- [ ] **MONDAY MORNING — Stockbot**: After 9:30 AM ET Monday (April 14), check first cycle logs: `curl -H "Authorization: Bearer $STOCKBOT_API_KEY" http://127.0.0.1:8000/api/paper-trading/session-results` — did momentum fire? Any errors?
- [ ] **GitHub push auth on Pi** — choose one:
  - (a) `git config --global credential.helper store` then `git push` (enter username + PAT once, stored)
  - (b) `ssh-keygen -t ed25519` then add `~/.ssh/id_ed25519.pub` to GitHub account settings
- [ ] **Open-source-rideshare — merge feature branch** (once push works): push `feature/background-checks-firebase-push` and open a PR — 7+ commits including background checks, Firebase, tipping, incentive system
- [ ] **Resistance-research — April 14 checkpoints**: CBP report noon + Eaton conference 3 PM (IEEPA refund Phase 1 readiness). Also watch Judge Leon's remand response (underground infrastructure scoping) — the key pre-condition before any SCOTUS ballroom application.
- [ ] **Resistance-research — April 17 stay expiration**: White House ballroom D.C. Circuit stay expires. SCOTUS application expected. Nashville (Crenshaw) watch continues.
- [ ] **Open-source-rideshare — Docker for integration tests** (~1,853 unit tests pass; integration tests need Docker/PostgreSQL).
- [ ] **Seedwarden — mockup images**: #1 Etsy conversion blocker. Canva or mockup generator needed.
- [ ] **Seedwarden — Taraxacum photo attribution**: Dandelion habit photo is CC BY-SA 3.0 (Greg Hume) — needs photo credits page before listing.
- [x] **Git identity** — resolved (thorn / thorn@local).
- [x] **Stockbot venv** — rebuilt with `ta` library.
- [x] **Workout — comprehensive plan** — complete and waiting review.

### Suggested Priorities for Next Session
1. **Stockbot** — April 14 AM: check first market-open cycle logs after 9:30 ET. Did momentum fire? Any signals? Any errors?
2. **Resistance-research** — April 14 afternoon: CBP noon report + 3 PM Eaton conference on IEEPA refund implementation. Leon remand response watch. Update tracker.
3. **open-source-rideshare** — If GitHub auth resolved: push `feature/background-checks-firebase-push` and open PR.
4. **off-grid-living** — `05-food-preservation.md` (next domain: canning, dehydration, fermentation, root cellar design, freeze-drying, water-glassing, lacto-fermentation deep dives — note: section 7 of `04-food-production.md` already covers overview, so this doc goes deeper).
5. **open-repo** — Content import pipeline: write extraction script for OpenFarm (crop/planting data → procedure schema), test with 10 records.
6. **Seedwarden** — PDF mockup images when ready.

---

## Your Notes for Orchestrator

> Leave feedback, redirections, or unblocking information here.
> The orchestrator reads this at the start of each session and clears it after processing.

---

## History

### April 13, 2026 (Session 79)
- Resistance-research: April 13 evening monitoring — no SCOTUS ballroom application filed; Leon remand response still pending (key pre-condition); Maryland April 17 deadline MOOT (Xinis disposed April 12, hearing April 28); CRITICAL CORRECTION: IEEPA tariffs already struck down 6-3 SCOTUS Feb 20 2026 — April 14 CIT conference is about REFUND IMPLEMENTATION; Section 122 is the live tariff fight. Tracker corrected.
- off-grid-living: 04-food-production.md complete (1,301 lines) — caloric math, annual/perennial crops, livestock, aquaculture, seed saving, soil systems, food preservation, water, cost tables, disaster scenarios including post-nuclear farming.
- open-source-rideshare: driver incentive/bonus program system — quest/peak-hours/streak/earnings-guarantee types, 6 new files, 36 tests, committed.

### April 13, 2026 (Session 78)
- Resistance-research: April 13 afternoon monitoring — May Day coalition significantly larger (NEA toolkit operational, NNU 200k, CTU formal vote, federal sector unions); ballroom SCOTUS app pending (no filing yet); Nashville no ruling; AFGE/VA CBA restoration added to tracker; CBP April 14 report is next checkpoint.
- off-grid-living: 07-heating-cooling.md complete (846 lines) — building envelope R-values, passive solar, wood stove sizing/species BTU table, rocket mass heater, masonry heater, propane, mini-split COP table, evaporative cooling, earth tubes, emergency protocols.
- open-repo: mvp-protocol-design.md complete (711 lines) — 5 JSON-LD content type schemas, endorsement schema, ActivityPub federation protocol, 5-phase bootstrapping plan, MVP stack decisions, success metrics.

### April 13, 2026 (Session 77)
- Stockbot: Fixed session persistence bug (shutdown was marking is_active=False, killing auto-resume on restart). Fixed results active flag. Added /api/paper-trading/session-results endpoint. All 3 sessions running.
- Resistance-research: April 13 monitoring — Roberts solo SCOTUS stay reinstated MSPB firing (huge: MSPB without quorum, 10k+ appeals frozen, Trump v. Slaughter signal); ballroom SCOTUS app imminent; Nashville dismissal imminent; May Day Strong general strike (May 1).
- off-grid-living: 06-energy-power.md complete (997 lines) — solar sizing, LiFePO4/lead-acid battery chemistry, micro-hydro, cost tables, EMP hardening.
- open-source-rideshare: Driver tipping system (37 new tests, TipRecord model, Stripe, 48h window, notifications).
- seedwarden: Wild edibles photos confirmed (CC0+CC BY-SA 3.0), native plants cross-links fixed, Region 5 content gap identified.
- open-repo: Landscape research initiated — 16-platform survey + architecture notes. Missing layer: practical/procedural knowledge + connective tissue. Architecture: federated + IPFS + ActivityPub.

### April 13, 2026 (Session 76)
- resistance-research: April 13 monitoring pass — White House ballroom (National Trust "no national security emergency" filing, SCOTUS window open); Abrego Garcia Nashville dismissal risk; MSPB oral argument held awaiting ruling; CIT April 14 CBP report due; mail voting EO clarification (EO 14399 vs 14248).
- off-grid-living: `03-water.md` complete (~850 lines) — full technical reference: wells, springs, rainwater harvesting, water rights law, pumping, cistern storage, treatment decision tree, greywater, emergency protocols, nuclear fallout water, cost tables.

### April 13, 2026 (Session 75)
- Stockbot: started 3 paper trading sessions — momentum/SPY,QQQ,MSFT + rsi_mean_reversion/AAPL,NVDA + sma_crossover/AMZN,SPY. All running, Alpaca connected, cycles logging. Will fire at Monday 9:30 AM ET market open.

### April 12–13, 2026 (Session 74)
- off-grid-living: master-outline.md created (752 lines, 16 domains) — site selection through nuclear disaster protocols, cross-domain dependency map, development roadmap.
- resistance-research: 4 developments — Abrego Garcia v. Noem DOJ/Xinis confrontation (April 20 briefing, April 28 hearing); NPR/PBS permanent injunction; MSPB immigration judges ruling (Federal Circuit appeal); CIT Section 122 panel skepticism.
- seedwarden: verified all 120 plant images cached; stale note corrected.

### April 12, 2026 (Session 73)
- open-source-rideshare: Flutter FCM notification tap routing complete for both rider and driver apps. Fixed gitignore bug (root `lib/` was blocking Flutter lib/ dirs). Flutter apps committed (45 files, first time). Commit: 6f4f946.
- resistance-research: April 12 second monitoring pass — 6 developments (DHS shutdown, White House ballroom remand, mail voting second lawsuit, Schedule F in effect, No Kings pivot, Ramirez Ovando).

### April 12, 2026 (Session 72)
- Stockbot: Paper trading ready for Monday. Fixed 3 critical bugs: (1) web UI auth broken — missing `web/.env`, frontend compiled with empty API key, all calls 401; (2) `ib_insync` crash on every trading cycle due to `asyncio.get_event_loop()` in ThreadPoolExecutor thread; (3) cycle-log endpoint read from deprecated session field. End-to-end verified. Strategy choices: momentum/SPY,QQQ,MSFT + rsi_mean_reversion/AAPL,NVDA + sma_crossover/AMZN,SPY.

### April 12, 2026 (Session 71)
- Resistance-research: April 12 monitoring — 4 developments added (Gonzalez v. CBP Sacramento compliance violation; mail voting EO + 23-state suit; White House ballroom D.C. Circuit stay; CIT tariff hearing). March 28 No Kings protests: 8-9M, largest in U.S. history.
- Open-source-rideshare: Live driver ETA push to rider via WebSocket + background check result notifications (push+SMS on CLEAR/CONSIDER/SUSPENDED). 8 new tests (1,809 → 1,817).
- GitHub push block identified and documented.

### April 12, 2026 (Session 70)
- Resistance-research: published/ regenerated — Domains 10-15 fiscal estimates + subsections 10f/11f/14f now in published copy (2,497 → 2,595 lines).
- Open-source-rideshare: Checkr background check integration + Firebase FCM push notifications (feature/background-checks-firebase-push). 101 new tests (1,708 → 1,809).

### April 12, 2026 (Session 69)
- Resistance-research: Domains 11-15 deepened — inline fiscal estimates added to all 25 subsections; new subsections 11f (Dental/Vision/LTC — Germany/Japan/Canada models, $50-100B/year LTC benefit) and 14f (Use of Force/De-escalation — Camden NJ model, RAND 28-48% force reduction, $10-14B/year). All 22 domains now at full depth. Proposal 2,466 → 2,544 lines.

### April 12, 2026 (Session 68)
- Resistance-research: Domain 10 deepened — fiscal estimates added to 10a-10e; new subsection 10f (Universal Pre-K + Childcare) — Heckman $7-13/dollar ROI, France/Nordic/Canada precedents, $55-85B/year net. Proposal 2,446 → 2,466 lines.

### April 12, 2026 (Session 67)
- Open-source-rideshare: Audit Logging & Compliance Reporting — AuditLog model (9 categories, 3 severities), compliance report generator, 3 admin endpoints, 14 event dispatchers wired into existing endpoints, 94 tests. Unit tests 1,614 → 1,708.

### April 12, 2026 (Session 66)
- Open-source-rideshare: SMS/Email notification integration (Twilio + SendGrid, 13 templates, user preferences, 5 endpoints, 113 tests). Unit tests 1,501 -> 1,614.

### April 12, 2026 (Session 65)
- Open-source-rideshare: Driver payout & settlement system (Stripe Connect onboarding, bank management, settlement calc, 11 endpoints, 117 tests). Unit tests 1,384 -> 1,501.

### April 12, 2026 (Session 64)
- Open-source-rideshare: Fare splitting (6 endpoints, FareSplit model, equal/custom splits, accept/decline/pay, 118 tests). Unit tests 1,266 -> 1,384.

### April 12, 2026 (Session 63)
- Open-source-rideshare: Multi-stop rides / waypoints (7 endpoints, RideWaypoint model, OSRM multi-point routing, 113 tests). Unit tests 1,153 -> 1,266.

### April 12, 2026 (Session 62)
- Open-source-rideshare: Recurring rides / commute scheduling (7 endpoints, RecurringRide model, scheduler integration, 106 tests). Unit tests 1,047 -> 1,153.

### April 12, 2026 (Session 61)
- Open-source-rideshare: Admin document verification (5 admin endpoints, 89 tests, state machine review flow). Unit tests 1,018 -> 1,047.

### April 12, 2026 (Session 60)
- Open-source-rideshare: Saved locations (home/work/custom favorites, CRUD, ride request integration, 88 tests) + Vehicle mapper bugfix (40 tests fixed). Unit tests 980 -> 1,018.

### April 12, 2026 (Session 59)
- Open-source-rideshare: Driver ETA estimation — OSRM routing with haversine fallback, 2 REST endpoints, WebSocket live ETA push, 44 tests. Unit tests 980 -> 1,024.

### April 12, 2026 (Session 58)
- Open-source-rideshare: Transparent demand pricing — geohash demand zones, Redis sliding window, supply counting, linear capped multiplier (1.5x default), full rider transparency, admin config, 69 tests. Unit tests 911 -> 980.

### April 12, 2026 (Session 57)
- Open-source-rideshare: In-app chat messaging — ChatMessage model, chat service (ride-status validation, persistence, read receipts, unread counts), WebSocket chat_message handler + REST fallback (4 endpoints), 68 tests. Unit tests 843 -> 911.

### April 12, 2026 (Session 56)
- Open-source-rideshare: Vehicle management & WAV matching — Vehicle model (9 types, capacity, WAV flag), 6 CRUD endpoints, WAV-aware ride matching, accessibility_required on rides, 53 tests. Unit tests 790 -> 843.

### April 12, 2026 (Session 55)
- Open-source-rideshare: Ride pooling (shared rides) — RidePool/PoolLeg models, pool matching (cosine similarity + detour), 6 pool endpoints, discounted fares (25%/35%), 46 tests. Unit tests 744 -> 790.

### April 12, 2026 (Session 54)
- Open-source-rideshare: Ride & driver metrics dashboard (2 admin analytics endpoints, 8 schemas, 20 tests). Unit tests 724 -> 744.

### April 12, 2026 (Session 53)
- Open-source-rideshare: Admin feedback & disputes (7 endpoints, 6 schemas, Alembic migration, 65 tests). Unit tests 659 -> 724.

### April 12, 2026 (Session 52)
- Open-source-rideshare: Service area geofencing (polygon boundaries, admin CRUD, ride validation, GiST spatial index, graceful degradation, 31 tests). Unit tests 628 -> 659.

### April 12, 2026 (Session 51)
- Open-source-rideshare: Ride receipt endpoint (detailed fare breakdown, payment info, driver/vehicle details, promo/tip, receipt number). Fixed 3 pre-existing auth test failures. Unit tests 615 -> 628.

### April 12, 2026 (Session 50)
- Open-source-rideshare: Promo code & referral system (flat/percent discounts, admin CRUD, rider validation, referral codes, fare estimate/request integration, 38 tests). Unit tests 577 -> 615.

### April 12, 2026 (Session 49)
- Seedwarden: Product readiness pass — fixed cross-links, updated product audit (19 products), verified survival garden completeness, voice consistency pass.

### April 12, 2026 (Session 48)
- Open-source-rideshare: Rider cancellation during retry (explicit retry-aware cancellation policy, WebSocket retry metadata, dispatch race-condition guard, 8 tests). Unit tests 507 -> 515.

### April 12, 2026 (Session 47)
- Open-source-rideshare: Admin cancellation stats dashboard (2 endpoints, 3 schemas, 12 tests) + driver earnings enhancements (cancellation fee income, daily timeseries, 13 tests). Unit tests 482 -> 507.

### April 12, 2026 (Session 46)
- Open-source-rideshare: Dispatch retry logic (exponential backoff retries for unmatched rides, 5 max retries, auto-cancel after exhaustion). Unit tests 468 -> 482.

### April 12, 2026 (Session 45)
- Open-source-rideshare: Dispatch scheduler (background asyncio task, auto-dispatches SCHEDULED rides within 15-min window, matching + WebSocket notifications). Unit tests 451 -> 468.

### April 12, 2026 (Session 44)
- Open-source-rideshare: Scheduled rides feature (SCHEDULED status, scheduling service, 3 endpoints, cancellation support, 2 Alembic migrations). Unit tests 420 -> 451.

### April 12, 2026 (Session 43)
- Open-source-rideshare: Cancellation fee collection via Stripe (PaymentType enum, create_cancellation_payment_intent, frontend client_secret). Unit tests 408 -> 420.

### April 12, 2026 (Session 42)
- Open-source-rideshare: WebSocket heartbeat & connection health (30s ping, 10s timeout, dead connection pruning, activity tracking, health diagnostics). Unit tests 379 -> 408.

### April 12, 2026 (Sessions 40-41)
- Open-source-rideshare: Cancellation policy engine, notification service stub, driver rating aggregation, rate limiting middleware, admin SOS WebSocket. Unit tests 318 -> 385. Seedwarden: 7-region survival garden listing copy.

### April 12, 2026 (Session 37)
- Open-source-rideshare: Alembic migration for safety tables. Seedwarden: Survival Garden expanded to 7 regions (+414 lines).

### April 12, 2026 (Session 36)
- Open-source-rideshare: Safety service (SOS alerts, trip sharing, emergency contacts). 8 API endpoints, 51 tests. Unit tests 202 -> 253.

### April 12, 2026 (Session 35)
- Open-source-rideshare: Auth service tests (4->16), auth endpoint tests (13), deps tests (13), routing tests (6). Unit tests 158 -> 202.

### April 12, 2026 (Session 34)
- Open-source-rideshare: Profile endpoint tests (14) + ride endpoint tests (29). Unit tests 129 -> 158.

### April 12, 2026 (Session 33)
- Open-source-rideshare: Profile screens for both Flutter apps (rider + driver). 4 new backend endpoints.

### April 12, 2026 (Session 32)
- Workout: Comprehensive multi-tier plan (1,053 lines, 3 equipment tiers, 4 frequencies).
- Open-source-rideshare: Ride history + rating flow for rider app. Driver ride history screen.

### April 12, 2026 (Session 31)
- Resistance-research: Publication-ready format created in `published/` — clean proposal (2,497 lines), executive summary, README index. Working originals untouched.
- Seedwarden: Companion Planting Chart product (382 lines, $5, 40 plants, Etsy listing copy).

### April 12, 2026 (Sessions 28-30)
- Resistance-research: Domains 7-8 deepened to full evidence standard (Session 28). Domain 22 (Reparations & Racial Justice) added — 84 lines, 13th feedback loop (Session 29). Cross-domain quality pass completed — Domains 4, 5, 9 deepened, all 22 domains at full evidence standard, proposal at 2,446 lines (Session 30).

### April 11, 2026 (Session 26)
- Resistance-research: Domain 21 (Data Privacy & Digital Surveillance) added (~80 lines). Proposal at 2,055 lines, 21 domains, 12 feedback loops.
- Seedwarden: SEO-optimized titles applied to 11 of 17 Etsy listings.

### April 11, 2026 (Session 25)
- Resistance-research: Domain 20 — Economic Concentration and Antitrust added (~130 lines). Proposal at 1,927 lines, 20 domains, 11 feedback loops. Corporate Power-Democracy Loop. Executive summary fully updated.

### April 11, 2026 (Session 24)
- Resistance-research: Cryptographic voting systems deep dive (remote-electronic-voting-research.md Section 4 expanded, 370->490 lines). Three-layer verification model. ElectionGuard deployments documented.
- Resistance-research: Algorithmic decision-making in immigration enforcement (new file, 270 lines). Domain 16d expanded.
- Seedwarden: Etsy SEO and market research (new file, 402 lines). All exploration queue items complete.

### April 11, 2026 (Session 23)
- Resistance-research: Section 5.5 International Benchmarks & Fiscal Analysis added (1,649->1,781 lines). $500-800B/year investment offset by internal revenue.
- Seedwarden: Tier 2 improvements — caloric tables for 4 regions, seasonal growing calendar for 19 plants.
- Open-source-rideshare: Regulatory compliance research (1,002 lines, 9 sections, 7 city deep dives).

### April 11, 2026 (Sessions 20-22)
- Resistance-research: Domains 16-19 added (Immigration, Labor, Social Safety Net, National Security). Proposal at 1,649 lines, 19 domains, 10 feedback loops.
- Seedwarden: Legal disclaimers (all 18 products), free lead magnet, bundle listings, cross-links, voice pass, PDFs regenerated. Pre-launch 6/8 done.
- Open-source-rideshare: Cooperative business model research (744 lines, 6 cooperatives analyzed)

### April 11, 2026 (Sessions 1-19)
- Democratic renewal proposal (694 lines, 5 parts), litigation tracker, crisis analysis updates
- Stockbot: 2 bugs fixed in dashboard_api.py
- Open-source-rideshare: full architecture + backend scaffold through admin API + deployment guide (45->253 tests)
- Resistance-research: proposal expanded to 1,319 lines, 19 domains, remote voting integration

### April 10, 2026
- System initialized — workspace scaffolding built (PROJECTS.md, WORKLOG.md, CHECKIN.md, BLOCKED.md, INBOX.md)
- Agent profiles and slash commands installed
- Awaited: project goals, Pi SSH setup, API key on Pi
