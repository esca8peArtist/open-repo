---
title: "Implementation Guide Outline: Tiers 1–3 Setup"
project: cybersecurity-hardening
created: 2026-04-26
author: research-agent
status: outline
depends_on: threat-model.md, opsec-playbook.md
---

# Implementation Guide Outline: Tiers 1–3 Setup

**Assessment**: Option C is the correct next step. This outline confirms the recommendation in NEXT_PHASE.md and provides the detailed structure needed to write the full guide.

The two existing documents leave a precisely bounded gap: a motivated, non-technical Tier 1 or Tier 2 reader who finishes the playbook still cannot execute on it without outside help. The failure modes are not hypothetical — they appear directly in the playbook's tool descriptions (GrapheneOS requires specific hardware, browser, and USB requirements that are not listed; Signal's privacy settings are scattered across 11 sections with no ordered sequence; Tor + Mullvad configuration is described but the "why order matters" is absent). The implementation guide fills that gap with no redundancy against the existing documents.

---

## Feasibility Assessment

**Scope is bounded and executable.** The five core topics — data broker opt-outs, GrapheneOS install, Signal hardening, Tor/VPN routing, file encryption and metadata minimization — are discrete. Each can be written independently and assembled. None require primary research beyond what the playbook already cites; this is translation work (strategic guidance → executable steps) plus verification steps and maintenance cadence that the playbook omits.

**Verification steps are the most important addition.** The playbook's biggest gap is the absence of confirmation procedures. A user who follows instructions and ends up with a misconfigured setup is worse off than one who has no setup — they have false confidence. Every section of the implementation guide must answer: how do you confirm this worked?

**Estimated effort to write the full guide**: 6–8 hours of focused writing, broken down by section below. This is achievable as a single session or two working sessions.

---

## Outline

### Preamble (150 words, 20 min)

State the scope explicitly: this guide operationalizes the opsec-playbook.md recommendations. The threat context is in threat-model.md. This document does not re-explain the threats — it provides executable steps for implementing countermeasures, with verification at each step.

Define the tier labels (same as playbook, referenced not repeated). Note that sections are ordered by population impact, not technical complexity. A reader can stop at any section and have implemented something real.

---

### Part 0 — Data Broker Opt-Outs (Tier 1+, no technical expertise required)

**Threat addressed**: Data broker pipeline documented in threat-model.md Section II. ELITE address confidence scoring, Venntel/Accurint location data pipelines, LexisNexis Accurint commercial surveillance database.

**Why this comes first**: Highest population impact, zero technical barrier. Reduces existing exposure in databases that currently exist and are actively queried by ICE/CBP. Can be completed in a single afternoon.

**Content to cover**:

1. The four federal opt-out programs that require no explanation — they are statutory:
   - OptOutPrescreen.com (FCRA opt-out from pre-screened credit offers — also removes you from Equifax, Experian, Innovis, TransUnion marketing lists)
   - DMAchoice.org (Direct Marketing Association — removes from catalog, magazine, and other direct mail lists; $2 processing fee)
   - NAI opt-out (Network Advertising Initiative — browser-based opt-out from member ad-network tracking; must be repeated per browser and per device)
   - Digital Advertising Alliance opt-out (similar scope to NAI, different members; use both)

2. Major data broker opt-out submissions (the 20 highest-priority brokers by data depth and confirmed law enforcement use):
   - LexisNexis/Accurint: opt-out form + documentation requirements
   - BeenVerified: opt-out URL and confirmation process
   - Spokeo: opt-out and removal verification steps
   - WhitePages: opt-out and time-to-removal estimate
   - Intelius: opt-out process
   - Radaris: opt-out process
   - PeopleFinder: opt-out
   - US Search: opt-out
   - Instant Checkmate: opt-out
   - PeekYou: opt-out
   - Pipl: opt-out process (slightly more involved)
   - FamilyTreeNow: opt-out (fast removal, good to start with as a confidence-builder)
   - Whitepages Premium: separate from Whitepages free, separate opt-out
   - ZabaSearch: opt-out form
   - Addresses.com: opt-out
   - InfoTracer: opt-out form link
   - TruthFinder: opt-out form
   - PublicRecordsNow: opt-out
   - Acxiom: opt-out via their consumer portal (acxiom.com/optout)
   - Epsilon: opt-out via EpsilonDataAlliance.com

3. Automation note: EasyOptOuts ($20/year) and DeleteMe ($130/year) automate ongoing re-submission — data brokers re-add people from public records, so one-time opt-out is not permanent. The economics are: DeleteMe's rate covers approximately 750+ brokers with quarterly re-submission. For most Tier 1/2 users, this is the right trade. Manual opt-outs from the top 20 above are free and cover the highest-risk brokers.

