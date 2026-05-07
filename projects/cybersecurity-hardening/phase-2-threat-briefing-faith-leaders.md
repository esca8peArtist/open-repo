---
title: "Phase 2 Threat Briefing: Faith Leaders and Spiritual Communities"
project: cybersecurity-hardening
created: 2026-05-07
status: production-ready
phase: Phase 2
audience: Pastors, priests, rabbis, imams, ministers, faith community administrators, interfaith coalitions, sanctuary congregations, chaplains
distribution-tier: Phase 2 — Priority Constituency 5
companion-playbooks:
  - opsec-playbook.md
  - device-hardening-guide.md
  - activist-organizing-playbook.md
  - phase-2-activist-organizing-security-playbook.md
gist-url: https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108
next-review: 2026-08-07
---

# Phase 2 Threat Briefing: Faith Leaders and Spiritual Communities

**For**: Pastors, priests, rabbis, imams, ministers, faith community administrators, sanctuary congregations, and interfaith networks
**Date**: May 7, 2026
**Prepared by**: Cybersecurity Hardening Project (public-source research corpus)
**Companion resource**: Full OpSec corpus — https://gist.github.com/esca8peArtist/e90dd6a0bd6805e0ddbe0e8d1ee7d108

---

## Why Faith Communities Are Targeted in May 2026

Faith communities occupy a unique position in the current threat landscape: they are simultaneously among the most legally protected institutions (First Amendment free exercise protections, historic sensitive-location status) and among the most practically exposed (open-membership social structures, publicly accessible worship schedules, documented history of providing sanctuary and social services to populations under active enforcement pressure).

The specific threat shift in January 2025 is the most important precedent this briefing can communicate: the Trump administration rescinded the Biden-era policy that required ICE agents to seek additional authority before conducting immigration enforcement actions at sensitive locations, including churches, schools, and hospitals. This 14-year-old protection was ended by executive policy change on January 20, 2025, the first day of the administration.

The consequences are documented and ongoing. ICE has conducted enforcement operations at church properties in Georgia, North Carolina, California, and Louisiana. Pastors in multiple states have reported visits from federal agents requesting congregant names and addresses. A judge issued a preliminary injunction protecting some Quaker, Baptist, Lutheran, and MCC congregations from warrantless church-site enforcement operations in February 2026 — but the injunction applies to named congregations and does not create a general prohibition on church-site enforcement.

The core threat to faith leaders is not primarily digital. It is the conversion of a congregation's open-community social structure into an ICE intelligence source, combined with the digital surveillance infrastructure that can correlate location data from congregant phones, social media from church events, and administrative records from pastoral care interactions.

---

## Current Threat Landscape — May 2026

### Threat 1: Church-Site Enforcement — The End of Sensitive Location Protection

The January 20, 2025 policy rescission fundamentally changed the legal landscape for sanctuary congregations. Under prior policy, ICE was required to obtain supervisory approval before conducting enforcement actions at sensitive locations including houses of worship. That requirement no longer exists.

**Documented incidents through May 2026**:
- Tucker, Georgia (2025): ICE activated an undocumented man's GPS ankle monitor to lure him outside a church building, then arrested him
- Charlotte, North Carolina (November 2025): ICE raided a church yard while 15–20 church members were conducting property maintenance and their children played games
- Los Angeles (January 29, 2026): ICE raided a food ministry event at a Methodist church parking lot and arrested a community member
- Multiple jurisdictions: Faith leaders have reported federal agents visiting their offices requesting names and addresses of congregants, with some DOJ attorneys reportedly holding internal briefings referencing a nationwide plan targeting religious communities

**Legal status**: A February 2026 preliminary injunction (ELCA Minnesota, United Church of Christ) blocked warrantless enforcement at several specifically named congregations. The injunction does not protect congregations outside the named parties. Legal challenges to the rescission are ongoing in multiple federal circuits.

**What this means for sanctuary congregations**: Operating as a sanctuary congregation in 2026 requires understanding that the legal protection that made sanctuary viable for 40 years — the institutional respect for religious space as off-limits to enforcement — has been formally revoked. The question is now operational: what physical, administrative, and digital practices reduce risk to the congregation and to the people it is protecting?

