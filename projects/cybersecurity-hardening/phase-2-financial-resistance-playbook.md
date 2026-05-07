---
title: "Financial Resistance Playbook: Legal Financial Privacy for Advocacy Organizations, Mutual Aid Networks, and High-Risk Individuals"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Phase 2
version: 1.0
depends_on:
  - threat-model.md
  - palantir-threat-model.md
  - PHASE_2_SEQUENCING_STRATEGY.md
confidence: high — grounded in confirmed IRS LCA Palantir contract documentation, FinCEN SAR reporting October 2025 guidance, Wall Street Journal and IRS targeting reporting (October 2025), Chainalysis 2026 crypto sanctions report, Form 1099-DA broker reporting requirements (2025 tax year), FinCEN whistleblower program emergency deadline, and debanking regulatory actions
audience: Advocacy organizations, mutual aid networks, labor unions under IRS scrutiny, individual activists with financial surveillance concerns, nonprofit attorneys, community fund managers
word_count: ~3,500
legal_notice: This playbook addresses legal financial privacy practices only. It does not address illegal sanctions evasion, money laundering, tax evasion, or financial structuring (deliberately breaking transactions to stay below reporting thresholds). Those are federal crimes. The threat this playbook addresses is the IRS LCA platform's documented use for politically targeted financial surveillance of advocacy organizations and individuals, and the financial data pipeline that feeds Palantir's social-graph mapping.
---

# Financial Resistance Playbook

**Legal notice — read first**: This guide addresses lawful financial privacy practices for organizations and individuals who face documented government financial surveillance. It does not provide guidance on illegal activities including money laundering, tax evasion, sanctions violations, or financial structuring. The threats this guide addresses are: (1) the IRS LCA Palantir platform being used for politically targeted investigation of left-leaning nonprofits and donors; (2) FinCEN SAR reporting creating financial records accessible to government investigation; (3) Palantir's financial data pipeline connecting an advocacy organization's financial activity to its immigration and law enforcement profile; and (4) cryptocurrency KYC records at regulated exchanges being accessible to IRS LCA. All countermeasures described here are legal and standard practice in the nonprofit and financial privacy communities.

**Bottom line up front**: The single most important financial privacy action for any advocacy organization or individual in 2026 is documentation — not concealment. An IRS investigation cannot be defeated by hiding money; it can be defended against with clear documentation that all financial activity is consistent with the organization's stated mission. The countermeasures in this guide are designed to reduce the attack surface of an IRS or FinCEN investigation, not to hide activity that would be illegal if discovered.

---

## Section 1: The Financial Surveillance Stack — What Is Being Used Against You

### 1.1 IRS LCA — The Palantir Financial Investigation Platform

**What it is**: The IRS Criminal Investigation Division holds a $130M+ contract with Palantir for the LCA (Lead Central Analyst) platform. LCA is built on Palantir Gotham and integrates IRS tax return data, financial institution records, FinCEN SAR and CTR data, cryptocurrency exchange compliance data, and external commercial financial databases into a unified investigation platform.

**The social graph capability**: LCA maps social networks among investigation targets using financial transaction patterns. Regular transactions between your organization's accounts and any account connected to someone under investigation draws your organization into the social graph of that investigation. This is not a marginal risk: it is the explicit design of the platform, documented in Palantir's IRS contract language.

**The 2025 escalation**: In October 2025, the Wall Street Journal reported that the Trump administration planned changes at the IRS that would enable politically motivated investigations of nonprofit organizations and their donors — specifically targeting "left-leaning groups." The plans include installing political allies at IRS Criminal Investigation, weakening the involvement of IRS lawyers in criminal cases to enable faster politically motivated referrals, and compiling lists of Democratic donors and left-leaning nonprofits for investigation. A September 25, 2025 National Security Presidential Memorandum gave federal agencies and the IRS greater authority to investigate nonprofits alleged to be engaged in "political violence or domestic terrorism" — a category whose boundaries have been applied broadly.

**What is actually at risk**: Any advocacy organization that has financial transactions with organizations under IRS investigation; any donor whose giving history is in the IRS LCA social graph; and any mutual aid network or labor fund whose financial activity is characterized as structuring, money laundering, or material support.

**Countermeasure**: Section 2 — organizational financial hygiene; Section 3 — donor privacy architecture.

### 1.2 FinCEN SAR Reporting — The Bank Suspicious Activity Pipeline

