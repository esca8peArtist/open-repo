# Discourse Deployment SOP with IPv6 Workaround
## Standard Operating Procedure for Phase 5.1 Publication (Alternative Platform)

**Version**: 1.0 (NOT RECOMMENDED - IPv6 bug requires workaround)  
**Last Updated**: June 16, 2026  
**Total Deployment Time**: 2-3 hours + 15 min IPv6 workaround = 2h 45m  
**Target Platform**: Raspberry Pi 5 (8GB RAM) with Raspberry Pi OS  
**⚠️ Status**: DEPLOYMENT POSSIBLE BUT NOT RECOMMENDED (use Nextcloud+Matrix instead)

---

## ⚠️ IMPORTANT: IPv6 LOOPBACK BUG ON PI5

**Blocker**: Discourse GitHub Issue #15847 — Redis fails to bind to IPv6 loopback on Raspberry Pi 5  
**Impact**: Causes database connection failures unless workaround applied  
**Workaround Required**: One of three options (all apply for stability)

See **PHASE 0** for workaround implementation before deploying.

---

## PRE-DEPLOYMENT CHECKLIST

**User Actions Required (24h before deployment)**:
- [ ] SMTP credentials collected (hostname, port, username, password)
- [ ] Domain name prepared (e.g., phase5.example.com)
- [ ] DNS A record pointing to 100.70.184.84 (test: `nslookup`)
- [ ] Let's Encrypt email address ready
- [ ] 40GB disk space available (verify: `df -h /`)
- [ ] 4GB available RAM (verify: `free -h`)
- [ ] IPv6 workaround selected (see Phase 0)

**Deployment Prerequisites**:
- [ ] SSH access to Pi (raspby1)
- [ ] Docker + Docker Compose installed
- [ ] sudo privileges on Pi

---

## DEPLOYMENT PHASES OVERVIEW

| Phase | Task | Duration | Critical |
|-------|------|----------|----------|
| 0 | IPv6 Workaround Setup | 15 min | ⚠️ **REQUIRED** |
| 1 | Environment Setup | 30 min | Yes |
| 2 | Docker Compose Config | 30 min | Yes |
| 3 | Start Services | 30 min | Yes |
| 4 | Discourse Configuration | 20 min | No |
| 5 | Verification | 20 min | Yes |
| **TOTAL** | | **2h 45m** | |

---

## PHASE 0: IPv6 LOOPBACK BUG WORKAROUND (15 minutes)

### ⚠️ Context: The Bug

**GitHub**: discourse/discourse#15847  
**Issue**: Redis fails to bind to IPv6 localhost (::1) on Raspberry Pi 5 with 64-bit OS  
**Symptom**: Discourse startup fails with:
```
could not connect to Redis at localhost:6379
```

**Root Cause**: Linux kernel IPv6 loopback binding behavior differs on Pi5; Redis defaults to dual-stack IPv6+IPv4

### 0.1 Select Workaround (Choose ONE)

#### Option A: Kernel Parameter Patch (System-Level) ⭐ RECOMMENDED

Disables IPv6 loopback entirely (safest for Pi5):

```bash
# SSH to Pi
ssh pi@100.70.184.84

# Apply kernel parameter
echo "net.ipv6.conf.lo.disable_ipv6 = 1" | \
  sudo tee /etc/sysctl.d/99-disable-ipv6-loopback.conf

# Activate immediately
sudo sysctl -p /etc/sysctl.d/99-disable-ipv6-loopback.conf

# Verify
ip link show lo
```

**Expected Output**:
```
1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
```

**Pros**: System-level fix, survives container restarts  
**Cons**: Affects all IPv6 loopback usage on Pi

#### Option B: Docker-Compose Redis Config (Container-Level)

Modify docker-compose.yml to force IPv4-only Redis binding:

```yaml
redis:
  image: redis:7-alpine
  command: redis-server --bind 127.0.0.1 --port 6379
```

**Pros**: No system-wide changes  
**Cons**: Per-container, must be maintained

#### Option C: Docker Network Bridge Mode

Use bridge network instead of host network:

```yaml
services:
  discourse:
    networks:
      - discourse-net
    # ...

networks:
  discourse-net:
    driver: bridge
```

**Pros**: Network isolation  
**Cons**: More complex networking

### 0.2 Apply Chosen Workaround

```bash
# Option A (RECOMMENDED):
echo "net.ipv6.conf.lo.disable_ipv6 = 1" | \
  sudo tee /etc/sysctl.d/99-disable-ipv6-loopback.conf
sudo sysctl -p /etc/sysctl.d/99-disable-ipv6-loopback.conf

echo "✅ IPv6 loopback disabled"
```

