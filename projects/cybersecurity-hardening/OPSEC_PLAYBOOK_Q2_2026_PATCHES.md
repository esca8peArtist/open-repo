---
title: "OpSec Playbook — Q2 2026 Integration Patches"
project: cybersecurity-hardening
created: 2026-06-06
status: ready-to-integrate
version: 1.0
purpose: >
  Patch blocks ready for direct insertion into opsec-playbook.md and the three Phase 2
  scenario playbooks. Each patch is labeled with its target document and target location.
  Patches add new threat context or update existing sections with Q2 2026 developments.
  No existing guidance should be deleted — all patches are additive.
source_documents:
  - THREAT_ENVIRONMENT_Q2_2026_UPDATE.md (2026-06-06)
  - PHASE_2_THREAT_INTEGRATION_CHECKLIST.md (2026-06-06)
integration_priority: Complete HIGH items before July 26 Phase 2 Wave 1 distribution
---

# OpSec Playbook Q2 2026 Integration Patches

This document contains ready-to-insert patch blocks for `opsec-playbook.md` and the three Phase 2 scenario playbooks. Each block is clearly labeled with its target document and insertion location.

---

## PATCH 1: opsec-playbook.md — DOGE Data Access Update

**Target document**: `opsec-playbook.md`
**Target location**: Part 8 (DOGE cross-agency data fusion, referenced in the current introduction) — add this block to the DOGE section or insert where DOGE is discussed
**Priority**: HIGH

```
### DOGE June 2026 Update — Voter Roll Matching and OPM Injunction

**Status as of June 6, 2026**: Materially worse than the June 2025 SSA access documented in this guide.

**New confirmed elements**:
- Court filings (January 2026) revealed DOGE employees at SSA coordinating with a political
  advocacy group to match SSA data (including immigration status) against state voter rolls
  "to find evidence of voter fraud and to overturn election results in certain States."
- Former SSA chief data officer Charles Borges filed a whistleblower disclosure confirming
  300M+ Americans' records were copied to a virtual database without security protocols.
- The Supreme Court authorized DOGE data access to SSA data in April 2026 (overriding
  Fourth Circuit limits), but DOGE likely violated even that order per subsequent court filings.
- A New York federal court issued a preliminary injunction on June 6, 2026 halting DOGE's
  access to OPM data (federal employee, retiree, and job applicant records).

**Why this changes your threat model**:
The prior threat framing was: DOGE can access federal benefit data for government efficiency
review. The current confirmed threat is: DOGE data is being actively used against political
opposition organizations and advocacy groups by routing federal benefit data to a partisan
advocacy group for voter roll targeting.

This is no longer a privacy-by-negligence threat. It is a targeted political surveillance
operation using federal data infrastructure.

**Countermeasures**: Unchanged — the data in SSA, OPM, and IRS systems cannot be removed.
The practical mitigation is to reduce commercial data broker contributions (which can be
removed via opt-out) because those supplement the federal data to create enforcement
confidence scores. For activists with organizational roles: consult a privacy attorney
before submitting any organizational data to federal benefit programs where alternatives exist.
```

---

## PATCH 2: opsec-playbook.md — Biometric Threat Expansion

**Target document**: `opsec-playbook.md`
**Target location**: Part or section on biometric threats / device seizure / physical surveillance countermeasures
**Priority**: HIGH

