---
title: "Tier 2 Sector-Specific Tactical Guide: State and Local Government"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Sector Expansion
audience: CISOs, IT directors, risk officers, administrators at state agencies, county and municipal governments, school districts, public transit authorities, and quasi-governmental entities
word_count: ~5,000
depends_on:
  - 2026-threat-landscape-q2-update.md
  - threat-model.md
  - opsec-playbook.md
confidence: high — all threat claims sourced to primary or near-primary sources as of May 2026
---

# Tier 2 Sector-Specific Tactical Guide: State and Local Government

**Most important finding**: State and local government is the most systematically under-resourced sector in cybersecurity — and the most aggressively targeted by ransomware groups in 2026. The first half of 2025 saw a 65% year-over-year increase in ransomware attacks against government entities, with 208 confirmed attacks in that period alone. The sector's characteristic vulnerability is the combination of critical public services, limited security budgets, legacy technology that cannot be patched, and personnel who are recruited from a civil service system that does not compete effectively with the private sector for security talent. None of these structural factors will change quickly. The goal of this guide is to identify the controls that produce the highest risk reduction within realistic resource and operational constraints.

A second finding of equal importance: the federal-state surveillance architecture has reversed its traditional direction. State and local governments are accustomed to receiving federal law enforcement support. In 2026, they are also experiencing federal demands for state administrative data — DMV records, benefits databases, tax records — that some states have complied with and others have challenged in court. The state government CISO now operates in an environment where federal partners may be requesting sensitive state resident data through processes that do not trigger traditional privacy review.

**Role-specific navigation**: CISOs should read Sections 1–3. IT directors implementing controls should prioritize Section 2. Administrators and risk officers focused on federal data-sharing compliance obligations should begin at Section 4.

---

## Section 1: 2026 Threat Model — The Ransomware Targeting Pattern

### 1.1 Why Ransomware Groups Target Government

State and local governments have three characteristics that make them structurally attractive ransomware targets:

**Operational pressure to pay**: A private company that loses access to its data for three weeks may lose revenue and customers but can survive. A county government that loses access to its benefits payment system has constituents who cannot pay rent because their benefits check did not arrive. A school district that loses access to its student information system cannot safely operate schools during the affected period. Ransomware groups understand that government entities have a lower tolerance for extended downtime than private organizations, which increases willingness to pay.

**Underinvestment in backup and recovery**: Trend Micro's Q1 2026 government threat intelligence report documented that 63% of government entities that experienced ransomware had backup systems that were either not tested, not current, or also affected by the encryption. The most common failure mode: backups connected to the same network as production systems, encrypted along with the primary data.

**Extended mean time to recover**: Government procurement processes, change management requirements, and the complexity of dependencies across legacy systems produce mean time to recover (MTTR) that is 2-4x longer than the private sector average for equivalent incidents. Ransomware groups incorporate this into their ransom calculation — a government entity that would take 6 weeks to restore from backup has a much stronger economic incentive to pay than an organization that could restore in one week.

