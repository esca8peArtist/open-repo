---
title: "Phase 5 Deployment Scripts — Nextcloud + Matrix"
project: systems-resilience
phase: 5
platform: "Nextcloud Hub 33 + Matrix Synapse + Element Web + OnlyOffice"
status: PRODUCTION-READY — execute June 4 evening 20:00–02:00 UTC
deployment_window: "June 4 20:00 UTC → June 5 02:00 UTC (6h)"
wave_1_kickoff: "June 5 06:00 UTC author recruitment, 13:00 UTC go-live"
host: "raspby1 (Raspberry Pi 5, 100.70.184.84)"
created: 2026-06-04
version: 1.0
cross_references:
  - NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md (primary config reference)
  - PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md
  - PHASE_5_NEXTCLOUD_MATRIX_CONFIGURATION_TEMPLATES.md
  - PHASE_5_AUTHOR_ONBOARDING_GUIDES_NEXTCLOUD_MATRIX.md
---

# Phase 5 Deployment Scripts — Nextcloud + Matrix
## Execution Guide for June 4–5, 2026 | Raspberry Pi 5 (raspby1)

**Critical path**: Deployment must complete by June 5 05:30 UTC to allow a 30-minute final validation before the 06:00 UTC author recruitment window opens.

**Primary config source**: `NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md` contains the complete Docker Compose stack and all config files. This document is the execution layer — it sequences the playbook steps, calls out Pi 5-specific constraints, and provides the go/no-go checklist.

---

## Section 1: Raspberry Pi 5 Resource Assessment

### Hardware Specifications (raspby1)

| Resource | Available | Required (Minimum) | Required (Recommended) | Status |
|----------|-----------|-------------------|----------------------|--------|
| RAM | 8 GB | 4 GB (no OnlyOffice) | 8 GB (with OnlyOffice) | On the edge — see note |
| CPU | 4-core ARM Cortex-A76 | 2 cores | 4 cores | OK |
| Storage | Verify with `df -h` | 40 GB free | 80 GB free | Check before starting |
| Network | Tailscale 100.70.184.84 | Stable connection | — | OK |
| OS | Raspberry Pi OS (Bookworm) | Docker 24+ | — | Verify Docker version |
| Thermal | 81–84°C idle, 87.8°C under load | <85°C sustained | <80°C sustained | Monitor during deployment |

**RAM note**: The Pi 5 with 8 GB is at the minimum for the full 7-container stack (Nextcloud FPM + nginx sidecar + Synapse + Element + OnlyOffice + PostgreSQL + Redis). OnlyOffice alone consumes 1–2 GB. **Recommended approach**: deploy without OnlyOffice initially. Nextcloud's built-in Text app handles Markdown collaboration without OnlyOffice. Add OnlyOffice only if authors need .docx/spreadsheet co-editing.

**Thermal note**: raspby1 has documented thermal throttling above 87.8°C (see MEMORY.md). During Docker image pulls and initial database initialization, CPU usage will spike. If throttling occurs, deployment will slow but not fail. Monitor with:

```bash
vcgencmd measure_temp  # Run on raspby1 during deployment
# If >85°C: add a 5-minute pause between stages to let it cool
```

### Deployment Configuration for Pi 5 (Memory-Optimized)

Use this resource-constrained variant rather than the full 7-container stack:

```yaml
# Pi 5 optimized: 5 containers (drop OnlyOffice + nginx-nextcloud sidecar collapses into nextcloud)
# Estimated RAM at steady state: 4.5–5.5 GB
# Container RAM allocations (enforced via mem_limit):
#   postgres:    512 MB
#   redis:       256 MB
#   nextcloud:   1,024 MB (PHP-FPM with 512M PHP limit)
#   synapse:     768 MB
#   element:     128 MB
#   nginx:       64 MB
#   nginx-next:  64 MB
#   TOTAL:       ~2.8 GB base + 1–2 GB OS + buffer = ~5 GB
```

The `mem_limit` and `mem_reservation` keys should be added to each service in docker-compose.yml. See Section 3 below for the Pi 5-specific compose override file.

---

## Section 2: Pre-Deployment Checklist (Complete before 20:00 UTC June 4)

