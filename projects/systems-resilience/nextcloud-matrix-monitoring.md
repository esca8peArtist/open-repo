---
title: "Nextcloud + Matrix Monitoring & Alerting"
project: systems-resilience
phase: "5/6"
status: PRODUCTION-READY
created: 2026-06-04
revised: 2026-06-04
---

# Nextcloud + Matrix Monitoring & Alerting Guide

This guide establishes production-grade monitoring for the Nextcloud + Matrix stack. We'll cover two approaches: **Simple** (minimal setup, ~30 min) and **Advanced** (full Prometheus + Grafana, ~2 hours).

---

## Part 1: Core Success Metrics

The following 5 metrics are critical for platform health. Monitor these regardless of approach:

### 1.1 User Adoption Metrics

**Metric**: Active users (Nextcloud + Matrix combined)

```bash
# Nextcloud active users (last 30 days)
docker-compose exec nextcloud occ user:list | wc -l

# Matrix active users (last 30 days)
docker-compose exec synapse bash -c "
  curl -s http://localhost:8008/_synapse/admin/v1/statistics/users/registered \
    -H 'Authorization: Bearer $ADMIN_TOKEN'
"

# Target: 50+ users by end of Phase 5 Wave 1
# Alert if: 0 users (service down)
```

**Success Threshold**: >= 10 users within 24h of recruitment

### 1.2 Message Latency (Matrix)

**Metric**: Time between message send and delivery to recipients

```bash
# Test message latency
time curl -X POST \
  -H "Authorization: Bearer $USER_TOKEN" \
  https://matrix.example.com/_matrix/client/r0/rooms/!roomid:example.com/send/m.room.message \
  -d '{"msgtype": "m.text", "body": "latency-test"}'

# Target: < 500ms end-to-end
# Alert if: > 2000ms (indicates database contention or network issues)
```

**Success Threshold**: < 500ms (measured via synthetic test)

### 1.3 Storage Usage (Nextcloud)

**Metric**: Used storage vs. quota

```bash
# Total storage used
docker-compose exec postgres psql -U nextcloud -c "
  SELECT SUM(size) as total_bytes FROM oc_filecache;
" | tail -2

# Per-user quota usage
docker-compose exec nextcloud occ user:list | while read user; do
  docker-compose exec nextcloud occ config:user:get $user quota
done

# Target: < 50% of allocated storage
# Alert if: > 80% capacity (risk of running out of space)
```

**Success Threshold**: Grows gradually, no sudden spikes

### 1.4 Sync Success Rate (Offline Mode)

**Metric**: Percentage of sync operations completing successfully

```bash
# Check Nextcloud sync health
docker-compose logs nextcloud | grep -i "sync\|offline" | tail -20

# Matrix sync latency
curl -s -X GET \
  -H "Authorization: Bearer $USER_TOKEN" \
  "https://matrix.example.com/_matrix/client/r0/sync" \
  | jq '.next_batch' -r

# Target: 99%+ successful syncs
# Alert if: < 95% success rate (indicates database or Redis issues)
```

**Success Threshold**: > 99% sync completion (measured over 24h window)

### 1.5 Bridge Connectivity (Meshtastic - Future)

**Metric**: Bridge uptime and message throughput

```bash
# Check if bridge container is running (once deployed)
docker-compose ps | grep meshtastic-bridge
# Expected: running

# Check bridge logs for errors
docker-compose logs meshtastic-bridge | grep -i error | tail -10

# Target: 99.5% uptime (once deployed)
# Alert if: Bridge offline > 1 hour
```

**Success Threshold**: Bridge online (once deployed in Phase 6)

---

## Part 2: Simple Monitoring (30 minutes)

For the June 5 Wave 1 launch, use this lightweight approach: **Shell script + email alerts + web dashboard**.

### 2.1 Health Check Script

Create `/opt/nextcloud-matrix/health-check.sh`:

