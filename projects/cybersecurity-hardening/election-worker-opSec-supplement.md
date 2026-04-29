---
title: "Election Worker OpSec Supplement"
project: cybersecurity-hardening
created: 2026-04-29
status: complete
depends_on: device-hardening-guide.md, opsec-playbook.md, hardware-procurement-guide.md
confidence: high — sourced from CISA, election official surveys, threat reporting, federal election security status (April 2026)
---

# Election Worker and Observer OpSec Supplement

**Purpose**: This supplement addresses operational security specific to election workers, election observers, poll monitors, and voting rights advocates. It extends the general hardening guides in cybersecurity-hardening with threat modeling specific to the 2026 election environment.

**Context**: April 2026 marked a significant change in the federal election security landscape:
- CISA (Cybersecurity and Infrastructure Security Agency) announced loss of 14 positions and $40 million in election security capacity
- FY2027 federal budget proposal eliminates the election security program entirely
- 75% of local election officials report insufficient replacement resources
- 38% of election officials report personal harassment or threats
- Election worker OpSec tools and support structures are less available than in 2024

**Threat profile for 2026**:
- Doxing and public identification of election workers
- Social media-based intimidation and threats
- Fraud allegations targeting specific workers or procedures
- Potential physical targeting of polling locations
- Disinformation campaigns targeting voter confidence

---

## Part 1: Information Compartmentalization

### 1.1 Separate Work and Personal Identities

Election work creates a permanent public record of your role. Countermeasures:

**Do**:
- Use your full legal name and official title in election-related contexts (you cannot hide; elections are public process)
- Maintain a public election-worker professional identity tied only to your election role
- Keep your personal life (residence, family, social media) compartmentalized from your election role

**Don't**:
- Link your election worker name to personal social media accounts
- Post about election work on personal social accounts
- Use the same email address for election work and personal accounts
- Include your address, phone, or family information in any election-related document

**Practical steps**:
1. Create a separate email address for election work: `[yourname].election@[domain].gov` or similar
2. Keep personal social media locked down (privacy settings: friends-only, no location tagging)
3. For communication with other election workers: use official channels (encrypted email, official government systems)
4. Document any suspicious inquiries about your personal information

### 1.2 Communication Security for Sensitive Election Information

Election information is public after decisions are made, but during procedures, sensitive operational details should be protected.

**Tier 1** (general election procedures, public information):
- Email and standard communications are fine
- Phone calls are acceptable

**Tier 2** (ongoing investigations, security incidents, fraud allegations):
- Use encrypted messaging (Signal for phone, Signal desktop for computer)
- Avoid email unless official channels support encryption
- Phone calls are preferable to text for sensitive discussions

**Tier 3** (threats against election workers, imminent security incidents):
- Call law enforcement directly
- Do not rely on email
- Document the time, nature, and severity of threat
- Escalate to county/state election officials and law enforcement immediately

### 1.3 Social Media During Election Period

**General principle**: Do not use personal social media to discuss election work, even in favorable ways.

**Why**: Your statements can be selectively quoted, misrepresented, or used to create the impression that you have personal bias. Even factually correct statements about procedures can be weaponized in fraud litigation.

**Practical guidance**:
- If you have an official election role, do not post about work on personal accounts
- If you must communicate publicly about election procedures, use official channels (county website, official social media accounts, public meetings)
- Assume anything you write will be screenshotted, taken out of context, and potentially used in legal proceedings
- Example: A post saying "We use hand-marked paper ballots to prevent hacking" can be quoted as "Election workers admit that machines can be hacked" in misleading contexts

---

## Part 2: Physical Security and Threat Management

### 2.1 De-Identification in Public

Election workers are now identified in public records and may be doxxed online.

**Countermeasures**:
- Vary your route and schedule for commuting to election sites
- Do not establish predictable patterns (same time, same route, same coffee shop)
- Tell trusted colleagues about threat concerns; establish informal monitoring
- Report suspicious activities (vehicles following you, unfamiliar people watching your home, concerning messages)
- Consider threat assessment: Does your election work involve a particular controversy or litigation? Are you personally named in any fraud allegations or legal filings?

