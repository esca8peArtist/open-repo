# Check-in Briefing

> This file is updated by the orchestrator before going idle.
> When you drop in, read this first. It's designed to get you up to speed in under 5 minutes.
> After reviewing, clear the "Since Last Check-in" section and leave notes in "Your Notes" for the orchestrator to pick up.

---

## Since Last Check-in

**Period**: April 13, 2026
**Sessions run**: 75–92

### Accomplished (Session 92)

#### resistance-research — Labor policy domain evidence deepening
`domain-deepening/labor-evidence.md` (663 lines):

- **Union decline**: Private-sector density 6.0% (2024) vs. 34–35% peak (1950s). Public-sector density still 32.5% — the labor movement now lives almost entirely in government employment.
- **Productivity-pay divergence**: +59.7% productivity vs. +15.8% typical worker pay (1979–2019, EPI). Labor share of income: 63–65% (1970s) → 57–58% (2020s).
- **Minimum wage — Card-Krueger**: The 1994 payroll-data reanalysis rebutted the Neumark-Wascher critique on methodological grounds. Dube/Lester/Reich (2010) county-pair design; Cengiz et al. (2019) bunching estimator — both find no employment loss at normal policy ranges. Monopsony framework (Manning 2003, Dube 2019) is the theoretical explanation. Germany 2015 experiment: 70,000–900,000 jobs predicted lost; near-flat actual (IAB). Seattle UW hours-reduction finding: methodological flaw documented (40% exclusion of multi-location employers).
- **Tipped minimum wage**: $2.13 since 1991. Seven equal-pay states (CA, OR, WA, MN, NV, MT, AK). ROC United research: tipped workers in states with separate sub-minimum wage face 2x sexual harassment rate.
- **Sectoral bargaining**: Germany 44% coverage (extension mechanism; employer-exit risk documented), France 98% coverage with only 8% union density (erga omnes extension), Austria 95–98% (compulsory chambers), Ghent system (union-administered UI → Denmark 67%, Belgium 65% union density).
- **Gig economy**: IRS estimates $54B/year in lost payroll taxes from misclassification. EU Platform Workers Directive (2024) — presumption of employment. UK *Uber v. Aslam* [2021] UKSC 5. California Prop 22: $224M gig industry campaign — currently under CA Supreme Court review.
- **Organizing rights**: EPI: 41.5% of organizing campaigns see illegal firings; 78% see captive audience meetings. NLRB case processing: 18–24 months from petition to resolution. Canada card-check comparison: 27–29% density vs. US 10%. NLRA 1935 racial exclusion: 2.4M farmworkers + 2.5M domestic workers still uncovered.
- **OSHA**: 1:82,000 inspector ratio vs. ILO 1:10,000 minimum; 165-yr inspection cycle at current pace. Heat deaths +30% (2013–2022); still no federal heat stress standard. US fatal work injury rate 3.5/100K vs. Germany 1.24/100K.
- **Paid leave**: FMLA covers only ~56% of workers (employer size/tenure thresholds); <20% can afford to take it unpaid. US = 0 weeks statutory paid parental leave (only wealthy country). State experiments (CA, NJ, NY, RI, MA, CO) show no employment effects.
- **Non-competes**: FTC (2024) rule covering ~30M workers (18% of workforce), estimated $300B annual wage gain — struck down 5th Circuit August 2024. Starr (2019): 4% wage suppression in enforcing states vs. California.
- **Mandatory arbitration**: 60.1M workers (56% of nonunion private-sector) in mandatory arbitration (Colvin 2018, up from 2% in 1992). Win rate: 21.4% in arbitration vs. 36.4% in federal court. Average award: $23,548 vs. $143,497 in court.
- **Fiscal estimates**: Federal paid leave ~$200B/yr (0.38% payroll tax split); OSHA rebuild ~$2.2B/yr (tripling current budget); minimum wage: EPI estimates $15/hr reduces SNAP $4.6B/yr + Medicaid $3.4B/yr.
- **7 contested findings** with methodological precision (employment effects above 60% median, German coverage decline warning, union productivity tradeoff, portable benefits adverse selection, non-compete California exceptionalism, agricultural organizing structural limits, arbitration reform political ceiling post-*Epic Systems*).