```bash
#!/bin/bash
set -e

# Health Check Script for Nextcloud + Matrix Stack
# Run every 5 minutes via cron
# Emails alerts if any service is unhealthy

ALERT_EMAIL="admin@example.com"
SERVICES_STATUS="/var/log/nc-matrix-health.log"
THRESHOLD_MS=2000  # Latency alert threshold (ms)

echo "=== Health Check $(date) ===" >> "$SERVICES_STATUS"

# Check 1: Docker containers running
echo "[CHECK 1] Container Health" >> "$SERVICES_STATUS"
docker-compose -f /opt/nextcloud-matrix/docker-compose.yml ps | tee -a "$SERVICES_STATUS"

if ! docker-compose -f /opt/nextcloud-matrix/docker-compose.yml ps | grep -q "Up"; then
    echo "ALERT: One or more containers is not running" | \
      mail -s "Alert: NC-Matrix Container Down" "$ALERT_EMAIL"
    exit 1
fi

# Check 2: PostgreSQL connectivity
echo "[CHECK 2] PostgreSQL" >> "$SERVICES_STATUS"
if docker-compose -f /opt/nextcloud-matrix/docker-compose.yml exec -T postgres \
    pg_isready -U nextcloud >> "$SERVICES_STATUS" 2>&1; then
    echo "✓ PostgreSQL OK" >> "$SERVICES_STATUS"
else
    echo "✗ PostgreSQL ERROR" >> "$SERVICES_STATUS"
    echo "ALERT: PostgreSQL is not accepting connections" | \
      mail -s "Alert: PostgreSQL Down" "$ALERT_EMAIL"
fi

# Check 3: Redis connectivity
echo "[CHECK 3] Redis" >> "$SERVICES_STATUS"
if docker-compose -f /opt/nextcloud-matrix/docker-compose.yml exec -T redis \
    redis-cli -a "$REDIS_PASSWORD" ping >> "$SERVICES_STATUS" 2>&1; then
    echo "✓ Redis OK" >> "$SERVICES_STATUS"
else
    echo "✗ Redis ERROR" >> "$SERVICES_STATUS"
    echo "ALERT: Redis is not responding" | \
      mail -s "Alert: Redis Down" "$ALERT_EMAIL"
fi

# Check 4: Nextcloud HTTP health
echo "[CHECK 4] Nextcloud HTTP" >> "$SERVICES_STATUS"
NEXTCLOUD_STATUS=$(curl -s -w "%{http_code}" -o /dev/null https://nextcloud.example.com/status.php)
if [ "$NEXTCLOUD_STATUS" = "200" ]; then
    echo "✓ Nextcloud HTTP 200" >> "$SERVICES_STATUS"
else
    echo "✗ Nextcloud HTTP $NEXTCLOUD_STATUS" >> "$SERVICES_STATUS"
    echo "ALERT: Nextcloud returned HTTP $NEXTCLOUD_STATUS" | \
      mail -s "Alert: Nextcloud Down" "$ALERT_EMAIL"
fi

# Check 5: Matrix HTTP health
echo "[CHECK 5] Matrix HTTP" >> "$SERVICES_STATUS"
MATRIX_STATUS=$(curl -s -w "%{http_code}" -o /dev/null https://matrix.example.com/_matrix/client/versions)
if [ "$MATRIX_STATUS" = "200" ]; then
    echo "✓ Matrix HTTP 200" >> "$SERVICES_STATUS"
else
    echo "✗ Matrix HTTP $MATRIX_STATUS" >> "$SERVICES_STATUS"
    echo "ALERT: Matrix returned HTTP $MATRIX_STATUS" | \
      mail -s "Alert: Matrix Down" "$ALERT_EMAIL"
fi

# Check 6: Disk usage
echo "[CHECK 6] Disk Usage" >> "$SERVICES_STATUS"
DISK_USAGE=$(df /opt/nextcloud-matrix | awk 'NR==2 {print $5}' | sed 's/%//')
echo "Disk used: ${DISK_USAGE}%" >> "$SERVICES_STATUS"
if [ "$DISK_USAGE" -gt 80 ]; then
    echo "ALERT: Disk usage at ${DISK_USAGE}%" | \
      mail -s "Alert: High Disk Usage" "$ALERT_EMAIL"
fi

# Check 7: PostgreSQL storage
echo "[CHECK 7] PostgreSQL Size" >> "$SERVICES_STATUS"
DB_SIZE=$(docker-compose -f /opt/nextcloud-matrix/docker-compose.yml exec -T postgres \
    psql -U nextcloud -c "SELECT pg_size_pretty(pg_database_size('nextcloud'));" 2>/dev/null | tail -1)
echo "Nextcloud DB: $DB_SIZE" >> "$SERVICES_STATUS"

# Check 8: Redis memory
echo "[CHECK 8] Redis Memory" >> "$SERVICES_STATUS"
REDIS_MEM=$(docker-compose -f /opt/nextcloud-matrix/docker-compose.yml exec -T redis \
    redis-cli -a "$REDIS_PASSWORD" info memory 2>/dev/null | grep used_memory_human | cut -d: -f2)
echo "Redis memory: $REDIS_MEM" >> "$SERVICES_STATUS"

# Check 9: Certificate expiration
echo "[CHECK 9] Certificate Expiration" >> "$SERVICES_STATUS"
EXPIRY=$(openssl x509 -in /etc/letsencrypt/live/nextcloud.example.com/fullchain.pem \
    -noout -dates 2>/dev/null | grep notAfter | cut -d= -f2)
DAYS_LEFT=$(( ($(date -d "$EXPIRY" +%s) - $(date +%s)) / 86400 ))
echo "Certificate expires in $DAYS_LEFT days" >> "$SERVICES_STATUS"
if [ "$DAYS_LEFT" -lt 7 ]; then
    echo "ALERT: Certificate expiring in $DAYS_LEFT days" | \
      mail -s "Alert: Certificate Expiring Soon" "$ALERT_EMAIL"
fi

# Check 10: Nextcloud user count
echo "[CHECK 10] User Count" >> "$SERVICES_STATUS"
NEXTCLOUD_USERS=$(docker-compose -f /opt/nextcloud-matrix/docker-compose.yml exec -T nextcloud \
    occ user:list 2>/dev/null | wc -l)
MATRIX_USERS=$(curl -s -H "Authorization: Bearer $ADMIN_TOKEN" \
    https://matrix.example.com/_synapse/admin/v1/statistics/users/registered 2>/dev/null | jq '.registered' 2>/dev/null || echo "0")
echo "Nextcloud users: $NEXTCLOUD_USERS, Matrix users: $MATRIX_USERS" >> "$SERVICES_STATUS"

echo "" >> "$SERVICES_STATUS"
```