**What it does**: Financial institutions are required to file Suspicious Activity Reports (SARs) with FinCEN when they detect patterns of activity that suggest money laundering, structuring, tax evasion, or other financial crimes. SARs are filed without the account holder's knowledge and are not accessible to the subject of the report. They flow to a FinCEN database that law enforcement — including the IRS, FBI, and DHS — can query.

**The mutual aid and advocacy risk**: Banks have filed SARs against mutual aid networks and advocacy organizations when their transaction patterns triggered automated risk-scoring systems. Common triggers: large numbers of small transactions from multiple senders (matching mutual aid distribution patterns); regular cash deposits (common in organizations that collect donations at community events); transactions to or from individuals in high-risk categories (e.g., immigration legal services organizations with clients who are undocumented); and any pattern that matches money-laundering typologies in bank compliance software, even when the actual activity is entirely lawful.

**2025 guidance update**: FinCEN issued new SAR guidance in October 2025 (SAR-FAQs-October-2025.pdf) intended to reduce SAR filing burdens for financial institutions by clarifying that SARs should be filed based on actual suspicious activity, not on automated risk-scoring alone. This does not eliminate the SAR risk — it gives organizations grounds to push back on account closures driven by over-filing.

**Countermeasure**: Section 2.3 — transaction pattern documentation; Section 4 — account architecture.

### 1.3 Cryptocurrency Exchange KYC Data in the IRS Pipeline

**The documented linkage**: Starting with the 2025 tax year, every custodial cryptocurrency exchange is required to issue Form 1099-DA reporting gross proceeds from digital asset sales. Major U.S. exchanges — Coinbase, Kraken, Gemini — have sent this data to the IRS since 2025. The IRS LCA platform has documented access to exchange compliance data (Coinbase is specifically mentioned in contract language). This means: any cryptocurrency transaction on a regulated U.S. exchange with KYC (Know Your Customer) verification creates a permanent IRS-accessible record linking the transaction to the account holder's SSN.

**What is not in the IRS pipeline**: Monero (XMR) transactions on-chain, between self-custody wallets that have never touched a regulated KYC exchange. Monero uses ring signatures, stealth addresses, and RingCT to obscure sender, receiver, and transaction amount on its blockchain. The IRS has publicly acknowledged difficulty tracing Monero and offered $625,000 for a Monero-tracing solution. Bitcoin does not provide this protection — Bitcoin's blockchain is public, and IRS-contracted Chainalysis can trace Bitcoin transactions with significant accuracy.

**The critical caveat**: Monero's on-chain privacy is real but the entry and exit points are the vulnerability. Monero that has ever touched a regulated exchange with your KYC data on record creates a link between your SSN and a Monero wallet address in the IRS LCA database. Monero's privacy is meaningful only if the funds originated from a non-KYC source (peer-to-peer exchange, in-person swap, mining) and have never touched a regulated exchange.

**Countermeasure**: Section 5 — cryptocurrency privacy architecture.

### 1.4 Palantir Foundry Financial-to-Immigration Data Bridge

**What it does**: Palantir's architecture at DHS and IRS enables cross-agency queries that connect financial data to immigration records. The DOGE-era executive directive to eliminate "information silos" across agencies is being implemented through Palantir's "mega API" architecture. The practical result: an ELITE address confidence score (immigration) can incorporate financial data from LCA (IRS), and an IRS LCA investigation of an advocacy organization can incorporate DHS immigration enforcement data about the organization's clients.

**For organizations that serve undocumented clients or mixed-status families**: Financial records that identify your organization as providing services to undocumented individuals can become part of ICE's ImmigrationOS social graph. This is not an abstract possibility — it is the designed function of Palantir's cross-agency data architecture.

**Countermeasure**: Section 2.2 — client financial record separation; operational security between financial records and client case records.

### 1.5 Debanking Risk — Account Closure as a Chilling Effect Tool

**The documented pattern**: Financial institutions have closed accounts belonging to advocacy organizations, civil rights groups, and political activists based on automated risk-scoring and compliance pressure. The Biden administration's debanking of crypto businesses documented in a December 2025 House report shows the broad scope of this power; the pattern applies to advocacy organizations as readily as to financial services firms. A 2026 regulatory shift (OCC removal of "reputation risk" from supervisory guidance) reduced some debanking pressure for crypto firms but did not address debanking of advocacy organizations.

**The risk mechanism**: An advocacy organization that becomes the subject of an IRS investigation or that has transactions that trigger SAR filing is at risk of account closure by its bank. Account closure at the primary institution is operationally devastating for an organization that processes payroll, pays vendors, and receives donations. The countermeasure is financial institution diversification.