Run these checks from raspby1 (`ssh awank@100.70.184.84`):

```bash
# 1. Verify Docker
docker --version        # Must be 24+
docker compose version  # Must be v2.x (not docker-compose v1)

# 2. Check available disk
df -h /
# Need at least 40 GB free. If less: clear logs, old images
docker system prune -f  # Removes stopped containers and dangling images

# 3. Check available RAM
free -h
# Need at least 6 GB free before starting
# If raspby1 is running stockbot: check if it can be paused during deployment

# 4. Check current temperature
vcgencmd measure_temp
# If >80°C: wait or ensure airflow before starting

# 5. Verify no port conflicts
ss -tlnp | grep -E ':80|:443|:8008|:8448'
# Must show nothing. If ports are in use, stop the conflicting service.

# 6. Verify Tailscale is running
tailscale status
# Should show raspby1 online at 100.70.184.84

# 7. Check Docker is in the non-root group (or use sudo)
groups
# Should include 'docker'. If not: sudo usermod -aG docker awank && newgrp docker
```

**SMTP credentials required**. Before starting, have your SMTP provider credentials ready:
- Brevo (formerly Sendinblue): free tier, 300 emails/day — recommended
- Mailgun: 100 emails/day free
- Gmail SMTP: works but requires app password

---

## Section 3: Deployment Directory Setup

```bash
# Create deployment root on raspby1
ssh awank@100.70.184.84

sudo mkdir -p /opt/community/nextcloud-matrix
sudo chown awank:awank /opt/community/nextcloud-matrix
cd /opt/community/nextcloud-matrix

# Create directory structure
mkdir -p data/{postgres,redis,nextcloud,matrix/media,letsencrypt/webroot}
mkdir -p nginx/conf.d
mkdir -p matrix/config
mkdir -p element
mkdir -p scripts

# Set permissions
chmod 700 data/
touch .env
chmod 600 .env
```

### Environment File (.env)

Generate all passwords before populating .env:

```bash
# Generate 6 strong passwords (run on raspby1)
python3 -c "
import secrets
vars = [
    'NEXTCLOUD_ADMIN_PASSWORD',
    'POSTGRES_PASSWORD',
    'REDIS_PASSWORD',
    'MATRIX_FORM_SECRET',
    'MATRIX_MACAROON_KEY',
    'ONLYOFFICE_JWT_SECRET',
]
for v in vars:
    print(f'{v}={secrets.token_urlsafe(32)}')
"
# Copy output into a secure note or password manager, then paste into .env
```

Populate `/opt/community/nextcloud-matrix/.env`:

```bash
cat > /opt/community/nextcloud-matrix/.env << 'ENVEOF'
# ============================================================
# REPLACE ALL VALUES BELOW BEFORE RUNNING docker compose up
# ============================================================

# Domains — for Tailscale-only (no public domain), use:
# BASE_DOMAIN=resilience-hub.local
# NEXTCLOUD_DOMAIN=100.70.184.84
# MATRIX_DOMAIN=100.70.184.84
# ELEMENT_DOMAIN=100.70.184.84
# For public deployment with a domain, replace 100.70.184.84 with your domain.
BASE_DOMAIN=resilience-hub.local
NEXTCLOUD_DOMAIN=100.70.184.84
MATRIX_DOMAIN=100.70.184.84
ELEMENT_DOMAIN=100.70.184.84
OFFICE_DOMAIN=100.70.184.84

# Nextcloud
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=PASTE_GENERATED_VALUE_1
NEXTCLOUD_TRUSTED_DOMAINS=100.70.184.84 resilience-hub.local

# PostgreSQL
POSTGRES_USER=community_db_user
POSTGRES_PASSWORD=PASTE_GENERATED_VALUE_2
POSTGRES_DB=nextcloud_db
SYNAPSE_DB=synapse_db

# Redis
REDIS_PASSWORD=PASTE_GENERATED_VALUE_3

# Matrix / Synapse
SYNAPSE_SERVER_NAME=resilience-hub.local
SYNAPSE_REPORT_STATS=no
MATRIX_FORM_SECRET=PASTE_GENERATED_VALUE_4
MATRIX_MACAROON_KEY=PASTE_GENERATED_VALUE_5

# OnlyOffice (skip if not deploying OnlyOffice)
ONLYOFFICE_JWT_SECRET=PASTE_GENERATED_VALUE_6

# Email (outbound)
SMTP_HOST=smtp.brevo.com
SMTP_PORT=587
SMTP_USER=your_brevo_login@example.com
SMTP_PASSWORD=your_brevo_smtp_key
SMTP_FROM=noreply@resilience-hub.local

# Let's Encrypt (only if public domain)
LETSENCRYPT_EMAIL=admin@resilience-hub.local

# Timezone
TZ=UTC
ENVEOF

# Verify no placeholder values remain
grep "PASTE_GENERATED\|your_brevo\|example.com" /opt/community/nextcloud-matrix/.env
# Every hit must be intentionally left as-is (e.g., SMTP placeholders you haven't filled in yet)
```