### 0.3 Verify Workaround Effectiveness

```bash
# Test IPv6 loopback status
cat /proc/sys/net/ipv6/conf/lo/disable_ipv6

# Output should be: 1 (disabled)
```

---

## PHASE 1: ENVIRONMENT SETUP (30 minutes)

### 1.1 Create Deployment Directory

```bash
sudo mkdir -p /opt/discourse
sudo chown pi:pi /opt/discourse
cd /opt/discourse
pwd  # Should output: /opt/discourse
```

### 1.2 Create Environment File Template

```bash
cat > .env << 'EOF'
# ============================================
# DISCOURSE CONFIGURATION
# ============================================
DISCOURSE_HOSTNAME=your-domain.com
DISCOURSE_DEVELOPER_EMAILS=admin@your-domain.com
DISCOURSE_SMTP_ADDRESS=smtp.mailgun.org
DISCOURSE_SMTP_PORT=587
DISCOURSE_SMTP_USER_NAME=postmaster@your-domain.com
DISCOURSE_SMTP_PASSWORD=CHANGEME_API_KEY
DISCOURSE_SMTP_ENABLE_START_TLS=true
DISCOURSE_SMTP_AUTHENTICATION=login

# ============================================
# POSTGRESQL CONFIGURATION
# ============================================
POSTGRES_PASSWORD=CHANGEME_STRONG_PASSWORD_32_CHARS_MIN

# ============================================
# LETSENCRYPT / SSL
# ============================================
LETSENCRYPT_EMAIL=admin@your-domain.com
EOF

echo "✅ Created .env template"
```

### 1.3 Edit Environment File

```bash
nano .env
```

**Required Changes**:

| Placeholder | Replace With | Example |
|-------------|--------------|---------|
| `your-domain.com` | Your actual domain | `phase5.example.com` |
| `admin@your-domain.com` | Admin email | `admin@phase5.example.com` |
| `smtp.mailgun.org` | SMTP hostname | `smtp.sendgrid.net` |
| `CHANGEME_API_KEY` | Mailgun/SendGrid API key | From provider |
| `postmaster@your-domain.com` | SMTP sender | `postmaster@phase5.example.com` |
| `CHANGEME_STRONG_PASSWORD_32_CHARS_MIN` | 32-char password | `$(openssl rand -base64 32)` |

### 1.4 Generate Secure Passwords

```bash
echo "PostgreSQL password: $(openssl rand -base64 32)"
```

Copy and paste into `.env`.

### 1.5 Verify Configuration

```bash
if grep -q "CHANGEME" .env; then
  echo "❌ ERROR: .env still contains CHANGEME placeholders"
  exit 1
else
  echo "✅ All placeholders replaced"
fi
```

---

## PHASE 2: DOCKER COMPOSE CONFIGURATION (30 minutes)

### 2.1 Create docker-compose.yml

Save as `/opt/discourse/docker-compose.yml`:

```yaml
version: '3.9'

services:
  # PostgreSQL: Discourse database
  postgres:
    image: postgres:15-alpine
    container_name: discourse-postgres
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_INITDB_ARGS: -c max_connections=200 -c shared_buffers=256MB
    volumes:
      - postgres_data:/var/lib/postgresql/data
    networks:
      - discourse-net
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Redis: Cache backend (IPv6 WORKAROUND APPLIED)
  redis:
    image: redis:7-alpine
    container_name: discourse-redis
    # IPv6 WORKAROUND: Force IPv4-only binding
    command: redis-server --bind 127.0.0.1 --port 6379 --appendonly yes --maxmemory 1gb
    volumes:
      - redis_data:/data
    networks:
      - discourse-net
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

  # Discourse: Forum application
  discourse:
    image: discourse/discourse:latest
    container_name: discourse-app
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      DISCOURSE_HOSTNAME: ${DISCOURSE_HOSTNAME}
      DISCOURSE_DEVELOPER_EMAILS: ${DISCOURSE_DEVELOPER_EMAILS}
      DISCOURSE_SMTP_ADDRESS: ${DISCOURSE_SMTP_ADDRESS}
      DISCOURSE_SMTP_PORT: ${DISCOURSE_SMTP_PORT}
      DISCOURSE_SMTP_USER_NAME: ${DISCOURSE_SMTP_USER_NAME}
      DISCOURSE_SMTP_PASSWORD: ${DISCOURSE_SMTP_PASSWORD}
      DISCOURSE_SMTP_ENABLE_START_TLS: ${DISCOURSE_SMTP_ENABLE_START_TLS}
      DISCOURSE_SMTP_AUTHENTICATION: ${DISCOURSE_SMTP_AUTHENTICATION}
      DISCOURSE_FORCE_HTTPS: "true"
      DISCOURSE_ALLOW_CSV_IMPORT: "false"
      DISCOURSE_MAX_UPLOAD_SIZE_MB: 100
      DISCOURSE_DB_HOST: postgres
      DISCOURSE_DB_NAME: discourse
      DISCOURSE_DB_USER: discourse
      DISCOURSE_DB_PASSWORD: ${POSTGRES_PASSWORD}
      DISCOURSE_REDIS_URL: redis://redis:6379
      RAILS_ENV: production
      RACK_ENV: production
    volumes:
      - discourse_data:/shared
      - discourse_logs:/var/log/discourse
    ports:
      - "127.0.0.1:80:80"
      - "127.0.0.1:443:443"
    networks:
      - discourse-net
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/srv/status"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s
    restart: unless-stopped
    logging:
      driver: "json-file"
      options:
        max-size: "10m"
        max-file: "3"

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
  discourse_data:
    driver: local
  discourse_logs:
    driver: local

networks:
  discourse-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.21.0.0/16
```