4. Verification: After two to four weeks, search your name on the top five brokers. Document what is still present. Re-submit where needed. Note: some brokers remove the public listing but retain data for law enforcement query — this cannot be confirmed from the consumer side, but public listing removal is the achievable target.

**Estimated writing time**: 45 minutes

---

### Part 1 — Hardware Selection (Tier 2+)

**Threat addressed**: Device forensics (Cellebrite, GrayKey), manufacturer legal compulsion (Apple iCloud subpoenas), carrier telemetry.

**Content to cover**:

1. Which Pixel models support GrapheneOS — current supported list (Pixel 6 through Pixel 9 series as of 2026; always verify at grapheneos.org/faq before purchasing). Note that Pixel 6a, 7a, 8a (the "a" budget variants) are supported and cost significantly less than flagship models.

2. Where to buy: GrapheneOS recommends purchasing directly from Google Store or a reputable retailer. Avoid Amazon Marketplace third-party sellers — supply chain integrity for a device you are trusting with your security matters. Swappa.com is an acceptable source for refurbished Pixel devices with carrier-unlocked status.

3. Carrier-unlocked status: confirm the device is unlocked before purchasing. A carrier-locked Pixel may have firmware modifications. How to verify: Settings > About Phone > SIM status.

4. What to do with your existing phone during setup: keep it on, use it normally, do not announce the transition.

**Estimated writing time**: 20 minutes

---

### Part 2 — GrapheneOS Installation (Tier 2+)

**Threat addressed**: Same as Part 1. This is the highest-friction technical step in the entire guide and the one most likely to fail without explicit guidance.

**Content to cover**:

1. Pre-installation checklist:
   - Charge device to 80%+
   - Use Chrome or Chromium on a desktop/laptop (the web installer uses WebUSB, which Firefox does not support as of 2026; Safari does not support it at all)
   - Use a known-good USB-C cable (data-capable, not charge-only — this is a common failure point; cables labeled "charging only" will not work)
   - Note the Pixel model and build number before starting (Settings > About Phone)

2. Enable OEM Unlock:
   - Settings > About Phone > tap Build Number 7 times to enable Developer Options
   - Settings > System > Developer Options > OEM unlocking (toggle on)
   - Why this matters: OEM unlock is required to flash a custom OS. On some Pixel models, this toggle takes 15–60 seconds to activate after tapping. Common mistake: toggling and immediately proceeding before it activates.

3. Web installer process (grapheneos.org/install/web):
   - Connect device in fastboot mode (power off, then hold Volume Down + Power)
   - Select device from browser prompt
   - Unlock bootloader (this wipes the device — expected)
   - Flash GrapheneOS
   - Lock bootloader (this step is critical and often skipped — locking the bootloader re-enables verified boot, which is what makes GrapheneOS more secure than a stock OS with an unlocked bootloader)
   - Reboot

4. Common failure modes and diagnosis:
   - "Device not found" in browser: Check USB cable (try a different one), check that Chrome is used, check that USB debugging is not enabled (it interferes with fastboot)
   - OEM unlock toggle grayed out: SIM card must be inserted OR device is on a carrier-locked unit
   - Bootloader won't re-lock: Indicates the flash did not complete cleanly; re-run from flash step

5. Verification — how to confirm GrapheneOS installed correctly:
   - Settings > About Phone > Android Version should show GrapheneOS version, not "Android"
   - Settings > Security > check that "OEM unlocking" toggle is now grayed out (locked bootloader)
   - Settings > Security > Verified Boot should show "Device is locked" and "Verified"
   - Power off and back on — GrapheneOS shows its own boot screen, not the Google "G" logo

**Estimated writing time**: 60 minutes

---

### Part 3 — Post-Install GrapheneOS Configuration (Tier 2+)

**Threat addressed**: Ad-SDK location harvesting (Venntel pipeline), app-level data collection, forensic extraction after seizure.

**Content to cover**:

1. Auto-reboot: Settings > Security > Auto reboot — set to 18 hours or shorter (default). This returns the device to Before First Unlock (BFU) state if not unlocked, substantially complicating forensic extraction after seizure.

2. Network permission controls: Settings > Apps > [app name] > Permissions > Network — GrapheneOS adds the ability to deny network access entirely to any app. Apply this to every app that doesn't need internet access: calculator, camera, contacts, etc. This is the primary technical countermeasure against ad-SDK location harvesting.