```
### Biometric Field Toolkit — June 2026 Update

Three parallel biometric capability expansions became operational in Q2 2026. Existing
guidance (power off device, disable Face ID, assert attorney rights) remains correct;
this update adds the specific new capabilities to the threat picture.

**1. ICE Iris Scanning — $25.1M Contract, June 1, 2026**

ICE finalized a no-bid $25.1M contract with Bi2 Technologies on May 22, 2026,
deploying 1,570+ mobile iris scanners to agents nationwide. Contract effective June 1, 2026.
Database: 5M+ booking, arrest, and incarceration records from 47 states.

Combined with Mobile Fortify (facial recognition, 200M+ DHS records) and Clearview AI
(50B+ internet-scraped images), ICE agents now operate a three-layer field biometric
toolkit: distance facial ID (Clearview/HART), identity confirmation at close range (iris),
and database confirmation across federal and state criminal records.

Countermeasure: Do not consent to iris scanning outside of formal arrest processing. The
legal status of compelled iris scanning in non-arrest encounters is unsettled. Assert
your Fifth Amendment right to silence and request attorney consultation.

**2. Clearview AI — 50B+ Images, Confirmed ICE HSI and CBP Use**

- ICE HSI contract: $9.2M (active)
- CBP contract: $225,000 one-year contract signed February 11, 2026
- Database: 50+ billion images scraped from the internet — includes journalist profile
  photos, social media photos, protest photos, news coverage photos
- Not constrained by HART/DHS enrollment requirements — any public photo suffices

Critical jurisdictional gap: Illinois law bars Illinois police from using Clearview.
Federal ICE agents operating in Illinois face no such restriction.

Countermeasure: Any photo posted publicly online is permanently in Clearview's index.
Retroactive removal is not possible. For future exposure reduction: minimize new public
photo posts; for protest or enforcement action coverage, mask coverage should extend to
distinctive features (hair, visible tattoos) that appear in your indexed public photos.

**3. Cellebrite Spring 2026 — iOS 26 AFU Extraction + Safeguard Mode**

Cellebrite's Spring 2026 release (April 2026) achieved:
- iOS 26 and iPhone 17 support for AFU (After First Unlock) state extraction
- New "Safeguard Mode": if a device is seized while unlocked (AFU state), Cellebrite
  can preserve AFU access indefinitely — defeating the iOS 72-hour auto-reboot protection

What Safeguard Mode does not defeat: A device powered off completely before seizure is in
BFU (Before First Unlock) state. Cellebrite cannot establish AFU access on a powered-off
device. BFU extraction capability is substantially more limited.

Countermeasure (unchanged, now even more critical): POWER OFF your device completely
before any anticipated seizure event — border crossing, protest, checkpoint, enforcement
contact. A locked screen is not sufficient because of Safeguard Mode. Power off.
```

---

## PATCH 3: opsec-playbook.md — DHS Administrative Subpoenas

**Target document**: `opsec-playbook.md`
**Target location**: Section on anonymous account security, OSINT countermeasures, or social media section
**Priority**: HIGH

```
### DHS Administrative Subpoenas — Scale Confirmed, Partial Tech Compliance Documented

**Updated status (June 2026)**:
DHS has issued hundreds of administrative subpoenas (no judicial authorization required)
to Google, Meta, Reddit, and Discord to unmask anonymous accounts posting about ICE raids
or criticizing ICE operations.

Compliance pattern confirmed:
- Google, Meta, and Reddit partially complied with some subpoenas before legal challenge
- ACLU filed motions to quash; DHS withdrew some subpoenas to avoid adverse rulings
- Disclosures that occurred before legal challenge cannot be undone

New case (2026): A Philadelphia man received a subpoena four hours after emailing a DHS
official with criticism. Two federal agents and a local police officer appeared at his
home two weeks later.

New target: Columbia University was pressured to share data on a student who participated
in pro-Palestinian protests — expanding the target scope from social media accounts to
institutional records.

**The compliance-then-withdrawal pattern**:
Even where DHS withdrew subpoenas after ACLU intervention, the partial compliance before
challenge means real identity data was disclosed to DHS in some cases before the legal
challenge could prevent it. Withdrawal does not undo disclosed data.

**What this means for account architecture**:
An account registered with a real email address, verified with your phone number, or
accessed from an IP address connected to your identity is a single subpoena away from
identity disclosure. The only protection is complete separation at account creation —
not post-hoc anonymization.

Full anonymous account protocol:
1. Dedicated device not associated with your real identity
2. VPN active before account creation and during every session
3. Registration email: ProtonMail created over VPN or Tor, no connection to real identity
4. No phone verification tied to a real carrier number — use a VoIP number (MySudo)
   purchased without identity, or skip phone verification entirely
5. No payment method linked to your identity
6. Never access from a network associated with your home, workplace, or regular locations
```

---

## PATCH 4: phase-2-journalist-security-playbook.md — DOJ Guidelines Rescinded

**Target document**: `phase-2-journalist-security-playbook.md`
**Target location**: Section 1.4 (Grand Jury Subpoenas for Source Testimony) — replace or supplement the "DOJ guidelines limitation" paragraph
**Priority**: HIGH — most urgent update for journalist playbook

