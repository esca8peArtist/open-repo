---
title: "Phase 5 Deployment Checklist and User Onboarding"
project: systems-resilience
phase: 5
status: PRODUCTION-READY — June 5-15 deployment window
created: 2026-06-05
version: 1.0
cross_references:
  - PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP_v2.md
  - NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md
  - PHASE_5_MESHTASTIC_BRIDGE_CONTINGENCY.md
---

# Phase 5 Deployment Checklist and User Onboarding
## Pre-Deployment | 15-Step Runbook | Post-Deployment | Onboarding | Monitoring | Recovery

---

## Part 1: Pre-Deployment Verification (7 Steps)

Complete all 7 steps before running any Docker command. Estimated time: 30 minutes.

### Step 1 — Verify Host Infrastructure

```bash
# SSH into raspby1
ssh awank@100.70.184.84

# Docker version (must be Engine 24+, Compose v2)
docker --version
docker compose version
# Expected: Docker version 26.x, Docker Compose version v2.x

# Available RAM (need ≥ 3.5 GB free)
free -h
# MemAvailable row must show ≥ 3.5G

# Available disk (need ≥ 32 GB free)
df -h /
# Avail column must show ≥ 32G

# CPU temperature (Pi 5 — must be below 85°C)
vcgencmd measure_temp
# If ≥ 85°C, stop and add cooling before proceeding
```

- [ ] Docker Engine 24+ confirmed
- [ ] Compose v2 confirmed
- [ ] RAM: ≥ 3.5 GB available
- [ ] Disk: ≥ 32 GB free
- [ ] Temperature: < 85°C

### Step 2 — Verify Tailscale Connectivity

```bash
# On raspby1
tailscale status
# Confirm: raspby1 = 100.70.184.84 (self)
# Confirm: any author machines already on the network are listed

# On a remote machine, verify raspby1 is reachable
ping 100.70.184.84 -c 3
# Must succeed (3/3 packets received)
```

- [ ] Tailscale daemon running on raspby1
- [ ] raspby1 IP confirmed as 100.70.184.84
- [ ] Reachable from at least one remote machine

### Step 3 — Verify Credentials Are Ready

```bash
# Confirm .env exists and has no placeholders
cd /opt/community/nextcloud-matrix
[ -f .env ] && echo "EXISTS" || echo "MISSING — create from Section 3.1 of Roadmap"
grep "REPLACE_WITH" .env && echo "PLACEHOLDERS FOUND — fill in before proceeding" || echo "No placeholders: OK"

# Confirm .env permissions are restrictive
ls -la .env
# Must show: -rw------- (chmod 600)
```

- [ ] `.env` file exists
- [ ] Zero lines match "REPLACE_WITH"
- [ ] File permissions are 600

### Step 4 — Verify Configuration Files Are Present

```bash
cd /opt/community/nextcloud-matrix

for f in \
  docker-compose.yml \
  init-db.sql \
  element/config.json \
  matrix/config/homeserver.yaml \
  matrix/config/log.yaml \
  nginx/nginx.conf \
  nginx/conf.d/00-http.conf \
  nginx/conf.d/10-nextcloud.conf \
  nginx/conf.d/11-matrix.conf \
  nginx/conf.d/12-element.conf; do
    [ -f "$f" ] && echo "OK: $f" || echo "MISSING: $f"
done
```

- [ ] All 10 files present (0 MISSING lines in output)

### Step 5 — Verify TLS Certificates

```bash
cd /opt/community/nextcloud-matrix

# Self-signed (Tailscale-only deployment)
[ -f data/certs/fullchain.pem ] && [ -f data/certs/privkey.pem ] \
  && echo "TLS: OK" || echo "TLS: MISSING — generate certificates first (Section 3.7 of Roadmap)"

# Verify certificate is not expired
openssl x509 -in data/certs/fullchain.pem -noout -dates 2>/dev/null \
  && echo "Certificate dates checked" || echo "Cannot read certificate"
```

- [ ] `fullchain.pem` and `privkey.pem` present in `data/certs/`
- [ ] Certificate not expired (notAfter date is in the future)

