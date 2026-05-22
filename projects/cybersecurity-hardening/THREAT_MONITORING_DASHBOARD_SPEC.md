---
title: "Threat Monitoring Dashboard Specification — Real-Time Visibility for Phase 3"
created: "2026-05-23"
status: "PRODUCTION-READY — Phase 3 infrastructure security"
scope: "Dashboard design, metrics, alert visualization, escalation indicators"
deadline: "June 1, 2026"
owner: "Cybersecurity-Hardening Infrastructure Planning"
---

# Threat Monitoring Dashboard Specification

*Created May 23, 2026. A dashboard is where ops teams stare to detect emerging threats. This spec defines what to monitor during Phase 3 distribution (August-December 2026) when attack surface is highest.*

---

## Part 1: Dashboard Purpose

**During Phase 3**, the team is:
- Distributing security curriculum to 20-30 organizations
- Conducting briefings + training sessions
- Managing high-volume email outreach
- Running infrastructure 24/7

**Attack scenarios**:
- Attacker compromises mailbox to intercept outreach
- Attacker targets team infrastructure (DDoS, intrusion)
- Insider threat (disgruntled team member)
- Social engineering (phishing targeted at team)

**Dashboard goal**: Detect any of these within 5 minutes of occurrence

---

## Part 2: Dashboard Panels

### Panel 1: System Health (Top-Left)

**Metrics displayed**:
- Endpoint status: # devices online / # expected devices
- Average CPU usage: threshold warning at >70%
- Average memory usage: threshold warning at >80%
- Disk usage: critical alert if >90%
- Network latency: alert if >100ms (Tailscale mesh unhealthy)

**Color coding**:
```
Green:  All systems healthy
Yellow: Warning threshold (approaching limit)
Red:    Critical threshold (action needed)
```

**Example**: "18/20 endpoints online (2 offline >1hr)" → Yellow alert

---

### Panel 2: Authentication & Access (Top-Center)

**Metrics displayed**:
- Login success rate: # successful logins / # attempts (target: >95%)
- Device posture compliance: # compliant devices / # total (target: 100%)
- Failed authentication attempts (last 24h): # attempts
- MFA bypass attempts: # (should be 0)
- New devices added: # (audit for unexpected additions)

**Threshold alerts**:
- Login success rate <90%: possible account compromise
- Device posture <90%: possible security breach
- Failed attempts >10 in 1h: possible brute force

**Example**: "Failed auth attempts: 5 (user: john@..., IP: 203.x.x.x)" → Click to investigate

---

### Panel 3: Threat Detection (Top-Right)

**Metrics displayed**:
- Critical alerts (last 24h): # (malware, privilege escalation, etc.)
- High alerts (last 24h): # (suspicious behavior, policy violations)
- Medium alerts (last 24h): # (info only)
- Suppressed alerts: # (whitelisted false positives)
- Alert response time: avg time to auto-remediate (target: <10 min)

**Alert detail**: Click on "Critical alerts" to see:
```
Time: 2026-05-23 14:32:15 UTC
Device: laptop-anya (100.120.18.84)
Rule: Malware detected: curl binary (VirusTotal 5/71 engines)
Status: AUTO-ISOLATED (endpoint revoked Tailscale access)
Action: HUMAN REVIEW (awaiting approval to permanently revoke)
Evidence: /tmp/evidence-2026-05-23-14-32.tar.gz
```

---

### Panel 4: Network Traffic Patterns (Bottom-Left)

**Metrics displayed**:
- Inbound connections: # active connections
- Outbound connections: # active connections
- Data exfiltration alerts: # (any transfer >1GB)
- Geolocation anomalies: # users accessing from unexpected countries
- Tor/proxy usage: # devices detected on privacy networks

**Example**: "Outbound: 4 active connections, 2.3 GB transferred (to AWS S3) in 2h" → Normal for backups

---

### Panel 5: Incident Timeline (Bottom-Center)

**Chronological view** of recent incidents:

```
[14:32] CRITICAL: Malware detection on laptop-anya (auto-isolated)
        └─ VirusTotal hit: curl binary flagged
        └─ Auto-action: Revoke Tailscale access
        └─ Human action: Pending approval

[14:15] HIGH: SSH brute force on server-01 from 203.x.x.x
        └─ Attempts: 23 failed logins in 5 min
        └─ Auto-action: Rate-limit IP via UFW
        └─ Status: Resolved (IP blocked)

[13:42] MEDIUM: Policy violation on laptop-john
        └─ File detected: unencrypted_PII.csv in Downloads/
        └─ Auto-action: Quarantine + auto-encrypt
        └─ Status: Resolved

[13:15] LOW: Device updated (os-update on laptop-anya)
        └─ From: Ubuntu 20.04 → 22.04
        └─ Status: OK (OS updated, device posture improved)
```

---

### Panel 6: Team Status (Bottom-Right)

**At-a-glance team health**:
- # team members online (detected via Tailscale)
- # on-call engineer(s) (for critical escalations)
- Time since last security incident: 72h 15m (if any)
- SLA adherence: 100% (all alerts responded <30min)

**On-call rotation**:
```
2026-05-23 00:00 — 2026-05-24 00:00: Alice (alice@example.com)
2026-05-24 00:00 — 2026-05-25 00:00: Bob (bob@example.com)
2026-05-25 00:00 — 2026-05-26 00:00: Carol (carol@example.com)
```

**Click "Alice" → Contact info: Phone, Slack, Emergency email**

---

## Part 3: Dashboard Interaction