**Countermeasure**: Section 4 — account architecture diversification.

---

## Section 2: Organizational Financial Hygiene

### 2.1 Documentation-First Approach

The IRS LCA platform can be used to investigate any organization. The defense against a politically motivated investigation is not financial concealment — it is clear, contemporaneous documentation of the lawful purpose of all financial activity. For every transaction category that could be mischaracterized:

- **Maintain a transaction register** explaining the purpose of each non-routine transaction at the time it occurs (not retroactively)
- **For cash donations**: receipt book with donor name and amount (for donors who consent) or anonymous donation log with event/collection context noted
- **For unusual transaction patterns**: board minutes or officer notes contemporaneously explaining the business purpose (e.g., "Q3 mutual aid distribution: $50,000 disbursed to 200 recipients for food and housing assistance per organization's 501(c)(3) charitable purpose")
- **For foreign transactions**: document the payee's legitimate identity and the lawful purpose before the transaction, not after

**Why contemporaneous documentation matters**: The LCA platform's social graph analysis is based on patterns, not individual transactions. An investigator looking at your organization's financial records cannot infer purpose from patterns alone. Contemporaneous documentation provides the alternative interpretation: this pattern is what mutual aid distribution looks like, not what money laundering looks like.

### 2.2 Separating Client Records from Financial Records

For organizations that serve immigration clients, domestic violence survivors, or other populations whose identities require protection: financial records (invoices, payments, grants) should never contain client identifying information. Use client case numbers (not names) in financial records. Accounts payable and receivable should reference service categories (e.g., "legal representation — case # 2026-0047") rather than client identity.

The Palantir financial-immigration data bridge means that a financial record containing a client's name can become an IRS-accessible record that feeds into the immigration system's profile of that individual. This is not hypothetical — it is the designed function of cross-agency data integration.

### 2.3 Transaction Pattern Awareness

Automated bank compliance software triggers SAR filing based on patterns. Patterns most likely to trigger SAR review for advocacy organizations:

- **Structuring-adjacent patterns**: Multiple cash deposits just below $10,000 within short time windows, even when done for entirely legitimate reasons (separate events, separate collection points). Document the source and event for each cash deposit separately in your records.
- **Multiple small inflows**: Mutual aid networks that receive many small PayPal, Venmo, or Zelle contributions from many individuals may trigger SAR patterns. Platform-based mutual aid fundraising should use nonprofit-oriented tools (PayPal Giving Fund, Stripe Climate, GoFundMe Charity) that have cleaner compliance profiles than peer-to-peer payment apps.
- **Cross-border transactions**: Any transaction with a foreign entity triggers enhanced compliance review. For organizations with international connections, document the relationship and purpose before the transaction.

---

## Section 3: Donor Privacy Architecture

### 3.1 Fiscal Sponsorship for Donor Privacy

Fiscal sponsorship is a legal and common arrangement in the nonprofit sector: a donor gives to a 501(c)(3) fiscal sponsor organization, which receives and disburses funds to the sponsored project or organization. The donor's gift is to the fiscal sponsor, not directly to the advocacy organization. This reduces the number of donor records directly associated with your organization.

**Established fiscal sponsors**: Tides Foundation (tides.org), Amalgamated Charitable Foundation (amalgamatedcharitable.org), and Community Partners (communitypartners.org) provide fiscal sponsorship for advocacy projects. Using a fiscal sponsor insulates small donor records from direct IRS scrutiny of your organization, while preserving the donor's tax deductibility.

**Note**: Fiscal sponsorship is not concealment. The fiscal sponsor maintains donor records and reports to the IRS as required. The effect is that your organization's donors are one step removed from your organization's financial profile in the IRS LCA social graph.

### 3.2 Recurring Small Donations — Platform Selection

For organizations that receive recurring small donations, platform selection affects SAR exposure:

| Platform | SAR Risk | Privacy Notes |
|---|---|---|
| PayPal Giving Fund | Lower | Specifically designed for nonprofits; PayPal's compliance team recognizes charitable patterns |
| Stripe (with nonprofit account) | Lower | Stripe has nonprofit-specific compliance review policies |
| GoFundMe Charity | Lower | Clear charitable purpose context |
| Personal Venmo/Cash App | Higher | Peer-to-peer platforms flag charitable-pattern receipts as potentially suspicious |
| Cryptocurrency (Bitcoin) | Higher | Public blockchain; IRS Chainalysis can trace; exchange KYC creates SSN link |
| Cryptocurrency (Monero, non-KYC) | Lower | On-chain privacy; see Section 5 for required conditions |

