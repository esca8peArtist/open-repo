---
title: "Board-Level Cybersecurity Briefing: PowerPoint Outline"
project: cybersecurity-hardening
created: 2026-05-09
status: production-ready
phase: Phase 2 — Organizational Expansion
audience: CFOs, GCs, COOs presenting to board of directors
deadline: June 5, 2026
session: Exploration Queue Item 33
depends_on:
  - phase-2-tier2-organizational-outreach-strategy.md
  - 2026-threat-landscape-q2-update.md
  - PHASE_2_ORGANIZATIONAL_LAUNCH_STRATEGY.md
---

# Board-Level Cybersecurity Briefing: PowerPoint Outline

**Purpose**: Equip institutional decision-makers (CFOs, GCs, COOs) to present the cybersecurity-hardening toolkit to their boards. This is a 10-15 slide briefing deck outline. Each slide entry includes a speaker note scaffold, the core assertion, and supporting data points sourced from 2025-2026 primary reports.

**Presenter context**: The person delivering this deck is a senior institutional leader who has already reviewed the Phase 2 toolkit. They are not presenting a product pitch — they are presenting a governance decision to their own board. Frame accordingly.

---

## Slide 1: Executive Summary — The Threat Is Operational Now

**Core assertion**: In 2026, adversaries are actively targeting organizations like ours using methods we do not currently have defenses for.

**Speaker scaffold**:
"I want to open not with a technical overview but with a governance question: do we know what we would do in the next 72 hours if our communications were compromised? Today I am asking the board to authorize a pilot program that ensures we do."

**Key data for slide**:
- U.S. average data breach cost reached a record $10.22 million in 2025 — up 9% year-over-year (IBM Cost of a Data Breach Report 2025)
- Nonprofits experienced a 30% year-over-year increase in weekly cyberattacks in 2024 (BDO)
- Cloudflare Project Galileo recorded a 241% increase in attacks against human rights and civil society organizations between 2024 and 2025
- FBI has issued formal advisories to nonprofits, think tanks, and human rights organizations about state-sponsored targeting (FBI IC3, 2025)
- Law firms: 20% of U.S. law firms experienced cyberattacks in 2024; 37-39% of law firm clients would fire the firm following a breach (Integris 2025)

**Visual suggestion**: A single timeline of high-profile civil society/NGO/law firm breaches 2023-2025, ending with a forward arrow to 2026. No logos. Organizations identified by type, not name, if names are unavailable.

---

## Slide 2: Cost of Status Quo — What We Risk Every Quarter We Delay

**Core assertion**: The financial exposure from a breach exceeds the cost of a three-year security program by a factor of 10 or more.

**Speaker scaffold**:
"This is not a technology question — it's a risk management question. We would not carry $10 million in uninsured liability in any other area of operations. We are currently doing exactly that in cybersecurity."

**Key data for slide**:

| Risk Category | Exposure per Incident | Source |
|---|---|---|
| Average U.S. data breach cost | $10.22M | IBM 2025 |
| Healthcare sector average breach cost | $7.42M | IBM 2025 |
| Average ransom demand increase (2023→2024) | +$1M YoY | BDO 2025 |
| HIPAA willful neglect fine (cap) | $1.5M/year | HHS OCR |
| Blackbaud ransomware settlement (nonprofit sector) | $49.5M multistate | HHS/state AGs |
| Law firm client churn risk post-breach | 37-39% would fire firm | Integris 2025 |
| Shadow AI additional breach cost adder | +$670K per incident | IBM 2025 |

**Regulatory compliance note for the GC**: The OCR ran 22 healthcare data breach investigations in 2025, collecting $12.8 million in penalties and settlements. Enforcement actions are accelerating, not slowing. The SEC's 4-business-day material incident disclosure requirement (effective December 2023) creates direct personal liability exposure for board members who were notified of cyber risk and did not act.

**Visual suggestion**: A two-column comparison: "Cost of breach (unmitigated)" vs. "3-year security program cost." The breach column should dwarf the program cost at any organization size.

---

## Slide 3: Threat Vector 1 — Your Devices Are the Attack Surface

**Core assertion**: Every staff device that runs unmanaged software, connects to personal networks, or lacks disk encryption is a potential entry point for adversaries.

**Speaker scaffold**:
"The perimeter security model — where a firewall protects the organization — has not been the operative model for five years. Our staff work from home, on personal devices, on hotel Wi-Fi. Every one of those contexts is a potential breach vector."

