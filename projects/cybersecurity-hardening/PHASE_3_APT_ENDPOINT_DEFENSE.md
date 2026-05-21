---
title: "Phase 3 APT Endpoint Defense"
project: cybersecurity-hardening
phase: 3
status: research-complete
created: 2026-05-21
target-execution: June–July 2026
confidence: high
---

# Phase 3: APT Endpoint Defense

**Most critical finding**: APT-level threats against home labs and small operations are no longer hypothetical. State-affiliated actors actively target personal infrastructure to stage lateral movement into employer networks, exfiltrate cryptocurrency wallets, and recruit compromised machines into botnets. The defining characteristic of APT intrusions is dwell time — adversaries persist for weeks or months before acting. Budget EDR with Wazuh + osquery provides detection coverage that closes the most common dwell-time vectors without enterprise spending.

---

## 1. Kernel-Level Protections

### Linux: AppArmor vs. SELinux

Both are Mandatory Access Control (MAC) frameworks that confine processes beyond standard Unix DAC (discretionary access control). The difference is enforcement model and complexity.

**AppArmor** (path-based, profile-driven):
- Default on Ubuntu, Debian, Raspberry Pi OS
- Confines specific applications by defining profiles listing allowed file paths and permissions
- Lower operational overhead: profiles are human-readable and there are community-maintained profiles for common applications
- When a process violates its profile, AppArmor can either log the violation (complain mode) or block it (enforce mode)
- **Use for**: Raspberry Pi 5 (stockbot, seedwarden), Ubuntu servers, any system where you want incremental hardening without restructuring the entire system

```bash
# Check AppArmor status
sudo aa-status

# Install additional profiles
sudo apt install apparmor-profiles apparmor-profiles-extra

# Put a profile in enforce mode
sudo aa-enforce /etc/apparmor.d/usr.bin.python3

# Audit violations
sudo journalctl -f | grep apparmor
```

**SELinux** (label-based, policy-driven):
- Default on RHEL, Fedora, CentOS Stream
- Every file, process, port, and socket receives a security label; policy defines which label contexts can interact
- Substantially harder to administer: initial learning curve of 20–40 hours to write custom policies competently
- Significantly stronger isolation: a compromised process cannot escape its label context even if it achieves root
- **Use for**: Any system where compliance requirements demand SELinux (HIPAA, PCI-DSS), or when you have dedicated time to manage it properly

**Recommendation for home lab**: AppArmor on all Raspberry Pi and Ubuntu systems. The operational overhead of SELinux at home-lab scale is not justified against the marginal security improvement.

### Additional Kernel Hardening (sysctl)

Add to `/etc/sysctl.d/99-hardening.conf`:

```ini
# Disable kernel pointer exposure in /proc
kernel.kptr_restrict = 2

# Restrict dmesg to root
kernel.dmesg_restrict = 1

# Disable core dumps
fs.suid_dumpable = 0

# Enable ASLR (Address Space Layout Randomization)
kernel.randomize_va_space = 2

# Disable IP forwarding (unless acting as router)
net.ipv4.ip_forward = 0

# Prevent SYN flood attacks
net.ipv4.tcp_syncookies = 1

# Ignore ICMP redirects (prevent routing table poisoning)
net.ipv4.conf.all.accept_redirects = 0
net.ipv6.conf.all.accept_redirects = 0
```

Apply with: `sudo sysctl -p /etc/sysctl.d/99-hardening.conf`

### Windows: Windows Defender + WDAC

**Windows Defender** (built-in, free) provides real-time protection, cloud-delivered signatures, and behavioral monitoring. Key hardening steps:

1. Enable cloud-delivered protection and automatic sample submission
2. Enable tamper protection (prevents malware from disabling Defender)
3. Enable Attack Surface Reduction (ASR) rules — blocks common initial-access techniques:
   ```powershell
   # Block Office apps from creating child processes
   Set-MpPreference -AttackSurfaceReductionRules_Ids D4F940AB-401B-4EFC-AADC-AD5F3C50688A -AttackSurfaceReductionRules_Actions Enabled
   # Block credential stealing from LSASS
   Set-MpPreference -AttackSurfaceReductionRules_Ids 9E6C4E1F-7D60-472F-BA1A-A39EF669E4B2 -AttackSurfaceReductionRules_Actions Enabled
   ```

**Windows Defender Application Control (WDAC)**:
- Allows only explicitly approved applications to run (allowlisting)
- Significantly raises the bar for persistence: attackers cannot simply drop and execute new binaries
- Configured via XML policy files, deployed via Group Policy or Intune
- Start in audit mode, review logs for 2–4 weeks, then switch to enforcement
- Free, built-in on Windows 10/11 Pro and Enterprise

---

## 2. Behavioral Detection: EDR on a Budget

### Wazuh (Free, Self-Hosted)