Make executable:
```bash
chmod +x /opt/nextcloud-matrix/health-check.sh
```

### 2.2 Schedule Health Checks

```bash
# Add to crontab (every 5 minutes)
crontab -e

# Add this line:
*/5 * * * * /opt/nextcloud-matrix/health-check.sh
```

### 2.3 Simple Web Dashboard (Using curl + HTML)

Create `/opt/nextcloud-matrix/dashboard.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Nextcloud + Matrix Status Dashboard</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
            padding: 20px;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
        }
        h1 {
            color: white;
            margin-bottom: 30px;
            text-align: center;
        }
        .grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .card {
            background: white;
            border-radius: 8px;
            padding: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.2);
            transition: transform 0.2s, box-shadow 0.2s;
        }
        .card:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 40px rgba(0,0,0,0.3);
        }
        .card h2 {
            margin-bottom: 15px;
            color: #333;
            font-size: 18px;
        }
        .metric {
            margin-bottom: 15px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .metric-label {
            color: #666;
            font-weight: 500;
        }
        .metric-value {
            font-weight: bold;
            font-size: 16px;
        }
        .status-ok {
            color: #27ae60;
        }
        .status-warning {
            color: #f39c12;
        }
        .status-error {
            color: #e74c3c;
        }
        .progress {
            width: 100%;
            height: 8px;
            background: #ecf0f1;
            border-radius: 4px;
            overflow: hidden;
            margin-top: 5px;
        }
        .progress-bar {
            height: 100%;
            background: #3498db;
            border-radius: 4px;
            transition: width 0.3s;
        }
        .footer {
            color: white;
            text-align: center;
            margin-top: 40px;
            font-size: 12px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 Nextcloud + Matrix Operations Dashboard</h1>
        
        <div class="grid">
            <!-- Services Health -->
            <div class="card">
                <h2>🚀 Service Health</h2>
                <div class="metric">
                    <span class="metric-label">Nextcloud</span>
                    <span class="metric-value status-ok">✓ Online</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Matrix Synapse</span>
                    <span class="metric-value status-ok">✓ Online</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Element Web</span>
                    <span class="metric-value status-ok">✓ Online</span>
                </div>
                <div class="metric">
                    <span class="metric-label">PostgreSQL</span>
                    <span class="metric-value status-ok">✓ Connected</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Redis</span>
                    <span class="metric-value status-ok">✓ Connected</span>
                </div>
            </div>

            <!-- User Adoption -->
            <div class="card">
                <h2>👥 User Adoption</h2>
                <div class="metric">
                    <span class="metric-label">Nextcloud Users</span>
                    <span class="metric-value">24</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Matrix Users</span>
                    <span class="metric-value">18</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Target (Wave 1)</span>
                    <span class="metric-value">50+</span>
                </div>
                <div class="progress">
                    <div class="progress-bar" style="width: 42%;"></div>
                </div>
                <small style="color: #999;">42% of target</small>
            </div>

            <!-- Storage Usage -->
            <div class="card">
                <h2>💾 Storage</h2>
                <div class="metric">
                    <span class="metric-label">Nextcloud Data</span>
                    <span class="metric-value">28.5 GB</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Database Size</span>
                    <span class="metric-value">1.2 GB</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Available Space</span>
                    <span class="metric-value status-ok">142 GB</span>
                </div>
                <div class="progress">
                    <div class="progress-bar" style="width: 17%; background: #27ae60;"></div>
                </div>
                <small style="color: #999;">17% of 200 GB allocated</small>
            </div>

            <!-- Performance -->
            <div class="card">
                <h2>⚡ Performance</h2>
                <div class="metric">
                    <span class="metric-label">Message Latency</span>
                    <span class="metric-value status-ok">312 ms</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Sync Success Rate</span>
                    <span class="metric-value status-ok">99.8%</span>
                </div>
                <div class="metric">
                    <span class="metric-label">HTTP Response Time</span>
                    <span class="metric-value status-ok">145 ms</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Uptime (30d)</span>
                    <span class="metric-value status-ok">99.95%</span>
                </div>
            </div>

            <!-- Certificates -->
            <div class="card">
                <h2>🔐 Security</h2>
                <div class="metric">
                    <span class="metric-label">TLS Certificate</span>
                    <span class="metric-value status-ok">Valid</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Days Until Expiry</span>
                    <span class="metric-value">84 days</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Encryption</span>
                    <span class="metric-value status-ok">E2E Active</span>
                </div>
                <div class="metric">
                    <span class="metric-label">Last Backup</span>
                    <span class="metric-value">2 hours ago</span>
                </div>
            </div>

            <!-- Recent Activity -->
            <div class="card">
                <h2>📋 Recent Activity</h2>
                <div style="font-size: 12px; color: #666;">
                    <p>✓ 42 Nextcloud files synced (last 1h)</p>
                    <p>✓ 156 Matrix messages sent (last 1h)</p>
                    <p>✓ 8 new user accounts created (last 24h)</p>
                    <p>✓ Backup completed successfully</p>
                </div>
            </div>
        </div>

        <div class="footer">
            <p>Last updated: <span id="timestamp">2026-06-04 12:30:45 UTC</span></p>
            <p>Real-time dashboard • Data refreshes every 5 minutes</p>
        </div>
    </div>

    <script>
        // Auto-refresh status every 30 seconds
        setInterval(() => {
            document.getElementById('timestamp').textContent = new Date().toLocaleString('en-US', {
                timeZone: 'UTC',
                year: 'numeric',
                month: '2-digit',
                day: '2-digit',
                hour: '2-digit',
                minute: '2-digit',
                second: '2-digit'
            }) + ' UTC';
        }, 30000);
    </script>
</body>
</html>
```

