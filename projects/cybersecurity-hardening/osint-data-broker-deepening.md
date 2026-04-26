---
title: "OSINT and Data Broker Landscape: Deepening Research (2025-2026)"
project: cybersecurity-hardening
created: 2026-04-26
status: complete
confidence: high — primary sources (FTC press releases, CPPA enforcement orders, state legislation texts, independent service testing)
depends_on: threat-model.md, implementation-guide.md
---

# OSINT and Data Broker Landscape: Deepening Research (2025-2026)

**Purpose**: This document deepens the data broker coverage in `threat-model.md` and `implementation-guide.md Part 0`. It identifies gaps in the existing documents, provides 2025-2026 sourced findings, evaluates automated opt-out tools, and proposes specific edits with line numbers to both parent documents.

**Lead finding**: The data broker landscape has changed materially in 2025-2026 in two directions simultaneously — more regulatory teeth (California's DELETE Act is live, Montana closed the warrant loophole, FTC finalized orders against Venntel/Gravy) while government procurement is expanding aggressively (ICE issued a formal RFI for ad tech MAID data, Palantir's ELITE and ImmigrationOS scale up). The regulatory gains are real but they lag the surveillance build-up by at least 18-24 months and do not constrain federal agencies. Opt-out remains the most actionable individual countermeasure, and the California DROP platform has meaningfully reduced the friction of doing so — but only for California residents.

---

## I. Data Broker Market 2026: Scale and Key Players

