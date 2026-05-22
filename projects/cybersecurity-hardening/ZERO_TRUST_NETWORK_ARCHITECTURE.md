---
title: "Zero-Trust Network Architecture — Tailscale + Authentik Implementation"
created: "2026-05-23"
status: "PRODUCTION-READY — Phase 3 infrastructure security"
scope: "Zero-trust mesh network design, identity layer, device posture, segmentation"
deadline: "June 1, 2026"
owner: "Cybersecurity-Hardening Infrastructure Planning"
---

# Zero-Trust Network Architecture

*Created May 23, 2026. Zero-trust is the modern security paradigm: no user or device is trusted by default. Every access request is authenticated, authorized, and encrypted — regardless of whether you're inside or outside the corporate network. For distributed Phase 3 teams, zero-trust replaces VPN with mesh networking.*

---

## Part 1: Zero-Trust Principles

### 1.1 Traditional VPN (Bad for Distributed Teams)

```
VPN → Corporate Network → Internal Services
  Problem: If attacker compromises one device, they're "inside" and can access everything
```

### 1.2 Zero-Trust Model (Good for Distributed Teams)

```
Device → Authentication (Who are you?)
       → Device Posture Check (Is your device secure?)
       → Encryption (Encrypt all traffic)
       → Authorization (What can you access?)
       → Logging (Who accessed what, when?)
```

**Key difference**: Trust is NOT based on network location (inside vs outside). Trust is based on:
1. **Identity**: Who are you? (Verified by Authentik)
2. **Device health**: Is your device patched, encrypted, compliant? (Verified by osquery)
3. **Context**: Where are you, when, from what network? (Verified by Tailscale)
4. **Access policy**: What specific resource are you accessing? (Verified by Authentik)

---

## Part 2: Tailscale — Zero-Trust Mesh VPN

### 2.1 What is Tailscale?

Tailscale is a **managed mesh VPN** that creates a private network among devices.

```
Device A          Device B          Device C
(laptop)         (desktop)         (server)
    ↓                ↓                  ↓
[Tailscale client] [Tailscale client] [Tailscale client]
    ↓                ↓                  ↓
    └────────────────┴──────────────────┘
         [100.x.x.x private network]
```

**Key features**:
- Each device gets a private IP (100.x.x.x/32)
- All traffic encrypted (WireGuard protocol)
- No central server (peer-to-peer, except for key exchange)
- Works through firewalls/NAT (no port forwarding needed)
- Magic DNS (devices known by hostname, not IP)

### 2.2 Setup for Distributed Team

**1. Create Tailscale account** (free tier available):
```bash
# Go to https://tailscale.com/
# Sign up with OAuth (Google, GitHub, etc.)
# Or enterprise setup (for large teams)
```

**2. Install client on each device** (Linux, macOS, Windows):
```bash
# macOS
brew install tailscale

# Linux
curl -fsSL https://tailscale.com/install.sh | sh

# Windows
choco install tailscale
```

**3. Authenticate device**:
```bash
sudo tailscale up

# Opens browser → confirm device → granted access to Tailscale network
# Device now has private IP, e.g., 100.120.18.84
```

**4. Create DNS entries** (hostname-based access):
In Tailscale admin console: `<hostname>.0x1234.ts.net` → auto-resolved by Tailscale

**Result**: Devices can ping each other by IP or hostname (all encrypted, no firewall rules needed)

### 2.3 Advanced Tailscale Features

**VPN Exit Node** (route all traffic through Tailscale server):
- Useful for distributed teams to appear as single IP
- Protects against ISP surveillance
- Setup: One device as exit node; others configured to route through it

**Subnet Routers** (connect entire office subnet):
- Replaces traditional VPN gateway
- One device in office runs `tailscale up --advertise-routes=10.0.0.0/24`
- Other devices access office services without individual installation

**Tailscale ACLs** (access control lists):
```hcl
// Only allow laptop to SSH to server
{
  "acls": [
    {
      "action": "accept",
      "src": ["tag:laptops"],
      "dst": ["tag:servers:22"]
    }
  ],
  "tagOwners": {
    "tag:laptops": ["anya@example.com"],
    "tag:servers": ["anya@example.com"]
  }
}
```