### 3.3 Large Donor Records and the IRS Social Graph

For individual donors who are giving significant amounts to organizations under IRS scrutiny: the IRS LCA platform maps relationships across financial records. A donor who has given to multiple organizations that are simultaneously under investigation becomes a node in the LCA social graph. Document the legitimate philanthropic purpose of each donation (mission alignment, relationship with the grantee) in contemporaneous records.

---

## Section 4: Account Architecture and Debanking Mitigation

### 4.1 Primary Account + Backup Institution

Every advocacy organization should maintain relationships with at least two financial institutions: a primary account at a larger institution for routine operations, and a backup account at a community credit union or mission-aligned institution for continuity if the primary account is closed.

Community credit unions have lower automated risk-scoring infrastructure than major banks and more relationship-based account management. De-banking risk (account closure) is substantially lower at community credit unions. Recommended: open a community credit union account before you need it — account opening at a credit union takes 2–3 weeks and requires an established organizational identity.

**Mission-aligned institutions**: Amalgamated Bank (amalgamatedbank.com), National Cooperative Bank (ncb.coop), and Community Reinvestment Act-focused credit unions serve advocacy organizations and have compliance frameworks designed for nonprofit financial patterns.

### 4.2 Operational and Reserve Account Separation

Maintain separate accounts for:
- **Operating funds**: Payroll, vendor payments, monthly expenses
- **Program funds**: Restricted grants, mutual aid distributions, specific program expenses
- **Reserve/savings**: Long-term reserves, legal defense fund

Account separation does two things: it reduces the blast radius of a debanking event (closure of the operating account does not immediately affect reserve funds), and it creates clear financial documentation (grant funds are visible as flowing through program accounts, not commingled with operating expenses).

### 4.3 For Individual Activists: Community Credit Union Over Large Banks

Large bank automated risk-scoring is more aggressive than community credit union compliance review. Individuals who have financial activity patterns associated with advocacy work (large numbers of small transfers, nonprofit deposits, unusual geographic patterns) face higher debanking risk at large banks than at community credit unions. Establish a community credit union relationship as your primary account.

---

## Section 5: Cryptocurrency Privacy Architecture

### 5.1 The Core Principle: Bitcoin Is Not Private

Bitcoin's public blockchain means every transaction is permanently visible to anyone, including IRS-contracted Chainalysis. If you have ever used a regulated Bitcoin exchange (Coinbase, Kraken, Gemini), your wallet address is linked to your SSN in the IRS LCA database. "Mixing" services for Bitcoin have been shut down and their operators prosecuted (e.g., Tornado Cash, Bitcoin Fog). Bitcoin is not appropriate for financial privacy in an IRS-scrutiny context.

Zcash (ZEC) offers optional privacy via shielded transactions, but most Zcash transactions are "transparent" (unshielded), and exchange delistings have reduced Zcash's liquidity significantly. As of 2026, at least 10 countries impose bans or strict exchange restrictions on Monero and Zcash.

### 5.2 Monero — The Only Practical On-Chain Privacy Tool (With Conditions)

Monero (XMR) provides genuine transaction privacy through ring signatures (obscures sender), stealth addresses (obscures receiver), and RingCT (hides transaction amount). The IRS has publicly acknowledged significant difficulty tracing Monero transactions. The Chainalysis 2026 crypto report confirms that Monero remains the hardest privacy coin to trace.

**Required conditions for Monero's privacy to be meaningful**:

1. **Never touch a regulated KYC exchange with the privacy wallet**. If your Monero funds originated on Coinbase and you moved them to a self-custody wallet, the Coinbase record links your SSN to the wallet address. KYC-origin Monero is traceable at the entry point even if on-chain transactions are private.

2. **Non-KYC acquisition only**: Options for non-KYC Monero acquisition — in-person peer-to-peer swap with a known party (no exchange record); Bisq (bisq.network, decentralized peer-to-peer exchange with no KYC) or Haveno (haveno.exchange, Bisq successor); mining on commodity hardware; or LocalMonero equivalents available in your jurisdiction. The entry point is the most important privacy control.