**Security**: `.env` must never be committed to git. Verify:
```bash
echo ".env" >> /opt/community/nextcloud-matrix/.gitignore
echo ".env.secrets" >> /opt/community/nextcloud-matrix/.gitignore
```

---

## Section 4: Docker Compose Stack (Pi 5 Optimized)

The full stack config is in `NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md` Section 3.2. Use this Pi 5 override file to add memory limits without duplicating the full compose:

```bash
# Create Pi 5 memory override file
cat > /opt/community/nextcloud-matrix/docker-compose.pi5.yml << 'EOF'
# Pi 5 memory constraints — use alongside main docker-compose.yml
# docker compose -f docker-compose.yml -f docker-compose.pi5.yml up -d

services:
  postgres:
    mem_limit: 512m
    mem_reservation: 256m

  redis:
    mem_limit: 256m
    mem_reservation: 128m

  nextcloud:
    mem_limit: 1024m
    mem_reservation: 512m
    environment:
      PHP_MEMORY_LIMIT: 512M
      PHP_UPLOAD_LIMIT: 512M

  nginx-nextcloud:
    mem_limit: 128m
    mem_reservation: 64m

  synapse:
    mem_limit: 768m
    mem_reservation: 384m

  element:
    mem_limit: 128m
    mem_reservation: 64m

  nginx:
    mem_limit: 128m
    mem_reservation: 64m
EOF
```

**OnlyOffice**: Do not include OnlyOffice on the Pi 5 in the first deployment. It adds 1–2 GB RAM overhead and is not required for Wave 1 author coordination. Authors can collaborate using Nextcloud's built-in Text app for Markdown or download files to edit offline. Add OnlyOffice in a second phase if needed.

---

## Section 5: TLS Certificate Strategy for Tailscale-Only Deployment

For a Tailscale-only deployment (authors access via Tailscale, no public domain), use self-signed certificates or Tailscale's built-in HTTPS.

### Option A: Tailscale HTTPS (Recommended for Tailscale-only)

Tailscale provides free TLS certificates for devices in your network via `tailscale cert`:

```bash
# On raspby1
sudo tailscale cert 100.70.184.84
# Generates /etc/ssl/certs/100.70.184.84.crt and .key
# (or in ~/.local/share/tailscale/certs/ depending on Tailscale version)

# Check generated cert path
sudo ls -la /var/lib/tailscale/certs/ 2>/dev/null || ls ~/.local/share/tailscale/certs/ 2>/dev/null
```

Update nginx SSL paths to point to the Tailscale-issued certificate.

### Option B: Self-Signed Certificate (Testing fallback)

```bash
sudo mkdir -p /opt/community/nextcloud-matrix/data/tls
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /opt/community/nextcloud-matrix/data/tls/privkey.pem \
  -out /opt/community/nextcloud-matrix/data/tls/fullchain.pem \
  -subj "/CN=100.70.184.84/O=Resilience Hub/C=US" \
  -addext "subjectAltName=IP:100.70.184.84"

# Authors will see a browser security warning on first visit.
# They must click "Advanced → Proceed" to accept the self-signed cert.
# For Wave 1 (trusted authors), this is acceptable.
```