**MFA for Device Approval**:
- Require TOTP to authenticate new device
- Or use email approval (new device requires email confirmation)

---

## Part 3: Authentik — Identity & Access Management (IAM)

### 3.1 What is Authentik?

Authentik is an **open-source identity provider** (like Okta/Azure AD, but free + self-hosted).

**Architecture**:
```
[User] → [Login Portal] → [Authentik Server] → [Verify Password + MFA]
                                  ↓
                          [Check device posture]
                                  ↓
                          [Check device geolocation]
                                  ↓
                          [Grant/Deny access]
```

### 3.2 Setup Authentik

**Installation** (Docker):
```bash
docker pull ghcr.io/goauthentik/server:latest
docker run -d \
  -p 9000:9000 \
  -p 9443:9443 \
  --name authentik \
  -e AUTHENTIK_SECRET_KEY=$(openssl rand -base64 32) \
  -e AUTHENTIK_POSTGRESQL__PASSWORD=$(openssl rand -base64 32) \
  ghcr.io/goauthentik/server:latest
```

**Access admin console**: https://localhost:9443 (default user: akadmin)

### 3.3 Configure OIDC (OpenID Connect)

Connect Tailscale to Authentik for identity-aware access control:

```bash
# In Authentik, create OIDC provider:
# 1. Applications → Create
# 2. Name: tailscale
# 3. Type: OpenID Connect (OIDC)
# 4. Client ID: [auto-generated]
# 5. Client Secret: [auto-generated]
# 6. Redirect URI: https://login.tailscale.com/oidc/callback
```

**Enable device flow authentication**:
- When user runs `tailscale up`, redirects to Authentik login
- User authenticates (password + TOTP MFA)
- Device posture check: Is device encrypted? Is OS updated?
- If all pass: Device granted Tailscale access
- If fail: Device denied (force compliance)

---

## Part 4: Device Posture Checking

### 4.1 What is Device Posture?

Device posture = whether a device is secure + compliant

**Checks performed** (via osquery):
```
✓ Is disk encrypted? (LUKS on Linux, FileVault on macOS, BitLocker on Windows)
✓ Is OS up-to-date? (run `apt upgrade`, `brew update`, Windows Update)
✓ Is antivirus running? (allow Defender on Windows)
✓ Is firewall enabled? (ufw on Linux, pfctl on macOS)
✓ Is screen lock enabled? (automatic sleep + password on unlock)
✓ Are no USB devices plugged in? (block USB except keyboard/mouse)
✓ Is full-disk encryption key in TPM? (Linux/Windows)
```

### 4.2 Implement Device Posture Checks

**In Authentik**, create conditional access policy:
```
IF user attempts to login
  THEN check device posture
  IF device posture = compliant
    THEN grant access
  ELSE
    THEN require remediation OR deny access
```

**Remediation flow** (user-friendly):
1. Device fails posture check
2. Authentik shows message: "Your device must enable FileVault before accessing"
3. User runs system settings → enables FileVault
4. Retries login → posture check passes
5. Access granted

**Enforcement levels**:
- **Audit-only**: Log failures, allow access (for non-critical teams)
- **Warn-only**: Notify user, allow access (for testing)
- **Block**: Deny access until compliant (for sensitive work)

---

## Part 5: Network Segmentation

### 5.1 Segmentation by Role

Not all devices need access to all services. Create zones:

```
ZONE 1: Laptops (user devices)
  ├─ Can access: Email, docs, Slack, public APIs
  └─ Cannot access: Database servers, private keys, infrastructure

ZONE 2: Servers (data processing)
  ├─ Can access: Database, file storage, internal APIs
  └─ Cannot access: Internet (except specific outbound IPs)

ZONE 3: Infrastructure (admins only)
  ├─ Can access: Kubernetes, deployment tools, monitoring
  └─ Restricted to 2 admin devices + MFA
```