3. **Self-custody wallet required**: Use Feather Wallet (featherwallet.org) for desktop or Cake Wallet (cakewallet.com) for mobile — both are open-source self-custody Monero wallets with no KYC requirement. Never leave Monero on an exchange.

4. **Legal use only**: Monero is legal to own and transact in the United States as of May 2026, classified as property by the IRS. Lawful advocacy organizations accepting Monero donations for privacy reasons are not violating any law. Monero used for structuring (deliberately breaking transactions to avoid reporting thresholds) or for prohibited conduct remains illegal regardless of the coin used.

### 5.3 Cryptocurrency Donations to Advocacy Organizations

For organizations that accept cryptocurrency donations for donor privacy:
- Publish a Monero wallet address (not Bitcoin) for privacy-sensitive donations
- Disclose to donors that all cryptocurrency donations are still reportable as income to the IRS (Form 1099-DA from exchanges, or self-reporting for non-exchange receipts)
- Do not use the organizational Monero wallet for any transaction that has ever touched a KYC exchange on either end
- Keep a Monero donation log for internal records (date, amount in XMR and USD equivalent at receipt) for IRS Form 990 purposes

---

## Section 6: Cash — The Most Accessible Financial Privacy Tool

### 6.1 Cash for Operational Expenses

Cash creates no electronic record accessible to the IRS LCA platform, FinCEN SAR system, or Palantir's financial data pipeline. For organizations with concerns about financial surveillance: maximize cash use for operational expenses where practical (event supplies, printed materials, small vendor payments).

**The legal limit**: Cash transactions below $10,000 are not subject to mandatory Currency Transaction Reports (CTRs) from financial institutions. Transactions above $10,000 in cash require CTR filing. There is no legal requirement on the payor or recipient for sub-$10,000 cash transactions beyond normal record-keeping.

**The illegal conduct to avoid**: Structuring — deliberately breaking cash transactions into amounts below $10,000 to avoid CTR filing — is a federal crime under 31 U.S.C. § 5324. The guidance here is to use cash for legitimate operational expenses that naturally fall below reporting thresholds, not to structure transactions to stay below them.

### 6.2 Cash for Individual Activists

For individual activists with financial surveillance concerns: cash for everyday expenses (groceries, transit, local purchases) leaves no payment card record in commercial data broker pipelines that feed Palantir's financial databases. The most straightforward financial privacy action available to anyone is using cash instead of payment cards for routine purchases.

**Prepaid cards as cash equivalent**: Prepaid debit cards purchased with cash at retail stores (Walgreens, CVS, 7-Eleven) allow electronic payments without a bank account or payment card in your name. Most prepaid cards do not require ID verification for loads under $500. This provides payment card functionality without creating bank account records.

### 6.3 Money Orders for Rent and Recurring Payments

For individuals who wish to pay rent or recurring expenses without linking a bank account to their address (which flows into ELITE address confidence scoring): USPS money orders and retail-outlet money orders (Western Union, MoneyGram, available at grocery stores and pharmacies) allow payment with a documented receipt without requiring a bank account in your name. Purchase money orders with cash.

---

## Section 7: Implementation Checklists

### Checklist A: New Organization Setup — Financial Privacy Baseline

- [ ] Open a primary operating account at a community credit union or mission-aligned bank
- [ ] Open a secondary account at a different institution for reserve/program funds (debanking protection)
- [ ] Establish a transaction register or document-purpose system for all non-routine transactions
- [ ] Identify a fiscal sponsor for donor privacy if your organization will receive individual donations from people with surveillance concerns
- [ ] Review all payment platform choices for SAR risk (prefer PayPal Giving Fund or Stripe nonprofit over personal Venmo/Cash App)
- [ ] Consult with a nonprofit attorney about your 501(c)(3) documentation and mission consistency

### Checklist B: Existing Organization — Quarterly Financial Security Review

- [ ] Has any transaction this quarter been with an entity under IRS investigation? Document the lawful purpose of the relationship.
- [ ] Are any transaction patterns this quarter matching structuring-adjacent patterns (multiple cash deposits near $10K threshold, unusual recipient concentration)?
- [ ] Have any accounts been flagged by the bank for compliance review? Document response.
- [ ] Are client/case records fully separated from financial records?
- [ ] Has your cryptocurrency wallet (if any) maintained clean KYC separation?
- [ ] Is your reserve account at a separate institution from your operating account?

### Checklist C: Individual Activist Baseline

