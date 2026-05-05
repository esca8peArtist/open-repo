---
title: "Tor and Anonymity Guide"
project: cybersecurity-hardening
created: 2026-05-05
status: complete
depends_on: opsec-playbook.md, threat-model.md, vpn-and-network-hardening-guide.md
confidence: high — sourced from Tor Project official documentation, Tor Browser manual, Privacy Guides Tor overview, EFF Surveillance Self-Defense
---

# Tor and Anonymity Guide

> **Danger**: Tor is not unbreakable. It provides strong anonymity against most adversaries but has documented weaknesses against nation-state-level traffic correlation. Endpoint attacks — malware, browser exploits, and behavioral deanonymization — remain the most common real-world path to identification. Use Tor as one layer of defense, not the only one.

---

## Threat Model: Who You Are Protecting Against

| Threat | Tor Helps | Tor Does Not Help |
|---|---|---|
| ISP logging your browsing | Yes — ISP sees only Tor traffic | Persistent fingerprinting if you use the same browser |
| Website logging your IP | Yes — exit node IP shown, not yours | Website cookies, fingerprinting, login linkage |
| Local network monitoring (Wi-Fi) | Yes — traffic encrypted in tunnel | |
| Law enforcement subpoena to your ISP | Yes — ISP has no browsing records | Subpoena to services you logged into over Tor |
| NSA-level traffic correlation | Partial — expensive, not bulk | Targeted individuals with entry/exit node visibility |
| Malware on your device | No | No |
| Logging into personal accounts over Tor | No — Tor can't help if you identify yourself | |

**Assets at risk**: Your IP address (and thereby your identity), your browsing history, and the fact that you are visiting particular destinations.

**Who Tor is for**: People who need strong anonymity for browsing, accessing .onion services, or creating accounts that must not link back to their real identity.

**Who Tor is not for**: Users who need high-speed performance (streaming, large downloads); users whose only concern is ISP data selling (a VPN is sufficient and faster for that use case).

---

## Part 1: Installing Tor Browser

### Why Tor Browser (Not Just Tor)

Tor the network is a set of relays that anonymize traffic. Using Tor the network alone (with a standard browser, for example) does not provide anonymity, because:
- Standard browsers have unique fingerprints (fonts, canvas rendering, screen dimensions, plugin lists) that identify you even without an IP address.
- Standard browsers send identifying headers that Tor cannot hide.

Tor Browser is Firefox modified by the Tor Project to eliminate fingerprinting differences between users. Every Tor Browser user presents the same fingerprint — creating a large anonymity set. The goal is not to hide that you use Tor, but to ensure you are indistinguishable from all other Tor Browser users.

### Download Tor Browser