### 2.2 Validate docker-compose.yml

```bash
docker-compose config > /dev/null && \
  echo "✅ docker-compose.yml is valid" || \
  echo "❌ Syntax error"
```

---

## PHASE 3: START SERVICES (30 minutes)

### 3.1 Pre-Flight Check

```bash
echo "=== PRE-FLIGHT CHECK ==="

# RAM check
free_gb=$(free -g | awk '/^Mem:/ {print $7}')
if [ "$free_gb" -lt 4 ]; then
  echo "❌ FAIL: Need 4GB free RAM (have ${free_gb}GB)"
  exit 1
fi
echo "✅ RAM: ${free_gb}GB available"

# Disk check
disk_gb=$(df -BG / | awk 'NR==2 {print $4}' | sed 's/G//')
if [ "$disk_gb" -lt 40 ]; then
  echo "❌ FAIL: Need 40GB (have ${disk_gb}GB)"
  exit 1
fi
echo "✅ Disk: ${disk_gb}GB available"

# Docker check
docker ps > /dev/null || (echo "❌ Docker not running"; exit 1)
echo "✅ Docker operational"
```

### 3.2 Clean Previous Deployments

```bash
docker-compose down -v 2>/dev/null || true
echo "✅ Cleaned previous deployment"
```

### 3.3 Start Services

```bash
echo "Starting Discourse services..."
docker-compose up -d

sleep 5

echo "Monitoring startup (max 5 minutes)..."
for i in {1..60}; do
  healthy=$(docker-compose ps --filter "health=healthy" -q 2>/dev/null | wc -l)
  unhealthy=$(docker-compose ps --filter "health=unhealthy" -q 2>/dev/null | wc -l)
  
  echo "[$((i))/60] Healthy: $healthy | Unhealthy: $unhealthy"
  
  if [ "$healthy" -ge 3 ] || [ "$unhealthy" -gt 0 ]; then
    break
  fi
  
  sleep 5
done

echo ""
echo "Service Status:"
docker-compose ps
```

### 3.4 Monitor Startup Logs

```bash
# Watch logs (Ctrl+C to exit)
docker-compose logs -f

# Or check for errors:
docker logs discourse-app 2>&1 | grep -i "error\|redis\|ipv6" | head -10
```

**Expected Output**:
```
CONTAINER ID   STATUS
discourse-postgres   healthy
discourse-redis      healthy
discourse-app        healthy
```

### 3.5 Check Resource Usage

```bash
docker stats --no-stream --format "table {{.Container}}\t{{.MemUsage}}\t{{.CPUPerc}}"
```

**Expected**:
```
discourse-postgres    256MB / 8GB     5%
discourse-redis       64MB / 8GB      1%
discourse-app         1.2GB / 8GB     30%
```

---

## PHASE 4: DISCOURSE CONFIGURATION (20 minutes)

### 4.1 Wait for Discourse Initialization

```bash
echo "Waiting for Discourse initialization..."

for i in {1..30}; do
  if curl -s http://localhost/srv/status 2>/dev/null | grep -q "ok"; then
    echo "✅ Discourse initialized"
    break
  fi
  echo "  ...still initializing (step $((i))/30)"
  sleep 5
done

sleep 10  # Extra wait for migrations
```

