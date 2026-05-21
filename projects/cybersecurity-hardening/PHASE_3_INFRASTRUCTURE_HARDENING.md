---
title: "Phase 3 Infrastructure Hardening"
project: cybersecurity-hardening
phase: 3
status: research-complete
created: 2026-05-21
target-execution: June–July 2026
confidence: high
---

# Phase 3: Infrastructure Hardening

**Most critical finding**: The single highest-leverage infrastructure security action for a Raspberry Pi home lab is network segmentation with a flat-network-to-VLAN migration. A flat home network — where your IoT devices, Pi lab, personal laptops, and smart TV all share the same broadcast domain — means a compromised smart plug or baby monitor has direct Layer 2 access to attack stockbot's API endpoints, sniff traffic, and reach the router admin interface. VLANs eliminate this lateral movement path at the network layer before any software security control is even invoked.

---

## 1. Network Segmentation: VLANs for the Pi Home Lab

### VLAN Architecture

| VLAN | ID | Purpose | Devices | Internet Access | Inter-VLAN |
|---|---|---|---|---|---|
| Trusted | 10 | Primary personal devices | Laptops, phones, work machines | Yes | No |
| Lab | 20 | Pi home lab projects | stockbot Pi, seedwarden Pi, NAS | Yes (restricted) | No |
| IoT | 30 | Smart home devices | Cameras, smart plugs, thermostats | Yes (limited) | No |
| Guest | 40 | Visitor WiFi | Guest devices | Yes | No |
| Management | 99 | Router/switch admin | Router, managed switch | No | Admin only |

Inter-VLAN traffic is blocked by default (enforced at the router/firewall). The only permitted inter-VLAN flows are explicitly defined:
- Trusted → Lab: SSH (port 22), specific application ports (e.g., stockbot dashboard on port 8080)
- Management: only accessible from Trusted VLAN, never from other VLANs or internet

### Hardware Requirements

VLAN segmentation requires either:
1. A **managed switch** that supports 802.1Q VLAN tagging (e.g., TP-Link TL-SG108E, ~$30; Netgear GS308E, ~$35)
2. A **router with VLAN support** — pfSense, OPNsense, or a consumer router running OpenWrt

**Recommended minimum setup**:
- OPNsense or pfSense on a small PC (e.g., Protectli Vault, $200–350) as the router/firewall
- TP-Link TL-SG108E as the managed switch
- A WiFi access point that supports VLAN-tagged SSIDs (e.g., TP-Link EAP series, Ubiquiti UniFi)

**If you already have a consumer router**: OpenWrt supports VLANs on many devices. Check `openwrt.org/toh` for your router's compatibility. This is the lowest-cost path but requires comfort with OpenWrt configuration.

### Firewall Rules (OPNsense/pfSense example)

```
# VLAN 30 (IoT) rules
# Allow IoT to reach internet (DNS on VLAN 30 gateway, HTTP/HTTPS only)
pass out on IoT interface proto tcp from IoT:network to any port {80, 443}
pass out on IoT interface proto udp from IoT:network to IoT:gateway port 53
# Block all inter-VLAN from IoT
block in on IoT interface from IoT:network to Lab:network
block in on IoT interface from IoT:network to Trusted:network
block in on IoT interface from IoT:network to Management:network

# VLAN 20 (Lab) rules
# Allow Lab outbound (needed for package updates, API calls)
pass out on Lab interface from Lab:network to any
# Allow Trusted to reach specific Lab services
pass in on Trusted interface proto tcp from Trusted:network to Lab:network port {22, 8080, 443}
# Block all other inbound to Lab
block in on Lab interface from !Trusted:network to Lab:network
```

---

## 2. Identity and Access Management: SSO with Authentik

### Why SSO for a Home Lab

Without SSO, each Pi project maintains its own credentials and authentication. This creates credential sprawl: separate passwords for stockbot dashboard, Wazuh web UI, NAS admin, router admin, etc. SSO centralizes authentication through a single identity provider, enables MFA enforcement across all applications, and provides a single audit log of who accessed what and when.

### Authentik

Authentik is a self-hosted, open-source identity provider supporting OIDC, SAML 2.0, LDAP, and proxy authentication. It is the recommended SSO solution for home labs over Keycloak because:
- Significantly lower resource footprint (Keycloak requires 512MB–1GB RAM; Authentik runs in ~256MB)
- More modern UI with better Docker Compose deployment
- Built-in outpost/proxy mode that can protect applications that don't natively support OIDC