### 5.2 Tailscale ACLs per Zone

```hcl
{
  "acls": [
    // Laptops can SSH to servers, but not vice versa
    {
      "action": "accept",
      "src": ["tag:laptops"],
      "dst": ["tag:servers:22,443"]
    },
    // Servers cannot initiate connections to laptops
    {
      "action": "deny",
      "src": ["tag:servers"],
      "dst": ["tag:laptops"]
    },
    // Infrastructure admins can access everything
    {
      "action": "accept",
      "src": ["tag:admins"],
      "dst": ["*"]
    },
    // Everyone else: nothing by default
    {
      "action": "deny",
      "src": ["*"],
      "dst": ["*"]
    }
  ],
  "tagOwners": {
    "tag:laptops": ["anya@example.com"],
    "tag:servers": ["sys-admin@example.com"],
    "tag:admins": ["anya@example.com"]
  }
}
```

---

## Part 6: Deployment Checklist

| Component | Setup | Verify |
|---|---|---|
| **Tailscale** | Install on all devices; authenticate | `tailscale status` shows all devices |
| **Authentik** | Deploy Docker container | https://localhost:9443 accessible |
| **OIDC Provider** | Create in Authentik | Client ID + Secret in config |
| **Device Posture** | Configure osquery + Authentik checks | Device fails posture → remediation required |
| **ACLs** | Define role-based zones | Test: laptop cannot SSH to admin server |
| **MFA** | Enable TOTP for Authentik | Login requires TOTP code |
| **Monitoring** | Wazuh monitors Authentik logs | Failed login attempts logged |

---

## Part 7: Testing Zero-Trust Network

### 7.1 Positive Test Cases

```
✓ Authenticated user on compliant device → Access granted
✓ User accesses Tailscale service → Encrypted tunnel established
✓ Device posture fails → User prompted to remediate
✓ User remediates → Re-authentication succeeds
```

### 7.2 Security Test Cases

```
✓ Compromised device (no disk encryption) → Access denied
✓ Device on untrusted network (VPN detected) → Warn user or deny
✓ Expired MFA token → Force re-authentication
✓ Device tries to access unauthorized service (per ACL) → Connection refused
```

### 7.3 Load Testing

```
✓ 100 devices authenticating simultaneously → no slowdown
✓ Continual OIDC token refresh → no connection drops
✓ Device posture check on all 100 devices → completes <2 sec
```

---

## Part 8: Maintenance & Monitoring

**Daily**:
- Monitor Wazuh for authentication failures (Authentik logs)
- Check Tailscale status: all devices online
- Verify device posture pass rate (target: >95%)

**Weekly**:
- Review ACL changes (who got new permissions?)
- Check for device removals (employees leaving?)
- Audit failed login attempts (brute force attempts?)

**Monthly**:
- Review OIDC token expiration policy (is 90 days right?)
- Check for stale devices (devices not seen in 30+ days)
- Audit administrator role assignments (who has admin access?)

---

## Part 9: Comparison: Zero-Trust vs Traditional VPN

| Aspect | Traditional VPN | Zero-Trust (Tailscale + Authentik) |
|---|---|---|
| **Setup** | Complex (requires admin) | Simple (`tailscale up`) |
| **Trust Model** | Trust if inside network | Trust based on identity + device |
| **Encryption** | Tunnel-level only | Per-connection + per-service |
| **Access Control** | IP-based (crude) | Identity + device posture + context |
| **Scalability** | Gateway bottleneck | Peer-to-peer (scales to 1000s) |
| **Cost** | Enterprise: $$$$ | Open-source: $0 |
| **Maintenance** | High (VPN server mgmt) | Low (cloud-based) |
| **User Experience** | "Connect to VPN → access everything" | "Login → posture check → access specific service" |

---

**Document Status**: PRODUCTION-READY  
**Next Deliverable**: THREAT_MONITORING_DASHBOARD_SPEC.md (real-time visibility)  
**Owner**: Cybersecurity-Hardening Infrastructure Planning  
**Deadline**: June 1, 2026