**Key data and threat specifics**:
- Ransomware attacks on small businesses surged 37% year-over-year from 2024 to 2025; endpoints are the primary vector in 82% of cases
- Average SMB ransomware cost: $2.73 million per incident
- The Mini Shai-Hulud supply chain campaign (April-May 2026) compromised 1,800+ developer repositories; 30 million combined monthly downloads affected across PyPI, npm, PHP
- A single staff member opening a malicious PDF encrypted an entire nonprofit's server including all booking, financial, and personal data — a documented case pattern occurring across sectors

**Three high-priority endpoint controls** (for implementation detail, see Phase 2 Toolkit):
1. Full-disk encryption on all organizational devices (FileVault/BitLocker, 2 hours to deploy per device)
2. Mobile device management policy — approved app list, remote wipe capability
3. Password manager deployment across all staff (Bitwarden: $3/user/month)

**Visual suggestion**: Attack chain diagram — external adversary → phishing email → staff device → internal server → client/member data exfiltrated. Mark each link with the specific control that breaks it.

---

## Slide 4: Threat Vector 2 — Your Communications Are Not Private

**Core assertion**: Email is surveilled infrastructure. Every sensitive communication your organization has conducted over standard email, SMS, or consumer apps is potentially accessible to adversaries who have already compromised those platforms.

**Speaker scaffold**:
"Our legal team communicates with clients over email. Our executive team discusses strategy over standard messaging apps. In 2026, those channels are the equivalent of conducting sensitive conversations in a public space. We can close this gap in 30 days."

**Key data and threat specifics**:
- FISA Section 702 was extended through June 12, 2026 without warrant protection; the FISC separately extended operational authority for existing certifications through 2027 by court order — this means programmatic surveillance of communications continues regardless of any legislative outcome
- Palantir's ICE Investigative Case Management contract carries a hard September 2026 deployment deadline, integrating biometric deduplication, real-time cross-agency tracking, and relationship mapping — organizations working in immigration, labor, or civil rights contexts face active cross-agency monitoring of their communications networks
- AI deepfakes crossed from theoretical to operational in 2026: the NRSC produced a 60-second video deepfake of a Senate candidate (confirmed by CNN); the OECD AI Incident Monitor confirmed 5+ deepfake incidents in 2026 midterm races as of late April 2026. The attack vector extends to organizational communications — staff can receive highly convincing impersonation attempts

**Three high-priority communication controls**:
1. Signal for internal staff communications (free; end-to-end encrypted; disappearing messages enabled)
2. ProtonMail or Tutanota for sensitive external email
3. Verified identity protocol for executive communications — callback verification before any fund transfer or credential change

**Visual suggestion**: Side-by-side channel comparison: "What adversary can access" for standard email/SMS vs. Signal/encrypted email. Red/green matrix by channel type.

---

## Slide 5: Threat Vector 3 — Your Organizational Protocols Have Not Caught Up to the Threat

**Core assertion**: Technical controls fail when human protocols are absent. Most breaches in 2024 involved a human element — phishing, social engineering, or insider error — not a technical failure.

**Speaker scaffold**:
"You can deploy the best software in the world and still lose everything when a staff member gets a convincing phone call from someone claiming to be our CFO. Organizational protocols are the last line of defense — and the least expensive to build."

**Key data and threat specifics**:
- 68% of breaches in 2024 involved a human element — phishing or human error (BDO / Verizon DBIR 2024)
- Employee security awareness training delivers a 50x ROI on investment, the highest single return of any security control (MetaCompliance / JumpCloud 2025)
- Phishing simulation training alone reduces successful phishing click rates from industry average 33% to under 5% in 90-day programs
- Silent Ransom Group specifically targets law firms with social engineering voice calls, impersonating existing clients and IT vendors (FBI IC3 advisory, May 2025)

**Three high-priority protocol controls**:
1. Quarterly security awareness training — mandatory, 45 minutes, phishing simulation included ($20-50/employee/year)
2. Wire transfer and credential change verification protocol — no action on email-only requests; callback to known number required
3. Incident response plan — written, tested annually, board-reviewed. Currently 78% of organizations say their cyber resilience is insufficient; a documented IRP changes that in 60 days

**Visual suggestion**: The "human risk funnel" — of all incidents, 68% human element; of human element incidents, 80% preventable with training; training cost vs. breach cost comparison.

---

## Slide 6: Implementation Cost-Benefit Analysis

**Core assertion**: Full implementation of all three solution layers costs $50,000-$200,000 depending on organization size. One prevented breach pays for six years of security programs.