**Docker Compose deployment** (run on a dedicated Pi or VM, bind to Tailscale IP):
```yaml
# docker-compose.yml
version: "3.4"
services:
  postgresql:
    image: docker.io/library/postgres:16-alpine
    restart: unless-stopped
    environment:
      POSTGRES_PASSWORD: ${PG_PASS:?error}
      POSTGRES_USER: authentik
      POSTGRES_DB: authentik
    volumes:
      - database:/var/lib/postgresql/data

  redis:
    image: docker.io/library/redis:alpine
    restart: unless-stopped

  server:
    image: ghcr.io/goauthentik/server:latest
    restart: unless-stopped
    command: server
    environment:
      AUTHENTIK_REDIS__HOST: redis
      AUTHENTIK_POSTGRESQL__HOST: postgresql
      AUTHENTIK_POSTGRESQL__USER: authentik
      AUTHENTIK_POSTGRESQL__NAME: authentik
      AUTHENTIK_POSTGRESQL__PASSWORD: ${PG_PASS}
      AUTHENTIK_SECRET_KEY: ${AUTHENTIK_SECRET_KEY:?error}
    ports:
      - "100.x.x.x:9000:9000"   # Bind to Tailscale IP only — never 0.0.0.0
      - "100.x.x.x:9443:9443"
    volumes:
      - ./media:/media
      - ./custom-templates:/templates

  worker:
    image: ghcr.io/goauthentik/server:latest
    restart: unless-stopped
    command: worker
    environment:
      AUTHENTIK_REDIS__HOST: redis
      AUTHENTIK_POSTGRESQL__HOST: postgresql
      AUTHENTIK_POSTGRESQL__USER: authentik
      AUTHENTIK_POSTGRESQL__NAME: authentik
      AUTHENTIK_POSTGRESQL__PASSWORD: ${PG_PASS}
      AUTHENTIK_SECRET_KEY: ${AUTHENTIK_SECRET_KEY}

volumes:
  database:
```

**Critical**: Replace `100.x.x.x` with your specific Tailscale IP. Never bind to `0.0.0.0`.

**MFA enforcement**: Authentik supports TOTP (time-based one-time passwords), WebAuthn/FIDO2 (hardware keys like YubiKey), and email-based verification. Enable TOTP at minimum for all admin accounts; WebAuthn for high-privilege accounts if you have a hardware key.

---

## 3. Zero Trust Architecture

### Core Principles for Home Lab

Zero trust replaces the implicit "trust everything inside the network" model with explicit, continuous verification. For a home lab:

1. **Device trust**: every device must be enrolled and known before it can access lab services
2. **Identity verification**: every access requires authentication, even from "trusted" VLANs
3. **Least privilege**: no service gets more network access than it needs for its function
4. **Assume breach**: design as if an attacker is already inside; minimize blast radius

### Tailscale as Zero Trust Network Layer

Tailscale implements zero trust at the network layer. It builds an encrypted WireGuard mesh between all devices you enroll, regardless of their physical network location. Every device has a cryptographic identity tied to your identity provider.

**Key zero trust features in Tailscale**:
- **ACLs (Access Control Lists)** define which device can reach which service on which port — by identity, not by IP
- **Device posture checks**: require devices to meet security criteria (e.g., OS up to date, disk encryption enabled) before granting access
- **MFA enforcement**: require TOTP or SSO re-authentication for sensitive access
- **Tailscale SSH**: certificate-based SSH that logs every session; eliminates the need for managing SSH keys across devices

**ACL policy example** (tailnet policy file):
```json
{
  "acls": [
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["tag:lab:22", "tag:lab:8080", "tag:lab:443"]
    },
    {
      "action": "accept",
      "src": ["tag:lab"],
      "dst": ["tag:lab:*"]
    }
  ],
  "tagOwners": {
    "tag:lab": ["group:admin"]
  },
  "ssh": [
    {
      "action": "accept",
      "src": ["group:admin"],
      "dst": ["tag:lab"],
      "users": ["pi", "root"]
    }
  ]
}
```

**Tailscale free tier** (for personal use): supports up to 3 users and 100 devices — more than sufficient for a home lab.

---

## 4. DNS Security: DoH/DoT and Filtering

### Encrypted DNS

Plain DNS (UDP port 53) exposes every domain lookup to passive surveillance and man-in-the-middle injection. DNS-over-HTTPS (DoH) and DNS-over-TLS (DoT) encrypt lookups.

**Implementation options**:

**Option A: NextDNS (Recommended for home lab)**
- Cloud-hosted, free tier: 300,000 queries/month (typically sufficient for a home lab)
- Per-device or per-network profiles with custom block lists
- Real-time analytics showing every DNS query, blocked or allowed
- DoH and DoT endpoints; can be configured on individual devices or router-wide
- Functions as a cloud Pi-hole: ad blocking, malware domain blocking, custom rules

Configuration for a Pi:
```bash
# Configure systemd-resolved to use NextDNS DoT
sudo mkdir -p /etc/systemd/resolved.conf.d/
cat << 'EOF' | sudo tee /etc/systemd/resolved.conf.d/nextdns.conf
[Resolve]
DNS=45.90.28.0#your-profile-id.dns.nextdns.io
DNSOverTLS=yes
EOF
sudo systemctl restart systemd-resolved
```

**Option B: Quad9 (Privacy-first, no account required)**
- Swiss non-profit, strict no-logging policy, subject to Swiss privacy law
- Automatic malware domain blocking via integrated threat intelligence feeds
- Free, no rate limits, no account required
- DoH: `https://dns.quad9.net/dns-query`
- DoT: `tls://dns.quad9.net`
- Best when you want automatic threat blocking without configuring anything

**Option C: AdGuard Home (Self-hosted)**
- Runs on a Pi; provides DNS filtering and ad blocking for your entire network
- More control than NextDNS, no rate limits, full privacy (no third-party DNS provider)
- Higher maintenance: you manage blocklist updates, upstream resolver configuration
- Install: `curl -s -S -L https://raw.githubusercontent.com/AdguardTeam/AdGuardHome/master/scripts/install.sh | sh -s -- -v`
- Configure to use Quad9 or NextDNS as upstream (for threat intelligence) while providing local ad blocking

**Recommendation**: NextDNS for the free tier convenience and analytics, falling back to Quad9 if NextDNS query limits are exceeded. Add AdGuard Home in Phase 4 if you want full self-hosted DNS control.

### DNSSEC

Enable DNSSEC validation wherever possible. Quad9 validates DNSSEC by default. NextDNS has a DNSSEC toggle in profile settings. This prevents DNS spoofing attacks where a compromised resolver returns falsified IP addresses for legitimate domains.

---

## 5. Home Lab Specific: Firewall Hardening

### iptables Hardening for Pi (if not using pfSense/OPNsense)

Default policy: deny all, allow only what is needed.

```bash
# Reset rules
sudo iptables -F && sudo iptables -X

# Default policies: DROP
sudo iptables -P INPUT DROP
sudo iptables -P FORWARD DROP
sudo iptables -P OUTPUT ACCEPT

# Allow established connections
sudo iptables -A INPUT -m conntrack --ctstate ESTABLISHED,RELATED -j ACCEPT

# Allow loopback
sudo iptables -A INPUT -i lo -j ACCEPT

# Allow SSH only from Tailscale interface (tailscale0)
sudo iptables -A INPUT -i tailscale0 -p tcp --dport 22 -j ACCEPT

# Allow specific application port from Lab VLAN only
sudo iptables -A INPUT -s 192.168.20.0/24 -p tcp --dport 8080 -j ACCEPT

# Log and drop everything else
sudo iptables -A INPUT -j LOG --log-prefix "DROPPED: " --log-level 4
sudo iptables -A INPUT -j DROP

# Persist rules
sudo apt install iptables-persistent
sudo netfilter-persistent save
```

**SSH hardening** (`/etc/ssh/sshd_config`):
```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
MaxAuthTries 3
ClientAliveInterval 300
ClientAliveCountMax 2
AllowUsers pi
X11Forwarding no
# Restrict to Tailscale interface only
ListenAddress 100.x.x.x  # your Tailscale IP
```

### Tailscale MFA Enforcement

Tailscale's identity-layer MFA requirement ensures that even if an attacker obtains a device's Tailscale auth key, they cannot access the tailnet without also passing the identity provider's MFA challenge.

Enable in Tailscale admin console:
1. Settings → Security → Enable "Require two-factor authentication for login"
2. Each user must have TOTP or hardware key enrolled in your identity provider (Google, Authentik, etc.)

---

## 6. Raspberry Pi-Specific Hardening Checklist

This section applies to all Pi devices running lab projects (stockbot, seedwarden).