### Step 6 — Validate Docker Compose Syntax

```bash
cd /opt/community/nextcloud-matrix
docker compose --env-file .env config > /dev/null && echo "Compose config: VALID" || echo "Compose config: INVALID — check docker-compose.yml"
```

- [ ] `docker compose config` exits without errors

### Step 7 — Verify SMTP Credentials (Optional but Recommended)

```bash
# Quick SMTP test using Python
python3 -c "
import os, smtplib
host = os.environ.get('SMTP_HOST', 'smtp.brevo.com')
port = int(os.environ.get('SMTP_PORT', 587))
user = os.environ.get('SMTP_USER', '')
pw   = os.environ.get('SMTP_PASSWORD', '')
try:
    s = smtplib.SMTP(host, port, timeout=10)
    s.starttls()
    s.login(user, pw)
    s.quit()
    print('SMTP: OK')
except Exception as e:
    print(f'SMTP: FAIL — {e}')
" 
```

- [ ] SMTP test passes (or documented as deferred — email is optional for Phase 5)

**Pre-deployment gate**: All 7 steps passing = proceed to deployment. Any MISSING or FAIL = stop and fix.

---

## Part 2: Deployment Runbook (15 Steps)

Estimated total time: 90–120 minutes. Steps are sequential; do not skip.

### Step 1 — Create Directory Structure

```bash
ssh awank@100.70.184.84
cd /opt/community/nextcloud-matrix

mkdir -p data/{postgres,redis,nextcloud,matrix/media}
mkdir -p data/certs
mkdir -p scripts
chmod 700 data/
echo "Directories created"
```

### Step 2 — Copy Configuration Files to Host

```bash
# If running from dev machine with files in git repo:
rsync -av \
  /home/awank/dev/SuperClaude_Framework/projects/systems-resilience/config/ \
  awank@100.70.184.84:/opt/community/nextcloud-matrix/

# Or: copy each file individually via scp/rsync as needed
# Verify all config files are in place (re-run Step 4 of pre-deployment)
```

### Step 3 — Pull Docker Images in Parallel

```bash
cd /opt/community/nextcloud-matrix

# Pull all images simultaneously (saves ~5 minutes)
docker pull postgres:16-alpine &
docker pull redis:7-alpine &
docker pull nextcloud:33-fpm-alpine &
docker pull matrixdotorg/synapse:latest &
docker pull vectorim/element-web:latest &
docker pull nginx:1.27-alpine &
wait

echo "All images pulled"
docker images | grep -E "postgres|redis|nextcloud|synapse|element|nginx"
```

### Step 4 — Initialize Synapse Configuration

```bash
cd /opt/community/nextcloud-matrix
source .env

# Generate Synapse signing key and base config (one-time only)
docker compose run --rm \
  -e SYNAPSE_SERVER_NAME="${SYNAPSE_SERVER_NAME}" \
  -e SYNAPSE_REPORT_STATS=no \
  synapse generate

# Extract the auto-generated secrets
echo "=== Copy these into matrix/config/homeserver.yaml ==="
grep -E "macaroon_secret_key|form_secret|signing_key_path" ./data/matrix/homeserver.yaml
```

Update `matrix/config/homeserver.yaml` with the extracted macaroon_secret_key and form_secret values. Then verify:

```bash
python3 -c "import yaml; yaml.safe_load(open('matrix/config/homeserver.yaml'))" \
  && echo "homeserver.yaml: VALID YAML" \
  || echo "homeserver.yaml: YAML SYNTAX ERROR"
```

### Step 5 — Start Infrastructure Layer (PostgreSQL + Redis)

```bash
cd /opt/community/nextcloud-matrix
docker compose --env-file .env up -d postgres redis

echo "Waiting 30s for databases to initialize..."
sleep 30

docker compose ps postgres redis
# Both must show: (healthy)
```

**Gate**: Do not proceed until both containers show `(healthy)`.

### Step 6 — Verify Database Initialization

