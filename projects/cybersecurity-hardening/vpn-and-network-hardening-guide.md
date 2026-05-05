---
title: "VPN and Network Hardening Guide"
project: cybersecurity-hardening
created: 2026-05-05
status: complete
depends_on: opsec-playbook.md, threat-model.md
confidence: high — sourced from Mullvad official documentation, ProtonVPN support, EFF, Privacy Guides, IVPN documentation, court-verified no-log policy research
---

# VPN and Network Hardening Guide

> **Danger**: A VPN is not anonymity. It shifts trust from your ISP to the VPN provider. If the VPN provider has logs, keeps payment records, or is subject to jurisdiction-appropriate legal process, you can be identified. Understand this before treating a VPN as a security guarantee.

---

## Threat Model: Who You Are Protecting Against

| Threat | VPN Helps | VPN Does Not Help |
|---|---|---|
| ISP selling your browsing data to advertisers | Yes — ISP sees only VPN traffic | Endpoint tracking (cookies, fingerprinting) |
| ISP logging traffic content | Yes — traffic is encrypted | Provider logs, if any exist |
| Network-level surveillance (Wi-Fi sniffing) | Yes — traffic encrypted in transit | Device compromise |
| Law enforcement subpoena to your ISP | Yes — ISP has no content records | Subpoena to VPN provider |
| NSA backbone surveillance | Partial — content encrypted | Traffic correlation at scale against targeted individuals |
| Malware, phishing, endpoint attacks | No | No |

**Assets at risk**: Your browsing history, the IP addresses you connect to, your real IP address (as seen by websites), and connection metadata your ISP retains.

**Prerequisite**: Before selecting a VPN, understand what you are protecting against. A VPN to watch streaming content has different requirements than a VPN for protecting activist communications.

---

## Part 1: VPN Selection Criteria

### Jurisdiction

The most important factor is the legal environment in which the VPN provider operates.

**Five Eyes, Nine Eyes, Fourteen Eyes** are intelligence-sharing alliances. VPN providers incorporated in these jurisdictions can be compelled by intelligence agencies under laws that may not require judicial oversight or disclosure to the target:

- Five Eyes: USA, UK, Canada, Australia, New Zealand
- Nine Eyes: adds France, Netherlands, Denmark, Norway
- Fourteen Eyes: adds Germany, Belgium, Italy, Sweden, Spain

A provider in Sweden (Mullvad) or Switzerland (ProtonVPN) has stronger legal protections against covert disclosure than a U.S.-based provider, but is not immune — EU and Swiss law allow compelled disclosure for serious crimes.

**The most relevant question is not jurisdiction alone, but what data the provider actually retains.** A U.S. provider with genuinely zero logs provides less actionable information under an NSL than a Swiss provider with extensive logs.

### Logging Policy

"No logs" is a marketing claim. Evaluate it through independent audit results and case history.

**Court-verified no-log providers** (as of 2025):