**OS and User**:
- [ ] Raspberry Pi OS Lite (no desktop) — reduces attack surface
- [ ] Change default `pi` password or disable it; create a named user account
- [ ] Disable default `pi` account if not in use: `sudo usermod -L pi`
- [ ] Enable unattended security upgrades: `sudo apt install unattended-upgrades && sudo dpkg-reconfigure unattended-upgrades`

**Network**:
- [ ] Assign static IP via DHCP reservation on router (Pi should not change IPs)
- [ ] Disable WiFi and Bluetooth if using wired Ethernet only: `sudo rfkill block wifi && sudo rfkill block bluetooth`
- [ ] Confirm Pi is on Lab VLAN, not Trusted or IoT VLAN

**Services**:
- [ ] Disable all services not in use: `sudo systemctl list-units --type=service --state=active`
- [ ] Disable Avahi/mDNS if not needed: `sudo systemctl disable --now avahi-daemon`
- [ ] Disable Bluetooth service: `sudo systemctl disable --now bluetooth`

**Encryption and Integrity**:
- [ ] Enable AppArmor: `sudo apt install apparmor apparmor-utils && sudo aa-enforce /etc/apparmor.d/*`
- [ ] Apply sysctl hardening from PHASE_3_APT_ENDPOINT_DEFENSE.md
- [ ] Wazuh agent installed and reporting to manager

**Monitoring**:
- [ ] restic backup running nightly (confirm with `systemctl status homelab-backup.timer`)
- [ ] Wazuh FIM configured to monitor `/home/pi/`, `/etc/`, `/usr/bin/`, `/usr/sbin/`
- [ ] Log rotation configured: `sudo logrotate -d /etc/logrotate.conf`

---

## 7. Confidence Levels and Known Gaps

**High confidence**: Tailscale as the zero trust access layer is production-proven, actively maintained, and the right tool for this environment. VLAN segmentation with OPNsense/pfSense is well-documented.

**High confidence**: NextDNS free tier provides solid DNS security with minimal setup. Quad9 as a fallback is unconditionally reliable.

**Medium confidence**: Authentik SSO setup requires 2–4 hours of initial configuration and occasional maintenance (updates, OIDC client registration for each new application). The operational overhead is justified once you have 5+ services but is borderline for 2–3 services.

**Medium confidence**: The iptables rules described are correct and functional but require manual updating when new services are added. Consider migrating to `ufw` for simpler management if iptables rule complexity grows.

**Known gap**: Physical security. Zero trust and network segmentation assume logical network control. Physical access to a Pi (USB boot, JTAG) bypasses all software controls. Mitigation: lock down boot order in Pi firmware to prevent USB boot; place Pi hardware in a locked enclosure if physical security is a concern.

**Known gap**: IPv6. The firewall rules above are IPv4-only. If your ISP provides IPv6, ensure firewall rules explicitly cover IPv6 traffic (`ip6tables` rules or a combined `nftables` ruleset). Unfiltered IPv6 can create bypass paths around IPv4 firewall rules.

---

## Sources

- [Tailscale Zero Trust Networking](https://tailscale.com/use-cases/zero-trust-networking)
- [Tailscale Zero Trust Definition](https://tailscale.com/docs/concepts/zero-trust)
- [How to Use Tailscale for Zero-Trust Networking (2026)](https://oneuptime.com/blog/post/2026-01-27-tailscale-zero-trust-networking/view)
- [Homelab Network Security: 7 Zero-Trust Steps (2026)](https://readthemanual.co.uk/secure-your-homelab-2025/)
- [5 Secure Networking Projects for Your Home Lab](https://www.virtualizationhowto.com/2025/08/5-secure-networking-projects-for-your-home-lab-this-weekend/)
- [Best Encrypted DNS — Quad9 vs NextDNS vs Cloudflare (May 2026)](https://stateofsurveillance.org/guides/technical/encrypted-dns-comparison/)
- [NextDNS vs Cloudflare vs Quad9 Comparison](https://factually.co/product-reviews/electronics-tech/nextdns-vs-cloudflare-vs-quad9-best-public-doh-dot-resolvers-2026-73bc72)
- [Linux Server Hardening Steps and Best Practices](https://www.zenarmor.com/docs/linux-tutorials/linux-server-hardening-steps-and-best-practices)
- [Linux Security: Firewall, SELinux, AppArmor (April 2026)](https://dasroot.net/posts/2026/04/linux-security-firewall-selinux-apparmor/)
- [Tailscale Home Lab Remote Access](https://medium.com/@Techdad11207/remote-access-to-your-cisco-homelab-with-tailscale-subnet-routing-a3749d66dc76)