**If you receive threats**:
- Document the threat (screenshot, date, time, content, source)
- Contact local law enforcement and file a report
- Provide the report to your election office
- Consider notification to Secret Service if threats reference specific venues or times
- Increase physical security awareness (don't be alone, vary patterns, keep phone charged)

### 2.2 Polling Location Security

Polling places are public spaces, but election workers have elevated security concerns.

**Before voting begins**:
- Arrive early to ensure voting machines are secure
- Verify that physical security measures are in place (barriers, signage, procedures for securing completed ballots)
- Establish clear communication protocols in case of disruption

**During voting**:
- Stay visible and professional
- If someone is disruptive, do not engage in argument — follow your jurisdiction's procedures for managing disruptions
- Document unusual activity (people photographing ballots, people entering restricted areas, concerns about chain of custody)
- Report concerns to law enforcement if safety is at risk

**After voting closes**:
- Follow chain-of-custody procedures exactly (these are your legal protection)
- Ensure all ballots, machines, and records are secured
- Document the time you left the location and any unusual events

### 2.3 Vehicles and Travel

If you transport election materials or travel to multiple voting locations:

**Vehicle security**:
- Park in visible, well-lit areas
- Lock all doors while away from the vehicle
- Do not leave election equipment unattended in a vehicle
- If transporting ballots or sensitive materials, use government vehicles if available (they have more security oversight than personal vehicles)
- Consider a dash cam for your commute (provides documentation if you're targeted)

**Personal travel**:
- Tell a trusted person where you're going and when you'll return
- Share your location with a trusted contact during transport of sensitive materials
- Keep your phone charged
- Know the location of nearby law enforcement

---

## Part 3: Digital Security for Election Workers

### 3.1 Device Hardening for Election-Specific Work

Apply the hardening recommendations from device-hardening-guide.md with this addition:

**Election-specific email security**:
- Use your official election email, not personal email, for all election-related communication
- Enable two-factor authentication if your election office provides it
- Assume your email may be subpoenaed in litigation — do not write anything you would not want to defend in court
- Keep election-related documents on official systems, not personal devices
- If documents must be portable, encrypt them (most governments provide encrypted USB drives; if not, use VeraCrypt)

**Voter information and data security**:
- Voter registration data, addresses, and identifying information are sensitive
- Follow all legal restrictions on what information can be disclosed
- If you handle this data, keep it on secure, government systems
- Report any suspected breaches immediately to your election office and to state/federal authorities
- Do not copy voter data to personal devices or unencrypted USB drives

### 3.2 CISA Resources (Changed April 2026)

**Critical note**: CISA's election security program faced severe cuts in April 2026. The following resources may no longer be available:

**Historically available** (status in April 2026 uncertain):
- Election Security Operations Centers (ESORCs) — state-level coordination
- EI-ISAC (Elections Infrastructure Information Sharing and Analysis Center)
- Regional advisors for election security
- Training and resources for election officials

**What to do instead**:
- Contact your state election office (Secretary of State) for guidance
- Reach out to your state attorney general's office (election integrity unit)
- National Association of Election Officials (NAAEO) and state election associations may have resources
- Contact your state's congressional delegation if you believe election infrastructure is under threat
- Document all security concerns and preserve evidence for potential litigation

### 3.3 Fraud Allegations and Online Disinformation

Fraudulent claims about election procedures are common and often target specific workers.

**If you're accused of fraud or misconduct**:
1. Do not respond publicly or on social media
2. Contact your election office immediately
3. Preserve all documentation related to your work (procedures, training, communication with colleagues)
4. Consider consulting with an attorney if the allegation is serious or surfaces in legal proceedings
5. Document the allegation, source, and date
6. Report coordinated harassment to law enforcement if it reaches that threshold

**If you encounter disinformation about election procedures**:
- Do not engage on social media
- Provide factual information only through official channels
- Report coordinated disinformation campaigns to your election office and to law enforcement
- For threats accompanying disinformation, escalate to law enforcement

---

## Part 4: Threat Assessment Framework for Election Workers

Use this framework to evaluate your threat level and adjust precautions accordingly.

### 4.1 Tier Classification

**Tier 1 — Standard election worker**:
- Role: Poll worker, election judge, clerical role in election office
- Threat: General public scrutiny, occasional public criticism of election procedures
- OpSec level: Follow general device hardening; compartmentalize personal/professional identity
- Additional precautions: None required beyond standard cybersecurity practices

**Tier 2 — Targeted election worker**:
- Role: Directly involved in ballot counting, election certification, or audit procedures
- Threat: Specific allegations of fraud or misconduct; litigation; public identification
- OpSec level: Implement all Part 1-3 recommendations; consider threat assessment
- Additional precautions: Report threats to law enforcement; coordinate with election office on security

**Tier 3 — High-profile election worker**:
- Role: County election official, election administrator, or worker in a contested/litigated election
- Threat: Doxxing, coordinated harassment, physical threats, threats to family
- OpSec level: Full implementation; consider additional physical security measures
- Additional precautions: Threat assessment, coordination with law enforcement, legal counsel, elected officials

### 4.2 When to Escalate

Contact law enforcement if you experience:
- Direct threats of violence
- Sustained harassment or doxing
- Suspicious vehicles or people near your home
- Threats to your family members
- Attempts to access election systems or equipment
- Suspicious packages or communications

Contact your election office immediately if you experience:
- Technical anomalies with voting equipment
- Unexplained discrepancies in ballot counts or records
- Suspicious activity during election procedures
- Pressure to deviate from procedures
- Concerns about chain of custody

---

## Sources

- [CISA: Election Security](https://www.cisa.gov/election-security) (As of April 2026 — capacity reduced)
- [Brennan Center: Election Official Security in 2026 Survey](https://www.brennancenter.org/)
- [EAC: Security Best Practices for Election Officials](https://www.eac.gov/)
- [NAAEO: National Association of Election Officials](https://naaeo.org/)
- [Stanford Internet Observatory: 2026 Election Disinformation Tactics](https://sio.stanford.edu/)
- [Election Assistance Commission: Incident Response Guide](https://www.eac.gov/documents-and-reports)