```
### DOJ Journalist Protection Guidelines — Rescinded April 2025, Activated May 2026

**Status**: The voluntary DOJ guidelines (28 C.F.R. § 50.10) that limited journalist
subpoenas have been formally rescinded. This is no longer a future risk — it is current
policy in active use.

**What was rescinded**: Attorney General Bondi issued a memorandum in April 2025 revoking
the Biden-era policy that prohibited DOJ from using subpoenas or other investigative tools
against journalists who possess and publish classified information obtained in newsgathering.
The previous policy required high-threshold justification, AG approval, and presumption
against journalist subpoenas.

**2026 documented activations**:

January 2026 — Washington Post reporter Hannah Natanson:
The FBI executed a search warrant at Natanson's home in connection with a classified
information investigation of a government contractor. Agents compelled Face ID unlock
of her devices. This is the first documented forced biometric journalist device search
under the revised guidelines.

May 2026 — Wall Street Journal Iran war coverage:
DOJ issued grand jury subpoenas to WSJ reporters for source records related to the
newspaper's reporting on the U.S.-Israel Iran conflict. President Trump personally
directed acting AG Todd Blanche to pursue the investigation, providing a stack of articles
labeled "treason" in a handwritten note. The CPJ condemned the subpoenas on May 26, 2026.
DOJ stated the subpoenas target leakers, not the journalists themselves — but
the method requires accessing journalist records to identify those leakers.

**Operational implications for source protection**:

Under the prior guideline framework, a journalist could plan on significant advance notice
and a high legal threshold before source-identifying records were subpoenaed.

Under the Bondi framework, no such planning assumption is valid. Standard federal grand
jury subpoena and search warrant authority applies. Third-party records (carrier call logs,
Google email, iCloud storage) can be compelled without notice to the journalist.

This changes source communication security from "best practice" to "legal self-protection":
- A journalist who uses Signal from first contact with a source is protecting themselves
  from being a subpoenable conduit, not only protecting the source.
- Gmail, Outlook, iCloud email, and any carrier-logged call or SMS are now legally 
  accessible under the revised policy without the prior high threshold.
- ProtonMail (Swiss law, no metadata of message content retained) and Signal (retains
  only account creation date and last connection date) remain outside the effective reach
  of a US subpoena for message content.
- SecureDrop routes document receipt through the Tor network and retains no metadata
  linking the submission to any journalist or source identity.

The shield law gap remains: The federal PRESS Act has not been enacted. State shield laws
do not apply in federal proceedings. A federal grand jury can subpoena a journalist and
a federal judge can hold the journalist in contempt for refusing.
```

---

## PATCH 5: phase-2-journalist-security-playbook.md — FISA 702 June 12 Update

**Target document**: `phase-2-journalist-security-playbook.md`
**Target location**: Section 1.2 (FISA Section 702) — replace the "Congressional status as of May 2026" paragraph
**Priority**: HIGH

```
**Congressional status as of June 6, 2026**:

Section 702 expires June 12. The Senate voted 47-52 on June 5 on a motion to proceed to
long-term reauthorization — the measure failed. Seven Republicans joined Democrats in
opposition. Senate Majority Leader Thune acknowledged "on June 12, that program goes dark"
and suggested leadership would attempt another procedural vote before the deadline.

A legislative lapse is possible for the first time in this reauthorization cycle.

**What a lapse does and does not change for journalists**:
Even if Section 702 expires on June 12, the Foreign Intelligence Surveillance Court (FISC)
issued an administrative order separately extending operational authority for existing
Section 702 certifications through 2027. NSA collection of foreign-targeted communications
continues under FISC authority regardless of congressional action or inaction.

The warrant reform that would have protected journalist queries (the Government Surveillance
Reform Act, S.4082) has not been enacted. No warrant requirement for journalist queries of
the Section 702 database has passed in any form.

For journalists using Signal with foreign sources: no operational change regardless of the
June 12 outcome. Signal has zero stored content for the FBI to query.
```

---

## PATCH 6: phase-2-immigration-surveillance-evasion-playbook.md — Iris Scanning and Clearview

**Target document**: `phase-2-immigration-surveillance-evasion-playbook.md`
**Target location**: Section 1.3 (Mobile Fortify) — add after existing Mobile Fortify text
**Priority**: HIGH