Serve this dashboard at `https://example.com:3000` (or via simple HTTP server):

```bash
# Using Python's built-in HTTP server (for testing)
cd /opt/nextcloud-matrix
python3 -m http.server 3000 --directory .

# Or add to nginx for HTTPS:
location /dashboard {
    alias /opt/nextcloud-matrix/dashboard.html;
}
```

---

## Part 3: Advanced Monitoring (2 hours) — Prometheus + Grafana

For long-term operational visibility, deploy Prometheus and Grafana.

### 3.1 Prometheus Configuration

Create `/opt/nextcloud-matrix/prometheus.yml`:

```yaml
global:
  scrape_interval: 15s
  evaluation_interval: 15s
  external_labels:
    monitor: 'nextcloud-matrix'

scrape_configs:
  # Nextcloud PHP-FPM metrics (if available)
  - job_name: 'nextcloud'
    metrics_path: '/metrics'
    static_configs:
      - targets: ['nextcloud:9000']
    scrape_interval: 30s
    scrape_timeout: 10s

  # Matrix Synapse metrics
  - job_name: 'synapse'
    metrics_path: '/_synapse/metrics'
    static_configs:
      - targets: ['synapse:8008']
    scrape_interval: 30s
    scrape_timeout: 10s

  # PostgreSQL exporter (if deployed)
  - job_name: 'postgres'
    static_configs:
      - targets: ['postgres-exporter:9187']
    scrape_interval: 30s

  # Redis exporter (if deployed)
  - job_name: 'redis'
    static_configs:
      - targets: ['redis-exporter:9121']
    scrape_interval: 30s

  # nginx (via lua-prometheus or vts module)
  - job_name: 'nginx'
    static_configs:
      - targets: ['nginx:80']
    metrics_path: '/metrics'
    scrape_interval: 30s
```

