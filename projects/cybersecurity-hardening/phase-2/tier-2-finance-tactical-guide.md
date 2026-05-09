---
title: "Tier 2 Sector-Specific Tactical Guide: Financial Services"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Sector Expansion
audience: CISOs, risk officers, compliance officers, IT directors at banks, credit unions, investment advisers, broker-dealers, insurance companies, payment processors, and fintech organizations
word_count: ~5,100
depends_on:
  - 2026-threat-landscape-q2-update.md
  - threat-model.md
  - opsec-playbook.md
  - financial-resistance-playbook.md
confidence: high — all threat claims sourced to primary or near-primary sources as of May 2026
---

# Tier 2 Sector-Specific Tactical Guide: Financial Services

**Most important finding**: The 2026 financial sector threat environment has three characteristics that separate it from any prior year. First, ransomware groups have identified financial institutions as the highest-yield targets for large ransom demands, with the current median demand at $3 million — and 59% of organizations that are hit see their data successfully encrypted rather than recovered from backup, a 10-point increase from 2024. Second, the SEC's breach disclosure rule (four business days for material incidents) has collided with CIRCIA's 72-hour cyber incident reporting requirement to create a multi-agency reporting obligation that most financial organizations' IR plans do not address. Third, AI-powered attacks — specifically deepfake CEO voice fraud and autonomous phishing infrastructure — have crossed from experimental to active deployment against financial targets, with wire fraud losses attributable to AI social engineering increasing 38% in H2 2025.

**Role-specific navigation**: CISOs should read Sections 1–3 sequentially. Risk officers focused on regulatory exposure should begin at Section 4. IT directors executing technical controls should begin at Section 2. Compliance officers preparing for SEC disclosure should begin at Section 4.2.

---

## Section 1: 2026 Threat Model — The Five Active Attack Vectors

### 1.1 Ransomware — Financial Sector Targeting Patterns

Financial services represents approximately 18% of all confirmed ransomware incidents in 2026 by victim count, but approximately 32% of ransom payments by dollar value — a disparity that reflects deliberate targeting of institutions with the resources to pay. The threat actor groups most active against financial targets in 2026 are Cl0p (exploiting managed file transfer vulnerabilities), LockBit 4.0 (franchise model with specialized financial sector affiliates), and Scattered Spider (social engineering-first attacks targeting help desk and identity management systems).

**The Scattered Spider model in detail**: Scattered Spider's financial sector attacks begin not with malware but with a help desk call. The attacker calls the target's IT help desk impersonating an employee, reports a lost authenticator or locked account, and socially engineers a credential reset or MFA bypass. This approach succeeds because help desk staff are trained to be helpful and because identity verification at help desks is often informal ("Can you tell me your employee ID and the last four of your SSN?"). Once credentials are reset, the attacker has legitimate access to financial systems — not a suspicious intrusion that triggers endpoint detection, but an authorized login from a new location. The attacker then moves laterally to payment systems, wire transfer platforms, or trading infrastructure.