```
**June 2026 Update: ICE Biometric Toolkit Expanded**

Since this playbook was written, ICE has deployed two additional biometric capabilities:

**Iris Scanning ($25.1M, Bi2 Technologies, effective June 1, 2026)**:
ICE has deployed 1,570+ mobile iris scanners to field agents. The scanner accesses a
database of 5M+ booking and incarceration records from 47 states. Iris scanning is used
as a close-range identity confirmation step when facial identification is uncertain.

If you are approached by an ICE agent who requests a biometric scan:
- You are not required to consent to iris scanning outside of formal arrest processing.
- The legal status of compelled iris scanning in a street encounter is unsettled.
- Assert your right to consult an attorney before submitting to any biometric collection.
- Do not verbally confirm or deny your identity without your attorney present.

**Clearview AI (ICE HSI, $9.2M contract; database of 50+ billion internet images)**:
Separate from Mobile Fortify (which uses the HART database of DHS-enrolled images), ICE's
Homeland Security Investigations division uses Clearview AI. Clearview's database includes
photos scraped from Facebook, Instagram, news sites, and any other public website.

If you have any photos posted online — profile photos, news coverage photos, event photos
posted by friends or organizations — those images may be in Clearview's database and may
be used to identify you even without a HART-enrolled biometric record.

**Your countermeasure for Clearview**: The data broker opt-outs in Section 2 reduce your
commercial record footprint. They do not remove photos from Clearview's database.
For photos already posted, no removal is currently available. For future exposure: review
your social media privacy settings so that new photos are not publicly accessible.
```

---

## PATCH 7: phase-2-immigration-surveillance-evasion-playbook.md — DOGE SSA Data

**Target document**: `phase-2-immigration-surveillance-evasion-playbook.md`
**Target location**: Insert as new subsection after existing ELITE/ImmigrationOS sections
**Priority**: HIGH

```
### 1.6 DOGE — Federal Benefit Data in the Enforcement Pipeline

**What happened**: In early 2026, court filings revealed that Department of Government
Efficiency (DOGE) employees at the Social Security Administration improperly accessed
records for over 300 million Americans — including immigration status, bank account
numbers, Social Security numbers, wage histories, and home addresses. DOGE employees
were coordinating with an outside political advocacy group to match this data against
voter rolls. A federal court issued a preliminary injunction on June 6, 2026 halting
further DOGE access to OPM records.

**Your exposure**: If you have ever received any Social Security benefit, received a
Social Security number, had wages reported to the SSA by an employer, or are enrolled
in any federal benefit program, your records were part of the accessed dataset.

SSA's records include immigration status data that can identify undocumented individuals
and DACA recipients.

**Why this matters for your enforcement risk**: The ELITE system already draws from
Medicaid data (HHS data-sharing agreement, December 2025). DOGE's access created a
pathway for SSA data — including wage history, employment patterns, and immigration
status — to enter the same enforcement pipeline. New System of Record Notices issued
alongside the DOGE litigation are expanding the legal authorization for SSA-to-ICE
data sharing beyond what existed before.

**What you can do**: You cannot remove your records from SSA. The practical response is:
1. Complete the data broker opt-out process (Section 2) to reduce what commercial data
   sources contribute to your ELITE address confidence score.
2. Do not provide address information to any government contact that you are not legally
   required to provide.
3. If you have any organizational connection to groups being targeted by DOGE or IRS
   (see the IRS LCA threat model in threat-model.md), consult an immigration attorney
   about your combined exposure profile.
```

---

## PATCH 8: phase-2-activist-organizing-security-playbook.md — FBI at Protests

**Target document**: `phase-2-activist-organizing-security-playbook.md`
**Target location**: Section 1.4 (Layer 4 — Field Biometric at Protest Perimeters) — add after existing text
**Priority**: HIGH

```
**June 2026 Update: FBI Integration Confirmed at Protest Sites**

Current and former DHS officials have confirmed that agents at Minneapolis protests are
using at least two facial recognition systems simultaneously: Mobile Fortify (NEC engine,
DHS HART database) and Clearview AI (50B+ internet images). FBI agents, separately from
ICE, are using facial recognition at protests to add individuals to federal investigative
databases.

The class action lawsuits filed in February 2026 — Hilton v. Noem (Maine) and Tincher v.
Noem (Minnesota) — document the following confirmed pattern across at least two states:
- Agents scanning observers' faces at close range with smartphones
- Photographing license plates of vehicles parked near enforcement events
- Following people home from enforcement observations
- Informing individuals they are now in a "domestic terrorist database"
- Asking individuals why they were present and what organization they belonged to

DHS officially denies the existence of a domestic terrorist database.

**Why FBI integration changes the threat picture**:
ICE facial recognition creates immigration enforcement exposure. FBI facial recognition
creates potential federal criminal investigation exposure — which is a different legal
basis with different downstream consequences. A person in an FBI investigative database
is not at risk of deportation, but may be at risk of law enforcement contact, further
investigation, or future adverse action in any federal proceeding (job application,
security clearance, immigration benefit application, criminal proceeding).

**Countermeasures remain unchanged; the stakes are higher**:
- Physical countermeasures (mask, hat, changed clothing color from prior protests) remain
  the correct approach for minimizing new facial recognition enrollments from protest
  attendance. See Section 4.1.
- Do not photograph or video record agents using your primary identity-linked device.
- If approached by agents and asked for identification: in a non-arrest situation, you
  are not legally required to identify yourself in most states. Know your state's stop
  and identify law. Do not volunteer information about your organization or activities.
```