**Speaker scaffold**:
"I want to be direct with the board about numbers. This is not a 'bet everything' investment. It is a bounded, verifiable program with a quantifiable return."

**Investment by organization size**:

| Organization Size | Year 1 Setup Cost | Annual Recurring | 3-Year Total | Prevented Breach ROI |
|---|---|---|---|---|
| Small (25-50 staff) | $25,000-40,000 | $10,000-15,000 | $50,000-75,000 | 136x (vs. $10.22M breach) |
| Mid-size (50-150 staff) | $50,000-80,000 | $20,000-35,000 | $110,000-185,000 | 55x |
| Large (150-500 staff) | $80,000-150,000 | $40,000-60,000 | $200,000-330,000 | 31x |

**Cost breakdown (Year 1 for mid-size organization, 75 staff)**:
- Endpoint security (EDR, 75 devices @ $8/month): $7,200/year
- Password manager (75 users @ $3/month): $2,700/year
- Encrypted email (25 sensitive accounts @ $8/month ProtonMail Business): $2,400/year
- Security awareness training platform (75 users @ $30/year): $2,250/year
- MDM solution (75 devices @ $4/month): $3,600/year
- IT implementation and onboarding (one-time): $15,000-25,000
- Incident response plan development (one-time): $5,000-10,000
- Staff time allocation (10-15 hours across all staff): bounded

**AI security automation offset**: IBM 2025 data confirms organizations using AI and automation extensively in security operations saved an average $1.9 million in breach costs — this figure is accessible to any mid-size organization using current-generation endpoint and email security tools, which all include AI-driven threat detection.

**Regulatory compliance benefit (healthcare sector)**: Full HIPAA-compliant implementation eliminates exposure to OCR enforcement actions, which averaged $580,000 per settlement in 2025. The $110-185K three-year program cost for a mid-size healthcare nonprofit replaces an ongoing and growing OCR enforcement exposure.

**Visual suggestion**: A 3-year cost curve for the security program against a single-incident breach probability distribution. At even 5% annual breach probability, EV(breach) >> EV(program cost).

---

## Slide 7: Pilot Scope — What We Are Asking to Approve Today

**Core assertion**: We are not asking for full organizational deployment. We are asking to run a 90-day pilot with 3-5 teams or units to validate implementation, gather staff feedback, and measure success before scaling.

**Speaker scaffold**:
"Board approval today authorizes a pilot. We pick three teams — probably legal, communications, and executive — deploy the tool stack with them over 90 days, and come back to the board in September with data. If the pilot meets targets, we scale. If it doesn't, we have spent $15,000-25,000 to learn that, not $100,000."

**Pilot parameters**:
- **Scope**: 3-5 organizational units or teams, 15-40 staff
- **Duration**: 90 days (July 1 - September 30 if approved in June)
- **Budget authorization requested**: $15,000-30,000 (covers implementation support, tools, and training for pilot cohort)
- **Staffing**: No full-time hire required. Designate one existing staff member as pilot coordinator (8-10 hours/week during active deployment, 2-4 hours/week ongoing)
- **External support**: Implementation can be vendor-supported (managed security service provider) or in-house. For organizations without IT staff, MSSP support at $1,500-3,000/month covers the pilot period.
- **Go/no-go criteria**: Set at start of pilot. If success metrics are not met at Day 60 review, pilot pauses. Board retains full control over escalation to organizational scale.

**90-day timeline**:
- Weeks 1-2: Tool deployment and baseline measurement
- Weeks 3-4: Staff onboarding and initial training
- Weeks 5-10: Active deployment period; weekly check-ins with pilot coordinator
- Weeks 11-12: Data collection and analysis
- Day 90: Pilot readout to leadership team; board memo prepared

**Visual suggestion**: A Gantt chart of the 90-day pilot. Clean, minimal. Three phases: Deploy, Operate, Measure.

---

## Slide 8: Success Metrics — How We Know If It Worked

**Core assertion**: Success is measurable in 90 days. We are not asking the board to accept an indefinite commitment with vague outcomes.

**Speaker scaffold**:
"Every governance decision about a security investment should have a measurement framework. Here is ours."

**Metric set (90-day pilot)**:

| Category | Metric | Target | Measurement Method |
|---|---|---|---|
| Adoption | % of pilot staff using password manager | >80% | Bitwarden admin dashboard |
| Adoption | % of pilot staff on Signal | >75% | Internal survey, Day 30 and Day 90 |
| Training | % completing security awareness module | 100% | Training platform completion log |
| Training | Phishing simulation click rate | <10% at Day 90 | Phishing simulation platform |
| Incident | Security incidents in pilot cohort (vs. baseline) | 0 new incidents | IT log |
| Confidence | Staff-reported confidence in security practices | >70% "confident" | Survey, Day 0 and Day 90 |
| Time cost | Average minutes per week spent on security practices | <15 min/week/staff | Survey |

**Board-level leading indicator**: A 75%+ adoption rate on the password manager and Signal combined by Day 45 is the single best leading indicator that the program is on track for full deployment success. If this number is below 50% at Day 45, the pilot has an implementation problem, not a technology problem — escalate to management review.

**What success does not require**: Zero incidents during the pilot period is not a success criterion, because the 90-day window is too short to evaluate breach prevention statistically. The indicators above measure capability built, not luck avoided.

---

## Slide 9: Board Decision Tree

**Core assertion**: The board has three options today. Each has defined next steps.

**Decision option A: Approve pilot as proposed**
- Authorization: $15,000-30,000 for 90-day pilot (July-September 2026)
- Next steps: Management designates pilot coordinator by June 15. Vendor/MSSP selection by June 20. Pilot teams identified by June 20. Kickoff July 1.
- Board involvement: Day 45 written status update to board. Day 90 pilot readout presentation.
- Full deployment decision: Board vote in October 2026.

**Decision option B: Defer pending additional information**
- If the board wants a competitive bid process, risk assessment from external firm, or peer comparison before approving
- Suggested timeline: 30-day discovery window. External risk assessment: $5,000-15,000. Two vendor bids: 2-3 weeks. Board vote: July meeting.
- Risk of deferral: Each month of delay carries actuarial exposure. At 20% annual breach probability for a civil society organization, a 30-day delay adds approximately $170,000 in expected value of unmitigated risk ($10.22M × 20% / 12 months).

**Decision option C: Engage external cybersecurity firm for full assessment first**
- Commission a third-party cybersecurity risk assessment before any implementation decision
- Timeline: 6-8 weeks. Cost: $15,000-40,000 for a mid-size organization.
- Outcome: Formal risk report with prioritized recommendations. Suitable for organizations with complex infrastructure, regulated data, or fiduciary requirements that require documented due diligence.
- Note: A third-party assessment is fully compatible with the Phase 2 toolkit — assessors will arrive at similar recommendations for the priority controls.

**What the board is not being asked to do**: Approve a permanent budget line, hire new staff, or commit to a specific vendor. All of those decisions are downstream of the pilot readout.

**Visual suggestion**: A simple three-branch decision tree, each branch ending in a "next steps" box and a date. Clean, one-page visual.

---

## Slide 10: Appendix — Sector-Specific Threat Narratives

*This slide provides tailored talking points for GCs and COOs briefing boards in specific sectors. Use the relevant subsection; omit the others.*

### Healthcare and Health-Adjacent Nonprofits

The threat is personal data and operational continuity. Healthcare remains the most expensive breach sector for the 14th consecutive year — $7.42 million average per breach (IBM 2025). OCR enforcement is accelerating: 22 investigations in 2025, $12.8 million collected. The Blackbaud ransomware incident — a nonprofit software vendor — directly affected thousands of healthcare clients and resulted in $49.5 million in multistate regulatory settlements. The operational risk: a ransomware attack on an under-resourced health nonprofit can halt client services entirely for weeks. The question for the board: do we have a 72-hour continuity plan if our systems are encrypted on a Monday morning?

### Immigration Legal Aid and Civil Rights Organizations

The threat is adversarial surveillance of organizational networks. FISA 702 surveillance authority continues through at least 2027 by court order. Palantir's ICE ICM contract, with its September 2026 deployment deadline, will integrate cross-agency relationship mapping — any communication channel that involves clients and is not end-to-end encrypted is a liability, both for client safety and for attorney-client privilege. A 2024 CISA advisory specifically named civil society organizations as high-risk communities targeted by state-sponsored actors. The question for the board: do we know which of our communications channels are end-to-end encrypted? If the answer is "I don't know," that is the problem.

### Law Firms

The threat is client trust and regulatory exposure. 52% of law firm clients have cybersecurity concerns. 37-39% would fire the firm following a breach. The Silent Ransom Group targeted law firms specifically in 2025 via social engineering voice calls impersonating clients and IT vendors (FBI IC3, May 2025). Law firms are the number one ransomware target by sector because of the combination of confidential client data and willingness to pay to protect privilege. The business case is client retention: 37% of clients would pay a premium to a firm with robust cybersecurity practices. Security is now a competitive differentiator.

