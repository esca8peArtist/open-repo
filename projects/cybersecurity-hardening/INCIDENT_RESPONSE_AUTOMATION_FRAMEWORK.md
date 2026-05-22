---
title: "Incident Response Automation Framework — SOAR + Wazuh/osquery Integration"
created: "2026-05-23"
status: "PRODUCTION-READY — Phase 3 infrastructure security"
scope: "Automation-first incident response playbooks, SOAR integration, alerting architecture, escalation paths"
deadline: "June 1, 2026"
owner: "Cybersecurity-Hardening Infrastructure Planning"
---

# Incident Response Automation Framework

*Created May 23, 2026. This document designs automated incident response infrastructure for distributed team operations running Phase 3 curriculum and capability distribution. Automation is critical because manual incident response during high-profile distribution (August-December 2026) would overload human operators. This architecture enables 24/7 threat detection + response with minimal human intervention.*

---

## Part 1: Architecture Overview

### 1.1 Three-Layer Incident Response

```
[Endpoint Detection]  [Log Aggregation]  [SOAR Orchestration]  [Escalation]
    ↓                      ↓                    ↓                    ↓
osquery agents    →  Wazuh server      →  SOAR playbooks    →  Slack/Email
(local monitoring)  (centralized logs)  (automated response)   (human decision)
```

**Detection Layer** (osquery):
- File integrity monitoring (FIM) — detects unauthorized code changes
- Process monitoring — detects anomalous process execution
- Network connection tracking — detects unexpected outbound connections
- System calls auditing — detects privilege escalation attempts

**Aggregation Layer** (Wazuh):
- Centralized log collection from all endpoints
- Correlation engine — detects multi-step attack patterns
- Alerting — triggers when suspicious patterns detected

**Orchestration Layer** (SOAR playbook):
- Automated containment (isolate compromised endpoint, block user session, etc.)
- Threat intelligence lookup — cross-check against known malware signatures
- Automated remediation — apply patches, revoke credentials, etc.

**Escalation Layer** (Human decision):
- Critical/suspicious alerts → Slack notification + decision required
- Routine violations → auto-remediated with notification
- False positives → suppressed after 3 occurrences

---

### 1.2 Response Time Targets

| Threat Level | Detection Time | Containment Time | Escalation |
|---|---|---|---|
| **Critical** (active attack) | <5 min | <10 min (auto-isolate) | Immediate Slack + call |
| **High** (breach indicator) | <15 min | <30 min (auto-disable account) | 5-min Slack |
| **Medium** (policy violation) | <1 hour | Auto-remediate + log | Daily summary |
| **Low** (info only) | <24 hours | Log only | Monthly review |

---

## Part 2: Wazuh + osquery Deployment Architecture

### 2.1 Wazuh Server (Central)

**Installation** (Ubuntu 20.04 LTS or later):

```bash
# Add Wazuh repo
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | apt-key add -
echo "deb https://packages.wazuh.com/4.x/apt/ stable main" | tee /etc/apt/sources.list.d/wazuh.list
apt-get update

# Install Wazuh manager
apt-get install wazuh-manager

# Install Elasticsearch + Kibana (for visualization)
apt-get install elasticsearch kibana

# Start services
systemctl start wazuh-manager
systemctl start elasticsearch
systemctl start kibana

# Verify
curl http://localhost:9200/ (Elasticsearch health)
wazuh-control status (Wazuh manager status)
```

**Firewall Rules** (critical):
- Wazuh agent communication: UDP 514 (agent→manager, encrypted)
- Elasticsearch: TCP 9200 (internal only, 127.0.0.1)
- Kibana: TCP 5601 (internal only, 127.0.0.1 or Tailscale network)

**High Availability** (Phase 3 distributed teams):
- Deploy 2 Wazuh managers (primary + secondary)
- Use virtual IP (keepalived) for failover
- Replicated Elasticsearch cluster (3+ nodes)
- Critical for 24/7 operation during distribution campaign

---

### 2.2 osquery Agent (Endpoints)

**Installation on Linux**:

```bash
# Add osquery repo
curl -L https://pkg.osquery.io/linux/osquery.key | apt-key add -
echo "deb [arch=amd64] https://pkg.osquery.io/linux/deb deb main" | sudo tee /etc/apt/sources.list.d/osquery.list
apt-get update

# Install osquery
apt-get install osquery

# Configure osquery to send logs to Wazuh (in /etc/osquery/osquery.conf):
{
  "options": {
    "config_plugin": "filesystem",
    "logger_plugin": "filesystem",
    "distributed_plugin": "tls",
    "disable_logging": false
  },
  "packs": {
    "security": "/etc/osquery/packs/security.conf"
  }
}
```

**macOS Installation**:

```bash
# Install via Homebrew
brew install osquery

# Or download .pkg from https://osquery.io/downloads

# Configuration same as Linux
```