---

## PATCH 9: phase-2-activist-organizing-security-playbook.md — Admin Subpoenas

**Target document**: `phase-2-activist-organizing-security-playbook.md`
**Target location**: Section 1.5 (Layer 5 — Account Unmasking) — replace or supplement existing text
**Priority**: HIGH

```
**June 2026 Update: Scale, Tech Compliance, and the Four-Hour Response**

The scale of DHS administrative subpoenas against anti-ICE accounts has grown to hundreds
since the original documentation in this playbook.

**Compliance pattern now confirmed**: Google, Meta, and Reddit partially complied with DHS
subpoenas before legal challenges were filed. The ACLU successfully challenged some subpoenas
and DHS withdrew them — but withdrawal does not undo disclosures that occurred before the
legal challenge reached the platform.

**New cases (2026)**:
- Philadelphia case: A man received a DHS subpoena to Google four hours after emailing
  a DHS official with criticism. Two federal agents and a local police officer appeared
  at his home two weeks later to interrogate him about the email.
- Columbia University: DHS used administrative subpoenas to pressure the university to
  share information about a student who participated in pro-Palestinian protests.

**The four-hour response time is the critical new data point**: DHS is monitoring and
subpoenaing in near-real time. There is no grace period to "clean up" a newly created
account after a politically sensitive communication. Anonymous infrastructure must be
fully established before any sensitive activity begins.

**What this means for organizational account architecture**:
Organizational accounts that post about ICE activity, legal observer networks that share
enforcement location alerts, and any account that has ever criticized ICE operations in
any public context are at risk.

The minimum standard for any account in this category:
- Separate device from all personal activity
- VPN active during every session (never post from home or work network)
- Registration with ProtonMail address created over VPN or Tor
- No phone verification on primary carrier number
- No payment linked to your identity
- Do not cross-post between this account and any account linked to your real identity

Organizations that have already been subpoenaed or received legal process should
immediately consult an attorney before responding or producing any records.
```

---

## Threat Model Section Patches (for threat-model.md or opsec-playbook.md threat section)

**Target**: Wherever the current threat model table or actor list appears
**Priority**: MEDIUM (updates existing entries with June 2026 data)

```
### Updated Threat Actor Table — Q2 2026 Additions

Add or update the following entries in the threat actor/capability table:

| Actor | Q2 2026 Update | Confirmed Capability |
|-------|----------------|---------------------|
| ICE (field operations) | Iris scanning deployed June 1 ($25.1M Bi2, 1,570 units) | Iris ID + Mobile Fortify facial + Clearview AI = three-layer biometric stack |
| ICE HSI | Clearview AI contract ($9.2M, confirmed operational) | 50B+ image facial recognition independent of HART enrollment |
| CBP | Clearview AI tactical contract (Feb 11, 2026, $225K) | Facial recognition with internet-scraped image database |
| FBI | AI inventory doubled (19→50 use cases); 4 new facial ID systems deployed | Protest surveillance via facial recognition to investigative databases |
| DHS/DOGE | SSA data accessed for 300M+ including immigration status; voter roll matching confirmed | Federal benefit data as political targeting tool |
| DOJ | Journalist protection guidelines rescinded (April 2025); WSJ subpoenas (May 2026) | Grand jury subpoenas for source identification without prior AG approval threshold |
| Cellebrite | iOS 26 AFU extraction + Safeguard Mode (Spring 2026 release) | Defeats iOS 72-hour auto-reboot; full iOS 26/iPhone 17 coverage |
```

---

*Patches created 2026-06-06. All patch text is final and ready for direct insertion. Before inserting each patch, read the target section to ensure the patch text does not duplicate existing content that has already been updated since the playbooks were created. Prioritize HIGH items before July 26 Phase 2 Wave 1 distribution.*