The data broker market reached approximately $312-342 billion in 2025-2026, with a projected CAGR of 7-10% through 2031-2032. ([The Business Research Company](https://www.thebusinessresearchcompany.com/report/data-broker-global-market-report)) North America remains the largest regional market.

The broker ecosystem breaks into four functional tiers with different threat profiles:

**Tier A — Law Enforcement Data Products (Highest Threat)**
These have confirmed direct contracts with DHS, ICE, FBI, or CBP and are the primary targets for opt-out effort.

- **[LexisNexis / Accurint](https://optout.lexisnexis.com/)** — $9.75M DHS contract (2021, ongoing). Aggregates court records, property records, financial records, address history, relatives, associates. Confirmed integration into Palantir's ELITE platform via the CLEAR product (Thomson-Reuters/LexisNexis are competitors but their data largely overlaps). In May 2025, LexisNexis disclosed a breach of 364,000+ individuals via a third-party development platform. Active civil rights litigation alleges Accurint violates consent and privacy laws for non-citizens. ([TechCrunch breach report](https://techcrunch.com/2025/05/28/data-broker-giant-lexisnexis-says-breach-exposed-personal-information-of-over-364000-people/))

- **[Venntel / Gravy Analytics](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data)** — Collected location data from 17 billion signals per day from ~1 billion mobile devices via advertising SDK ecosystem. Sold location data to DHS, IRS, and FBI without consumer consent. January 2025: FTC finalized order prohibiting both companies from selling sensitive location data. January 2025: Gravy Analytics separately suffered a 17-terabyte data breach when hackers gained root access and control over Amazon S3 buckets — the irony that law enforcement's data source was itself breached is significant. No consumer opt-out mechanism available; FTC order provides the only protection channel. ([FTC press release](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data), [EPIC](https://epic.org/ftc-takes-action-against-data-brokers-for-selling-sensitive-location-data/))

- **[Babel Street](https://www.amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats-to-pro-palestine-student-protestors-migrants/)** — Provides social media OSINT aggregation to DHS agencies. FBI signed a contract worth up to $27 million for 5,000 licenses to Babel Street's Locate X product. Amnesty International (August 2025) identified Babel Street as posing direct surveillance threats to pro-Palestine student protesters. No consumer opt-out exists — this is social media aggregation of public data, not a consumer data broker in the traditional sense. The countermeasure is operational security on social media, not opt-out.

- **[CLEAR / Thomson-Reuters](https://www.thomsonreuters.com/en/products/clear.html)** — Directly confirmed integration into Palantir's ELITE deportation targeting platform. Public records aggregation focused on law enforcement customers. Consumer opt-out is not publicly available for the CLEAR law enforcement product.

**Tier B — Large Commercial Brokers (Medium Threat, High Reach)**
These have no confirmed direct law enforcement contracts but are part of the data ecosystem that feeds Tier A brokers.

- **[Acxiom](https://isapps.acxiom.com/optout/optout.aspx)** — Claims data on 2.5 billion consumers globally, averaging ~1,500 data points per individual. Collects: names, addresses, phone numbers, browsing history, purchase history, demographic data, social media activity. Consumer opt-out is available and does not require identity verification. Opt-out processed within two weeks of email confirmation — but data already sold to marketers before request date is not recalled. ([Acxiom privacy page](https://www.acxiom.com/privacy/us/))

- **[Epsilon](https://us.epsilon.com/privacy/epsilon-data-alliance-opt-out)** — Major marketing data aggregator. Consumer opt-out mechanism is available via Epsilon Data Alliance. Epsilon has created privacy dashboards as part of CCPA adaptation but declined to disclose specific data sources to congressional inquiry (2013 record still stands). No known government contracts for immigration enforcement.

**Tier C — People-Search / Background Check (Direct Public Exposure)**
These are the brokers that expose home addresses and personal associations to anyone who searches — the most actionable category for individual opt-outs.
BeenVerified, Spokeo, WhitePages, Intelius, Radaris, TruePeopleSearch, FastPeopleSearch, and ~200 others. All covered in existing `implementation-guide.md` Part 0 step 0.2. See gap analysis in Section V below.

**Tier D — Credit Bureaus (Statutory Framework)**
Experian, Equifax, TransUnion, Innovis. Subject to Fair Credit Reporting Act (FCRA), not just state privacy law. OptOutPrescreen.com (already in implementation guide) is the primary statutory opt-out for marketing use.

---

## II. The Ad Tech MAID Vector: Emerging 2026 Threat

This is the most important development not adequately covered in the existing threat model.

In January 2026, ICE issued a formal Request for Information (RFI) asking ad tech companies to demonstrate capabilities for supplying location data derived from Mobile Advertising IDs (MAIDs) for investigative use. The RFI did not reference warrants, court orders, or judicial authorization. ([The Register, January 27, 2026](https://www.theregister.com/2026/01/27/ice_data_advertising_tech_firms/), [Biometric Update](https://www.biometricupdate.com/202602/ice-seeks-industry-input-on-ad-tech-location-data-for-investigative-use))

**How MAIDs work**: Every Android and iOS device has an advertising identifier (Google Advertising ID or Apple IDFA). Apps that include advertising SDKs — which is nearly every free app — report the device's location along with the MAID to ad network infrastructure. This data is aggregated by brokers like the now-ordered Venntel. ICE's argument is that purchasing MAID-linked data is legally distinct from the cell phone location data addressed in *Carpenter v. United States* (2018) because it is tied to an advertising ID, not a phone number. This is a thin distinction — the entire MAID enrichment industry exists specifically to cross-reference MAIDs with personal identities.

**Practical implication for users**: Any commercial Android or iOS device running ad-supported apps is continuously generating MAID-linked location data that is legally purchasable by federal law enforcement. This is not addressable through data broker opt-outs alone — it requires the platform-level countermeasures covered in implementation guide Parts 1-3 (GrapheneOS or iOS with privacy hardening).

Sources: [ACLU analysis](https://www.aclu.org/news/privacy-technology/dhs-is-circumventing-constitution-by-buying-data-it-would-normally-need-a-warrant-to-access), [Yahoo News coverage](https://www.yahoo.com/news/articles/ice-bypassing-constitution-buy-ad-154005460.html)

---

## III. Regulatory Landscape 2025-2026: What Changed

### A. California Delete Act — The Most Important Development for Residents

California's SB 362 (2023) created two major mechanisms that came online in 2025-2026:

**The DROP Platform (live January 1, 2026)**: The Delete Request and Opt-Out Platform at privacy.ca.gov allows California residents to submit a single deletion request that cascades to all registered data brokers simultaneously. Brokers have 45 days to retrieve and process deletion requests. Critically, the continuous deletion cycle (brokers must check DROP every 45 days) means re-addition from public records triggers automatic re-deletion — this is qualitatively different from one-time opt-outs. ([California privacy.ca.gov](https://privacy.ca.gov/drop/about-drop-and-the-delete-act/))

**Data Broker Registration Enforcement**: The California Privacy Protection Agency created a Data Broker Enforcement Strike Force. Unregistered brokers face $200/day fines. Recent enforcement:
- ROR Partners LLC (Nevada marketing firm): $56,600 fine for failing to register. ([CPPA announcement](https://cppa.ca.gov/announcements/2025/20251203.html))
- National Public Data / Jerico Pictures (Florida): $46,000 fine — the company that exposed 2.9 billion records in 2024 then filed for bankruptcy without meaningful consumer restitution. ([CPPA enforcement action](https://cppa.ca.gov/announcements/2025/20250220.html))
- Washington state data broker: Fined for failing to register. ([CPPA announcement](https://cppa.ca.gov/announcements/2025/20250729.html))
- CalPrivacy brought a new round of enforcement actions against data brokers in January 2026. ([CPPA 2026 announcement](https://cppa.ca.gov/announcements/2026/20260108.html))

California SB 361 (effective January 2026) additionally requires data brokers to disclose AI use, whether they share data with government entities, and doubles penalties for non-compliance. ([ScanComply analysis](https://scancomply.com/blog/california-sb-361-data-broker-law-2026))

**Limitation**: DROP only covers California residents and only reaches registered data brokers — law enforcement data products like Accurint and CLEAR are categorically exempted from most state privacy frameworks.

### B. Montana SB 282 — Closing the Data Broker Loophole for State Law Enforcement (May 2025)

Montana became the first U.S. state to require a warrant before state or local law enforcement can purchase commercial data. SB 282 (signed May 2025, effective October 1, 2025) prohibits law enforcement from acquiring geolocation data, financial transaction records, biometric information, electronic communications metadata, and "sensitive data" (health status, religious affiliation, immigration status, precise geolocation) from commercial brokers without a judge-signed warrant or subpoena. ([EFF analysis](https://www.eff.org/deeplinks/2025/05/montana-becomes-first-state-close-law-enforcement-data-broker-loophole), [Reason.com](https://reason.com/2025/05/16/new-montana-law-blocks-the-state-from-buying-private-data-to-skirt-the-fourth-amendment/))

**Important caveat**: This applies only to Montana state and local law enforcement — not to federal agencies. ICE and DHS are not covered.

### C. State Comprehensive Privacy Law Expansion

As of late 2025, twenty states have comprehensive consumer privacy laws in effect. Twelve states now require businesses to honor the Global Privacy Control (GPC) browser signal as a valid opt-out of sale/sharing: California, Colorado, Connecticut, Delaware, Maryland, Minnesota, Montana, Nebraska, New Hampshire, New Jersey, Oregon, and Texas. ([ManageEngine state law tracker](https://insights.manageengine.com/privacy-compliance/us-state-data-privacy-laws/))

In 2025 alone, comprehensive laws became newly enforceable in Delaware, Iowa, Minnesota, Nebraska, New Hampshire, New Jersey, Tennessee, and Maryland.

California, Connecticut, and Colorado announced a joint investigative sweep; 10 states formed a Consortium of Privacy Regulators. This coordinated enforcement is a meaningful development — it means data brokers cannot simply relocate to a non-enforcement state.

### D. CCPA Enforcement: Recent Major Penalties

- **Disney**: $2.75 million settlement for CCPA opt-out noncompliance. ([California AG announcement](https://iapp.org/news/a/california-s-attorney-general-issues-largest-ccpa-fine-to-date/))
- **Healthline**: $1.55 million — then-largest CCPA penalty, health data platform. ([WilmerHale analysis](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250708-california-ag-issues-largest-monetary-penalty-in-most-recent-ccpa-enforcement-action))
- **Tractor Supply Company**: $1.35 million fine, required business practice changes. ([CPPA announcement](https://cppa.ca.gov/announcements/2026/20260108.html))

These penalties are significant in context: they represent the regulatory floor for major consumer-facing companies but do not touch the law enforcement data product market, which operates under separate legal frameworks.

### E. FTC Actions Against Location Data Brokers

The FTC finalized two major orders in January 2025:

**Gravy Analytics / Venntel** (January 2025): Banned from selling sensitive consumer location data. Prohibited from collecting data from real-time bidding exchanges for non-auction purposes. Required to delete historical location data. ([FTC final order](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data))

**Mobilewalla** (January 2025): Banned from selling sensitive location data. First FTC allegation that collecting data from ad exchanges for non-auction purposes is an unfair act or practice — a significant legal theory that could constrain the broader MAID ecosystem. ([FTC press release](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-banning-mobilewalla-selling-sensitive-location-data))

**Limitation**: FTC civil enforcement does not cover federal agencies as data purchasers. ICE's purchase of Venntel data was lawful under the third-party doctrine even after the FTC found Venntel's collection practices unlawful — the agencies that bought the data are not parties to the enforcement action.

---

## IV. Automated Opt-Out Tools: Evaluation for Tier 1 Readers

The existing implementation guide (Step 0.3) covers EasyOptOuts and DeleteMe at a high level. This section deepens that evaluation with 2026 data and adds Incogni and Optery.

### Service Comparison Table

| Service | Annual Cost | Broker Coverage | Key Feature | Best For |
|---------|-------------|-----------------|-------------|----------|
| [Incogni](https://incogni.com/) | ~$96/yr ($7.99/mo) | 420+ brokers | Deloitte-verified; fully automated; 60-day re-submission cycle for public, 90-day for private | Tier 1 users wanting hands-off ongoing protection |
| [DeleteMe](https://joindeleteme.com/) | ~$130/yr ($10.75/mo) | ~100 listing brokers + 750 monitored | Human-led removals with before/after screenshots; quarterly reports | Users who want verifiable documented evidence |
| [Optery](https://www.optery.com/) | Free (self-service) / ~$39/yr (automated) | 300-600+ (plan-dependent) | Free tier lets users see their exposure before paying; detailed dashboard | Users who want to understand scope before committing |
| [Privacy Bee](https://privacybee.com/) | ~$96/yr ($8/mo) | 400-885+ (plan-dependent) | Broad broker coverage including non-listing commercial brokers; breach monitoring | Users wanting broadest commercial database coverage |
| [EasyOptOuts](https://easyoptouts.com/) | ~$20/yr | Major brokers | Lowest cost; automated re-submission | Budget-constrained Tier 1 users |

Sources: [TechTimes 2026 guide](https://www.techtimes.com/articles/314536/20260219/best-data-broker-removal-services-2026-practical-guide.htm), [CyberNews Incogni review](https://cybernews.com/privacy-tools/incogni-review/), [AllAboutCookies DeleteMe vs Privacy Bee](https://allaboutcookies.org/deleteme-vs-privacy-bee)

### Key Findings for Recommendation

**Incogni is the strongest recommendation for Tier 1 non-technical users** in 2026. Its independent Deloitte audit (2025) verifies that deletion requests are sent, tracked, and renewed as described — this is the only service with third-party verification of its process. PCMag Editors' Choice 2025. In independent testing, Incogni completed 326 removal requests in one subscription cycle, estimating 244+ hours saved. 10-month cybernews.com testing: successfully removed data from 40+ data broker sites. ([Incogni review, CyberNews](https://cybernews.com/privacy-tools/incogni-review/), [TechRadar](https://www.techradar.com/reviews/incogni))

**DeleteMe gap disclosure**: The existing implementation guide recommends DeleteMe as covering "750+ brokers" — this language comes from DeleteMe's own marketing. Independent analysis finds the standard plan actively processes ~100 listing-based brokers, with the remaining 650+ being "monitored" rather than actively removed. This is a meaningful distinction for readers relying on this number. ([OneRep's DeleteMe review](https://onerep.com/blog/deleteme-review))

**Privacy Bee caveat**: Privacy Bee claims 885 brokers but the 60-day response window before follow-up means some brokers remain live for weeks. High marks for dedicated support. Stronger for commercial database removal than listing sites.

**EasyOptOuts**: Still a good budget option but does not include Deloitte-style verification. Appropriate for Tier 1 users who have already done the manual opt-outs in Step 0.2 and want automated maintenance at lowest cost.

**The California DROP advantage**: For California residents, submitting through DROP (privacy.ca.gov) before subscribing to a paid service provides significant free baseline coverage — all registered California data brokers must comply. The DROP does not cover law enforcement data products.

---

## V. Gap Analysis: Existing Documents

### A. Gaps in `threat-model.md`

**Gap 1: Venntel breach not adequately flagged (Section II.B)**
The existing entry notes the Gravy Analytics breach but does not note the 17-terabyte scale and the specific compromise of Amazon S3 buckets. The forensic detail matters because it illustrates that law enforcement surveillance databases are themselves high-value attack targets — the breach exposed location data for an estimated billion devices.

**Gap 2: ICE ad tech MAID RFI not yet in threat model**
The January 2026 ICE RFI for ad tech/MAID data (Section II.C of existing threat model partially covers this) is the most significant emerging procurement vector and should be elevated. It represents a formal, documented attempt to purchase location data tied to advertising identifiers — a category not currently covered by *Carpenter* protections and not reachable by data broker opt-outs.

**Gap 3: Montana SB 282 not mentioned**
The existing threat model does not note that Montana has closed the warrant loophole for state law enforcement, which is relevant context for readers in Montana and useful as a legislative model discussion.

**Gap 4: National Public Data breach (2024) not mentioned**
The breach of 2.9 billion records, subsequent bankruptcy, and near-zero consumer restitution ($46,000 fine vs. 2.9 billion affected records) illustrates that data brokers can absorb catastrophic breaches with minimal accountability. This is relevant to the threat model's discussion of the commercial data ecosystem's risks.

---

### B. Gaps in `implementation-guide.md Part 0`

**Gap 1: California DROP platform not mentioned (Step 0.1)**
California residents can now submit a single deletion request through DROP (privacy.ca.gov) that reaches all registered data brokers simultaneously. This should be the first step for California residents before the individual broker opt-outs in Step 0.2. The DROP was not live when the implementation guide was written.

**Gap 2: DeleteMe coverage claim should be corrected (Step 0.3, line 129)**
The guide states DeleteMe "Covers 750+ brokers" — this is DeleteMe's marketing figure. Active removal is ~100 listing-based brokers. The distinction between "covered" (monitored) and "actively removed" should be noted.

**Gap 3: Incogni not mentioned (Step 0.3)**
Incogni (Surfshark's data removal product) is now the strongest independently-verified automated removal service available, with Deloitte audit backing and PCMag Editors' Choice. At $96/year it is cheaper than DeleteMe's $130/year. For non-technical Tier 1 readers, Incogni should be the first-listed recommendation.

**Gap 4: Global Privacy Control (GPC) signal not mentioned**
Twelve states now legally require businesses to honor the GPC browser signal as a valid opt-out of data sale. Adding GPC to Firefox or Chrome (via browser extension) provides always-on, automatic opt-out signaling across sites. This is a five-minute step applicable to all tiers.

**Gap 5: Babel Street has no consumer opt-out**
The existing guide mentions Venntel but not Babel Street. Babel Street's Locate X product is being used to track protesters and immigration enforcement targets and has no consumer opt-out. This gap in the opt-out framework should be explicitly named so readers understand its limits.

---

## VI. Proposed Specific Edits

### Edit 1: threat-model.md — Expand Venntel Entry (around line 152-156)

**Current text** (lines 152-156):
```
**Venntel (owned by Gravy Analytics)**
- ICE Enforcement and Removal Operations used Venntel to "access/gain information to accurately identify digital devices"
- Collects location data harvested from smartphone apps (through the ad SDK ecosystem) — this is commercial location data derived from apps you install
- FTC alleged in 2024 that Venntel sold sensitive consumer location data without proper consent
- Note: Gravy Analytics itself was breached in early 2025
```

**Proposed replacement**:
```
**Venntel (owned by Gravy Analytics)**
- ICE Enforcement and Removal Operations used Venntel to "access/gain information to accurately identify digital devices"
- Collected location data from ~17 billion daily signals across ~1 billion mobile devices via advertising SDKs — data derived from apps you install
- FBI contract: up to $27 million for Babel Street's Locate X product (social media OSINT aggregation; no consumer opt-out exists)
- FTC finalized order (January 2025) prohibiting Gravy Analytics and Venntel from selling sensitive consumer location data; required deletion of historical location databases
- January 2025: Gravy Analytics suffered a 17-terabyte breach — hackers gained root access and control over Amazon S3 buckets containing location data for an estimated billion devices. Law enforcement's commercial surveillance source was itself a major breach target.
- No consumer opt-out available for Venntel data. The FTC order provides the only restriction, and it does not retroactively restrict already-sold government access.
```

---

### Edit 2: threat-model.md — Add MAID/Ad Tech Subsection to Section II.C

**Add after line 184** (after "Practical implication" paragraph in Ad Tech Location Data section):

```
**January 2026 escalation**: ICE issued a formal Request for Information asking ad tech companies to demonstrate capabilities for supplying MAID-linked location data for investigative use. The RFI did not reference warrants, court orders, or judicial authorization. ICE's legal theory: MAID-linked data is not covered by *Carpenter v. United States* (2018) because it is tied to an advertising identifier rather than a phone number — a distinction the privacy and legal community considers a technicality, given the MAID enrichment industry's ability to cross-reference these identifiers with personal identities within seconds. This procurement vector is not reachable by data broker opt-outs; it requires platform-level countermeasures (Part 1-3 of the implementation guide).

Sources: [The Register](https://www.theregister.com/2026/01/27/ice_data_advertising_tech_firms/), [Biometric Update](https://www.biometricupdate.com/202602/ice-seeks-industry-input-on-ad-tech-location-data-for-investigative-use), [ACLU](https://www.aclu.org/news/privacy-technology/dhs-is-circumventing-constitution-by-buying-data-it-would-normally-need-a-warrant-to-access)
```

---

### Edit 3: threat-model.md — Add Montana SB 282 and National Public Data to Section II.A (Legal Framework)

**Add after line 137** (after the DHS Inspector General paragraph):

```
**State law exception — Montana SB 282 (effective October 1, 2025)**: Montana became the first U.S. state to require a warrant before state or local law enforcement can purchase geolocation data, biometric information, financial transaction records, or other "sensitive data" from commercial brokers. This is significant as a legislative model but does not constrain federal agencies including ICE and DHS. ([EFF](https://www.eff.org/deeplinks/2025/05/montana-becomes-first-state-close-law-enforcement-data-broker-loophole))

**National Public Data breach (2024-2025)**: Jerico Pictures, Inc. (doing business as National Public Data) suffered a breach exposing 2.9 billion records — full names, Social Security numbers, addresses, and dates of birth for virtually every American adult plus records from Canada and the UK. The company filed for bankruptcy in October 2024. The California Privacy Protection Agency fined the company $46,000 — $0.000016 per affected record. Class action plaintiffs received nothing due to insolvency. This illustrates the accountability gap in the data broker industry: catastrophic breaches produce near-zero consequences. ([Wikipedia — NPD breach](https://en.wikipedia.org/wiki/2024_National_Public_Data_breach))
```

---

### Edit 4: implementation-guide.md — Add California DROP to Step 0.1

**Add after line 59** (after the DAA opt-out section, before the Step 0.2 heading):

```
**California DELETE Act — DROP Platform (California residents only)**
If you are a California resident, this is now the highest-priority action in Part 0. The Delete Request and Opt-Out Platform (DROP) at privacy.ca.gov allows you to submit a single deletion request that cascades to all registered California data brokers simultaneously. Brokers are legally required to retrieve and process these requests within 45 days on an ongoing basis — meaning re-addition from public records triggers automatic re-deletion.

- URL: https://privacy.ca.gov/drop/
- Process: Create an account, verify your California residency, submit one request. The system handles all registered brokers.
- Limitation: Does not cover law enforcement data products (Accurint, CLEAR) or unregistered brokers. After DROP submission, still complete Steps 0.2-0.3 for brokers outside California's jurisdiction.
- Time to effect: Up to 45 days for initial processing; ongoing automatic maintenance after that.
```

---

### Edit 5: implementation-guide.md — Correct DeleteMe Coverage Claim and Add Incogni (Step 0.3, around lines 128-131)

**Current text** (lines 127-131):
```
**EasyOptOuts** (~$20/year): Automated opt-outs with re-submission. Covers major brokers. Acceptable for Tier 1 users who want ongoing protection without manual quarterly re-submission.

**DeleteMe** (~$130/year): Covers 750+ brokers with quarterly re-submission and a confirmation report. This is the right trade for Tier 2 users who want thorough ongoing coverage. The cost is less than the time value of quarterly manual submissions.
```

**Proposed replacement**:
```
**Incogni** (~$96/year, $7.99/month via Surfshark): The strongest independently-verified automated removal service as of 2026. Covers 420+ brokers with 60-day re-submission cycles for public brokers and 90-day for commercial databases. Its processes were verified by a Deloitte independent assurance assessment in 2025 — the only service with third-party verification. PCMag Editors' Choice. For non-technical Tier 1 users who want ongoing protection without quarterly manual resubmissions, this is the recommended first choice. ([incogni.com](https://incogni.com/))

**EasyOptOuts** (~$20/year): Automated opt-outs with re-submission. Covers major people-search brokers. Acceptable for Tier 1 users who have completed the manual opt-outs in Step 0.2 and want automated maintenance at lowest cost.

**DeleteMe** (~$130/year): Uses human-led removals for ~100 listing-based brokers with before/after screenshot documentation and quarterly reports. Marketed as covering "750+ brokers" but active removal is ~100; the remainder are monitored but not actively processed. Best for Tier 2 users who want documented evidence of removal for specific high-priority brokers.

**Privacy Bee** (~$96/year): Broad coverage including commercial (non-listing) databases. 60-day response window before follow-up. Stronger for commercial database removal than listing sites.
```

---

### Edit 6: implementation-guide.md — Add Global Privacy Control Step

**Add after line 59** (in Step 0.1, as a new bullet before or after the DAA opt-out):

```
**Global Privacy Control (GPC) browser signal** — automatic, ongoing opt-out across compliant sites
Twelve states (including California, Colorado, Connecticut, Delaware, Maryland, Minnesota, Montana, Nebraska, New Hampshire, New Jersey, Oregon, Texas) now legally require businesses to honor the GPC signal as a valid opt-out from data sale and sharing. GPC is a browser header that signals your opt-out preference automatically to every site you visit.

- Firefox: Enable in Settings > Privacy & Security > "Tell websites not to sell or share my data" (built-in as of Firefox 120+).
- Chrome: Install the [GPC extension](https://globalprivacycontrol.org/#download) from the official site.
- Brave: GPC is enabled by default.
- Process: One-time setup, automatic thereafter. No per-site action required.
- Time estimate: 2 minutes.
- Note: GPC only reaches sites that are legally obligated to honor it (those covered by the twelve state laws above) and sites that have voluntarily opted in. It does not reach data brokers who sell to law enforcement.
```

---

## VII. Confidence Notes and Evidence Gaps

**High confidence** (primary sources, government documents):
- FTC enforcement orders (Venntel, Mobilewalla): direct FTC press releases
- California DELETE Act / DROP: CPPA official announcements
- Montana SB 282: EFF analysis + legislative text
- ICE ad tech RFI: SAM.gov procurement filing + contemporaneous reporting

**Medium confidence** (service reviews, market figures):
- Automated service broker coverage counts: figures from company self-reporting + independent reviews. Independent testing by cybernews.com, TechRadar, and AllAboutCookies is the best available; no academic peer-reviewed comparisons exist.
- Market size figures ($312-342B range): vary by research firm and methodology; consistent directionally.

**Known gaps not resolved by this research**:
- Acxiom and Epsilon direct government contracts: no confirmed contracts for immigration enforcement found. The 2013 congressional inquiry is the most recent public record of data source refusal. Worth a separate targeted research pass.
- CLEAR's full data source list and how opt-outs from Accurint affect CLEAR queries: these are the same Thomson-Reuters entity. The interaction between consumer suppression in Accurint and CLEAR law enforcement product access is not publicly documented.
- Effectiveness of DROP at actually preventing law enforcement access: the platform prevents registered commercial brokers from re-acquiring data, but does not reach law enforcement data products and does not address MAID-derived data.

---

## Sources

- [FTC Final Order: Gravy Analytics / Venntel (January 2025)](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-prohibiting-gravy-analytics-venntel-selling-sensitive-location-data)
- [FTC Final Order: Mobilewalla (January 2025)](https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-finalizes-order-banning-mobilewalla-selling-sensitive-location-data)
- [California Privacy Protection Agency: Data Broker Registry](https://cppa.ca.gov/data_brokers/)
- [California DROP Platform: About DROP and the Delete Act](https://privacy.ca.gov/drop/about-drop-and-the-delete-act/)
- [EFF: Montana Becomes First State to Close the Law Enforcement Data Broker Loophole (May 2025)](https://www.eff.org/deeplinks/2025/05/montana-becomes-first-state-close-law-enforcement-data-broker-loophole)
- [The Register: ICE Ad Tech RFI (January 27, 2026)](https://www.theregister.com/2026/01/27/ice_data_advertising_tech_firms/)
- [Biometric Update: ICE Seeks Industry Input on Ad Tech Location Data](https://www.biometricupdate.com/202602/ice-seeks-industry-input-on-ad-tech-location-data-for-investigative-use)
- [TechCrunch: LexisNexis Breach (May 2025)](https://techcrunch.com/2025/05/28/data-broker-giant-lexisnexis-says-breach-exposed-personal-information-of-over-364000-people/)
- [Wikipedia: 2024 National Public Data Breach](https://en.wikipedia.org/wiki/2024_National_Public_Data_breach)
- [CPPA: Enforcement Action Against National Public Data (February 2025)](https://cppa.ca.gov/announcements/2025/20250220.html)
- [CPPA: New Enforcement Actions Against Data Brokers (January 2026)](https://cppa.ca.gov/announcements/2026/20260108.html)
- [CalPrivacy: Delete Act Regulations Approved (November 2025)](https://cppa.ca.gov/announcements/2025/20251113.html)
- [ScanComply: California SB 361 AI Disclosure Rules (effective January 2026)](https://scancomply.com/blog/california-sb-361-data-broker-law-2026)
- [IAPP: Largest CCPA Fine to Date](https://iapp.org/news/a/california-s-attorney-general-issues-largest-ccpa-fine-to-date)
- [WilmerHale: CCPA Enforcement Summary (July 2025)](https://www.wilmerhale.com/en/insights/blogs/wilmerhale-privacy-and-cybersecurity-law/20250708-california-ag-issues-largest-monetary-penalty-in-most-recent-ccpa-enforcement-action)
- [CyberNews: Incogni Review (10-month test)](https://cybernews.com/privacy-tools/incogni-review/)
- [TechTimes: Best Data Broker Removal Services 2026](https://www.techtimes.com/articles/314536/20260219/best-data-broker-removal-services-2026-practical-guide.htm)
- [AllAboutCookies: DeleteMe vs Privacy Bee 2026](https://allaboutcookies.org/deleteme-vs-privacy-bee)
- [OneRep: DeleteMe Review 2026](https://onerep.com/blog/deleteme-review)
- [TechRadar: Incogni Review](https://www.techradar.com/reviews/incogni)
- [ComplianceHub: The Delete Act 2026](https://compliancehub.wiki/the-delete-act-your-2026-right-to-disappear-from-data-brokers/)
- [ManageEngine: US State Data Privacy Laws 2025-2026](https://insights.manageengine.com/privacy-compliance/us-state-data-privacy-laws/)
- [ACLU: DHS Circumventing Constitution via Data Broker Purchases](https://www.aclu.org/news/privacy-technology/dhs-is-circumventing-constitution-by-buying-data-it-would-normally-need-a-warrant-to-access)
- [Amnesty International: Babel Street Surveillance Threats (August 2025)](https://www.amnesty.org/en/latest/news/2025/08/usa-global-tech-made-by-palantir-and-babel-street-pose-surveillance-threats-to-pro-palestine-student-protestors-migrants/)
- [EPIC: FTC Takes Action Against Data Brokers](https://epic.org/ftc-takes-action-against-data-brokers-for-selling-sensitive-location-data/)
- [Acxiom US Privacy Page](https://www.acxiom.com/privacy/us/)
- [Big-Ass Data Broker Opt-Out List (GitHub, updated March 28, 2026)](https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List)