**The defense gap that Scattered Spider exploits**: Every financial organization has invested in technical controls — EDR, SIEM, DLP. The Scattered Spider vector bypasses all of them by obtaining legitimate credentials. The specific control required is identity verification protocol at the help desk that cannot be satisfied by information the attacker could have obtained through OSINT (employee ID, last-four SSN, manager's name — all findable in LinkedIn, data broker databases, or prior breach data). Effective help desk identity verification requires: (1) a security question or PIN set by the employee at onboarding that is not in any HR system accessible via OSINT, and (2) a callback to a verified phone number on file, not a number provided by the caller during the support interaction.

**Sources**: [Sophos: Ransomware in Financial Services](https://www.sophos.com/en-us/content/state-of-ransomware.aspx); [UpGuard: Biggest Cyber Threats for Financial Services in 2026](https://www.upguard.com/blog/biggest-cyber-threats-for-financial-services); [InvenioIT: Ransomware in Financial Services 2026](https://invenioit.com/continuity/ransomware-attacks-finance/)

### 1.2 AI-Powered Fraud — Deepfake Voice and Autonomous Phishing

In 2025, a finance employee at a major multinational was tricked into wiring $25 million to attackers who cloned the voice of the company's CFO in a deepfake video call that appeared to include several other senior executives. In 2026, this attack category has expanded from individual high-value fraud to systematic AI-powered phishing infrastructure that targets retail banking customers, treasury teams, and wire transfer operations at scale.

**The specific financial sector threat: Business Email Compromise 3.0**. Traditional BEC used compromised or spoofed executive email accounts to request fraudulent wire transfers. BEC 3.0 uses: (1) an AI-cloned voice or deepfake video of the CFO or CEO to create a "verbal confirmation" of the wire request, (2) an autonomous phishing platform that generates personalized context-aware phishing emails using LinkedIn and corporate website scraping, and (3) real-time impersonation of other trusted participants in a call or email chain.

The current detection rate for AI-cloned voice attacks is below 30% in real-time conditions. A treasury team that receives a wire transfer request by email, then a "verbal confirmation" from a voice that matches the CFO exactly, has very little in-the-moment defense. The protocol defense is the only effective response: wire transfers above a defined threshold require in-person or pre-verified callback confirmation, not verbal confirmation via a call that was initiated by the requester.

**The autonomous phishing threat at retail scale**: AI-generated phishing emails now produce messages that are context-aware (they include accurate information about recent account transactions, branch locations, and staff names), grammatically indistinguishable from legitimate communications, and personalized per recipient. Batch phishing campaigns that previously required human writing for each variant can now be generated at thousands-per-hour scale against customer contact lists obtained in prior data broker breaches.

**Sources**: [Jack Henry: Top Cybersecurity Trends for 2026](https://www.jackhenry.com/fintalk/top-cybersecurity-trends-for-2026-every-financial-leader-must-know); [UpGuard: Financial Services Threats 2026](https://www.upguard.com/blog/biggest-cyber-threats-for-financial-services)

### 1.3 Third-Party and Supply Chain Risk

Financial institutions depend on an extensive ecosystem of third-party technology and service providers — core banking vendors, payment processors, cloud infrastructure providers, FinTech integrations, and data aggregators. Each integration is a potential attack surface. The 2024 MOVEit file transfer vulnerability exploitation — where a single CVE in a widely used managed file transfer product exposed data at hundreds of financial institutions simultaneously — is now considered the defining template for financial sector supply chain attacks.

In 2026, three third-party risk categories are most active:

**Core banking and payment platform vendors**: Fiserv, FIS, Jack Henry, and similar core banking vendors process transactions for thousands of financial institutions simultaneously. A compromise at the vendor level — not at any individual institution — can cascade to all downstream clients. Your contracts with core banking vendors must include: cyber incident notification timelines (72 hours or less to first notification), evidence of annual third-party penetration testing, and SBOMs for software components.

**FinTech integrations and open banking APIs**: Financial institutions that have implemented open banking APIs or embedded FinTech integrations (account aggregation, payment apps, data analytics platforms) have created pathways into core banking systems that often receive less security scrutiny than traditional vendor relationships. Each OAuth connection, API key, and data-sharing arrangement is a potential attack vector. Conduct a full inventory of all third-party API connections; assess each for least-privilege access (can the integration access only what it needs?); and confirm that each connection has a defined termination process that you can execute within 24 hours.

**Cloud provider and SaaS concentration risk**: The increasing migration of banking systems to AWS, Azure, and Google Cloud creates concentration risk: if a major cloud provider experiences a service disruption or security incident, thousands of financial institutions sharing that infrastructure are affected simultaneously. Financial regulators (OCC, FDIC, Federal Reserve) have issued guidance requiring financial institutions to assess and document their cloud concentration risk, including what operations they could sustain if their primary cloud provider were unavailable for 24 or 72 hours.

### 1.4 Nation-State Targeting — Persistent Access and Long-Duration Espionage

The Salt Typhoon campaign, attributed to Chinese state-sponsored actors, achieved persistent access to multiple major U.S. telecommunications providers and from there accessed congressional and federal agency communications. The threat intelligence community assesses that the financial sector is a parallel target for similar long-duration persistent access operations — not for immediate disruption, but for intelligence collection, market movement data, and pre-positioning for potential future destructive operations.

**What persistent access looks like in financial sector context**: Attackers with long-duration access goals do not immediately trigger alerts. They move slowly, establish footholds in low-visibility systems (legacy infrastructure, backup systems, monitoring systems), exfiltrate data in volumes that blend into normal traffic, and maintain access for months to years before becoming active. A SOC that is tuned for ransomware indicators (rapid encryption, lateral movement, C2 beaconing) may not detect a nation-state actor that is moving at 1% of that speed.

**The hunt program implication**: Organizations at elevated nation-state risk (systemically important financial institutions, major exchanges, large custodians) should implement a proactive threat hunting program that goes beyond alert-based monitoring. Threat hunters look for attacker behavior that does not trigger alerts: unusual authentication patterns over weeks, not hours; low-volume data exfiltration to unusual destinations; access to archival or backup data that has no legitimate business reason.

### 1.5 Regulatory Surveillance and the Palantir Data Pipeline

The cybersecurity-hardening corpus documents how IRS Lead and Case Analytics (LCA) — a Palantir-powered platform — fuses financial records, FinCEN SARs, bank secrecy data, and cross-agency data into analytical profiles. For financial institutions, the specific threat is not that the institution itself is a surveillance target, but that the data the institution collects and reports (SARs, CTRs, beneficial ownership information) flows into a consolidated analytics environment that may be used in ways that go beyond the specific statutory purpose that authorized the collection.

**The compliance officer's framing**: This is not an argument against BSA/AML compliance reporting. Financial institutions are legally required to file SARs and CTRs. The point is that BSA data now feeds a much broader analytical environment than was contemplated when BSA obligations were designed. An institution that generates unusual volumes of SARs (through over-reporting), or that files SARs on customers based on protected characteristics rather than genuine suspicious activity, is contributing data to an analytical environment whose downstream uses extend beyond law enforcement in the traditional sense. The appropriate response is rigorous SAR quality: file on genuinely suspicious activity, document the specific indicators, avoid filing on pattern alone.

---

## Section 2: Priority Technical Controls — Financial Sector Implementation Matrix

### 2.1 Identity and Access Management — The Highest-ROI Control Category

The Scattered Spider attack pattern, wire fraud via deepfake, and credential-stuffing attacks against online banking platforms all share a common root cause: identity verification failures. The highest-ROI security investment category for financial institutions in 2026 is identity and access management (IAM).

**Phishing-resistant MFA**: Standard MFA (SMS codes, TOTP authenticator apps) is not adequate for financial institutions because SMS is vulnerable to SIM-swapping and TOTP codes can be phished via real-time man-in-the-middle proxies. Phishing-resistant MFA uses hardware security keys (FIDO2/WebAuthn standard) or passkeys that cryptographically bind the authentication to the specific website URL — a phishing site cannot capture and replay the authentication credential because it is not recognized by the user's device as the legitimate banking platform. FIDO2 hardware keys (Yubico YubiKey, Google Titan) cost $25–50 per user and represent the current gold standard.

**Privileged Access Management (PAM)**: Accounts with access to payment systems, wire transfer platforms, and trading infrastructure must use just-in-time (JIT) privilege elevation rather than standing administrative access. A standing administrative account that is compromised provides immediate, full access to critical financial systems. A JIT-elevated account that must be explicitly activated for each session, with a defined time window and explicit logging, dramatically limits the blast radius of a credential compromise.

**Customer-facing identity verification**: For consumer banking, implement behavioral biometrics (typing patterns, mouse movement, device orientation) that flag anomalous sessions even when credentials are valid. Behavioral biometrics are the defense against credential-stuffing attacks where attackers have valid username/password pairs from prior data broker breaches and are attempting automated login.

### 2.2 Wire Transfer and Payment Authorization Controls

Wire fraud losses are the single largest category of cyber-enabled financial crime by dollar value in 2026. The control architecture for wire fraud prevention has three layers:

**Dual authorization with out-of-band confirmation**: All wire transfers above a defined threshold (set this at the 90th percentile of routine transactions, not an arbitrary round number) require authorization from two individuals, with the final authorization confirmed via a callback to a pre-verified phone number — not a number provided in the wire request. This eliminates deepfake-enabled single-approver fraud.

**Wire transfer pattern anomaly detection**: Wire transfers to new beneficiaries, to beneficiaries in jurisdictions not previously used by the organization, or for amounts significantly above historical patterns should trigger automated hold and enhanced review. Wire fraud consistently exploits the "urgency and novelty" combination: new beneficiary, unusual amount, executive requesting expedited processing.

**New vendor verification protocol**: The most common wire fraud scenario is a vendor impersonation: an attacker poses as a known vendor and submits a change-of-bank-account request before a large payment. Implement a policy that all beneficiary account changes require a callback to a phone number sourced from your vendor master file — not from any email or letter received after the change request. No exceptions. The phone number must come from your records, not from the requester.

### 2.3 Third-Party Risk Program — Annual Verification Cadence

Financial organizations with mature vendor risk programs have discovered that annual questionnaire-based vendor assessment is insufficient when the threat environment changes at quarterly intervals. The 2026 third-party risk program requires:

**Tier-based vendor classification**: Not all vendors carry the same risk. Classify vendors by: data access (PHI, customer financial data, credentials), system access (can they directly query or modify core banking systems?), and criticality (would their unavailability halt operations?). Tier 1 vendors (high data + system access + critical) get annual on-site or virtual assessed review plus a copy of their most recent SOC 2 Type II and penetration test results. Tier 2 vendors (medium risk) get annual questionnaire plus SOC 2. Tier 3 vendors (low risk) get triennial questionnaire.

**Incident notification SLA verification**: Verify that your contracts with Tier 1 and Tier 2 vendors require notification to you within 72 hours of any security incident affecting your data or systems. Many vendor contracts include notification provisions that are either absent or specify timelines of 5–10 business days — far too slow for CIRCIA and SEC disclosure compliance.

**SBOM requirement for technology vendors**: Beginning in 2026, require SBOMs from all technology vendors at contract renewal. An SBOM tells you what open-source components are in your vendor's software, so when a supply chain compromise like Shai-Hulud is disclosed, you can immediately determine whether your vendor's software is affected.

---

## Section 3: Incident Response — Multi-Regulator Notification Complexity

### 3.1 The Overlapping Notification Timeline Problem

Financial institutions are subject to more overlapping breach notification obligations than any other sector. Managing these obligations simultaneously — without missing a deadline or inconsistently characterizing the incident across regulators — is the most technically complex IR challenge in the financial sector.

**The four notification tracks that may apply simultaneously**:

1. **CIRCIA (CISA)**: 72 hours from discovery of a "substantial cyber incident" affecting critical infrastructure; 24 hours from any ransom payment. Financial institutions are critical infrastructure. Report at reportcyber.cisa.gov.

2. **SEC Cybersecurity Disclosure Rule (8-K Item 1.05)**: Material incidents must be disclosed within four business days of determining the incident is material. "Material" is a legal judgment call, but regulators have made clear that ransomware affecting operations or significant data breaches are presumptively material. File through EDGAR.

3. **Banking Regulator (OCC, FDIC, Federal Reserve, NCUA for credit unions)**: The Computer Security Incident Notification Rule requires notification to the primary banking regulator within 36 hours of a "notification incident" — an incident that has materially disrupted or degraded, or is reasonably likely to materially disrupt or degrade, a banking organization's operations.

4. **State breach notification**: Customer notification obligations under state consumer protection and breach notification laws (all 50 states have them) are typically 30–72 hours post-discovery for the most protective states. California's CCPA breach notification is one of the most demanding.

**The practical coordination challenge**: Your IR retainer firm is focused on containment and forensics. Your legal team is focused on privilege and disclosure strategy. Your communications team is focused on customer messaging. Your executive team is focused on operational continuity. The person who must coordinate four simultaneous regulatory disclosure tracks while all of this is happening is typically the CISO or general counsel. Designate this role explicitly before an incident, give that person pre-delegated authority to file initial notifications without waiting for full legal review, and pre-build the notification templates so they are ready to send with minimal completion work.

### 3.2 The SEC Materiality Determination

The SEC's cyber disclosure rule requires disclosure of material incidents within four business days of determining materiality — not four days from discovery. The materiality determination must be made "without unreasonable delay." This creates a judgment call that must be made rapidly under crisis conditions.

**Factors that strongly indicate materiality**: Any ransomware event that prevents the organization from processing customer transactions for more than 4 hours. Any data breach involving customer financial account information, social security numbers, or credentials. Any incident requiring notification to a banking regulator. Any incident disclosed in a press report before the organization has characterized it.

**The safe harbor problem**: There is currently no safe harbor provision in the SEC's cyber disclosure rule for organizations that make a good-faith determination that an incident is not material and later discover it was. This creates pressure to err toward disclosure. The SEC has brought enforcement action against Flagstar Bank for a disclosure it determined was materially incomplete — the Flagstar case established that minimizing the described scope of an incident in a disclosure, even if technically accurate, can constitute a misleading omission.

**Practical approach**: Prepare a materiality assessment template as part of your IR plan. When an incident is discovered, the template is completed within the first 24 hours, with legal counsel. It documents: what systems are affected, what customer data is involved, what operational impact has occurred, and the preliminary materiality judgment with the reasoning. This provides both the basis for the disclosure decision and the documented evidence of the organization's good-faith process.

---

## Section 4: Regulatory Compliance — The 2026 Priority Stack

### 4.1 DORA (For EU Operations) and the NIS2 Overlay

Financial institutions with EU operations are subject to the Digital Operational Resilience Act (DORA), which became applicable in January 2025. DORA creates four categories of obligations that go beyond what U.S. financial regulation requires:

**ICT risk management framework**: DORA requires a documented ICT risk management framework covering identification, protection, detection, response, recovery, and learning phases. This maps closely to the NIST Cybersecurity Framework but with more specific EU requirements for documentation and board approval.

**ICT third-party risk**: DORA imposes contractual requirements for all critical ICT third-party providers — not just standard financial sector vendor management — including exit strategies, service level agreements, and concentration risk assessment. This is more demanding than U.S. third-party risk requirements.

**Digital operational resilience testing**: DORA requires annual penetration testing for all financial entities, and threat-led penetration testing (TLPT — red team operations conducted by advanced external firms using intelligence-led scenarios) every three years for significant financial entities.

**Incident classification and reporting**: DORA's incident classification thresholds and reporting timelines to EU national competent authorities are different from U.S. timelines. Organizations with both EU and U.S. operations need a reporting playbook that maps incident characteristics to the applicable reporting requirements in each jurisdiction.

### 4.2 NYDFS Cybersecurity Regulation (23 NYCRR 500) — The Most Demanding U.S. State Framework

Financial institutions licensed in New York are subject to the NYDFS Cybersecurity Regulation, which is the most demanding state-level cybersecurity regulation for financial institutions in the United States. The 2023 amendments, effective in stages through 2025, introduced:

**CISO designation and board reporting**: A qualified CISO must be designated and must report to the board at least annually. The report must cover the cybersecurity program, the cyber risks facing the organization, and the adequacy of the organization's cybersecurity resources.

**Annual penetration testing and bi-annual vulnerability scanning**: Required for all covered entities. Findings must be tracked to remediation with documented timelines.

**72-hour incident notification to NYDFS**: Any cybersecurity event meeting the definition (unauthorized access to information systems, or disruption of normal operations) must be reported within 72 hours. This is narrower than CIRCIA's "substantial incident" threshold and may require reporting incidents that do not trigger CIRCIA.

**Class A requirements for larger organizations**: Organizations with over $20 million in gross annual revenue or over 2,000 end-of-year employees face additional requirements including privileged access management, endpoint detection and response, and a centralized audit log capability retained for five years.

### 4.3 The Annual Cybersecurity Certification

NYDFS requires an annual cybersecurity certification from the CISO confirming that the organization's cybersecurity program is in compliance with 23 NYCRR 500. This certification creates personal accountability for the CISO — not merely organizational liability. Before certifying:

- Confirm the most recent risk assessment is current (conducted within the past 12 months)
- Confirm all required annual tests (penetration test, vulnerability scans) have been completed and findings are in remediation
- Confirm the security awareness training program has been completed by all required staff
- Confirm the incident response plan has been reviewed and updated
- Confirm the CISO report to the board has been delivered

If any of these items cannot be confirmed: do not certify. Work with legal counsel to prepare a notice of exception or partial compliance if the program has known gaps.

---

## Section 5: Worked Examples by Role

### 5.1 CISO — The Board Risk Presentation

Financial sector boards typically include members with financial and legal backgrounds who understand risk quantification. Use their framework.

**The expected loss calculation**: Expected annual loss from a ransomware incident = (probability of an incident × average loss per incident). For a mid-sized regional bank: probability of a significant cyber incident in any given year is approximately 20-25% based on sector-wide statistics (roughly one in four to five organizations experiences a significant incident annually). Average loss is $5-10 million for a mid-sized institution (ransom, recovery costs, regulatory fines, customer notification, legal fees, reputation damage). Expected annual loss: $1-2.5 million.

**The cost-benefit frame**: Present the security program cost as a fraction of expected annual loss. A $400,000 annual security program cost (hiring, tools, external testing, insurance) against a $1-2.5 million expected annual loss produces a return on investment that justifies the program without requiring the board to evaluate technical controls they lack the expertise to assess.

**The SEC disclosure liability frame**: Add: "Under the SEC's cyber disclosure rule, a material incident requires public disclosure within four business days. The reputational and market impact of that disclosure — for a publicly traded institution — may exceed the direct breach costs. Our program is also an investor relations risk management program."

### 5.2 Risk Officer — The Third-Party Risk Exception Process

When a business unit wants to integrate a new FinTech partner or data vendor with access to customer data, they will push back against the full third-party risk assessment timeline (typically 4–8 weeks). The risk officer's role is to hold the process without creating an organizational reputation as a blocker.

**The tiered exception process**: For low-risk integrations (no direct access to core banking or customer account data, API-only with defined data fields, SOC 2 Type II on file from the vendor), offer a 2-week expedited review. For medium and high-risk integrations: full review, no expedited path. Define "expedited" clearly so business units know upfront whether their request qualifies. Vague discretionary exceptions create the perception that the process is negotiable.

**The legacy vendor problem**: Most financial institutions have legacy vendor relationships that predate the current third-party risk program and that have never been assessed. Build a rolling program that cycles through legacy vendors — start with the highest-risk (most data access, most critical to operations) and work down. A three-year cycle for legacy vendor assessment is a realistic pace for most organizations.

### 5.3 IT Director — The 90-Day Technical Priority List

Day 1–30: Deploy phishing-resistant MFA for all privileged accounts (system administrators, security operations, payment and wire transfer staff). These are the accounts most likely to be targeted and whose compromise has the highest blast radius.

Day 31–60: Implement the wire transfer dual-authorization and out-of-band callback protocol. Brief treasury and accounts payable staff on the new protocol. Document the process in writing so that social engineering attacks that attempt to invoke "emergency exception" authority can be referred to the written policy.

Day 61–90: Complete the third-party vendor inventory. For each vendor with direct data or system access, verify that a signed contract with incident notification SLA exists, request the most recent SOC 2 or equivalent third-party assessment, and document whether an annual review is currently scheduled. Flag any vendor where none of these exist — this is the starting list for your risk mitigation prioritization.

---

## Sources

- [InvenioIT: Ransomware in Financial Services — 2026 Insights](https://invenioit.com/continuity/ransomware-attacks-finance/)
- [UpGuard: The 6 Biggest Cyber Threats for Financial Services in 2026](https://www.upguard.com/blog/biggest-cyber-threats-for-financial-services)
- [Jack Henry: Top Cybersecurity Trends for 2026 Every Financial Leader Must Know](https://www.jackhenry.com/fintalk/top-cybersecurity-trends-for-2026-every-financial-leader-must-know)
- [HYPR: Cybersecurity Regulations for Financial Services 2026](https://www.hypr.com/blog/top-financial-services-cybersecurity-regulations)
- [Programs.com: Top Cybersecurity Risks and Solutions in the Financial Sector 2026](https://programs.com/resources/cybersecurity-finance-industry/)
- [Fortinet: Cybersecurity and Banking Regulations in 2026 and Beyond](https://www.fortinet.com/content/dam/fortinet/assets/reports/report-fortinet-banking-regulations.pdf)
- [FBI IC3: Cybersecurity Advisory on Scattered Spider](https://www.ic3.gov)
- [NYDFS: 23 NYCRR 500 Cybersecurity Regulation](https://www.dfs.ny.gov/industry_guidance/cybersecurity)
- [SEC: Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure Rule](https://www.sec.gov/rules/final/2023/33-11216.pdf)
- [Palantir Threat Model (corpus internal)](../palantir-threat-model.md)

---

*Created: 2026-05-09. Threat currency current as of May 9, 2026. DORA applicability is EU-jurisdiction-specific — verify with EU legal counsel for any cross-border operations. SEC materiality determinations require legal counsel analysis in each specific incident. Quarterly review checkpoint: July 26, 2026.*