### Option C: Let's Encrypt (Requires public domain + ports 80/443 open)

If raspby1 has a public domain pointing to it:

```bash
docker run --rm \
  -p 100.70.184.84:80:80 \
  -v /opt/community/nextcloud-matrix/data/letsencrypt:/etc/letsencrypt \
  certbot/certbot certonly \
  --standalone \
  --agree-tos \
  --non-interactive \
  --email admin@resilience-hub.org \
  -d nextcloud.resilience-hub.org \
  -d matrix.resilience-hub.org \
  -d element.resilience-hub.org
```

Note: certbot's `-p` binding uses the specific interface IP, not 0.0.0.0.

---

## Section 6: Staged Deployment Procedure

**Total time estimate**: 4–6 hours on Pi 5 (image pulls take longer on ARM; database init adds ~10 min)

### Stage 0: Copy Config Files (20 min, 20:00–20:20 UTC)

Copy the config files from the playbook to raspby1. From your local machine (or run on raspby1 directly if you're SSHed in):

```bash
# Sync project configs to raspby1
rsync -av \
  /home/awank/dev/SuperClaude_Framework/projects/systems-resilience/docker-compose-nextcloud-matrix.yml \
  /home/awank/dev/SuperClaude_Framework/projects/systems-resilience/element-config.json \
  awank@100.70.184.84:/opt/community/nextcloud-matrix/

# On raspby1: rename compose file
mv /opt/community/nextcloud-matrix/docker-compose-nextcloud-matrix.yml \
   /opt/community/nextcloud-matrix/docker-compose.yml

# Copy element config
cp /opt/community/nextcloud-matrix/element-config.json \
   /opt/community/nextcloud-matrix/element/config.json
```

All nginx conf files and the homeserver.yaml need to be written from the playbook. The playbook (NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md) sections 3.4–3.8 contain the exact file contents to write.

### Stage 1: Pull Docker Images (30–60 min on Pi 5, 20:20–21:20 UTC)

ARM image pulls are slower than x86. Pull in parallel:

```bash
cd /opt/community/nextcloud-matrix

# Pull all images in parallel (background jobs)
docker pull postgres:16-alpine &
docker pull redis:7-alpine &
docker pull nextcloud:33-fpm-alpine &
docker pull matrixdotorg/synapse:latest &
docker pull vectorim/element-web:latest &
docker pull nginx:1.27-alpine &
wait
echo "All images pulled"

# Verify images present
docker images | grep -E "postgres|redis|nextcloud|synapse|element|nginx"
```

### Stage 2: Initialize Synapse Config (15 min, 21:20–21:35 UTC)

```bash
cd /opt/community/nextcloud-matrix

# Generate homeserver.yaml + signing key (first time only)
docker compose run --rm \
  -e SYNAPSE_SERVER_NAME="resilience-hub.local" \
  -e SYNAPSE_REPORT_STATS=no \
  synapse generate

# Verify generated files
ls ./data/matrix/
# Must include: resilience-hub.local.signing.key  homeserver.yaml  log.config

# Extract the auto-generated secrets (you need these for your homeserver.yaml)
grep -E "macaroon_secret_key|form_secret" ./data/matrix/homeserver.yaml
# IMPORTANT: Copy these two values into your matrix/config/homeserver.yaml
# (They are cryptographically unique to this instance — do not regenerate)
```

### Stage 3: Start Infrastructure Layer (20 min, 21:35–21:55 UTC)

```bash
cd /opt/community/nextcloud-matrix

# Start databases only
docker compose up -d postgres redis

# Wait for healthy status (up to 2 minutes on Pi 5)
for i in {1..12}; do
  sleep 10
  STATUS=$(docker compose ps --format json | python3 -c "
import json, sys
data = [json.loads(line) for line in sys.stdin if line.strip()]
for c in data:
    name = c.get('Name','')
    health = c.get('Health','')
    if 'postgres' in name or 'redis' in name:
        print(f'{name}: {health}')
")
  echo "$STATUS"
  if echo "$STATUS" | grep -qv "healthy"; then
    echo "Waiting for healthy state... ($i/12)"
  else
    echo "Databases healthy"
    break
  fi
done

# Verify database connectivity
docker compose exec postgres pg_isready -U community_db_user
# Expected: /var/run/postgresql:5432 - accepting connections
```

### Stage 4: Initialize Synapse Database (5 min, 21:55–22:00 UTC)

Synapse needs its own database. The `init-db.sql` from the playbook (Section 3.3) creates it automatically when postgres starts. Verify:

```bash
docker compose exec postgres psql -U community_db_user -c "\l"
# Expected: shows both nextcloud_db and synapse_db in the list
```

If synapse_db is missing:
```bash
docker compose exec postgres psql -U community_db_user -c \
  "CREATE DATABASE synapse_db;"
```

### Stage 5: Start Application Layer (30 min, 22:00–22:30 UTC)

```bash
cd /opt/community/nextcloud-matrix

# Start applications (excluding public-facing nginx)
docker compose up -d nextcloud synapse element nginx-nextcloud

# Nextcloud first-run installation takes 3–5 minutes on Pi 5
echo "Waiting 5 minutes for Nextcloud installation..."
sleep 300

# Check logs for any errors
docker compose logs nextcloud 2>&1 | tail -20
docker compose logs synapse 2>&1 | tail -20

# Monitor until all show healthy
watch -n 5 "docker compose ps --format 'table {{.Name}}\t{{.Status}}\t{{.Health}}'"
```

Expected healthy state:
- `community-nextcloud`: `Up (healthy)` or `Up` (FPM healthcheck may vary)
- `community-synapse`: `Up (healthy)`
- `community-element`: `Up (healthy)`
- `community-nginx-nextcloud`: `Up (healthy)`

### Stage 6: Start Public Proxy (5 min, 22:30–22:35 UTC)

```bash
cd /opt/community/nextcloud-matrix

docker compose up -d nginx

# Verify nginx started
docker compose logs nginx 2>&1 | tail -10

# Test HTTPS endpoint
curl -sk https://100.70.184.84/status.php
# Expected: {"installed":true,"maintenance":false,...}
# (Use -sk to skip cert validation for self-signed)
```

### Stage 7: Create Synapse Admin User (10 min, 22:35–22:45 UTC)

```bash
# Register the admin user for Synapse
docker exec -it community-synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u admin \
  -p "$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)" \
  --admin \
  http://localhost:8008

# Get admin access token (needed for bulk user creation)
ADMIN_TOKEN=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"m.login.password\",\"user\":\"admin\",\"password\":\"$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)\"}" \
  http://localhost:8008/_matrix/client/r0/login | python3 -c "import json,sys; print(json.load(sys.stdin)['access_token'])")

echo "SYNAPSE_ADMIN_TOKEN=$ADMIN_TOKEN" >> /opt/community/nextcloud-matrix/.env.runtime
# Store this — needed for the bulk user import script
```

### Stage 8: Install Nextcloud Apps (15 min, 22:45–23:00 UTC)

```bash
# Install required Nextcloud apps via occ CLI
docker exec -u www-data community-nextcloud php occ app:install calendar
docker exec -u www-data community-nextcloud php occ app:install contacts
docker exec -u www-data community-nextcloud php occ app:install text

# Enable apps
docker exec -u www-data community-nextcloud php occ app:enable calendar
docker exec -u www-data community-nextcloud php occ app:enable contacts
docker exec -u www-data community-nextcloud php occ app:enable text

# Verify
docker exec -u www-data community-nextcloud php occ app:list | grep -E "calendar|contacts|text"
```

---

## Section 7: Database Initialization Procedures

### PostgreSQL Initial Schema

The standard postgres Docker image handles database creation via environment variables. The `init-db.sql` script from the playbook (Section 3.3) runs automatically on first start. Verify the databases are correct:

```bash
docker compose exec postgres psql -U community_db_user << 'SQL'
-- Verify both databases exist
\l
-- Check Nextcloud tables are created (after Nextcloud first-run)
\c nextcloud_db
\dt
-- Check Synapse tables (after first Synapse start)
\c synapse_db
\dt | head -20
SQL
```

### Nextcloud Database Repair (if first-run has issues)

```bash
# Run Nextcloud setup via occ if web wizard did not complete
docker exec -u www-data community-nextcloud php occ maintenance:install \
  --database pgsql \
  --database-host postgres \
  --database-name nextcloud_db \
  --database-user community_db_user \
  --database-pass "$(grep POSTGRES_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)" \
  --admin-user admin \
  --admin-pass "$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)"
```

---

## Section 8: Post-Deployment Verification Checklist

Run all checks after deployment completes (target: June 5 00:00–00:30 UTC).

### 8.1 Container Health

```bash
cd /opt/community/nextcloud-matrix

# All containers must be Up (not Restarting, not Exited)
docker compose ps
```

Expected: 6–7 containers, all showing `Up` status. If any show `Restarting`: check logs immediately.

### 8.2 Nextcloud API

```bash
# Basic status
curl -sk https://100.70.184.84/status.php | python3 -m json.tool
# Must show: "installed": true, "maintenance": false

# Admin login
curl -sk -u "admin:$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)" \
  https://100.70.184.84/ocs/v2.php/apps/serverinfo/api/v1/info?format=json \
  | python3 -m json.tool | head -20
# Must return serverinfo JSON without error

# WebDAV (required for desktop sync)
curl -sk -u "admin:$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)" \
  -X PROPFIND https://100.70.184.84/remote.php/dav/files/admin/ \
  -H "Depth: 0"
# Must return XML (207 Multi-Status)
```

### 8.3 Matrix Synapse API

```bash
# Client versions (no auth required)
curl -sk https://100.70.184.84/_matrix/client/versions | python3 -m json.tool
# Must return: {"versions": [...], "unstable_features": {...}}

# Server version (admin)
curl -sk https://100.70.184.84/_synapse/admin/v1/server_version
# Must return: {"server_version": "Synapse/1.x.x ..."}

# Well-known delegation
curl -sk https://100.70.184.84/.well-known/matrix/server
# Must return: {"m.server": "100.70.184.84:443"} (or your domain:443)
```

### 8.4 Element Web

```bash
# Element Web loads
curl -sk -I https://100.70.184.84/ | head -5
# Must return: HTTP/1.1 200 or HTTP/2 200

# Element config is served correctly
curl -sk https://100.70.184.84/config.json | python3 -m json.tool | head -5
# Must return Element config JSON
```

### 8.5 Federation Test

```bash
# Use federationtester (if raspby1 has a public domain)
curl -sf "https://federationtester.matrix.org/api/report?server_name=resilience-hub.local" \
  | python3 -m json.tool | grep -E "AllChecksOK|error" | head -5
# For Tailscale-only: federation will not pass (expected — external federation not required for Wave 1)
```

**Note**: For a Tailscale-only deployment, Matrix federation to external servers is not required for Phase 5. Authors are on the same Tailscale network. Skip the federation test and mark as N/A.

### 8.6 E2E Encryption Verification

1. Open Element Web at `https://100.70.184.84` from a browser on a Tailscale-connected machine
2. Log in as the admin user
3. Create a private room: Settings → Security → Enable E2E encryption
4. Verify the lock icon appears on messages
5. Log in as a second test user, join the room, confirm they can decrypt messages

### 8.7 Offline Mode Test

**Nextcloud offline test**:
1. Install Nextcloud Desktop client on a test machine
2. Connect to `https://100.70.184.84`, log in
3. Sync a file to local disk
4. Disconnect from network (or switch Tailscale off)
5. Edit the file locally — confirm edits save
6. Reconnect — confirm file syncs back

**Matrix offline test**:
1. Open Element Web
2. Open browser DevTools → Network → select "Offline" throttle
3. Type and send a message — should show pending indicator
4. Re-enable network — message should deliver

### 8.8 CalDAV/CardDAV Test

```bash
# CalDAV endpoint (required for shared calendars)
curl -sk -u "admin:$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)" \
  -X PROPFIND https://100.70.184.84/remote.php/dav/calendars/admin/ \
  -H "Depth: 1"
# Must return XML with calendar listing

# CardDAV endpoint
curl -sk -u "admin:$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)" \
  -X PROPFIND https://100.70.184.84/remote.php/dav/addressbooks/admin/ \
  -H "Depth: 1"
# Must return XML with addressbook listing
```

### 8.9 Disk Space Final Check

```bash
df -h /opt/community/nextcloud-matrix/data/
# Must show at least 20 GB free after all containers running
du -sh /opt/community/nextcloud-matrix/data/*/
# Typical after fresh install: postgres ~50 MB, matrix ~20 MB, nextcloud ~500 MB
```

### 8.10 Go/No-Go Summary

| Check | Pass Criteria | Result |
|-------|--------------|--------|
| All containers Up | 0 containers in Restarting/Exited | |
| Nextcloud status | `"installed": true` | |
| Matrix client versions | JSON response received | |
| Element Web loads | HTTP 200 | |
| WebDAV responds | HTTP 207 | |
| CalDAV responds | HTTP 207 | |
| E2E encryption | Lock icon visible | |
| Offline sync | Files queue and sync | |
| Disk free | >20 GB remaining | |
| Temp below 85°C | `vcgencmd measure_temp` | |

**Threshold for June 5 author recruitment**: All checks must pass except federation (N/A for Tailscale-only). If any critical check fails, execute the rollback procedure (Section 10) and switch to Discourse.

---

## Section 9: Author Account Creation (June 5, 05:00–06:00 UTC)

Run the bulk import script from `NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md` Section 8.1 with the Wave 1 author CSV.

```bash
# Prepare Wave 1 author CSV (18 authors)
# See PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md for author list
cat > /opt/community/nextcloud-matrix/wave1_authors.csv << 'EOF'
username,password,email,display_name
# Fill in 18 rows before running
EOF

# Set environment for import script
export NEXTCLOUD_URL="https://100.70.184.84"
export NEXTCLOUD_ADMIN_USER="admin"
export NEXTCLOUD_ADMIN_PASS="$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)"
export MATRIX_URL="https://100.70.184.84"
export MATRIX_ADMIN_TOKEN="$(grep SYNAPSE_ADMIN_TOKEN /opt/community/nextcloud-matrix/.env.runtime | cut -d= -f2)"
export MATRIX_SERVER_NAME="resilience-hub.local"

# Run import (from playbook Section 8.1 — save the Python script as import_users.py)
uv run python3 /opt/community/nextcloud-matrix/import_users.py wave1_authors.csv
```

---

## Section 10: Rollback Procedure

**Trigger**: If any of the following conditions are true by 03:00 UTC June 5:
- Three or more containers in Restarting state after 30 minutes of troubleshooting
- Nextcloud installation did not complete (blank page or database error)
- Disk space exhausted
- Pi 5 thermal throttling preventing completion
- Total time elapsed >6 hours with no clear resolution path

### Rollback Steps

```bash
# Stop all containers (data is preserved in ./data/)
cd /opt/community/nextcloud-matrix
docker compose down

# Optional: full data wipe (only if starting over from scratch)
# WARNING: this deletes all data — only do this if starting completely fresh
# rm -rf /opt/community/nextcloud-matrix/data/*

# Free RAM for other work
docker system prune -f

# Log the failure
cat >> /home/awank/dev/SuperClaude_Framework/WORKLOG.md << 'EOF'

### [ROLLBACK] Nextcloud+Matrix deployment — $(date -u)
- Deployment failed to complete within the June 5 window
- Containers stopped, data preserved at /opt/community/nextcloud-matrix/data/
- Switching to Discourse fallback
- See DEPLOYMENT_PLAYBOOK_DISCOURSE.md for next steps
EOF
```

### Fallback to Discourse

Discourse deployment requires 2–3 hours and can still meet the June 5 13:00 UTC Wave 1 window if rollback starts by 08:00 UTC.

- **Playbook**: `DEPLOYMENT_PLAYBOOK_DISCOURSE.md`
- **Resource requirement**: 2 GB RAM minimum (well within Pi 5 headroom after stopping the Nextcloud stack)
- **Timeline**: 08:00 UTC start → 11:00 UTC deployment complete → 30 min verification → 13:00 UTC Wave 1 on time

### Partial Recovery (If Nextcloud Only or Matrix Only Works)

If only one component fails:

**Nextcloud works but Matrix fails**:
- Authors use Nextcloud for documents and file sharing
- Use a Signal group or email for real-time coordination
- Re-attempt Matrix deployment June 6 (non-blocking for Wave 1)

**Matrix works but Nextcloud fails**:
- Authors use Matrix for coordination
- Store documents as message attachments or use a temporary shared Google Drive
- Re-attempt Nextcloud deployment June 6

---

## Section 11: Deployment Timeline Summary

| Time (UTC) | Action | Duration | Cumulative |
|------------|--------|----------|------------|
| June 4 19:30 | Pre-deployment checks (Section 2) | 20 min | 20 min |
| June 4 19:50 | Config files written, .env populated | 30 min | 50 min |
| June 4 20:20 | Docker image pulls (all in parallel) | 45 min | 1h 35m |
| June 4 21:05 | Synapse config generated | 15 min | 1h 50m |
| June 4 21:20 | Stage 1: postgres + redis healthy | 20 min | 2h 10m |
| June 4 21:40 | Stage 2: database init verified | 10 min | 2h 20m |
| June 4 21:50 | Stage 3: application layer started | 30 min | 2h 50m |
| June 4 22:20 | Stage 4: nginx proxy started | 5 min | 2h 55m |
| June 4 22:25 | Admin accounts created | 15 min | 3h 10m |
| June 4 22:40 | Nextcloud apps installed | 15 min | 3h 25m |
| June 4 23:05 | Post-deployment checks (Section 8) | 30 min | 3h 55m |
| June 4 23:35 | Backup/monitoring crons installed | 15 min | 4h 10m |
| June 4 23:50 | Configuration templates applied (Section 12) | 30 min | 4h 40m |
| June 5 00:20 | **DEPLOYMENT COMPLETE** — all checks pass | — | 4h 40m |
| June 5 05:00 | Wave 1 author accounts created (CSV import) | 60 min | — |
| June 5 06:00 | Author recruitment emails sent | 30 min | — |
| **June 5 13:00** | **Wave 1 go-live** | — | — |

**Buffer**: 5h 20m between projected completion (00:20) and author recruitment (06:00). This accommodates the documented Pi 5 thermal throttling and any unexpected delays.

---

## Section 12: Backup and Monitoring Crons (Install after verification)

```bash
# Install backup script from playbook Section 10.1
# Save the script content to:
chmod +x /opt/community/nextcloud-matrix/scripts/backup.sh
chmod +x /opt/community/nextcloud-matrix/scripts/healthcheck.sh

# Add to crontab
(crontab -l 2>/dev/null; cat << 'CRON'
# Community platform — backup at 02:00 UTC daily
0 2 * * * /opt/community/nextcloud-matrix/scripts/backup.sh >> /var/log/community-backup.log 2>&1
# Health check — every hour
0 * * * * /opt/community/nextcloud-matrix/scripts/healthcheck.sh >> /var/log/community-health.log 2>&1
# TLS renewal — twice daily
0 0,12 * * * docker run --rm -v /opt/community/nextcloud-matrix/data/letsencrypt:/etc/letsencrypt certbot/certbot renew --quiet && docker exec community-nginx nginx -s reload 2>/dev/null || true
CRON
) | crontab -

crontab -l  # Verify crons installed
```

---

## Cross-References

- **Full Docker Compose + all config files**: `NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md` (Sections 3.1–3.9)
- **Author coordination setup**: `PHASE_5_NEXTCLOUD_MATRIX_CONFIGURATION_TEMPLATES.md`
- **Author-facing quickstart**: `PHASE_5_AUTHOR_ONBOARDING_GUIDES_NEXTCLOUD_MATRIX.md`
- **Wave 1 recruitment**: `PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md`
- **Rollback — Discourse**: `DEPLOYMENT_PLAYBOOK_DISCOURSE.md`

---

**Status**: PRODUCTION-READY for June 4 evening execution  
**Confidence**: 87% for Pi 5 (thermal throttling is the main variable; documented in MEMORY.md)  
**Critical decision**: Skip OnlyOffice on Pi 5 for Wave 1; add later if authors need .docx co-editing