```bash
# Check both databases exist
docker exec community-postgres psql -U community_user -c "\l" | grep -E "nextcloud_db|synapse_db"
# Must show both database names

# Check Synapse DB encoding (must be C locale)
docker exec community-postgres psql -U community_user -c \
  "SELECT datname, datctype FROM pg_database WHERE datname='synapse_db';"
# datctype must be 'C'
```

### Step 7 — Start Application Layer

```bash
cd /opt/community/nextcloud-matrix
docker compose --env-file .env up -d nextcloud synapse element

echo "Waiting 90s for applications to initialize..."
sleep 90

docker compose ps
# All three containers should show "Up" (healthy checks may take 2 more minutes)
```

### Step 8 — Start Reverse Proxy

```bash
cd /opt/community/nextcloud-matrix
docker compose --env-file .env up -d nginx

sleep 10
docker compose ps nginx
# nginx must show "Up" and "(healthy)"
```

### Step 9 — Full Stack Status Check

```bash
docker compose ps --format "table {{.Name}}\t{{.Status}}\t{{.Ports}}"
```

Expected output:
```
NAME                    STATUS              PORTS
community-nginx         Up (healthy)        127.0.0.1:80->80/tcp, 127.0.0.1:443->443/tcp
community-nextcloud     Up (healthy)
community-postgres      Up (healthy)
community-redis         Up (healthy)
community-synapse       Up (healthy)
community-element       Up (healthy)
```

**Gate**: All 6 containers Up. If any show "Restarting" or "Exit", check logs before proceeding.

### Step 10 — API Health Checks

```bash
source /opt/community/nextcloud-matrix/.env

# Test Nextcloud (via Tailscale or localhost)
curl -sk https://100.70.184.84/status.php | python3 -m json.tool
# Expected: "installed": true, "maintenance": false

# Test Matrix client API
curl -sk https://100.70.184.84/_matrix/client/versions | python3 -m json.tool
# Expected: versions array with r0.x and v1.x entries

# Test Element Web
curl -sk -I https://100.70.184.84:8443/ | head -3
# Expected: HTTP/1.1 200 or HTTP/2 200

echo "=== All API checks complete ==="
```

### Step 11 — Create Matrix Admin User

```bash
docker exec -it community-synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u admin \
  -p "SECURE_ADMIN_PASSWORD" \
  --admin \
  http://localhost:8008

echo "Matrix admin user created. Log in at Element Web to verify."
```

### Step 12 — Create Default Matrix Rooms

```bash
# Get admin access token
MATRIX_TOKEN=$(curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"type":"m.login.password","user":"admin","password":"ADMIN_PASSWORD"}' \
  http://localhost:8008/_matrix/client/r0/login \
  | python3 -c "import sys,json; print(json.load(sys.stdin)['access_token'])")

echo "Token obtained: ${MATRIX_TOKEN:0:20}..."

# Create coordination rooms
for room in "phase-5-general" "phase-5-feedback" "coordination" "technical"; do
  curl -s -X POST \
    -H "Authorization: Bearer $MATRIX_TOKEN" \
    -H "Content-Type: application/json" \
    -d "{\"name\":\"$room\",\"room_alias_name\":\"$room\",\"preset\":\"private_chat\",\"visibility\":\"private\"}" \
    http://localhost:8008/_matrix/client/v3/createRoom | python3 -m json.tool | grep room_id
done

echo "Default rooms created"
```

### Step 13 — Configure Nextcloud (Post-First-Run)

```bash
# Install required Nextcloud apps
for app in calendar contacts text twofactor_totp; do
  docker exec -u www-data community-nextcloud php occ app:enable $app
  echo "  Enabled: $app"
done

# Create editorial calendar
docker exec -u www-data community-nextcloud php occ \
  dav:create-calendar admin editorial-calendar "Phase 5 Editorial Calendar"

# Set file sharing policies (see Roadmap Section 4.2 for full config)
docker exec -u www-data community-nextcloud php occ config:app:set \
  core shareapi_default_expire_date --value="yes"
docker exec -u www-data community-nextcloud php occ config:app:set \
  core shareapi_expire_after_n_days --value="30"

echo "Nextcloud configured"
```

### Step 14 — Install Monitoring and Backup Crons