**Sources**:
- Religion News Service, "How the Sanctuary Movement Became the Faithful's Answer to ICE Raids" (March 2026) — https://religionnews.com/2026/03/23/how-the-sanctuary-movement-became-the-faithfuls-answer-to-ice-raids/
- Word & Way, "Judge Freezes ICE Raids at Some Baptist, Lutheran, and MCC Churches" (February 2026) — https://wordandway.org/2026/02/14/judge-freezes-ice-raids-at-some-baptist-lutheran-mcc-churches/

---

### Threat 2: Congregant Data as an ICE Intelligence Surface

Faith communities maintain membership records, prayer request registrations, food pantry intake forms, and pastoral care logs that contain identifying information about congregation members. In the current enforcement environment, these records represent an intelligence surface that ICE can seek through legal process or, in some documented cases, through direct requests to pastoral staff.

**The digital layer of this threat**:
- Church management software (Planning Center, Breeze, ChurchTrac, Pushpay) stores congregant name, address, email, and phone data in cloud-hosted databases. Most church management platforms are hosted by U.S.-based cloud providers that comply routinely with U.S. legal process.
- Worship service attendance, small group participation, and volunteer records in these systems document congregant presence and associations
- Social media posted by churches tagging congregants at events (photos with location tags, tagged attendance posts) publicly documents the associations between individuals and the congregation

**What has been documented**: In at least one confirmed case (New England), federal agents visited a church directly requesting congregant names and addresses — a direct administrative request rather than formal legal process. The pastoral privilege protecting communications between clergy and congregants in the confessional context does not generally protect administrative membership records from legal process.

**Source**: People's World, "ICE Now Grabbing People Out of Churches" — https://www.peoplesworld.org/article/ice-now-grabbing-people-out-of-churches/

---

### Threat 3: Penlink Location Data — Congregant Phones at Religious Events

DHS's $2.9 million Penlink PLX contract enables real-time collection and aggregation of cellphone location data from advertising SDK networks. Penlink's capability includes identifying which cellphones were in a specific location at a specific time, and tracking all locations those phones subsequently visited.

A church that hosts a known sanctuary congregation service, a Know Your Rights training, or a food pantry serving immigrant communities has effectively registered every phone in the building with a location-based profile that is accessible to DHS without a warrant or court order.

**The operational implication**: Congregants who attend immigration-adjacent faith community events at a church with a known sanctuary designation are generating location records that correlate their presence at that site with their phones' subsequent movements. This is not a risk that encrypted communications addresses — it is a risk that requires either leaving phones out of the building or understanding that phone presence at a designated sanctuary location creates a permanent record.

**Source**: Prism Reports, "DHS is Buying Access to Real-Time Location Data" (April 29, 2026) — https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/

---

### Threat 4: Clergy Activism as a Surveillance Trigger

Progressive faith leaders are increasingly visible in public anti-ICE organizing — documented in Religion News Service's March 2026 analysis of the sanctuary movement and the January 2026 clergy deployment to Minneapolis during ICE operations. This public visibility has made some faith leaders targets of the same Babel Street persistent monitoring deployed against political organizers.

Once a faith leader's name or social media handle appears in keyword-matched content monitored by Babel Street's persistent search, all future public content they generate is automatically monitored. The "radical" designation applied by Babel Street's DHS contracts operates on keyword matching, not on any assessment of actual threat — a sermon posted to YouTube referencing immigration enforcement, a Facebook post about a food pantry arrest, or an Instagram story from a rally can trigger persistent monitoring status.

**Source**: Religion News Service, "Progressive Faith Leaders Found New Power in Protesting ICE. Can Their Movement Survive Success?" (March 2026) — https://religionnews.com/2026/03/22/progressive-faith-leaders-found-new-power-in-protesting-ice-can-their-movement-survive-success/

---

## Sector-Specific Response Architecture

### Step 1: Congregant Data Minimization and Records Audit (Immediate — This Week)

The highest-leverage action for protecting congregants is reducing what administrative records the congregation holds in discoverable form:

- **Audit what your church management system contains**: Does it store home addresses, immigration status information, or household composition data? Does it need to? Data minimization — storing only what is necessary for ministry operations — directly reduces discovery surface.
- **Cloud hosting review**: Does your church management software store data with a U.S.-based provider? Review whether that provider's terms of service commit to notifying you before complying with legal process. Most do not provide such notice by default.
- **Social media photo review**: Review past social media posts that tag congregants at church events, particularly events related to immigration advocacy. Consider removing location-tagged photos that document the presence of at-risk individuals at your facility.