**Official source**: [torproject.org](https://www.torproject.org) — this is the only legitimate source.

> **Danger**: Do not search for "Tor Browser download" in a search engine and click the first result. Malicious Tor Browser lookalikes exist. Verify the URL is exactly `https://www.torproject.org`.

**Verify the download (strongly recommended)**:
1. On the torproject.org download page, each release includes a cryptographic signature.
2. Download the signature file (.asc) alongside the browser package.
3. Import the Tor Project signing key: `gpg --auto-key-locate nodefault,wkd --locate-keys torbrowser@torproject.org`
4. Verify the signature: `gpg --verify tor-browser-linux64-<version>.tar.xz.asc tor-browser-linux64-<version>.tar.xz`
5. A valid result shows: "Good signature from 'Tor Browser Developers (signing key) <torbrowser@torproject.org>'"

**Detailed verification instructions**: [torproject.org/download/verify](https://www.torproject.org/download/verify/)

### Install on Windows

1. Download the Windows installer (.exe) from torproject.org.
2. Double-click to run. Windows may show a security warning — click "Run anyway" if you have verified the signature.
3. Choose an install directory. The default is your Desktop.
4. Launch "Start Tor Browser" from the installed shortcut.
5. Tor Browser opens a "Connect to Tor" screen. Click "Connect" if your internet is unrestricted.

### Install on macOS

1. Download the macOS .dmg from torproject.org.
2. Open the .dmg and drag Tor Browser to your Applications folder.
3. On first launch, macOS may warn about an unidentified developer. Go to System Settings → Privacy & Security → click "Open Anyway."
4. Tor Browser opens. Click "Connect."

### Install on Linux

1. Download the .tar.xz for your architecture (64-bit is standard).
2. Extract: `tar -xf tor-browser-linux64-<version>_ALL.tar.xz`
3. Navigate to the extracted folder: `cd tor-browser/`
4. Launch: `./start-tor-browser.desktop` or run `./Browser/start-tor-browser`

> **Note**: Tor Browser does not install system-wide on Linux. The extracted folder contains the complete browser. Keep it in a stable location (e.g., `~/Applications/`) and create a desktop shortcut if needed.

### Tor Browser 15.0 (October 2025)

Tor Browser 15.0, released October 2025, is based on Firefox ESR 140. It includes vertical tabs, tab groups, and improved usability. Security protections remain equivalent to prior versions. Update automatically via Tor Browser → About → Check for Updates.

---

## Part 2: Tor Circuits — How They Work

### Circuit Architecture

When you visit a website in Tor Browser, the browser builds a Tor circuit:

1. **Guard (Entry) Node**: The first relay. Your device connects to this relay directly. Your ISP can see that you are connecting to a Tor guard node.
2. **Middle Node**: A relay your guard passes traffic to. Neither the guard nor the exit knows both your identity and your destination.
3. **Exit Node**: The relay that makes the final connection to the destination website. The exit sees the destination but not who you are.

Each of the three relays knows only its neighbors — not the full path. This is the core of Tor's anonymity model.

### Circuit Lifespan

Tor Browser creates a new circuit for each domain you visit. The circuit for a given domain remains active for up to 10 minutes from first use. After that, a new circuit is built. This prevents an observer from correlating activity over time to the same circuit.

You can manually request a new circuit: click the padlock icon in the address bar → "New Circuit for this Site."

For a completely fresh identity: Tor Browser → hamburger menu → "New Identity." This closes all tabs, clears all state, and builds entirely new circuits.

### Guard Relay Pinning

Your guard (entry) node is deliberately kept stable over 2–3 months. This is intentional. The reason: if Tor randomly selected a new entry node for every circuit, an attacker who operates many Tor relays could increase their chances of being both your entry and exit node (enabling traffic correlation). With a stable guard, the attacker must specifically compromise your guard node rather than getting lucky in a random selection.

> **Practical implication**: Do not try to change your guard relay. Tor's circuit selection algorithm is mathematically optimized for anonymity. Manual overrides weaken it. [Source: torproject.org guard relay documentation](https://support.torproject.org/tor-browser/security/guard-relay/)

---

## Part 3: Stream Isolation

Stream isolation is Tor Browser's method of ensuring that different activities cannot be correlated by an observer who controls relays.

By default, Tor Browser uses a separate circuit for each domain. This means your browsing on `example.com` uses a different circuit than `anothersite.com`. An exit node that controls one circuit cannot link your two browsing sessions.

**What this protects**: A malicious exit node operator cannot confirm that the person connecting to `activistforum.org` is the same person connecting to `gmail.com`.

**What this does not protect**: If you log into an account on a site (e.g., Gmail), you have identified yourself to that site regardless of which circuit you used to reach it.

---

## Part 4: Entry and Exit Node Risks

### Entry Node (Guard) Risks

Your ISP can see that you are connecting to a Tor guard node. In some threat models, using Tor itself is a red flag. If this is a concern:

**Tor Bridges**: Bridge relays are unlisted Tor relays that are not publicly known. Your ISP cannot block or identify them as Tor traffic. Obtain bridge addresses from:
- [bridges.torproject.org](https://bridges.torproject.org)
- Email `bridges@torproject.org` with "get transport obfs4" in the body

**obfs4 and Snowflake bridges**: The `obfs4` transport obfuscates Tor traffic so it does not look like Tor. Snowflake uses WebRTC to blend traffic with normal browser activity. Snowflake is easier to set up; obfs4 is more effective against deep packet inspection.

**Configure bridges in Tor Browser**:
1. Tor Browser → Connection Settings → Use a bridge → Select or enter bridge addresses.
2. For obfs4: enter the bridge line provided by the Tor Project.
3. For Snowflake: select "Snowflake" from the built-in list — no additional configuration needed.

### Exit Node Risks

The exit node can see your destination and the content of unencrypted connections.

- Always use HTTPS. Tor Browser enforces HTTPS where available (HTTPS-Only Mode). If you see an HTTP connection, the exit node sees your data in plaintext.
- Do not submit passwords, personal information, or login credentials over HTTP through Tor — even HTTP to a site you trust, because the exit node is not your trusted party.
- Exit nodes are operated by volunteers, some of whom are malicious. Multiple security researchers have documented exit nodes performing SSL stripping, traffic injection, and credential harvesting on unencrypted connections.

### Traffic Correlation Attack (NSA-Level Risk)

A "global passive adversary" (an entity that can observe traffic entering and leaving the Tor network) can correlate timing and volume patterns to link you to your destination. This attack is well-documented in academic literature and is theoretically feasible for the NSA given its backbone surveillance capability.

**Important nuance**: This is not a bulk surveillance technique. It is computationally expensive and requires active operation against a specific target. For the vast majority of users, this threat is not realistic in practice. For national security journalists or high-profile targets of government investigation, this threat is real.

**Mitigation**: There is no complete mitigation against a global passive adversary within Tor. Latency-adding techniques (adding random delays) are implemented in Tor's design but imperfect. For highest-risk scenarios, physical security (dedicated hardware, air gaps, offline communication) is necessary in addition to Tor.

---

## Part 5: Security Configuration

### Security Level Settings

Tor Browser has three security levels: Standard, Safer, Safest.

**Standard**: Default Firefox protections plus Tor. JavaScript enabled. Suitable for browsing clearnet sites.

**Safer**: Disables JavaScript on non-HTTPS sites. Removes potentially dangerous fonts. Disables SVG, MathML. Use this for general privacy browsing.

**Safest**: Disables JavaScript everywhere. Removes all fonts except defaults. Disables images on non-HTTPS sites. This is appropriate for high-risk browsing and .onion sites.

**Configure**:
1. Tor Browser → hamburger menu → Security Settings (or shield icon in toolbar).
2. Drag the slider to "Safer" or "Safest."

> **Practical tradeoff**: "Safest" will break many websites. Use it when security is the priority; switch to "Standard" for ordinary browsing where you are not concerned about anonymity.

### NoScript Configuration

Tor Browser includes NoScript, which blocks JavaScript by default on new sites. At "Standard" level, NoScript allows scripts by default. At "Safer" and "Safest," it blocks them.

Do not whitelist scripts on sites you visit via Tor for anonymity purposes. A malicious site can use JavaScript to:
- Enumerate local network resources (revealing your actual IP in some configurations)
- Exploit browser vulnerabilities
- Link Tor sessions via localStorage or IndexedDB

### Never Maximize the Browser Window

Tor Browser's design relies on all users presenting an identical fingerprint. Your screen size is part of your fingerprint. Maximizing the window to your screen's native resolution breaks uniformity. Keep Tor Browser at its default window size.

---

## Part 6: Common Mistakes

### 1. Logging Into Accounts Over Tor

Logging into Gmail, Facebook, or any account that knows your real identity immediately deanonymizes you for that site. If you need to use an anonymous Tor identity to access a site, that site cannot be linked to your real-world accounts.

**Correct pattern**: Create separate accounts for Tor activity. Never access personal accounts in Tor Browser.

### 2. Opening Downloaded Files in External Applications

PDFs, Word documents, and other files downloaded through Tor can contain active content (JavaScript in PDFs, macros in Word) that opens network connections and reveals your real IP outside the Tor tunnel.

**Correct pattern**: Use "Safest" security level, which mitigates many of these risks. For sensitive files, open them in a virtual machine disconnected from the internet, or use a dedicated offline device.

### 3. Installing Additional Extensions

Tor Browser's fingerprint relies on all users being identical. Adding extensions (ad blockers, password managers, etc.) makes your browser unique and fingerprintable.

**Correct pattern**: Do not install extensions in Tor Browser. If you need extensions, use a separate browser profile. NoScript and uBlock Origin variants designed for Tor are already included where appropriate.

### 4. Using Torrents or P2P Over Tor

BitTorrent and P2P applications bypass the SOCKS proxy and connect directly, revealing your real IP. Additionally, Tor's design is optimized for low-latency interactive traffic, not high-bandwidth sustained transfers — torrenting over Tor degrades the network for all users.

### 5. Tab Correlation

If you have two tabs open in Tor Browser — one where you are logged in with your real identity and one where you are anonymous — browser state (cache, cookies, session storage) can leak between tabs.

**Correct pattern**: Use "New Identity" to completely separate sessions. Never mix identified and anonymous activity in the same Tor Browser session.

---

## Part 7: Accessing .onion Services

.onion addresses are hidden services that operate entirely within the Tor network. The server's IP address is hidden from you; you are hidden from the server.

**Why .onion services are more secure than clearnet via Tor**:
- There is no exit node. Traffic never leaves the Tor network.
- The connection is end-to-end encrypted between your Tor client and the hidden service.
- Neither party learns the other's IP address.

**Examples of legitimate .onion services**:
- SecureDrop for whistleblowing: many news organizations provide .onion SecureDrop addresses. The Freedom of the Press Foundation maintains a directory at [securedrop.org](https://securedrop.org).
- ProtonMail .onion: `protonmailrmez3lotccipshtkleegetolb73fuirgj7r4o4vfu7ozyd.onion`
- DuckDuckGo .onion: `https://duckduckgogg42xjoc72x3sjasowoarfbgcmvfimaftt6twagswzczad.onion`

**How to access .onion addresses**: Simply enter the .onion URL into Tor Browser's address bar. Tor Browser resolves .onion addresses natively.

---

## Security Configuration Checklist

- [ ] Tor Browser downloaded only from torproject.org
- [ ] Download signature verified before installation
- [ ] Security level set to "Safer" or "Safest" depending on use case
- [ ] Browser window not maximized (keeps at default size)
- [ ] No additional extensions installed
- [ ] HTTPS-Only Mode enabled (default in Tor Browser)
- [ ] "New Identity" used when switching between sensitive sessions
- [ ] Downloaded files opened in sandboxed/offline environment, not directly
- [ ] Not logged into personal accounts in Tor Browser
- [ ] Bridge relays configured if ISP blocks Tor or if Tor usage is itself sensitive
- [ ] Guard relay not manually overridden

---

## Troubleshooting

**Problem**: Tor Browser cannot connect.
**Solution**: Check your internet connection. If Tor is blocked by your ISP or network, try bridges: Connection Settings → Use a bridge → Snowflake (easiest, no configuration). If Snowflake is blocked, obtain obfs4 bridges from [bridges.torproject.org](https://bridges.torproject.org).

**Problem**: Very slow browsing.
**Solution**: Tor adds inherent latency. For speed: use "Standard" security level (JavaScript enabled makes pages load faster). Choose Tor Browser for tasks that require anonymity, and a hardened standard browser for non-anonymous browsing. Do not attempt large file downloads through Tor.

**Problem**: Site shows "You appear to be using Tor" and blocks access.
**Solution**: Some sites block Tor exit node IP ranges. Use Tor Browser → New Circuit for This Site to get a different exit node. If the site consistently blocks Tor, it is deliberately restricting Tor users — consider whether the site's tracking is part of your threat model.

**Problem**: Warning: "Something is interfering with Tor Browser."
**Solution**: This indicates a potential proxy interception or MITM on your local network. Check whether your network uses content filtering (corporate proxy, school network). On such networks, configure Tor bridges to tunnel through the proxy.

---

## Sources

- [Tor Project Official Download](https://www.torproject.org/download/)
- [Tor Browser Manual: Managing Identities](https://tb-manual.torproject.org/managing-identities/)
- [Tor Project: Understanding Guard Relays](https://support.torproject.org/tor-browser/security/guard-relay/)
- [Tor Project: Guard Relay Specification](https://spec.torproject.org/guard-spec/index.html)
- [Privacy Guides: Tor Overview](https://www.privacyguides.org/en/advanced/tor-overview/)
- [Tor Project: Improving Anonymity via Guard Parameters](https://blog.torproject.org/improving-tors-anonymity-changing-guard-parameters/)
- [EFF Surveillance Self-Defense: Tor](https://ssd.eff.org/module/how-to-use-tor-browser)