```bash
chmod +x /opt/community/nextcloud-matrix/scripts/backup.sh

# Add crons (backup at 02:00 UTC; healthcheck every hour)
(crontab -l 2>/dev/null; cat << 'CRONS'
0 2 * * * /opt/community/nextcloud-matrix/scripts/backup.sh >> /var/log/community-backup.log 2>&1
0 * * * * /opt/community/nextcloud-matrix/scripts/healthcheck.sh >> /var/log/community-health.log 2>&1
CRONS
) | crontab -

crontab -l | grep -E "backup|health"
echo "Crons installed"
```

### Step 15 — Final Log Review

```bash
# Check for errors across all containers
for container in community-postgres community-redis community-nextcloud \
                  community-synapse community-element community-nginx; do
  echo "=== $container (last 10 lines, errors only) ==="
  docker logs --tail=20 "$container" 2>&1 | grep -iE "error|fatal|exception|panic" | head -5
  echo ""
done

echo "=== Deployment complete at $(date -u) ==="
```

**Deployment complete gate**: Zero fatal/panic errors in any container log + all API checks passing (Step 10) = deployment successful.

---

## Part 3: Post-Deployment Verification (8 Steps)

Run these after deployment completes, before sending author invitations.

### Step 1 — Admin Access Verification

```bash
# Nextcloud: log in at https://100.70.184.84 with admin/ADMIN_PASSWORD
# Element Web: log in at https://100.70.184.84:8443 with @admin:resilience-hub.local
echo "Manual verification: open browser and log into both services"
```

- [ ] Nextcloud admin login successful
- [ ] Element Web login successful
- [ ] Matrix admin room visible in Element

### Step 2 — Create 5 Test Users and Verify Login

```bash
# Create 5 test Nextcloud users
for i in $(seq 1 5); do
  docker exec -u www-data community-nextcloud php occ user:add \
    --password-from-env \
    --display-name "Test User $i" \
    testuser0$i
  # Note: set OC_PASS env var first
done

# Create corresponding Matrix users
docker exec -it community-synapse register_new_matrix_user \
  -c /data/homeserver.yaml -u testuser01 -p TestPass123 --no-admin http://localhost:8008
```

- [ ] 5 test Nextcloud users created
- [ ] 5 test Matrix users created
- [ ] At least one test user can log into Nextcloud
- [ ] At least one test user can log into Element Web
- [ ] Test message sent and received in #phase-5-general room

### Step 3 — Calendar Sync Test

```bash
# Test CalDAV endpoint responds
curl -s -u admin:ADMIN_PASSWORD \
  -X PROPFIND \
  https://100.70.184.84/remote.php/dav/calendars/admin/editorial-calendar/ \
  -H "Depth: 0" | head -20
# Expected: XML response (207 Multi-Status)
```

- [ ] CalDAV endpoint responds with XML
- [ ] Editorial calendar appears in author's native calendar app (manual test)

### Step 4 — Offline Sync Test (Nextcloud)

1. Install Nextcloud Desktop Client on a test machine
2. Connect to `https://100.70.184.84` with a test user account
3. Sync a folder from Nextcloud
4. Disable network on the test machine
5. Edit a synced file
6. Re-enable network
7. Verify the edit syncs back to server

- [ ] Nextcloud Desktop Client syncs successfully
- [ ] File edited offline syncs on reconnection
- [ ] No sync conflict errors

### Step 5 — Offline Messaging Test (Element Web)

1. Log into Element Web with a test user
2. Join #phase-5-general room
3. Open browser Developer Tools → Network → set throttle to "Offline"
4. Type and attempt to send a message
5. Message should show a pending/clock indicator
6. Set throttle back to normal
7. Message should send within 3 seconds

- [ ] Message queues when offline (pending indicator visible)
- [ ] Message sends on reconnection

### Step 6 — Backup Script Test

```bash
/opt/community/nextcloud-matrix/scripts/backup.sh
# Should complete without errors

ls -lh /mnt/backup/community-platform/$(date +%Y-%m-%d)/
# Should show: nextcloud_db.sql.gz, synapse_db.sql.gz, nextcloud-data.tar.gz, matrix-data.tar.gz, config.tar.gz
```