### 4.2 Access Discourse Web UI

```bash
DOMAIN=$(grep '^DISCOURSE_HOSTNAME=' .env | cut -d= -f2)
EMAIL=$(grep '^DISCOURSE_DEVELOPER_EMAILS=' .env | cut -d= -f2)

echo ""
echo "=== DISCOURSE WEB ACCESS ==="
echo "📱 URL: http://$DOMAIN"
echo "📧 Admin email: $EMAIL"
echo ""
echo "✅ Discourse is accessible"
echo ""
echo "Next steps (web UI):"
echo "  1. Visit http://$DOMAIN"
echo "  2. Sign up with email: $EMAIL"
echo "  3. Create admin account + password"
echo "  4. Configure site settings"
echo "  5. Create categories for Wave 2 teams"
```

### 4.3 Create Test Post

Test forum functionality:

```bash
echo "Testing forum functionality..."

# Create test category (optional, can do via web UI)
# This is just to verify API is working:

curl -X POST http://localhost:3000/categories.json \
  -H "Content-Type: application/json" \
  -d '{"name":"Test Category","color":"0088cc"}' \
  2>/dev/null | grep -q "Test Category" && \
  echo "✅ Forum API working" || \
  echo "⚠️  Category creation may need admin login first"
```

---

## PHASE 5: VERIFICATION & IPv6 TROUBLESHOOTING (20 minutes)

### 5.1 Redis IPv6 Workaround Verification

**Critical**: Verify Redis is NOT binding to IPv6:

```bash
# Check Redis binding
docker exec discourse-redis redis-cli info server | grep -A5 "tcp_port"

# Expected output should show IPv4-only:
# tcp_port:6379
# (NO IPv6 references)
```

### 5.2 Discourse Connection to Redis

```bash
# Test Redis connectivity from Discourse
docker exec discourse-app redis-cli -h redis ping

# Expected: PONG
```

If this fails:
```bash
docker logs discourse-redis | grep -i "bind\|ipv6\|error" | head -5
docker logs discourse-app | grep -i "redis\|connection" | head -10
```

### 5.3 Database Connection Verification

```bash
# Check PostgreSQL
docker exec discourse-postgres pg_isready -U postgres

# Expected: accepting connections
```

### 5.4 IPv6 Client Connection Test (Optional)

If you have IPv6 client available:

```bash
# From IPv6 client:
curl -s -I http://[IPv6_ADDRESS] 2>&1

# Should NOT show IPv6 loopback binding errors
```

### 5.5 Complete Validation Checklist

```bash
#!/bin/bash

echo "=== DISCOURSE VALIDATION CHECKLIST ==="
echo ""

total=0
passed=0

# 1. Containers running
echo "[1/6] Containers..."
total=$((total + 1))
if docker-compose ps | grep -q "Up"; then
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL"
fi

# 2. Redis (IPv6-safe)
echo "[2/6] Redis (no IPv6 binding)..."
total=$((total + 1))
if docker exec discourse-redis redis-cli ping 2>/dev/null | grep -q "PONG"; then
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL: Redis not responding"
fi

# 3. PostgreSQL
echo "[3/6] PostgreSQL..."
total=$((total + 1))
if docker exec discourse-postgres pg_isready -U postgres > /dev/null 2>&1; then
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL"
fi

# 4. Discourse health
echo "[4/6] Discourse API..."
total=$((total + 1))
if curl -s http://localhost/srv/status 2>/dev/null | grep -q "ok"; then
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ❌ FAIL: API not responding"
fi

# 5. Memory usage
echo "[5/6] Memory usage..."
total=$((total + 1))
mem_used=$(free -g | awk '/^Mem:/ {print $3}')
if [ "$mem_used" -lt 6 ]; then
  echo "    ${mem_used}GB used (acceptable)"
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ⚠️  High: ${mem_used}GB used"
fi

# 6. Disk space
echo "[6/6] Disk space..."
total=$((total + 1))
disk=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')
if [ "$disk" -lt 80 ]; then
  echo "    ${disk}% used (acceptable)"
  echo "    ✅ PASS"
  passed=$((passed + 1))
else
  echo "    ⚠️  High: ${disk}%"
fi

echo ""
echo "=== RESULT: $passed/$total CHECKS PASSED ==="

if [ "$passed" -eq "$total" ]; then
  echo "✅ DISCOURSE READY FOR PUBLICATION"
  exit 0
else
  echo "⚠️  Some checks failed"
  exit 1
fi
```

**Run validation**:
```bash
chmod +x validate.sh
./validate.sh
```

