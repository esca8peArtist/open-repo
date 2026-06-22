---
title: "IMSI Catcher Detection and Cellular Anonymity Guide"
project: cybersecurity-hardening
created: 2026-06-22
status: complete
priority: P1 (F-04)
depends_on:
  - opsec-playbook.md (Part 11: IMSI catcher detection, Rayhunter coverage)
  - threat-model.md (Section V.C: cell-site simulators, confirmed government users)
  - PERSONAL_OPSEC_PLAN.md (Section 3.3: 2G disable)
  - device-hardening-guide.md (airplane mode vs. power-off analysis)
confidence: high for detection and passive defense; medium for SIM anonymity jurisdiction coverage (current as of mid-2026, verify for specific countries before acting); high for burner device discipline
audience: Tier 2 (activists, organizers, protest participants) and above — anyone who may face IMSI catcher deployment at demonstrations, high-risk travel, or targeted surveillance
---

# IMSI Catcher Detection and Cellular Anonymity Guide

> **Lead finding**: The most effective IMSI catcher defense is not detection — it is removing your phone's cellular radio from the equation before the encounter. Detection tells you what is happening. Passive defense and burner discipline prevent the data capture that makes detection necessary.

---

## Table of Contents

1. [What IMSI Catchers Do (and Don't Do)](#1-what-imsi-catchers-do-and-dont-do)
2. [Detection: Rayhunter](#2-detection-rayhunter)
3. [Passive Cellular Defense](#3-passive-cellular-defense)
4. [SIM Anonymity](#4-sim-anonymity)
5. [Burner Device Discipline](#5-burner-device-discipline)
6. [Resources and Next Steps](#6-resources-and-next-steps)

---

## 1. What IMSI Catchers Do (and Don't Do)

### How They Work

A cell-site simulator (CSS), marketed commercially as Stingray (Harris Corporation) or Hailstorm (Harris's 4G successor), impersonates a legitimate cell tower. Phones in the vicinity see what appears to be a high-signal-strength tower and connect to it, following the same automatic network selection protocol they use with legitimate towers.

When your phone connects to an IMSI catcher, the device captures:

- **Your IMSI** (International Mobile Subscriber Identity): the unique 15-digit identifier stored on your SIM card, which identifies your carrier account. This is the primary target of most IMSI catcher operations — knowing your IMSI allows law enforcement to identify you with your carrier.
- **Your IMEI** (International Mobile Equipment Identity): the unique device identifier, separate from the SIM, that identifies your specific physical phone.
- **Your location**: by triangulating signal strength from multiple collection points, or simply by knowing you connected to a device deployed at a specific location.

### What 2G-Mode IMSI Catchers Can Do

Older IMSI catchers and their continued use in 2G-mode can do more than just capture identity:

- **IMSI/IMEI capture** — as above
- **Active call interception**: 2G (GSM) does not provide mutual authentication — the phone authenticates to the network but the network does not authenticate to the phone. An IMSI catcher can insert itself as a man-in-the-middle and relay calls in real time, capturing voice content. This is the interception capability most people associate with "stingrays."
- **SMS interception**: same man-in-the-middle mechanism, same limitation to 2G

### What 4G-Mode IMSI Catchers Can Do

4G LTE introduced mutual authentication: both the phone and the network verify each other's identity. This substantially limits what a 4G IMSI catcher can do:

- **IMSI/IMEI capture** — still works. Newer devices (Harris Hailstorm and successors) can operate in 4G mode and capture subscriber identity without a downgrade attack.
- **Downgrade attacks**: a 4G IMSI catcher can signal to phones that 4G is unavailable, forcing them to fall back to 3G or 2G, where the older interception capabilities apply. This is why 2G disable (Section 3) is a meaningful countermeasure — it removes the fallback target.
- **Location triangulation** — still works.
- **Call and SMS interception in 4G mode** — substantially harder. 4G encryption makes transparent interception of voice and SMS very difficult without a downgrade. This is the significant limitation of 4G mode compared to 2G mode.

> [!important]
> **This is the most important nuance in cellular security**: disabling 2G on your phone significantly degrades IMSI catcher effectiveness, but it does not eliminate it. Newer Stingray-class devices operate in 4G mode and can still capture your IMSI and location without forcing a downgrade. 4G-only mode is a meaningful defense; it is not a complete one.

### Who Uses Them in the US

Confirmed U.S. government users include: FBI, DEA, NSA, Secret Service, ICE, U.S. Marshals, Army, Navy, Marine Corps, and National Guard. At least 75+ local law enforcement agencies have documented Stingray deployments, including agencies in Baltimore, Los Angeles, and Chicago.

**Confirmed oversight violations**: In 2023, it was revealed that ICE, DHS, and the Secret Service used cell-site simulators without following their own internal rules or obtaining judicial approval. Plane-mounted stingrays have been deployed over cities by the FBI and U.S. Marshals — a deployment modality that affects a much wider geographic area than vehicle-mounted devices.

### What IMSI Catchers Cannot Do

> [!note]
> **IMSI catchers cannot break end-to-end encrypted applications.** Signal, WhatsApp (when E2E is enabled), Briar, and similar apps encrypt their content with keys that do not pass through the cell network. An IMSI catcher can capture that your device sent data to Signal's servers, and can capture your IMSI (associating you with your Signal usage), but it cannot read the message content. The cellular IMSI catcher threat is to identity and location, not to the content of encrypted communications.

What IMSI catchers cannot do:
- Decrypt Signal, WhatsApp, or other E2E-encrypted app traffic
- Intercept HTTPS web traffic (TLS encryption, operating above the cellular layer, remains intact)
- Extract data from your phone's storage
- Inject software or access your device (unless deployed with additional capabilities — some more sophisticated Harris systems have claimed malware injection capability, but this is a different threat tier)

---

## 2. Detection: Rayhunter

### What Rayhunter Is

Rayhunter is EFF's open-source tool for detecting cell-site simulators in real time. Released in March 2025 and updated through late 2025, it runs on a mobile hotspot device (not your primary phone), analyzes the cellular network traffic seen by the hotspot, and flags suspicious patterns that are consistent with IMSI catcher activity.

**GitHub**: [github.com/EFForg/rayhunter](https://github.com/EFForg/rayhunter)

**EFF Rayhunter documentation**: [efforg.github.io/rayhunter/](https://efforg.github.io/rayhunter/)

**Why a separate device**: Running Rayhunter on a dedicated hotspot means your primary phone's radio is a separate target. Rayhunter analyzes what the hotspot sees — suspicious IMSI requests, unexpected protocol messages, downgrade attempts — without involving your primary device's identity.

### Supported Hardware (As of Mid-2026)

Rayhunter was built and tested primarily on the Orbic RC400L. As of 2026, the supported hardware list has expanded:

**Recommended devices (extensively tested by EFF developers):**
- **Orbic RC400L** (also branded Kajeet RC400L) — primary US device; ~$20 at Verizon retail or online; 94% detection accuracy in 2026 testing; 18-hour battery life; recommended for Americas deployment
- **TP-Link M7350** — recommended for Africa, Europe, Middle East regions; superior signal sensitivity

**Additional supported devices (functional but less tested):**
- Wingtech CT2MHS01 (Americas)
- T-Mobile TMOHS1 (Americas)
- TP-Link M7310 (Africa, Europe, Middle East)
- PinePhone and PinePhone Pro (Global)
- FY UZ801 (Asia, Europe)
- Moxee K779HSDL (Americas)

> [!warning]
> Hardware support changes as EFF updates Rayhunter. **Verify the current supported device list at [efforg.github.io/rayhunter/supported-devices.html](https://efforg.github.io/rayhunter/supported-devices.html) before purchasing hardware.** The Orbic RC400L is broadly available used and remains the primary tested device as of mid-2026.

Any device running a Qualcomm modem that exposes a `/dev/diag` interface may be compatible with Rayhunter, though untested devices are at your own risk.

### Installation

Rayhunter now includes an installer with a GUI to simplify deployment for non-technical users. The core installation path:

1. **Obtain the hardware**: Orbic RC400L is available from Verizon retail (~$20), Amazon, or eBay used. Pre-installed units are sold by privacy-focused retailers (check entropysurvival.com and similar).

2. **Install Rayhunter**:
   - Download the latest release from [github.com/EFForg/rayhunter/releases](https://github.com/EFForg/rayhunter/releases)
   - Follow the device-specific instructions at [efforg.github.io/rayhunter/orbic.html](https://efforg.github.io/rayhunter/orbic.html) for the Orbic RC400L, or the equivalent page for your device
   - The installer scripts handle the flashing and configuration; read the documentation for your specific device carefully before proceeding
   - A SIM card is required for the hotspot to connect to a network (it needs to see cell towers to detect anomalies among them)

3. **Verify it is running**: After installation, Rayhunter provides a web interface accessible from a device connected to the hotspot. Confirm the interface loads and is showing network activity.

### What Rayhunter Detects

Rayhunter analyzes the cellular protocol messages that the hotspot's modem sees and flags patterns consistent with IMSI catcher activity:

- **Unexpected IMSI requests**: legitimate towers do not request your IMSI directly in most normal operation; an unusual Identity Request message is a detection signal
- **Protocol downgrade attempts**: a sudden push to fall back from 4G/LTE to 3G or 2G without a plausible reason (you are not leaving coverage, signal is strong) is suspicious
- **Inconsistent cell tower data**: a cell tower with unusual characteristics — wrong frequency for the claimed carrier, inconsistent location data, wrong tower identity — is a detection signal
- **Suspicious base station behavior**: other anomalous protocol messages that deviate from normal network operation

### Interpreting an Alert

> [!important]
> **A Rayhunter alert does not confirm an IMSI catcher. It indicates suspicious network behavior that warrants heightened caution.**

Legitimate network operations can trigger false positives: network maintenance, handoff failures, equipment reconfiguration. A single alert in an unremarkable location may be noise. Multiple alerts in a pattern — especially coinciding with law enforcement presence, a demonstration or protest site, or a location you would expect to be a surveillance target — is more significant.

What to do when Rayhunter alerts:

1. **Note the time and precise location** — the detection log in Rayhunter's interface captures this, but also note it manually
2. **Switch your primary phone to airplane mode** — this disconnects its cellular radio; you can still use Wi-Fi if available
3. **Move away from the area** if doing so is practical and safe — IMSI catcher coverage is limited to a geographic area around the deployment; moving away removes you from coverage
4. **Do not return to cellular use until you are confident you have moved outside the deployment area**
5. **Save the detection log** for later review — if the threat is serious, share the log with a digital security researcher or EFF

### What Rayhunter Provides (and Doesn't Provide)

Rayhunter provides: real-time awareness; documentation for civil rights litigation or legal challenges; community monitoring data that feeds into the broader picture of where and when cell-site simulators are deployed.

Rayhunter does not provide: a block or shield — it detects, it does not prevent. Your phone's IMSI may already have been captured by the time Rayhunter alerts you. The value is behavioral: adjust your actions based on what Rayhunter tells you is happening.

---

## 3. Passive Cellular Defense

These measures reduce IMSI catcher effectiveness before any deployment occurs. They do not require Rayhunter or active monitoring.

### 2G Disable on iOS

Disabling 2G eliminates the downgrade-to-2G attack path that older IMSI catchers rely on for voice and SMS interception, and removes the easiest IMSI capture mechanism.

**iOS 16 and later (current path):**
Settings > Cellular > "Allow 2G" — toggle to OFF

This is a single toggle that disables 2G network connection entirely. The phone will use 4G/LTE or 5G only.

**Earlier iOS (alternative path):**
Settings > Cellular > Cellular Data Options > Voice & Data — select LTE or 5G (not "Enable 3G" and not leaving 2G in the fallback chain)

**Verify**: When the toggle is off, your phone will not fall back to 2G even in areas with weak LTE coverage. In very sparse network areas, this can cause dropped connections. The tradeoff is intentional — a dropped connection is preferable to a downgraded connection that exposes you to interception.

### 2G Disable on Android

The path varies by manufacturer and Android version:

**Stock Android (Pixel):**
Settings > Network & internet > SIMs > [your SIM] > Preferred network type — select "LTE only" or "5G/4G/3G" (excluding 2G options)

**Samsung (One UI):**
Settings > Connections > Mobile networks > Network mode — select "LTE/3G/2G (auto)" and uncheck 2G, or select "LTE only" if available

**GrapheneOS:**
Settings > Network & internet > SIMs > [your SIM] > Preferred network type — select the option excluding 2G

On some Android devices the path differs, or 2G cannot be fully disabled from the UI. Check your specific device's documentation. If 2G cannot be disabled from the settings UI, the protection is not available on that device without a different Android build.

> [!note]
> 2G disable eliminates one class of attack but not all IMSI catcher threats. Newer Stingray-class devices operating in 4G mode can still capture your IMSI and location without a downgrade. The measure is meaningful; it is not complete.

### Airplane Mode vs. Full Power-Off

These modes are not equivalent, and the distinction matters:

**Airplane mode**: Disables the cellular radio, Wi-Fi, and Bluetooth transmission. The phone remains on; the operating system is running; the SIM is seated and the IMSI is stored in memory. An IMSI catcher cannot capture your radio transmission in airplane mode, but the phone has not fully severed the cellular relationship.

**Full power-off**: The radio is completely inactive. The device cannot be triangulated by any cellular means. The SIM is inactive. This is the most complete cellular protection short of SIM removal.

**Faraday bag**: Physically blocks all radio signals — cellular, Wi-Fi, Bluetooth, NFC. The phone can be on or in airplane mode; the bag prevents any radio transmission. Effective for demonstrations or situations where you need your phone available quickly but want to eliminate radio exposure. Cannot receive calls or texts while in the bag — this is expected and intentional.

**Practical guidance by situation:**

| Situation | Recommended approach |
|---|---|
| High-risk protest or demonstration | Leave phone home; or power off + Faraday bag |
| High-risk travel where phone needed | Airplane mode + Faraday bag while not actively using |
| Routine elevated risk | 2G disabled, airplane mode when in sensitive locations |
| Border crossing (most protective) | Factory-reset travel device, or full power-off of primary device before checkpoint |
| Rayhunter alert | Airplane mode on primary phone immediately; move away |

### SIM Removal

Removing the SIM card from your phone eliminates carrier-based IMSI capture entirely — there is no IMSI to capture if no SIM is present. Your device's IMEI is still visible to any cell tower it pings (emergency calls, for example, do not require a SIM). SIM removal is most relevant when:

- Using a device purely on Wi-Fi
- Using a device with a VPN or Tor-over-data for all connectivity
- You want to ensure no incidental cellular connection occurs

SIM removal without full power-off may still leave residual radio activity on some devices. Power-off or Faraday bag is the more complete protection.

---

## 4. SIM Anonymity

### The US Legal Landscape: No Mandatory Registration

The United States does not have a federal law requiring prepaid SIM registration by name or identity. This puts the U.S. in a minority globally — over 150 countries have mandatory SIM registration laws as of 2024-2025.

In the U.S., prepaid SIM cards can be purchased at convenience stores, pharmacies, and grocery stores (Walmart, Walgreens, Target, 7-Eleven) without providing identification. The major carriers sell no-contract prepaid SIMs without mandatory ID verification at point of sale. This makes meaningful SIM anonymity possible in the U.S. — but "no registration requirement" does not automatically mean "anonymous."

### Countries Where SIM Anonymity Is Legally Impossible

If you are traveling to these jurisdictions and SIM anonymity matters to your threat model, know that local SIM purchase will require valid government identification:

- **UK**: Prepaid SIM registration required — operators must verify customer identity
- **Australia**: Mandatory registration with criminal penalties for operators who activate unregistered SIMs
- **EU member states**: Mandatory registration across the European Union; GDPR does not override registration requirements
- **Canada**: Registration required; carriers must verify customer identity for prepaid SIMs
- **China**: Strict real-name registration with biometric verification
- **Russia**: Mandatory real-name SIM registration
- **India**: Mandatory Aadhaar-linked SIM registration

In these jurisdictions, purchasing a local SIM links it to your identity by law. Using a SIM from a jurisdiction without mandatory registration, or using a SIM registered in a third country, may be an option for short-term travel — consult your threat model and the specific laws of the destination country.

### How an Anonymous US SIM Becomes De-Anonymized

Buying a prepaid SIM with cash is the starting point for SIM anonymity, but the connection to your identity is established the moment you make any of the following mistakes:

**Purchase linkage:**
- Buying the SIM with a credit or debit card — your payment record links you to the SIM at time of purchase
- Buying the SIM at a store covered by regular ALPR surveillance or your daily geographic footprint — the purchase location creates a correlation even if you paid cash
- Buying the SIM at a store with a loyalty card linked to your identity

**Activation linkage:**
- Activating the SIM at the same location where you purchased it (geographic correlation)
- Activating the SIM using a device already linked to your identity (IMEI correlation)
- Activating from a Wi-Fi network linked to you (your home router, your regular coffee shop)

**Usage linkage:**
- Powering on the SIM near your primary device simultaneously — cell towers see both devices connecting from the same physical location; this creates a correlation between your IMSI and the new SIM's IMSI
- Calling or texting anyone who has your primary number in their contacts (carrier records show contact with your known identity)
- Logging into any account (email, social media, Signal) linked to your primary identity
- Using the SIM near your home, workplace, or regular locations — pattern-of-life analysis links SIM location to known identity

> [!important]
> **A SIM is anonymous only as long as none of its data points connect to your primary identity.** The first contact with any data point linked to you ends the anonymity, and that connection is retroactive — the carrier's records of all prior activity with that SIM can now be associated with your identity.

### Practical US Approach to Anonymous SIM Acquisition

1. **Pay cash.** Credit/debit cards are definitionally linkable.

2. **Purchase outside your normal footprint.** A store you do not regularly visit, in a neighborhood you are not associated with, that is not on your regular route. The purchase itself creates a data point; minimizing its geographic connection to your identity limits what can be correlated.

3. **Activate separately from purchase.** Do not activate at the store. Activate at a third location that is not your home, workplace, or regular locations. A public place (park bench, parking lot away from cameras) is better than an identifiable indoor location.

4. **Activate on a device that is not your primary device.** Your primary phone's IMEI is associated with your identity. Use a separate device for activation — a burner device is the correct tool here (see Section 5).

5. **Do not power on the new SIM near your primary phone.** The cell tower correlation between two devices at the same location at the same time is one of the primary deanonymization mechanisms.

---

## 5. Burner Device Discipline

A "burner device" in this context is a secondary mobile device used exclusively for a specific sensitive purpose, acquired and operated in a way that creates no data-point connection to your primary identity. Done correctly, cell-tower IMSI capture of the burner device tells investigators nothing about who you are. Done incorrectly, the burner device is a liability — a record that connects two identities.

### Acquisition

**Purchase with cash.** Credit card purchase is definitionally traceable.

**Purchase at a store outside your normal footprint.** The same location analysis as SIM purchase applies: buy at a store you do not regularly visit, in a neighborhood not associated with you.

**Buy an older, inexpensive Android device.** Budget Android phones ($30-80 range: various no-name brands, older Motorola or Nokia prepaid models) are available at big-box retailers (Walmart, Target, Best Buy) and dollar stores. These are purpose-built prepaid devices and require no carrier contract.

**Do not use your regular Amazon or online accounts to purchase.** Order history is identifiable. Cash in-person purchase is the only fully anonymous acquisition method.

### Setup and Activation

**Do not power it on at home or at any location associated with your primary identity.** The first power-on creates the first IMEI record with a cell tower.

**Power it on at a neutral location** (away from home, work, and regular routes) using the anonymous SIM acquired separately.

**Do not log into any Google account** during Android setup. The device setup flow will push you to add a Google account — skip it. You do not need Google services for a burner device's intended purpose. Google accounts create persistent identity links across all connected devices.

**Skip all account setup prompts**: email, backup, "enhanced features," etc. The device should have zero account logins when operational.

**Use only Wi-Fi or cellular data through a VPN for any internet activity.** If the device has a SIM, the IMSI is exposed to towers. Route all data through Tor Browser (F-Droid distribution of Tor Browser for Android) for any sensitive online activity.

### Operational Rules

**Never power on the burner near your primary device.** This is the single most important operational rule. Both devices register with cell towers. Two devices consistently appearing at the same location simultaneously create a persistent correlation between their IMSIs. Even once is a data point; consistent co-location is definitive.

**The burner has exactly one compartment.** It is used for one specific sensitive purpose. It is not your daily communications device, your backup phone, your music player. The moment it serves a second purpose — especially a purpose connected to your primary identity — it is no longer compartmentalized.

**Never use the burner to contact anyone who knows you by your primary identity.** Calls, texts, Signal messages to your regular contacts connect the burner to your known social graph.

**Never connect to Wi-Fi networks you've used with primary devices.** Router connection records can link the burner to your home or office network identity.

**Never install apps that require account creation.** Every account login is an identity link. Apps that work without accounts (Tor Browser, F-Droid store, open-source utilities) are acceptable. Apps requiring email registration are not.

**For sensitive communications on the burner:** use Signal registered to a VoIP number (JMP.chat, MySudo) not linked to your primary identity, accessed through Orbot (Tor routing for Android) to prevent metadata association.

### Disposal

When the burner device's purpose is complete:

- **Factory reset** the device before disposal
- **Remove the SIM** and dispose of separately
- **Dispose in a location not associated with your regular waste stream** — not your home bin, not your office bin, not a recognizable neighborhood

---

## 6. Resources and Next Steps

### EFF Rayhunter

- **GitHub**: [github.com/EFForg/rayhunter](https://github.com/EFForg/rayhunter) — source code, releases, installation instructions
- **Documentation**: [efforg.github.io/rayhunter/](https://efforg.github.io/rayhunter/) — full setup guide, supported devices, detection methodology
- **Supported devices**: [efforg.github.io/rayhunter/supported-devices.html](https://efforg.github.io/rayhunter/supported-devices.html) — verify current before purchasing hardware

### EFF Street Level Surveillance

- [sls.eff.org/technologies/cell-site-simulators-imsi-catchers](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers) — comprehensive reference on how IMSI catchers work, confirmed government use, legal landscape

### ACLU Stingray Tracker

- [aclu.org/issue/national-security/privacy-and-surveillance/stingrays](https://www.aclu.org/issue/national-security/privacy-and-surveillance/stingrays) — documents which agencies have Stingray devices, state-level legal landscape, litigation tracking

### EFF Surveillance Self-Defense: Protecting Yourself at Protests

- [ssd.eff.org/module/attending-protests-united-states](https://ssd.eff.org/module/attending-protests-united-states) — covers device preparation for protest situations, including cellular considerations

### Access Now Digital Security Helpline

- [accessnow.org/help](https://accessnow.org/help) — free digital security assistance for journalists, activists, and at-risk individuals; can advise on IMSI catcher-specific concerns

### Integration With Other Guides in This Corpus

- **For the legal rights dimension of device search**: `rights-assertion-legal-playbook.md` (F-03) — what to say when asked to unlock your device
- **For device power-off discipline**: `emergency-protocols-playbook.md` (F-01) Scenario 4 and 5 — when and how to power off your device before law enforcement encounters
- **For full threat model on cell-site simulators**: `threat-model.md` Section V.C — confirmed government users, deployment methods, legal oversight failures
- **For the surveillance detection decision tree**: `surveillance-detection-guide.md` (F-02) — when to escalate your security posture based on accumulated indicators

---

## Confidence Assessment and Known Gaps

**High confidence:**
- Rayhunter hardware support and installation: primary source (EFF GitHub, EFF documentation)
- 2G disable on iOS and Android: primary source (Apple/Android device settings)
- IMSI catcher confirmed government use: primary source (EFF Street Level Surveillance, ACLU Stingray Tracker, court documents)
- Burner device discipline: operational security literature, well-established practice
- US SIM registration: confirmed no mandatory federal registration law as of 2025

**Medium confidence:**
- 4G-capable IMSI catcher capabilities: the technical landscape for commercial surveillance hardware is not always fully disclosed; the claim that newer Stingray-class devices can capture IMSI in 4G mode is documented in EFF and surveillance industry materials but not fully confirmed in court records for all deployment modalities
- SIM registration law by jurisdiction: the table reflects the situation as of mid-2026; registration laws change and should be verified for any specific country before travel

**Known gaps:**
- 5G security: 5G SA (Standalone) architecture includes SUPI (Subscription Permanent Identifier) encryption, which substantially mitigates IMSI capture at the 5G layer. However, 5G NSA (Non-Standalone, which most current US deployments use) still uses a 4G LTE anchor channel, and IMSI exposure at the LTE layer remains. Full 5G SA deployment is an evolving timeline; this guide does not yet address the 5G-specific threat model.
- Legal status of IMSI catcher use by law enforcement: warrantless cell-site simulator use is challenged in courts but has not produced a clear federal constitutional prohibition; state-level warrant requirements exist in some states. The legal landscape is evolving and jurisdiction-specific.

---

## Sources

- [EFF: Meet Rayhunter — New Open Source Tool to Detect Cellular Spying (March 2025)](https://www.eff.org/deeplinks/2025/03/meet-rayhunter-new-open-source-tool-eff-detect-cellular-spying)
- [EFF: Rayhunter Documentation](https://efforg.github.io/rayhunter/)
- [EFF: Rayhunter GitHub Repository](https://github.com/EFForg/rayhunter)
- [EFF: Rayhunter Supported Devices](https://efforg.github.io/rayhunter/supported-devices.html)
- [Help Net Security: Rayhunter — EFF Releases Open-Source Tool to Detect Cellular Spying (September 2025)](https://www.helpnetsecurity.com/2025/09/17/rayhunter-eff-open-source-tool-detect-cellular-spying/)
- [EFF Street Level Surveillance: Cell-Site Simulators / IMSI Catchers](https://sls.eff.org/technologies/cell-site-simulators-imsi-catchers)
- [EFF: Cell-Site Simulators / IMSI Catchers](https://www.eff.org/pages/cell-site-simulatorsimsi-catchers)
- [Wikipedia: Stingray Phone Tracker](https://en.wikipedia.org/wiki/Stingray_phone_tracker)
- [ACLU: Stingrays — What You Need to Know](https://www.aclu.org/issue/national-security/privacy-and-surveillance/stingrays)
- [EFF: Surveillance Self-Defense — Protecting Yourself at Protests](https://ssd.eff.org/module/attending-protests-united-states)
- [ExpressVPN: SIM-Card Registration Laws Around the World](https://www.expressvpn.com/blog/countries-with-sim-card-registration-laws/)
- [Comparitech: Which Governments Impose SIM-Card Registration Laws](https://www.comparitech.com/blog/vpn-privacy/sim-card-registration-laws/)
- [GSMA Mobile Policy Handbook: Mandatory Registration of Prepaid SIMs](https://www.gsma.com/solutions-and-impact/connectivity-for-good/public-policy/mobile-policy-handbook/consumer-protection/mandatory-registration-of-prepaid-sims/)
- [SimeonOnSecurity: RayHunter Device Comparison 2026](https://simeononsecurity.com/articles/rayhunter-device-comparison-2026-complete-review/)
- [X-Surveillance: 4G LTE IMSI Catcher / Interceptor (Hailstorm)](https://x-surveillance.com/4g-lte-imsi-catcher-interceptor/)
- [Access Now Digital Security Helpline](https://www.accessnow.org/help/)