**Windows Installation** (Wazuh native agent, not osquery):
- Use WinLogBeat + Windows Event Log forwarding instead
- Send to Wazuh via port 514
- Monitor: Windows Defender alerts, failed logins, privilege escalation attempts

---

### 2.3 Wazuh Agent Integration

**Deploy Wazuh agent on all endpoints** (Linux, macOS, Windows):

```bash
# Linux
curl -s https://packages.wazuh.com/4.x/apt/pool/main/w/wazuh-agent/wazuh-agent_4.x.x-1_amd64.deb | dpkg -i -

# macOS
curl -s https://packages.wazuh.com/4.x/osx/wazuh-agent-4.x.x-1.osx.pkg | installer -pkg - -target /

# Windows (PowerShell, run as admin)
Invoke-WebRequest -Uri https://packages.wazuh.com/4.x/windows/wazuh-agent-4.x.x-1.msi -OutFile wazuh-agent.msi
msiexec.exe /i wazuh-agent.msi /q WAZUH_MANAGER=<MANAGER_IP> WAZUH_REGISTRATION_SERVER=<MANAGER_IP> WAZUH_AGENT_GROUP=prod

# Start agent
systemctl start wazuh-agent (Linux)
launchctl start com.wazuh.agent (macOS)
net start WazuhSvc (Windows)
```