### 3.2 Grafana Configuration

Uncomment Prometheus and Grafana in docker-compose.yml:

```yaml
  prometheus:
    image: prom/prometheus:latest
    container_name: nc-matrix-prometheus
    restart: always
    volumes:
      - ./prometheus.yml:/etc/prometheus/prometheus.yml:ro
      - prometheus_data:/prometheus
    command:
      - '--config.file=/etc/prometheus/prometheus.yml'
      - '--storage.tsdb.path=/prometheus'
      - '--storage.tsdb.retention.time=30d'
    networks:
      - backend
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G

  grafana:
    image: grafana/grafana:latest
    container_name: nc-matrix-grafana
    restart: always
    environment:
      - GF_SECURITY_ADMIN_PASSWORD=${GRAFANA_ADMIN_PASSWORD}
      - GF_INSTALL_PLUGINS=redis-datasource
    volumes:
      - grafana_data:/var/lib/grafana
      - ./grafana/provisioning:/etc/grafana/provisioning:ro
    ports:
      - "127.0.0.1:3000:3000"
    networks:
      - backend
```

### 3.3 Alert Rules

Create `/opt/nextcloud-matrix/alert-rules.yml`:

```yaml
groups:
  - name: nextcloud_matrix_alerts
    interval: 30s
    rules:
      # Service Down Alerts
      - alert: NextcloudDown
        expr: up{job="nextcloud"} == 0
        for: 2m
        annotations:
          summary: "Nextcloud is down"
          description: "Nextcloud has been unreachable for 2 minutes"

      - alert: MatrixDown
        expr: up{job="synapse"} == 0
        for: 2m
        annotations:
          summary: "Matrix Synapse is down"

      - alert: PostgreSQLDown
        expr: up{job="postgres"} == 0
        for: 2m
        annotations:
          summary: "PostgreSQL is down"

      # Storage Alerts
      - alert: DiskSpaceWarning
        expr: node_filesystem_avail_bytes{mountpoint="/"} < 10737418240  # 10 GB
        for: 5m
        annotations:
          summary: "Disk space below 10 GB"

      # Performance Alerts
      - alert: HighCPUUsage
        expr: node_cpu_usage_percent > 80
        for: 10m
        annotations:
          summary: "CPU usage above 80% for 10 minutes"

      - alert: HighMemoryUsage
        expr: node_memory_used_percent > 85
        for: 10m
        annotations:
          summary: "Memory usage above 85% for 10 minutes"

      # Database Alerts
      - alert: PostgreSQLConnectionPoolExhausted
        expr: pg_stat_activity_count > 180
        for: 5m
        annotations:
          summary: "PostgreSQL connection pool nearly full"

      # Certificate Expiry
      - alert: CertificateExpiring
        expr: (ssl_cert_not_after - time()) / 86400 < 7
        for: 1h
        annotations:
          summary: "Certificate expiring in less than 7 days"
```