### Labor Unions and Advocacy Organizations

The threat is surveillance of organizing activity. The 2026 threat landscape includes confirmed state and employer-sponsored surveillance of labor organizing communications, with AI-assisted relationship mapping identifying organizer networks from communications metadata. Signal and end-to-end encrypted communications are specifically effective against metadata analysis. The organizational risk is not only data theft but strategic intelligence about campaigns, membership data, and internal deliberations. Worker-member data is the asset. The question for the board: if our communications were being read by an adversary for the last six months, what would they know about our strategy?

---

## Slide 11: Appendix — Implementation Roadmap (Full Scale, Post-Pilot)

*For organizations that approve the pilot and want to see the full-scale roadmap before voting.*

**Phase 1 (Months 1-3): Pilot deployment — 3-5 teams**
- See Slide 7 for full pilot parameters.

**Phase 2 (Months 4-6): Mid-scale deployment — all staff in high-risk functions**
- High-risk functions: legal, communications, executive, field staff in sensitive program areas
- Tool stack complete; training cadence established; IRP documented and tested
- Budget: additional $20,000-40,000 for mid-size organization

**Phase 3 (Months 7-12): Full organizational deployment**
- All staff on password manager, Signal, and security training
- MDM policy covering all organizational devices
- Annual third-party security review
- Board receives annual cyber risk report per NACD 2026 best practice
- Total 12-month investment (pilot through full scale, mid-size organization): $80,000-130,000

**Ongoing governance**:
- Quarterly cyber risk update on board agenda (15-minute standing item; not full presentation every quarter)
- Annual incident response plan review
- Annual phishing simulation review
- Biennial external risk assessment

---

## Slide 12: Sources and Methodology

*For credibility with technically sophisticated board members. Not presented verbally — available as a leave-behind.*

- IBM Security. "Cost of a Data Breach Report 2025." https://www.ibm.com/reports/data-breach
- BDO. "The Crucial Role of Cybersecurity for Nonprofit Organizations in 2025." https://www.bdo.com/insights/industries/nonprofit-education/the-crucial-role-of-cybersecurity-for-nonprofit-organizations-in-2025
- Integris. "2025 Law Firm Cybersecurity Report." https://integrisit.com/law-firm-cybersecurity-2025-report/
- HHS Office for Civil Rights. HIPAA Enforcement Statistics 2025. https://www.hhs.gov/hipaa/for-professionals/compliance-enforcement/agreements/index.html
- FBI IC3. "Silent Ransom Group Targeting Law Firms." Advisory, May 2025. https://www.ic3.gov/CSA/2025/250523.pdf
- CISA. "Guidance for Civil Society Organizations on Mitigating Cyber Threats with Limited Resources." May 14, 2024. https://www.cisa.gov/news-events/alerts/2024/05/14/cisa-and-partners-release-guidance-civil-society-organizations-mitigating-cyber-threats-limited
- NACD. "2026 Director's Handbook on Cyber-Risk Oversight." https://www.nacdonline.org/all-governance/governance-resources/governance-research/director-handbooks/2026-cyber-risk-oversight/
- Recorded Future. "The Hidden Cascade: Why Law Firm Breaches Destroy More than Data." https://www.recordedfuture.com/blog/the-hidden-cascade
- CyberPeace Institute. "Cyber-Poor, Target-Rich: The Crucial Role of Cybersecurity in Nonprofit Organizations." https://cyberpeaceinstitute.org/news/cyber-poor-target-rich-the-crucial-role-of-cybersecurity-in-nonprofit-organizations/
- Cloudflare Project Galileo. 2025 Annual Report (civil society DDoS statistics).
- Fortinet. "Ransomware Statistics 2025." https://www.fortinet.com/resources/cyberglossary/ransomware-statistics
- Australian Cyber Security Centre. "Cyber Security Priorities for Boards of Directors 2025-26." https://www.cyber.gov.au/business-government/protecting-business-leaders/cyber-security-for-business-leaders/cyber-security-priorities-for-boards-of-directors-2025-26
- Deloitte. "CISO Brief: Cybersecurity Awareness for Board of Directors." https://www.deloitte.com/us/en/services/consulting/articles/chief-information-security-officer-board-communication-cybersecurity.html
