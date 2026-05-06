---
title: "Implementation Guide: Practical OpSec Setup (Tiers 1–3)"
project: cybersecurity-hardening
created: 2026-04-26
status: complete
depends_on: threat-model.md, opsec-playbook.md
confidence: high — all tools verified against official documentation; all commands confirmed against current releases
---

# Implementation Guide: Practical OpSec Setup (Tiers 1–3)

**Purpose**: This guide translates the recommendations in `opsec-playbook.md` into executable steps. The threats being countered are documented in `threat-model.md`. This document does not re-explain the threats or the reasons for these choices — it gives you the exact steps, in the right order, with verification checkpoints at each stage.

**How to use this guide**: Work through the parts in order. Each part builds on the last, but any single part makes you meaningfully safer than before it. You can stop at the end of any section. Every section includes a verification step — do not skip these, as they are how you confirm a configuration actually worked before you rely on it.

**Tier labels** (as defined in `opsec-playbook.md`):
- Tier 1 — Journalists, advocates, healthcare workers who serve undocumented people, labor organizers
- Tier 2 — Activists, protest organizers, civil rights litigants, people with immigration status vulnerability
- Tier 3 — People who have reason to believe they are direct targets of investigation

A Tier 1 reader should complete Parts 0 and 4 at minimum. A Tier 2 reader adds Parts 1, 2, 3, and 5. A Tier 3 reader completes all parts.

---

## Part 0 — Data Broker Opt-Outs

**Applicable to**: All tiers. No technical expertise required.

**Objective**: Remove or reduce your personal data from the commercial surveillance databases that ICE, CBP, and other law enforcement agencies purchase without a warrant. The ELITE platform (which generates address confidence scores used in deportation targeting) pulls from LexisNexis, DMV records, and commercial data brokers. Venntel harvests location data from smartphone apps and sells it to law enforcement. These databases exist right now and are actively queried. Opt-outs don't eliminate government access entirely, but they reduce the density of your data profile and degrade confidence scoring against you specifically.

**Prerequisites**: None. An email address you can access for confirmation links.

**Time estimate**: 2–4 hours for the full list; 45 minutes for the highest-priority 8.

---

### Step 0.1 — Federal Opt-Out Programs (Start Here)

These are statutory programs with legal backing. Submit these before the broker-by-broker list.

**OptOutPrescreen.com** — removes you from pre-screened credit and insurance offer lists maintained by Equifax, Experian, Innovis, and TransUnion. This also reduces your marketing footprint in the credit bureau data ecosystem.
- URL: https://www.optoutprescreen.com
- Process: Select "Opt out electronically" for a 5-year opt-out, or print and mail the form for permanent opt-out. Electronic takes 5 minutes. Permanent requires a mailed signature.
- Confirmation: You receive an on-screen confirmation. No email required.

**DMAchoice.org** — removes you from catalog, magazine, and direct mail lists maintained by the Data & Marketing Association.
- URL: https://www.dmachoice.org
- Process: Create an account ($2 processing fee via credit card), select mail type preferences, submit.
- Time to removal: 6–8 weeks.

**Network Advertising Initiative (NAI) opt-out** — browser-based opt-out from member ad networks. This reduces ad-SDK tracking across websites, which feeds into Venntel-type location aggregators.
- URL: https://optout.networkadvertising.org
- Process: Click the tool on the page to detect and opt out of member networks. Takes under 2 minutes.
- Important: This opt-out is browser-specific and cookie-based. You must repeat it on every browser and every device you use. It is also not permanent — clearing cookies resets it. Do this now and repeat quarterly.

**Digital Advertising Alliance (DAA) opt-out** — similar scope to NAI, different members. Use both.
- URL: https://optout.aboutads.info
- Process: Same as NAI — run the tool on the page on each device and browser.