### Real-Time Updates
- Refresh every 10 seconds (not too fast = CPU hog, not too slow = miss alerts)
- Critical alerts: sound + browser notification (even if dashboard unfocused)

### Drill-Down Navigation
- Click any metric to see details
- Example: Click "Critical alerts: 1" → see malware alert details
- Click alert → see evidence files, auto-remediation status, approval workflow

### Export/Reporting
- Generate PDF report: daily/weekly/monthly threat summary
- Send email report to leadership (formatted for non-technical audience)

---

## Part 4: Dashboard Implementation

### Technology Stack

**Option A: Kibana (Elasticsearch native)**
- Included with Wazuh deployment
- Pros: free, integrated, real-time
- Cons: steeper learning curve

**Option B: Grafana (Universal dashboard)**
- Works with any data source (Wazuh, Prometheus, Datadog)
- Pros: beautiful UI, many integrations
- Cons: separate deployment needed

**Recommendation**: Start with Kibana (already deployed with Wazuh), migrate to Grafana if team prefers UI

### Kibana Configuration

**Create new dashboard**:
1. Kibana → Dashboards → Create new
2. Add visualizations (panels):
   - Area chart: Login success rate over time
   - Gauge: Device posture compliance %
   - Data table: Critical alerts (last 24h)
   - Geo map: Failed login attempts by location
   - Timeline: Incident log

**Create alerts** (notifications):
1. Kibana → Alerting → Create alert
2. Condition: "Critical alert from Wazuh"
3. Action: Send Slack message to #security

**Sample Kibana query** (system health):
```
source:"wazuh" AND rule.level:(12 OR 13 OR 14)
```
*Returns: All critical/severe alerts*

---

## Part 5: Sample Dashboard Screens

### Screen 1: Normal Operations (All Green)

```
┌─────────────────────────────────────────────────────┐
│ SYSTEM HEALTH       │ AUTH & ACCESS      │ THREATS   │
├─────────────────────┼────────────────────┼───────────┤
│ 20/20 online ✓      │ Success: 98% ✓     │ Critical: 0 ✓ │
│ CPU: 45% ✓          │ Compliance: 100% ✓ │ High: 0 ✓      │
│ Memory: 62% ✓       │ Failed: 0 ✓        │ Medium: 0 ✓    │
│ Disk: 52% ✓         │ MFA bypass: 0 ✓    │ Response: 2m ✓ │
│ Latency: 35ms ✓     │ New devices: 0 ✓   │                │
└─────────────────────┴────────────────────┴───────────┘

INCIDENT TIMELINE:
[12:00] Device online: laptop-bob
[11:45] Device online: server-01
[11:30] Device posture check: all compliant
```

### Screen 2: Alert State (Yellow/Red)

```
┌─────────────────────────────────────────────────────┐
│ SYSTEM HEALTH       │ AUTH & ACCESS      │ THREATS   │
├─────────────────────┼────────────────────┼───────────┤
│ 19/20 online ⚠      │ Success: 92% ⚠     │ Critical: 1 🔴 │
│ CPU: 78% ⚠          │ Compliance: 95% ⚠  │ High: 3 ⚠      │
│ Memory: 85% ⚠       │ Failed: 8 ⚠        │ Medium: 2 ⚠    │
│ Disk: 51% ✓         │ MFA bypass: 0 ✓    │ Response: 7m ⚠ │
│ Latency: 145ms 🔴   │ New devices: 1 ⚠   │                │
└─────────────────────┴────────────────────┴───────────┘

CRITICAL ALERT: [14:32] Malware on laptop-anya (auto-isolated)
  ACTION REQUIRED: Approve permanent isolation
  EVIDENCE: /tmp/evidence-2026-05-23-14-32.tar.gz [Download]
  [APPROVE] [INVESTIGATE] [FALSE POSITIVE]
```

---

## Part 6: Mobile Dashboard

**For on-call engineer on phone**:
- Simplified view: critical alerts only
- Large touch targets for quick action
- Slack integration: "Approve isolation?" → tap ✓
- Push notification for each critical alert

---

## Part 7: Compliance & Audit Logging

**Everything logged**:
- Who viewed dashboard (audit trail)
- Who approved/denied incident response (change management)
- All dashboard queries (immutable audit log)

**Export for compliance**:
- Monthly threat report (for board)
- Incident report (for legal)
- Posture report (for auditors)

---

## Part 8: Dashboard Maintenance

**Weekly**:
- Review false positives (suppress noise)
- Check dashboard responsiveness (refresh rate OK?)
- Update on-call rotation

**Monthly**:
- Review alert thresholds (are we detecting too much/too little?)
- Audit who has dashboard access
- Backup dashboard config

**Quarterly**:
- Update Wazuh rules (new threat intelligence)
- Refactor visualizations (make faster)
- Train new team members on dashboard

---

## Deployment Checklist

- [ ] Kibana running (port 5601)
- [ ] Create new dashboard
- [ ] Add 6 visualization panels (health, auth, threats, network, timeline, team)
- [ ] Configure Slack webhook for critical alerts
- [ ] Create Wazuh alert rules
- [ ] Test normal operations
- [ ] Test critical alert scenario (trigger manually)
- [ ] Train team on dashboard
- [ ] Document on-call procedures
- [ ] Configure mobile view
- [ ] Set up audit logging

---

**Document Status**: PRODUCTION-READY  
**Owner**: Cybersecurity-Hardening Infrastructure Planning  
**Deadline**: June 1, 2026

**Item 38 Complete**: All 3 deliverables (Incident Response, Zero-Trust, Monitoring) production-ready for Phase 3 execution.

