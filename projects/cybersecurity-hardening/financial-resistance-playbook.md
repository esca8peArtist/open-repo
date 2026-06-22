---
title: "Financial Resistance and Privacy Playbook: Legal Financial Privacy for Advocacy Organizations and Activists"
project: cybersecurity-hardening
created: 2026-05-06
status: scenario-specific-guide
phase: Phase 2
session: 844
depends_on:
  - threat-model.md
  - opsec-playbook.md
  - palantir-threat-model.md
  - PHASE_2_SEQUENCING_STRATEGY.md
confidence: high — grounded in documented IRS LCA platform capabilities (The Intercept, TechCrunch, Tax Notes), confirmed IRS-DHS data-sharing agreement and court rulings (PBS, Federal News Network, FindLaw), FinCEN regulatory framework (FinCEN.gov), and Monero tracing difficulty (IRS $1.25M Chainalysis bounty, Decrypt reporting); Monero exchange-vulnerability claims grounded in IRS LCA contract data-source documentation
audience: Advocacy organizations under political scrutiny, mutual aid networks, individual donors to causes under surveillance, activists with reason to believe they are under IRS or FinCEN investigation, nonprofit financial managers, legal service organizations
---

# Financial Resistance and Privacy Playbook

**This playbook addresses LEGAL financial privacy practices. It does NOT address illegal sanctions evasion, money laundering, or structuring — those are federal crimes and are not the concern of this corpus.**

---

**Executive Summary for Advocacy Organizations and Mutual Aid Networks**: The financial surveillance infrastructure targeting advocacy organizations in 2026 is documented and operational. The IRS Criminal Investigation division's Lead and Case Analytics (LCA) platform, a $130M+ Palantir Foundry deployment, maps social networks across individual tax records, financial transactions, bank statements, FinCEN data, and cryptocurrency wallets in a single queryable system. Under the Trump administration, IRS Criminal Investigation has explicitly pivoted toward investigating "left-leaning groups." An IRS-DHS data-sharing agreement — which a federal judge found violated the Internal Revenue Code — nonetheless received appellate clearance to proceed. DOGE personnel have obtained access to SSA and IRS data systems post-SCOTUS. None of this requires illegal behavior to create risk: legitimate advocacy organizations, mutual aid networks, and individual donors can become subjects of LCA financial surveillance simply by having financial connections to organizations or individuals under investigation.

The countermeasures in this playbook are not about hiding. They are about maintaining the financial separation, documentation discipline, and organizational hygiene that makes surveillance harder to weaponize, legal defense stronger, and chilling effects on legitimate advocacy less effective.

---

## Part 1: Understanding the Financial Surveillance Stack

### 1.1 The IRS Lead and Case Analytics (LCA) Platform

The LCA platform is the financial surveillance capability that most directly threatens advocacy organizations and their donors. It is not merely a tax compliance tool — its documented capabilities describe "massive-scale" data mining, social network mapping among investigation targets, and IP address analysis to identify suspects and establish relationships across federal databases.

**Confirmed LCA data sources** (per contract documents reviewed by The Intercept and TechCrunch):
- Individual tax forms and returns (1040, corporate filings, 990s for nonprofits)
- Affordable Care Act enrollment data
- Bank statements and financial transactions
- All FinCEN data, explicitly including Suspicious Activity Reports (SARs)
- Cryptocurrency wallet data: Bitcoin, Ethereum, Litecoin, Ripple, and "dark web data from seized servers and exchangers"
- Coinbase and other regulated exchange compliance data
- Communications metadata: calls, texts, emails
- IP address records

**The social graph threat**: LCA does not investigate isolated transactions. It maps *relationships* — building a network graph of financial connections among investigation targets. If your organization sends a check to an entity that is already under LCA investigation, or if an LCA investigation target donates to your organization, your financial accounts enter the social graph of that investigation. This is the same entity-resolution mechanism documented in `palantir-threat-model.md` applied to financial data: the system links entities together and the links are persistent.