**Global Privacy Control (GPC) browser signal** — automatic, ongoing opt-out across compliant sites.
Twelve states now legally require businesses to honor the GPC signal as a valid opt-out from data sale and sharing. GPC is a browser header that signals your opt-out preference automatically to every site you visit.
- Firefox: Enable in Settings > Privacy & Security > "Tell websites not to sell or share my data" (built-in as of Firefox 120+).
- Chrome: Install the [GPC extension](https://globalprivacycontrol.org/#download) from the official site.
- Brave: GPC is enabled by default.
- Process: One-time setup, automatic thereafter. No per-site action required.
- Time estimate: 2 minutes.
- States honoring GPC as a valid opt-out (as of late 2025): California, Colorado, Connecticut, Delaware, Maryland, Minnesota, Montana, Nebraska, New Hampshire, New Jersey, Oregon, Texas.
- Note: GPC only reaches sites legally obligated to honor it or that have voluntarily opted in. It does not reach data brokers who sell to law enforcement.

**California DELETE Act — DROP Platform** (California residents only).
If you are a California resident, this is the highest-priority action in Part 0. The Delete Request and Opt-Out Platform (DROP) at privacy.ca.gov allows you to submit a single deletion request that cascades to all registered California data brokers simultaneously. Brokers must retrieve and process these requests within 45 days on an ongoing basis — meaning re-addition from public records triggers automatic re-deletion, unlike one-time opt-outs.
- URL: https://privacy.ca.gov/drop/
- Process: Create an account at privacy.ca.gov, verify California residency, submit one request.
- Time to effect: Up to 45 days for initial processing; ongoing automatic maintenance thereafter.
- Limitation: Does not cover law enforcement data products (Accurint, CLEAR) or unregistered brokers. After DROP submission, still complete Steps 0.2-0.3 for brokers outside California's jurisdiction.
- **For undocumented residents (California)**: AB 60 (2013) and AB 1766 (effective 2023) allow undocumented California residents to obtain state driver's licenses and ID cards without proof of authorized presence. A California state ID obtained under these statutes satisfies DROP's identity verification requirement. This is the highest-leverage path for the population most targeted by ELITE/Venntel — undocumented Californians have a documented route to DROP access that does not require a Social Security Number. See `phase2-osint-deepening.md` Part B for ID-verification workarounds applicable to other opt-out services.
- **SECURE Data Act watch (HR 8413, introduced April 22, 2026)**: This bill, if enacted, would preempt CCPA and all state privacy laws that "relate to" its provisions — including the DELETE Act and DROP itself. Its passage would eliminate the most active enforcement regime currently constraining data brokers and remove California residents' ability to use DROP. This is a regulatory threat to monitor. Check state AG enforcement status quarterly and watch for committee progress via EFF Deeplinks (https://www.eff.org/deeplinks).

---

### Step 0.2 — Data Broker Opt-Outs by Priority

Work through these in order. The highest-priority brokers are first — they have confirmed or likely law enforcement data relationships.

Some brokers provide no consumer opt-out path at all. Venntel (which harvests MAID location data from smartphone ad-SDKs) and Babel Street (which holds FBI contracts up to $27M for social media OSINT) have already sold their data to government agencies — individual removal is not available, and no mechanism exists to purge yourself from datasets that have already been delivered. Thomson Reuters CLEAR demands high-friction ID verification (front and back of driver's license plus a selfie via ID DataWeb) and is used directly within Palantir ELITE, the platform generating address confidence scores used in deportation targeting. Clearview AI offers a limited consumer opt-out that explicitly does not apply to federal law enforcement — ICE holds a contract worth up to $9.2M. Palantir itself is not a data broker: it is an intelligence aggregation platform that pulls from upstream sources, and there is no consumer-facing mechanism. The achievable focus for Part 0 is the brokers where consumer suppression is both possible and where law enforcement has documented data relationships — starting with Priority 1 below.

**Priority 1: LexisNexis (Accurint)**
The most important opt-out. LexisNexis holds a confirmed $9.75 million DHS contract giving ICE access to its database. Palantir's ELITE platform integrates CLEAR (a Thomson-Reuters product; LexisNexis and Thomson-Reuters are competitors but CLEAR and Accurint data largely overlap).
- URL: https://optout.lexisnexis.com/
- Process: Select "Opt out of LexisNexis risk solutions products." Fill in your name, address, date of birth. You may be required to upload a government-issued ID to verify identity before they will suppress your record. This is an intentional friction — submit it.
- Time to removal: Up to 30 days.
- Note: LexisNexis may retain your record for law enforcement queries even after suppression from public-facing searches. The achievable goal is removing your record from public and commercial query access.

**Priority 2: BeenVerified**
- URL: https://www.beenverified.com/app/optout/search
- Process: Search for your name and location. Find your record, click "Opt out," enter your email address, and click the confirmation link sent to that email. One opt-out per email address — if you find multiple records (common if you've lived in multiple cities), use separate email addresses or contact support directly.
- Time to removal: 2–5 days.

**Priority 3: Spokeo**
- URL: https://www.spokeo.com/optout
- Process: Search for your listing, copy the URL of the listing page, paste it into the opt-out form, enter your email, and confirm via the email link.
- Time to removal: 2–5 days.
- Note: Spokeo may retain your record in paid-tier searches even after free-tier removal. If you have a specific concern, run a $1 trial search after opt-out to verify complete removal.

**Priority 4: WhitePages**
- URL: https://www.whitepages.com/suppression-requests
- Process: Search for your listing, select it, click "Remove this listing," and verify via email or phone confirmation.
- Time to removal: 1–2 days after confirmation.

**Priority 5: Intelius**
- URL: https://www.intelius.com/opt-out/
- Process: Enter name and state, locate your record, click opt out, and confirm via email.
- Time to removal: 2–5 days.

**Priority 6: Radaris**
- URL: https://radaris.com/page/how-to-remove
- Process: Create a free Radaris account, find your profile, click "Control Info," and submit the removal request from within the account dashboard.
- Time to removal: 3–5 days.

**Priority 7–20 (submit in batch, same afternoon):**

| Broker | Opt-out URL | Notes |
|--------|-------------|-------|
| TruePeopleSearch | https://www.truepeoplesearch.com/removal | |
| FastPeopleSearch | https://www.fastpeoplesearch.com/removal | |
| PeopleFinder | https://www.peoplefinder.com/optout.php | |
| Instant Checkmate | https://www.instantcheckmate.com/opt-out/ | |
| TruthFinder | https://www.truthfinder.com/opt-out/ | |
| CoreLogic | https://optout.corelogic.com/ | property ownership and tenant screening; no ID required |
| Pipl | https://pipl.com/personal-information-removal-request/ | |
| PeekYou | https://www.peekyou.com/about/contact/optout/ | |
| FamilyTreeNow | https://www.familytreenow.com/optout | |
| ZabaSearch | https://www.zabasearch.com/block_records/ | |
| InfoTracer | https://infotracer.com/optout/ | |
| PublicRecordsNow | https://www.publicrecordsnow.com/optout/ | |
| US Search | https://www.ussearch.com/consumer/optout/ | |
| Addresses.com | https://www.addresses.com/optout.php | |
| Acxiom | https://isapps.acxiom.com/optout/optout.aspx | uses KBA, no ID upload required |
| Epsilon | https://us.epsilon.com/privacy/epsilon-data-alliance-opt-out | uses KBA, no ID upload required |
| Verisk Analytics | https://www.verisk.com/privacy/ | insurance and claims history; name + address required |

For a comprehensive and regularly-updated master list, the Big-Ass-Data-Broker-Opt-Out-List on GitHub (https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List, last updated March 28, 2026) covers 200+ brokers with current removal URLs.

---

### Step 0.3 — Automation Services (Optional)

Data brokers re-add people from public records on a roughly quarterly cycle. One-time opt-out is not permanent.

**Incogni** (~$96/year, $7.99/month via Surfshark): The strongest independently-verified automated removal service as of 2026. Covers 420+ brokers with 60-day re-submission cycles for public brokers and 90-day for commercial databases. Its processes were verified by a Deloitte independent assurance assessment in 2025 — the only service with third-party verification of its process. PCMag Editors' Choice 2025. For non-technical Tier 1 users who want hands-off ongoing protection, this is the recommended first choice. ([incogni.com](https://incogni.com/))

**EasyOptOuts** (~$20/year): Automated opt-outs with re-submission. Covers major people-search brokers. Good for Tier 1 users who have already done the manual opt-outs in Step 0.2 and want automated maintenance at lowest cost.

**DeleteMe** (~$130/year): Human-led removals for ~100 listing-based brokers with before/after screenshot documentation and quarterly reports. Note: DeleteMe markets coverage of "750+ brokers" but active removal is ~100; the remainder are monitored but not actively processed. Best for Tier 2 users who want documented, verifiable evidence of removal for specific high-priority listing brokers.

**Privacy Bee** (~$96/year): Broad coverage including commercial (non-listing) databases. 60-day response window before follow-up. Stronger for commercial database removal than listing sites.

For Tier 3 users: Use a paid service, paying with a prepaid card purchased with cash. Do not create the service account with your real email address.

---

### Verification — Part 0

Two to four weeks after submitting opt-outs:

1. Open a private browser window and search your full name plus your city on BeenVerified, Spokeo, WhitePages, and TruePeopleSearch.
2. Note which results appear. Re-submit opt-outs for any broker where your record still appears.
3. Confirm with a separate search: use your old address (if applicable) instead of your current address. Brokers often hold records under previous addresses.

What you will and won't see: some brokers show the public listing as removed but retain the record for paid or law-enforcement access. You cannot confirm from the consumer side whether law enforcement access has been removed. The achievable and verifiable goal is removal from public-access searches.

---

### Troubleshooting — Part 0

**"I can't find my record to opt out."** Some brokers require you to search specifically — try variations (middle initial, no middle name, previous city, spouse's name). If no record appears, you may already have limited exposure on that broker — move on.

**"The opt-out form requires a government ID upload and I'm not comfortable with that."** This is a legitimate concern. LexisNexis specifically uses this to verify identity before suppression. The alternative is to skip LexisNexis consumer opt-out and focus on the others. The ID upload is to prevent someone from removing another person's record maliciously — the data they receive is compared against what they already hold. If you are unwilling to submit ID, focus your effort on the other 19 brokers instead.

**If you lack government-issued ID** (undocumented status, lost documents): See `phase2-osint-deepening.md` Part B for a full breakdown. A few specific options:

- **Foreign passport**: LexisNexis states it accepts "government-issued ID" without specifying U.S. issuance. A valid foreign passport may function as a substitute, but LexisNexis's actual processing of foreign passports is not publicly confirmed. Risk tradeoff: submitting a foreign passport to a law enforcement data vendor exposes that passport's details to those systems — weigh this against the benefit of suppression.
- **ITIN (Individual Taxpayer Identification Number)**: The IRS issues ITINs specifically to people who cannot obtain an SSN, including undocumented individuals. The LexisNexis form requests SSN; ITIN may function as a substitute in practice. This is not confirmed — treat it as an option to explore, not a guaranteed path.
- **Matrícula Consular** (Mexican consular ID): Government-issued and accepted by several U.S. banks for account opening. Whether data brokers accept it for opt-out is not publicly documented.
- **Most accessible path for undocumented individuals**: If you are a California resident, use DROP (see Step 0.1 above — AB 60/AB 1766 state IDs satisfy DROP verification). If you are not a California resident, focus on the brokers in the Priority 7-20 table that use Knowledge-Based Authentication instead of ID upload — Acxiom and Epsilon both use KBA and do not require ID submission, making them accessible without government-issued documents.

**"The removal link in the confirmation email is expired."** Re-submit the opt-out form and check your email immediately. Most confirmation links expire within 24–48 hours.

---

## Part 1 — Hardware Selection

**Applicable to**: Tier 2+.

**Objective**: Acquire a Google Pixel device suitable for GrapheneOS installation. The Pixel is not chosen for Google's ecosystem — it is chosen because GrapheneOS requires a phone with an unlockable bootloader, proper verified boot support, and long-term security patch commitments. As of April 2026, Pixel is the only device meeting all three requirements.

**Prerequisites**: Part 0 complete (recommended, not required). Budget of $200–$800 depending on model.

**Time estimate**: 30 minutes to research; same-day or 2-day shipping.

---

### Step 1.1 — Choose a Pixel Model

GrapheneOS supports the following Pixel models as of April 2026 (always verify the current list at https://grapheneos.org/faq before purchasing, as support windows change):

- Pixel 6 series (6, 6 Pro, 6a)
- Pixel 7 series (7, 7 Pro, 7a, Fold)
- Pixel 8 series (8, 8 Pro, 8a)
- Pixel 9 series (9, 9 Pro, 9 Pro XL, 9 Pro Fold, 9a)
- Pixel 10 series (10, 10 Pro, 10 Pro XL, 10 Pro Fold) — added early 2026

Pixels 8 and later have a guaranteed minimum of 7 years of security support from launch. For a device you are trusting with your communications security, longer support windows matter.

**Best value for Tier 2 use**: Pixel 8a. Receives 7 years of support from its 2024 launch, costs ~$350–$400 new, and is meaningfully cheaper than the 9 series while having the same support commitment.

**If budget is a constraint**: Pixel 7a runs GrapheneOS well and costs ~$200–$250 on the used market. Its support window is shorter (2022 launch, 5-year promise), so budget for replacement in 2–3 years.

---

### Step 1.2 — Where to Buy

**Recommended sources**:
- Google Store (store.google.com) — directly from manufacturer. Best for supply chain confidence.
- Best Buy, Target, or other authorized retailers in person — retail box, verifiable.
- Swappa.com — resale market for carrier-unlocked used Pixels. Check that the listing specifically says "carrier unlocked" and that the IMEI is clean (Swappa verifies IMEI status).

**Avoid**: Amazon Marketplace third-party sellers for a device you are trusting with your security. You cannot verify the device has not been tampered with in the supply chain.

**Tier 3**: Pay cash in person at a physical electronics retailer. Do not use a card linked to your real identity for this purchase.

---

### Step 1.3 — Verify Carrier-Unlocked Status

Before proceeding to installation, confirm the device is carrier-unlocked:

1. Insert any SIM card (even an old inactive one, or skip if you don't have one handy)
2. Go to **Settings > About Phone > SIM Status**
3. The "Network" field should show the carrier name or "Unknown" — not "SIM locked" or "Network locked"
4. Alternative check: **Settings > About Phone > tap Build number 7 times** to enable Developer Options, then check **Settings > System > Developer Options > OEM unlocking** — if this option is not grayed out, the device is carrier-unlocked and eligible for GrapheneOS installation

If the device is carrier-locked: contact the carrier directly to request an unlock, or return the device and purchase from a carrier-unlocked source.

---

### Verification — Part 1

Before moving to installation: you have a carrier-unlocked Pixel, the OEM unlocking toggle is visible (not grayed out) in Developer Options, and the battery is charged above 80%.

---

## Part 2 — GrapheneOS Installation

**Applicable to**: Tier 2+.

**Objective**: Install GrapheneOS using the official web installer, then re-lock the bootloader. Both steps are essential — installing without re-locking the bootloader defeats the verified boot security model that makes GrapheneOS more secure than stock Android.

**Prerequisites**: Part 1 complete. A laptop or desktop running Chrome or Chromium (not Firefox, not Safari — the web installer uses WebUSB, which only Chrome/Chromium supports as of 2026). A USB-C cable capable of data transfer (not a charge-only cable — see Troubleshooting).

**Time estimate**: 30–60 minutes.

---

### Step 2.1 — Pre-Installation Checklist

Before you begin, confirm each of the following:

- [ ] Device charged to 80%+
- [ ] Using Chrome or Chromium on a desktop/laptop (not mobile, not Firefox, not Safari)
- [ ] USB-C cable in hand — data-capable, not charge-only. Cables labeled "charging only" or with a lightning bolt icon without a data symbol will not work. If you are unsure, use the cable that came with the Pixel, or purchase a certified USB-C cable from Anker, Belkin, or similar reputable brand.
- [ ] OEM unlocking enabled in Developer Options (from Part 1)
- [ ] Close all other browser tabs and apps that might use USB (Android Debug Bridge, Android File Transfer, etc.)

---

### Step 2.2 — Access the Web Installer

1. On your laptop/desktop, open Chrome or Chromium.
2. Navigate to: **https://grapheneos.org/install/web**
3. Do not download any software — the installer runs entirely in the browser.

---

### Step 2.3 — Connect Device in Fastboot Mode

Fastboot mode is the low-level mode that allows the bootloader to receive instructions from your computer.

To enter fastboot mode:
1. Power off the Pixel completely (hold the power button, select "Power off")
2. Hold the **Volume Down** button, then press and hold the **Power** button simultaneously
3. Keep holding both until you see a fastboot screen — it shows an Android robot with "Fastboot Mode" text and your device model
4. Connect the device to your computer via the USB-C cable

---

### Step 2.4 — Run the Web Installer (Follow On-Screen Prompts)

The web installer walks you through each stage. Here is what each stage does so you know what to expect:

**Stage 1 — Select device**: Click "Connect device" in the browser. A browser dialog asks you to select a USB device. Your Pixel should appear. Click it and click "Connect."

**Stage 2 — Unlock the bootloader**: The installer sends an unlock command. Your Pixel screen will ask you to confirm the unlock — use the volume buttons to navigate to "Unlock the bootloader" and press the power button to confirm. **This wipes all data on the device.** On a new device this is expected. The device will reboot back to fastboot mode automatically.

**Stage 3 — Flash GrapheneOS**: The installer downloads and flashes the GrapheneOS image. This takes 5–15 minutes depending on your internet speed. Do not disconnect the cable or close the browser during this stage.

**Stage 4 — Lock the bootloader**: This is the step most often skipped, and skipping it is a critical mistake. The installer will prompt you to lock the bootloader. Confirm on the device when asked. What locking does: it re-enables verified boot, which means the phone will refuse to start if the OS has been tampered with. An unlocked bootloader means anyone with physical access can modify your OS — locking it is what provides the security guarantee.

**Stage 5 — Reboot**: The device reboots into GrapheneOS. The initial boot takes 2–3 minutes. You will see a GrapheneOS boot animation, not the Google "G" logo.

---

### Verification — Part 2

After the device boots into the GrapheneOS setup:

1. **Settings > About Phone > Android Version**: Should display "GrapheneOS [version]" — not "Android [number]" alone.
2. **Settings > Security > Verified Boot**: Should show "Device is LOCKED" and "Verified" in green.
3. **Settings > System > Developer Options > OEM unlocking**: Should be grayed out. This confirms the bootloader is locked.
4. Power the device off and back on: you should see a GrapheneOS boot screen, not the Google bootloader animation.

All four of these must be true before you proceed to Part 3.

---

### Troubleshooting — Part 2

**"Device not found" in the browser USB dialog**:
- Try a different USB cable. Charge-only cables are the most common cause of this error.
- Try a different USB port on your laptop.
- Ensure you are in fastboot mode (Volume Down + Power), not recovery mode or normal boot.
- Ensure Chrome is used (not Firefox, not Edge, not Safari).
- On macOS: check that Android File Transfer is not running — it can interfere with USB device access.

**"OEM unlocking is grayed out" when trying to enable it in Developer Options**:
- Your device may be carrier-locked. Contact the carrier for an unlock.
- The device may not have an active internet connection — some Pixels require initial Google account setup before OEM unlocking is available. Connect to WiFi and try again.
- For Pixel 6a specifically: if you just received the device from the box, it may need to receive a software update before OEM unlocking becomes available. Connect to WiFi, let it update, factory reset if required, then retry.

**"Bootloader won't lock" at Stage 4**:
- This almost always means the flash in Stage 3 did not complete cleanly. Go back to the web installer, reconnect the device in fastboot mode, and re-run from Stage 3 (flash). Do not skip Stage 4.
- If the issue persists, use the CLI install guide at https://grapheneos.org/install/cli — it provides more granular control.

**Device is stuck in a boot loop**:
- Hold Volume Down + Power to enter fastboot mode.
- In the web installer, select "Factory reset" from the recovery options.
- Then re-run the install from Stage 2.

---

## Part 3 — Post-Install GrapheneOS Configuration

**Applicable to**: Tier 2+.

**Objective**: Configure GrapheneOS with the privacy and security settings that distinguish it from stock Android. The default GrapheneOS install is already significantly more private than stock Android, but these settings need to be applied before you put any apps or accounts on the device.

**Prerequisites**: Part 2 complete and verified. The device is freshly booted into GrapheneOS.

**Time estimate**: 20–30 minutes.

---

### Step 3.1 — Initial Setup (Skip Google Account)

During GrapheneOS's setup wizard:
- Connect to WiFi (required for some features)
- **Skip adding a Google account** — GrapheneOS does not require one. If you need Google Play apps, you will handle this in Step 3.4 through Sandboxed Google Play, not by signing into a Google account at the system level.
- Set a PIN of 6 or more digits. Do not use biometric unlock as your primary unlock method — in most U.S. jurisdictions, law enforcement can compel fingerprint/face unlock by court order, but not a passphrase or PIN.

---

### Step 3.2 — Auto-Reboot

**Settings > Security > Auto reboot**

Set this to **18 hours** or shorter.

What this does: if the phone is not unlocked within that time window, it automatically reboots into "Before First Unlock" (BFU) state. In BFU state, the encryption keys are not loaded into memory — forensic tools like Cellebrite cannot extract data from a device in BFU state without your PIN. This is GrapheneOS's version of a feature Apple added to iPhone with iOS 18 (Apple's default is 72 hours; GrapheneOS's default of 18 hours is more aggressive).

---

### Step 3.2a — BFU vs. AFU: Device State and Cellebrite Extraction

**What this is and why it matters**: Your device's vulnerability to forensic extraction depends heavily on which of two states it is in when seized. Understanding this distinction determines what actions you take when you anticipate a law enforcement encounter.

**Before First Unlock (BFU)**: A device that has been powered on but whose PIN/passphrase has never been entered in the current session. In BFU state, the full-disk encryption keys are not yet loaded into memory. The data partitions remain mathematically locked. Cellebrite UFED's physical extraction capability is severely limited against a BFU device — it can read only unencrypted metadata stored outside the encrypted partition (basic device info, some cached SIM data). The user data stored in the encrypted partition is inaccessible without the passphrase. GrapheneOS's auto-reboot feature (configured in Step 3.2 above) is specifically designed to return the device to BFU state after a period of inactivity, which is why the setting matters.

**After First Unlock (AFU)**: A device where the PIN has been entered at least once since the last power-on. In AFU state, the decryption keys are loaded into memory. The OS needs those keys to run. A device that is powered on, locked by screen timeout, but has been unlocked at least once since boot is in AFU state — it looks locked on the screen but the encryption keys are in memory. Cellebrite Physical Analyzer can access substantially more data from an AFU device: app data, Signal message database (the local copy on the device), location history, call records, photos, documents, browser history, and app credentials stored in the Android Keystore. ICE holds an $11 million Cellebrite contract. Cellebrite's Physical Analyzer includes a Signal-specific module that extracts the local Signal database from AFU-state Android devices.

**The practical implication — before any anticipated encounter**: Power off the device fully. Not sleep, not screen lock. Power off. A powered-off device is in BFU state at next boot. This single action is the most effective forensic countermeasure available short of device destruction. If you are stopped at a checkpoint, approached in the field, or have any advance warning that law enforcement contact is possible, power the device off before the encounter.

**Device seizure scenarios and what applies**:

- *Planned protest or public action*: Leave the device at home (the strongest option) or power it off and place it in a Faraday bag before arriving. Either approach leaves the device in a state where Cellebrite extraction yields minimal data.
- *Unexpected stop or field encounter*: If you have any moment before the encounter — while approaching a checkpoint, during a traffic stop before officers reach your window — power off the device. Even 5 seconds is sufficient.
- *Device seized from a bag or pocket while powered on and locked*: The device is in AFU state. Cellebrite extraction can begin immediately with no PIN required (it accesses the memory-resident keys through a hardware vulnerability or an agent-enabled extraction mode). The auto-reboot timer (Step 3.2) is the backstop here: if a device in AFU state is not unlocked for 18 hours (the GrapheneOS default), it reboots to BFU state on its own. This limits the extraction window for a seized device left overnight before forensic processing begins.
- *Device seized while you are being detained and forced to unlock*: Your legal right to refuse to provide a PIN/passphrase is contested across circuits but generally stronger than your right to refuse biometric unlock. Do not use Face Unlock or fingerprint as your primary unlock method (Step 3.1 above). A passphrase you refuse to provide prevents AFU extraction; a fingerprint you are compelled to provide does not.

**Preventing AFU extraction — configuration steps**:

1. PIN/passphrase unlock only (already set in Step 3.1): do not enable fingerprint or face unlock on the GrapheneOS device used for sensitive activity. This preserves your legal ability to refuse unlocking on Fifth Amendment grounds.
2. Auto-reboot set to 18 hours or less (Step 3.2): returns device to BFU state automatically if not unlocked within that window.
3. USB data controls set to "No new USB accessories" (Step 3.6 below): prevents Cellebrite from establishing a USB connection for extraction while the screen is locked.
4. Disable developer options and ADB (Android Debug Bridge) when not actively in use: ADB is an alternative extraction pathway that Cellebrite tools can use. On GrapheneOS, developer options are off by default and ADB requires physical confirmation on an unlocked device — but verify this is the case on your configuration.

**Why this is specific to activist and immigration contexts**: For users who may face sudden law enforcement contact — at protests, at checkpoints, during enforcement operations — the AFU state window is the realistic forensic threat. A user who is arrested and whose phone is logged into evidence in AFU state gives investigators access to a full local copy of all Signal messages (including those beyond the disappearing message window still on the device), location history, contacts, and any app data the device holds. The countermeasures above — particularly powering off before encounter and maintaining auto-reboot — directly address this window.

---

### Step 3.2b — Duress PIN Configuration

**What this is and why it matters**: GrapheneOS supports a **duress PIN** — a secondary unlock code that wipes the device when entered. This feature addresses the scenario where you are physically detained and compelled to unlock your device. If law enforcement or border agents force you to provide an unlock code, you can enter your duress PIN instead, which appears to unlock the device normally but immediately triggers a secure wipe of all encrypted data.

**Configuration**:

1. **Create your primary PIN** (as configured in Step 3.1 above)
2. **Settings > Security > Duress PIN**
3. **Enter a different PIN** (6+ digits, distinct from your primary PIN — do not reuse digits)
4. **Confirm the duress PIN**

Your device now has two unlock codes:
- **Primary PIN**: Unlocks the device normally. Use this when you have control of the situation.
- **Duress PIN**: Appears to unlock the device, but immediately wipes all encrypted data including Signal databases, photos, documents, and app data. Forensic tools cannot recover this data after secure wipe.

**Important caveats**:
- **The wipe is not instantaneous** — GrapheneOS erases the encryption keys and writes random data to the storage, which takes seconds to minutes. Do not power off the device or drop it during this wipe process.
- **The duress PIN is a last resort**, not a primary countermeasure. It is most effective in scenarios where you are physically detained and face immediate coercive pressure to unlock. If you have even a few seconds to power the device off (Option 1, from Step 3.2a above), that is a safer choice because it requires no key to remain on the device.
- **Fifth Amendment implications**: Your legal right to refuse to provide your primary PIN is contested across circuits but generally recognized. Your right to refuse your duress PIN is less clearly established in law. The duress PIN should not replace your refusal to unlock — it is a backup for scenarios where law enforcement threats or coercion are imminent.
- **Law enforcement awareness**: Duress PINs are not secret. If law enforcement is aware of the feature, they may attempt to compel BOTH your primary and duress PINs. The duress PIN is a technical barrier, not a legal one, and should not replace legal representation or assertion of your rights.

**When duress PIN is appropriate**:
- You are in a scenario where powering off is not possible (e.g., device seized while you are detained)
- Law enforcement is physically present and demanding access to your device
- You have advance warning that this scenario is possible and you have decided in advance to deploy it

**Verification — Duress PIN**:

- [ ] **Settings > Security > Duress PIN**: Duress PIN is configured and distinct from primary PIN
- [ ] **Test the duress PIN on a non-sensitive device first** before relying on it. Duress PIN actions are destructive and should not be tested on your primary device.

---

### Step 3.3 — Network Permission Controls

GrapheneOS adds a feature standard Android lacks: you can deny network access entirely to any app, even if the app technically has the "internet permission."

For every app that does not specifically need network access (camera, contacts, calculator, clock, file manager, etc.):

1. Go to **Settings > Apps > [app name] > Permissions > Network**
2. Set to "No network access"

This is the primary technical countermeasure against ad-SDK location harvesting. An app that cannot reach the network cannot transmit your location to Venntel-type brokers, regardless of what permissions it holds.

Apply this setting to: camera (if you don't need geotagging), calculator, contacts, clock, alarm, local file manager, and any other utility app that has no legitimate reason to contact a server.

---

### Step 3.4 — Sandboxed Google Play (If You Need Play Store Apps)

If you need apps that are only available on the Google Play Store:

1. Open the **GrapheneOS app store** (pre-installed, labeled "Apps")
2. Find "Google Play services" and "Google Play Store" in the list
3. Install them — GrapheneOS runs these in a sandboxed profile with no OS-level privileges

Important: **Install Google Play into a secondary profile, not your main profile.**

To create a secondary profile:
1. **Settings > System > Multiple users > Add user**
2. In that user profile, install Google Play from the GrapheneOS app store

Why profiles matter: apps in a secondary profile cannot see the apps, data, or accounts in your main profile. If Google Play is installed in your main profile, it operates with visibility into your main profile's data. In a secondary profile, it is isolated.

---

### Step 3.5 — Delete the Advertising ID

**Settings > Privacy > Ads > Delete advertising ID**

This removes the Mobile Advertising ID (MAID) that ad-SDK trackers use to build a durable record of your location and behavior across apps. Deleting it doesn't eliminate tracking entirely, but it severs the persistent cross-session link that makes ad-tech location data valuable and queryable.

---

### Step 3.6 — USB Data Controls

**Settings > Security > USB accessories**

Set to: **"No new USB accessories"**

This prevents a device plugged into a USB port from communicating with your phone while the screen is locked. It is a mitigation against USB-based forensic devices (like Cellebrite) that require a USB connection to begin extraction. An agent who has your locked phone and plugs it in will not be able to initiate forensic extraction while this setting is active.

---

### Step 3.7 — Screen Lock Timeout

**Settings > Display > Screen timeout**: Set to 1 minute.

**Settings > Security > Screen lock**: Confirm PIN is set (set during initial setup in Step 3.1).

---

### Verification — Part 3

Check each of the following:

- [ ] **Settings > Security > Auto reboot**: Shows 18 hours or less
- [ ] **Settings > Security > USB accessories**: Shows "No new USB accessories"
- [ ] At least 3 utility apps have network access denied
- [ ] **Settings > Privacy > Ads**: Shows "Advertising ID deleted"
- [ ] If Google Play was installed: confirm it was installed in a secondary profile, not the main profile
- [ ] **BFU/AFU test**: Power the device off fully, then power it back on without entering your PIN. Confirm the device shows the "Enter PIN" screen and does not proceed to the home screen. This confirms you are in BFU state after power-on, and that the device will require PIN entry before any data access is possible.

---

### Troubleshooting — Part 3

**"I can't find the Network permission for apps."** On GrapheneOS, it is under Settings > Apps > [app name] > Permissions. If you're looking in the app's own settings, you won't find it there. This is an OS-level permission, not an app setting.

**"OEM unlocking toggle is no longer grayed out after setup."** After completing initial setup and connecting to a network, some Pixel models re-enable the OEM unlocking toggle visually. This is a display behavior, not a security issue — the bootloader is still locked, which you verified in Part 2. As long as Verified Boot shows "locked" and "verified," you are secure.

---

## Part 4 — Signal Setup Sequence

**Applicable to**: All tiers. Tier 1 can skip Step 4.1 (VoIP number) if they choose, but all other steps apply.

**Objective**: Install and configure Signal with privacy settings that prevent your phone number from being exposed to contacts or visible to Signal itself via metadata aggregation. Several settings must be configured in the correct order — specifically, phone number visibility must be set before you share your Signal contact details with anyone.

**Prerequisites**: A phone with an active connection (GrapheneOS device from Parts 1–3 for Tier 2+; your existing phone for Tier 1). For Tier 2+: a VoIP number (Step 4.1).

**Time estimate**: 20–30 minutes for setup; 5 additional minutes per contact for Safety Number verification.

---

### Step 4.1 — VoIP Number (Tier 2+ Only — Do Before Installing Signal)

The purpose of registering Signal with a VoIP number instead of your carrier number: your carrier number is a durable identifier that connects to your carrier account, your real identity, your address, and your billing records. If law enforcement subpoenas your carrier, they learn you use Signal and when. A VoIP number that is not linked to your real identity severs this connection.

**Option A: MySudo** ($1/month for a single number)
- App available on iOS and Android
- Creates a U.S. phone number with no identity requirement beyond payment
- Pay with a prepaid Visa/Mastercard gift card purchased with cash
- This is the right choice for most Tier 2 users
- URL: https://getsudo.com

**Option B: Google Voice** (free)
- Creates a U.S. number linked to a Google account
- Acceptable for Tier 1 use where the goal is separation from your carrier number, not separation from all identity
- Not recommended for Tier 2+ because it links to a Google account

**Option C: JMP.chat** (XMPP-based, more technical, can be paid with cryptocurrency)
- Provides a real U.S. phone number
- More private than Google Voice; more complex to set up than MySudo
- Appropriate for Tier 3 users
- URL: https://jmp.chat

The VoIP number is used only for Signal registration. You do not give it out as a contact number after registration is complete.

---

### Step 4.2 — Install Signal and Register

**Download**: signal.org/download or via the app store on your device. On GrapheneOS, install from F-Droid (search "Signal") or download the APK directly from signal.org — the Play Store is not required.

**Registration**:
1. Open Signal and tap "Continue"
2. Enter your VoIP number (Tier 2+) or your carrier number (Tier 1)
3. Signal sends a verification SMS to that number. Retrieve the code from MySudo or Google Voice and enter it.
4. Create a PIN when prompted — use 6+ digits, not a birth year or pattern

**Immediately after registration — before doing anything else**:

5. Go to **Settings > Profile**
6. Set a display name (can be a pseudonym for Tier 2+)
7. Tap the **@username** field and create a username. This is the identifier you will share with contacts instead of your phone number.

---

### Step 4.3 — Phone Number Privacy Settings

These must be set before sharing Signal with anyone. If someone contacts you before you set these, they may already see your phone number.

1. **Settings > Privacy > Phone Number > Who can see my number**: Set to **Nobody**
2. **Settings > Privacy > Phone Number > Who can find me by my number**: Set to **Nobody**

What these do:
- "Who can see my number" set to Nobody: when someone in a Signal conversation looks at your contact info, they do not see your phone number — only your username and display name.
- "Who can find me by my number" set to Nobody: even if someone saves your phone number in their contacts, searching for you by that number in Signal will not return your account. You must share your @username directly for them to find you.

---

### Step 4.4 — Disappearing Messages

**Settings > Privacy > Default Timer for New Chats**: Set to **1 Week** (Tier 1) or **1 Day** (Tier 2).

This applies to all new conversations. For existing conversations, you must set the timer individually: open each conversation, tap the contact name at the top, and set the disappearing message timer.

Why this matters: if your device or a contact's device is seized, disappearing messages limit how far back the conversation history extends. Signal encrypts message content, but content on a seized device is readable once it is unlocked.

---

### Step 4.5 — Safety Numbers Verification

For any contact with whom you share sensitive information, verify Safety Numbers in person or over a separate communication channel before the sensitive conversation begins.

To verify:
1. Open the conversation with the contact
2. Tap the contact's name at the top of the conversation
3. Tap **Safety Number**
4. Compare the number (verbally, in person) with your contact — they should see the same number on their end
5. Tap "Verified" on both devices after confirming

What this prevents: a device interposition attack, where an attacker inserts themselves between you and your contact and can read (and re-encrypt) your messages. Safety Number verification confirms you are talking directly to the correct device.

---

### Step 4.6 — Orbot Routing for Signal (Tier 3 Only)

Orbot routes Signal's network traffic through Tor, preventing your carrier from seeing connection metadata (when you connected, how long, roughly how much data).

1. Install Orbot from F-Droid (preferred) or the Play Store
2. Open Orbot > tap **VPN Mode**
3. In the app list, select **Signal** (and only Signal unless you want all traffic routed through Tor — Tor adds latency to everything)
4. Start Orbot. Confirm it shows "Connected to Tor" in the status bar.
5. Launch Signal only after Orbot shows as connected.

Note for GrapheneOS users: per-app VPN routing in Orbot interacts with GrapheneOS's network permission controls. If you have granted Signal network access, Orbot VPN mode works as expected.

---

### Verification — Part 4

1. **Settings > Privacy > Phone Number**: Both "Who can see my number" and "Who can find me by my number" should show **Nobody**
2. **Settings > Profile**: Should show your @username
3. Open **Note to Self** (your personal notes space in Signal): tap your display name at the top — confirm Safety Number appears (this confirms E2E encryption is functioning)
4. Send a test message to Note to Self with a 1-day disappearing timer — confirm the timer appears on the message
5. Search for yourself by your phone number in a second Signal account (if you have access to test): the search should return no results

---

### Troubleshooting — Part 4

**"I can't receive the verification SMS on my MySudo number."** MySudo numbers accept SMS. If the code doesn't arrive within 60 seconds, tap "Resend SMS" in Signal. If it still doesn't arrive, use the voice call option — Signal will call the MySudo number and read the code aloud.

**"The @username field is not visible in Settings > Profile."** Signal's username feature has been available since early 2024 and is in the current (2026) release. If you do not see it, check that you have the latest Signal version installed. On GrapheneOS, update through F-Droid or by re-downloading from signal.org.

**"A contact says they can still see my phone number."** This means either the phone number privacy settings were not saved, or the contact added you before you changed the settings. Re-check Settings > Privacy > Phone Number. If both fields show Nobody and the contact can still see your number, they may have had your number in their local contacts before you changed the settings — the visibility of your number to that specific contact will resolve when you are next contacted fresh by them.

---

## Part 5 — Tor Browser and Mullvad VPN

**Applicable to**: Tier 2+.

**Objective**: Set up a working VPN-then-Tor configuration for sensitive browsing. The VPN (Mullvad) hides your Tor usage from your ISP. Tor hides your browsing destination from Mullvad. Together, they create a two-layer anonymization chain where no single party has both your identity and your browsing destination.

The threat this addresses: NSA backbone collection gathers internet metadata. Your ISP can see that you connect to Tor (even if not what you do there). Using Tor alone — without VPN — may flag you as a Tor user to ISP-level analysis. The VPN-first configuration prevents this.

**Prerequisites**: A computer (Mullvad and Tor Browser run on macOS, Windows, and Linux). For Tier 3 using GrapheneOS: both Orbot and Tor Browser for Android are available.

**Time estimate**: 45–60 minutes for setup and verification.

---

### Step 5.1 — Mullvad Account Setup

Mullvad is recommended because: it accepts cash by mail and Monero (no identity required), its account system uses a random number instead of an email address, and it has a court-verified no-log policy (Swedish authorities have attempted to obtain user data and found no logs to provide).

**Create a Mullvad account**:
1. Go to: https://mullvad.net
2. Click "Get started" — Mullvad immediately generates a random **account number** (a 16-digit string). Save this in KeePassXC. This number is your entire account identity — there is no email address, no password, no name.
3. Add time to the account. Payment options:
   - **Cash by mail** (most anonymous): Instructions at https://mullvad.net/help/sending-cash/ — mail physical cash in an envelope to Mullvad's address. They credit your account within a few business days.
   - **Monero** (most private digital option): Mullvad provides a one-time XMR address at checkout.
   - **Prepaid Visa gift card** purchased with cash: Acceptable for Tier 2. Enter the card as a standard card payment — Mullvad does not verify the cardholder name.
   - **Standard credit/debit card**: Acceptable for Tier 1 where financial privacy is not a concern.
4. Download the Mullvad app for your operating system from the same page.

---

### Step 5.2 — Mullvad Configuration

After installing:

1. Open the Mullvad app and enter your account number
2. Go to **Settings > VPN settings**
3. Confirm **Kill switch** is enabled. Mullvad's kill switch is on by default and cannot be disabled — it automatically blocks all internet traffic if the VPN connection drops, preventing your real IP from being exposed momentarily.
4. Server selection: Connect to a server in **Sweden** or **Netherlands**. These jurisdictions are inside GDPR territory, which creates a procedural barrier (MLAT process required) for U.S. law enforcement to compel Mullvad to provide data — as opposed to simply serving an NSL.
5. Click **Connect**.

---

### Step 5.3 — Mullvad Leak Test (Do Before Using Tor)

With Mullvad connected:

1. Open a regular browser (Chrome, Firefox, Safari)
2. Go to: https://mullvad.net/check
3. The page should show:
   - "You are connected to Mullvad" (green checkmark)
   - Your IP address should be a Mullvad server IP, not your real IP
   - DNS leak check should show Mullvad DNS servers only — not your ISP's DNS servers

**If the leak test shows your real IP**: The VPN is not connected. Check the Mullvad app — it should show "Connected" with a green indicator. Try reconnecting. If problems persist, check that Mullvad's kill switch is engaged and restart the app.

**If the leak test shows a DNS leak** (DNS servers belonging to your ISP appear): Go to **Settings > DNS settings** in the Mullvad app and enable "Use Mullvad DNS." Reconnect and re-test.

Do not proceed to Tor until the Mullvad leak test is clean.

---

### Step 5.4 — Tor Browser Installation

**Download only from the official Tor Project website**: https://www.torproject.org/download/

Do not download Tor Browser from any other source — there are documented cases of fake Tor Browser distributions containing malware.

**Signature verification** (recommended for Tier 2+):
- The download page provides a cryptographic signature for each release
- Instructions for verifying with GPG: https://support.torproject.org/tbb/how-to-verify-signature/
- If you have GPG installed, run: `gpg --verify tor-browser-*.asc` after importing the Tor Project's signing key

**Installation**: Standard application install for your OS. On macOS, drag to Applications. On Linux, extract the tarball to a location of your choice and run `./start-tor-browser.desktop`.

---

### Step 5.5 — Tor Browser Security Settings

After installing and launching Tor Browser:

1. Click the **shield icon** in the toolbar (top right)
2. Click **Advanced Security Settings**
3. Set the security level to **Safest**

What Safest mode does:
- Disables JavaScript on all sites by default (the primary category of browser exploit used to deanonymize Tor users)
- Disables SVG images and some font loading
- Makes most websites look visually plain but eliminates a major class of technical attack

You can enable JavaScript temporarily on a specific site by clicking the shield icon and toggling "Enhanced Tracking Protection" for that site — but do this only when necessary and only on sites you trust.

---

### Step 5.6 — The VPN-Then-Tor Sequence

The order of operations matters. Every session:

1. **First**: Connect Mullvad. Confirm it shows "Connected" in the app.
2. **Then**: Launch Tor Browser.

If Tor Browser is launched before Mullvad is connected: your ISP sees a connection to a Tor guard node. Using Tor is legal but may flag your traffic for ISP-level analysis. The VPN-first configuration prevents this.

After your session:
1. Close Tor Browser.
2. Optionally disconnect Mullvad (or leave it connected — there's no harm in keeping Mullvad connected during regular browsing as well).

---

### Step 5.7 — Behavioral Rules for Tor Browser

These are not suggestions — violations deanonymize you:

- **Do not log into any account linked to your real identity.** Not your Google account, not your personal email, not any social media. The moment you authenticate as yourself, the anonymity is over for that session.
- **Do not download files and open them outside Tor Browser.** A PDF that opens in Preview or Adobe Reader can make network connections outside the Tor tunnel. If you must download a file, open it while offline or use a disposable VM (Tails, Qubes).
- **Do not change the browser window size.** Screen dimensions are used for browser fingerprinting. Tor Browser sets a standard window size to make all users look identical. Resizing the window makes you unique in the anonymity set.
- **Do not install extensions.** Every extension modifies your browser fingerprint. Use Tor Browser as downloaded.
- **Use HTTPS only.** Tor Browser enforces this where available, but verify: the lock icon should appear in the address bar for any site where you enter information.

---

### Verification — Part 5

With Mullvad connected and Tor Browser open:

1. In Tor Browser, go to: https://check.torproject.org
   - Should display: "Congratulations. This browser is configured to use Tor."
   - The IP shown should be a Tor exit node address.
2. In Tor Browser, go to: https://mullvad.net/check
   - Should show a Tor exit node IP (not your real IP and not your Mullvad IP)
   - Confirms traffic is flowing through Tor, not directly out of the Mullvad tunnel
3. The circuit shown in the Tor Browser's circuit visualization (padlock icon in address bar) should show three hops: Guard, Middle relay, Exit node.

---

### Troubleshooting — Part 5

**"check.torproject.org says I'm not using Tor."** Confirm Mullvad was connected before launching Tor Browser. Close Tor Browser entirely (not just the window — quit the application), reconnect Mullvad, and re-launch Tor Browser.

**"Tor Browser won't connect at all."** Tor may be blocked on the network you're using (some workplace or public WiFi networks block Tor). Solution: use Tor bridges. In Tor Browser, go to **Settings > Connection > Use a bridge**. Select "obfs4" or "Snowflake" — these obfuscate Tor traffic to look like regular HTTPS. Click "Request a bridge from Tor Project" to get one automatically.

**"Websites are very slow or won't load."** This is normal — Tor routes through three relays, adding latency. Do not use Tor for streaming video or large downloads. It is designed for text-based browsing and sensitive research, not for all internet activity.

**"Mullvad keeps disconnecting."** Check your network stability. If on WiFi, try Ethernet. Enable **Lockdown mode** in Mullvad settings if you want all internet blocked (not just VPN traffic blocked) when disconnected.

---

## Part 6 — File Encryption and Metadata Minimization

**Applicable to**: Tier 1+ (metadata stripping); Tier 3 (VeraCrypt containers and age encryption).

**Objective**: Protect sensitive files at rest from forensic extraction, and remove identifying metadata from documents before sharing them. A Word document shared with a lawyer, an organizer, or a journalist may contain your name, GPS coordinates, edit history, and the name of the machine that created it — metadata that becomes evidence in an investigation.

**Prerequisites**: A computer. VeraCrypt and ExifTool are free and work on all major operating systems.

**Time estimate**: 30 minutes to install tools; 5 minutes per document for metadata stripping; 20 minutes for initial VeraCrypt container setup.

---

### Step 6.1 — Document Metadata Stripping

Every document you create and share may contain:

- **Author name**: pulled from your OS account name or Office settings
- **Creation timestamp and modification timestamps**
- **Edit history**: previous versions of the text may be recoverable from the file
- **Machine name**: the name of the computer that created the file
- **GPS coordinates**: present in documents created on or with a phone
- **Embedded thumbnails**: in image files, thumbnails are stored separately from the main image and may contain versions of the image after cropping that reveal what you removed

**ExifTool** is the standard tool for stripping this metadata. It works on documents, images, PDFs, and most other file types.

**Install ExifTool**:
- macOS: `brew install exiftool` (requires Homebrew), or download from https://exiftool.org
- Windows: download the Windows Executable from https://exiftool.org
- Linux: `sudo apt install libimage-exiftool-perl` (Debian/Ubuntu) or equivalent

**Strip metadata from a file**:
```
exiftool -all= document.docx
```

This removes all metadata fields from the file and saves the result. A backup file (`document.docx_original`) is created automatically.

**Strip metadata and overwrite without backup**:
```
exiftool -all= -overwrite_original document.docx
```

**Confirm the strip worked**:
```
exiftool document.docx
```

The output should show no Author, no Creator, no GPS data, no modification history. If you see fields like "Creator: John Smith" or "GPS Position: 29.76, -95.36", the strip did not work on those fields — try running exiftool with `-All=` (capital A) instead.

**For images specifically**: GPS coordinates are the most critical field to strip from photos.
```
exiftool -gps:all= photo.jpg
```
Or strip all metadata:
```
exiftool -all= photo.jpg
```

**MAT2** (Linux and Tails): A GUI tool that does the same thing as ExifTool with a drag-and-drop interface. Available in the Tails OS by default. Install on Ubuntu/Debian: `sudo apt install mat2`

---

### Step 6.2 — Safer Document Sharing Practices

Before implementing encryption, the simplest improvement is behavioral:

- **Share content as Signal text messages** rather than attached documents when possible. Text in a Signal message contains no file metadata.
- **Screenshots**: Always crop out the URL bar, account names, notification badges, and any identifying UI elements before sharing. The uncropped version of a screenshot is a metadata document.
- **Configure your camera to not embed GPS**: On GrapheneOS, the camera does not embed location by default. On iOS: Settings > Privacy & Security > Location Services > Camera > Never. On standard Android: open Camera > Settings > disable "Save location."

---

### Step 6.3 — VeraCrypt Encrypted Containers (Tier 3)

A VeraCrypt encrypted container is a single file that functions like a hard drive — you mount it with a passphrase, read and write files inside it, then unmount it. While unmounted, the container file is indistinguishable from random data and cannot be opened without the passphrase.

**Install VeraCrypt**: https://veracrypt.fr (download page has signed installers for Windows, macOS, and Linux)

**Create a container**:

1. Open VeraCrypt. Click **Create Volume**.
2. Select **"Create an encrypted file container."** Click Next.
3. Select **"Standard VeraCrypt volume."** (Not Hidden Volume — see note below.) Click Next.
4. Click **Select File**. Navigate to where you want to store the container (an external encrypted drive is ideal). Give it a non-obvious name — something like `archive_2024.pak` looks more innocuous than `secrets.vc`. Click Save, then Next.
5. Encryption algorithm: leave at **AES**. Hash algorithm: **SHA-512**. Click Next.
6. Set the container size — start with something reasonable for your needs (2–10 GB for documents; larger if you need to store encrypted backups).
7. Set a **passphrase**: use a minimum of 6 random words from a diceware word list (https://thewordlist.net or just roll dice with the EFF word list at https://eff.org/dice). Write this passphrase down and store it somewhere physically secure, not on the computer.
8. Move your mouse randomly over the window for a few seconds (this generates entropy for the encryption key), then click **Format**. The container is created.

**Mount the container to use it**:
1. In VeraCrypt's main window, select a drive letter (Windows) or mount point (macOS/Linux)
2. Click **Select File**, navigate to your container file
3. Click **Mount**, enter your passphrase
4. The container appears as a drive — copy files in and out normally

**Unmount when done**: In VeraCrypt, select the mounted volume and click **Dismount**. Do this before closing the laptop lid or stepping away. A mounted VeraCrypt volume is accessible to any process on the machine — unmounting it means the data is no longer in accessible memory.

**A note on Hidden Volumes**: VeraCrypt's hidden volume feature lets you have two passphrases: one that opens a decoy container, one that opens the real one. This provides plausible deniability under coercion. However, maintaining a convincing decoy volume requires discipline — you must regularly add innocuous-looking files to the decoy to make it believable. For most users, a standard volume with a strong passphrase is the right choice. Hidden volumes are appropriate only for Tier 3 users facing the specific threat of compelled decryption with a plausible deniability defense available.

---

### Step 6.4 — age Encryption for File Transfer

age (https://github.com/FiloSottile/age) is a simple, modern file encryption tool. It encrypts a file to a specific recipient's public key — only the holder of the corresponding private key can decrypt it. Unlike PGP, age requires no key signing infrastructure or web of trust.

**Use case**: encrypting a file before sharing it (over email, Signal, or any channel) when you want the recipient — not just the channel — to be the only person who can open the file.

**Install age**:
- macOS: `brew install age`
- Linux: `sudo apt install age` (Debian/Ubuntu) or download from https://github.com/FiloSottile/age/releases
- Windows: download from the releases page above

**Generate your keypair**:
```
age-keygen -o age-key.txt
```
This creates `age-key.txt` containing both your private key and your public key. The public key is shown in the file header — share only the public key with people who want to encrypt files to you. Keep `age-key.txt` secure (put it in your VeraCrypt container).

**Encrypt a file to a recipient**:
```
age -r age1xxxxxxxxxxxxxxx file.txt > file.txt.age
```
Replace `age1xxxxxxxxxxxxxxx` with the recipient's public key. The output file (`file.txt.age`) can only be decrypted by the recipient.

**Decrypt a file**:
```
age -d -i age-key.txt file.txt.age > file.txt
```

---

### Verification — Part 6

1. Create a test document in Word or LibreOffice. Save it.
2. Run `exiftool test.docx` — note the metadata fields present (Author, Creator, etc.)
3. Run `exiftool -all= -overwrite_original test.docx`
4. Run `exiftool test.docx` again — the metadata fields should be absent or show minimal/empty values
5. If using VeraCrypt: mount the container, create a test file inside it, unmount, then try to open the container file with a text editor — it should display as random binary data (unreadable), confirming encryption is working

---

### Troubleshooting — Part 6

**"exiftool is not found."** Confirm installation: on macOS, run `which exiftool` — if empty, re-install via Homebrew. On Linux, run `exiftool --version`. On Windows, confirm the exiftool directory is in your system PATH, or run it using its full path.

**"After stripping metadata, the Word document looks different."** ExifTool modifies only metadata, not document content. If the document looks different, something other than metadata was changed. Re-run with `-all=` (standard) and check the `_original` backup to compare.

**"VeraCrypt says my passphrase is wrong."** VeraCrypt is case-sensitive. Check caps lock. If you're using a passphrase with spaces, ensure you entered exactly the right number of spaces. There is no passphrase recovery — if you lose the passphrase, the container is unrecoverable. This is why storing the passphrase in a physically secure location (not digitally) matters.

---

## Part 7 — Quick-Start Checklists by Tier

These are single-reference lists. Use them to confirm you have completed each section and to share with others who are starting from scratch.

---

### Tier 1 Minimum Viable Setup

No technical expertise required. Estimated total time: 3–5 hours.

- [ ] Data broker opt-outs submitted to top 8 priority brokers (Part 0, Steps 0.1–0.2)
- [ ] OptOutPrescreen.com submitted
- [ ] NAI and DAA browser opt-outs completed on all devices
- [ ] Signal installed with disappearing messages set to 1 week (Part 4, Steps 4.2–4.4)
- [ ] Signal phone number set to Nobody in both privacy fields (Part 4, Step 4.3)
- [ ] Signal username created (Part 4, Step 4.2)
- [ ] Full-disk encryption enabled on laptop (FileVault on macOS; LUKS at installation on Linux; BitLocker with a strong PIN on Windows — not TPM-only mode)
- [ ] Phone unlock uses 6-digit PIN, not biometric
- [ ] KeePassXC installed with a strong master passphrase (download: https://keepassxc.org)
- [ ] Safety Numbers verified with at least one trusted contact (Part 4, Step 4.5)

---

### Tier 2 Setup (Adds to All Tier 1 Items)

Estimated additional time: 4–6 hours.

- [ ] Carrier-unlocked Pixel purchased (Part 1)
- [ ] GrapheneOS installed, bootloader locked, verified (Part 2)
- [ ] GrapheneOS post-install configuration complete: auto-reboot, network permissions, advertising ID deleted, USB data controls (Part 3)
- [ ] Google Play installed in secondary profile if needed (Part 3, Step 3.4)
- [ ] MySudo VoIP number acquired, paid with prepaid card (Part 4, Step 4.1)
- [ ] Signal registered on VoIP number, username set, phone visibility set to Nobody (Part 4, Steps 4.2–4.3)
- [ ] Safety Numbers verified with primary contacts in person (Part 4, Step 4.5)
- [ ] Mullvad installed, account created without email, leak tested (Part 5, Steps 5.1–5.3)
- [ ] Tor Browser installed, security set to Safest (Part 5, Steps 5.4–5.5)
- [ ] VPN-then-Tor confirmed working via check.torproject.org (Part 5, Step 5.6 + Verification)
- [ ] ExifTool installed; tested on a document (Part 6, Steps 6.1 + Verification)
- [ ] Data broker opt-outs re-submitted to full top-20 list (Part 0, Step 0.2)

---

### Tier 3 Setup (Adds to All Tier 2 Items)

Estimated additional time: 3–4 hours beyond Tier 2.

- [ ] Qubes OS or Tails OS for sensitive desktop activity (Qubes: https://qubes-os.org; Tails: https://tails.net)
- [ ] Orbot installed; Signal routed through Tor via Orbot (Part 4, Step 4.6)
- [ ] VeraCrypt container created with diceware passphrase, passphrase stored physically off-device (Part 6, Step 6.3)
- [ ] age keypair generated; public key shared with relevant contacts (Part 6, Step 6.4)
- [ ] ExifTool/MAT2 used as a pre-sharing step before sharing any document (Part 6, Verification)
- [ ] DeleteMe or EasyOptOuts service active, paid with prepaid cash card (Part 0, Step 0.3)
- [ ] Monero (XMR) acquired without KYC for digital payments tied to sensitive activity (see opsec-playbook.md Part 5.2)
- [ ] Legal representation identified proactively (NLG: https://nlg.org; EFF: https://eff.org; ACLU: https://aclu.org)
- [ ] Incident response plan documented and shared with trusted contacts (see opsec-playbook.md Part 9.3)
- [ ] YubiKey hardware security key configured for all critical accounts (https://yubico.com)

---

## Part 8 — Maintenance Schedule

**Objective**: Ensure the tools and configurations put in place today remain effective. GrapheneOS vulnerabilities get patched, data brokers re-add your records, Tor Browser updates address active exploits, and the legal landscape around surveillance tools shifts. Maintenance is not optional — a six-month-old unpatched GrapheneOS installation is meaningfully less secure than a current one.

---

### Monthly Tasks (15–20 minutes)

**GrapheneOS updates**:
- **Settings > System > System update**
- Install any available update promptly. GrapheneOS patches often address kernel-level vulnerabilities. The GrapheneOS project also sometimes withdraws infrastructure in response to government pressure (as it did in France in November 2025) — staying updated keeps you on current-configuration releases.

**Tor Browser updates**:
- **Help > About Tor Browser**
- If a new version is available, the update banner appears automatically on startup. Update before your next sensitive browsing session. Tor Browser updates frequently address JavaScript engine vulnerabilities that could be used to deanonymize users.

**Signal updates**:
- Check the app store or F-Droid (on GrapheneOS) for a Signal update.
- Signal updates have addressed security disclosures including the NSA-warned QR code attack vector from February 2025. Stay current.

**Review new app permissions on GrapheneOS**:
- After app updates, new permissions may have been requested.
- **Settings > Apps** — review any apps that show a permission change notification.

---

### Quarterly Tasks (1–2 hours)

**Re-submit data broker opt-outs**:
- Data brokers re-add records from public sources every 3–6 months. Re-submit to the top 5 priority brokers: BeenVerified, Spokeo, WhitePages, Intelius, Radaris.
- If you are using DeleteMe or EasyOptOuts, confirm the service is still active and the last run completed successfully.

**Mullvad leak re-test**:
- Connect Mullvad and visit https://mullvad.net/check
- Mullvad changes server configurations periodically. Re-verify that no DNS leaks are occurring.
- Confirm your account still has time remaining.

**Threat intelligence review**:
- Check these sources for new surveillance capability disclosures since your last review:
  - EFF Deeplinks: https://www.eff.org/deeplinks
  - 404 Media: https://404media.co
  - The Intercept: https://theintercept.com
- Specifically look for: new Palantir contracts, new data broker law enforcement partnerships, new legal rulings on compelled decryption, new ICE/CBP surveillance tool deployments.
- Update your personal threat assessment: has your organizing activity, legal exposure, or public profile changed since last quarter?

**Safety Numbers check**:
- For your highest-trust Signal contacts: re-verify Safety Numbers in person or via out-of-band confirmation if you haven't done so in 3+ months. Safety Numbers change when a contact reinstalls Signal or gets a new device.

---

### Annual Tasks (2–3 hours)

**Rotate Mullvad account**:
- Create a new Mullvad account number, add payment time, and begin using it. Delete the old account.
- Why: account numbers accumulate metadata over time (connection timestamps, server usage patterns). Starting fresh limits this.

**Rotate VeraCrypt container passphrases**:
- For high-value containers: create a new container with a new passphrase, transfer files, securely delete the old container (use a secure delete tool, not just trash, on unencrypted drives — on GrapheneOS and encrypted disks, regular deletion is sufficient because the data remains encrypted).

**Verify GrapheneOS device support status**:
- Go to: https://grapheneos.org/faq#supported-devices
- Confirm your specific Pixel model is still within the support window. When a device leaves GrapheneOS support, it no longer receives security patches — plan device replacement before this occurs, not after.
- Pixel 8 and later: 7-year support from launch. Pixel 7a: 5-year support from 2022 launch (approaching end of support in 2027). Pixel 6a: 5-year support from 2022 (approaching end of support in 2027).

**Legal landscape review**:
- Section 702 reauthorization status (currently renewed through April 2026; renewal debate is ongoing as of this writing)
- Fifth Amendment/compelled decryption case law in your circuit
- Check opsec-playbook.md for updates and reassess whether your tier level should change

---

## Conclusion

At the end of each part, you have implemented a real, discrete improvement to your security posture:

- **After Part 0**: Your data profile in law enforcement-accessible commercial databases is reduced.
- **After Parts 1–3**: Your primary communication device no longer generates ad-SDK location data or manufacturer legal exposure.
- **After Part 4**: Your Signal account is not linked to your phone number, and your communications have forward-looking deletion enabled.
- **After Part 5**: Your sensitive browsing does not create a trail at your ISP.
- **After Part 6**: Documents you share do not contain embedded metadata that could identify you or your location.
- **After Part 7**: You have a reference checklist to share with others who need to implement the same protections.
- **After Part 8**: Your setup remains effective over time rather than degrading.

None of these measures are foolproof against a determined, targeted investigation with full government resources. They are, however, meaningful protections against the bulk commercial surveillance infrastructure documented in `threat-model.md` — the ELITE address confidence scoring, the Venntel location data pipeline, the ad-tech data market ICE entered in January 2026, and the carrier metadata analysis that flows into the IRS LCA and NSA contact-chaining systems.

The goal is not perfect security. It is meaningful friction, reduced data density, and the practical elimination of the most likely attack vectors against most people in the threat categories described in `opsec-playbook.md`.

---

## Key Sources

All tools in this guide link to their official sources:

- GrapheneOS install: https://grapheneos.org/install/web
- GrapheneOS FAQ (supported devices): https://grapheneos.org/faq
- Signal download: https://signal.org/download
- Signal phone number privacy: https://support.signal.org/hc/en-us/articles/6712070553754
- Mullvad VPN: https://mullvad.net
- Mullvad connection check: https://mullvad.net/check
- Tor Browser: https://www.torproject.org/download/
- Tor check: https://check.torproject.org
- VeraCrypt: https://veracrypt.fr
- age encryption: https://github.com/FiloSottile/age
- ExifTool: https://exiftool.org
- MySudo: https://getsudo.com
- Orbot: https://guardianproject.info/apps/org.torproject.android/
- KeePassXC: https://keepassxc.org
- Big-Ass-Data-Broker-Opt-Out-List: https://github.com/yaelwrites/Big-Ass-Data-Broker-Opt-Out-List
- EFF Surveillance Self-Defense: https://ssd.eff.org
- Privacy Guides: https://privacyguides.org

*This guide depends on `threat-model.md` for the underlying threat capability analysis and `opsec-playbook.md` for the strategic framework. Reassess your tier level and this guide's applicability whenever either of those documents is updated.*