### Step 2: Operational Security for Sanctuary Operations (30 Days)

If your congregation operates as a sanctuary congregation or hosts immigration-related services, the following operational protocol significantly reduces risk:

- **Phone-free sensitive spaces**: For rooms or events where you are providing services to undocumented individuals or housing sanctuary guests, establish a norm of phones being left in vehicles or stored in a basket at the door. This is not about distrust — it is about the Penlink location data reality. Every phone in the room is generating a record.
- **Pastoral care communications via Signal**: For clergy communications with congregants who have immigration vulnerability, use Signal rather than church email or standard SMS. Signal stores nothing that can be produced in response to legal process.
- **Know Your Rights posting**: Post clearly visible Know Your Rights information for congregants in languages spoken in your community. The ACLU of Missouri has a model guidance document for places of worship — https://www.aclu-mo.org/know-your-rights/guidance-places-worship-immigration-enforcement/

### Step 3: Clergy Personal OpSec for Publicly Active Faith Leaders (30 Days)

For faith leaders who are publicly visible in immigration advocacy:

- Data broker opt-out execution (companion corpus Part 0) for yourself and for staff with public-facing roles — your home address, phone number, and family associations in commercial databases are accessible via OSINT tools ICE uses for operational planning
- Review social media settings: separate your personal social media from your ministry social media. Content from your personal accounts documenting your home, your family's routines, or your personal travel is accessible via Babel Street monitoring regardless of your intent
- Device hardening for pastoral devices: Enable full-disk encryption on any device that holds pastoral communications or congregant information. Enable a PIN rather than biometric unlock (law enforcement can compel biometrics but generally cannot compel a memorized PIN under the Fifth Amendment). Full protocol in companion corpus device-hardening-guide.md.

---

## Playbooks Available

- **opsec-playbook.md** — Core operational security applicable to faith leaders and congregation administrators
- **device-hardening-guide.md** — Device hardening including PIN vs. biometric guidance, border-crossing protocol, and encryption setup
- **activist-organizing-playbook.md** — Comprehensive counter-surveillance guide for public-facing faith leaders engaged in protest and advocacy contexts
- **phase-2-activist-organizing-security-playbook.md** — Condensed May 2026 protocol guide

---

## Timeline

- **Now**: Congregant data audit; cloud hosting review; social media photo review for at-risk individuals
- **30 days**: Phone-free protocol for sensitive spaces; pastoral communications migration to Signal; clergy data broker opt-outs
- **February 2026 injunction status**: Watch for court developments — the preliminary injunction protecting named congregations may be appealed or expanded
- **August 7, 2026**: Quarterly review of this briefing
- **November 2026**: Midterm election — elevated threat window for faith-based voter registration and get-out-the-vote activities in immigrant communities

---

## Sources

1. Religion News Service: How the Sanctuary Movement Became the Faithful's Answer to ICE Raids (March 2026) — https://religionnews.com/2026/03/23/how-the-sanctuary-movement-became-the-faithfuls-answer-to-ice-raids/
2. Word & Way: Judge Freezes ICE Raids at Some Baptist, Lutheran, and MCC Churches (February 2026) — https://wordandway.org/2026/02/14/judge-freezes-ice-raids-at-some-baptist-lutheran-mcc-churches/
3. Prism Reports: DHS Buying Access to Real-Time Location Data via Penlink PLX (April 2026) — https://prismreports.org/2026/04/29/dhs-surveillance-location-data-penlink-plx/
4. People's World: ICE Now Grabbing People Out of Churches — https://www.peoplesworld.org/article/ice-now-grabbing-people-out-of-churches/
5. Religion News Service: Progressive Faith Leaders Found New Power in Protesting ICE (March 2026) — https://religionnews.com/2026/03/22/progressive-faith-leaders-found-new-power-in-protesting-ice-can-their-movement-survive-success/
6. ACLU of Missouri: Guidance for Places of Worship — https://www.aclu-mo.org/know-your-rights/guidance-places-worship-immigration-enforcement/
7. America Magazine: Faith Groups Sue over Trump Administration Policy to Permit ICE Arrests at Churches (February 2025) — https://www.americamagazine.org/politics-society/2025/02/12/faith-groups-sue-trump-ice-raids-churches-249911/

---

*Briefing date: May 7, 2026. Corpus reflects enforcement landscape as of May 7, 2026. Quarterly review: August 7, 2026.*