---

### Stockbot Note
Paper trading LIVE since April 13. First market open was Monday April 14. Orchestrator cannot check cycle logs without `STOCKBOT_API_KEY` in env. Check manually:
```
curl -H "Authorization: Bearer $STOCKBOT_API_KEY" http://127.0.0.1:8000/api/paper-trading/cycle-log?limit=20
```
Or `http://127.0.0.1:8000` → Trading page.

---

### Needs Your Input

**open-source-rideshare — GitHub push still blocked**
Sessions 77–92 of commits piling up locally. Options:
- (a) `git config --global credential.helper store` + push once with username/PAT
- (b) `ssh-keygen -t ed25519` on Pi → add public key to GitHub account
- (c) `git remote set-url origin git@github.com:...` + add SSH key to GitHub

**resistance-research — April 17/20 events: what happened?**
- Did Leon act after the April 17 D.C. Circuit stay expired? Did SCOTUS intervene? Did construction start?
- CAPE Phase 1 launched April 20 — how did it go? Any reporting on the $46B ACH enrollment gap or rejected refunds?
- Abrego Garcia DOJ brief was due April 20 — what position did they take?
Drop updates in INBOX.md when you have them.

**Stockbot — paper trading check-in**
Can you share the cycle logs or a screenshot from the Trading page? We can't pull them without the API key in env. Without performance data, stockbot work is stuck at monitoring-only.

---

### Suggested Priorities (Next Session)
1. **Resistance-research**: April 20 post-event monitoring pass (needs user to drop news in INBOX.md first). Alternately: off-grid-living quality review pass (all 16 domains complete — time for consistency + cross-reference audit).
2. **Open-source-rideshare**: Trip/driver activity heatmap analytics, or rider/driver notification history log.
3. **Seedwarden**: PDF mockup images still the #1 Etsy conversion blocker — any Canva access?
4. **Resistance-research deepening queue**: 5 domains with no dedicated deepening file yet — Social Safety Net (18), National Security (19), Economic Concentration (20), Data Privacy (21), Reparations (22).

---

### History

#### Accomplished (Session 90)

#### resistance-research — Tax policy evidence deepening
`domain-deepening/tax-policy-evidence.md` (609 lines, 130 citations). Billionaire effective rates, buy-borrow-die, TCJA pass-through, $688B tax gap, starve-the-beast refutation, ETI revenue-maximizing rates (56–73%), FTT design lessons, carbon tax evidence, $580–995B reform range.

#### open-source-rideshare — Rider spending analytics + driver tax summary
41 new tests. Full suite: **2,386 passing.** 4 endpoints: rider spending summary/CSV, driver 1099 summary/CSV.

---

#### Accomplished (Session 89)

#### resistance-research — Criminal justice evidence deepening
`domain-deepening/criminal-justice-evidence.md` (658 lines, 79 citations):
- Lead-crime ROI $17–$221/dollar; READI Chicago 63% fewer shooting arrests (J-PAL 2022 RCT); body cameras null result (DC Metro RCT); Fryer vs Knox-Lowe-Mummolo conflict handled; Ban the Box 3.4 ppt harm to Black male employment; Portugal 20-yr decriminalization vs. Oregon Measure 110; RAND prison education $1=$5.

#### off-grid-living — ALL 16 DOMAINS COMPLETE
`16-skills-knowledge.md` (2,091 lines). 4-tier skill framework; Tier 1 survival; Tier 2 infrastructure; food production; advanced skills; learning pathways; community skill inventory; age-staged child development; mental health; ~30 book library; cost tables $4,600/$13,260/$32,970; master checklist.

#### open-source-rideshare — Lost and found system
60 new tests. **2,345 passing.** LostItemReport model; reported/matched/claimed/returned/donated/discarded status machine; 9 endpoints; self-referential matched_report_id FK; migration a1b2c3d4e5f6.