Wazuh is an open-source unified XDR and SIEM platform. It covers: real-time log analysis, file integrity monitoring (FIM), vulnerability detection, and incident correlation. The architecture is manager + agent: the manager runs on a server (or VM), agents run on each endpoint.

**What Wazuh detects**:
- File integrity changes (modified binaries, new cron jobs, altered SSH configs)
- Log-based threat detection using built-in rule sets (based on MITRE ATT&CK)
- Rootkit detection via Rootcheck module
- Vulnerability inventory by cross-referencing installed packages against NVD/CVE databases
- Active response: can automatically block IPs triggering brute-force patterns

**Deployment for home lab** (Wazuh manager on a dedicated Pi or VM):
```bash
# Install Wazuh manager (on Ubuntu 22.04 / Debian 12)
curl -sO https://packages.wazuh.com/4.x/wazuh-install.sh
sudo bash wazuh-install.sh -a

# Agent installation on monitored endpoints (Pi, Windows, Linux)
# Linux agent:
curl -sO https://packages.wazuh.com/4.x/wazuh-agent.deb
sudo WAZUH_MANAGER="<manager-ip>" dpkg -i wazuh-agent.deb
sudo systemctl start wazuh-agent
```

Bind the Wazuh manager API to `127.0.0.1` or the Tailscale IP — never to `0.0.0.0` per absolute project security rules.

### osquery Integration with Wazuh

osquery exposes the operating system as a relational database: you write SQL queries against running processes, network connections, loaded modules, user accounts, and more. Wazuh has a native module to collect osquery output and generate alerts.

**High-value osquery queries for home lab**:
```sql
-- Detect new listening ports
SELECT pid, address, port, protocol FROM listening_ports WHERE port NOT IN (22, 80, 443, 8080);

-- Find processes with unexpected network connections
SELECT p.name, p.pid, c.remote_address, c.remote_port
FROM process_open_sockets c JOIN processes p USING(pid)
WHERE c.remote_address NOT IN ('0.0.0.0', '::', '127.0.0.1');

-- Detect new cron jobs (common persistence mechanism)
SELECT command, path, minute, hour FROM crontab;

-- Find SUID/SGID binaries not in baseline
SELECT path, permissions FROM file
WHERE (permissions LIKE '%s%' OR permissions LIKE '%S%')
AND path NOT IN ('/usr/bin/sudo', '/usr/bin/passwd');
```

Add to Wazuh's `ossec.conf`:
```xml
<wodle name="osquery">
  <disabled>no</disabled>
  <run_daemon>yes</run_daemon>
  <log_path>/var/log/osquery/osqueryd.results.log</log_path>
  <add_labels>yes</add_labels>
</wodle>
```

---

## 3. Threat Intelligence Integration

### Free IOC Feeds

**AlienVault OTX (Open Threat Exchange)** — Free account gives access to community-shared IOC pulses (malicious IPs, domains, file hashes). Wazuh can integrate directly:
```bash
# Wazuh OTX integration (via Python script)
pip install OTXv2
python /var/ossec/integrations/otx.py
```

**Abuse.ch Feeds** (no account required):
- URLhaus: malicious URLs used for malware distribution
- Feodo Tracker: botnet C2 infrastructure IPs
- SSL Blacklist: malicious certificates
- Export in various formats; can be loaded into Suricata or pfSense as block lists

**CISA KEV (Known Exploited Vulnerabilities)** — Publicly available JSON feed of CVEs with confirmed active exploitation. Cross-reference against your Wazuh vulnerability inventory:
```bash
curl -s https://www.cisa.gov/sites/default/files/feeds/known_exploited_vulnerabilities.json | jq '.vulnerabilities[].cveID'
```

### MISP for Structured Threat Intel (Optional, Advanced)

MISP (Malware Information Sharing Platform) is a self-hosted platform for structured threat intelligence. It is a significant operational investment for a home lab (running on a VM, maintaining feeds). Defer MISP deployment until Phase 4 unless you have a specific use case requiring structured IOC correlation. For Phase 3, AlienVault OTX + Abuse.ch feeds provide sufficient threat intelligence integration with Wazuh at manageable overhead.

---

## 4. Incident Response Playbook

This playbook follows NIST SP 800-61 Rev. 3 (released April 2025, aligned with CSF 2.0).

### Phase 1: Detection

**Sources that indicate compromise**:
- Wazuh alert: file integrity change on `/etc/crontab`, `/etc/passwd`, or any binary in `/usr/bin`
- Wazuh alert: new listening port on an unexpected address
- osquery: process with outbound connection to a known-bad IP (from Abuse.ch feed)
- Authentication logs: multiple failed SSH attempts followed by success from new IP
- AppArmor: enforced profile violation generating DENIED logs

**Triage checklist**:
1. Is this a true positive or a known benign change? (Check change log, recent deployments)
2. What is the affected system? (Name, IP, role in home lab)
3. What is the blast radius if this system is fully compromised? (Does it have access to Tailscale? Backups? Other systems?)
4. What is the earliest evidence of the anomaly? (Check Wazuh logs for the 72 hours prior)