- [ ] Backup script completes without errors
- [ ] All 5 backup files present
- [ ] Nextcloud exits maintenance mode after backup

### Step 7 — TLS Certificate Validation

```bash
# Check certificate expiry
openssl s_client -connect 100.70.184.84:443 -servername nextcloud.resilience-hub.local \
  </dev/null 2>/dev/null | openssl x509 -noout -dates
# notAfter must be at least 30 days in the future

# Auto-renewal cron present (for Let's Encrypt deployments)
crontab -l | grep certbot | wc -l
# Should be ≥ 1 if using Let's Encrypt
```

- [ ] Certificate valid for ≥ 30 days
- [ ] Auto-renewal cron installed (Let's Encrypt only)

### Step 8 — Security Binding Check

```bash
# Verify no services bind to 0.0.0.0
ss -tlnp | grep "0.0.0.0" | grep -v "127.0.0.1"
# Output must be EMPTY. Any line here is a violation of CLAUDE.md policy.

# Check docker ps for exposed ports
docker ps --format "{{.Names}}\t{{.Ports}}" | grep -v "127.0.0.1"
# Output must be EMPTY (all ports must show 127.0.0.1:PORT binding)
```

- [ ] Zero services bound to 0.0.0.0
- [ ] All Docker port bindings use 127.0.0.1

**Post-deployment gate**: All 8 steps passing = platform ready for author onboarding.

---

## Part 4: User Onboarding Guide (First 5-10 Users)

### 4.1 Author Account Creation (Batch)

Prepare a CSV with author details:

```csv
username,password,email,display_name
smith_jane,TempPass2026!,jane@example.com,Jane Smith
jones_bob,TempPass2026!,bob@example.com,Bob Jones
garcia_alex,TempPass2026!,alex@example.com,Alex Garcia
chen_wei,TempPass2026!,wei@example.com,Wei Chen
patel_priya,TempPass2026!,priya@example.com,Priya Patel
```

Run bulk creation:

```bash
# Using the import script from NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md Part 8
export NEXTCLOUD_ADMIN_PASS="$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)"
export MATRIX_ADMIN_TOKEN="syt_admin_..."
export NEXTCLOUD_URL="https://100.70.184.84"
export MATRIX_URL="http://localhost:8008"
export MATRIX_SERVER_NAME="resilience-hub.local"

python3 import_users.py wave1_authors.csv
```

### 4.2 Welcome Email Template

```
Subject: Your Phase 5 Collaboration Platform Access

Hello [NAME],

Your contributor account is ready. Here's everything you need:

--- FILE COLLABORATION (Nextcloud) ---
URL: https://100.70.184.84
Username: [USERNAME]
Temporary password: [PASSWORD]
Action: Change your password on first login.

Recommended: Install Nextcloud Desktop Client for offline access
  Download: https://nextcloud.com/install/#install-clients
  Server URL: https://100.70.184.84
  Once installed, mark your assigned folder as "Available offline"

--- COMMUNITY CHAT (Matrix/Element) ---
URL: https://100.70.184.84:8443
Username: @[USERNAME]:resilience-hub.local
Password: same as above (change it on first login)

Join these rooms after logging in:
  - #phase-5-general:resilience-hub.local
  - #phase-5-feedback:resilience-hub.local
  - #coordination:resilience-hub.local

--- CALENDAR ---
Your editorial calendar is shared in Nextcloud. To sync to your device:
  CalDAV URL: https://100.70.184.84/remote.php/dav/calendars/[USERNAME]/editorial-calendar/
  Username: [USERNAME] / Password: your Nextcloud password

--- FIRST STEPS ---
1. Log into Nextcloud and change your password
2. Log into Element with the same credentials
3. Post in #coordination: "[USERNAME] confirmed access"
4. Open your assigned document in Nextcloud and add a comment: "Ready"

Questions? Post in #technical:resilience-hub.local or reply to this email.

Welcome to the team.
```

### 4.3 Channel Creation Templates

Create these rooms in Matrix (via admin API or Element client) for Wave 1:

| Room Alias | Purpose | Access |
|-----------|---------|--------|
| `#phase-5-general` | General discussion, announcements | All Wave 1 authors |
| `#phase-5-feedback` | Outline and draft feedback requests | All Wave 1 authors |
| `#coordination` | Editor ↔ author coordination | All Wave 1 authors + editors |
| `#technical` | Infrastructure questions | All users |
| `#domain-a-food-water` | Domain A working group | Domain A authors only |
| `#domain-b-energy` | Domain B working group | Domain B authors only |
| `#domain-c-health` | Domain C working group | Domain C authors only |
| `#domain-d-comms` | Domain D working group | Domain D authors only |
| `#domain-e-governance` | Domain E working group | Domain E authors only |
| `#admin-ops` | Admin/orchestrator private channel | Admin only |

### 4.4 Onboarding Day-by-Day Schedule (First 5 Days)

| Day | Author Action | Admin Action |
|-----|--------------|-------------|
| Day 1 | Receive welcome email | Send bulk welcome emails |
| Day 1 | Log into Nextcloud, change password | Verify all logins succeed in Nextcloud admin panel |
| Day 2 | Log into Element, join rooms | Confirm all room joins in Matrix admin |
| Day 2 | Install Nextcloud Desktop Client (optional) | Monitor sync logs |
| Day 3 | Post confirmation in #coordination | Check: all authors confirmed |
| Day 3 | Open assigned document, add "Ready" comment | Verify document access per author |
| Day 4 | Begin editing assigned outline/draft | Daily standup in #coordination at 09:00 UTC |
| Day 5 | Sync CalDAV calendar (optional) | Add key deadlines to editorial calendar |

---

## Part 5: Moderation Playbook (10-Item Procedure)

### Moderation Principles

The platform is invite-only and populated with vetted authors. Moderation actions are rare. The following procedures apply when issues arise.

### Procedure 1 — Inappropriate Content Posted in Matrix Room

1. Screenshot the message with timestamp for the record
2. Use Element "report content" feature on the message
3. If urgent: remove the message via Synapse admin API:
   ```bash
   curl -X POST \
     -H "Authorization: Bearer $MATRIX_ADMIN_TOKEN" \
     "http://localhost:8008/_synapse/admin/v1/rooms/!ROOM_ID/delete_local_messages" \
     -d '{"limit": 1}'
   ```
4. Send a private DM to the user explaining the issue
5. Log the incident with timestamp and action taken

### Procedure 2 — Disruptive User in Matrix Room

1. First occurrence: private DM warning with specific policy citation
2. Second occurrence: temporary mute via Synapse admin:
   ```bash
   # Deactivate user temporarily (re-enable with "deactivated": false)
   curl -X PUT \
     -H "Authorization: Bearer $MATRIX_ADMIN_TOKEN" \
     -H "Content-Type: application/json" \
     -d '{"deactivated": true}' \
     "http://localhost:8008/_synapse/admin/v2/users/@USERNAME:resilience-hub.local"
   ```
3. Third occurrence: permanent removal from platform

### Procedure 3 — Spam or Bot Activity

1. Immediately deactivate the user account (see Procedure 2, step 2)
2. Purge the spam messages from affected rooms
3. Check Synapse registration logs to identify how the account was created
4. Tighten registration if needed (registration_requires_token: true is the default)

### Procedure 4 — Unauthorized File Sharing in Nextcloud

1. In Nextcloud admin panel: Settings → Sharing → review active shares
2. Delete the unauthorized share:
   ```bash
   docker exec -u www-data community-nextcloud php occ \
     sharing:cleanup-remote-storages
   ```
3. DM the user with a reminder of file sharing policies

### Procedure 5 — Account Compromise Suspected

1. Immediately deactivate the account (Procedure 2, step 2)
2. Change the user's password via admin:
   ```bash
   # Nextcloud
   docker exec -u www-data community-nextcloud php occ \
     user:resetpassword USERNAME
   # Matrix
   curl -X PUT \
     -H "Authorization: Bearer $MATRIX_ADMIN_TOKEN" \
     -d '{"new_password": "SECURE_TEMP_PASSWORD"}' \
     "http://localhost:8008/_synapse/admin/v2/users/@USERNAME:resilience-hub.local"
   ```
3. Audit recent file access in Nextcloud: Settings → Activity
4. Review Matrix login history: check Synapse access tokens for the user
5. Contact the user via out-of-band channel (email) to confirm account status
6. Re-activate after identity confirmed

### Procedures 6-10 — Additional Scenarios

**Procedure 6 — Author requests account deletion**: Deactivate Nextcloud account, deactivate Matrix account, remove from all shared folders, archive their draft documents to admin folder, confirm deletion via email.

**Procedure 7 — Platform performance degradation**: Run `docker stats --no-stream`, identify which container is consuming excess resources, check if Nextcloud background jobs are running (`php occ background:cron`), restart the offending container if needed.

**Procedure 8 — Disk space warning (>80% full)**: Run Matrix media purge (Section 5.5 of Roadmap), archive old Nextcloud versions (`php occ versions:cleanup`), check and rotate log files, notify admin to provision additional storage if within 7 days of full.

**Procedure 9 — Matrix room compromise**: Remove all members from room, create a new private room, re-invite verified members only, transfer any important message history via screenshot or export.

**Procedure 10 — Author complains about missing messages**: Check Element offline mode (IndexedDB full?), have them clear browser cache and re-sync, verify Matrix account is not deactivated, check Synapse logs for delivery errors.

---

## Part 6: Monitoring Dashboard Specification

### 6.1 Hourly Health Check (Automated)

```bash
#!/bin/bash
# /opt/community/nextcloud-matrix/scripts/healthcheck.sh
# Cron: 0 * * * * /opt/community/.../healthcheck.sh >> /var/log/community-health.log 2>&1

set -euo pipefail
COMPOSE_DIR="/opt/community/nextcloud-matrix"
ALERT_EMAIL="admin@resilience-hub.org"
NEXTCLOUD_URL="http://localhost:80"   # via Docker network
MATRIX_URL="http://localhost:8008"
failures=()

check_container() {
  local name="$1"
  local status
  status=$(docker inspect --format='{{.State.Health.Status}}' "$name" 2>/dev/null || echo "not_found")
  [[ "$status" == "healthy" ]] || failures+=("$name: $status")
  echo "[$(date -u +%H:%M:%S)] $name: $status"
}

check_api() {
  local name="$1" url="$2"
  curl -sf --max-time 10 "$url" > /dev/null 2>&1 \
    || failures+=("API unreachable: $name ($url)")
  echo "[$(date -u +%H:%M:%S)] API $name: $(curl -so /dev/null -w '%{http_code}' --max-time 10 "$url" 2>/dev/null || echo 'FAIL')"
}

# Container health
for c in community-postgres community-redis community-nextcloud community-synapse community-nginx; do
  check_container "$c"
done

# API health
check_api "Nextcloud" "http://localhost:80/status.php"
check_api "Matrix" "http://localhost:8008/_matrix/client/versions"
check_api "Element" "http://localhost:8443/"

# Disk space
disk_pct=$(df -h "$COMPOSE_DIR" | tail -1 | awk '{print $5}' | tr -d '%')
[[ "$disk_pct" -lt 85 ]] || failures+=("Disk ${disk_pct}% — approaching full")
echo "[$(date -u +%H:%M:%S)] Disk: ${disk_pct}%"

# Report
if [[ "${#failures[@]}" -gt 0 ]]; then
  echo "ALERT: ${#failures[@]} failure(s)"
  printf -- '- %s\n' "${failures[@]}"
  printf 'Community Platform Alert\n\n%s\n' "$(printf '- %s\n' "${failures[@]}")" \
    | mail -s "Platform Alert — $(hostname)" "$ALERT_EMAIL" 2>/dev/null || true
fi
```

### 6.2 Key Metrics to Track

| Metric | Target | Check Command |
|--------|--------|--------------|
| All containers healthy | 6/6 | `docker compose ps --format "{{.Status}}" | grep -v healthy | wc -l` (should be 0) |
| Nextcloud response time | < 2s | `curl -o /dev/null -s -w '%{time_total}' https://100.70.184.84/status.php` |
| Matrix API response time | < 500ms | `curl -o /dev/null -s -w '%{time_total}' http://localhost:8008/_matrix/client/versions` |
| Active Matrix users | Track weekly | Synapse admin API: `/_synapse/admin/v2/users?guests=false&deactivated=false` |
| Disk usage | < 80% | `df -h /opt/community/nextcloud-matrix/data | tail -1` |
| Container restarts | 0 per day | `docker ps --format "{{.Names}}: {{.Status}}" | grep -v "Up "` |
| Backup success | Daily | `ls -la /mnt/backup/community-platform/$(date +%Y-%m-%d)/` |
| CPU temperature (Pi 5) | < 85°C | `vcgencmd measure_temp` |

### 6.3 Weekly Operational Review Checklist

Every Monday at 09:00 UTC:

- [ ] Review `/var/log/community-health.log` for recurring errors
- [ ] Check backup log `/var/log/community-backup.log` — verify 7 successful backups
- [ ] Run `docker stats --no-stream` and record container RAM usage
- [ ] Check disk: `df -h /opt/community/nextcloud-matrix/data`
- [ ] Check active users: `docker exec -u www-data community-nextcloud php occ user:list | wc -l`
- [ ] Review Matrix admin for any pending moderation
- [ ] Check TLS certificate expiry (< 30 days remaining = renew now)
- [ ] Update Docker images if new versions available (non-production; test first): `docker compose pull`

---

## Part 7: Rollback and Disaster Recovery

### 7.1 Clean Rollback (Fresh Deployment Failure)

Use this if deployment failed before any production data was written:

```bash
cd /opt/community/nextcloud-matrix

# Stop and remove all containers and volumes
docker compose down -v

# Remove data directories (ONLY safe on fresh deployment before production use)
sudo rm -rf data/postgres data/redis data/nextcloud data/matrix

# Recreate empty directories
mkdir -p data/{postgres,redis,nextcloud,matrix/media}

# Save failure log
docker compose logs --no-color 2>&1 | gzip > /tmp/deploy-failure-$(date +%Y%m%d-%H%M%S).log.gz

# Fix the identified issue, then restart from Runbook Step 5
echo "Ready to retry. Fix the issue first."
```

### 7.2 Partial Recovery (Service Down, Data Intact)

Use this if one container fails after production data exists:

```bash
# Identify which container is down
docker compose ps

# Attempt restart first
docker compose restart CONTAINER_NAME

# If restart fails, check logs
docker logs --tail=50 CONTAINER_NAME

# If Nextcloud is in maintenance mode
docker exec -u www-data community-nextcloud php occ maintenance:mode --off

# If database needs repair
docker exec -u www-data community-nextcloud php occ db:add-missing-indices
docker exec -u www-data community-nextcloud php occ maintenance:repair
```

### 7.3 Full Disaster Recovery from Backup

See Section 6.2 of `PHASE_5_NEXTCLOUD_MATRIX_DEPLOYMENT_ROADMAP_v2.md` for the complete restore procedure. Summary:

1. Stop all containers: `docker compose down`
2. Start postgres only: `docker compose up -d postgres`
3. Restore both databases from `.sql.gz` backups
4. Restore file data from tar archives
5. Start all containers: `docker compose up -d`
6. Run Nextcloud repair: `php occ maintenance:repair && maintenance:mode --off`
7. Verify all services healthy (Post-Deployment Verification, Part 3 above)

### 7.4 Fallback Platform (If Stack Cannot Be Recovered)

If Nextcloud+Matrix cannot be brought online within the deployment window:

1. Check `PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md` for the Discourse fallback
2. Discourse deployment time: 2-3 hours (Docker-based)
3. For immediate coordination while fixing: use a temporary shared Google Drive folder + Signal group for the first 24 hours
4. Communicate the delay to authors via email within 2 hours of the go-live deadline

---

**Document Version**: 1.0
**Created**: June 5, 2026
**Status**: PRODUCTION-READY
**Confidence**: 87% (based on verified stack components; Pi 5 thermal constraints noted)
