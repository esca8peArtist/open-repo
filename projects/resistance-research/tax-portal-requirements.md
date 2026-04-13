# Tax Portal Application — Software Requirements Specification

**Document ID**: TAX-PORT-SRS-001
**Version**: 1.0
**Date**: 2026-03-12
**Status**: Draft
**Classification**: Public

---

## Table of Contents

1. [Document Overview](#1-document-overview)
2. [System Vision](#2-system-vision)
3. [Stakeholders and User Personas](#3-stakeholders-and-user-personas)
4. [Functional Requirements — Citizen Portal](#4-functional-requirements--citizen-portal)
5. [Functional Requirements — Government Portal](#5-functional-requirements--government-portal)
6. [Non-Functional Requirements](#6-non-functional-requirements)
7. [Anti-Fraud Requirements](#7-anti-fraud-requirements)
8. [Requirements for Closing Loopholes](#8-requirements-for-closing-loopholes)
9. [Implementation Roadmap](#9-implementation-roadmap)
10. [Compliance and Legal Requirements](#10-compliance-and-legal-requirements)
11. [Success Metrics](#11-success-metrics)

---

## 1. Document Overview

### 1.1 Purpose

This Software Requirements Specification (SRS) defines the functional and non-functional requirements for the United States Government Tax Portal — a unified, government-operated, free platform replacing the current fragmented tax filing ecosystem dominated by private commercial interests.

This document is the authoritative reference for system design, procurement, development, testing, and ongoing operation of the Tax Portal. It establishes what the system must do, under what constraints, and how success is measured.

### 1.2 Scope

The Tax Portal encompasses two interconnected systems:

1. **Citizen Portal**: Public-facing interface through which individual taxpayers, tax professionals, and authorized representatives file returns, make payments, track refunds, and manage their tax accounts.

2. **Government Portal**: Internal and partially public-facing interface through which IRS and Treasury personnel collect, process, analyze, and report on tax data; conduct fraud detection; manage enforcement; and publish aggregated transparency data to the public.

This specification covers federal income tax filing for individuals (Form 1040 and all schedules), business entities (Forms 1065, 1120, 1120-S), employment tax (Form 941), and associated payment and account management functions. State tax integration is addressed as an interoperability requirement.

### 1.3 Intended Audience

- IRS Office of the Chief Information Officer
- Treasury Department technology leadership
- Congressional oversight committees (House Ways and Means, Senate Finance)
- Procuring agencies and government contracting officers
- Open source developer community
- Accessibility advocates and civil society reviewers
- State tax authority partners
- Academic and policy researchers

### 1.4 Relationship to Tax Reform

This specification is one component of a broader tax reform program. The portal implements and enforces requirements from the companion Tax Reform Requirements document. Where tax law changes (e.g., elimination of stepped-up basis, mandatory broker reporting of cryptocurrency) are referenced here, this document assumes the legal authority exists or will exist. The portal is designed to accommodate legislative changes through configuration rather than requiring re-engineering.

### 1.5 Definitions and Acronyms

| Term | Definition |
|------|-----------|
| ACH | Automated Clearing House — electronic bank transfer network |
| AGI | Adjusted Gross Income |
| BOIR | Beneficial Ownership Information Report |
| CTC | Child Tax Credit |
| EITC | Earned Income Tax Credit |
| ERO | Electronic Return Originator — tax professional authorized to e-file |
| FATCA | Foreign Account Tax Compliance Act |
| FedRAMP | Federal Risk and Authorization Management Program |
| FEIN | Federal Employer Identification Number |
| FISMA | Federal Information Security Modernization Act |
| IAL | Identity Assurance Level (NIST 800-63) |
| IRS | Internal Revenue Service |
| MFA | Multi-Factor Authentication |
| NIST | National Institute of Standards and Technology |
| OIC | Offer in Compromise |
| OMB | Office of Management and Budget |
| PA | Power of Attorney |
| PII | Personally Identifiable Information |
| PTIN | Preparer Tax Identification Number |
| SLA | Service Level Agreement |
| SSA | Social Security Administration |
| SSN | Social Security Number |
| TIN | Taxpayer Identification Number |
| VITA | Volunteer Income Tax Assistance |
| WCAG | Web Content Accessibility Guidelines |

### 1.6 Requirements ID Schema

Requirements are identified using the following schema:

```
TAX-PORT-[AREA]-[NUMBER]
```

Areas:
- `AUTH` — Authentication and Identity
- `PREP` — Pre-population and Data Import
- `FILE` — Filing Experience
- `SUB` — Submission and Confirmation
- `PAY` — Payment and Refund
- `ACCT` — Account and History
- `NOTIF` — Notifications and Communication
- `A11Y` — Accessibility and Multilingual
- `PRO` — Tax Professional Access
- `GOV` — Government Portal (general)
- `COLLECT` — Collection and Processing
- `FRAUD` — Fraud Detection and Prevention
- `AUDIT` — Audit and Enforcement
- `TRANS` — Transparency Dashboard
- `3P` — Third-Party Data Integration
- `PERF` — Performance
- `SEC` — Security
- `PRIV` — Privacy
- `INTER` — Interoperability
- `LOG` — Auditability and Logging
- `OSS` — Open Source and Vendor Independence
- `LOOP` — Loophole Enforcement
| `METRIC` — Success Metrics |

Example: `TAX-PORT-AUTH-001`

---

## 2. System Vision

### 2.1 What This Replaces

The current U.S. tax filing system is a failure of public administration:

- **Commercial domination**: Private companies (Intuit TurboTax, H&R Block, TaxAct) extract billions annually from citizens to perform a task the government already has the data to do automatically.
- **Free File failure**: The IRS Free File program, established in 2002, was deliberately undermined by private partners who hid free options, steered users to paid products, and successfully lobbied to prevent the IRS from building its own system.
- **Fragmentation**: Citizens must gather documents from multiple sources (employers, banks, brokers), re-enter data the IRS already has, and navigate inconsistent interfaces across a dozen vendors.
- **Accessibility failure**: No single authoritative government interface exists. Non-English speakers, elderly users, and low-income filers are disproportionately harmed.
- **Opacity**: Citizens have no centralized view of their tax account, cannot easily see their full filing history, and must call phone queues or mail letters to resolve issues.
- **Tax gap**: The $600+ billion annual tax gap is partly attributable to system complexity that makes compliance difficult and evasion easy.

The Tax Portal replaces:
- All IRS Free File vendor relationships
- EFTPS (Electronic Federal Tax Payment System) — to be absorbed
- "Where's My Refund" standalone tool
- Get Transcript standalone tool
- IRS Online Account (partial functionality)
- Paper correspondence for most account actions
- Phone-dependent processes for account management

### 2.2 Core Value Proposition — Citizens

- **Free, forever**: No cost to any citizen for any return of any complexity. Tax filing is a civic obligation; the government bears the cost.
- **Pre-populated**: The IRS already receives W-2s, 1099s, bank interest, broker statements, and Social Security income. The portal pre-fills this data. Most citizens confirm and submit.
- **Fast**: W-2 employees with standard situations complete filing in under 15 minutes. Complex filers with investments and schedules complete filing in under 60 minutes.
- **Understandable**: Every line is explained in plain language. No tax expertise required.
- **One place**: Account history, payments, correspondence, notices, refund tracking — all in one authenticated portal.
- **Trustworthy**: Government-owned, no advertisements, no upselling, no data sharing with third parties.

### 2.3 Core Value Proposition — Government

- **Real-time data**: Processing and analytics in near-real-time rather than annual batch cycles.
- **Fraud reduction**: Integrated fraud detection at every layer of the filing and processing pipeline.
- **Tax gap closure**: Pre-population and third-party matching make underreporting structurally harder.
- **Public accountability**: Aggregated, anonymized data published publicly so citizens can see how the tax system is operating.
- **Cost reduction**: Automated processing reduces cost-per-return from approximately $40 to under $5.
- **Enforcement efficiency**: Case management, document exchange, and audit communication all in one system.

### 2.4 Non-Goals

This system explicitly does NOT:

- **Set tax policy**: The portal implements law as written. Policy decisions belong to Congress.
- **Replace tax courts or formal appeals**: The portal supports case initiation and document exchange but does not replace formal legal proceedings.
- **File state returns directly** (Phase 1): State integration is a Phase 2+ feature. The portal will export state-ready data but not submit to state systems until integration agreements are in place.
- **Serve as financial advice**: The system calculates tax liability under current law. It does not provide financial planning advice.
- **Store data beyond legal retention requirements**: Data is retained only as long as legally required and then deleted.
- **Surveil citizens beyond tax administration**: Data collected for tax purposes is used only for tax administration. No behavioral profiles. No data sharing with law enforcement except as required by specific legal process with transparency reporting.
- **Require citizens to use the portal**: Paper filing remains legally available. The portal is the preferred and promoted option, not the mandatory one (though electronic filing mandates may be established separately by Congress for specific categories).

---

## 3. Stakeholders and User Personas

### 3.1 Citizen Filer — W-2 Employee (Simple Return)

**Profile**: Employed by a single employer, receives a W-2, takes the standard deduction, may have mortgage interest or charitable contributions but not enough to itemize, may have children qualifying for CTC/EITC.

**Volume**: Approximately 100 million filers. The modal American taxpayer.

**Goals**: File accurately, get refund quickly, spend minimal time.

**Pain points**: Paying $60-$150 for software to enter data the IRS already has. Confusion about whether to itemize. Fear of making mistakes.

**Portal experience target**: Login, confirm pre-populated W-2 data, answer 8-12 questions, review, submit. Under 15 minutes.

### 3.2 Self-Employed / Small Business Filer

**Profile**: Sole proprietor or single-member LLC. Receives 1099-NEC from multiple clients. Has business expenses. May have home office, vehicle use, health insurance deduction. Files Schedule C.

**Volume**: Approximately 25 million filers.

**Goals**: Claim all legitimate deductions, understand quarterly estimated tax obligations, avoid underpayment penalties.

**Pain points**: Complexity of Schedule C, record-keeping requirements, quarterly payment calculations, SE tax calculation.

**Portal experience target**: Guided Schedule C interview with plain-language prompts. SE tax automatically calculated. Estimated tax payment schedule generated automatically.

### 3.3 Complex Filer

**Profile**: Has investment income (Schedule D), rental property (Schedule E), partnership or S-corp income (K-1s), foreign financial accounts, or multiple business interests. May employ a tax professional.

**Volume**: Approximately 15 million filers.

**Goals**: Accurate filing of complex situations, minimize tax within legal bounds, avoid audit triggers.

**Pain points**: K-1 timing (arrive late, hold up filing), complexity of passive activity rules, cost basis tracking, foreign reporting requirements.

**Portal experience target**: Full Schedule D/E/K-1 support with guided interview. Cost basis import from brokers. FBAR/8938 integration. Extension filing with estimated payment.

### 3.4 Low-Income Filer (EITC Priority)

**Profile**: Income below $60,000. May qualify for EITC, CTC, Child and Dependent Care Credit, Premium Tax Credit. May have had no filing requirement in past years.

**Volume**: Approximately 30 million EITC-eligible filers.

**Goals**: Claim all credits owed, receive refund as fast as possible. For many, the EITC refund is the largest financial transaction of the year.

**Pain points**: Complexity of EITC eligibility rules (qualifying child, residency, income limits). Predatory tax preparer fees that consume a large share of the refund. Refund anticipation loans. Confusion about filing requirement thresholds.

**Portal experience target**: EITC eligibility prominently surfaced. Interview specifically designed to identify qualifying children and optimize credit. No barriers to claiming credits owed.

### 3.5 Non-English Speaker

**Profile**: Primary language is not English. May have limited English proficiency. Files taxes (all legal residents and many non-citizens have filing obligations).

**Volume**: Approximately 25 million potential filers with limited English proficiency.

**Goals**: Understand what is being asked, file accurately, avoid errors from mistranslation.

**Pain points**: English-only interfaces. Machine translation that introduces errors. No culturally appropriate guidance.

**Portal experience target**: Full portal available in 10 languages with professional (not machine) translation. Language selection persistent across sessions. Phone support available in same languages.

### 3.6 Elderly / Low-Tech User

**Profile**: Age 65+. May have limited digital literacy. May use screen magnification or assistive technology. May have fixed income from Social Security and pensions. May prefer phone or in-person assistance.

**Volume**: Approximately 50 million filers age 65+.

**Goals**: File accurately without confusion. Understand notices and correspondence. Avoid scams (elderly disproportionately targeted by tax scams).

**Pain points**: Confusing interfaces. Small text. Complex navigation. Difficulty with MFA using smartphones. Inability to speak with a human.

**Portal experience target**: Large-text mode. Simplified interface option. Easy handoff to phone support. VITA site integration for in-person assistance.

### 3.7 Tax Professional

**Profile**: CPA, enrolled agent, or registered tax preparer. Prepares returns for multiple clients. Holds a PTIN. May be ERO-authorized for e-filing.

**Volume**: Approximately 700,000 active tax preparers.

**Goals**: Efficient client management. Batch processing. Clear audit trail for professional responsibility. Client authorization management.

**Pain points**: Separate systems for each client. Manual re-entry of data available electronically. Authorization paper forms. No integrated client communication.

**Portal experience target**: Professional dashboard with client list. Client authorization via electronic Form 2848/8821. Batch submission capability. Client notification of return status.

### 3.8 IRS Revenue Officer

**Profile**: Enforcement employee responsible for collection, audit, or examination. Needs access to taxpayer account data to perform official duties.

**Goals**: Efficient case management. Access to complete account history. Document exchange with taxpayer. Timeline tracking.

**Pain points**: Fragmented systems requiring access to multiple internal databases. Slow document exchange via mail. Difficulty tracking case timelines.

**Portal experience target**: Unified case management with complete account view. Integrated document request and receipt. Secure two-way communication with taxpayer.

### 3.9 IRS Data Analyst

**Profile**: Statistical or analytical staff responsible for aggregate reporting, compliance research, and tax gap estimation.

**Goals**: Access to anonymized/aggregated data. Query capability across large datasets. Export for analysis.

**Portal experience target**: Analytical dashboard with query capability. Pre-built reports for standard outputs. Data export to standard formats.

### 3.10 Treasury / OMB

**Profile**: Senior officials responsible for budget projections, policy analysis, and economic modeling.

**Goals**: Real-time revenue visibility. Policy impact modeling. Historical trend data.

**Portal experience target**: Executive dashboard. Revenue-by-category breakdowns. Year-over-year comparisons. Policy scenario modeling tools.

### 3.11 Congressional Staff

**Profile**: Staff of House Ways and Means, Senate Finance, or Budget Committees. Responsible for tax policy research and oversight.

**Goals**: Understand distributional effects of tax law. Audit IRS enforcement patterns. Identify policy gaps.

**Portal experience target**: Access to public transparency dashboard with full download capability. Custom report generation. Historical data access.

### 3.12 Public / Researcher

**Profile**: Journalist, academic, think tank analyst, or interested citizen.

**Goals**: Understand how the tax system is operating. Verify claims about effective tax rates. Research tax enforcement patterns.

**Portal experience target**: Fully public transparency dashboard. No login required. Machine-readable data downloads. Clear methodology documentation.

---

## 4. Functional Requirements — Citizen Portal

### 4.1 Authentication and Identity Verification

#### 4.1.1 Multi-Factor Authentication

**TAX-PORT-AUTH-001**
- **Requirement**: The system SHALL require multi-factor authentication for all citizen account access.
- **Rationale**: Tax accounts contain highly sensitive financial PII. Single-factor authentication is insufficient given the volume and value of identity theft targeting tax refunds.
- **Acceptance Criteria**: No account can be accessed with username/password alone. Login without a second factor returns an authentication challenge, not account access.

**TAX-PORT-AUTH-002**
- **Requirement**: The system SHALL support the following second factors: TOTP authenticator app, hardware security key (FIDO2/WebAuthn), SMS OTP (as fallback only, with disclosure of risks), and government-issued identity verification via Login.gov.
- **Rationale**: Different users have different device capabilities and security preferences. Offering multiple options increases adoption while maintaining security.
- **Acceptance Criteria**: All listed second factor types work end-to-end. SMS OTP is presented as a fallback option, not the default, with a visible disclosure that SMS is less secure than app-based authentication.

**TAX-PORT-AUTH-003**
- **Requirement**: The system SHALL NOT require biometric authentication as the sole or mandatory method of identity verification.
- **Rationale**: Biometrics cannot be changed if compromised. Mandating biometrics excludes citizens who cannot or will not provide them. Prior IRS biometric vendor arrangements (ID.me) created public trust failures.
- **Acceptance Criteria**: A citizen can complete identity verification and full account access without ever providing a biometric. Biometric options, if offered, are opt-in and not required for any function.

**TAX-PORT-AUTH-004**
- **Requirement**: The system SHALL lock accounts after 5 consecutive failed authentication attempts and require identity re-verification to unlock.
- **Rationale**: Prevents brute-force credential stuffing attacks against tax accounts.
- **Acceptance Criteria**: After 5 failed attempts, login is disabled. Account unlock requires identity re-verification via a separate, out-of-band channel (not the same compromised credential).

#### 4.1.2 Identity Proofing

**TAX-PORT-AUTH-005**
- **Requirement**: The system SHALL implement identity proofing at NIST SP 800-63A Identity Assurance Level 2 (IAL2) for all accounts with access to tax return data or refund functions.
- **Rationale**: IAL2 provides reasonable assurance that the account holder is who they claim to be, appropriate for the sensitivity of tax data and refund fraud risk.
- **Acceptance Criteria**: Identity proofing process meets all IAL2 requirements as defined in NIST SP 800-63A, including evidence validation and identity binding. Third-party IAL2 audit confirms compliance before production launch.

**TAX-PORT-AUTH-006**
- **Requirement**: The system SHALL integrate with Login.gov as the primary identity proofing and authentication service.
- **Rationale**: Login.gov is the government's shared identity service, designed specifically for this purpose, IAL2 compliant, and avoids per-agency duplication of identity infrastructure.
- **Acceptance Criteria**: Citizens can create a Login.gov account from within the Tax Portal flow or link an existing Login.gov account. All identity proofing is delegated to Login.gov. The Tax Portal does not independently store identity documents.

**TAX-PORT-AUTH-007**
- **Requirement**: The system SHALL provide an alternative identity verification path for citizens who cannot complete online identity proofing, including in-person verification at IRS Taxpayer Assistance Centers and USPS Identity Verification locations.
- **Rationale**: Online identity proofing has a non-trivial failure rate, particularly for elderly citizens, those without government-issued ID, and those without consistent address history. No citizen should be locked out of tax filing due to identity proofing failure.
- **Acceptance Criteria**: An in-person verification pathway exists and is documented. Citizens who fail online proofing are presented with in-person options and a locator for verification sites.

#### 4.1.3 Account Recovery

**TAX-PORT-AUTH-008**
- **Requirement**: Account recovery SHALL require identity re-verification equivalent to initial account creation (IAL2) and SHALL NOT rely solely on knowledge-based authentication (KBA) questions.
- **Rationale**: KBA questions (mother's maiden name, first pet, etc.) are trivially defeated through social media research. Using KBA for account recovery of sensitive tax accounts creates a significant security vulnerability.
- **Acceptance Criteria**: Account recovery flow does not present KBA questions as the primary recovery mechanism. Recovery requires either re-verification via Login.gov or in-person verification at an IRS facility.

**TAX-PORT-AUTH-009**
- **Requirement**: Account recovery SHALL be possible for citizens who have lost access to all registered second factors, through a secure, identity-verified process that cannot be completed in under 24 hours (cooling-off period to prevent social engineering attacks).
- **Rationale**: Legitimate users do lose devices. A recovery path must exist. The 24-hour delay prevents attackers who have obtained partial credentials from immediately exploiting account recovery.
- **Acceptance Criteria**: Recovery path exists for total second-factor loss. Process requires IAL2 identity re-verification. System enforces minimum 24-hour delay between recovery initiation and account access restoration. Citizen is notified at original registered contact methods when recovery is initiated.

#### 4.1.4 Authorized Representative Access

**TAX-PORT-AUTH-010**
- **Requirement**: The system SHALL support electronic designation of authorized representatives via Form 2848 (Power of Attorney) and Form 8821 (Tax Information Authorization), with electronic signatures meeting the legal requirements of those forms.
- **Rationale**: Many taxpayers authorize tax professionals or family members to act on their behalf. This must be supported electronically to reduce paper burden.
- **Acceptance Criteria**: Electronic Form 2848 and 8821 can be completed and submitted within the portal. Authorized representatives can access the taxpayer's account with scope limited to what the authorization specifies. Both taxpayer and representative receive confirmation of authorization.

**TAX-PORT-AUTH-011**
- **Requirement**: The system SHALL support estate representative access for deceased taxpayers, including executor and administrator access verified against probate documentation.
- **Rationale**: Estates have tax filing obligations. Executors must be able to access deceased taxpayer accounts to file final returns and estate returns.
- **Acceptance Criteria**: An executor can apply for access to a deceased taxpayer's account. Access is granted only after verification of executor status. Access is scoped to tax years relevant to the estate.

**TAX-PORT-AUTH-012**
- **Requirement**: Authorized representative access SHALL be scoped to only the permissions granted in the authorization document and SHALL be revocable by the taxpayer at any time.
- **Rationale**: Authorization must not exceed its grant. Taxpayers must retain control over who has access to their accounts.
- **Acceptance Criteria**: Representative access is automatically limited to the scope specified in Form 2848/8821. Taxpayer can revoke authorization immediately through the portal. Revocation takes effect within 15 minutes of taxpayer action.

---

### 4.2 Pre-Population and Data Import

**TAX-PORT-PREP-001**
- **Requirement**: The system SHALL automatically pre-populate the following data types from IRS records when available: W-2 (wages, withholding, benefits), 1099-INT (bank interest), 1099-DIV (dividends), 1099-B (broker transactions, including cost basis), 1099-NEC (non-employee compensation), 1099-MISC (miscellaneous income), 1099-G (government payments, unemployment), 1099-R (retirement distributions), 1099-SSA (Social Security benefits), 1098 (mortgage interest), 1098-E (student loan interest), 1099-SA (HSA distributions), Form 5498 (IRA contributions), 1095-A (ACA marketplace coverage), and 1099-DA (digital asset transactions, when in effect).
- **Rationale**: All of this data is reported to the IRS by third parties. Re-entering it is a pure compliance burden on citizens. Pre-population is the core value proposition of the portal.
- **Acceptance Criteria**: For each data type listed, if the IRS has received the relevant information return for a taxpayer's SSN/TIN, that data appears pre-populated in the relevant section of the return. Pre-population success rate ≥ 95% for W-2 data (primary form type) measured in testing with synthetic test data.

**TAX-PORT-PREP-002**
- **Requirement**: Pre-populated data SHALL display the source (payer name and EIN), the date the data was received by the IRS, and a clear visual indicator distinguishing pre-populated data from citizen-entered data.
- **Rationale**: Citizens must be able to verify that pre-populated data matches their records. Transparency about data provenance builds trust and enables error detection.
- **Acceptance Criteria**: Every pre-populated field or section includes a visible "Source: [Payer Name] — Received by IRS on [date]" indicator. Visual distinction (e.g., different background color or icon) between pre-populated and manually entered data is present and described in the accessibility documentation.

**TAX-PORT-PREP-003**
- **Requirement**: The system SHALL provide a mechanism for citizens to dispute pre-populated data, with a workflow that: (a) allows the citizen to enter their corrected values, (b) flags the discrepancy for IRS review, (c) does not prevent submission of the return while the dispute is pending, and (d) notifies the citizen of dispute resolution.
- **Rationale**: Third-party data is sometimes incorrect. Citizens must not be forced to accept incorrect pre-populated data or be unable to file due to a data dispute.
- **Acceptance Criteria**: Dispute workflow exists for each pre-populated data type. Citizen can override pre-populated values and submit. Dispute is recorded and routed to appropriate IRS unit. Citizen receives notification within 30 days of dispute status.

**TAX-PORT-PREP-004**
- **Requirement**: The system SHALL provide manual entry fallback for all data types when pre-populated data is not available, with guided entry that validates formatting and cross-checks entered values against known ranges.
- **Rationale**: Not all payers have filed information returns on time or at all. Manual entry must be available as a fallback.
- **Acceptance Criteria**: Every section of the return that can be pre-populated also has a working manual entry interface. Manual entry includes input validation (e.g., EIN format, numeric ranges) with inline error messages.

**TAX-PORT-PREP-005**
- **Requirement**: The system SHALL carry forward relevant data from the prior year's return, including: prior year AGI (for identity verification), carryforward items (capital loss carryforward, net operating loss, charitable contribution carryforward, passive activity loss carryforward, basis in partnerships and S-corps), and prior year filing status and dependent information as suggestions.
- **Rationale**: Many tax items must be tracked across years. Failing to carry these forward leads to errors that disadvantage the taxpayer and generate audit issues.
- **Acceptance Criteria**: For taxpayers with a prior year return in the system, all carryforward items are automatically populated with prior year values. Taxpayer can review and modify. Prior year AGI is pre-filled for identity verification purposes.

**TAX-PORT-PREP-006**
- **Requirement**: When generating state return data, the system SHALL export all federal return data relevant to state returns and provide it to the state integration layer in a standardized format.
- **Rationale**: Most state income taxes are based on federal AGI with state-specific adjustments. Eliminating re-entry of federal data for state returns reduces burden and errors.
- **Acceptance Criteria**: State return data export includes all standard starting-point fields. States that have integrated with the portal receive this data via the state integration API.

**TAX-PORT-PREP-007**
- **Requirement**: The system SHALL display a "data freshness" indicator for each pre-populated item showing when the IRS received it from the payer, and SHALL allow early filers to file with known-incomplete data with a clear disclosure.
- **Rationale**: Filers who file in January or early February may not have all information returns available (payers have until January 31 for W-2s, February 28/March 31 for 1099s). Citizens should be informed of what data is present and what may still be expected.
- **Acceptance Criteria**: Each pre-populated item shows its receipt date. A "possibly incomplete" banner is shown when the system detects that expected information returns (based on prior year) have not yet been received. Filing is not blocked.

---

### 4.3 Filing Experience

**TAX-PORT-FILE-001**
- **Requirement**: The primary filing interface SHALL use an interview-style question-and-answer format that generates the appropriate forms and schedules based on citizen responses, without requiring the citizen to know which IRS forms are relevant.
- **Rationale**: The organizing principle of tax software should be the citizen's life situation, not IRS form structure. Form 1040 and its schedules are outputs of the interview, not inputs.
- **Acceptance Criteria**: A citizen can complete a full federal return without ever being asked to identify which IRS forms they need. The system determines form requirements based on interview answers. Expert mode (form-direct entry) is available for tax professionals.

**TAX-PORT-FILE-002**
- **Requirement**: The system SHALL provide a plain-language explanation for every line item on the return, accessible via an inline help mechanism, explaining: what the item is, why it affects the tax calculation, and how the system calculated the value.
- **Rationale**: Citizens cannot be expected to understand tax law. Plain-language explanations at the point of decision reduce errors, reduce anxiety, and build trust.
- **Acceptance Criteria**: Every line item has an associated help text at reading level ≤ 8th grade (Flesch-Kincaid or equivalent). Help text explains the item without jargon or cross-references to the Internal Revenue Code. Help text is accessible without leaving the filing flow.

**TAX-PORT-FILE-003**
- **Requirement**: The system SHALL display real-time tax calculations as the citizen progresses through the interview, showing the running total of estimated refund or amount owed, and SHALL explain what changed when the number changes.
- **Rationale**: Citizens want to understand how their situation affects their tax bill. Real-time feedback keeps citizens engaged and enables them to catch errors as they occur.
- **Acceptance Criteria**: A persistent display shows current estimated refund/owed amount. When the amount changes due to a citizen input, a brief explanation of the change appears (e.g., "Adding this mortgage interest increased your itemized deductions above the standard deduction, saving you $340").

**TAX-PORT-FILE-004**
- **Requirement**: The system SHALL automatically compare the standard deduction to the taxpayer's itemizable deductions and present both options with a clear recommendation, allowing the citizen to choose.
- **Rationale**: Most citizens default to the standard deduction even when itemizing would benefit them, due to the complexity of making the comparison. Automated comparison eliminates this disadvantage.
- **Acceptance Criteria**: Before finalizing deductions, the system presents a side-by-side comparison showing standard deduction amount vs. itemized deduction total. If itemized exceeds standard, the system recommends itemizing and quantifies the benefit. Citizen can override recommendation.

**TAX-PORT-FILE-005**
- **Requirement**: The system SHALL proactively notify citizens of relevant tax law changes that affect their return compared to the prior year, with plain-language explanations of the change and its estimated impact.
- **Rationale**: Tax law changes frequently. Citizens should not be surprised by changes in their refund amount without explanation.
- **Acceptance Criteria**: When a tax law change (enacted after the prior filing season) affects a line item on the current return, the system displays a notification at that point in the interview: "The Child Tax Credit changed this year. Previously it was $X per child; it is now $Y per child. For your 2 qualifying children, this means [impact statement]."

**TAX-PORT-FILE-006**
- **Requirement**: The filing interface SHALL implement complexity gating — citizens are only presented with questions and sections relevant to their tax situation. A W-2-only filer with standard deduction never encounters Schedule C, D, or E questions.
- **Rationale**: Exposing all citizens to the full complexity of the tax code creates confusion and errors. Progressive disclosure surfaces complexity only when needed.
- **Acceptance Criteria**: A taxpayer with only W-2 income, no dependents, and standard deduction completes filing in ≤ 15 questions. Schedule complexity gates are tested with a defined set of taxpayer profiles; each profile sees only relevant sections.

**TAX-PORT-FILE-007**
- **Requirement**: The system SHALL allow citizens to save their return at any point and resume on any device, with session data encrypted and retained for a minimum of 180 days from the last save.
- **Rationale**: Many citizens cannot complete their return in a single session. Save-and-resume is essential for accessibility and usability.
- **Acceptance Criteria**: Save functionality is available throughout the interview. A saved return can be resumed on a different device after re-authentication. Saved data is retained for 180 days. Citizens are notified before saved data expires.

**TAX-PORT-FILE-008**
- **Requirement**: The system SHALL display an estimated completion time at the start of the filing session, updated dynamically as the interview progresses, based on the complexity of the taxpayer's situation.
- **Rationale**: Citizens need to know how long the process will take so they can allocate appropriate time. Unknown completion time is a barrier to starting.
- **Acceptance Criteria**: Estimated completion time is displayed at session start and updated at major section transitions. Estimates are calibrated against actual completion times from user testing and production data.

**TAX-PORT-FILE-009**
- **Requirement**: The system SHALL perform pre-submission error checking that identifies: mathematical errors, missing required information, inconsistencies between sections, and common IRS rejection reasons — all presented in plain language with guidance for resolution.
- **Rationale**: Returns rejected by IRS e-file systems create delays and frustration. Pre-submission checking reduces rejection rates.
- **Acceptance Criteria**: Pre-submission check runs before the submission confirmation screen. All identified issues are listed with plain-language explanations and direct links to the relevant section of the interview for correction. The citizen can proceed to submission after reviewing issues (no mandatory blocking except for legally invalid returns).

**TAX-PORT-FILE-010**
- **Requirement**: The system SHALL provide a "what-if" scenario modeling tool, accessible at any point during filing, that allows citizens to model the tax impact of changes such as: additional retirement contributions, additional withholding, business expense changes, and filing status changes (where legally applicable).
- **Rationale**: Tax planning is most effective when citizens understand how their decisions affect their tax bill. The portal has all the data needed for real-time modeling.
- **Acceptance Criteria**: What-if tool allows modification of at least the following variables: traditional IRA/401k contributions, estimated business income/expense changes, charitable contributions. Results show the tax impact in dollars and explain the mechanism (e.g., "contributing $500 more to your traditional IRA would reduce your taxable income by $500, saving you approximately $110 in federal tax at your marginal rate of 22%").

**TAX-PORT-FILE-011**
- **Requirement**: The system SHALL include an EITC eligibility maximizer that: (a) proactively screens all filers for EITC eligibility, (b) identifies all qualifying children and relatives, (c) models the EITC amount for all possible claiming combinations, and (d) recommends the combination that maximizes the credit.
- **Rationale**: Billions of dollars in EITC go unclaimed each year due to complex eligibility rules. The portal has the information needed to maximize this credit for low-income filers.
- **Acceptance Criteria**: Every filer is screened for EITC eligibility regardless of whether they initiate the EITC section. For eligible filers with multiple potential qualifying persons, the system tests all eligible combinations and presents the maximum-credit option. EITC calculation is verified against IRS Publication 596 test cases.

**TAX-PORT-FILE-012**
- **Requirement**: The system SHALL support all schedules and forms required for individual income tax, including but not limited to: Schedules A, B, C, D, E, F, H, J, R, SE; Forms 2106, 2441, 3800, 4562, 4797, 4868, 5329, 5695, 6251, 8283, 8582, 8606, 8615, 8801, 8812, 8829, 8839, 8863, 8949, and all numbered forms referenced in Form 1040 instructions.
- **Rationale**: Complete form coverage is required for the portal to serve all taxpayers. Gaps in form coverage force complex filers to use paper or third-party software.
- **Acceptance Criteria**: All forms listed in the current-year Form 1040 instructions as potentially required are supported within the portal interview framework. Form coverage is documented and published. Gaps (if any in Phase 1) are disclosed.

---

### 4.4 Submission and Confirmation

**TAX-PORT-SUB-001**
- **Requirement**: The system SHALL support electronic signature of tax returns meeting the requirements of IRS Publication 1345 and applicable Treasury regulations, which is legally binding without a wet (physical) signature for electronically filed returns.
- **Rationale**: E-signatures for tax returns are legally established. Wet signatures are not required for e-filed returns and add unnecessary friction.
- **Acceptance Criteria**: Electronic signature process complies with IRS e-file requirements. Signed return is legally binding. Signature process includes identity attestation ("Under penalties of perjury, I declare...") with the statutory language.

**TAX-PORT-SUB-002**
- **Requirement**: Upon successful submission, the system SHALL provide: (a) a unique submission confirmation number, (b) a timestamped confirmation page, (c) a downloadable PDF copy of the submitted return, and (d) an email confirmation to the taxpayer's registered address.
- **Rationale**: Citizens need proof of timely submission. The confirmation number is evidence of filing and needed for subsequent inquiries.
- **Acceptance Criteria**: All four confirmation elements are provided within 60 seconds of submission. Confirmation PDF is identical to the submitted return. Email confirmation is delivered within 5 minutes.

**TAX-PORT-SUB-003**
- **Requirement**: The system SHALL provide real-time e-file acknowledgment within 24 hours showing whether the return was accepted by IRS systems or rejected, and in the case of rejection, SHALL provide the rejection reason in plain language with specific instructions for correction.
- **Rationale**: IRS e-file rejection reason codes are cryptic. Plain-language translation of rejection reasons enables citizens to correct and resubmit without external help.
- **Acceptance Criteria**: Acceptance/rejection status is visible in the citizen's account within 24 hours of submission. Rejection reasons are displayed in plain language corresponding to each IRS rejection code. For each rejection reason, guidance for correction is provided.

**TAX-PORT-SUB-004**
- **Requirement**: The system SHALL support filing of amended returns (Form 1040-X) for any prior year return on file in the system, with pre-population of the original return data and a comparison view showing original vs. amended values.
- **Rationale**: Amendments are a normal part of the tax process. Citizens should not need external software to amend a return filed through the portal.
- **Acceptance Criteria**: 1040-X can be initiated from the account history view for any prior year return. Original values are pre-populated. Changes are highlighted. Amended return goes through the same submission and confirmation process as original returns.

**TAX-PORT-SUB-005**
- **Requirement**: The system SHALL support filing of extension requests (Form 4868) with automatic calculation of estimated tax due, integrated with the payment system for estimated tax payment at extension filing.
- **Rationale**: Extensions are extremely common. The extension request must be coupled with an estimated tax payment to avoid penalties. Citizens often file extensions without knowing they need to pay estimated tax.
- **Acceptance Criteria**: 4868 can be filed through the portal. System calculates estimated tax owed based on available income data and prior year as a fallback. Payment integrated into extension workflow. Extension confirmed by IRS e-file acknowledgment.

**TAX-PORT-SUB-006**
- **Requirement**: The system SHALL present a final review checklist before submission showing: all income sources included, deductions and credits applied, refund or amount owed, payment method selected (if applicable), bank account for direct deposit (if applicable), and acknowledgment of key attestations.
- **Rationale**: A final review checkpoint reduces errors and ensures citizens have reviewed their return before submitting under penalty of perjury.
- **Acceptance Criteria**: Final checklist screen is presented before signature and submission. Checklist is generated dynamically based on the taxpayer's specific return. Citizen must scroll through and confirm the checklist before proceeding to signature.

---

### 4.5 Payment and Refund

**TAX-PORT-PAY-001**
- **Requirement**: The system SHALL support direct payment from a bank account via ACH debit, with no transaction fee, for all balance-due returns, estimated tax payments, and extension payments.
- **Rationale**: ACH bank payment is the lowest-cost, most reliable payment method and should be available fee-free as the primary payment option.
- **Acceptance Criteria**: ACH payment available for all payment types. No fee charged. Bank account information is validated before return submission. Payment scheduled for the filing deadline or a taxpayer-specified future date up to the filing deadline.

**TAX-PORT-PAY-002**
- **Requirement**: The system SHALL support debit card and credit card payments, with a clear, prominent disclosure of the convenience fee (charged by the payment processor, not the IRS) before the citizen completes payment.
- **Rationale**: Some citizens may prefer card payment for cash flow or rewards reasons. The fee must be disclosed before commitment.
- **Acceptance Criteria**: Card payment available. Fee amount displayed in dollars (not just as a percentage) before payment confirmation. Fee disclosure cannot be skipped or minimized. ACH option is presented alongside card option with "No Fee" label.

**TAX-PORT-PAY-003**
- **Requirement**: The system SHALL support installment agreement applications (Form 9465) directly within the portal, with real-time eligibility determination based on balance owed and compliance history, and immediate confirmation of agreement terms.
- **Rationale**: Many citizens cannot pay in full. The installment agreement process is currently cumbersome. Online application with immediate approval for qualifying balances reduces burden.
- **Acceptance Criteria**: Installment agreement application integrated into the payment flow for balance-due returns. Eligibility for streamlined installment agreement (currently balances ≤ $50,000) determined in real time. Terms presented and accepted online. Agreement confirmation provided immediately. ACH debit enrollment available for monthly payments.

**TAX-PORT-PAY-004**
- **Requirement**: The system SHALL support Offer in Compromise application initiation (Form 656) within the portal, with a pre-qualification screening tool, document upload capability, and status tracking.
- **Rationale**: OIC is an important taxpayer right. The current application process is extremely paper-intensive. Portal support reduces burden on eligible taxpayers.
- **Acceptance Criteria**: OIC pre-qualification tool (based on published IRS criteria) available in the portal. Form 656 can be completed and submitted electronically. Required supporting documents can be uploaded. Application status is trackable in the account.

**TAX-PORT-PAY-005**
- **Requirement**: The system SHALL provide real-time refund status, replacing the current "Where's My Refund" tool, with status displayed in the authenticated citizen account showing: return received, return processing, refund approved, refund sent (with date and method), and if delayed, the specific reason for delay in plain language.
- **Rationale**: "Where's My Refund" provides minimal information and is the source of enormous citizen frustration. Real-time status with plain-language explanations dramatically improves the experience.
- **Acceptance Criteria**: Refund status visible within the authenticated account. Status updates within 24 hours of IRS processing actions. Delay reasons are specific and actionable (e.g., "Your return requires identity verification. We sent a letter to your address on file on [date]. Please respond by [date].") rather than generic.

**TAX-PORT-PAY-006**
- **Requirement**: The system SHALL support the following refund delivery methods: direct deposit to up to 3 bank accounts with specified amounts or percentages, paper check to address on file, U.S. Savings Bonds (if still available), and application of refund to next tax year's estimated taxes — all selectable by the citizen during filing.
- **Rationale**: IRS allows multiple refund methods. Citizens should have clear, easy access to all options.
- **Acceptance Criteria**: All four methods available during return filing. Split direct deposit supports up to 3 accounts with flexible allocation. Method selection is clearly confirmed in the submission checklist and confirmation.

**TAX-PORT-PAY-007**
- **Requirement**: The system SHALL provide estimated quarterly tax payment reminders and worksheets for taxpayers with self-employment income or other non-withheld income, with pre-calculated suggested payment amounts based on current-year data and prior-year safe harbor calculations.
- **Rationale**: Underpayment penalties are avoidable if citizens know what to pay and when. Automated calculation and reminders significantly reduce underpayment.
- **Acceptance Criteria**: Citizens with Schedule C income or other non-withheld income receive quarterly reminders before each estimated payment deadline (April 15, June 15, September 15, January 15). Reminder includes calculated safe-harbor payment amount. Payment can be made directly from the reminder notification.

---

### 4.6 Account and History

**TAX-PORT-ACCT-001**
- **Requirement**: The system SHALL maintain and display a complete filing history for all returns on record, including: return type, tax year, filing date, AGI, total tax, refund or balance due, and filing status — with the ability to download the full return as a PDF for any year.
- **Rationale**: Citizens need access to their own tax history for mortgages, financial aid, benefits applications, and personal records. The government holds this data; citizens should have easy access to it.
- **Acceptance Criteria**: Filing history displays all returns in the IRS system for the authenticated taxpayer. Full return PDF available for download for any year. History page is printable in a format useful for third-party requests.

**TAX-PORT-ACCT-002**
- **Requirement**: The system SHALL display complete payment history including: all payments made, payment method, date, amount, and the tax period and form the payment was applied to.
- **Rationale**: Citizens need to verify that their payments have been properly credited. Current systems make this unnecessarily difficult.
- **Acceptance Criteria**: All payments in IRS records for the taxpayer are displayed. Payment application (which period and form) is shown. Payments can be searched and filtered by date and type.

**TAX-PORT-ACCT-003**
- **Requirement**: The system SHALL display all IRS notices and letters sent to the taxpayer, with the full text of the notice, a plain-language explanation of what it means and what action is required, and the ability to respond online where responses are appropriate.
- **Rationale**: IRS notices are currently sent by mail, are often confusing, and responding requires another paper letter or a phone call. Online access to notices with plain-language explanation and online response dramatically reduces burden.
- **Acceptance Criteria**: All notices generated for the taxpayer are accessible in the portal within 24 hours of generation (and concurrently with mailing). Each notice includes a plain-language summary section. For notices requiring a response, an online response pathway is available.

**TAX-PORT-ACCT-004**
- **Requirement**: The system SHALL provide a transcript ordering function equivalent to all current IRS transcript types (Return Transcript, Account Transcript, Record of Account Transcript, Wage and Income Transcript, Verification of Non-filing Letter) that can be downloaded immediately as a PDF.
- **Rationale**: Transcripts are frequently needed by citizens for mortgages, financial aid, and other purposes. The current Get Transcript process, while improved, is still separate and cumbersome.
- **Acceptance Criteria**: All transcript types available for download within the authenticated account. Transcripts are available for the same tax years as current IRS systems. Downloaded transcripts are identical to those produced by current IRS transcript systems.

**TAX-PORT-ACCT-005**
- **Requirement**: The system SHALL display the current account balance for each tax period, including: total assessed tax, payments applied, penalties and interest assessed (with explanations of how calculated), abatements granted, and net balance due or overpayment.
- **Rationale**: Citizens often do not understand why they owe more than they thought, or why a refund was reduced. Transparent balance display with penalty/interest explanation reduces confusion and disputes.
- **Acceptance Criteria**: Account balance is current as of the prior business day. Penalties and interest are broken down by type (failure to file, failure to pay, estimated tax underpayment) with plain-language calculation explanations.

---

### 4.7 Notifications and Communication

**TAX-PORT-NOTIF-001**
- **Requirement**: The system SHALL send proactive notifications to citizens when: a W-2 or other information return is received and available for review, the filing deadline is approaching (30, 14, 7, and 1 day before), an estimated tax payment deadline is approaching, a notice has been issued to the account, refund status changes, a balance becomes due, an audit communication is received, and an authorized representative takes action on the account.
- **Rationale**: Proactive notifications reduce missed deadlines, reduce surprise, and enable timely responses to issues.
- **Acceptance Criteria**: All notification triggers listed are implemented. Notifications are sent via email (required), SMS (opt-in), and visible in the portal account dashboard. Notification timing is configurable by the citizen for reminder notifications (e.g., choose 7-day vs. 14-day reminder).

**TAX-PORT-NOTIF-002**
- **Requirement**: The system SHALL support two-way secure messaging between citizens and IRS representatives, replacing phone and mail for account inquiries, notice responses, and documentation requests.
- **Rationale**: The IRS phone system is a significant burden on both citizens and IRS staff. Two-way secure messaging reduces this burden and creates a written record.
- **Acceptance Criteria**: Citizens can initiate a secure message to the IRS regarding any account matter. IRS can respond through the same thread. Message history is retained in the account. Responses to notices via messaging meet legal response requirements equivalent to mailed responses. IRS acknowledges receipt of messages within 1 business day and provides substantive response within 15 business days (or notifies of expected timeline for complex matters).

**TAX-PORT-NOTIF-003**
- **Requirement**: Citizens SHALL be able to configure notification preferences including: preferred channel (email, SMS, portal only), notification frequency (immediate vs. daily digest), and which notification types to receive at which channel.
- **Rationale**: Notification fatigue reduces compliance with important notifications. Citizen control over notification preferences increases engagement.
- **Acceptance Criteria**: Notification preferences page allows per-notification-type channel selection. Changes take effect within 1 hour. At least one notification channel must remain active for legally significant notifications (notices, audit communications).

---

### 4.8 Multilingual and Accessibility

**TAX-PORT-A11Y-001**
- **Requirement**: The full citizen portal, including all filing workflows, account management, notifications, and help content, SHALL be available in: English, Spanish, Simplified Chinese, Traditional Chinese, Vietnamese, Korean, Tagalog, Portuguese (Brazilian), Arabic, French, Russian, and Haitian Creole.
- **Rationale**: These 12 languages cover the primary languages of the LEP population in the United States with significant tax-filing populations. Tax compliance should not depend on English proficiency.
- **Acceptance Criteria**: All portal content is translated and maintained in all 12 languages. Translations are performed or reviewed by professional translators with tax domain knowledge, not solely machine translation. Tax-specific terminology is translated consistently using IRS-approved terminology where it exists.

**TAX-PORT-A11Y-002**
- **Requirement**: The system SHALL meet WCAG 2.1 Level AA as a minimum, with Level AAA compliance targeted for all critical filing flows.
- **Rationale**: WCAG 2.1 AA is the federal standard under Section 508. Higher AAA compliance for critical flows serves the 26% of American adults with disabilities.
- **Acceptance Criteria**: Automated accessibility audit (using tools such as axe-core or equivalent) passes all WCAG 2.1 AA checks for all pages. Manual accessibility audit by certified professional (IAAP CPWA or equivalent) confirms AA compliance. AAA compliance for account creation, return filing, and submission flows confirmed by audit.

**TAX-PORT-A11Y-003**
- **Requirement**: The system SHALL be fully navigable using keyboard alone, with visible focus indicators on all interactive elements meeting WCAG 2.1 AA focus visibility requirements.
- **Rationale**: Users with motor disabilities who cannot use a mouse depend on keyboard navigation. Focus visibility is essential for these users.
- **Acceptance Criteria**: Every interactive element on every page is reachable and operable by keyboard. Focus indicator is visible on all focused elements. Tab order follows logical reading order. No keyboard traps exist.

**TAX-PORT-A11Y-004**
- **Requirement**: The system SHALL be compatible with major screen readers (NVDA, JAWS, VoiceOver for iOS, TalkBack for Android) and SHALL be tested with these screen readers as part of the release process.
- **Rationale**: Screen reader users depend on correct semantic HTML and ARIA usage. Compatibility cannot be assumed; it must be tested.
- **Acceptance Criteria**: Screen reader testing with NVDA, JAWS, and VoiceOver is part of the QA process for every major release. All form fields have correct labels. All images have appropriate alt text. All dynamic content updates are announced to screen readers.

**TAX-PORT-A11Y-005**
- **Requirement**: All standard interface text SHALL be written at a reading level not exceeding grade 8 (Flesch-Kincaid or equivalent metric). Tax-specific terms that cannot be simplified SHALL be accompanied by plain-language explanations.
- **Rationale**: The average American reads at a 7th-8th grade level. Tax content must be understandable to the population it serves.
- **Acceptance Criteria**: Automated readability testing on all user-facing text confirms Flesch-Kincaid Grade Level ≤ 8 for standard content. Technical terms (e.g., "adjusted gross income") link to or display plain-language explanations.

**TAX-PORT-A11Y-006**
- **Requirement**: The system SHALL provide a low-bandwidth mode that reduces page weight by at least 70% through image compression, deferred loading of non-critical assets, and simplified layouts — with full functional equivalence to the standard interface.
- **Rationale**: Rural areas and lower-income households disproportionately have slow internet connections. Slow-loading pages prevent use of the portal.
- **Acceptance Criteria**: Low-bandwidth mode can be activated by user preference or auto-detected based on connection speed. Page weight in low-bandwidth mode is ≤ 30% of standard mode. All functions available in standard mode are available in low-bandwidth mode.

**TAX-PORT-A11Y-007**
- **Requirement**: The system SHALL support an assisted filing mode in which an IRS representative can co-browse with a citizen (with citizen's explicit consent) to provide real-time guidance without the representative being able to make changes to the return without citizen confirmation.
- **Rationale**: Some citizens need human assistance to file. Assisted filing enables IRS representatives and VITA volunteers to guide citizens without requiring in-person presence.
- **Acceptance Criteria**: Assisted filing mode can be initiated only with an explicit, documented consent action from the citizen. Representative can see the citizen's screen. Representative can annotate or highlight but cannot make changes directly. Any change must be confirmed by the citizen. Assisted session is logged.

**TAX-PORT-A11Y-008**
- **Requirement**: The system SHALL integrate a locator for VITA (Volunteer Income Tax Assistance) and TCE (Tax Counseling for the Elderly) sites, allowing citizens who prefer in-person assistance to find the nearest site with hours, services offered, and appointment availability where available.
- **Rationale**: Not all citizens can or will use the digital portal. In-person assistance is essential for full inclusivity. Integration with VITA avoids duplicate systems.
- **Acceptance Criteria**: VITA/TCE site locator is accessible from the portal without authentication. Search by ZIP code returns results sorted by distance with hours and services. Site database is updated in real time from the IRS VITA locator data.

---

### 4.9 Tax Professional Access

**TAX-PORT-PRO-001**
- **Requirement**: The system SHALL provide a dedicated tax professional portal with: PTIN-verified login, a client management dashboard, the ability to initiate and manage electronic Form 2848/8821 authorizations, and access to client accounts within the scope of those authorizations.
- **Rationale**: Tax professionals are a critical part of the filing ecosystem and serve the most complex taxpayers. A dedicated professional interface is more efficient than having them use the citizen interface.
- **Acceptance Criteria**: Tax professional portal login requires PTIN verification against IRS PTIN database. Client dashboard shows all clients with active authorizations. Authorization requests can be sent to clients electronically. Client account access is scoped exactly to the authorization granted.

**TAX-PORT-PRO-002**
- **Requirement**: The professional portal SHALL support batch filing capability allowing a preparer to submit multiple client returns in a single session, with per-return confirmation and error handling.
- **Rationale**: Tax professionals prepare hundreds or thousands of returns. Batch capability is a basic efficiency requirement for professional use.
- **Acceptance Criteria**: Batch submission accepts multiple completed returns. Each return in a batch receives individual confirmation or rejection. Errors in one return do not block submission of other returns in the batch. Batch submission is logged with preparer PTIN.

**TAX-PORT-PRO-003**
- **Requirement**: The professional portal SHALL enforce ERO (Electronic Return Originator) requirements including: preparer signature on returns, disclosure of preparation fees, and prohibition on preparers claiming refunds to preparer bank accounts.
- **Rationale**: ERO rules exist to protect taxpayers from fraudulent preparers. The portal must enforce these rules systematically.
- **Acceptance Criteria**: Return submitted by preparer includes preparer signature with PTIN. Preparation fee is disclosed on the return. System prevents specification of a bank account not matching the taxpayer's verified bank account for direct deposit of refund (prevents refund diversion fraud).

---

## 5. Functional Requirements — Government Portal

### 5.1 Collection and Processing

**TAX-PORT-COLLECT-001**
- **Requirement**: The government portal SHALL provide a real-time dashboard showing: returns received (count and aggregate revenue) by day, week, month, and year-to-date; refunds issued; balance due returns; and comparison to prior year and budget projections.
- **Rationale**: Real-time revenue visibility is essential for Treasury cash management and congressional oversight.
- **Acceptance Criteria**: Dashboard data is updated at minimum every 15 minutes during business hours. Data is accurate to within 1% of actual processed amounts verified by reconciliation.

**TAX-PORT-COLLECT-002**
- **Requirement**: The system SHALL process at least 98% of error-free electronically filed returns and issue refunds within 21 calendar days of receipt.
- **Rationale**: 21 days is the current IRS standard for e-file refunds. This becomes a system SLA rather than a target.
- **Acceptance Criteria**: Monthly reporting shows processing time distribution. ≥ 98% of returns processed within 21 days. Processing time measured from receipt to refund issuance or assessment. Exceptions (identity verification holds, fraud flags) are tracked separately.

**TAX-PORT-COLLECT-003**
- **Requirement**: The system SHALL maintain a real-time queue of unprocessed returns with status, error categorization, and aging — with automated escalation for returns approaching SLA deadlines.
- **Rationale**: Queue management is essential for processing efficiency and SLA compliance.
- **Acceptance Criteria**: Queue dashboard shows all unprocessed returns with status and days in queue. Automated alerts when return approaches 18-day processing threshold. Error categories are standardized and allow filtering.

---

### 5.2 Fraud Detection and Prevention

**TAX-PORT-FRAUD-001**
- **Requirement**: The system SHALL implement multi-layer fraud detection that operates at: (a) account creation (identity fraud), (b) return submission (return fraud), (c) refund issuance (refund fraud), and (d) ongoing (anomaly detection on filed data).
- **Rationale**: Fraud at any stage has different characteristics and requires different controls. Defense in depth is required.
- **Acceptance Criteria**: Each of the four layers has documented detection logic, alert thresholds, and workflow for flagged cases. Each layer is independently auditable.

**TAX-PORT-FRAUD-002**
- **Requirement**: The system SHALL detect the following identity theft indicators and flag returns for review: SSN previously reported as deceased by SSA, SSN used on more than one return in the same tax year, address not matching SSA or prior IRS records without explanation, IP address geolocation inconsistent with taxpayer's known location without VPN explanation, and new account filing with immediate large refund claim.
- **Rationale**: These patterns are documented identity theft indicators. Each has high predictive value for fraudulent returns.
- **Acceptance Criteria**: Each indicator is implemented as a detection rule with documented false positive rates from historical data. Flagged returns are queued for review within 2 hours.

**TAX-PORT-FRAUD-003**
- **Requirement**: The system SHALL implement AI/ML-based anomaly detection on all returns, trained on historical data, that identifies statistically unusual patterns beyond rule-based detection — with a false positive rate not to exceed 2% of total returns.
- **Rationale**: Rule-based detection misses novel fraud patterns. ML-based detection can identify patterns not yet codified as rules. The false positive rate cap protects legitimate taxpayers.
- **Acceptance Criteria**: ML model is implemented and in production. Model performance is reported monthly: true positive rate, false positive rate, precision, recall. False positive rate is measured against adjudicated outcomes. If false positive rate exceeds 2% for any demographic group, the model is retrained or threshold adjusted within 30 days.

**TAX-PORT-FRAUD-004**
- **Requirement**: The fraud detection system SHALL be subject to demographic bias audits at least annually, ensuring that detection rates, false positive rates, and investigation rates do not vary significantly by race, ethnicity, or income level beyond what is explained by legitimate risk factors.
- **Rationale**: Biased fraud detection would constitute discriminatory enforcement. The audit requirement ensures systematic accountability.
- **Acceptance Criteria**: Annual bias audit conducted by an independent party with access to demographic data (where legally available) and detection outcomes. Audit report published publicly. Statistically significant disparities (p < 0.05) trigger remediation plan within 60 days.

**TAX-PORT-FRAUD-005**
- **Requirement**: The system SHALL cross-reference 1099-DA (cryptocurrency) reported transactions against Schedule D and Form 8949 reported gains/losses, flagging discrepancies that exceed $1,000 for review.
- **Rationale**: Cryptocurrency is a significant source of underreported income. Cross-referencing broker-reported data against return data closes this gap.
- **Acceptance Criteria**: Cross-reference runs for all returns with cryptocurrency activity. Discrepancies exceeding threshold are flagged with the specific 1099-DA amounts vs. reported amounts. False positive rate for this check documented.

**TAX-PORT-FRAUD-006**
- **Requirement**: The system SHALL cross-reference FATCA-reported foreign financial account data against returns, flagging taxpayers with foreign accounts above the reporting threshold who did not file required forms (FBAR, Form 8938).
- **Rationale**: FATCA data is collected but not systematically used to identify non-filers of required foreign account disclosures.
- **Acceptance Criteria**: FATCA cross-reference runs annually after information return deadline. Non-filer flags are generated for taxpayers meeting the threshold. Cases are queued for compliance action.

**TAX-PORT-FRAUD-007**
- **Requirement**: The fraud case management system SHALL track: case creation date, fraud indicator that triggered review, IRS analyst assigned, current status, communications with taxpayer, adjudication decision, and outcome (confirmed fraud, legitimate return).
- **Rationale**: Case management is required for fraud analytics and for protecting taxpayer rights during the fraud review process.
- **Acceptance Criteria**: Case management system captures all fields listed. Cases have documented SLAs: initial review within 5 business days, adjudication within 45 business days. Taxpayer is notified within 5 business days of flag and has access to case status.

**TAX-PORT-FRAUD-008**
- **Requirement**: Citizens SHALL be able to report suspected tax fraud via a secure portal intake form, with whistleblower protections noted, and SHALL receive a case tracking number.
- **Rationale**: Citizen tips are a significant source of fraud detection. A portal intake reduces barriers to reporting.
- **Acceptance Criteria**: Fraud reporting form is accessible without authentication (to protect anonymous reporters) and with authentication (to track follow-up). Form captures all fields required for Form 3949-A (Information Referral). Reporter receives a tracking number. Tips are routed to Criminal Investigation.

---

### 5.3 Audit and Enforcement

**TAX-PORT-AUDIT-001**
- **Requirement**: The system SHALL assign a risk score to every filed return using a documented multi-factor model, with the risk score used to inform (but not solely determine) audit selection.
- **Rationale**: Systematic risk scoring replaces arbitrary or biased audit selection. Documentation ensures the model can be audited for bias and accuracy.
- **Acceptance Criteria**: Risk score is assigned to 100% of returns. Model factors are documented (even if individual factor weights are not public, the categories are). Risk score is not the only factor in audit selection — human review of high-score returns is required before case opening.

**TAX-PORT-AUDIT-002**
- **Requirement**: The system SHALL provide an audit case management interface that tracks: case type, tax year(s) under examination, taxpayer contact information, assigned revenue agent, issue(s) under examination, document requests sent, documents received, timeline and deadlines, proposed adjustments, taxpayer responses, and case disposition.
- **Rationale**: Comprehensive case management is essential for fair and efficient audit administration.
- **Acceptance Criteria**: All fields listed are captured in the case management system. Deadlines generate automated alerts. Case timeline is visible to both the IRS and the taxpayer (for their own case) in the portal.

**TAX-PORT-AUDIT-003**
- **Requirement**: Document requests in the audit process SHALL be issued through the portal with online response capability, allowing taxpayers to upload requested documents electronically and receive secure acknowledgment of receipt.
- **Rationale**: Document exchange by mail is slow, creates risk of loss, and is inefficient for both sides. Electronic document exchange is standard in commercial legal and accounting practice.
- **Acceptance Criteria**: IDR (Information Document Request) is issued through the portal and appears in the taxpayer's account. Taxpayer can upload responsive documents directly. IRS acknowledges receipt. Document upload supports common formats (PDF, JPEG, TIFF) up to 100MB per document.

---

### 5.4 Taxpayer Account Management (Government View)

**TAX-PORT-GOV-001**
- **Requirement**: Authorized IRS personnel SHALL be able to view a complete taxpayer account including all returns, payments, assessments, adjustments, penalties, interest, notices, correspondence, authorizations, and case history — with full audit logging of all access.
- **Rationale**: IRS employees need a complete account view to provide accurate assistance and conduct enforcement. Fragmented systems are a primary cause of errors and delays.
- **Acceptance Criteria**: Unified account view displays all account data listed for any taxpayer TIN. Access is role-based and limited to information necessary for the employee's function. Every access is logged (see TAX-PORT-LOG requirements).

**TAX-PORT-GOV-002**
- **Requirement**: The system SHALL enforce strict role-based access control (RBAC) for IRS personnel, with access levels corresponding to job function — ensuring customer service representatives cannot access audit case details they are not assigned to, and audit staff cannot access collection case details they are not assigned to.
- **Rationale**: Principle of least privilege. IRS employees have significant power over taxpayer lives; access must be limited to what each job function requires.
- **Acceptance Criteria**: RBAC matrix is documented and implemented. Access control is tested during security assessment. Attempts to access beyond role permissions are logged as security events.

---

### 5.5 Data Analytics and Reporting

**TAX-PORT-COLLECT-004**
- **Requirement**: The system SHALL provide an internal analytics platform with: pre-built reports for standard IRS reporting requirements (SOI reports, enforcement statistics), ad-hoc query capability, and data export in CSV/JSON formats.
- **Rationale**: The IRS produces extensive statistical publications. The portal should generate the underlying data for these publications from operational data rather than requiring separate data collection.
- **Acceptance Criteria**: All fields required for IRS Statistics of Income (SOI) publications are available in the analytics platform. Analysts can run ad-hoc queries within their authorized data scope. Export complies with taxpayer privacy protections (aggregation/anonymization for any external use).

**TAX-PORT-COLLECT-005**
- **Requirement**: The system SHALL support policy impact modeling that allows analysts to model the revenue effect of proposed tax law changes based on current return data, with the ability to export results for Congressional Budget Office scoring.
- **Rationale**: Tax policy decisions require revenue impact estimates. The portal has the underlying data; modeling tools eliminate the need for separate data requests and reduce estimation errors.
- **Acceptance Criteria**: Policy modeling tool supports parameterized changes to at least: income brackets and rates, standard deduction amounts, itemized deduction caps, credit amounts and phase-outs, and corporate rate. Model generates estimated revenue impact with confidence interval. Methodology is documented and auditable.

---

### 5.6 Public Transparency Dashboard

**TAX-PORT-TRANS-001**
- **Requirement**: The system SHALL publish a publicly accessible, no-login-required transparency dashboard displaying aggregated, anonymized tax data including all metrics listed in TAX-PORT-TRANS-002 through TAX-PORT-TRANS-012.
- **Rationale**: The tax system is a fundamental public institution. Aggregated data about how it operates — including effective tax rates by income level and enforcement patterns — belongs to the public.
- **Acceptance Criteria**: Dashboard is publicly accessible at a well-known URL. No authentication required. Works on mobile devices. Meets WCAG 2.1 AA.

**TAX-PORT-TRANS-002**
- **Requirement**: The transparency dashboard SHALL publish total federal revenue collected, broken down by: individual income tax, payroll tax (employee and employer), corporate income tax, estate and gift tax, and excise taxes — updated monthly and available as annual historical time series.
- **Acceptance Criteria**: Revenue data matches Treasury Bureau of Fiscal Service public data. Updated by the 15th of the following month. Historical data available to at least 2000.

**TAX-PORT-TRANS-003**
- **Requirement**: The transparency dashboard SHALL publish effective federal income tax rates by income percentile: bottom 50%, 50th-90th percentile, 90th-99th percentile, top 1%, top 0.1%, top 0.01% — showing the mean and median effective rate for each group, updated annually after filing season close.
- **Rationale**: Public understanding of how progressively (or not) the tax system operates requires this data. It is derived from returns in aggregate and contains no individual data.
- **Acceptance Criteria**: Effective rate data published annually, no later than December 31 of the filing year. Methodology (how effective rate is calculated — total tax / total income, with income definition specified) is published alongside the data.

**TAX-PORT-TRANS-004**
- **Requirement**: The transparency dashboard SHALL publish corporate effective tax rates by NAICS industry sector, showing the statutory rate, effective rate, rate gap, and total taxes paid by sector.
- **Rationale**: Corporate tax avoidance varies dramatically by industry. This data enables public accountability.
- **Acceptance Criteria**: Corporate rate data published annually. Aggregation ensures no individual company data is disclosed (minimum cell size of 10 companies, or use of suppression rules consistent with SOI practices).

**TAX-PORT-TRANS-005**
- **Requirement**: The transparency dashboard SHALL publish the estimated annual cost of each major tax expenditure (deduction, exclusion, credit, or other preference) as estimated by the Joint Committee on Taxation or Treasury Office of Tax Analysis, updated annually with the President's budget.
- **Rationale**: Tax expenditures — often called "loopholes" — cost the federal government hundreds of billions annually. This cost is not transparent to the public. Publishing it enables informed democratic debate.
- **Acceptance Criteria**: Tax expenditure data matches JCT or Treasury OTA published estimates. Expenditures sorted by cost (largest first). Estimated cost displayed in absolute dollars and as percentage of total revenue.

**TAX-PORT-TRANS-006**
- **Requirement**: The transparency dashboard SHALL publish IRS enforcement statistics including: total audits conducted, audit rate by income bracket (under $25K, $25K-$75K, $75K-$200K, $200K-$1M, over $1M, corporations by size), additional tax recommended and collected, and year-over-year trends.
- **Rationale**: Congressional testimony has established that the IRS audits low-income EITC filers at higher rates than millionaires due to resource constraints. This data must be public to enable accountability.
- **Acceptance Criteria**: Enforcement statistics published annually, consistent with IRS Data Book. Audit rate by income bracket clearly labeled. Year-over-year comparison available.

**TAX-PORT-TRANS-007**
- **Requirement**: The transparency dashboard SHALL publish tax gap estimates by gap type (underreporting, underpayment, non-filing) and income source, based on IRS National Research Program data, updated when new NRP data is available.
- **Rationale**: The tax gap quantifies noncompliance. Its composition reveals where enforcement resources should be directed. This data is essential for public and congressional oversight.
- **Acceptance Criteria**: Tax gap data matches published IRS tax gap estimates. Uncertainty ranges are published. Source methodology is linked.

**TAX-PORT-TRANS-008**
- **Requirement**: All data on the public transparency dashboard SHALL be downloadable in machine-readable formats: CSV, JSON, and via a public API with documentation.
- **Rationale**: Researchers, journalists, and policymakers need machine-readable data for analysis. PDF-only publication limits use.
- **Acceptance Criteria**: Every dataset on the dashboard has a "Download CSV" and "Download JSON" button. API is documented at a public developer portal. API is versioned and backward-compatible.

---

### 5.7 Third-Party Data Integration

**TAX-PORT-3P-001**
- **Requirement**: The system SHALL provide a mandatory electronic filing interface for all employers and payers required to file information returns (W-2, 1099-series), with: batch upload capability (CSV, XML per IRS specifications), real-time validation, and confirmation of receipt.
- **Rationale**: The existing FIRE (Filing Information Returns Electronically) system is functional but dated. A modern interface reduces errors and improves data quality.
- **Acceptance Criteria**: Payer interface supports all information return types. Batch upload validated against current IRS schema before acceptance. Confirmation with record count provided. Error reports highlight specific records with issues.

**TAX-PORT-3P-002**
- **Requirement**: The system SHALL implement a state tax authority data exchange protocol that allows participating states to: receive federal return data relevant to state returns (with taxpayer consent), transmit state return data back to IRS for federal matching, and access the pre-population data pipeline for state information returns.
- **Rationale**: Federal-state tax integration reduces dual filing burden and improves compliance across both systems.
- **Acceptance Criteria**: State exchange API documented and available to all 50 states and DC. Data exchange requires taxpayer consent (obtained during filing). At least 10 states integrated in Phase 2.

**TAX-PORT-3P-003**
- **Requirement**: The system SHALL receive and process real-time death notifications from the Social Security Administration to prevent fraudulent returns filed using deceased individuals' SSNs.
- **Rationale**: Filing returns using deceased SSNs is a common fraud pattern. Real-time SSA death data integration closes this vulnerability.
- **Acceptance Criteria**: SSA death data feed is operational. New death records are flagged in the system within 24 hours of SSA notification. Flagged SSNs trigger enhanced verification for any return submission.

---

## 6. Non-Functional Requirements

### 6.1 Performance

**TAX-PORT-PERF-001**
- **Requirement**: Page load time for all citizen portal pages SHALL be ≤ 2 seconds at the 95th percentile under normal load conditions, measured from server response initiation to full page interactivity (Time to Interactive).
- **Acceptance Criteria**: Performance testing with simulated load confirms p95 TTI ≤ 2 seconds. Synthetic monitoring confirms this threshold in production during non-peak periods.

**TAX-PORT-PERF-002**
- **Requirement**: The system SHALL sustain a minimum of 10 million concurrent authenticated sessions during peak filing periods (April 13-15), with no degradation in p95 page load time below 4 seconds and no increase in error rate above 0.1%.
- **Rationale**: April 14-15 represents the peak of annual tax filing. The system must not fail precisely when it is most needed.
- **Acceptance Criteria**: Load testing at 10M concurrent sessions demonstrates compliance with performance thresholds. Load testing is conducted annually before filing season. Results are published internally.

**TAX-PORT-PERF-003**
- **Requirement**: System availability SHALL be ≥ 99.9% measured on a rolling 30-day basis, excluding pre-announced maintenance windows. During filing season (January 15 – April 18), no maintenance windows are permitted without emergency justification.
- **Acceptance Criteria**: Uptime monitoring publishes monthly availability reports. Filing season restrictions are enforced by policy with emergency exception process documented.

**TAX-PORT-PERF-004**
- **Requirement**: Return processing (from submission to processing complete status) SHALL complete within 24 hours for ≥ 98% of electronically filed returns.
- **Acceptance Criteria**: Processing time SLA is tracked in the government dashboard. Monthly reporting shows compliance rate. Exceptions are categorized (fraud hold, error, complexity).

---

### 6.2 Security

**TAX-PORT-SEC-001**
- **Requirement**: The system SHALL achieve and maintain FedRAMP High authorization before processing any production taxpayer data.
- **Rationale**: FedRAMP High is the appropriate authorization level for systems handling sensitive financial PII at federal scale.
- **Acceptance Criteria**: FedRAMP High Authorization to Operate (ATO) obtained from sponsoring agency. Annual assessment maintains authorization. Significant changes trigger re-assessment per FedRAMP continuous monitoring requirements.

**TAX-PORT-SEC-002**
- **Requirement**: The system SHALL implement a zero-trust architecture in which no user, device, or network connection is trusted by default, and all access is continuously verified based on identity, device posture, and context.
- **Rationale**: Traditional perimeter-based security is insufficient for a system of this scale and sensitivity. Zero-trust is the current federal standard.
- **Acceptance Criteria**: Zero-trust architecture is documented in the system security plan. CISA Zero Trust Maturity Model level ≥ 3 (Advanced) is demonstrated for all five pillars (identity, device, network, application, data).

**TAX-PORT-SEC-003**
- **Requirement**: All taxpayer data SHALL be encrypted at rest using AES-256 or equivalent, and all data in transit SHALL use TLS 1.3 minimum, with TLS 1.2 permitted only for legacy state system integrations with a documented deprecation timeline.
- **Acceptance Criteria**: Encryption at rest verified by FedRAMP assessor. TLS configuration verified by vulnerability scan showing no TLS < 1.2 and TLS 1.2 only where documented exception exists.

**TAX-PORT-SEC-004**
- **Requirement**: The citizen portal SHALL contain no third-party analytics, advertising, or tracking scripts. All JavaScript served on citizen portal pages SHALL be government-owned or open source with documented provenance.
- **Rationale**: Third-party scripts on tax portal pages would send citizen behavioral data to private companies. This is categorically prohibited.
- **Acceptance Criteria**: Content Security Policy headers are set to block all external JavaScript except explicitly allow-listed government and open-source sources. Quarterly CSP audit confirms no unauthorized third-party scripts. No Google Analytics, Meta Pixel, or similar.

**TAX-PORT-SEC-005**
- **Requirement**: The system SHALL conduct annual penetration testing by an independent, qualified third party, with findings published in summary form (without exploitable details) and remediation tracked publicly.
- **Acceptance Criteria**: Annual pentest report produced. Critical and high findings remediated within 30 and 90 days respectively. Summary published.

**TAX-PORT-SEC-006**
- **Requirement**: The system SHALL operate a public bug bounty program through which security researchers can report vulnerabilities, with defined scope, safe harbor provisions, and reward structure.
- **Rationale**: Bug bounty programs supplement internal testing and leverage the security research community. They are standard practice for high-value government systems.
- **Acceptance Criteria**: Bug bounty program is operational through an established platform (e.g., HackerOne, Bugcrowd). Scope and safe harbor provisions are public. Critical vulnerability response SLA ≤ 48 hours.

**TAX-PORT-SEC-007**
- **Requirement**: Taxpayer data SHALL be retained only as long as required by law (IRS records retention schedules) and SHALL be deleted or anonymized upon expiration, with deletion verified and logged.
- **Acceptance Criteria**: Data retention schedule is documented for all data types. Automated deletion runs on schedule. Deletion is logged in the audit system. Annual verification that deletion is occurring per schedule.

---

### 6.3 Privacy

**TAX-PORT-PRIV-001**
- **Requirement**: The system SHALL collect only the minimum taxpayer data necessary to fulfill tax administration functions. No additional data (behavioral profiles, device fingerprinting beyond session security needs, location data beyond IP geolocation for fraud detection) shall be collected.
- **Rationale**: Data minimization is a foundational privacy principle. Tax data is among the most sensitive categories of personal information.
- **Acceptance Criteria**: Data inventory documents every data element collected, its purpose, legal authority, and retention period. Annual review confirms no data collected beyond documented purposes.

**TAX-PORT-PRIV-002**
- **Requirement**: Taxpayer data SHALL NOT be used for any purpose other than tax administration as authorized by 26 U.S.C. § 6103, and SHALL NOT be shared with other government agencies except as specifically authorized by that statute.
- **Rationale**: Section 6103 is the statutory framework for protection of tax return information. The portal must enforce these protections technically.
- **Acceptance Criteria**: All data sharing events are logged and categorized by legal authority. Annual audit of data sharing confirms no sharing without documented § 6103 authority. Law enforcement requests are tracked and reported in annual transparency report.

**TAX-PORT-PRIV-003**
- **Requirement**: The system SHALL publish an annual transparency report disclosing: number of law enforcement requests for taxpayer data by requesting agency, number of requests complied with (fully and partially), number challenged, and any significant legal decisions regarding data access.
- **Rationale**: Taxpayers cannot trust a system that secretly shares their data with law enforcement. Transparency reporting is standard for any system holding sensitive personal data.
- **Acceptance Criteria**: Transparency report published annually by September 30. Data is reported at the level of specificity used by major technology companies (e.g., Google, Microsoft) in their transparency reports.

**TAX-PORT-PRIV-004**
- **Requirement**: Citizens SHALL be able to access a log showing every IRS system access of their account, including: date/time, accessing employee ID (role, not name), purpose category, and data accessed — directly within their portal account.
- **Rationale**: Citizens have a right to know who has accessed their most sensitive financial data. This is an accountability mechanism for government employees.
- **Acceptance Criteria**: Citizen-facing access log is available in the account. Log is updated within 24 hours of each access. Log is retained for 3 years in the citizen view.

---

### 6.4 Accessibility and Inclusion (Non-Functional)

**TAX-PORT-A11Y-009**
- **Requirement**: An independent third-party accessibility audit SHALL be conducted annually, covering all citizen-facing portal functions, with results published publicly and remediation tracked.
- **Acceptance Criteria**: Annual audit by IAAP-certified accessibility professional or equivalent firm. Audit report published. All critical and serious issues remediated within 90 days.

**TAX-PORT-A11Y-010**
- **Requirement**: The system SHALL be tested on devices that were released at least 5 years prior to deployment, on connections simulating 3G speeds (approximately 1.5 Mbps), to ensure usability for citizens with older technology.
- **Acceptance Criteria**: Compatibility testing matrix includes devices from 5 years prior. Performance testing at 1.5 Mbps connection speed shows functional usability (all core functions complete without errors).

---

### 6.5 Interoperability

**TAX-PORT-INTER-001**
- **Requirement**: The system SHALL expose a documented, versioned RESTful API for all data that can be shared with state tax authorities, financial institutions, and other authorized integrators — with OpenAPI specification published at a public developer portal.
- **Rationale**: API-first design is required for integration with state systems and financial institutions. Public documentation enables partners to build integrations without custom arrangements.
- **Acceptance Criteria**: API specification published at public developer portal in OpenAPI 3.0 format. All endpoints documented with examples. API versioning policy ensures backward compatibility for minimum 24 months.

**TAX-PORT-INTER-002**
- **Requirement**: Authentication for API integrations SHALL use OAuth 2.0 with PKCE for citizen-authorized integrations and mTLS for institutional integrations (state agencies, financial institutions).
- **Acceptance Criteria**: OAuth 2.0 PKCE implementation tested against RFC 7636. mTLS implemented for institutional endpoints. No custom authentication schemes.

**TAX-PORT-INTER-003**
- **Requirement**: Citizen data exports SHALL be available in at minimum: PDF (IRS-formatted, for human use), JSON (machine-readable, structured per documented schema), and XML (for legacy system compatibility).
- **Acceptance Criteria**: All three export formats available for complete return data and account history. Export formats documented. JSON schema published.

---

### 6.6 Auditability and Logging

**TAX-PORT-LOG-001**
- **Requirement**: The system SHALL maintain an immutable audit log for every access to taxpayer data by any government employee or system process, capturing: timestamp, accessing identity (user ID and role), taxpayer TIN accessed, specific data accessed or action taken, and stated purpose (from a standardized list).
- **Rationale**: IRS employees have historically accessed taxpayer data without authorization. An immutable audit log with purpose tracking is the primary accountability mechanism.
- **Acceptance Criteria**: Audit log captures all fields listed for 100% of accesses. Log is immutable (no delete, no update — append only). Cryptographic integrity mechanism (e.g., hash chaining or certificate-timestamping) prevents tampering. Log is retained for minimum 7 years.

**TAX-PORT-LOG-002**
- **Requirement**: The audit log SHALL be queryable by IRS internal audit staff and by the Treasury Inspector General for Tax Administration (TIGTA), with access controls appropriate to each role.
- **Acceptance Criteria**: TIGTA has independent query access to the full audit log without requiring IRS cooperation. IRS internal audit has access appropriate to their oversight function. Queries are themselves logged.

**TAX-PORT-LOG-003**
- **Requirement**: Unauthorized access to taxpayer data (access outside the employee's assigned cases or authorized function) SHALL trigger an automated alert to TIGTA and the employee's manager within 1 hour.
- **Rationale**: Prompt detection of unauthorized access limits the harm from insider threats.
- **Acceptance Criteria**: Automated anomaly detection on the audit log identifies out-of-role accesses. Alert delivery to TIGTA and manager within 1 hour is verified in testing. False positive rate for this alert is documented and reviewed quarterly.

---

### 6.7 Open Source and Vendor Independence

**TAX-PORT-OSS-001**
- **Requirement**: All citizen-facing application code SHALL be published as open source under a permissive or copyleft license (recommended: GPL-3.0 or Apache 2.0), with source code available on a government-managed public repository.
- **Rationale**: Open source citizen-facing code enables public security review, promotes trust, prevents vendor lock-in, and allows states and other countries to benefit from the investment.
- **Acceptance Criteria**: Source code repository is public before production launch of each major feature. All code is licensed under the declared open source license. Government retains copyright.

**TAX-PORT-OSS-002**
- **Requirement**: No single vendor SHALL provide more than 40% of total system components or services (by contract value or by criticality), and all vendor contracts SHALL include data portability requirements allowing transition without data loss.
- **Rationale**: Vendor concentration creates dependency risk and pricing power. Data portability prevents lock-in.
- **Acceptance Criteria**: Vendor concentration is tracked in the system architecture documentation. All contracts include data portability and transition assistance clauses. Annual review confirms compliance.

**TAX-PORT-OSS-003**
- **Requirement**: The fraud detection ML models SHALL be documented with sufficient detail that an independent technical expert can understand the model's inputs, logic, and outputs — enabling audit for bias, accuracy, and legal compliance.
- **Rationale**: "Black box" fraud detection algorithms that affect citizens' rights (delayed refunds, audit selection) cannot be justified. Explainability is a due process requirement.
- **Acceptance Criteria**: Model documentation includes: feature list and definitions, training data description, model type and hyperparameters, validation methodology, performance metrics, and known limitations. Documentation reviewed by independent ML expert annually.

---

## 7. Anti-Fraud Requirements

### 7.1 Fraud Taxonomy

**TAX-PORT-FRAUD-009**
- **Requirement**: The system SHALL maintain a documented fraud taxonomy covering at minimum: (a) identity theft fraud (stolen SSN used to file for refund), (b) refund fraud (legitimate filer manipulates return for larger refund), (c) business payroll fraud (fictitious employees, inflated payroll tax claims), (d) offshore evasion (unreported foreign income and accounts), (e) cryptocurrency underreporting, (f) abusive tax shelters and promoter schemes, and (g) syndicated conservation easement fraud — with detection requirements specific to each type.
- **Acceptance Criteria**: Fraud taxonomy is documented. Each category has at least one implemented detection mechanism. Detection rates by category are tracked.

### 7.2 Velocity and Pattern Checks

**TAX-PORT-FRAUD-010**
- **Requirement**: The system SHALL implement velocity checks that flag: (a) more than 5 returns filed from the same IP address in a 24-hour period, (b) refund amounts in the top 0.1% for income level without corresponding third-party data, (c) new account created and return filed within 24 hours claiming refund over $5,000, (d) same bank account used for refunds on more than 3 returns with different SSNs.
- **Rationale**: These patterns are associated with organized refund fraud and identity theft mills. Velocity checks at these thresholds catch organized fraud while having minimal impact on legitimate filers.
- **Acceptance Criteria**: Each velocity check is implemented with documented thresholds. Flagged returns are reviewed before refund issuance. False positive rates are tracked monthly.

### 7.3 Identity Verification Escalation

**TAX-PORT-FRAUD-011**
- **Requirement**: The system SHALL implement graduated identity verification escalation that does not create disparate impact on demographic groups. Escalation to enhanced verification SHALL be triggered by risk indicators, not by demographic characteristics, and SHALL be consistently applied across all demographic groups.
- **Rationale**: Enhanced identity verification is a legitimate anti-fraud tool but can create disparate impact if applied inconsistently. Systematic fairness auditing is required.
- **Acceptance Criteria**: Escalation triggers are documented and do not include demographic variables. Escalation rates by demographic group (where measurable) are tracked. Disparities exceeding 20% relative difference between comparable income groups trigger review.

### 7.4 Cross-Agency Data Matching

**TAX-PORT-FRAUD-012**
- **Requirement**: With appropriate legal authority, the system SHALL cross-reference IRS data with: (a) SSA wage records (to detect unreported wages), (b) DHS immigration records (to detect SSN eligibility issues), (c) State Department passport data (to detect unreported foreign presence), (d) FinCEN suspicious activity reports (for high-wealth taxpayers).
- **Rationale**: Cross-agency matching is one of the most effective fraud detection methods. Each match type addresses a documented evasion pattern.
- **Acceptance Criteria**: Each cross-reference has documented legal authority under § 6103 or other applicable statute. Cross-reference results are used for risk scoring, not automatic adjustment. False positive risk is documented for each match type.

---

## 8. Requirements for Closing Loopholes

### 8.1 Step-Up Basis Tracking

**TAX-PORT-LOOP-001**
- **Requirement**: When legislation eliminates or modifies the step-up in basis at death, the system SHALL track cost basis through death events by: receiving date-of-death valuations from estate returns (Form 706), updating basis records for inherited assets, and pre-populating the adjusted basis on Schedule D for heirs who subsequently sell inherited assets.
- **Rationale**: The step-up in basis eliminates capital gains tax on appreciation during the owner's lifetime. Tracking it through death events enables enforcement of any legislative modification.
- **Acceptance Criteria**: If legislation is enacted, basis tracking through death events is implemented within 2 tax years. Test scenarios with estate returns and subsequent heir sales verified for correct basis propagation.

### 8.2 Wash Sale Detection

**TAX-PORT-LOOP-002**
- **Requirement**: The system SHALL automatically detect wash sales across all brokerage accounts reported via 1099-B for a taxpayer, flagging disallowed losses that were not correctly reported by the broker, and adjusting the reported loss accordingly.
- **Rationale**: Brokers are required to track wash sales within a single account but not across accounts. Taxpayers with multiple accounts can exploit this gap. Cross-account detection closes it.
- **Acceptance Criteria**: Wash sale detection runs across all 1099-B records for a TIN within a tax year. Detected cross-account wash sales are flagged and presented to the taxpayer for correction. Adjusted basis is propagated to subsequent sale.

**TAX-PORT-LOOP-003**
- **Requirement**: When cryptocurrency wash sale rules are enacted, the system SHALL apply wash sale detection to 1099-DA reported cryptocurrency transactions using the same logic as TAX-PORT-LOOP-002.
- **Acceptance Criteria**: Cryptocurrency wash sale detection implemented within 1 tax year of rule enactment.

### 8.3 Related-Party Transaction Flagging

**TAX-PORT-LOOP-004**
- **Requirement**: The system SHALL flag for review transactions between related parties as disclosed on the return (controlled groups, family members, pass-through entities with common ownership), where pricing appears inconsistent with arm's-length standards based on disclosed amounts and industry benchmarks.
- **Rationale**: Related-party transactions at non-arm's-length prices are a significant income-shifting mechanism. Systematic flagging improves detection.
- **Acceptance Criteria**: Related-party relationships are identified from Schedule L, Form 5471, Form 8858, and other disclosures. Flagged transactions are routed to the examination queue. False positive rate for this flag documented.

### 8.4 Passive Activity Loss Enforcement

**TAX-PORT-LOOP-005**
- **Requirement**: The system SHALL track passive activity loss carryforwards across tax years and automatically enforce the at-risk rules and passive activity loss rules when calculating allowable deductions, pre-populating Form 8582 with prior-year carryforwards.
- **Rationale**: Passive activity loss rules (§ 469) are complex and commonly misapplied. Systematic tracking and enforcement reduces errors — both unintentional and intentional.
- **Acceptance Criteria**: Passive activity loss carryforward from prior years is pre-populated. Form 8582 calculations are verified against the complex rules. Test cases covering all PAL rule scenarios are included in the test suite.

### 8.5 Shell Company Disclosure Enforcement

**TAX-PORT-LOOP-006**
- **Requirement**: The system SHALL enforce disclosure requirements for beneficial ownership of domestic entities by: cross-referencing FinCEN Beneficial Ownership Information Report (BOIR) data with tax return entity filings, flagging entities required to file BOIRs that have not, and requiring disclosure of related-entity interests on returns where applicable.
- **Rationale**: Shell companies are the primary vehicle for tax avoidance and evasion. Integrating BOIR data with tax filing closes the gap between corporate transparency and tax reporting.
- **Acceptance Criteria**: BOIR data exchange with FinCEN is operational. Non-filer flags generated for required BOIR entities. Flagged returns are routed for compliance review.

---

## 9. Implementation Roadmap

### Phase 1 — Foundation (Months 1–12)

**Objective**: Establish core infrastructure and serve the majority of simple filers.

**Deliverables**:
- Authentication infrastructure (Login.gov integration, MFA, IAL2 identity proofing)
- Pre-population of W-2, 1099-INT, 1099-DIV, and 1099-R data
- Form 1040 filing with standard deduction (Schedules A, B)
- Direct deposit refund processing
- ACH payment for balance-due returns
- Basic installment agreement application
- Account history (returns, payments)
- Email notifications (submission confirmation, refund status)
- English-language portal
- Basic government processing dashboard
- FedRAMP High authorization process initiated

**Success Gate**: 5 million returns successfully filed through the portal in Year 1 filing season.

### Phase 2 — Full Filing Support (Months 13–24)

**Objective**: Support all individual filing situations and integrate tax professionals.

**Deliverables**:
- All individual schedules and forms (C, D, E, F, SE, and all associated forms)
- K-1 import from partnership and S-corp returns
- Tax professional portal (PTIN verification, client management, batch filing)
- Electronic Form 2848/8821
- State integration API (10 states)
- Full multilingual support (12 languages)
- Fraud detection v1 (rule-based, identity theft, refund fraud)
- Secure two-way messaging with IRS
- Notice portal (display and online response)
- VITA site integration
- FedRAMP High authorization obtained

**Success Gate**: 30 million returns filed through the portal in Year 2. Tax professional adoption ≥ 20% of professional-filed returns.

### Phase 3 — Advanced Features (Months 25–36)

**Objective**: Full ecosystem integration, transparency, and advanced fraud detection.

**Deliverables**:
- All 50 states + DC integration
- ML-based fraud detection (with bias audit)
- Public transparency dashboard (all metrics from Section 5.6)
- Policy impact modeling tools
- Cryptocurrency integration (1099-DA processing)
- FATCA cross-reference
- What-if scenario modeling
- Full audit case management
- OIC application portal
- Phase 1 of loophole enforcement (wash sales, PAL tracking)

**Success Gate**: 60 million returns filed through the portal. Public transparency dashboard launched and publicly accessible.

### Phase 4 — Continuous Improvement (Ongoing from Month 37)

**Objective**: Continuous improvement, legislative adaptation, and expanding adoption.

**Activities**:
- Annual ML model retraining and bias audit
- Legislative change integration within 1 filing season of enactment
- Accessibility enhancements based on annual audit
- Feedback-driven UX improvements (user satisfaction surveys, usability testing)
- Additional loophole enforcement as legislation is enacted
- Expansion of state integrations and data exchange
- International tax complexity (GILTI, FDII, BEAT for large filers)

---

## 10. Compliance and Legal Requirements

| Requirement | Description | Applicability |
|-------------|-------------|---------------|
| Internal Revenue Code (Title 26) | Primary authority for all tax administration functions | All system functions |
| Privacy Act of 1974 (5 U.S.C. § 552a) | Governs collection, maintenance, use of records on individuals | All PII collection and use |
| 26 U.S.C. § 6103 | Confidentiality and disclosure of returns and return information | All taxpayer data access and sharing |
| 26 U.S.C. § 7216 | Prohibition on disclosure of return information by preparers | Tax professional access |
| E-Government Act of 2002 | E-filing authorization, electronic records | E-file, e-signature |
| Section 508, Rehabilitation Act | Accessibility requirements for federal technology | Citizen portal |
| FISMA (Federal Information Security Modernization Act) | Security requirements for federal systems | All system components |
| NIST SP 800-63 Digital Identity Guidelines | Identity proofing and authentication requirements | Authentication, IAL2 |
| NIST SP 800-53 Security Controls | Security control baseline for federal systems | Security architecture |
| FedRAMP High | Cloud security authorization program | Cloud infrastructure |
| OMB Circular A-130 | Managing Information as a Strategic Resource | Data governance |
| IRS Publication 1075 | Tax Information Security Guidelines for Federal, State and Local Agencies | Data handling |
| WCAG 2.1 | Web Content Accessibility Guidelines | Citizen portal |
| ADA Title II | Accessibility for government services | Citizen portal |
| Paperwork Reduction Act | Requirements for information collected from public | Forms and data collection |

---

## 11. Success Metrics

### 11.1 Adoption

**TAX-PORT-METRIC-001**
**Metric**: Percentage of individual federal income tax returns filed through the government portal.
**Baseline**: 0% (Year 0, system not yet deployed).
**Targets**:
- Year 1: 5% (approximately 7 million returns)
- Year 2: 20% (approximately 28 million returns)
- Year 3: 45% (approximately 63 million returns)
- Year 5: 80% (approximately 112 million returns)

**Measurement**: IRS e-file statistics, disaggregated by filing method.

### 11.2 Filing Time

**TAX-PORT-METRIC-002**
**Metric**: Median time from authentication to submission for W-2-only filers with standard deduction.
**Target**: ≤ 15 minutes.
**Measurement**: In-session timing from authentication event to submission event, sampled from consenting users. Reported annually.

**TAX-PORT-METRIC-003**
**Metric**: Median time for Schedule C filers with standard deduction.
**Target**: ≤ 45 minutes.

**TAX-PORT-METRIC-004**
**Metric**: Median time for filers with Schedule D, E, or itemized deductions.
**Target**: ≤ 90 minutes.

### 11.3 Cost Efficiency

**TAX-PORT-METRIC-005**
**Metric**: Cost per return processed through the government portal (total portal operating cost / returns filed).
**Target**: ≤ $5.00 per return by Year 3 (compared to estimated $40 per return for current paper and assisted filing).
**Measurement**: Annual cost accounting report from IRS CIO office.

### 11.4 Fraud

**TAX-PORT-METRIC-006**
**Metric**: Identity theft fraud rate (returns flagged as identity theft confirmed after investigation / total returns).
**Target**: ≤ 0.5% (improvement from current baseline).
**Measurement**: Fraud investigation outcomes reported quarterly.

**TAX-PORT-METRIC-007**
**Metric**: Fraud detection false positive rate (legitimate returns flagged for fraud review / total returns).
**Target**: ≤ 2%.
**Measurement**: Adjudication outcomes for flagged returns. Reported monthly during filing season.

**TAX-PORT-METRIC-008**
**Metric**: Refund fraud loss amount (dollars paid on fraudulent refund claims).
**Target**: 50% reduction from pre-portal baseline by Year 3.
**Measurement**: Fraud investigation financial outcomes.

### 11.5 Processing Speed

**TAX-PORT-METRIC-009**
**Metric**: Median time from return submission to refund deposit (for direct deposit returns with no fraud flag).
**Target**: ≤ 3 business days.
**Measurement**: Timestamp from submission acknowledgment to ACH settlement. Reported monthly.

**TAX-PORT-METRIC-010**
**Metric**: Percentage of returns processed within 21 calendar days.
**Target**: ≥ 98%.
**Measurement**: Processing queue data.

### 11.6 System Reliability

**TAX-PORT-METRIC-011**
**Metric**: System availability (uptime) measured monthly.
**Target**: ≥ 99.9% (≤ 43.8 minutes downtime per month).
**Measurement**: Synthetic monitoring from multiple geographic locations.

**TAX-PORT-METRIC-012**
**Metric**: System availability during peak filing days (April 13-18).
**Target**: ≥ 99.99% (≤ 52 seconds downtime for the period).
**Measurement**: Same as above with heightened monitoring.

### 11.7 Accessibility

**TAX-PORT-METRIC-013**
**Metric**: WCAG 2.1 AA compliance rate (percentage of WCAG 2.1 AA criteria passing in annual independent audit).
**Target**: 100% pass rate for AA, ≥ 80% for AAA on critical flows.
**Measurement**: Annual third-party accessibility audit report.

**TAX-PORT-METRIC-014**
**Metric**: Percentage of users self-reporting they were able to complete filing without assistance.
**Target**: ≥ 90% overall, ≥ 85% for non-English speakers, ≥ 85% for users age 65+.
**Measurement**: Post-filing survey (opt-in).

### 11.8 User Satisfaction

**TAX-PORT-METRIC-015**
**Metric**: User satisfaction rating (CSAT or equivalent) from post-filing survey.
**Target**: ≥ 85% satisfied or very satisfied.
**Measurement**: Post-filing survey, sample of ≥ 100,000 filers annually.

**TAX-PORT-METRIC-016**
**Metric**: Net Promoter Score (NPS) for the portal.
**Target**: ≥ 50 (compared to commercial tax software average of approximately 20-30).
**Measurement**: NPS survey embedded in post-filing confirmation page.

### 11.9 Tax Gap

**TAX-PORT-METRIC-017**
**Metric**: Estimated tax gap reduction attributable to portal-enabled enforcement improvements (pre-population, cross-referencing, fraud detection).
**Target**: ≥ 10% reduction in the voluntary compliance gap within 5 years of full deployment.
**Measurement**: IRS National Research Program estimates, with methodology crediting portal-attributable changes. Estimated baseline required before deployment.

### 11.10 Transparency

**TAX-PORT-METRIC-018**
**Metric**: Percentage of transparency dashboard datasets updated within their required frequency.
**Target**: 100% of datasets updated on schedule.
**Measurement**: Dashboard metadata showing last update timestamps compared to required schedule.

---

*End of Document*

**Revision History**

| Version | Date | Author | Changes |
|---------|------|--------|---------|
| 1.0 | 2026-03-12 | Tax Reform Working Group | Initial release |