**The political targeting concern**: IRS Criminal Investigation has reportedly shifted under Trump's direction toward investigating "left-leaning groups." Democratic members of Congress wrote to Palantir explicitly warning of a potential "surveillance nightmare" in which the LCA mega-database enables targeted investigation of political opponents. This concern is documented, not speculative: The Intercept (April 24, 2026) reported on the LCA platform's capabilities and the political context of its current deployment. [The Intercept — Palantir IRS LCA platform](https://theintercept.com/2026/04/24/palantir-irs-contract-data/), [Tax Notes — Palantir IRS contracts under scrutiny](https://www.taxnotes.com/featured-news/palantir-contracts-under-scrutiny-amid-irs-tax-data-controversy/2026/02/18/7tzns)

---

### 1.2 FinCEN and the Suspicious Activity Report (SAR) Pipeline

Financial institutions are required under the Bank Secrecy Act to file Suspicious Activity Reports (SARs) when they "know, suspect, or have reason to suspect" that a transaction meets suspicious activity criteria. The reporting threshold is $5,000 for banks ($2,000 for money services businesses). This is distinct from the Currency Transaction Report (CTR) threshold of $10,000 for cash transactions.

SARs are not probable-cause determinations. They are risk-based assessments made by compliance officers who often know little about an organization's work. Mutual aid fund transactions (large numbers of small cash disbursements), bail funds, and legal defense fund distributions can all trigger SAR filings purely based on pattern — not any underlying illegality.

**The LCA connection**: LCA explicitly ingests "all available" FinCEN data, including SARs. A SAR filed by your bank creates a record in the LCA pipeline, even if the underlying activity was entirely lawful. Organizations should know that their banking activity — particularly unusual cash patterns or large disbursements to many individuals — can generate SARs that feed directly into the IRS's political investigation infrastructure.

**October 2025 FinCEN guidance update**: FinCEN clarified in October 2025 that institutions are not required to file a SAR solely because a transaction occurs near the $10,000 CTR threshold. This was intended to reduce over-filing. However, the guidance does not prevent institutions from filing SARs based on pattern analysis of a customer relationship — meaning organizations with unusual transaction patterns relative to their account history remain at risk of SAR generation. [FinCEN SAR FAQ updates — WilmerHale analysis](https://www.wilmerhale.com/en/insights/client-alerts/20251028-fincen-clarifies-suspicious-activity-reporting-requirements)

---

### 1.3 DOGE Cross-Agency Data Sharing and the IRS-DHS Agreement

**IRS-DHS data-sharing agreement (2025–ongoing)**: In April 2025, Treasury Secretary Scott Bessent and DHS Secretary Kristi Noem signed an agreement allowing ICE to submit names and addresses of undocumented immigrants to the IRS for cross-verification against tax records. A federal judge found the IRS violated the Internal Revenue Code approximately 42,695 times by sharing taxpayer data with DHS — but a D.C. Circuit appeals court subsequently refused to block the arrangement pending final merits resolution. The data-sharing is therefore operational as of May 2026, despite documented violations of the IRC's taxpayer confidentiality protections.

**DOGE access to IRS systems**: DOGE personnel obtained access to IRS IT infrastructure concurrent with the DHS data-sharing initiative. The IRS's IT department was, per PBS News reporting, "largely taken over" by DOGE officials. This means the LCA platform's data — tax returns, financial records, FinCEN SARs — is accessible to personnel whose affiliations and data-handling protocols are not subject to normal IRS employee confidentiality requirements.

**SSA post-SCOTUS**: As documented in `PHASE_2_SEQUENCING_STRATEGY.md` Section 1.2, the Supreme Court in June 2025 cleared DOGE access to SSA data, and the Fourth Circuit in April 2026 removed remaining injunctive limits. SSA records (SSN, address history, employer records) are now operationally accessible to DOGE-affiliated personnel and cross-referenceable with the IRS financial data pipeline.

**Practical implication for organizations**: The financial surveillance threat is no longer limited to IRS Criminal Investigation conducting formal investigations. The LCA mega-database is accessible to personnel operating outside traditional IRS institutional constraints, and IRS records flow toward DHS and ICE through an agreement that courts have permitted to continue despite documented IRC violations. [PBS News — Taxpayer data wrongly shared with DHS](https://www.pbs.org/newshour/politics/data-of-thousands-of-taxpayers-wrongly-shared-with-dhs-court-filing-says), [Federal News Network — IRS-ICE data sharing court ruling](https://federalnewsnetwork.com/litigation/2026/02/court-says-the-irs-can-continue-to-share-immigrants-taxpayer-data-with-ice/)

---

### 1.4 Cryptocurrency Exchange KYC in the LCA Pipeline

LCA ingests cryptocurrency data from regulated U.S. exchanges. Coinbase is explicitly named in contract documentation. Any exchange that operates in the U.S. under FinCEN's money services business registration is subject to BSA reporting requirements, including KYC (Know Your Customer) registration for account holders and suspicious activity reporting.

When you open an account at a regulated U.S. cryptocurrency exchange, you provide:
- Legal name
- SSN or EIN
- Address
- Government-issued ID

Your wallet addresses used on that exchange are linked to your SSN in exchange compliance records. Those records are accessible to IRS LCA. This means that any Bitcoin transactions from wallets you created through a KYC exchange are traceable to your identity — both through chain analysis (Bitcoin's public ledger) and directly through the exchange's compliance database.

This is the entry-point vulnerability for all cryptocurrency privacy approaches: the on-chain technical privacy of a cryptocurrency is irrelevant if the wallet was created at a KYC exchange. All subsequent transactions from that wallet inherit the identity link established at account creation.

---

## Part 2: Organizational Financial Hygiene

### 2.1 Documentation as Legal Defense

The LCA platform's threat to advocacy organizations is not that it will find evidence of crimes. It is that it will find *patterns* that can be mischaracterized as suspicious. The most effective counter to financial surveillance used as a political weapon is rigorous documentation of the legitimate purpose of every transaction category in your financial operations.

**For every unusual transaction category, document**:
- The mission justification (how does this transaction advance the organization's exempt purpose?)
- The decision-making process (who authorized it, under what policy?)
- The recipients (who received funds, for what specific purpose?)
- The legal authority (what provision of the organization's bylaws or fiscal policy covers this?)

This documentation does not need to be public. It is internal records that make legal defense possible if an investigation is initiated. An organization that can produce a clear paper trail for all financial activity is significantly harder to mischaracterize than one that has no contemporaneous documentation.

**Specific documentation priorities**:
- Cash disbursements of any amount (document recipient, purpose, and authorization)
- Grants to individuals (document grantmaking policy and individual basis for award)
- International wire transfers (document foreign recipient's identity and mission-alignment)
- Cryptocurrency transactions (document wallet source, transaction purpose, and custody chain)
- Payments to politically sensitive vendors or partners (document arm's-length nature and legitimate purpose)

### 2.2 Account Separation: Mission-Aligned vs. Politically-Exposed

Organizations with both general operations and specific activities that are more politically exposed (voter registration, direct action support, immigration legal defense, mutual aid with undocumented populations) should maintain separate accounts for these distinct activity categories.

**The LCA social graph problem**: If your organization's primary operating account shows transactions with entities under LCA investigation, the entire account's transaction history becomes potentially visible to investigators building the social graph of that investigation. Separate accounts for politically exposed programs limit the blast radius: an investigator following the social graph of a connected entity reaches a dedicated account with limited transaction history, not your entire organization's finances.

**Account separation principles**:
- One account per legally distinct purpose (general operations, mutual aid fund, legal defense fund, bail fund)
- No transaction overlap between politically exposed accounts and general operations beyond authorized grants (which should be documented as transfers per your grantmaking policy)
- Board-level authorization documented for any transfer between accounts
- Each account should be explainable on its own: if investigators see only this account, is the activity comprehensible and legally defensible?

### 2.3 Form 990 and Public Disclosure Management

501(c)(3) organizations are required to file Form 990 annually, which is publicly available. Form 990 requires disclosure of:
- All revenues and expenses
- Names and compensation of officers, directors, and key employees
- Names and addresses of highest-paid contractors
- Significant program accomplishments
- Names of substantial contributors (on Schedule B, which is NOT publicly disclosed for 501(c)(3)s — this is a common misconception)

**The Schedule B protection**: Schedule B (significant donor names) is filed with the IRS but is protected from public disclosure for 501(c)(3)s under current law, following the Supreme Court's affirmation of donor privacy protections in *Americans for Prosperity Foundation v. Bonta* (2021). However, Schedule B is accessible to IRS investigators, including those using LCA. Donor name protection from public disclosure does not mean protection from IRS investigation.

Organizations should ensure their 990 narratives accurately describe their programs without providing an organizational roadmap that makes it easier to identify and target specific programs for investigation. This is not evasion — it is the difference between a functional program description and an internally-readable operational memo in a public document.

---

## Part 3: Donor Privacy Protection

### 3.1 Fiscal Sponsorship as Structural Privacy

Fiscal sponsorship is the arrangement in which a 501(c)(3) organization (the "fiscal sponsor") extends its tax-exempt status to an unincorporated project or initiative whose mission aligns with the sponsor's. Donors to a fiscally sponsored project make their contribution to the fiscal sponsor, which in turn grants the funds to the project.

**Privacy implications**: From a donor's perspective, fiscal sponsorship reduces the number of financial entities with which they have a direct traceable relationship. A donor to a fiscally sponsored project has a financial relationship with the fiscal sponsor, not the underlying project. If the underlying project comes under LCA investigation, the project's financial records held at the fiscal sponsor level are the investigative target — and fiscal sponsor organizations typically maintain internal records separate from their own operations.

**Fiscal sponsorship is not a privacy guarantee**: Investigators with appropriate legal authority can subpoena the fiscal sponsor's records for the specific project. What fiscal sponsorship provides is structural distance, not structural invisibility. It is one layer of organizational separation, not an impenetrable barrier.

**Common fiscal sponsors for advocacy and mutual aid work**:
- HIAS (for refugee-related work)
- New Venture Fund (for broad progressive policy work)
- Community Catalyst (for healthcare advocacy)
- Alliance for Global Justice (for international solidarity work)
- Tides Foundation (for a wide range of social change work)

The National Council of Nonprofits maintains current guidance on fiscal sponsorship models. [National Council of Nonprofits — Fiscal Sponsorship](https://www.councilofnonprofits.org/running-nonprofit/administration-and-financial-management/fiscal-sponsorship-nonprofits)

### 3.2 Anonymous Donation Channels

**First Amendment background**: Since *NAACP v. Alabama* (1958), courts have recognized a First Amendment right to anonymous association, including anonymous financial support of organizations. This right has been consistently reaffirmed, most recently in *Americans for Prosperity Foundation v. Bonta* (2021). Accepting anonymous donations is legal. Actively protecting donor privacy within the bounds of applicable tax law is legal and has constitutional grounding.

**Practical anonymous donation mechanisms**:

*Cash donations*: The most direct form of anonymous donation. Organizations are required to file Form 8300 for cash donations over $10,000. Cash donations under this threshold are not subject to separate reporting requirements beyond the organization's own bookkeeping (though good practice is to document receipt and donor-anonymous use consistent with your gift acceptance policy). Cash is traceable to the donor only if the donor is observed or identified at the point of giving.

*Money orders*: Purchasable with cash at convenience stores, post offices, and banks. Money orders under $3,000 can typically be purchased without identification. They are functionally anonymous from the organization's perspective (the organization receives a money order; it does not know who purchased it). Note: money orders over $3,000 from a single issuing entity within a period may require AML documentation at the point of purchase under federal MSB rules.

*Check from a donor-advised fund (DAF)*: Donor-advised funds allow donors to make an irrevocable contribution to the DAF (e.g., Fidelity Charitable, Schwab Charitable), take the tax deduction, and then direct grants from the DAF to recipient organizations over time. Grants from DAFs can be made without disclosing the underlying donor's identity to the recipient organization. The DAF itself knows the donor's identity, but the recipient sees only the DAF as the payer.

*Privacy coins for organizations that choose to accept them*: Addressed in Part 4.

### 3.3 What Organizations Cannot Do

Organizations cannot accept donations they know are intended to circumvent legal reporting requirements. If a donor explicitly tells you they are giving in a way specifically structured to avoid detection, accepting those funds creates legal risk. The distinction is between *offering privacy-preserving donation mechanisms* (legal) and *knowingly facilitating evasion of financial reporting requirements* (illegal).

---

## Part 4: Cryptocurrency and Digital Asset Privacy

### 4.1 Bitcoin vs. Monero: A Critical Distinction

This section addresses the most common misconception in advocacy community financial privacy discussions: that all cryptocurrencies provide similar privacy.

**Bitcoin is a public ledger.** Every Bitcoin transaction is permanently recorded on a blockchain that is publicly accessible to anyone. Chain analysis firms — Chainalysis and Elliptic are the two largest — hold contracts with the IRS, DEA, FBI, and CBP. Chainalysis won a $1.25 million IRS contract to develop Monero tracing tools, and maintains the most comprehensive institutional Bitcoin transaction graph in existence. [Chainalysis and Integra win $1.25M IRS contract — Bitcoin News](https://news.bitcoin.com/chainalysis-and-integra-win-1-25-million-irs-contract-to-break-monero/)

If your organization's Bitcoin wallet address is known (from a prior KYC exchange, a public donation page, or an on-chain link to a known address), Chainalysis can trace all transactions flowing to and from that address with high accuracy. Bitcoin provides pseudonymity, not privacy. Under Palantir's LCA data integration, chain analysis outputs feed directly into the broader financial social graph.

**Monero (XMR) has genuine on-chain privacy.** Monero uses three privacy technologies in combination:
- *Ring signatures*: Each transaction appears as one of a group of possible senders, making attribution to a specific sender cryptographically difficult
- *Stealth addresses*: Each transaction creates a one-time address for the recipient, preventing linking of incoming transactions to a known recipient address
- *RingCT (Ring Confidential Transactions)*: Transaction amounts are encrypted, hiding how much was sent

The IRS's $1.25 million investment specifically to attempt Monero tracing — and the fact that this contract was awarded because the IRS acknowledged it could not trace Monero with existing tools — confirms that Monero's on-chain privacy is genuine and meaningfully different from Bitcoin's.

**Critical caveat — entry and exit points are the vulnerability.** Monero's on-chain privacy is not the attack surface. The attack surface is where Monero connects to the regulated financial system:
- If you buy Monero at a KYC exchange (Coinbase, Kraken, etc.), the exchange has your SSN linked to your wallet
- If you sell Monero at a KYC exchange for USD, the exchange has your SSN linked to the receiving wallet
- Those exchange records are in the IRS LCA data pipeline

The practical rule: Monero's privacy only matters if the specific XMR in question has never touched a U.S. regulated exchange connected to your identity. If an organization receives a Monero donation from a wallet that was originally funded from a Coinbase account linked to the donor's SSN, the LCA system already has that connection.

### 4.2 Self-Custody Requirements

Self-custody means controlling your own cryptocurrency wallet private keys rather than holding funds at an exchange. For organizations and individuals using Monero for financial privacy, self-custody is not optional — it is the prerequisite.

Exchange-custodied Monero:
- Exchange holds your private keys
- Exchange has your KYC identity
- Exchange can be compelled to disclose transaction history
- IRS LCA has contract-based access to exchange compliance records

Self-custodied Monero (using Monero's official CLI or GUI wallet, or Feather Wallet):
- You hold your private keys
- No third party has your wallet-to-identity link
- Your transaction history is protected by Monero's on-chain privacy
- Access requires either compelled disclosure from you directly or a successful attack on Monero's cryptography (which as of 2026 the IRS acknowledges remains unsolved)

**Self-custody implementation for organizations**:
1. Download the official Monero wallet software from getmonero.org (verify the download signature)
2. Generate a wallet offline on a dedicated device if possible
3. Record your 25-word seed phrase on paper and store securely (not photographed, not in cloud storage, not emailed)
4. The organization's wallet address can be published for donations
5. Incoming funds are received directly to the self-custodied wallet

### 4.3 Peer-to-Peer Exchange Alternatives

LocalMonero, the primary peer-to-peer Monero exchange, delisted in May 2024. As of 2026, the primary alternatives for acquiring Monero without KYC connection are:

- **Bisq**: Decentralized peer-to-peer exchange, open-source, no central operator. Supports XMR trading. bisq.network
- **Haveno**: A Bisq-derived decentralized exchange specifically designed for Monero trading. haveno.exchange
- **In-person exchange**: Trading cash for XMR at a community level — documented in Bitcoin meetup communities, applicable to Monero
- **Mining**: Monero's Proof of Work algorithm (RandomX) is CPU-optimized and accessible on consumer hardware, making mining-acquired XMR the cleanest privacy baseline (no exchange connection ever)

**The exchange vulnerability reminder**: Every Bisq or Haveno trade that is connected to a bank account or credit card creates a financial record linking the trade to your identity. Peer-to-peer cash trades avoid this. Trades connected to traceable payment methods do not.

---

## Part 5: Cash-Based Financial Operations

### 5.1 Cash as the Baseline Privacy Tool

Cash is the single most effective financial privacy tool available to individuals and organizations. Cash transactions leave no transactional record in any database accessible to Palantir's LCA pipeline. A cash purchase does not appear in bank records, does not generate a FinCEN report, and cannot be reconstructed through chain analysis.

**The CTR threshold**: Financial institutions are required to file Currency Transaction Reports (CTRs) with FinCEN for cash transactions over $10,000. This is a reporting requirement, not a prohibition. Transactions over $10,000 in cash are entirely legal — they simply generate a FinCEN record. CTRs are available to IRS LCA. The threshold's existence does not mean organizations should avoid cash transactions over $10,000; it means organizations should understand that such transactions create a FinCEN record.

### 5.2 Structuring is Illegal — What This Means in Practice

**31 U.S.C. § 5324 prohibits structuring.** Structuring means deliberately breaking transactions into amounts below $10,000 specifically to avoid CTR reporting. It is a federal felony regardless of whether the underlying money is from a legal source. The law does not require that you be engaged in any other criminal activity — the act of structuring with intent to evade reporting is itself the crime. Penalties include up to 5 years in prison (up to 10 years if the structuring is part of a pattern or concurrent with another federal violation).

**What structuring looks like and how to avoid accusations of it**: An organization that regularly makes many small cash disbursements for legitimate programmatic reasons (mutual aid, housing assistance, food support) is not structuring. The relevant intent requirement is that the transaction-splitting was done *specifically to avoid a CTR*. Document the legitimate programmatic basis for your cash disbursement patterns. If your normal operations result in many cash transactions, your bookkeeping should make the legitimate purpose clear.

This playbook explicitly does not provide guidance on structuring and does not recommend it as a countermeasure. Any organization whose counsel or advisors suggest structuring to avoid financial scrutiny should seek new counsel immediately. [31 U.S.C. § 5324 — Cornell LII](https://www.law.cornell.edu/uscode/text/31/5324)

### 5.3 Cash Management for Sensitive Organizational Operations

For organizations that have legitimate programmatic reasons to operate primarily in cash (mutual aid networks that serve populations without bank accounts, street outreach programs, emergency housing assistance):

**Bookkeeping requirements**: All cash disbursements should be recorded in the organization's books with: date, amount, recipient description (anonymized as appropriate for client confidentiality), program purpose, and authorizing staff member. This documentation is for the organization's internal accountability and legal defense — not for public disclosure.

**Bank account strategy**: Organizations should not deposit all cash receipts and then make all cash disbursements through the same account in a pattern that looks like cycling. If your program model involves receiving restricted grants by wire and disbursing unrestricted program cash, the transaction pattern should be explainable from the grant documentation and program design.

**Petty cash funds**: Establish a documented petty cash policy with an authorized float amount, a reimbursement authorization process, and a monthly reconciliation. This is standard nonprofit financial management and provides the documentation that makes cash operations auditable and legally defensible.

---

## Part 6: Personal Financial Compartmentalization

### 6.1 Separate Accounts for Sensitive Work

The LCA social graph mapping works by following financial relationships. If an activist's personal bank account shows regular transactions with known organizing-related entities (payments to a printing company that prints flyers for protests, subscriptions to activist-adjacent services, donations to organizations under investigation), those transactions link the activist's personal financial identity to the investigation's social graph.

**Compartmentalization principles for individuals**:
- Maintain a separate account for personal financial activity unrelated to advocacy work
- Use cash, money orders, or privacy-preserving payment methods for activist-adjacent purchases
- Do not use your primary credit or debit card for purchases that document your organizing activity
- Pre-paid debit cards (purchased with cash) provide a layer of separation for individual purchases; they do require some identification in some contexts
- Venmo, CashApp, and Zelle all create transaction records that feed into LCA's financial data pipeline — use these only for transactions you are comfortable appearing in a financial investigation

### 6.2 Social Graph Minimization

The LCA platform maps social networks among investigation targets. The counter-strategy is to minimize the number of visible financial links between your accounts and organizations or individuals who are likely investigation targets.

**This is not financial secrecy — it is normal financial hygiene.** Most people do not make their complete financial transaction history publicly accessible. Compartmentalization simply extends normal financial hygiene to the specific threat that LCA poses: the financial social graph as a political targeting mechanism.

**Practical steps**:
1. Review your regular financial transaction patterns. Which recurring transactions create financial links to organizations or individuals that might be targeted?
2. For regular donations to advocacy organizations: consider whether giving through a donor-advised fund or in cash provides sufficient separation. A donation from your Fidelity Charitable DAF to an organization does not appear in your personal bank records.
3. For subscriptions, memberships, and dues to organizations under potential scrutiny: pay in cash or by money order where the organization can receive them.
4. For financial interactions with specific individuals known to be under investigation: consult with legal counsel before continuing to transact. The social graph inclusion is the risk, not the transaction itself — but legal counsel can advise on your specific situation.

### 6.3 Tax Filing and ITIN Users

Undocumented immigrants and others without Social Security Numbers who file taxes using Individual Taxpayer Identification Numbers (ITINs) are specifically in the IRS-DHS data-sharing pipeline. The IRS shared address data for approximately 2,260 ITIN filers with ICE in the initial disclosure — a disclosure that a federal judge found violated the Internal Revenue Code.

**For ITIN filers who are also engaged in advocacy work**: Your ITIN-linked tax records are one of the data sources flowing toward DHS under the current data-sharing agreement. Advice on this specific situation requires immigration and tax counsel together. This playbook cannot address the specific situation of undocumented individuals weighing the harms of tax compliance versus the risks of tax record data sharing — that is a judgment that requires individualized legal advice. Consult VITA programs and immigration legal aid organizations that can provide combined tax and immigration guidance.

---

## Part 7: Implementation Path

### Tier 1: Essential (All advocacy organizations and active mutual aid networks)

These measures represent baseline financial hygiene for any organization operating in a political environment where IRS scrutiny is plausible.

1. **Establish a documentation policy** for all unusual transaction categories (cash disbursements, grants to individuals, international transfers, cryptocurrency). Assign responsibility to a staff member or board treasurer. Implement within 30 days.

2. **Confirm Schedule B filing accuracy**: Verify that your organization's Form 990 Schedule B is filed but not publicly disclosed. If you have been publicly disclosing Schedule B voluntarily or erroneously, correct immediately.

3. **Separate accounts for distinct high-risk programs**: If your organization runs programs that could plausibly attract IRS scrutiny (immigration legal defense, bail fund, mutual aid for undocumented populations), open a separate bank account for each. Document the mission-alignment of each account and the organization's internal policy for inter-account transfers.

4. **Consult nonprofit tax counsel** about your specific financial risk profile. This playbook provides general orientation, not legal advice. An experienced nonprofit tax attorney can review your 990s and financial structure and advise on specific vulnerabilities.

**Time to implement**: 2–4 weeks (documentation policy + account separation + attorney consultation scheduling)

---

### Tier 2: Intermediate (Organizations actively receiving or disbursing funds for politically exposed programs; individual donors who give to organizations likely under LCA scrutiny)

All of Tier 1, plus:

5. **Explore fiscal sponsorship for highest-exposure programs**: If any of your programs carry the most political exposure, evaluate whether fiscal sponsorship through a larger, more established 501(c)(3) provides structural separation. Consult with the fiscal sponsor about their own risk management practices.

6. **Establish anonymous donation channels for donors who request them**: Publicize that your organization accepts cash and money orders. If technically feasible, establish a self-custodied Monero wallet and list the address for donations.

7. **Implement petty cash policy with written procedures**: If your organization already disburses cash, formalize the float, authorization, and reconciliation procedures. Have your attorney review the policy.

8. **Donor-advised fund outreach to large donors**: Brief major donors on the DAF mechanism for giving anonymously. Fidelity Charitable, Schwab Charitable, and Vanguard Charitable are the largest DAF sponsors.

9. **Review personal financial patterns** (for individual activists): Identify recurring transactions that create LCA social graph links. Switch to cash or money orders for contributions to organizations under scrutiny.

**Time to implement**: 4–8 weeks (fiscal sponsorship evaluation requires organizational decision-making; petty cash policy formalization is 1–2 days of staff time)

---

### Tier 3: Advanced (Organizations or individuals who have reason to believe they are currently under IRS investigation, have received subpoenas, or whose principals have been identified in LCA social graph mapping)

All of Tier 2, plus:

10. **Retain specialized tax litigation counsel immediately**: Do not rely on your regular nonprofit tax preparer for an active investigation. You need a tax attorney with IRS Criminal Investigation experience. The investigation posture is different from compliance posture.

11. **Implement full cryptocurrency privacy protocol**: Self-custodied Monero only. No KYC exchanges. Peer-to-peer acquisition only. Document the acquisition method and custody chain for organizational accountability purposes.

12. **Implement financial compartmentalization review**: Have counsel review all organizational accounts for LCA social graph exposure. Identify which accounts, if subpoenaed, would reveal the most operationally sensitive information, and evaluate whether restructuring those accounts is advisable.

13. **Establish a communication protocol with board members**: Board members have fiduciary responsibility and are often the named individuals in IRS investigations targeting organizations. Brief the board on the specific LCA threat model. Document that the board has been briefed.

14. **Review all vendor relationships for LCA social graph exposure**: Any vendor or contractor who is themselves under IRS investigation creates a social graph link from your organization to that investigation through payment records. Have counsel review whether any such relationships exist.

**Time to implement**: Ongoing — this tier represents an active legal response posture, not a one-time implementation project. The attorney relationship is the critical element.

---

## Part 8: FAQ for Advocacy Organizations and Individual Activists

**Q: Our organization does entirely lawful advocacy work. Why should we worry about IRS financial surveillance?**

The IRS LCA platform's documented pivot toward investigating "left-leaning groups" under Trump's direction means that political valence, not tax compliance status, is the relevant risk factor. The LCA platform's social-graph-mapping capability means that organizations connected — even through entirely legitimate transactions — to entities under investigation can become part of that investigation's evidence base. This is not about hiding illegal conduct. It is about maintaining documentation discipline and structural separation so that legitimate operations cannot be mischaracterized.

**Q: What is the difference between the CTR threshold and structuring? I want to make sure we're not accidentally doing something illegal.**

A Currency Transaction Report (CTR) is filed by your bank when you conduct a cash transaction over $10,000. This is a legal transaction — the reporting requirement is on the bank, not on you. Structuring (31 U.S.C. § 5324) is the crime of deliberately breaking transactions into amounts under $10,000 specifically to prevent the bank from filing a CTR. If your organization has a legitimate programmatic reason for its cash transaction patterns, you are not structuring. The test is intent: were the transaction amounts chosen based on your program design, or were they chosen specifically to stay under $10,000? Document the former carefully.

**Q: Is accepting Bitcoin donations a privacy risk?**

Yes, if the donor's Bitcoin wallet has any KYC exchange connection. All Bitcoin transactions are public on the blockchain. Chain analysis firms (Chainalysis, Elliptic) hold government contracts and can trace Bitcoin transactions with significant accuracy. Receiving Bitcoin donations exposes your organization's wallet to chain analysis linking. If you want to accept cryptocurrency for privacy reasons, Monero (with the entry/exit caveats in Part 4) is the technically appropriate choice. If you accept Bitcoin, assume the transaction history is visible to IRS LCA.

**Q: Can we accept completely anonymous cash donations? Is that legal?**

Yes. Anonymous cash donations are legal. Your obligation is to record the receipt in your books (amount, date, program designation) and to ensure you do not accept donations you know are intended to facilitate illegal activity. You are not required to document the identity of anonymous cash donors. Form 8300 is required only for cash transactions over $10,000.

**Q: Our organization doesn't file a 990 because we're small (under $50,000 in gross receipts). Are we still at risk from LCA financial surveillance?**

Organizations under $50,000 in gross receipts file Form 990-N (the "e-postcard"), which provides only minimal information. This reduces your exposure through the 990 channel. However, your bank account transactions remain potentially accessible through FinCEN SAR pipeline and, in an active investigation, through legal process (subpoena to your bank). The LCA social graph threat is primarily about financial transactions connecting you to investigation targets, not about your 990 filing status. Small organizations with financial connections to larger organizations under LCA scrutiny can still enter the social graph through those financial links.

**Q: We run a mutual aid network and disburse cash to individuals regularly. How do we protect the privacy of people we help?**

Client confidentiality in service-providing organizations is a separate question from organizational financial privacy. Your obligation under tax law is to your own books — you do not need to include individual recipients' names in your public or IRS-facing records for program disbursements, so long as your internal records can substantiate the program purpose. Consult with your nonprofit attorney about appropriate record-keeping practices that maintain client privacy while satisfying IRS record-keeping requirements. This is a standard nonprofit operational question with established legal guidance.

**Q: What about Venmo and CashApp — can we use these for donations?**

Both Venmo (PayPal) and CashApp (Block, Inc.) are registered money services businesses subject to FinCEN registration and BSA reporting requirements. They file SARs when they observe suspicious activity. Venmo and CashApp transaction data is accessible to law enforcement through legal process. Both platforms have changed their reporting thresholds for 1099-K purposes (now required at $600 aggregate annual transactions). Neither is appropriate for privacy-sensitive organizational financial operations. They are appropriate for incidental, low-stakes peer-to-peer payments.

---

## Part 9: Scenario-Specific Implementation Checklists

This section provides detailed action checklists for two primary scenarios: organizations (nonprofits, mutual aid networks) and individuals (donors, activists, employees of politically exposed organizations). These checklists are more granular than the summary checklist at the end of this playbook.

### Scenario A: Organizational Financial Hygiene Checklist (Nonprofits, Advocacy Organizations, Mutual Aid Networks)

Use this checklist if your organization handles donations, grants, or operational funds and may face financial surveillance or political targeting.

**Phase 1: Financial Governance Foundation (Complete Before Implementing Any Changes)**

*Board and leadership alignment*:
- [ ] Schedule board meeting or leadership discussion: agenda item is "financial surveillance risk and organizational response"
- [ ] Distribute PHASE_2_SEQUENCING_STRATEGY.md Section 1.1 (IRS LCA) to board members
- [ ] Board acknowledges understanding that organizations can be subject to financial surveillance based on mission, not conduct
- [ ] Board authorizes finance committee to recommend financial structure changes (do not unilaterally implement without board alignment)

*Qualified financial counsel*:
- [ ] Identify nonprofit tax attorney or CPA with experience in advocacy organization financial structure
  - Search: "nonprofit tax counsel [your state]" or ask local ACLU/legal aid organization for referral
  - Require: experience with controversial causes (immigration, climate, racial justice, labor — organizations known to face IRS scrutiny)
  - Initial consultation should cover: IRS LCA threat, financial surveillance, legal structure options
- [ ] Schedule initial counsel consultation: brief description of your programs, mission, and financial scale (annual budget)
- [ ] Counsel should review this playbook and provide written assessment: "Risk level: [low/medium/high]" and "Recommended structure changes: [X, Y, Z]"

*Current financial audit*:
- [ ] Meet with finance team: collect all current financial accounts (checking, savings, investment, cryptocurrency if any)
- [ ] Document account holders: which board members, staff, or representatives have signing authority on each account?
- [ ] List all financial institutions: which banks, credit unions, payment processors?
- [ ] Note account history: have any accounts been closed or restricted? If yes, when and why?
- [ ] Review 12-month transaction history: identify patterns that might trigger SARs (many small disbursements, large cash withdrawals, international transfers)

**Phase 2: Account Structure (Implement With Counsel Guidance)**

*Determine appropriate account structure*:
- [ ] Counsel recommends: single account vs. multiple accounts based on program risk profile
- [ ] Low-risk guidance: general-purpose nonprofit account at reputable bank
- [ ] Medium-risk guidance: separate accounts for politically exposed programs (housing assistance, immigration aid, legal defense)
- [ ] High-risk guidance: accounts at credit unions or CDFIs rather than national banks (lower de-banking risk); backup account at second institution
- [ ] Document counsel's recommendation in writing; file with board meeting minutes

*Open new accounts if needed*:
- [ ] If opening new account: credit union preferred (member-owned, mission-driven, lower retaliation risk than commercial banks)
- [ ] Provide account name: use organization legal name (not mission-descriptive name that reveals sensitive program areas)
- [ ] Example: Instead of "Housing Assistance for Undocumented Immigrants Fund," use organization legal name plus generic program designation like "Program Support Account"
- [ ] Provide documentation: EIN, nonprofit status certificate, board resolution authorizing account opening
- [ ] Establish signing authority: at least 2 signatories on account to reduce risk of unilateral decisions to freeze account

*Establish backup account*:
- [ ] Even if not actively used, maintain account at second institution (different bank or credit union)
- [ ] Fund minimally: $500-$1,000 to keep account active
- [ ] Review quarterly: confirm account is still active and accessible
- [ ] Purpose: if primary account is frozen or closed, operational funds are not completely inaccessible

**Phase 3: Transaction Documentation and Bookkeeping**

*Document legitimate purpose for unusual transactions*:
- [ ] For each major transaction category, create internal memo: "Transaction Pattern and Legitimate Purpose"
- [ ] Example 1 (mutual aid): "Distributions from mutual aid fund reflect grant recipients identified through [outreach process]. Each distribution documented as individual grant per [granmaking policy]. Distributions average $[X]; highest single distribution $[Y]. Distribution is mission-aligned activity as defined in bylaws Section [Z]."
- [ ] Example 2 (international transfers): "International wire transfer to [country] represents [specific program purpose]. Recipient is [organization name, legal status]. Transfer is documented in grant agreement dated [date]. This is authorized charitable giving per bylaws Section [Z] and IRS Form 990 reporting."
- [ ] Store these memos on secure cloud drive (Google Drive, OneDrive, encrypted) with access controlled to finance committee
- [ ] Update memos annually: this is your documentary evidence if transaction patterns are questioned

*Establish financial transaction log*:
- [ ] All unusual transactions (cash withdrawals >$5,000, international transfers, large disbursements to individuals, cryptocurrency transfers) logged with: date, amount, recipient, purpose, program code, authorizing staff/board member
- [ ] Store in encrypted spreadsheet or accounting software with restricted access
- [ ] Monthly reconciliation: finance committee reviews log to ensure all large transactions are documented and purposeful

**Phase 4: Form 990 and Public Financial Disclosure Strategy**

*Form 990 preparation with counsel*:
- [ ] Schedule call with nonprofit tax counsel before 990 filing
- [ ] Counsel reviews 990 narrative sections (Part I, Part VII) for:
  - Accuracy of program descriptions (do not need to be operationally detailed, but must be truthful)
  - Sensitivity of program names (e.g., "Emergency Assistance" more neutral than "Bail Fund Support")
  - Financial disclosure completeness (cannot omit significant transactions, but can group/summarize appropriately)
- [ ] Counsel confirms Schedule B (donor names, not publicly available) is complete and filed
- [ ] File 990 by deadline; retain copy; update board that 990 is filed

*Address public perception if organization is high-profile*:
- [ ] If your organization is named in news as under investigation or facing political pressure:
  - [ ] Do not modify current 990 filings (this looks retaliatory and can trigger worse scrutiny)
  - [ ] If next 990 filing is due, counsel advises on whether to proactively explain transaction pattern changes in narrative
  - [ ] Generally recommended: brief, neutral explanation ("In Year [X], we adopted program-specific accounting to improve financial management and oversight")

**Phase 5: Cash Management and Money Handling**

*Cash donation protocol*:
- [ ] Establish written policy: "Cash donations of [$ amount or above] trigger this protocol"
- [ ] Protocol steps:
  1. Donor provides donation with or without name/address (organization accepts both anonymous and named cash gifts)
  2. Staff member counts cash, verifies amount, documents in cash log with: date, amount, donor name if provided, program designation
  3. Cash is deposited within [X days] to bank account; deposit slip retained and matched to log entry
  4. No separate "cash fund" is maintained; all cash is banked
- [ ] Retain cash log for minimum 7 years (standard IRS retention period)
- [ ] Purpose: demonstrates legitimate cash flow and routine banking, not structuring or hidden cash operations

*Money order and petty cash*:
- [ ] Petty cash float: maximum amount authorized (typical: $200-$500)
- [ ] Petty cash custodian: designated staff member
- [ ] Monthly reconciliation: all petty cash expenditures documented with receipt (no exceptions)
- [ ] Reimbursement: petty cash is replenished monthly from bank account; all reimbursement requests require receipt and program code
- [ ] For recurring small payments (office supplies, transportation, small grants): use money orders purchased with bank debit card (not cash) for better transaction record

**Phase 6: Donor Privacy Protections**

*Donor communication on privacy*:
- [ ] Create written donor privacy policy: what personal information is collected, how it is stored, how it is protected
- [ ] Policy includes: organization does not sell or share donor information; organization retains donor information for tax/audit purposes; organization is subject to donor disclosure law (Schedule B, though not publicly available)
- [ ] Provide policy to all donors at point of contribution
- [ ] Document that donor received policy (checkbox on donation form: "I have received the donor privacy policy")

*Anonymous donation acceptance*:
- [ ] Organization accepts donations without requiring donor name/address
- [ ] Establish mechanism: cash donations (anonymous accepted); online donations (can use masked email/payment method)
- [ ] Provide alternate donation channels: [Email for questions about anonymous donation] or [Form to request anonymous donation options]

*Donor-advised fund and fiscal sponsorship evaluation*:
- [ ] For major donors concerned about privacy: provide information on donor-advised funds
  - Example: Donor contributes to DAF at community foundation; DAF recommends grants to your organization
  - Donor's identity is known to foundation, not to recipient organization
- [ ] For high-risk programs: evaluate fiscal sponsorship through established fiscal sponsor in your field
  - Example: HIAS (for immigration work), LGBTQ organizations have LGBTQ-focused fiscal sponsors
  - Fiscal sponsorship provides structural distance between individual donor and controversial program
- [ ] Provide both options to major donors; allow them to choose based on their privacy preferences

**Phase 7: Cryptocurrency Donation Acceptance (If Applicable)**

*Decision: should your organization accept cryptocurrency?*
- [ ] Counsel assesses: does accepting cryptocurrency meaningfully reduce surveillance exposure vs. legal/compliance burden?
- [ ] Most organizations: answer is no. Crypto acceptance adds compliance complexity without proportional benefit.
- [ ] Organizations where it makes sense: those with significant donor base of crypto-native supporters (Bitcoin/Monero communities) where crypto acceptance is lower-friction than traditional donation methods

*If implementing cryptocurrency acceptance*:
- [ ] Accept only Monero (not Bitcoin; Bitcoin is traceable on chain)
- [ ] Set up self-custodied wallet: use official Monero CLI or GUI wallet from getmonero.org
- [ ] Generate wallet on air-gapped device (device never connected to internet); record seed phrase on paper; store securely
- [ ] Publish wallet address for donations (address is public; does not reveal donation history or your organization's identity)
- [ ] Do not use exchange-custodied Monero or hardware wallet that requires exchange withdrawal (adds KYC link)
- [ ] Monthly: convert received Monero to USD via decentralized exchange (Bisq or Haveno) and deposit to bank account
  - [ ] Use peer-to-peer cash trade if possible to avoid bank account linkage during exchange process
  - [ ] If trading to fiat: trade small amounts ($2,000-$5,000) to avoid single large transaction that might trigger SAR
  - [ ] Document each Monero-to-fiat trade: date, amount converted, trade method, bank deposit date
- [ ] Tax treatment: value received Monero donations at fair market value on receipt date (not exchange date); include in annual revenue
- [ ] Consult tax counsel on Form 990 reporting: "cryptocurrency donations" should appear in supplement to gross revenue

**Phase 8: Regular Review and Monitoring**

*Quarterly finance committee meeting*:
- [ ] Agenda includes: review of transaction logs for unusual patterns, account status update (any de-banking warnings?), donor privacy compliance check
- [ ] If anything unusual: report to counsel before publicizing or changing structure
- [ ] Update board annually: "Financial surveillance threat assessment remains current; controls in place"

*Annual counsel check-in*:
- [ ] Meet with nonprofit tax counsel once per year to review: any changes to law? Any changes to IRS/FinCEN enforcement priorities? Any organizational changes that affect risk profile?
- [ ] Update written documentation: counsel confirms current structure remains appropriate, or recommends changes

---

### Scenario B: Individual Financial Privacy Checklist (Activists, Donors, Employees of Exposed Organizations)

Use this checklist if you are an individual activist, donor to politically exposed organizations, or employee of advocacy organization, and have reason to believe your personal financial activity may be subject to LCA or related financial surveillance.

**Phase 1: Financial Baseline and Risk Assessment**

*Understand your current financial exposure*:
- [ ] List all financial accounts: checking, savings, investment, cryptocurrency
- [ ] List all credit cards and payment platforms: Venmo, CashApp, PayPal, Square
- [ ] Document institutions: which banks, credit unions, payment processors?
- [ ] Review account history: over last 12 months, what is the range and pattern of transactions?

*Assess your LCA exposure*:
- [ ] Do you donate to organizations that are or could be under investigation?
- [ ] Do you work for an organization under political scrutiny?
- [ ] Do you purchase from vendors associated with activism (printing companies that print protest materials, activist-aligned bookstores, etc.)?
- [ ] Do you receive payments from politically-aligned sources (consulting, contract work for advocacy organizations)?
- [ ] If yes to any: you have moderate to high LCA exposure

*Document your performance/employment baseline*:
- [ ] If employed: save copy of your most recent performance evaluation
- [ ] If self-employed or contracting: document your current income level and major clients
- [ ] If retired: document your income sources
- [ ] Purpose: if you become subject to investigation or your employment is affected, you have baseline to compare against

**Phase 2: Compartmentalization Strategy (Personal + Activist)**

*Separate personal and activist-related finances*:
- [ ] Maintain a personal checking account: for routine personal expenses (housing, utilities, food, personal shopping)
- [ ] Do NOT use personal account for: donations to activist organizations, payments to politically sensitive vendors, activist-related purchases
- [ ] For activist spending: use dedicated payment method (see Phase 3)

*Personal account best practices*:
- [ ] Use personal account for: salary deposit, mortgage/rent, utilities, groceries, personal insurance, personal healthcare
- [ ] Avoid: any transaction that could be characterized as activism-related
- [ ] Goal: if this account alone is examined, it appears to be routine personal finances unrelated to activism

**Phase 3: Activist-Related Transaction Methods**

*Option A: Secondary personal debit card*:
- [ ] Open second checking account at same bank or different institution
- [ ] Use second account exclusively for: donations, activist purchases, payments to politically sensitive vendors
- [ ] Fund account with: transfers from primary account (documented, legitimate transfer)
- [ ] Withdrawal method: debit card or check from secondary account only; never use primary card for activist spending

*Option B: Cash-based spending*:
- [ ] For activist purchases under $1,000: withdraw cash from primary account (documented as "cash withdrawal," normal transaction)
- [ ] Use cash to purchase: activist materials, donations, payments to politically sensitive vendors
- [ ] No transaction record at point of sale; no transaction pattern link between your identity and vendor

*Option C: Prepaid debit cards*:
- [ ] Purchase prepaid debit card with cash (no purchase record)
- [ ] Load funds onto card with cash or from secondary account
- [ ] Use prepaid card for online activist-related purchases
- [ ] Limitation: some prepaid cards require ID at purchase or loading; research which cards have minimal ID requirements

*Option D: Avoid high-surveillance payment methods*:
- [ ] Do not use for activist spending: Venmo, CashApp, Zelle, PayPal (all create permanent transaction records visible in LCA)
- [ ] If you use these platforms: use only for transactions with close friends/family where activism link is not apparent
- [ ] If activist spending with activist-affiliated people: use Signal Pay (if available), in-person cash, or check

**Phase 4: Donation Strategies**

*Direct donations to organizations*:
- [ ] Donate via cash or money order (address envelope to organization; send via postal mail)
- [ ] Donate via check from personal account (less private than cash, but still creates partial separation from second-party payment networks)
- [ ] Donate via organization's website if they accept payment methods other than credit card (some accept cryptocurrency, some accept PayPal, etc.)
- [ ] If website requires credit card: use secondary account debit card, not primary card

*Donor-advised funds (if you have significant donation capacity)*:
- [ ] If you donate >$5,000/year to activist organizations:
  - [ ] Consider opening a donor-advised fund (DAF) through a community foundation or national DAF provider (Fidelity Charitable, Schwab Charitable)
  - [ ] Donate to your DAF from your primary account (legitimate charitable contribution, tax deductible)
  - [ ] DAF recommends grants from your DAF to activist organizations (you control where the money goes)
  - [ ] Advantage: your name is associated with the DAF, not with recipient organizations
  - [ ] Foundation has record of your donation; recipient organizations do not know your identity directly
- [ ] Consult with tax advisor: DAF structure can significantly improve privacy for major donors

*Fiscal sponsorship (if donor relationship is ongoing)*:
- [ ] If you provide regular funding to an activist project:
  - [ ] Investigate whether a fiscal sponsor exists for that project's program area
  - [ ] Donate to the fiscal sponsor designated for the project
  - [ ] Fiscal sponsor has your donation information; the specific project does not
  - [ ] This adds a layer of organizational separation
  - [ ] Find sponsors: fiscalsponsordirectory.org, or ask the project which sponsors serve their area

**Phase 5: Employment Financial Tracking**

*If you work for an advocacy organization or politically exposed employer*:
- [ ] Understand your organization's financial health: is it under financial stress that might lead to account closure?
- [ ] Follow organization's 990 filing: does the organization file annual Form 990? (Requirement for organizations >$50k annual revenue)
- [ ] If organization is under investigation or public scrutiny: consider whether continuing employment poses retaliation risk (see cybersecurity-hardening/whistleblower-playbook.md)
- [ ] Document your employment baseline: recent evaluations, compensation level, benefits

*For contractors or consultants to activist organizations*:
- [ ] Maintain separate bank account for contractor income vs. personal income
- [ ] Track all invoices and payments: dates, amounts, payment methods
- [ ] For major contracts (>$5,000/year): consult tax advisor on whether separate business entity (LLC, sole proprietorship) makes sense
- [ ] Purpose: if you are subject to investigation, clear documentation of legitimate income is important

**Phase 6: Credit Monitoring and Account Security**

*Personal credit monitoring*:
- [ ] Establish credit freeze with all three credit bureaus (Equifax, Experian, TransUnion)
  - [ ] Reason: under LCA investigation, adversary might attempt to open credit accounts in your name to gather intelligence
  - [ ] Credit freeze requires you to unfreeze to open legitimate credit; minor inconvenience but strong protection
  - [ ] Process: each bureau has free online freeze option; takes 5 minutes per bureau

*Bank account monitoring*:
- [ ] Set up alerts on all accounts: email alert for any withdrawal >$500, any check clearance, any unusual transaction
- [ ] Review account statements monthly: look for unauthorized transactions, unauthorized access, unusual payment patterns
- [ ] If account is closed or restricted: contact bank immediately; ask why; document reason in writing

*Credit card monitoring*:
- [ ] Check credit report annually (free at annualcreditreport.com): look for unauthorized accounts, inquiries, collections
- [ ] Dispute any unauthorized activity immediately

**Phase 7: Cryptocurrency for Personal Privacy (If Applicable)**

*Monero for financial privacy* (only if you have sophisticated technical capability):
- [ ] Monero provides on-chain privacy for transactions (sender, receiver, amount hidden)
- [ ] **Only use if**: you understand the exchange vulnerability (any KYC-connected Monero gives away your identity at the entry point)
- [ ] Appropriate use: receiving non-KYC Monero from activist networks and self-custodying for long-term holding

*How to acquire non-KYC Monero*:
- [ ] Bisq or Haveno decentralized exchange: trade Bitcoin or cash for Monero
- [ ] In-person trade: find local Monero community and trade cash for XMR (Bitcoin meetups sometimes include Monero traders)
- [ ] Accept Monero as payment: if you work for activist organization that receives Monero, self-custody it
- [ ] Do NOT: buy Monero from regulated exchange (Coinbase, Kraken, Gemini) with your identity; this defeats privacy purpose

*Self-custody for Monero holdings*:
- [ ] Use official Monero wallet (getmonero.org) or Feather Wallet (featherwallet.org)
- [ ] Generate wallet on air-gapped device if possible; record seed phrase on paper
- [ ] Never share private key; never import into hardware wallet connected to internet

*When to consider Monero*: only if you have reason to believe your financial accounts are subject to active investigation or if you are part of activist network that uses Monero as standard financial tool. For most individuals, the complexity and technical risk outweigh the privacy benefit.

**Phase 8: Ongoing Monitoring**

*Monthly self-check*:
- [ ] Review all account statements: any unexpected transactions?
- [ ] Check credit alerts: any unusual activity?
- [ ] Review activist spending patterns: are you maintaining separation between personal and activist finances?

*Quarterly review with trusted advisor*:
- [ ] Meet with trusted friend or advisor who understands activist finance
- [ ] Discuss: any changes in circumstances? Any new exposure? Any new financial accounts needed?

*Annual consultation with financial advisor or tax professional*:
- [ ] Tax advisor can review whether current structure is tax-efficient and appropriate for your situation
- [ ] If you have significant income or assets: consider whether LLC or trust structure makes sense for privacy reasons

---

## Resource Directory

### Legal Counsel and Tax Guidance
- **National Council of Nonprofits**: councilofnonprofits.org — general nonprofit financial management guidance including fiscal sponsorship
- **National Center on Philanthropy and the Law (NYU)**: law.nyu.edu/ncpl — academic center for nonprofit law; practitioner resources
- **Alliance for Justice — Bolder Advocacy**: bolderadvocacy.org — guides for 501(c)(3) and 501(c)(4) organizations on permissible advocacy activity
- **Lawyers Committee for Civil Rights Under Law**: lawyerscommittee.org — legal defense for organizations facing government retaliation
- **Center for Constitutional Rights**: ccrjustice.org — legal defense for organizations under government surveillance or prosecution

### Cryptocurrency Tools
- **Monero Project**: getmonero.org — official wallet software, documentation, and community
- **Feather Wallet**: featherwallet.org — lightweight Monero desktop wallet (open source, audited)
- **Bisq**: bisq.network — decentralized peer-to-peer exchange for Monero acquisition
- **Haveno**: haveno.exchange — Bisq-derived decentralized exchange, Monero-focused

### Financial Threat Documentation
- **The Intercept — Palantir IRS LCA reporting**: theintercept.com/2026/04/24/palantir-irs-contract-data/
- **EFF — Financial surveillance and the BSA**: eff.org/issues/financial-privacy
- **EPIC — Donor Privacy**: epic.org/issues/democracy-free-speech/donor-privacy/

### Fiscal Sponsorship Networks
- **Fiscal Sponsor Directory**: fiscalsponsordirectory.org — searchable directory of fiscal sponsors by program area
- **Alliance for Global Justice**: afgj.org — fiscal sponsorship for international solidarity and domestic social justice projects

---

## Summary Checklist

**Tier 1 — All organizations**:
- [ ] Documentation policy in place for all unusual transaction categories
- [ ] Schedule B filed (not publicly disclosed) — confirm with accountant
- [ ] Separate accounts for high-exposure programs
- [ ] Nonprofit tax counsel consulted

**Tier 2 — Politically exposed programs and individual activists**:
- [ ] Fiscal sponsorship evaluated for highest-exposure programs
- [ ] Anonymous donation channels established (cash/money order acceptance; Monero wallet if appropriate)
- [ ] Petty cash policy written and reviewed by counsel
- [ ] Major donors briefed on donor-advised fund mechanism
- [ ] Personal financial patterns reviewed for LCA social graph exposure

**Tier 3 — Active investigation risk**:
- [ ] Tax litigation counsel retained (specialized, not general nonprofit accountant)
- [ ] Full cryptocurrency privacy protocol implemented (self-custodied Monero only)
- [ ] Financial compartmentalization review completed with counsel
- [ ] Board briefed on LCA threat model; briefing documented
- [ ] Vendor relationships reviewed for social graph exposure

---

**Legal notice**: All guidance in this playbook assumes operations within legal boundaries. Organizations should consult with qualified nonprofit tax counsel and legal advisors before implementing any changes to financial structure, donation practices, or cryptocurrency operations. This playbook does not constitute legal or tax advice. The threat model and countermeasures described here are general in nature; specific organizations' situations may present different risks and appropriate responses that only qualified counsel familiar with the organization's specific facts can assess.

**Version**: 1.0
**Last updated**: May 6, 2026
**Next review**: July 26, 2026 (aligned with corpus quarterly review)
**Cross-references**: threat-model.md, palantir-threat-model.md, opsec-playbook.md, PHASE_2_SEQUENCING_STRATEGY.md Sections 1.1, 2.4, 3.4