3. Sandboxed Google Play (if you need Google Play apps):
   - Install via the GrapheneOS app store (pre-installed)
   - Sandboxed Google Play runs in an isolated profile with no special OS privileges — it cannot see other apps, cannot access the hardware directly, and cannot track location without explicit permission
   - Do not install Google Play in your main profile — create a separate profile for it

4. Disable advertising ID: Settings > Privacy > Ads > Delete advertising ID

5. Screen lock: Settings > Display > Screen timeout (set to 1 minute); Settings > Security > Screen lock (set PIN of 6+ digits)

6. Disable USB data when locked: Settings > Security > USB accessories — set to "No new USB accessories"

**Estimated writing time**: 30 minutes

---

### Part 4 — Signal Setup Sequence (Tier 1+)

**Threat addressed**: Carrier metadata exposure, identity linkage via phone number, NSA contact graph construction.

**Why sequence matters**: Several Signal privacy settings depend on others being configured first, and some must be set before any contacts are added (Safety Numbers, for instance, change when you verify — earlier is better).

**Content to cover**:

1. VoIP number setup (Tier 2+, do before installing Signal):
   - Google Voice: free, linked to a Google account — acceptable for Tier 2, not Tier 3
   - MySudo (getsudo.com): $1/month plan provides a real U.S. number with no identity requirement beyond payment; pay with a prepaid card
   - JMP.chat: XMPP-based, more technical, can be purchased via cryptocurrency
   - The VoIP number is used only for Signal registration — you will not give it out as a contact number

2. Signal installation and account setup (ordered):
   - Install from official app store or signal.org
   - Register with the VoIP number (you will receive an SMS verification code on that number)
   - Immediately after registration: Settings > Profile — set a display name and username
   - Settings > Profile > username — this creates your @username
   - Settings > Privacy > Phone Number > "Who can see my number" — set to Nobody
   - Settings > Privacy > Phone Number > "Who can find me by my number" — set to Nobody
   - These two settings must be configured before sharing Signal with anyone, or your phone number is already visible

3. Disappearing messages default:
   - Settings > Privacy > Default Timer — set to 1 Week (Tier 1) or 1 Day (Tier 2)
   - This applies to all new conversations; existing conversations require manual update

4. Safety Numbers verification (for important contacts):
   - Open conversation > contact name at top > Safety Number
   - Compare the number verbally or in person with your contact
   - Tap "Verified" after confirming
   - Why: if Signal is forced to hand over metadata, it cannot reveal message content — but Safety Numbers verification confirms you are communicating with the right person, not an interposed device

5. Orbot integration (Tier 3 — routes Signal through Tor):
   - Install Orbot from F-Droid (preferred) or Play Store
   - Open Orbot > VPN mode > select Signal (and only Signal unless you want all traffic routed through Tor)
   - Verify Orbot is running before opening Signal

6. Verification — confirm Signal is configured correctly:
   - Settings > Privacy > Phone Number: both fields should show Nobody
   - Open a conversation: tap the contact name — confirm Safety Numbers is shown (indicates E2E encryption is active)
   - Settings > Profile > username: should show your @username
   - Test disappearing messages: send a test message to Note to Self, confirm timer appears

**Estimated writing time**: 45 minutes

---

### Part 5 — Tor Browser and Mullvad Integration (Tier 2+)

**Threat addressed**: ISP-level traffic analysis, IP-based identity tracking, NSA backbone collection of browsing metadata.

**Content to cover**:

1. Mullvad installation and account setup:
   - mullvad.net — download for your OS
   - Account creation: no email required — Mullvad generates a random account number; save it in KeePassXC
   - Payment: Mullvad accepts cash by mail (most anonymous), Monero, Bitcoin, and standard cards. For Tier 2: purchase a prepaid Visa with cash and use it here.
   - Connect to a server (Sweden or Netherlands recommended for GDPR procedural barrier)

2. Mullvad leak test before using Tor:
   - With Mullvad connected: visit mullvad.net/check in a regular browser
   - Confirm: your real IP is not shown; DNS leak check should show Mullvad servers only
   - If the leak test shows your real IP, do not proceed — disconnect, check Mullvad's kill switch setting (Settings > Kill switch — enable), reconnect, re-test

3. Tor Browser installation:
   - Download only from torproject.org — verify the cryptographic signature if you have GPG installed (instructions on torproject.org/download)
   - Install and launch (do not configure browser settings; do not add extensions; use as downloaded)
   - Security Settings: click the shield icon > Advanced Security Settings > set to Safest (disables JavaScript, prevents a significant class of browser exploits)