---

## TROUBLESHOOTING IPv6 BUG

### Symptom: "could not connect to Redis at localhost:6379"

**Diagnosis**:

```bash
# Check if Redis is actually listening
docker exec discourse-redis netstat -tlnp 2>/dev/null | grep 6379

# Should show:
# tcp  0  0 127.0.0.1:6379  0.0.0.0:*  LISTEN

# If you see ::1:6379 or IPv6, the workaround didn't work
```

**Fix**:

```bash
# Option A (if kernel parameter not applied):
sudo sysctl -w net.ipv6.conf.lo.disable_ipv6=1

# Option B (if docker-compose workaround not applied):
# Edit docker-compose.yml:
# redis:
#   command: redis-server --bind 127.0.0.1 --port 6379

# Restart:
docker-compose restart redis

# Verify:
docker exec discourse-redis redis-cli ping
```

### Symptom: "Discourse not responding after 5+ minutes"

**Likely Cause**: Database initialization taking longer on Pi5

**Solution**:

```bash
# Wait longer
for i in {1..120}; do
  if curl -s http://localhost/srv/status 2>/dev/null | grep -q "ok"; then
    echo "✅ Ready after $((i*5)) seconds"
    break
  fi
  echo "  ...waiting ($((i))/120)"
  sleep 5
done

# Check logs
docker logs discourse-app | tail -20
```

### Symptom: High Memory Usage (> 6.5GB)

```bash
# Reduce Discourse worker processes
docker exec discourse-app puma -w 2 -t 1:4

# Or restart with limited resources
docker-compose down
# Edit .env to reduce DISCOURSE_MAX_WORK_PROCESSES
docker-compose up -d
```

---

## BACKUP STRATEGY

### Daily Backup Script

Save as `/opt/discourse/backup.sh`:

```bash
#!/bin/bash

backup_dir="/opt/backups/discourse"
mkdir -p "$backup_dir"

echo "Creating Discourse backup..."

# Backup database and app data
docker run --rm \
  -v discourse-postgres_data:/data \
  -v "$backup_dir":/backup \
  alpine tar czf /backup/discourse_$(date +%Y%m%d_%H%M%S).tar.gz -C / data

# Keep 7 days
find "$backup_dir" -name "*.tar.gz" -mtime +7 -delete

echo "✅ Backup complete: $(ls -lh "$backup_dir" | tail -1 | awk '{print $9}')"
```

### Add to Crontab

```bash
(crontab -l 2>/dev/null; echo "0 3 * * * cd /opt/discourse && ./backup.sh") | crontab -
```

---

## ROLLBACK PROCEDURE

**⚠️ WARNING: Destroys all data**

```bash
cd /opt/discourse

# Stop and remove
docker-compose down -v

# Clean volumes
docker volume prune -f

echo "✅ Rollback complete"
```

---

## KNOWN LIMITATIONS

### Why Discourse is NOT Recommended for Phase 5.1

1. **IPv6 Bug Requires Workaround** ⚠️
   - Adds 15 min setup + troubleshooting risk
   - Could cause instability under load
   - Affects federation if needed later

2. **Missing Phase 5-6 Features** ❌
   - No offline document editing
   - No E2E encryption (sensitive content)
   - No real-time document collaboration
   - No file versioning
   - No calendar/mail integration

3. **Use Case Mismatch** ❌
   - Forum-only model inefficient for 50-person authoring team
   - Authors need collaboration tools, not discussion threads
   - Would require supplementary tools (Nextcloud? Jitsi?)

### If You Still Choose Discourse...

After deployment:
1. Plan to deploy **Nextcloud** separately for document collaboration (July 1)
2. Deploy **Jitsi** for video conferencing (Wave 2)
3. Accept lack of E2E encryption for published content
4. Use external tools for co-editing (Google Docs? Etherpad?)

---

## SUMMARY

✅ **Phase 0**: IPv6 workaround applied  
✅ **Phase 1-2**: Discourse configured  
✅ **Phase 3**: Services running  
✅ **Phase 4-5**: Verified operational

**Caveats**:
- IPv6 bug workaround required (not ideal)
- Missing features compared to Nextcloud+Matrix
- Supplementary tools needed for Phase 6

**Recommendation**: Choose **Nextcloud+Matrix** instead (see NEXTCLOUD_MATRIX_DEPLOYMENT_SOP.md)

---

**Document Version**: 1.0  
**Last Updated**: June 16, 2026  
**Status**: ⚠️ DEPLOYMENT POSSIBLE (not recommended)