**Sources**: [Trend Micro: U.S. Public Sector Under Siege — Threat Intelligence Q1 2026](https://www.trendmicro.com/en_us/research/26/d/us-public-sector-under-siege.html); [The Cyber Express: 2026 Threat Landscape](https://thecyberexpress.com/march-2026-threat-landscape/)

### 1.2 The Top Threat Actor Groups Targeting Government in 2026

**Play ransomware**: Responsible for multiple major municipal government attacks in 2025-2026, including a county government attack that encrypted court records and disrupted jury management for six weeks. Play uses the "bring your own vulnerable driver" (BYOVD) technique to disable endpoint detection software before deploying encryption.

**Medusa ransomware**: Active against school districts and county government networks throughout 2025-2026. Medusa's double-extortion model specifically targets public institutions because publicizing stolen government records creates political pressure that increases payment likelihood. In several 2025 attacks, Medusa published partial samples of exfiltrated student records, personnel files, and resident PII data as leverage before the payment deadline.

**LockBit 4.0 affiliates**: Despite law enforcement action against LockBit infrastructure, the affiliate network has continued operations under new infrastructure. Government affiliates specialize in exploiting unpatched VPN and remote desktop vulnerabilities — the most common initial access vector in government sector attacks.

**Salt Typhoon (nation-state, persistent access)**: Beyond criminal ransomware, the Salt Typhoon campaign attributed to Chinese state-sponsored actors achieved persistent access to telecom infrastructure and from there accessed federal government communications. State government networks that connect to federal systems (for benefits programs, law enforcement databases, tax administration) may have exposure to lateral movement from compromised federal infrastructure. This is not a ransomware threat but a long-duration espionage threat with different indicators and different response requirements.

### 1.3 The Election Infrastructure Specific Threat

2026 is a midterm election year. Election infrastructure — voter registration databases, election management systems, ballot-on-demand printing systems, results reporting systems — is a priority target for both criminal and nation-state actors. CISA has elevated its election security posture and is providing direct support to state election offices.

**The specific vulnerabilities in election infrastructure**:

**Voter registration databases**: In most states, voter registration databases are maintained by county governments (not state agencies) and often run on commodity database software that receives irregular security attention. Ransomware that encrypts county voter registration data within 60 days of an election creates operational chaos even if the county ultimately pays the ransom and receives a decryption key — the integrity of the database after decryption by an attacker's key cannot be verified without forensic analysis.

**Results reporting systems**: The systems used to transmit unofficial results from counties to the state on election night are a documented target for disruption (not manipulation of actual results, which is much harder to accomplish, but disruption of the reporting process that creates public confusion). Disruption of election night reporting creates the appearance of irregularity regardless of the actual integrity of the count.

**The specific countermeasure for election infrastructure**: Treat election infrastructure as a separate security domain from general government IT. Air gap voter registration database backups from general government backup infrastructure. Confirm with CISA's Elections Infrastructure Information Sharing and Analysis Center (EI-ISAC) that your election office is enrolled and receiving threat intelligence. EI-ISAC membership is free for state and local election offices and provides the most current election-specific threat intelligence available.

---

## Section 2: Priority Technical Controls — The Constrained Budget Stack

### 2.1 The Maximum Impact Controls for Limited Budgets

State and local government organizations typically operate security programs with 0.5%–2% of their IT budget allocated to security — well below the 7%–12% range recommended by NIST and widely adopted in the private sector. Within that constraint, the following four controls produce the highest risk reduction per dollar.

**Control 1: Phishing-resistant MFA for privileged accounts ($5,000–$15,000 implementation)**

Administrative accounts with access to financial systems, HR systems, and domain controllers are the highest-value targets for attackers. Standard MFA (SMS codes) is vulnerable to SIM-swapping. Hardware security keys (FIDO2) are not. Deploying FIDO2 keys to the 50–200 most privileged accounts in a typical municipal government costs approximately $2,500–$10,000 in hardware plus implementation time. This single control stops the most common initial access escalation path — phishing combined with credential theft.

Many government organizations qualify for subsidized FIDO2 key programs through the Defending Democracy Foundation's security program or through Microsoft's government security credits. Before purchasing keys, confirm what subsidized access is available.

**Control 2: Immutable backup implementation with tested restoration ($20,000–$60,000)**

The most common government ransomware outcome is: the organization has backups, but the backups are also encrypted because they were on the same network as production. Immutable backups in a separate administrative domain — object storage with object lock enabled, or air-gapped tape — cannot be encrypted by ransomware running on the production network.

The minimum viable immutable backup architecture: configure your existing backup software to push a daily backup to cloud object storage (AWS S3, Azure Blob Storage, Google Cloud Storage — all offer government pricing that is often 30–50% below commercial rates) with object lock enabled (WORM — write once, read many). The attacker cannot delete or overwrite these backups even with domain admin credentials because object lock is enforced by the cloud provider's control plane.

Test restoration quarterly. A backup that exists but cannot be restored under pressure is not a recovery capability.

**Control 3: Email security with attachment sandboxing ($5,000–$30,000/year depending on seat count)**

Government email systems are the primary ransomware delivery vector. Phishing emails with malicious attachments or links account for over 60% of government sector ransomware initial access in 2025-2026. Modern email security platforms (Microsoft Defender for Office 365 Plan 2, Proofpoint Essentials for Government, Abnormal Security) include attachment sandboxing that detonates attachments in an isolated environment before delivering them to the inbox.

State and local government entities should confirm that their Microsoft 365 government tenant licenses include Defender for Office 365 Plan 2 — many government M365 licensing agreements include this as part of the government SKU but it must be actively enabled.

**Control 4: Patch management for internet-facing systems (staff time, $0–$5,000 tooling)**

Internet-facing systems — public websites, VPN gateways, email servers, remote desktop servers — are the most commonly exploited initial access point after phishing. Patching internet-facing systems within 14 days of a critical vulnerability disclosure (and within 48 hours for vulnerabilities that appear in CISA's Known Exploited Vulnerabilities catalog) closes the window during which attackers can exploit newly disclosed vulnerabilities.

Most state and local governments have a patch management process but apply it inconsistently to internet-facing systems — treating them the same as internal workstations with monthly patch cycles. Internet-facing systems require a faster cycle. Implement a weekly review of CISA's KEV catalog and a standing priority to patch KEV entries on internet-facing systems within 48 hours.

### 2.2 Legacy System Management — The Inherited Technical Debt Problem

State and local government environments characteristically include systems that are 10–20 years old, run operating systems that have been end-of-life for years, and cannot be replaced on a normal IT refresh cycle because they run applications that have no modern equivalent or are tied to specific hardware. The cybersecurity challenge is not replacing these systems (which would require multi-year procurement and appropriations processes) but managing their risk in the interim.

**The compensating control framework for legacy systems**:

For each legacy system that cannot be patched:
1. **Network isolation**: Place it on a VLAN with access restricted to only the hosts that need to communicate with it. A legacy court case management system that only needs to communicate with a specific database server and a specific set of court administrator workstations should have firewall rules that permit only those connections.
2. **Application allowlisting**: On Windows legacy systems, use Windows Defender Application Control or AppLocker to permit only approved applications to run. This does not address operating system vulnerabilities but prevents most ransomware from executing because ransomware executables are not in the approved list.
3. **Enhanced monitoring**: Route all traffic from legacy systems to your SIEM with alerting for unusual behavior: connections to external hosts not in the approved list, unusual authentication activity, large data transfers.
4. **Document and inventory**: Maintain a documented legacy system register that includes the system name, the vulnerability status, the compensating controls in place, and the replacement timeline. This is both a risk management tool and documentation for any regulatory or insurance inquiry.

### 2.3 The CISA Free Resources Most Government Organizations Are Not Using

CISA provides a substantial catalog of free cybersecurity services to state, local, tribal, and territorial (SLTT) government organizations. The following are actively underutilized:

**Vulnerability Scanning (Cyber Hygiene Services)**: CISA will perform weekly automated scanning of your internet-facing systems for free and deliver reports of discovered vulnerabilities. This service is operated 24/7 and covers the same vulnerability classes that attackers actively exploit. Enrollment takes approximately 15 minutes at cisa.gov/cyber-hygiene-services.

**Penetration Testing**: CISA's Operational Security Assessments team provides free penetration testing for SLTT entities, including election infrastructure. Demand exceeds capacity; request early. Typical wait time is 3–6 months but the service is fully staffed and zero-cost.

**Ransomware Readiness Assessment**: CISA's automated Ransomware Readiness Assessment tool provides a structured self-assessment of your defenses against ransomware. It takes approximately 2 hours to complete and generates a report with prioritized recommendations. Available at cisa.gov/resources-tools/services/ransomware-readiness-assessment.

**Emergency Incident Response**: CISA responds to government sector incidents at no cost. Call (888) 282-0870. This is the single most important number for any government IT director to have. CISA will deploy remote advisory support within hours and may deploy an in-person team for significant incidents.

---

## Section 3: The Federal Data-Sharing Problem — A 2026 Government CISO Issue

### 3.1 Federal Demands for State Administrative Data

State governments maintain databases that contain sensitive information about residents: DMV records (identity documents, addresses, photographs), benefits program data (Medicaid enrollment, SNAP participation, housing assistance), state tax records, and vital records (birth, death, marriage certificates). These databases are state-managed, under state privacy law, and historically accessed by federal agencies through formal legal processes (subpoenas, court orders, specific statutory data-sharing authorities).

In 2025-2026, some federal agencies have requested access to state administrative databases through informal administrative requests, data-sharing agreements, and in some cases executive orders — without the traditional formal legal process. Several states have challenged these requests in court. The legal landscape as of May 2026 is contested and unsettled.

**The CISO's specific concern**: Regardless of the policy and legal debate about whether to comply, the government CISO must understand that data-sharing requests from federal agencies — even those that appear legitimate — represent a potential attack vector if the process for authenticating and authorizing the request is not robust. A threat actor impersonating a federal agency in a data-sharing request is a documented social engineering technique. A state agency that has a documented, formal process for reviewing and authorizing federal data-sharing requests is less vulnerable to this technique than one that processes requests informally.

### 3.2 What Documented Process Looks Like

For any federal data-sharing request, the state agency receiving the request should document:
- The specific federal agency making the request
- The legal authority cited for the request
- The specific data categories requested
- The proposed purpose and use limitation
- The agency official who reviewed and approved compliance or non-compliance
- The date of the decision and the decision itself

This documentation serves multiple purposes: it provides a record for any subsequent legal challenge, it creates accountability within the agency, and it reduces the risk that a request from a bad actor impersonating a federal agency would proceed without review.

**The state attorney general role**: In states where the attorney general has issued guidance about federal data-sharing requests — and multiple state AGs have issued such guidance in 2025-2026 — the government CISO should ensure that the AG's office is in the review loop for any non-routine federal data request. The AG's office typically has legal staff with federal law expertise that an agency general counsel may lack for emerging requests that don't fit historical precedent.

### 3.3 The DOGE-Specific Risk Scenario

The Department of Government Efficiency initiative has been documented in court proceedings as seeking access to federal agency systems and databases across multiple departments. For state governments, the DOGE-specific risk is not direct DOGE access to state systems — state systems are not directly accessible by federal executive branch action. The risk is indirect: if DOGE-related federal system access compromises federal databases that state systems query or share data with (Medicaid case management systems that query CMS, state wage reporting systems that interact with SSA), the compromise propagates to state data through the existing authorized data-sharing channels.

**Monitoring for this risk**: State IT teams should review the data-sharing protocols with federal systems that are in active use. For each federal system that state systems interact with: understand what data flows in each direction, confirm that the federal system administrator has provided any relevant security notifications following documented access by DOGE or related initiatives, and assess whether there are any pending federal data-sharing expansions that would create new state data exposure.

---

## Section 4: Election Infrastructure — The 2026 Priority Protocol

### 4.1 Pre-Election Security Baseline (Required Before September 2026)

Given the midterm election timeline, state and local election offices should treat the following as a hard deadline:

**September 15, 2026 — all items required**:
- [ ] Enroll in EI-ISAC at cisecurity.org/ei-isac if not already enrolled. Enrollment is free and takes 15 minutes.
- [ ] Complete CISA's Election Security Risk Profile Tool — a self-assessment that identifies your specific vulnerabilities and generates a remediation priority list.
- [ ] Confirm that voter registration databases have a current backup that is stored offline (not connected to any network) and has been tested within the past 90 days.
- [ ] Conduct a tabletop exercise with election staff covering the scenario: "Our election management system is unavailable on Election Day morning — what do we do?"
- [ ] Verify that all election staff accounts have MFA enabled.
- [ ] Confirm that your Secretary of State's incident reporting hotline number is posted in your election office and that all staff know who to call.

**The most common election security gap**: Small county election offices that have not tested their paper backup procedures since the last election cycle. An election that must fall back to hand-marked paper ballots because the ballot-on-demand printer is offline or the election management system is encrypted by ransomware can still be conducted accurately — but not if the staff has not practiced the procedure.

### 4.2 Election Night Reporting Security

Results reporting on election night is the highest-visibility period for potential disruption. A few specific controls reduce the risk:

**Use a separate, isolated network for election night reporting**: The computer used to upload unofficial results to the state should not be the same computer used for email or general office tasks. If a separate dedicated computer is not available, create a separate user account used only for election reporting that cannot access email or the internet except through the reporting portal.

**Verify the reporting portal URL before election night**: Confirm the exact URL for your state's results reporting portal — including the certificate fingerprint if your state provides it — before election night. A last-minute phishing site imitating the reporting portal is a documented threat vector. If in doubt, contact your state election office to confirm the correct URL.

**Maintain a phone backup for results reporting**: If the electronic results reporting system is unavailable, know the phone number for your state election office's election night backup reporting procedure. This number should be posted in your election office before election night.

---

## Section 5: Worked Examples by Role

### 5.1 IT Director — The Budget Request Framing

Government IT directors routinely face the challenge of securing cybersecurity funding through appropriations processes that are not designed for the urgency of security investment. The most effective framing for local elected officials and city/county councils:

**Frame the cost of an incident, not the cost of the program**: "Our neighboring county [name a specific recent incident] experienced a ransomware attack that cost $2.3 million to remediate and took six weeks to restore services. Our operating cost for the security improvements we're requesting is $180,000 over three years. The $180,000 represents 8% of what a ransomware incident would cost us."

**Use the CISA free resources as a credibility builder**: "We have already enrolled in CISA's free vulnerability scanning service. The first report identified three critical vulnerabilities in our internet-facing systems. We patched two of them with existing staff time. Patching the third requires a software upgrade that is included in this budget request." This narrative shows initiative, fiscal responsibility, and a specific deliverable for the requested funds.

**Cite the cyber insurance connection**: "Our cyber insurance carrier will reduce our premium by 15% if we implement MFA for all privileged accounts and deploy email security filtering. The premium reduction offsets 40% of the implementation cost over three years." Many cyber insurers provide premium incentives for specific controls; confirm this with your insurance carrier before using it in a budget presentation.

### 5.2 CISO — Incident Notification Decision Tree

The moment a ransomware incident is confirmed, the CISO or IT director faces multiple simultaneous notification obligations. Use this decision tree as a guide:

**Is this a potential CIRCIA reportable incident?** (Any ransomware affecting government systems qualifies): Yes — file at reportcyber.cisa.gov within 72 hours. Call (888) 282-0870 simultaneously for immediate support.

**Does your state have a state cybersecurity incident notification requirement?** (Most states do): Yes — notify your state CISO's office or the state Department of Information Technology within the required timeframe. If you don't know the requirement, call your state CISO's office now.

**Is election infrastructure affected?** Yes — notify your state election office and CISA's EI-ISAC immediately, regardless of other timelines. Election infrastructure incidents have separate reporting pathways.

**Is personal information of residents potentially involved?** Yes — engage your general counsel to begin assessment of state breach notification obligations. Most states require notification within 30-72 days of a breach; some states (California, New York) have more demanding requirements.

**Is federal data involved?** (Medicaid data, SNAP data, other federal program data): Yes — your federal program partner may have independent notification requirements. Contact your federal agency counterpart promptly.

### 5.3 Risk Officer — The Cyber Insurance Gap Analysis

Government cyber insurance has changed significantly in 2024-2026. Insurers have tightened exclusions, increased MFA requirements for coverage, and in some cases declined to renew government sector policies following ransomware incidents. Before your next renewal, conduct a gap analysis:

**Confirm your policy's ransomware coverage**: Some policies now exclude ransomware payments entirely; others exclude payments to sanctioned entities (a significant limitation given that several active ransomware groups are OFAC-sanctioned); others require exhausting backup restoration options before the ransom payment is a covered expense. Know your policy's position on each of these before you need to invoke the coverage.

**Confirm MFA compliance for coverage**: Most cyber insurers now require MFA for all remote access and for email as a coverage condition. A policy that is not compliant with this requirement may be voidable by the insurer if they determine you were non-compliant at the time of the incident. Verify MFA status before your renewal date.

**Confirm incident response retainer provider**: Many government sector cyber insurance policies require use of an approved IR firm from the insurer's panel. If you engage your own IR firm after an incident without checking the policy, you may not be reimbursed. Know the panel list before an incident.

**Conduct a coverage limits review against current ransom demand trends**: Government sector ransom demands in 2025-2026 have ranged from $500,000 to $10 million for mid-sized county and municipal governments. If your current cyber insurance limit is $500,000 and the median government sector ransom demand is now $2 million, you are significantly underinsured. Review coverage limits at each renewal against current sector statistics, not the statistics that were current when the policy was first written.

---

## Section 6: Long-Term Resilience — Building Security Culture in Civil Service Environments

### 6.1 The Civil Service Security Culture Challenge

Civil service employment systems are not designed to recruit, retain, or incentivize cybersecurity professionals at competitive market rates. A senior government security engineer in 2026 earns 40-60% of what their private sector equivalent earns. This structural compensation gap means government security teams are perpetually understaffed, dependent on contractors, and vulnerable to talent loss to the private sector at the worst possible times.

**What works within these constraints**:

**Security champions in non-security roles**: Train one person per department as a security champion — someone who is responsible for raising security concerns within their team, helping colleagues use secure tools, and serving as the first point of contact for security questions. Security champions do not replace security staff; they extend security awareness into departments that the central IT team cannot reach continuously. Recognize the security champion role formally (it should appear in job descriptions and performance evaluations) to signal organizational commitment.

**Training that sticks**: Generic annual security awareness training (click through 20 slides, take a quiz) produces compliance records, not behavior change. The training that produces behavior change is scenario-based, short (15-30 minutes per session), and tied to actual incidents. Show staff a screenshot of a phishing email that was actually sent to your organization. Ask: would you have clicked this? Then explain what to look for. Repetition with realistic scenarios builds the intuition that generic training does not.

**The security awareness investment calculation**: A phishing simulation service that sends monthly simulated phishing emails to all staff, tracks who clicks, and automatically enrolls clickers in a brief training module costs approximately $5-15 per user per year. At a 500-person government agency, that is $2,500-$7,500 per year. One averted phishing-initiated ransomware incident saves multiples of that cost. Most government security budgets should have this line item.

### 6.2 Mutual Aid Across Government Entities

State and local governments benefit from security information sharing that is available to them but underused. The Government Coordinating Council for each critical infrastructure sector facilitates information sharing between government entities. The Multi-State Information Sharing and Analysis Center (MS-ISAC) is specifically designed for state, local, tribal, and territorial governments and provides:

- Real-time threat intelligence including indicators of compromise for active campaigns
- 24/7 security operations center support for member governments
- Free malware analysis of suspicious files
- Incident response coordination assistance
- Access to the CISA network of resources through a single point of contact

MS-ISAC membership is free for qualifying SLTT entities. If your organization is not currently enrolled, enrollment at cisecurity.org takes 15 minutes. The threat intelligence value alone justifies the enrollment time.

---

## Sources

- [Trend Micro: U.S. Public Sector Under Siege — Q1 2026 Threat Intelligence](https://www.trendmicro.com/en_us/research/26/d/us-public-sector-under-siege.html)
- [The Cyber Express: March 2026 Threat Landscape](https://thecyberexpress.com/march-2026-threat-landscape/)
- [CISA: Cybersecurity Resources for High-Risk Communities](https://www.cisa.gov/audiences/high-risk-communities/cybersecurity-resources-high-risk-communities)
- [CISA: Cyber Hygiene Vulnerability Scanning Services](https://www.cisa.gov/resources-tools/services/vulnerability-scanning)
- [CISA: Known Exploited Vulnerabilities Catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)
- [CIS: EI-ISAC — Elections Infrastructure ISAC](https://www.cisecurity.org/ei-isac)
- [CISA: StopRansomware.gov — Government Sector Resources](https://www.stopransomware.gov)
- [CISA: Ransomware Readiness Assessment Tool](https://www.cisa.gov/resources-tools/services/ransomware-readiness-assessment)
- [Palantir Threat Model (corpus internal)](../palantir-threat-model.md)
- [Financial Resistance Playbook — SAR and federal data pipeline](../financial-resistance-playbook.md)

---

*Created: 2026-05-09. Threat currency current as of May 9, 2026. Election security requirements and state notification timelines vary by jurisdiction — confirm state-specific requirements with your state CISO's office. CIRCIA implementing regulations are pending finalization — requirements described reflect current CISA guidance. Quarterly review checkpoint: July 26, 2026.*
