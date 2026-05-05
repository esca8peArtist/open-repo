---
title: "Encrypted Messaging Implementation Guide"
project: cybersecurity-hardening
created: 2026-05-05
status: complete
depends_on: opsec-playbook.md, threat-model.md
confidence: high — sourced from EFF Surveillance Self-Defense, Signal official docs, Matrix.org, Briar Project official documentation, Freedom of the Press Foundation
---

# Encrypted Messaging Implementation Guide

> **Danger**: Encrypted messaging protects message content. It does not protect metadata (who you communicate with, when, how often), your device if seized, or the other party if they are compromised. Read the limitations section for each platform before assuming you are protected.

---

## Threat Model: Who You Are Protecting Against

Before installing anything, identify your threat model. The correct tool depends on what you are defending against.

| Threat Actor | Primary Attack Surface | Appropriate Tool |
|---|---|---|
| Corporate data harvester | App permissions, unencrypted messages | Signal (Tier 1 configuration) |
| Stalker or abusive partner | Metadata, account linkage | Signal with username isolation |
| Law enforcement with subpoena | Stored message content, account records | Signal, Briar, or Matrix self-hosted |
| Federal agency with NSL | Carrier metadata, connection records | Briar over Tor; Signal with VoIP registration |
| Active adversary with device access | Endpoint compromise, malware | No messaging app helps — device security first |

**Assets at risk**: The content of your communications, the identity of your contacts, the timing and frequency of your communications, and your location when communicating.

**What no messaging app can protect**: Your physical safety during in-person contact exchanges, the security posture of the other party's device, or communications you have already had on insecure platforms.

---

## Part 1: Signal

### What Signal Is and What It Actually Protects

Signal uses the Signal Protocol — a combination of the X3DH (Extended Triple Diffie-Hellman) key agreement and the Double Ratchet algorithm. This provides two critical properties:

- **Forward secrecy**: If a session key is later compromised, past messages cannot be decrypted because each message uses a derived ephemeral key.
- **Break-in recovery**: Even if an adversary compromises a session key, future messages become secure again as new keys are derived.

Signal's encryption has been independently audited multiple times and has survived formal cryptographic analysis. The FBI, when served with a grand jury subpoena for Signal account data in a 2022 case, received only: account creation date and last connection date. That is all Signal retains. Signal has published this transparently.

**What Signal does not protect**:
- Your carrier can see that your device is communicating with Signal's servers, and can provide this metadata under legal compulsion.
- If your device is seized or infected with spyware, encrypted messaging does not protect you — the adversary reads your messages from the screen.
- The primary real-world attack on Signal in 2025 was not cryptographic: Russian intelligence compromised Signal accounts by tricking users into linking attacker-controlled devices via malicious QR codes disguised as group invite links (NSA warning, February 2025). This is a social engineering attack, not a cryptographic one.