### Phase 2: Containment

**Immediate actions (within 15 minutes of confirmed incident)**:
1. Isolate the affected system from the network: remove Tailscale node, disconnect from switch/WiFi
2. Snapshot the system state if virtualized (preserve evidence)
3. Do NOT reboot — rebooting may destroy volatile evidence (running processes, in-memory IOCs)
4. Preserve logs: copy `/var/log/` and Wazuh agent logs to a separate system before any remediation

**Short-term containment**:
- Block the attacker's IP at the firewall/router (iptables, pf, or router ACL)
- Rotate all credentials that the compromised system had access to: SSH keys, API tokens, Tailscale auth keys, any credentials stored in environment variables or config files

### Phase 3: Eradication

1. Identify the initial access vector (phishing link, exploited service, compromised dependency)
2. Confirm the full scope: check all systems the compromised host had network access to
3. Remove the malware/backdoor — do not attempt to clean a rootkit in place; reinstall the OS
4. Patch the exploited vulnerability before bringing any system back online

### Phase 4: Recovery

1. Restore from a known-good backup (see PHASE_3_RANSOMWARE_RECOVERY_PLAN.md for procedure)
2. Verify backup integrity with hash comparison before restoring
3. Bring systems back online one at a time, monitoring Wazuh for reinfection indicators
4. Re-enable Tailscale connectivity only after confirming clean state

### Phase 5: Post-Incident

1. Document timeline, initial vector, lateral movement path, and dwell time
2. Update Wazuh rules to detect the specific TTPs used
3. Assess whether any data was exfiltrated (review outbound network logs for the dwell period)
4. Report to relevant parties if breach involved others' data (email contacts, etc.)

---

## 5. Practical Scope for Home Environment

### Priority Order for Deployment

1. **Wazuh manager + agents** — highest ROI, covers all active Pi systems and Windows machine
2. **AppArmor enforcement** on stockbot and seedwarden — protects against supply chain compromises post-deployment
3. **sysctl hardening** on all Linux systems — 15-minute implementation, significant reduction in kernel exploit surface
4. **Windows Defender ASR rules** — protects the Windows machine against the most common initial-access techniques
5. **Abuse.ch feed integration** into router/firewall — blocks known-bad infrastructure at network level

### Confidence Levels and Known Gaps

**High confidence**: Wazuh is production-ready for home lab use. AppArmor profiles for common applications are well-maintained. sysctl hardening is well-documented and low risk.

**Medium confidence**: osquery SQL rules for anomaly detection require tuning to reduce false positives in home lab context (expected legitimate processes will trigger initial alerts). Plan 2–3 hours of tuning after initial deployment.

**Known gap**: Memory forensics. APT-grade attackers using fileless malware (loading payloads entirely in memory, never writing to disk) will evade file integrity monitoring. Wazuh + osquery will catch indicators of compromise in network connections and process behavior, but not the payload itself. This gap is acceptable for home lab threat models; closing it requires commercial EDR (CrowdStrike, SentinelOne) at $50–150/endpoint/year.

**Known gap**: macOS coverage. If any macOS devices are on the Tailscale network, their coverage with Wazuh is weaker than Linux or Windows. Consider Wazuh agent on macOS plus enabling built-in System Integrity Protection (SIP) and Gatekeeper enforcement.

---

## Sources

- [Wazuh EDR for Home Lab — Setup Guide](https://medium.com/@rishavkumarthapa/day-26-setting-up-wazuh-for-endpoint-detection-and-response-edr-a-beginners-guide-4277d4707052)
- [Open-Source EDR Solutions Overview](https://www.packetlabs.net/posts/open-source-edr-solutions/)
- [Wazuh Home Lab Implementation](https://judelanning.com/posts/open-source-edr-with-wazuh/)
- [Linux Hardening — Kernel Security 2026](https://blog.aicademy.ac/hardening-linux-kernel-security-2026)
- [AppArmor vs SELinux Comparison](https://tuxcare.com/blog/selinux-vs-apparmor/)
- [SELinux and AppArmor — Beyond Basic Security](https://www.veeble.com/blog/selinux-and-apparmor-hardening-linux-servers-beyond-basic-security/)
- [Linux Server Hardening Best Practices](https://linuxsecurity.com/features/linux-server-practical-hardening-guide)
- [MISP Threat Intelligence Platform](https://www.misp-project.org/)
- [Open Source Threat Intel Feeds](https://github.com/Bert-JanP/Open-Source-Threat-Intel-Feeds)
- [MISP vs OpenCTI 2025 Guide](https://www.cosive.com/misp-vs-opencti)
- [NIST SP 800-61 Rev. 3 — Incident Response](https://csrc.nist.gov/pubs/sp/800/61/r3/final)
- [NIST 800-61 Rev. 3 Framework Analysis](https://linfordco.com/blog/nist-sp-800-61/)