4. VPN-then-Tor sequence and why order matters:
   - Connect Mullvad FIRST, confirm it is connected (check the Mullvad icon in your system tray shows a green lock)
   - Then launch Tor Browser
   - Result: your ISP sees Mullvad VPN traffic. Mullvad sees a Tor connection but not your destination. The Tor network handles the destination.
   - If you launch Tor Browser before connecting Mullvad: your ISP can see you are connecting to Tor. Using Tor alone is not illegal but flags you as a Tor user in traffic analysis. For Tier 2 users where ISP metadata is a concern, this defeats part of the purpose.

5. Verification — confirm the chain is working:
   - With Mullvad connected and Tor Browser open: visit check.torproject.org — should say "Congratulations. This browser is configured to use Tor."
   - The IP shown should be a Tor exit node address, not your real IP or Mullvad IP
   - Visit mullvad.net/check inside Tor Browser — will show a Tor exit node IP, confirming traffic is going through Tor and not directly from your Mullvad IP

6. Behavioral rules for Tor Browser:
   - Do not log in to any account associated with your real identity
   - Do not download files and open them in other applications (PDFs can make outbound connections outside Tor)
   - Do not change window size (browser fingerprinting uses window dimensions to narrow anonymity set)
   - Use Tor Browser only for the purpose that requires anonymity — close it when done

**Estimated writing time**: 50 minutes

---

### Part 6 — File Encryption and Metadata Minimization (Tier 1+)

**Threat addressed**: Device seizure and forensic extraction (Parts 1–3 of threat model), document metadata leakage (OSINT aggregation).

**Content to cover**:

1. VeraCrypt encrypted containers (supplemental layer for specific sensitive files):
   - Create a standard encrypted volume (not hidden volume for most users — hidden volumes require maintaining a convincing decoy, which is harder in practice than it sounds)
   - Volume creation walkthrough: VeraCrypt > Create Volume > Standard volume > choose file location > AES encryption > set strong passphrase (6-word diceware minimum)
   - Mount/unmount discipline: unmount when not in use — a mounted VeraCrypt volume is accessible to any process on the machine
   - Backup: the encrypted volume file can be copied to an external drive. The passphrase must not be stored on the same device.

2. age encryption for file-level encryption (simpler than PGP for files at rest or file transfer):
   - age (github.com/FiloSottile/age) uses X25519 key exchange — modern, simple, no key signing infrastructure
   - Key generation: `age-keygen -o key.txt`
   - Encrypt a file: `age -r [recipient-public-key] file.txt > file.txt.age`
   - Decrypt: `age -d -i key.txt file.txt.age > file.txt`
   - Primary use case: encrypting a file before attaching it to ProtonMail or sharing via OnionShare when you need the recipient (not just the channel) to be the decryption target

3. Document metadata stripping before sharing:
   - Word/LibreOffice files embed: author name, creation timestamp, modification history, sometimes GPS coordinates if created on a mobile device
   - ExifTool command-line (all platforms): `exiftool -all= document.docx` — strips all metadata
   - MAT2 (Linux/Tails): GUI tool for stripping metadata from PDFs, images, documents
   - Safer default: share content as plain text in Signal rather than as an attached document when possible
   - Image metadata: every smartphone photo includes GPS coordinates by default unless location services are disabled for the camera app. Check: GrapheneOS camera can be configured to not embed location. iOS: Settings > Camera > disable "Include GPS data."

4. Metadata minimization checklist before sharing any document:
   - Strip with ExifTool or MAT2
   - Confirm strip: `exiftool [file]` should show no Author, no GPS, no creation timestamp
   - If sharing a screenshot: crop to remove any identifying UI elements (URL bar, account names, notification badges)

**Estimated writing time**: 40 minutes

---

### Part 7 — Quick-Start Checklists by Tier

**Purpose**: Single-page reference. A reader who has completed each section can use these as a maintenance checklist and share-with-someone-else summary.

**Tier 1 Quick-Start (no technical expertise required)**:
- [ ] Submit data broker opt-outs to the top 20 brokers (Part 0)
- [ ] Signal installed with disappearing messages set (Part 4, steps 1–3 only)
- [ ] Signal phone number set to Nobody in privacy settings (Part 4, step 2)
- [ ] Full-disk encryption enabled on laptop (FileVault / LUKS — not covered in this guide, link to EFF SSD)
- [ ] Phone unlock uses PIN not biometric
- [ ] KeePassXC installed with a strong master passphrase