- **Mullvad**: Swedish jurisdiction. In 2023, Swedish police raided a Mullvad data center. They found no customer data to seize. Mullvad does not require an email to sign up, accepts cash and Monero payments, and issues account numbers rather than linked accounts. This is the most privacy-forward commercial VPN available. [mullvad.net](https://mullvad.net)

- **ProtonVPN**: Swiss jurisdiction. Independent audits by SEC Consult. Proton has been compelled to provide data to Swiss authorities in specific criminal cases (the 2021 climate activist case), but in that case the data sought was email (ProtonMail) metadata, not VPN logs. ProtonVPN's no-log claim has not been disproven. [protonvpn.com](https://protonvpn.com)

- **IVPN**: Gibraltar jurisdiction. Independent audit by Cure53 published publicly. Accepts Monero and cash payments. [ivpn.net](https://www.ivpn.net)

> **Danger**: Do NOT choose a VPN based on advertising, Reddit promotional posts, or affiliate-link review sites. The VPN industry is heavily corrupted by affiliate marketing where reviewers receive 30–50% of subscription revenue. Prioritize providers with public audit results and verifiable no-log track records.

### Audit Results

Ask whether a provider has published independent security audits. The audit should be:
- Conducted by an independent firm (Cure53, SEC Consult, Quarkslab are well-regarded)
- Published publicly (not just "we had an audit")
- Recent (within the past 2 years)

Mullvad publishes all audit results at [mullvad.net/blog/tag/audits](https://mullvad.net/blog/tag/audits). ProtonVPN publishes audits at [protonvpn.com/blog/security-audits](https://protonvpn.com/blog/security-audits).

### Protocol Selection

**WireGuard** is the recommended protocol for most users. It uses modern cryptography: Curve25519 for key exchange, ChaCha20-Poly1305 for symmetric encryption, and BLAKE2s for hashing. WireGuard's code base is approximately 4,000 lines — compared to OpenVPN's hundreds of thousands — making it significantly easier to audit and less likely to contain implementation errors.

WireGuard is faster than OpenVPN in practice due to its kernel-level implementation (on Linux) and simpler handshake.

> **Note**: As of January 15, 2026, Mullvad ended OpenVPN support entirely in favor of WireGuard. This reflects industry consensus on WireGuard's security and performance advantages.

**OpenVPN** remains an option on some providers and platforms. It is more mature and more configurable, but its code complexity is a liability from an auditing perspective. If you need OpenVPN for compatibility, ensure you are using TLS 1.2+ and AES-256-GCM cipher suites.

---

## Part 2: Mullvad VPN Setup

### Step 1: Create an Account

1. Navigate to [mullvad.net](https://mullvad.net).
2. Click "Get started."
3. Mullvad generates a 16-digit account number. **There is no email, no name, no account registration.** The account number is your only credential. Store it in a password manager.
4. Add time to the account: Mullvad accepts credit cards, PayPal, bank transfer, Swish, cash (mailed to their office), Bitcoin, and Monero. For highest anonymity, pay with cash or Monero.

> **Danger**: Paying with a credit card linked to your identity partially defeats the purpose of an anonymous VPN. The payment creates a record linking your identity to the account number. For high-risk users, cash or Monero payment is essential.

### Step 2: Download and Install the App

1. Go to [mullvad.net/en/download](https://mullvad.net/en/download).
2. Download the app for your platform (Windows, macOS, Linux, Android, iOS).
3. Install the application.
4. Open the app, enter your 16-digit account number.

### Step 3: Configure the Kill Switch

The Mullvad app's kill switch is enabled by default. It blocks all traffic outside the VPN tunnel if the connection drops. This prevents your real IP from leaking if the VPN disconnects unexpectedly.

**Verify the kill switch is active**:
1. Open Mullvad app → Settings → VPN Settings.
2. Confirm "Block when disconnected (kill switch)" is enabled.
3. Test it: connect to the VPN, note a website you can access. Disconnect the VPN manually (not via the app — pull the network cable or disable Wi-Fi). Try to access the website. If the kill switch works, the connection should fail completely rather than falling back to your real IP.

> **Danger**: The kill switch in third-party WireGuard clients (using Mullvad config files rather than the Mullvad app) must be manually configured. See Part 5 for WireGuard manual configuration.

### Step 4: Enable DNS Leak Protection

DNS queries reveal your browsing activity even if your traffic is encrypted. When connected to a VPN, DNS requests must go through the VPN's DNS servers, not your ISP's.

1. Mullvad app → Settings → VPN Settings → DNS Content Blockers.
2. Verify "Use custom DNS" is not set to an external resolver — Mullvad's default DNS (10.64.0.1) handles DNS within the tunnel.
3. Test for DNS leaks: visit [mullvad.net/en/check](https://mullvad.net/en/check) while connected. This shows your apparent IP and whether DNS is leaking.

### Step 5: Select a Server

1. In the Mullvad app, select a country and city.
2. For general privacy: select a server in a jurisdiction with strong privacy laws (Sweden, Switzerland, Iceland, Germany).
3. For performance: select a server geographically close to you (lower latency).
4. Avoid selecting servers in Five Eyes jurisdictions if your threat model includes government-level surveillance.

---

## Part 3: ProtonVPN Setup

### Why You Might Choose ProtonVPN over Mullvad

ProtonVPN integrates with ProtonMail and ProtonDrive. If you are already using the Proton ecosystem for encrypted email, ProtonVPN provides a unified privacy stack. ProtonVPN also offers a free tier (slower speeds, fewer servers) which is appropriate for users who cannot pay.

### Step 1: Create an Account

1. Navigate to [protonvpn.com](https://protonvpn.com).
2. Click "Get Proton VPN."
3. Enter an email address. For high-risk users, create a ProtonMail address and use that — do not use an address linked to your real identity.
4. Choose a plan. The free plan is functional but limited to 3 countries and medium speeds.

### Step 2: Install and Configure

1. Download the Proton VPN app from [protonvpn.com/download](https://protonvpn.com/download).
2. Log in with your Proton account.
3. Enable the kill switch: App → Settings → Kill Switch → Always-on.

**Kill switch modes**:
- "Permanent" (on by default when enabled): blocks internet access whenever VPN is not connected, including during system startup.
- "On": blocks internet if VPN disconnects unexpectedly, but allows non-VPN access when you manually disconnect.
For highest protection, use "Permanent."

### Step 3: Enable Multi-Hop (Secure Core)

ProtonVPN's "Secure Core" feature routes traffic through two VPN servers in different countries — traffic first passes through a server in a privacy-friendly jurisdiction (Switzerland, Iceland, Sweden), then exits through a second server. This means an adversary watching the exit server cannot correlate traffic back to your real IP without also compromising the entry server.

1. App → Settings → Secure Core → Enable.
2. In the server list, look for servers marked "SC" (Secure Core).
3. Performance impact: multi-hop routing adds latency. Expect 30–100ms additional latency compared to single-hop. This is an acceptable tradeoff for high-risk use cases.

> **Threat model note**: Secure Core is useful when you are concerned about a compromised exit server or surveillance at the network level of the exit country. It does not protect against a provider that logs, since Proton sees the initial connection. It adds meaningful protection against traffic correlation attacks.

---

## Part 4: Manual WireGuard Configuration

For users who want to use WireGuard without a provider's app, or who need to configure WireGuard on Linux at the system level.

### Why Manual Configuration

- Greater transparency — you can inspect exactly what the WireGuard configuration sends.
- Works on any Linux system without a proprietary app.
- Allows integration with system-level firewall rules.
- Required for router-level VPN configuration.

### Step 1: Generate a WireGuard Configuration (Mullvad Example)

1. Log in to your Mullvad account at [mullvad.net/account](https://mullvad.net/account).
2. Go to "WireGuard configuration."
3. Generate a key pair (Mullvad generates it for you in the browser, or you can generate locally and upload the public key for better key security).
4. Select a server and download the `.conf` file.

**Anatomy of a WireGuard .conf file**:
```ini
[Interface]
PrivateKey = <your_private_key>
Address = 10.64.x.x/32
DNS = 10.64.0.1

[Peer]
PublicKey = <server_public_key>
AllowedIPs = 0.0.0.0/0, ::/0
Endpoint = <server_ip>:51820
```

- `PrivateKey`: your device's private key. Keep this secret — it is the equivalent of a password.
- `Address`: the VPN-assigned IP for your device inside the tunnel.
- `DNS`: Mullvad's DNS server inside the tunnel. This is critical — if DNS is not set to the in-tunnel address, your DNS queries leak.
- `AllowedIPs = 0.0.0.0/0` means all traffic is routed through the tunnel (full tunnel mode).
- `Endpoint`: the Mullvad server's public IP and WireGuard port.

### Step 2: Install WireGuard on Linux

```bash
# Debian/Ubuntu
sudo apt install wireguard

# Fedora/RHEL
sudo dnf install wireguard-tools

# Arch Linux
sudo pacman -S wireguard-tools
```

### Step 3: Deploy the Configuration

```bash
# Copy the config file to the WireGuard directory
sudo cp mullvad-se-sto.conf /etc/wireguard/wg0.conf

# Set correct permissions (private key must not be readable by others)
sudo chmod 600 /etc/wireguard/wg0.conf

# Start the WireGuard interface
sudo wg-quick up wg0

# Verify connection
sudo wg show
```

### Step 4: Add a Kill Switch (UFW Method for Ubuntu/Debian)

WireGuard's `wg-quick` supports a `PostUp`/`PreDown` configuration for kill switch behavior. Add to the `[Interface]` section of your `.conf` file:

```ini
[Interface]
PrivateKey = <your_private_key>
Address = 10.64.x.x/32
DNS = 10.64.0.1
PostUp = ufw default reject outgoing; ufw allow out on wg0 from any to any
PreDown = ufw default allow outgoing
```

> **Danger**: This kill switch blocks all non-VPN traffic. Test on a non-critical system first. If you misconfigure this and the VPN fails to start, you may lose all outbound connectivity until you manually remove the UFW rule. Have physical console access or an alternative connection method available.

### Step 5: Auto-start on Boot (systemd)

```bash
sudo systemctl enable wg-quick@wg0
sudo systemctl start wg-quick@wg0
```

---

## Part 5: DNS Over HTTPS / DNS Over TLS

Even with a VPN, DNS configuration on your local network is a security consideration. When not connected to a VPN, DNS queries go to your ISP by default.

### Why DNS Encryption Matters

Standard DNS is unencrypted. Your ISP (and any network intermediary) can see every domain you query. ISPs sell this data. DNS over HTTPS (DoH) and DNS over TLS (DoT) encrypt DNS queries.

### Configure DNS Over HTTPS in Firefox

1. Firefox → Settings → Privacy & Security → scroll to DNS over HTTPS.
2. Enable "Max Protection" — Firefox will only resolve DNS over HTTPS and will block the page if DoH is unavailable.
3. Choose a resolver. Options:
   - **Cloudflare (1.1.1.1)**: Fast, logs minimal data, U.S. company. Publishes annual transparency reports.
   - **NextDNS**: Configurable blocking, logs optional, can disable logging entirely.
   - **Mullvad's DNS (adblock.dns.mullvad.net)**: Uses Mullvad's infrastructure, best for Mullvad VPN users.

### Configure DNS Over HTTPS System-Wide (Linux — systemd-resolved)

```bash
# Edit /etc/systemd/resolved.conf
sudo nano /etc/systemd/resolved.conf

# Add or modify:
[Resolve]
DNS=1.1.1.1#cloudflare-dns.com 9.9.9.9#dns.quad9.net
DNSOverTLS=yes
DNSSEC=yes
```

Then restart: `sudo systemctl restart systemd-resolved`

---

## Part 6: Exit Node Risks and Multi-Hop Routing

### Exit Node Risks

When you use a VPN, your traffic exits from the VPN server. The VPN exit server sees your traffic in plaintext if the destination does not use HTTPS. Additionally:

- The exit server's IP address is what destination websites see. If the exit server's IP is on blocklists (e.g., because other VPN users have abused it), you may be blocked from services.
- Law enforcement in the exit country can monitor outbound traffic from VPN servers in that country.
- If you are accessing a resource that only exists in one country, you may need to exit in that country — accepting the associated legal risks.

### Multi-Hop Routing

Multi-hop routes your traffic through two or more VPN servers before exiting. The rationale: if an adversary is watching the exit server, they cannot trace traffic back to your real IP without also compromising the entry server (which is in a different jurisdiction and operated by the same provider).

**ProtonVPN Secure Core** (see Part 3) provides this. Mullvad also supports multi-hop by configuring two tunnel endpoints.

**When multi-hop provides meaningful protection**: When you are concerned about exit-server-level surveillance or traffic analysis at the VPN server level. Against a provider that logs, multi-hop provides no additional protection — the provider sees both ends.

---

## Performance vs. Security Tradeoffs

| Configuration | Security Level | Performance Impact |
|---|---|---|
| No VPN | Low | None |
| Single-hop VPN (WireGuard) | Moderate | 5–15% overhead |
| Single-hop VPN (OpenVPN) | Moderate | 15–30% overhead |
| Multi-hop VPN (Secure Core) | Higher | 30–60% overhead; 30–100ms added latency |
| VPN + Tor | High | Significant; Tor adds 100–300ms+ |
| Tor only | High for anonymity | Tor-level: 100–500ms typical |

> **Practical guidance**: For most users, a single-hop WireGuard VPN from Mullvad or ProtonVPN provides adequate protection against ISP surveillance and network-level monitoring with minimal performance impact. Multi-hop and Tor are appropriate when your threat model includes surveillance at the network level or targeted government investigation.

---

## VPN and Network Security Checklist

- [ ] VPN provider chosen based on verified no-log policy, independent audit, and jurisdiction
- [ ] Payment method does not link your identity to the account (cash, Monero, or pre-paid card)
- [ ] Kill switch enabled and tested (disconnect VPN, verify no traffic flows)
- [ ] DNS leak test passed ([mullvad.net/check](https://mullvad.net/check) or [dnsleaktest.com](https://dnsleaktest.com))
- [ ] WireGuard protocol selected (preferred over OpenVPN for most users)
- [ ] Server selected in appropriate jurisdiction for your threat model
- [ ] DNS over HTTPS enabled in browser and/or system
- [ ] For high-risk users: multi-hop (Secure Core) enabled
- [ ] VPN kill switch tested under simulated disconnect scenario

---

## Troubleshooting

**Problem**: VPN connects but DNS is leaking (dnsleaktest.com shows ISP DNS).
**Solution**: Check that the DNS setting in your WireGuard config or VPN app points to the in-tunnel DNS address (10.64.0.1 for Mullvad). On Linux with manual WireGuard, run `resolvectl status wg0` to verify the DNS resolver for the WireGuard interface. If systemd-resolved is not routing DNS through WireGuard, you may need to configure `DNS=` in your wg0 config and ensure systemd-resolved is set to use per-interface DNS.

**Problem**: Kill switch blocked all traffic; cannot reconnect to VPN.
**Solution**: On Linux with UFW: run `sudo ufw default allow outgoing` to restore outbound connectivity, then diagnose why the VPN failed to start. Check `sudo wg show` and `sudo journalctl -u wg-quick@wg0` for error messages.

**Problem**: VPN performance is very slow.
**Solution**: Try a server closer to your geographic location. WireGuard is significantly faster than OpenVPN — switch protocols if available. If using multi-hop, the added latency is expected; switch to single-hop for performance-sensitive tasks.

**Problem**: Websites blocking VPN IP addresses.
**Solution**: Many websites block known VPN IP ranges. Try different server locations. Mullvad and ProtonVPN rotate IP addresses regularly. For sites that require your apparent location to match your real location, a VPN exit in your home country is necessary.

---

## Sources

- [Mullvad: Using the Mullvad VPN App](https://mullvad.net/en/help/using-mullvad-vpn-app)
- [Mullvad: WireGuard on Linux Terminal](https://mullvad.net/en/help/wireguard-and-mullvad-vpn)
- [ProtonVPN: WireGuard Configuration Files](https://protonvpn.com/support/wireguard-configurations)
- [ProtonVPN: WireGuard on Linux Manual Setup](https://protonvpn.com/support/wireguard-linux)
- [Privacy Guides: VPN Overview](https://www.privacyguides.org/en/vpn/)
- [EFF: Surveillance Self-Defense - VPN](https://ssd.eff.org/module/choosing-vpn-thats-right-you)
- [IVPN: Why You Don't Need a VPN](https://www.ivpn.net/privacy-guides/why-you-dont-need-a-vpn/)