**Official source**: [signal.org](https://signal.org) — download only from this URL or your platform's official app store.

---

### Step 1: Install Signal

**Android**:
1. Open the Google Play Store (or F-Droid if you prefer open-source app distribution).
2. Search for "Signal Private Messenger" — publisher is "Signal Messenger LLC."
3. Verify the developer name before installing. Impersonation apps exist.
4. Tap "Install."

**iOS**:
1. Open the App Store.
2. Search "Signal — Private Messenger" — publisher is "Signal Messenger LLC."
3. Verify the publisher name.
4. Tap "Get."

**Desktop (Windows, macOS, Linux)**:
1. Navigate to [signal.org/download](https://signal.org/download).
2. Download the version for your platform.
3. On macOS: open the .dmg file, drag Signal to Applications. On first launch, macOS may warn about an "unidentified developer" — go to System Settings → Privacy & Security → click "Open Anyway."
4. On Linux: Signal provides a .deb package for Debian/Ubuntu systems and instructions for other distributions at the download page.

> **Note**: Signal on desktop requires you to link it to an existing Signal account on a mobile device. The desktop app does not function independently.

---

### Step 2: Create Your Account

1. Open Signal on your phone.
2. Signal requires a phone number for registration. This number is used only to verify your account — it does not need to be visible to your contacts (see Step 4).
3. Enter your phone number. Signal will send a 6-digit SMS verification code.
4. Enter the code when prompted.
5. Set a Profile Name. This is what your contacts see — it does not have to be your real name.
6. Set a Profile Photo (optional). If your threat model includes hiding that you use Signal, skip the photo.
7. Set a Registration Lock PIN: Settings → Account → Registration Lock. This prevents someone who has physical access to your SIM from re-registering your Signal account to a new device. Choose a PIN you will remember — you cannot recover your account without it after 7 days.

> **Common pitfall**: Choosing a memorable but weak PIN (birthdate, "123456"). Signal does not enforce PIN complexity, but a weak PIN defeats the purpose of Registration Lock.

---

### Step 3: Configure Privacy Settings

Navigate to Settings (your profile picture) → Privacy.

**Phone Number**:
- "Who can see my phone number" → set to "Nobody."
- "Who can find me by my phone number" → set to "Nobody."
This means people cannot find or contact you via your phone number unless you share it directly.

**Enable Signal Usernames**:
- Settings → Profile → tap the "@" field next to your name.
- Choose a username. This is what you share with new contacts instead of your phone number.
- Share this username rather than your number when making new contacts.

**Disappearing Messages**:
- Settings → Privacy → Default Timer for New Chats.
- Set a default disappearing messages timer. "1 week" is reasonable for most users; "1 day" for higher-risk contacts.
- You can always override this per conversation, but having a default prevents accidentally leaving messages indefinitely in new chats you forget to configure.

**Screen Security** (prevents screenshots):
- Settings → Privacy → Screen Security → enable.
This prevents Signal's content from appearing in the app switcher and prevents screenshots within the app.

**Screen Lock**:
- Settings → Privacy → Screen Lock → enable.
This requires your phone's biometric or PIN to open Signal, separate from your general phone lock.

---

### Step 4: Verify Safety Numbers

Safety Numbers are fingerprints of the cryptographic keys securing your conversation with a specific contact. Verifying them confirms you are communicating with the intended person and not a man-in-the-middle attacker.

**When to verify**: Before sharing sensitive information with any important contact.

**How to verify**:
1. Open the conversation with your contact.
2. Tap their name at the top → View Safety Number.
3. You will see a 60-digit number (displayed as 12 groups of 5 digits) and a QR code.
4. Two methods to verify:

**Method A — In Person (most secure)**:
- Both parties open the safety number screen simultaneously.
- Scan each other's QR code, or read the numbers aloud and confirm they match.
- Once verified, tap "Mark as Verified."

**Method B — Separate Secure Channel**:
- Read your safety number to your contact over a phone call (where you can recognize their voice) or in person, then confirm they read the same number back.
- Do not verify safety numbers over Signal itself — you are trying to verify the Signal channel, so using Signal to do it is circular.

**What a changed safety number means**: If Signal shows you that a safety number changed, it could mean your contact got a new phone, reinstalled Signal, or — in the worst case — someone has intercepted the channel. Confirm the change with your contact through a different channel before continuing sensitive communication.

> **Danger**: A 2025 attack by Russian intelligence involved sending malicious QR codes disguised as Signal group invite links. Never scan a QR code to "verify" a safety number or join a group unless you received it directly from a trusted contact in person. [Source: NSA cybersecurity advisory, February 2025]

---

### Step 5: Group Chats

Signal groups support up to 1,000 members. Group conversations are end-to-end encrypted. However, group security is only as strong as the least-secure member.

**Create a group**:
1. Tap the compose icon → New Group.
2. Add contacts from your Signal contact list.
3. Name the group.
4. Tap the group name → Group Settings to configure permissions.

**Configure group permissions**:
- "Who can add members" → set to "Admins Only."
- "Who can edit group info" → set to "Admins Only."
- Set group-level disappearing messages: group name → Disappearing Messages.

**Group security practices**:
- Before joining a group, set your Signal display name. Once you are in the group, all members can see changes to your display name, creating a record. Set the name you want before joining, not after.
- Groups cannot be verified the same way as 1:1 conversations. If you do not know everyone in a group personally, treat the group as a lower-security channel.
- Remove members promptly when their need for the group ends. Former members retain a copy of all messages sent while they were in the group.

**Group link settings** (relevant to the 2025 QR code attack):
- Settings → Group Settings → Group Link.
- If your group does not need a shareable link, disable this feature.
- If you use a group link, enable "Require Admin Approval" so new members cannot join without an admin confirming them.

---

### Threat Model by Use Case

**Journalist**: Signal is appropriate for source communications in most situations. Register Signal with a separate VoIP number (not your main carrier number). Enable disappearing messages with short timers. Use Safety Number verification with all sources before their first sensitive message. Be aware that your contact's device security is beyond your control — use SecureDrop for documents rather than Signal.

**Activist**: Signal is appropriate for organizing communications. Enable usernames and hide phone number from non-contacts. Do not use Signal groups for operational planning unless you trust every member. Consider whether your organizing network can tolerate a compromised member — if not, operate on a need-to-know basis rather than a full-group model.

**Underground network / high-risk operations**: Signal alone is insufficient. Use Signal over Tor or a VPN to obscure that you are connecting to Signal servers. Use Briar (see Part 3) for highest-sensitivity contacts. Consider that Signal's phone number registration means there is always a carrier record linking your account to a phone number, even if that link is obscured from contacts.

---

### Signal Security Checklist

- [ ] Installed from official source only (signal.org or official app store)
- [ ] Registration Lock PIN enabled (Settings → Account → Registration Lock)
- [ ] Phone number hidden from non-contacts (Settings → Privacy → Phone Number → Nobody)
- [ ] Username created and shared instead of phone number
- [ ] Default disappearing messages timer set (Settings → Privacy → Default Timer)
- [ ] Screen Security enabled (prevents screenshots)
- [ ] Safety Numbers verified with all sensitive contacts in-person or via separate channel
- [ ] Group link disabled or set to require admin approval
- [ ] Group permissions set to Admins Only for membership and editing

---

### Troubleshooting: Signal

**Problem**: Contact shows "waiting for message" or messages won't deliver.
**Solution**: Both parties must have data connectivity. Check that neither has blocked the other. Try calling within Signal to test connectivity. If the contact recently changed phones, wait for Signal to complete their key re-registration.

**Problem**: Safety number changed notification.
**Solution**: Contact your contact through a separate channel (phone call, in person) and confirm they recently changed devices or reinstalled Signal. If they did not, treat this as a potential compromise and stop sharing sensitive content until verified.

**Problem**: Messages are not disappearing on schedule.
**Solution**: Both parties must have the app open at some point within the disappearing window for deletion to trigger. Disappearing messages require the app to run.

**Problem**: Signal asks for my phone number again / "Registration Lock PIN" prompt.
**Solution**: If you set a Registration Lock, you must re-enter the PIN within 7 days if Signal detects a device change. If you forget the PIN, you must wait 7 days before Signal allows re-registration. This is by design — it is a security feature.

---

## Part 2: Matrix (Element Client)

### What Matrix Is and What It Actually Protects

Matrix is an open, decentralized communication protocol. Unlike Signal, Matrix is federated — you can host your own server, eliminating reliance on any single company. The most widely used client is Element.

Matrix's end-to-end encryption is based on the Olm and Megolm libraries, which implement protocols derived from the Signal Protocol's Double Ratchet algorithm. End-to-end encryption is enabled by default in direct messages and can be enabled in rooms.

**Critical difference from Signal**: Matrix encryption is device-specific. Each device you log in on has its own set of cryptographic keys. This requires active device verification across multiple sessions — a step many users skip, creating unverified device chains that weaken the trust model.

**Important 2025 change**: As of 2025/2026, Element is requiring device verification before devices can send and receive end-to-end encrypted messages in many configurations. Unverified devices are blocked from encrypted communication.

**Official source**: [matrix.org](https://matrix.org) | [element.io](https://element.io)

---

### Step 1: Choose a Homeserver

Matrix is federated. You choose which server hosts your account.

**Option A — matrix.org** (easiest, operated by Matrix.org Foundation):
- No setup required. Go to element.io and create an account.
- Limitation: matrix.org is a known target for legal process. If your threat model includes legal compulsion, self-hosting is preferable.

**Option B — Self-hosted Synapse**:
- Requires a server (VPS, home server) with a domain name.
- Installation: [matrix.org/docs/guides/synapse-installation](https://matrix.org/docs/guides/synapse-installation/)
- Benefit: You control all data. Law enforcement must approach you (or your hosting provider) directly rather than a third-party operator.
- Limitation: Requires technical competence to maintain securely. An insecure self-hosted instance can be worse than using matrix.org.

**Option C — Community-operated servers**:
- Servers like `libera.chat`, `tchncs.de`, and others exist. Research the server's jurisdiction and policy before choosing.

---

### Step 2: Create an Account (matrix.org / Element)

1. Navigate to [app.element.io](https://app.element.io) in your browser, or download the Element app for your platform from [element.io/get-started](https://element.io/get-started).
2. Click "Create Account."
3. Choose your homeserver: for matrix.org, leave the default. For a custom server, click "Edit" and enter the server address.
4. Choose a username (this becomes your Matrix ID: `@username:server.org`). This is visible to people you communicate with.
5. Set a password. Use a password manager to generate a strong password.
6. Complete any verification step (email is typically required on matrix.org).

---

### Step 3: Enable and Configure E2E Encryption

**Set up Secure Backup / Cross-Signing**:
1. After creating your account, Element will prompt you to set up Secure Backup. Do this immediately.
2. "Security & Privacy" → "Set up Secure Backup."
3. Choose "Generate a Security Key" (or passphrase — key is more secure).
4. Save the 24-character security key offline — in a password manager or printed and stored securely. This key is needed to recover your encryption keys on a new device. If you lose it, you lose access to your encrypted message history.
5. Element will use this key to create a "cross-signing" setup that allows your devices to automatically verify each other after you authenticate.

**What cross-signing does**: Cross-signing allows a new device to inherit the verified-device status of your existing devices by signing the new device's keys with a master identity key. When you log into Element on a second device, you verify it by scanning a QR code or comparing emoji with your existing device, rather than having all your contacts re-verify each device individually.

---

### Step 4: Verify Devices

**Verify your own devices**:
1. Log into Element on a second device (e.g., a desktop after setting up mobile).
2. Element will show "Verify this device" on the new login.
3. On the existing verified device, go to your account name → Security → Devices, and find the new unverified device.
4. Tap "Verify" → follow the emoji comparison or QR scan.
5. Confirm both devices show the same emoji/QR content — this is a cryptographic challenge proving both devices share the correct keys.

**Verify other users**:
1. Open a direct message with the contact.
2. Click their name → "Security" or "Verify" (UI varies by Element version).
3. Request verification. They accept on their end.
4. Complete the emoji comparison or QR scan.
5. Once verified, all devices cross-signed by that user are transitively trusted.

> **Common pitfall**: Skipping device verification and assuming messages are secure. Element will show a warning icon on unverified conversations. Unverified does not mean unencrypted — but it means you cannot confirm the encryption is with the intended person's actual device.

---

### Step 5: Creating Encrypted Rooms

1. Click the "+" next to "Rooms" → "New Room."
2. Name your room.
3. Under "Room Security" toggle "Enable end-to-end encryption" to on.
4. Note: Once a room is created with E2E encryption, this cannot be disabled. Once created without it, it cannot be added.
5. Invite members after creation.

**Room settings to configure**:
- "Who can read history" → "Members only (since they joined)" prevents new members from seeing history.
- "Who can join" → set appropriately (invite only for sensitive groups).

---

### Threat Model by Use Case

**Journalist**: Matrix with self-hosted Synapse provides the highest-trust configuration — you control the server and can verify no third party has access. Element's encrypted rooms with verified participants are appropriate for sensitive coordination. Self-hosting requires security maintenance (keep Synapse updated; an unpatched self-hosted server is worse than a well-managed commercial option).

**Activist**: Matrix rooms federated across servers can be disrupted if a homeserver is taken down. For resilient organizing, ensure critical participants have accounts on different homeservers. The federated model means some room metadata (which users are in which rooms) is visible to multiple servers.

**Underground network**: Matrix self-hosted with mandatory device verification and invite-only rooms provides a strong baseline. However, the complexity of key management means user error (joining from an unverified device, losing the security key) can silently degrade security.

---

### Matrix Security Checklist

- [ ] Account created on a homeserver appropriate to your threat model
- [ ] Secure Backup security key generated and stored offline (not in cloud)
- [ ] All own devices verified via cross-signing
- [ ] Key contacts verified via emoji comparison or QR scan
- [ ] All sensitive rooms have E2E encryption enabled
- [ ] Room history visibility set to "Members only (since they joined)"
- [ ] Element updated to latest version (security patches are released regularly)

---

### Troubleshooting: Matrix / Element

**Problem**: "Unable to decrypt" message errors.
**Solution**: This occurs when your device does not have the session key for a particular message. Most common cause: you were not online when the message was sent and the sender's device has since been replaced or rotated keys. Ask the sender to re-send, or ensure your Secure Backup is properly configured so keys are recoverable.

**Problem**: New device shows all conversations as unverified.
**Solution**: Complete cross-signing verification with your existing device. If your existing device is no longer available, restore from Secure Backup using your security key.

**Problem**: Contact's messages show a warning icon.
**Solution**: Their device is unverified. Complete the verification flow with them before sharing sensitive content.

---

## Part 3: Briar

### What Briar Is and What It Actually Protects

Briar is a peer-to-peer messaging application for Android. Unlike Signal and Matrix, Briar has no central server. Messages are synchronized directly between devices.

Briar routes all internet communications through Tor by default, providing strong metadata protection — not just content encryption. When both parties are online, messages transit through Tor. When internet access is unavailable, Briar can synchronize via Bluetooth and Wi-Fi.

**Key properties**:
- No phone number required for registration.
- No email address required.
- No central server to subpoena.
- Contact discovery requires physical proximity (QR code scan) — there is no address book lookup or phone number search.
- All messages are end-to-end encrypted.

**Current limitation**: Briar is Android-only. There is no iOS version (as of 2025). There is a desktop companion app (Briar Desktop) in development but not yet feature-complete for general use.

**Official source**: [briarproject.org](https://briarproject.org) — download from Google Play, F-Droid (recommended for avoiding Google), or direct APK from the Briar website.

---

### Step 1: Install Briar

**Via F-Droid (recommended — avoids Google Play data collection)**:
1. Install F-Droid from [f-droid.org](https://f-droid.org) if not already installed. You may need to enable "Install from unknown sources" for your browser in Android Settings → Apps → your browser → Install unknown apps.
2. Open F-Droid, search for "Briar."
3. Install.

**Via Google Play**:
1. Search "Briar Messenger" — developer is "The Briar Project."
2. Install.

**Via direct APK**:
1. Navigate to [briarproject.org](https://briarproject.org).
2. Download the APK directly.
3. Enable "Install unknown apps" for your file manager.
4. Open the APK.

---

### Step 2: Create Your Account

1. Open Briar.
2. You will be prompted to "Create Account."
3. Choose a nickname. **Choose carefully — you cannot change this after account creation.** This is what your contacts will see.
4. Set a strong password. This password encrypts your Briar database on your device. If you forget it, your Briar account and all contacts and messages are unrecoverable.
5. Briar will now start connecting to the Tor network. This takes 1–3 minutes on first launch. You will see a status indicator showing Tor connection progress.

> **Common pitfall**: Choosing a nickname that reveals your identity. Your Briar nickname should be a pseudonym, not your real name, because it will be visible to all your Briar contacts.

---

### Step 3: Add Contacts

Because Briar has no central directory, adding contacts requires direct interaction.

**Method A — QR Code Exchange (most secure)**:
1. Both parties must be physically together.
2. Tap the "+" icon → "Add contact at a distance" or "Add nearby contact."
3. "Add nearby contact" uses Bluetooth proximity. Both parties tap this option. Briar will ask for camera permission (to scan QR code) and location permission (for Bluetooth scanning).
4. One person scans the other's QR code. After about 30 seconds, the devices connect and the contact is added.

**Method B — Exchange links (remote)**:
1. Tap the "+" icon → "Add contact at a distance."
2. Briar generates a unique contact link for you.
3. You share this link with your contact via a separate secure channel (e.g., Signal, in person).
4. Your contact enters your link and shares theirs.
5. When both parties are online via Tor, Briar completes the contact exchange.

> **Note**: The "Add contact at a distance" link is single-use per exchange. Create a new one for each contact.

---

### Step 4: Configure Connections

1. Settings (gear icon) → Connections.
2. You will see toggles for: Tor (Internet), Wi-Fi (local network), Bluetooth.
3. **Tor should remain enabled for all internet connections**. Disabling Tor and using Briar over clearnet defeats the primary anonymity benefit.
4. Wi-Fi and Bluetooth sync are useful when internet is unavailable or monitored. Enable them when you need offline synchronization.

**Battery and performance note**: Briar's Tor routing means it is slower and uses more battery than Signal. It is not intended as a high-volume daily messaging app. Use it for specific high-sensitivity contacts where the metadata protection justifies the friction.

---

### Threat Model by Use Case

**Journalist covering protests or active events**: Briar's Bluetooth/Wi-Fi sync is uniquely useful when internet is cut, throttled, or monitored at a venue. A network of nearby Briar users can relay messages hop-by-hop even without internet access.

**Activist in repressive country**: Briar's Tor routing means ISPs cannot see that you are using a messaging service at all (they see Tor traffic, which can be obfuscated further with Tor bridges). No account registration data exists that can be compelled from a company. The tradeoff is that contact establishment requires direct exchange.

**Underground network**: Briar's no-central-server model means there is no company to subpoena for member lists, message metadata, or account records. The primary attack surface is physical: device seizure.

---

### Briar Security Checklist

- [ ] Installed from F-Droid or official briarproject.org (preferred over Google Play for highest privacy)
- [ ] Strong password chosen for account encryption
- [ ] Tor connection verified before communicating (green status indicator in app)
- [ ] Nickname is a pseudonym, not real name
- [ ] Contacts added via direct QR code exchange when possible
- [ ] Tor (internet) connections enabled in Settings → Connections
- [ ] Wi-Fi and Bluetooth enabled only when needed for offline sync

---

### Troubleshooting: Briar

**Problem**: Briar cannot connect to Tor.
**Solution**: Check your internet connection. Briar connects automatically when Tor is reachable. If you are in a network that blocks Tor, you will need to configure Tor bridges: Settings → Connections → Tor Bridges. The Tor Project provides bridge addresses at [bridges.torproject.org](https://bridges.torproject.org).

**Problem**: Contact is not receiving messages.
**Solution**: Both parties must be online via Tor simultaneously for delivery. Briar does not store messages on a server — if both parties are not online at the same time, messages queue until they meet (online, via Bluetooth, or via Wi-Fi). This is an intentional design choice, not a bug.

**Problem**: Forgot Briar password.
**Solution**: There is no account recovery. The password encrypts your local database. If you forget it, you must reinstall Briar (erasing all data) and create a new account. This is by design — there is no server to hold a recovery key.

---

## Comparative Platform Summary

| Feature | Signal | Matrix (Element) | Briar |
|---|---|---|---|
| Registration requirement | Phone number | Email (server dependent) | None |
| Server dependency | Signal servers | Homeserver (can self-host) | None |
| Tor routing by default | No | No | Yes |
| iOS support | Yes | Yes | No |
| Offline (Bluetooth/WiFi) | No | No | Yes |
| Forward secrecy | Yes | Yes (per session) | Yes |
| Group chats | Yes (up to 1,000) | Yes (rooms) | Yes (forums) |
| Best for | Daily secure comms | Organization/teams | Highest-risk contacts |
| Metadata visibility | Carrier sees Signal traffic | Server sees room metadata | Hidden via Tor |

---

## Sources

- [EFF Surveillance Self-Defense: How to Use Signal](https://ssd.eff.org/module/how-to-use-signal)
- [Signal: What is a Safety Number](https://support.signal.org/hc/en-us/articles/360007060632)
- [Signal: Safety Number Updates (blog)](https://signal.org/blog/safety-number-updates/)
- [Freedom of the Press: Signal for Beginners](https://freedom.press/digisec/blog/signal-beginners/)
- [Privacy Guides: Signal Configuration and Hardening](https://www.privacyguides.org/articles/2022/07/07/signal-configuration-and-hardening/)
- [EFF: Creating and Managing Signal Groups](https://ssd.eff.org/module/creating-and-managing-signal-groups)
- [Matrix.org: End-to-End Encryption](https://matrix.org/docs/matrix-concepts/end-to-end-encryption/)
- [Element: Verifying Your Devices](https://element.io/blog/verifying-your-devices-is-becoming-mandatory-2/)
- [Briar Project: How It Works](https://briarproject.org/how-it-works/)
- [Briar: Quick Start Guide](https://briarproject.org/quick-start/)
- [Activist Security Checklist: Signal](https://activistchecklist.org/signal/)