**Tier 2 Quick-Start (adds GrapheneOS + Tor/VPN)**:
- All Tier 1 items, plus:
- [ ] Carrier-unlocked Pixel purchased (Part 1)
- [ ] GrapheneOS installed and bootloader re-locked, verified (Part 2)
- [ ] GrapheneOS post-install configuration complete (Part 3)
- [ ] Signal VoIP number acquired (Part 4, step 1)
- [ ] Signal username set; phone number visibility set to Nobody (Part 4, step 2)
- [ ] Safety Numbers verified with primary contacts (Part 4, step 4)
- [ ] Mullvad installed and leak-tested (Part 5, steps 1–2)
- [ ] Tor Browser installed, security set to Safest (Part 5, step 3)
- [ ] VPN-then-Tor confirmed via check.torproject.org (Part 5, step 5)

**Tier 3 Quick-Start (adds Qubes/Tails + full financial/identity separation)**:
- All Tier 2 items, plus:
- [ ] Qubes OS or Tails OS for sensitive desktop activity (link to Qubes install docs)
- [ ] Orbot routing Signal through Tor (Part 4, step 5)
- [ ] VeraCrypt container for sensitive files, unmounted when not in use (Part 6, step 1)
- [ ] age encryption for sensitive file transfers (Part 6, step 2)
- [ ] ExifTool/MAT2 installed and used before sharing any documents (Part 6, steps 3–4)
- [ ] Monero acquired for sensitive payments (opsec-playbook.md Part 5.2)
- [ ] Legal representation identified proactively (NLG, EFF, ACLU)
- [ ] Incident response plan documented

**Estimated writing time**: 30 minutes

---

### Part 8 — Maintenance Schedule

**Why this section is necessary**: The playbook mentions "quarterly reassessment" but provides no specifics. Tools get deprecated, vulnerabilities are disclosed, legal frameworks shift. The opsec playbook explicitly notes that GrapheneOS withdrew French server infrastructure in November 2025 under government pressure — that is the kind of change that requires a maintenance-aware reader.

**Content to cover**:

Monthly:
- Check GrapheneOS update notification (Settings > System > System update). Install promptly — GrapheneOS patches often address kernel-level vulnerabilities.
- Check Tor Browser version (Help > About Tor Browser) — update if a new version is available. The Tor Browser version banner appears automatically; do not dismiss without updating.
- Check Signal update in your app store. Signal updates frequently and some updates address security disclosures.
- Review app permissions on GrapheneOS: any app that has acquired new permissions should be scrutinized.

Quarterly:
- Re-submit data broker opt-outs to the top 5 brokers (BeenVerified, Spokeo, WhitePages, Intelius, Radaris). These re-add from public records on approximately a quarterly cycle.
- Review opsec-playbook.md threat intelligence sources (EFF Deeplinks, 404 Media, The Intercept) for new surveillance contracts or capability disclosures.
- Test Mullvad leak check again (mullvad.net/check). Mullvad changes server configurations; re-verify.
- Assess personal threat level changes (new organizing activities, legal exposure, travel to regions with different threat models).

Annually:
- Rotate VPN account (Mullvad account numbers can be renewed or replaced; starting fresh limits account-level metadata accumulation).
- Review and rotate VeraCrypt container passphrases for high-value containers.
- Verify GrapheneOS-supported Pixel models list — if your device has left the support window, plan hardware refresh.

**Estimated writing time**: 20 minutes

---

## Estimated Total Effort

| Section | Writing time |
|---------|-------------|
| Preamble | 20 min |
| Part 0 — Data broker opt-outs | 45 min |
| Part 1 — Hardware selection | 20 min |
| Part 2 — GrapheneOS installation | 60 min |
| Part 3 — Post-install GrapheneOS config | 30 min |
| Part 4 — Signal setup sequence | 45 min |
| Part 5 — Tor + Mullvad | 50 min |
| Part 6 — File encryption + metadata | 40 min |
| Part 7 — Quick-start checklists | 30 min |
| Part 8 — Maintenance schedule | 20 min |
| **Total** | **~6 hours** |

The 6-hour estimate assumes no primary research required — all factual content is already present in threat-model.md and opsec-playbook.md. The implementation guide is translation and elaboration work, not new research. The one section that may require current-state verification before writing is Part 0 (data broker opt-out URLs change; some brokers fold or merge) — budget 30 minutes for link verification at the time of writing.

---

## What the Completed Three-Document Corpus Covers

- `threat-model.md` — What the surveillance infrastructure is and what it can do (complete)
- `opsec-playbook.md` — What countermeasures to implement and why (complete)
- `implementation-guide.md` — How to implement each countermeasure, in order, with verification steps (to produce, estimated 6 hours)

The implementation guide does not overlap with either existing document. It cites both but does not summarize them. Its purpose is purely operational: a reader with a new Pixel in hand and the playbook open should be able to follow Part 2 from first boot to a verified GrapheneOS installation without referring to any other resource.