---

#### Accomplished (Sessions 85–87)

#### resistance-research — April 13 current status + April 20 watch brief
- `monitoring/2026-04-13-current-status.md`: Leon/Ballroom CODE RED — April 17 stay expiry live. Abrego Garcia contempt threat live. Nashville/Crenshaw dismissal imminent. CAPE Phase 1 confirmed April 20. Humphrey's Executor narrowing likely.
- `monitoring/2026-04-20-watch.md` (46 sources): CAPE Phase 1 $120B enrolled of $165B total ($46B ACH gap); Abrego Garcia 4 scenarios (Liberia + exec-power most likely); Branch C (injunction reinstates) strongest for ballroom; May Day NEA/SEIU/National Nurses United/CTU/UTLA confirmed.

#### open-source-rideshare — Driver license/registration + Driver onboarding workflow
- 131 new tests, 2,239 passing. DriverLicense, VehicleRegistration models; 15 endpoints.
- Driver onboarding checklist (BGC + license + registration + inspection + insurance + profile); activate/suspend endpoints; 49 new tests; 2,288 passing.

#### off-grid-living — Domains 12, 13, 14
- `12-communications.md` (1,854 lines): ham radio, GMRS, Starlink, EMP hardening, grid-down protocols
- `13-community-organization.md` (1,785 lines): governance, mutual aid, conflict resolution, emergency decision-making
- `14-finances-trade.md` (1,516 lines): financial transition model, revenue streams, raw milk legality, USDA FSA loans, barter/LETS, 3 sample financial models

#### seedwarden — Pre-launch audit + Apartment Growing listing copy
All 21 products: legal disclaimers verified, cross-links verified. Apartment Growing Complete Guide upgraded Tier 3→Tier 2. Only blocker: PDF mockup images.

#### open-repo — OpenFarm content import pipeline
`content-import-openFarm.md` + `scripts/import_openFarm.py` (full implementation). OpenFarm live API shut down April 2025; CC0 data. Data acquisition path: self-hosted MongoDB export or Internet Archive.

---

#### Accomplished (Sessions 85–86)

#### resistance-research — April 17 monitoring brief
`monitoring/2026-04-17-results.md`. Leon SILENT 6 days post-D.C. Circuit remand (CODE RED). Branch C (stay expires, injunction reinstates) = live baseline. SCOTUS: Rao dissent is admin's best asset for cold filing. No Kings March 28 = 8 million participants (largest US single-day). CAPE Phase 1 confirmed April 20. Abrego Garcia April 20 DOJ brief. Humphrey's Executor added.

#### open-source-rideshare — Driver vehicle inspection records
69 new tests. Full suite: 2,108 passed. VehicleInspection (5 types, status machine pending_upload→approved/rejected/expired); 4 driver + 3 admin endpoints; auto-expiry (annual=365d/semi-annual=182d); admin review expires previous approved. Migration included.

#### off-grid-living — `12-communications.md` (1,854 lines)
Ham radio, GMRS/FRS/MURS, Starlink, Iridium/inReach, shortwave, CB, EMP hardening (E1/E2/E3, Faraday construction), grid-down protocols (coded status words GREEN/YELLOW/RED/GREY), power sizing, CBRN nuclear comms assessment, 55+ row cost table, decision matrix.

---

#### Accomplished (Session 84)

#### resistance-research — April 15 monitoring brief
`monitoring/2026-04-15-results.md`. Leon SILENT through April 15. Branch 3 confirmed live baseline. Nashville/Crenshaw still silent. Abrego Garcia Liberia track confirmed. Trump v. Slaughter added.

#### open-source-rideshare — Driver insurance document management
45 new tests. Full suite: 2,039 passed. Status machine pending_upload→approved/rejected/expired. 4 driver + 3 admin endpoints.

#### off-grid-living — `11-shelter-construction.md` (1,830 lines)
Site selection, foundations, stick/timber/earthen/straw bale, roofing, insulation, passive solar, CBRN hardening, decision matrix, cost tables.