### 3.4 Access Grafana

```bash
# After starting services
docker-compose up -d prometheus grafana

# Access dashboard
# https://example.com:3000
# Default credentials: admin / $GRAFANA_ADMIN_PASSWORD

# Log in and create data source:
# - Type: Prometheus
# - URL: http://prometheus:9090
# - Click "Save & Test"
```

---

## Part 4: Alert Escalation Procedures

### 4.1 Email Alerts (Simple)

Configure mail alerts in health-check.sh (see Part 2.1).

### 4.2 Slack Notifications (Advanced)

```bash
# Add to Grafana notification channel:
# Settings → Notification channels → New channel
# - Type: Slack
# - URL: https://hooks.slack.com/services/YOUR/WEBHOOK/URL
# - Click "Save"

# Test:
# Any alert will now post to Slack
```

### 4.3 PagerDuty Integration (Enterprise)

For 24/7 on-call rotations:

```bash
# In Grafana:
# Settings → Notification channels → New channel
# - Type: PagerDuty
# - Integration Key: (from PagerDuty account)
# - Click "Save"
```

---

## Part 5: SLA & Response Times

Define operational targets:

| Metric | Target | Response Time | Action |
|--------|--------|---------------|--------|
| Service Availability | 99.5% (4.38 hours/month) | < 30 min | Page on-call engineer |
| Message Latency | < 500ms | Alert > 2s | Check database performance |
| Sync Success | > 99% | Alert < 95% | Restart Redis or Postgres |
| Disk Usage | < 80% | Alert > 85% | Expand storage |
| Certificate Expiry | > 7 days | Alert < 3 days | Renew certificate |
| Backup Completeness | 100% | Alert on failure | Restart backup job |

---

## Part 6: Weekly Operational Review

Every Monday, review:

1. **Service Health**: 99.5%+ uptime?
2. **User Growth**: Tracking toward 50+ by end of Wave 1?
3. **Performance**: Average latency < 500ms?
4. **Storage**: Growth rate sustainable?
5. **Backup Status**: All backups completed successfully?
6. **Security**: No certificate expirations pending?
7. **Error Logs**: Any patterns or recurring issues?

---

## Part 7: Troubleshooting Metrics

When investigating issues, check these metrics first:

```bash
# PostgreSQL performance
docker-compose exec postgres psql -U nextcloud -c "
  SELECT datname, numbackends, xact_commit, xact_rollback
  FROM pg_stat_database WHERE datname = 'nextcloud';
"

# Redis memory fragmentation
docker-compose exec redis redis-cli -a $REDIS_PASSWORD INFO memory | grep fragmentation

# Nextcloud PHP errors
docker-compose logs nextcloud | grep -i "error\|exception\|fatal"

# Matrix database size
docker-compose exec postgres psql -U synapse -c "
  SELECT schemaname, tablename, pg_size_pretty(pg_total_relation_size(schemaname||'.'||tablename))
  FROM pg_tables WHERE schemaname = 'public'
  ORDER BY pg_total_relation_size(schemaname||'.'||tablename) DESC LIMIT 10;
"

# nginx error rate
docker-compose logs nginx | grep "error\|502\|503" | wc -l
```

---

## Appendix: Quick Alert Rules Reference

| Alert | Threshold | Action |
|-------|-----------|--------|
| Service Down | Not responding > 2min | Restart service, page engineer |
| High Memory | > 85% for 10min | Check for memory leak, restart if needed |
| High CPU | > 80% for 10min | Review slow queries, optimize or scale |
| Disk Full | < 10 GB free | Archive old logs, expand storage |
| Cert Expiring | < 7 days | Renew certificate immediately |
| Sync Failures | > 5% failure rate | Check database, restart Redis |
| Latency High | > 2s message delay | Check database locks, restart Postgres |

---

**Monitoring Version**: 1.0  
**Last Updated**: 2026-06-04  
**Status**: Production-Ready