**Monitoring Scope** (per agent):
- Log aggregation: /var/log/*.log, /var/log/auth.log, SSH logs, etc.
- File integrity: /etc/passwd, /etc/shadow, SSH config, sudoers file, app config files
- Process monitoring: suspicious process spawning, privilege escalation attempts
- Network monitoring: inbound/outbound connections (via netstat/ss)
- System auditing: systemd service changes, cron job modifications, user account changes

---

## Part 3: SOAR Playbook Architecture

**SOAR = Security Orchestration, Automation & Response**

A SOAR platform (open-source: Shuffle, TheHive; commercial: Splunk Phantom, Cortex XSOAR) automates incident response workflows.

### 3.1 Sample SOAR Playbook: Suspicious Process Execution

**Trigger**: Wazuh detects process matching rule "parent process not in whitelist"

**Automated Workflow**:

```
1. ALERT RECEIVED: process=curl, parent=bash, user=ubuntu, IP=192.168.1.5
   ↓
2. THREAT INTELLIGENCE LOOKUP:
   - Check VirusTotal: curl binary hash clean? Y→continue, N→escalate CRITICAL
   - Check abuse.ch: command-line matching known malware? N
   - Check OSINT database: ubuntu user known good? Y
   ↓
3. CONTEXT ENRICHMENT:
   - Whois IP: internal Tailscale → known good, suppress alert
   - Whois IP: external → escalate to HIGH
   ↓
4. IF EXTERNAL + SUSPICIOUS:
   - Isolate endpoint: revoke Tailscale access (temporary)
   - Disable user session: kill SSH sessions for ubuntu user
   - Preserve evidence: copy /var/log to secure storage
   - Notify: Slack #security "Suspicious process on ubuntu@ip-192-168-1-5, auto-isolated"
   ↓
5. HUMAN DECISION:
   - Security team reviews context in Slack
   - Approve remediation (revocation permanent) or restore (false positive)
   - Document in incident log
```

### 3.2 Playbook Library (Pre-Staged)

| Playbook Name | Trigger | Auto-Action | Escalation |
|---|---|---|---|
| **Brute Force SSH** | >5 failed logins in 5 min | Rate-limit IP (UFW) | If external IP: disable account |
| **Privilege Escalation** | Unexpected `sudo` without tty | Check audit trail; if suspicious: disable account | Auto-disable + Slack |
| **Malware Detection** | VirusTotal hit on binary | Quarantine file; isolate endpoint | Immediate Slack #security |
| **Credential Stuffing** | >10 auth attempts (known weak pass) | Lock account; reset password | Slack + email user |
| **Data Exfiltration** | Large file transfer (>1GB outbound) | Block transfer; review file type | If code/config: critical escalation |
| **Unauthorized SSH Key** | New public key in authorized_keys | Log modification details; add to monitoring | Alert + review |
| **Policy Violation** | Unencrypted text file with PII | Quarantine file; encrypt with LUKS | Daily summary email |
| **Supply Chain Check** | Package installation from untrusted source | Quarantine; check GPG signature | Auto-rollback + alert |

### 3.3 False Positive Suppression

**Problem**: Too many alerts = alert fatigue = humans ignore alerts

**Solution**: Auto-suppress after 3 identical occurrences within 24 hours
- Count identical alerts
- If count = 3 on day D, suppress alert from D+1 to D+7
- Requires human re-approval to extend suppression past 7 days
- Example: "curl from ubuntu user, external IP" triggers 3 times → suppress 7 days, notify team

**Whitelist Management**:
- Maintain approved_processes.conf (whitelisted process names, parents)
- Maintain approved_ips.conf (whitelisted external IPs)
- Maintain approved_users.conf (service accounts with elevated privs)
- Quarterly review: ensure whitelists are still valid

---

## Part 4: Alerting Rules (Wazuh Configuration)

### 4.1 Critical Alerts (Auto-Escalate + Isolate)

**SSH Brute Force Attempt**:
```xml
<rule id="100100" level="12">
  <if_sid>5710</if_sid>
  <frequency>5</frequency>
  <timeframe>300</timeframe>
  <description>Multiple SSH login failures from $srcip</description>
  <group>authentication_failures</group>
</rule>
```
*Trigger: 5+ failed SSH attempts in 5 minutes → Level 12 (critical) → auto-isolate IP with UFW rule*

**Privilege Escalation Attempt**:
```xml
<rule id="100200" level="12">
  <if_sid>5403</if_sid>
  <status>failed</status>
  <description>Sudo attempt failed: $user attempting unauthorized sudo</description>
  <group>privilege_escalation</group>
</rule>
```
*Trigger: Failed sudo attempt by non-whitelisted user → Level 12 → disable account*

**File Integrity Violation** (config files):
```xml
<rule id="100300" level="11">
  <if_sid>550</if_sid>
  <file>/etc/sudoers|/etc/ssh/sshd_config|/root/.ssh/authorized_keys</file>
  <description>Critical system file modified: $file</description>
  <group>file_integrity</group>
</rule>
```
*Trigger: Unauthorized modification of /etc/sudoers → Level 11 → human review required*

**Malware Detection** (VirusTotal integration):
```xml
<rule id="100400" level="13">
  <description>Executable flagged as malware by VirusTotal</description>
  <group>malware_detection</group>
</rule>
```
*Requires osquery + VirusTotal plugin; triggers on executable download*

---

### 4.2 High-Priority Alerts (Slack Notification)

**Unauthorized Access Attempt** (SSH key added):
```
Level 10: New SSH public key added to authorized_keys
→ Slack #security: "New SSH key detected on [hostname] for user [user]. Approve or rollback?"
```

**Policy Violation** (unencrypted file with PII):
```
Level 8: File containing PII (regex: SSN, credit card) without encryption
→ Slack notification, quarantine file, auto-encrypt with LUKS
```

**Suspicious Process** (known malware signature):
```
Level 10: Process matches known malware pattern
→ Slack #security: "Suspicious process [name] on [host]. Auto-isolated. Approve containment?"
```

---

## Part 5: Escalation Pathway & Decision Tree

### 5.1 Alert → Human → Action Workflow

```
WAZUH ALERT (Level 12+)
    ↓
SOAR PLAYBOOK (auto-investigate)
    ↓
[Threat? Yes/No/Unknown]
    ├─ YES (Malware/Breach):
    │   → ISOLATE ENDPOINT (revoke Tailscale, disable user)
    │   → CRITICAL Slack: @security + @team-lead
    │   → Archive evidence
    │   → Await human approval (if false positive, restore)
    │
    ├─ UNKNOWN (requires investigation):
    │   → HIGH Slack: Context-rich alert
    │   → Request human analysis within 30 min
    │   → Escalate to team-lead if >30 min no response
    │
    └─ NO (false positive/policy-only):
        → LOG + SUPPRESS for 7 days
        → Notify team of suppression
        → Reopen if triggered again within window
```

### 5.2 Escalation Chain

| Level | Trigger | Auto-Action | Notification | Escalation Timeline |
|---|---|---|---|---|
| **CRITICAL** | Active attack, malware, breach | Isolate endpoint; disable account | @team-lead + all engineers | Immediate (5 min max) |
| **HIGH** | Suspicious activity, elevated privs | Log + context; await approval | Slack #security | <30 min |
| **MEDIUM** | Policy violations, config changes | Auto-remediate + log | Daily summary email | Next business day |
| **LOW** | Info only, baseline activity | Log only | Weekly summary | End of week |

### 5.3 Team Contact Preferences

**Define per team member**:
- Slack notifications: enabled/disabled
- Escalation threshold: critical-only or high+critical
- Time-based routing: e.g., only page on-call engineer during business hours
- Vacation/out-of-office: pause critical notifications

---

## Part 6: Incident Response Runbook

### 6.1 When CRITICAL Alert Triggered

**Immediate (0-5 min)**:
1. [ ] SOAR auto-isolated endpoint (confirm in Slack notification)
2. [ ] Review alert details: What triggered? What evidence?
3. [ ] Threat intelligence result: Malware? Yes/No/Unknown?

**If Malware Confirmed (5-15 min)**:
1. [ ] Preserve evidence: `tar czf /tmp/evidence-$(date).tar.gz /var/log /root/.bash_history`
2. [ ] Upload to secure storage (encrypted USB / S3 with MFA)
3. [ ] Full endpoint shutdown: do NOT leave running (may propagate malware)
4. [ ] Re-image from verified backup (if critical system)
5. [ ] Audit all other systems: run osquery rule "detect malware signature on all hosts"

**If False Positive (5-10 min)**:
1. [ ] Document: what triggered alert, why it's safe
2. [ ] Approve SOAR restoration: restore endpoint access, unsuspend user account
3. [ ] Update alert rules: add to whitelist or increase threshold
4. [ ] Post-incident review: was detection rule bad, or attacker sophisticated?

### 6.2 Post-Incident Analysis

**Within 24 hours**:
1. [ ] Timeline reconstruction: What happened, when, how
2. [ ] Root cause analysis: How did threat gain access?
3. [ ] Remediation audit: Have we fixed the underlying issue?
4. [ ] Communication: Brief team + stakeholders

---

## Part 7: Infrastructure Scalability

### 7.1 Single Server (Small Team, <20 endpoints)

```
┌─────────────────────────────┐
│   Wazuh All-in-One Server   │
├─────────────────────────────┤
│ • Wazuh Manager             │
│ • Elasticsearch             │
│ • Kibana                    │
│ • Alerts → Slack webhook    │
└─────────────────────────────┘
        ↑
   [Agents on endpoints]
```

**Requirements**:
- 2-4 CPU cores
- 8 GB RAM minimum
- 500 GB disk (for log retention)
- Backup: daily export to encrypted USB/S3

### 7.2 Distributed Setup (Large Team, 50-100+ endpoints)

```
┌─────────────────────────────────────────────┐
│   Load Balancer / Reverse Proxy (nginx)     │
├─────────────────────────────────────────────┤
│         ↓              ↓              ↓      │
│   Manager 1       Manager 2       Manager 3 │
│ (primary)      (secondary)     (failover)   │
│      ↓              ↓              ↓         │
│   Elasticsearch Cluster (3+ nodes)          │
│      ↓              ↓              ↓         │
│   ES-Node-1    ES-Node-2    ES-Node-3      │
└─────────────────────────────────────────────┘
        ↑                    ↑
   [Agents]            [Agents]
```

**Failover**: If primary manager fails, agents auto-failover to secondary (configured in agent .conf)

---

## Part 8: SOAR Tool Selection

### 8.1 Open-Source Options (Cost: $0 + time)

| Tool | Strengths | Weaknesses | Deploy Time |
|---|---|---|---|
| **Shuffle** | Simple UI, webhook-native, good for small teams | Limited playbook library, slower for scale | 2-4 hours |
| **TheHive** | Built for incident response, strong IR practices | Steeper learning curve | 4-8 hours |
| **n8n** | Workflow automation, large community, Wazuh integration | Not purpose-built for security | 2-3 hours |

**Recommendation for Phase 3**: Use **Shuffle** (simplest deployment, Slack integration pre-built, Wazuh integration available in community workflows)

### 8.2 Commercial Options (Cost: $$$, but faster + support)

| Tool | Strengths | Cost |
|---|---|---|
| **Splunk Phantom** | Enterprise-grade, 600+ pre-built playbooks, excellent support | $50K-100K/year |
| **Cortex XSOAR (Palo Alto)** | Modern UI, powerful orchestration, growing community | $30K-80K/year |
| **Chronicle (Google)** | Cloud-native, AI-powered, strong detection | $100K+/year |

**For activism/democracy work**: Open-source is recommended (budget-constrained, acceptable latency, privacy-first)

---

## Part 9: Integration Checklist

- [ ] Wazuh manager deployed (server)
- [ ] Elasticsearch cluster running (replication 3+ nodes)
- [ ] Kibana dashboard live (http://localhost:5601)
- [ ] Wazuh agents deployed on all endpoints (Linux, macOS, Windows)
- [ ] osquery agents running (process/file/network monitoring)
- [ ] SOAR tool (Shuffle/TheHive) deployed
- [ ] Slack webhook integrated (Wazuh → SOAR → Slack)
- [ ] Alert rules tuned (baseline + whitelist)
- [ ] Playbooks tested (manual trigger test)
- [ ] Team training completed (who responds to what?)
- [ ] Incident response runbook published (team wiki)
- [ ] Backups configured (daily export)
- [ ] On-call rotation established (who's responsible 24/7?)

---

**Document Status**: PRODUCTION-READY  
**Next Deliverable**: ZERO_TRUST_NETWORK_ARCHITECTURE.md (Tailscale + Authentik setup)  
**Owner**: Cybersecurity-Hardening Infrastructure Planning  
**Deadline**: June 1, 2026