- [ ] Primary account at a community credit union (not a major bank)
- [ ] Cash for daily routine purchases
- [ ] Prepaid card (cash-purchased) for online purchases requiring a payment card
- [ ] Any cryptocurrency: Monero only, non-KYC entry point, self-custody wallet
- [ ] Money orders for rent if concerned about address-linked bank account records

---

## Section 8: Legal Resources

- **National Council of Nonprofits — Financial and Legal Resources**: councilofnonprofits.org
- **Bolder Advocacy (Alliance for Justice)**: bolderadvocacy.org — nonprofit advocacy law, IRS compliance
- **Tides Foundation — Fiscal Sponsorship**: tides.org
- **FinCEN whistleblower program** (for reporting financial crimes by third parties, not organizations defending themselves): fincen.gov
- **ACLU — Financial surveillance and data broker litigation**: aclu.org
- **EFF — Financial surveillance research**: eff.org

---

## Summary: Five Principles That Matter Most

1. **Documentation is the primary defense** — contemporaneous records explaining the lawful purpose of all financial activity is more powerful than any privacy tool. An IRS investigation that finds perfectly documented, mission-consistent transactions has nowhere to go.

2. **Bitcoin is not private; Monero with non-KYC origins is** — use the right tool for the stated goal. Accepting Bitcoin donations for "privacy" provides no actual privacy.

3. **Two institutions, not one** — debanking is a real risk. Reserve account at a different institution from operating account is the minimum continuity architecture.

4. **Separate client records from financial records** — especially for organizations serving undocumented clients. The Palantir financial-immigration bridge means that a financial record can become an immigration enforcement record.

5. **Cash is still the most accessible tool** — no platform, no SAR, no ELITE feed. For individuals and small organizations with limited resources for other measures: maximize cash use for everyday expenses.

---

**Version**: 1.0
**Created**: May 7, 2026
**Next scheduled review**: July 26, 2026 (quarterly corpus review)
**Cross-references**: `threat-model.md`, `palantir-threat-model.md`, `phase-2-immigration-surveillance-evasion-playbook.md` (Section 7 on financial privacy), `PHASE_2_SEQUENCING_STRATEGY.md` (Section 3.4 on financial resistance)

---

## Sources

- [Wall Street Journal — IRS political targeting of left-leaning groups, October 2025](https://doggett.house.gov/media/press-releases/democrats-launch-inquiry-weaponization-irs)
- [Chainalysis — 2026 Crypto Sanctions Report](https://www.chainalysis.com/blog/crypto-sanctions-2026/)
- [Chainalysis — 700% surge in crypto sanctions evasion 2025](https://amlnetwork.org/sanctions-enforcement/chainalysis-report-reveals-700-surge-in-crypto-sanctions-evasion-during-2025-amid-rising-state-activity/)
- [FinCEN — SAR FAQs October 2025](https://www.fincen.gov/system/files/2025-10/SAR-FAQs-October-2025.pdf)
- [CountDeFi — Can the IRS track crypto in 2026?](https://www.countdefi.com/blog/can-the-irs-track-cryptocurrency)
- [CCN — 10 countries restricting Monero and Zcash, 2026](https://www.ccn.com/education/crypto/countries-banning-privacy-coins-monero-zcash-2026/)
- [Baltex — Is Monero legal? XMR regulations and MiCA compliance](https://baltex.io/blog/ecosystem/is-monero-legal-xmr-regulations-mica-compliance)
- [Global Legal Insights — Blockchain and Cryptocurrency Laws USA 2026](https://www.globallegalinsights.com/practice-areas/blockchain-cryptocurrency-laws-and-regulations/usa/)
- [FINScan — Regulatory Roundup January 2026: Debanking and enforcement](https://www.finscan.com/post/regulatory-roundup-january-2026-debanking-enforcement-and-the-expanding-compliance-perimeter)
- [Charity Lawyer Blog — Politicization of the nonprofit sector, December 2025](https://charitylawyerblog.com/2025/12/01/the-rising-politicization-of-the-nonprofit-sector/)
- [TNPA — 2025 Nonprofit Policy Moments and 2026 Look Ahead](https://tnpa.org/2025-nonprofit-policy-moments-and-a-2026-look-ahead/)
- [EFF — ICE surveillance shopping spree (IRS LCA contract context)](https://www.eff.org/deeplinks/2026/01/ice-going-surveillance-shopping-spree)
- [PHASE_2_SEQUENCING_STRATEGY.md — Section 2.4 Financial Transaction Privacy](./PHASE_2_SEQUENCING_STRATEGY.md)
