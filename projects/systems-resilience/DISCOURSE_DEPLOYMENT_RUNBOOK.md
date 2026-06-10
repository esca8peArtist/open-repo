---
title: "Discourse Deployment Runbook — Raspberry Pi 5 (8GB)"
project: systems-resilience
phase: "5.1"
platform: "Discourse (Official Docker Launcher)"
status: PRODUCTION-READY — execute June 8 10:00–18:00 UTC
created: 2026-06-10
host: "raspby1 — 100.120.18.84 (Tailscale) / 100.70.184.84 (alt)"
deployment_window: "2026-06-08 10:00–18:00 UTC (8-hour window, 6–7 hour expected)"
publication_deadline: "2026-06-09 13:00 UTC"
cross_references:
  - DISCOURSE_DEPLOYMENT_PLAYBOOK.md
  - PHASE_5_1_CONTENT_READINESS.md
  - PHASE_5_1_PUBLICATION_OPERATIONAL_PROCEDURES.md
  - PHASE_5_1_PUBLICATION_ROLLBACK_PROCEDURE.md
---

# Discourse Deployment Runbook
## Raspberry Pi 5 (8GB RAM) — June 8, 2026 Production Deployment

**Execute this document on June 8, 2026. Publication window is June 9 13:00 UTC — platform must be verified operational by June 8 18:00 UTC.**

---

## Architecture Summary

```
External users (50–200 concurrent)
    |
    v
[Tailscale / public DNS]
    |
    v
Pi5 (100.120.18.84) — Discourse (Rails + Sidekiq + PostgreSQL + Redis)
    |                   Managed by official discourse_docker launcher
    |                   All-in-one container: single Docker process
    v
/var/discourse/shared/standalone/   (persistent volume — uploads, backups, logs)
```

Discourse's official deployment is a single container managed by its own `launcher` script, not a plain `docker-compose.yml`. PostgreSQL, Redis, nginx, and Sidekiq all run inside that one container via runit. This is the only officially supported production method. Do not use `docker-compose` or the `discourse/discourse:latest` image directly.

**Why Pi5 works for this deployment:**
- Discourse minimum: 1 GB RAM + 1 core. Pi5 8GB far exceeds this.
- Expected load: 50–200 concurrent users reading static forum topics.
- Pi5 thermal note: sustained bootstrap/compile step will push CPU to 87-88C (known behavior, see Memory notes). Bootstrap takes 15–25 minutes on Pi5 vs 5–10 minutes on x86 VPS — budget accordingly.
- Tailscale IP (100.120.18.84) is used for access; ensure DNS or hosts entries point to it.

---

## Deployment Timeline — June 8, 2026

| UTC Time | Phase | Task | Buffer |
|----------|-------|------|--------|
| 10:00 | Phase 1 | System prerequisites and checks | 30 min |
| 10:30 | Phase 2 | Docker installation and discourse_docker setup | 30 min |
| 11:00 | Phase 3 | app.yml configuration | 45 min |
| 11:45 | Phase 4 | Bootstrap (Pi5 will take 15–25 min) | 40 min |
| 12:25 | Phase 5 | SSL/TLS verification and admin account | 30 min |
| 12:55 | Phase 6 | Database init, backup config, SMTP verification | 45 min |
| 13:40 | Phase 7 | User provisioning (admin, moderators, author roles) | 45 min |
| 14:25 | Phase 8 | Community configuration (categories, permissions) | 45 min |
| 15:10 | Phase 9 | Publication category setup and content staging area | 30 min |
| 15:40 | Phase 10 | End-to-end verification and load test | 45 min |
| 16:25 | Phase 11 | Backup verification and disaster recovery setup | 30 min |
| 16:55 | Buffer | Issue resolution, re-testing | 65 min |
| **18:00** | **GATE** | **Platform verified — publication ready** | — |

If any phase runs long, notify immediately. The 65-minute buffer is real — do not treat it as scheduled downtime.

---

## Phase 1: System Prerequisites (10:00–10:30 UTC)

### 1.1 Check OS Version

Discourse's official Docker image is built for x86-64/amd64. Raspberry Pi 5 uses ARM64 (aarch64). The official Discourse Docker image does not support ARM64.

**Solution**: Use the `discourse/discourse_docker` launcher with the `bitnami/discourse` ARM-compatible image, or run the official x86 image under QEMU emulation (slow — not recommended for production). The recommended approach for Pi5 is the Bitnami Docker Compose stack.

```bash
# Confirm architecture
uname -m
# Expected on Pi5: aarch64

# Confirm OS
lsb_release -a
# Expected: Ubuntu 22.04 or 24.04 LTS, or Debian 12 Bookworm

# If running Raspberry Pi OS (Debian-based): confirmed ARM64
cat /etc/os-release | grep -E "^(NAME|VERSION_ID|ID)="
```

**CRITICAL — ARM64 ARCHITECTURE NOTE:**
The official Discourse launcher (`discourse_docker`) builds from source during bootstrap and does work on ARM64, but it requires the correct base image. Verify bootstrap succeeds before proceeding past Phase 4. If bootstrap fails with architecture errors, use the Bitnami fallback documented in Phase 4.3.

### 1.2 Docker Installation and Version Check

```bash
# Check if Docker is already installed
docker --version
# Acceptable: Docker 24.x, 25.x, 26.x, 27.x

# If Docker is not installed:
curl -fsSL https://get.docker.com -o /tmp/get-docker.sh
sudo sh /tmp/get-docker.sh

# Add your user to docker group (if not already)
sudo usermod -aG docker $USER
# Log out and back in for group change to take effect, OR:
newgrp docker

# Verify
docker run --rm hello-world
# Expected: "Hello from Docker!" message
```

### 1.3 Disk Space Verification

Discourse requires a minimum of 10 GB free. The Pi5 with publications will need:
- Discourse container image: ~2 GB
- Compiled assets after bootstrap: ~1.5 GB
- PostgreSQL data (grows with content): ~500 MB initial
- Upload storage: ~50 MB (Phase 5.1 bundle is 2.1 MB)
- Log retention: ~200 MB
- Backup storage (14 days): ~1 GB
- **Minimum recommended free space: 10 GB**

```bash
# Check available disk space
df -h /
# Look at the "Avail" column for the / partition

# If on a separate data partition:
df -h /var
df -h /home

# If disk is tight, free space:
sudo apt-get autoremove -y
sudo apt-get clean
docker system prune -f   # remove unused Docker images/containers

# Check current Docker disk usage
docker system df
```

### 1.4 Port Availability Checks

```bash
# Confirm ports 80 and 443 are not already in use
sudo ss -tlnp | grep -E ':80|:443'
# Expected: no output (ports are free)

# If something is using port 80 (common: nginx, Apache, another web server):
sudo ss -tlnp | grep ':80'
# Identify the process, then stop it:
# sudo systemctl stop nginx   (if nginx)
# sudo systemctl disable nginx

# Check if ufw firewall is active and configure it
sudo ufw status
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
# Do NOT add 0.0.0.0 — ufw rules apply to specific interfaces by default
# If you need to restrict to Tailscale only:
sudo ufw allow in on tailscale0 to any port 80
sudo ufw allow in on tailscale0 to any port 443
sudo ufw enable   # only if not already active
```

### 1.5 DNS / Hostname Configuration

For Discourse to issue a Let's Encrypt certificate, the hostname in `app.yml` must resolve to the server's public IP. For a Tailscale-only deployment, Let's Encrypt will not work (Tailscale IPs are not publicly routable).

**Decision: Public DNS vs. Tailscale-only vs. Self-signed**

| Option | Let's Encrypt | External Access | Complexity |
|--------|--------------|-----------------|-----------|
| Public domain (forum.yourdomain.com) | Yes | Yes | Medium |
| Tailscale MagicDNS (forum.yourtailnet.ts.net) | No (need ACME DNS challenge) | Tailscale only | Low |
| IP-only + self-signed cert | No | Tailscale only | Low |

For a 50–200 user community where all users can be on Tailscale, the IP-only + self-signed approach is operationally simplest and avoids DNS propagation delays.

**Tailscale-only setup (recommended for this deployment):**

```bash
# Get the Tailscale IP
tailscale ip -4
# Expected: 100.120.18.84 (or similar)

# The Discourse hostname will be the Tailscale IP
# SSL will use a self-signed cert (browser will warn; users accept once)
# OR use Tailscale's built-in HTTPS support:
sudo tailscale cert $(tailscale status --json | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['Self']['DNSName'].rstrip('.'))")
# This issues a real cert for the Tailscale MagicDNS hostname
```

**If using a public domain:** ensure the A record is set and propagated before Phase 4. Check propagation:

```bash
dig +short forum.yourdomain.com
# Expected: your Pi5's public IP

# From external host:
curl -s https://dns.google/resolve?name=forum.yourdomain.com&type=A | python3 -m json.tool
```

### 1.6 Prerequisites Verification Checklist

Before proceeding to Phase 2, confirm all of the following:

- [ ] `uname -m` returns `aarch64`
- [ ] OS is Ubuntu 22.04/24.04 LTS or Debian 12 (64-bit)
- [ ] `docker --version` returns 24.x or later
- [ ] `df -h /` shows 10+ GB available
- [ ] Ports 80 and 443 are free (`ss -tlnp | grep ':80\|:443'` returns no output)
- [ ] DNS hostname decision made and documented
- [ ] If public domain: A record verified with `dig`
- [ ] If Tailscale-only: Tailscale IP confirmed as `100.120.18.84`

**Rollback at this stage**: No deployment changes made yet. If prerequisites fail, address them before proceeding. Common blockers: disk space (extend partition or clean up), ports in use (stop conflicting services), Docker not installed (run install script).

---

## Phase 2: Discourse Docker Launcher Setup (10:30–11:00 UTC)

### 2.1 Clone Official Discourse Docker

```bash
# Create the discourse directory (official location)
sudo mkdir -p /var/discourse
sudo chown $USER:$USER /var/discourse

# Clone the official launcher
git clone https://github.com/discourse/discourse_docker.git /var/discourse
cd /var/discourse

# Verify the clone succeeded
ls /var/discourse/
# Expected: launcher  samples/  templates/  image/  containers/  (and other files)

ls /var/discourse/samples/
# Expected: standalone.yml  (the template we'll use)

# Check launcher is executable
ls -la /var/discourse/launcher
# Expected: -rwxr-xr-x (executable)
```

### 2.2 Install Prerequisites for Launcher

```bash
# The launcher needs git and basic tools
sudo apt-get update -y
sudo apt-get install -y git curl wget python3 yamllint

# Verify yamllint is available (we'll use it to validate app.yml)
yamllint --version
# Expected: yamllint X.X.X
```

### 2.3 Create Containers Directory

```bash
# The containers/ directory holds your app.yml
mkdir -p /var/discourse/containers
ls /var/discourse/containers/
# Expected: empty directory (app.yml will be created in Phase 3)
```

**Verification at end of Phase 2:**

```bash
ls /var/discourse/launcher /var/discourse/samples/standalone.yml /var/discourse/containers/
# All three should exist
```

**Rollback at this stage**: Remove `/var/discourse` and start over. No persistent state yet.

```bash
# Rollback:
sudo rm -rf /var/discourse
```

---

## Phase 3: app.yml Configuration (11:00–11:45 UTC)

### 3.1 Copy and Edit the Template

```bash
cp /var/discourse/samples/standalone.yml /var/discourse/containers/app.yml

# Open in editor
nano /var/discourse/containers/app.yml
```

### 3.2 Complete app.yml for Pi5 / Tailscale Deployment

Replace the entire contents of `/var/discourse/containers/app.yml` with the following. Fill in every `REPLACE_*` value before saving.

```yaml
## /var/discourse/containers/app.yml
## Phase 5.1 — Systems Resilience Community Platform
## Host: Raspberry Pi 5 (8GB) at 100.120.18.84 (Tailscale)
## Generated: 2026-06-08

templates:
  - "templates/postgres.template.yml"
  - "templates/redis.template.yml"
  - "templates/web.template.yml"
  - "templates/web.ratelimited.template.yml"

## Port bindings
## IMPORTANT: Bind to specific interface, NEVER 0.0.0.0
## For Tailscale-only: bind to Tailscale interface IP
## For public: bind to public IP
expose:
  - "100.120.18.84:80:80"    # HTTP (Let's Encrypt ACME if using public domain)
  - "100.120.18.84:443:443"  # HTTPS

## If you don't know the Tailscale IP at deploy time, use 127.0.0.1
## and put a reverse proxy in front:
# expose:
#   - "127.0.0.1:8080:80"
#   - "127.0.0.1:8443:443"

params:
  db_default_text_search_config: "pg_catalog.english"
  ## Pi5-tuned PostgreSQL settings (8GB RAM)
  db_shared_buffers: "512MB"     # 25% of PostgreSQL memory budget
  db_work_mem: "64MB"

env:
  LANG: en_US.UTF-8
  RAILS_ENV: production

  ## REPLACE with your actual hostname or IP
  ## For Tailscale MagicDNS: use your-machine-name.your-tailnet.ts.net
  ## For IP-only: use 100.120.18.84 (self-signed cert warning in browsers)
  DISCOURSE_HOSTNAME: "REPLACE_WITH_HOSTNAME_OR_IP"

  ## Admin email — this account gets admin privileges
  DISCOURSE_DEVELOPER_EMAILS: "REPLACE_WITH_ADMIN_EMAIL"

  ## SMTP Configuration
  ## If no SMTP: Discourse will queue emails but not send them
  ## Use Brevo (free tier: 300 emails/day), Mailgun, or AWS SES
  DISCOURSE_SMTP_ADDRESS: "REPLACE_WITH_SMTP_HOST"
  DISCOURSE_SMTP_PORT: 587
  DISCOURSE_SMTP_USER_NAME: "REPLACE_WITH_SMTP_USER"
  DISCOURSE_SMTP_PASSWORD: "REPLACE_WITH_SMTP_PASSWORD"
  DISCOURSE_SMTP_ENABLE_START_TLS: true
  DISCOURSE_SMTP_AUTHENTICATION: login
  DISCOURSE_NOTIFICATION_EMAIL: "noreply@REPLACE_WITH_YOUR_DOMAIN"
  DISCOURSE_CONTACT_EMAIL: "REPLACE_WITH_ADMIN_EMAIL"

  ## Site branding
  DISCOURSE_TITLE: "Systems Resilience Community"

  ## Performance — tuned for Pi5 (8GB, 4-core ARM)
  ## Unicorn workers: 2 is safe for Pi5; 3 is possible but watch RAM
  UNICORN_WORKERS: 2
  UNICORN_TIMEOUT: 60

  ## Rate limiting — generous for community of 50-200
  DISCOURSE_MAX_REQS_PER_IP_PER_MINUTE: 300
  DISCOURSE_MAX_REQS_PER_IP_PER_10_SECONDS: 60

  ## Access control
  ## true = require admin approval for new accounts (recommended for launch)
  DISCOURSE_MUST_APPROVE_USERS: false

  ## Let's Encrypt — only works with a real public domain
  ## Leave commented out if using Tailscale IP or self-signed
  # LETSENCRYPT_ACCOUNT_EMAIL: "REPLACE_WITH_ADMIN_EMAIL"

## Persistent volumes — DO NOT change these paths
volumes:
  - volume:
      host: /var/discourse/shared/standalone
      guest: /shared
  - volume:
      host: /var/discourse/shared/standalone/log/var-log
      guest: /var/log

## Plugins to install during bootstrap
hooks:
  after_code:
    - exec:
        cd: $home
        cmd:
          ## Docker manager (required — lets you manage Docker from Discourse UI)
          - git clone https://github.com/discourse/docker_manager.git plugins/docker_manager
          ## Optional: remove or add other plugins here
          ## - git clone https://github.com/discourse/discourse-solved.git plugins/discourse-solved
```

### 3.3 Validate app.yml Before Bootstrapping

A single YAML formatting error will fail the entire bootstrap. Always validate first.

```bash
# Validate with yamllint
yamllint /var/discourse/containers/app.yml
# Expected: no output (no errors)
# Any output = fix before proceeding

# Also check with Python's yaml parser
python3 -c "
import yaml
try:
    with open('/var/discourse/containers/app.yml') as f:
        data = yaml.safe_load(f)
    print('YAML OK')
    print(f'Hostname: {data[\"env\"][\"DISCOURSE_HOSTNAME\"]}')
    print(f'SMTP host: {data[\"env\"][\"DISCOURSE_SMTP_ADDRESS\"]}')
    print(f'Unicorn workers: {data[\"env\"][\"UNICORN_WORKERS\"]}')
except Exception as e:
    print(f'YAML ERROR: {e}')
"
# Expected:
# YAML OK
# Hostname: <your hostname>
# SMTP host: <your smtp host>
# Unicorn workers: 2
```

**Check for unreplaced REPLACE_* values:**

```bash
grep "REPLACE_" /var/discourse/containers/app.yml
# Expected: no output (all values have been replaced)
# If any output: fix those values before bootstrapping
```

### 3.4 Phase 3 Verification Checklist

- [ ] `/var/discourse/containers/app.yml` exists and is not empty
- [ ] `yamllint` returns no errors
- [ ] Python YAML parse returns "YAML OK"
- [ ] No `REPLACE_*` placeholders remain in file
- [ ] `DISCOURSE_HOSTNAME` is set to actual hostname or IP
- [ ] `DISCOURSE_DEVELOPER_EMAILS` is set to admin email
- [ ] SMTP credentials are filled in (or understood that email won't work)
- [ ] `expose` bindings use `100.120.18.84` not `0.0.0.0`

**Rollback**: Edit `app.yml` to correct any issues. No destructive changes yet.

---

## Phase 4: Bootstrap and Launch (11:45–12:25 UTC)

### 4.1 Run Bootstrap

Bootstrap compiles all Ruby gems, JavaScript, and CSS assets, runs database migrations, and starts Discourse for the first time. On Pi5 ARM64, this takes **15–25 minutes** (vs 5–10 on x86 VPS).

```bash
cd /var/discourse

# Bootstrap — watch the output carefully
sudo ./launcher bootstrap app 2>&1 | tee /tmp/discourse-bootstrap.log
```

**Expected output sequence (in order):**
```
using extra large images
Pups::ExecError  ... (ignore these — they're compile warnings, not fatal)
I, [...]  INFO -- : Successfully configured ...
I, [...]  INFO -- : Booting ...
```

**Bootstrap will:**
1. Pull the Discourse Docker base image (~1.5 GB download — allow 5–10 min on home internet)
2. Install Ruby gems and Node packages (~5–8 min)
3. Compile assets (~3–5 min)
4. Run database migrations (~1–2 min)
5. If `LETSENCRYPT_ACCOUNT_EMAIL` is set: issue TLS certificate (~1–2 min, requires DNS propagation)

```bash
# Monitor bootstrap progress in a second terminal
tail -f /tmp/discourse-bootstrap.log
```

### 4.2 Expected Bootstrap Completion

A successful bootstrap ends with output similar to:

```
Runtime error: ...  (ignore final warning lines — they're normal)
```

The bootstrap process exits 0 on success. Check:

```bash
echo "Bootstrap exit code: $?"
# Expected: 0
```

### 4.3 ARM64 Fallback (if official bootstrap fails)

If the official bootstrap fails with architecture errors on the Pi5:

```bash
# Check error type
grep -i "arch\|arm\|amd64\|x86" /tmp/discourse-bootstrap.log | tail -20
```

If you see errors about `exec format error` or `incompatible architecture`, the official image does not support ARM64. Use the Bitnami alternative:

```bash
# Bitnami Discourse Docker Compose (ARM64 compatible)
# Create /opt/discourse-bitnami/ working directory
sudo mkdir -p /opt/discourse-bitnami
cd /opt/discourse-bitnami

cat > docker-compose.yml << 'BITNAMI_COMPOSE_EOF'
version: '3.8'

services:
  postgresql:
    image: docker.io/bitnami/postgresql:16
    volumes:
      - postgresql_data:/bitnami/postgresql
    environment:
      POSTGRESQL_USERNAME: discourse
      POSTGRESQL_PASSWORD: REPLACE_POSTGRES_PASSWORD
      POSTGRESQL_DATABASE: discourse
    # Bind to loopback only
    ports:
      - "127.0.0.1:5432:5432"

  redis:
    image: docker.io/bitnami/redis:7.2
    environment:
      ALLOW_EMPTY_PASSWORD: "yes"
    volumes:
      - redis_data:/bitnami/redis/data
    ports:
      - "127.0.0.1:6379:6379"

  discourse:
    image: docker.io/bitnami/discourse:3
    ports:
      - "100.120.18.84:80:3000"
      - "100.120.18.84:443:3001"
    depends_on:
      - postgresql
      - redis
    volumes:
      - discourse_data:/bitnami/discourse
    environment:
      DISCOURSE_HOST: REPLACE_HOSTNAME
      DISCOURSE_DATABASE_HOST: postgresql
      DISCOURSE_DATABASE_USER: discourse
      DISCOURSE_DATABASE_PASSWORD: REPLACE_POSTGRES_PASSWORD
      DISCOURSE_DATABASE_NAME: discourse
      DISCOURSE_REDIS_HOST: redis
      DISCOURSE_SMTP_HOST: REPLACE_SMTP_HOST
      DISCOURSE_SMTP_PORT: 587
      DISCOURSE_SMTP_USER: REPLACE_SMTP_USER
      DISCOURSE_SMTP_PASSWORD: REPLACE_SMTP_PASSWORD
      DISCOURSE_SITE_NAME: "Systems Resilience Community"

  sidekiq:
    image: docker.io/bitnami/discourse:3
    depends_on:
      - discourse
    volumes:
      - discourse_data:/bitnami/discourse
    command: /opt/bitnami/scripts/discourse-sidekiq/run.sh
    environment:
      DISCOURSE_HOST: REPLACE_HOSTNAME
      DISCOURSE_DATABASE_HOST: postgresql
      DISCOURSE_DATABASE_USER: discourse
      DISCOURSE_DATABASE_PASSWORD: REPLACE_POSTGRES_PASSWORD
      DISCOURSE_DATABASE_NAME: discourse
      DISCOURSE_REDIS_HOST: redis

volumes:
  postgresql_data:
  redis_data:
  discourse_data:
BITNAMI_COMPOSE_EOF

# Start the Bitnami stack
docker compose up -d

# Watch startup (Discourse takes 3-5 min to initialize)
docker compose logs -f discourse
```

**Note:** If using Bitnami, commands in subsequent phases that reference `sudo ./launcher enter app` become `docker compose exec discourse bash`.

### 4.4 Start Discourse After Bootstrap

```bash
cd /var/discourse

# Start the container
sudo ./launcher start app

# Check status
sudo ./launcher status app
# Expected: "app: up" with uptime counter

# Check logs (last 50 lines)
sudo ./launcher logs app --tail 50
# Look for: "Discourse started" or "unicorn master loaded"
```

### 4.5 Initial Health Check

```bash
# Test HTTP (should redirect to HTTPS or return content)
curl -sv http://100.120.18.84/ 2>&1 | head -30
# Expected: HTTP 301 (redirect to HTTPS) or HTTP 200

# Test HTTPS (if TLS configured)
curl -svk https://100.120.18.84/about.json 2>&1 | head -50
# -k bypasses cert validation (for self-signed)
# Expected: JSON response with Discourse forum metadata

# If using public domain:
curl -sf https://forum.yourdomain.com/about.json | python3 -m json.tool
```

**Phase 4 Verification Checklist:**

- [ ] Bootstrap exits with code 0
- [ ] `sudo ./launcher status app` returns "app: up"
- [ ] `curl http://100.120.18.84/` returns HTTP response (not connection refused)
- [ ] `/tmp/discourse-bootstrap.log` shows no fatal errors

**Rollback at this stage:**

```bash
# Stop and destroy the container
cd /var/discourse
sudo ./launcher stop app
sudo ./launcher destroy app
# Edit app.yml to fix issues, then re-run bootstrap from Phase 4.1
```

---

## Phase 5: SSL/TLS Certificate Setup (12:25–12:55 UTC)

### 5.1 Option A: Tailscale HTTPS (Recommended for Pi5)

Tailscale provides free TLS certificates for machines with MagicDNS enabled. This avoids Let's Encrypt's public DNS requirement.

```bash
# Get your Tailscale MagicDNS hostname
tailscale status --json | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('Hostname:', d['Self']['DNSName'].rstrip('.'))
print('IP:', d['Self']['TailscaleIPs'][0])
"
# Example output:
# Hostname: raspby1.tail1234.ts.net
# IP: 100.120.18.84

# Issue Tailscale cert
tailscale_hostname=$(tailscale status --json | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['Self']['DNSName'].rstrip('.'))")
sudo tailscale cert "$tailscale_hostname"
# Expected: cert and key written to /var/lib/tailscale/certs/

# Find the cert and key files
ls -la /var/lib/tailscale/certs/
```

Update `DISCOURSE_HOSTNAME` in `app.yml` to the MagicDNS hostname and rebuild:

```bash
# Update hostname in app.yml
sed -i "s/REPLACE_WITH_HOSTNAME_OR_IP/$tailscale_hostname/" /var/discourse/containers/app.yml

# Rebuild to apply hostname change
cd /var/discourse
sudo ./launcher rebuild app
# On Pi5: takes 10–15 minutes (shorter than initial bootstrap)
```

### 5.2 Option B: Let's Encrypt (Only if public domain configured)

If you have a public domain pointing to this Pi5:

```bash
# In app.yml, uncomment LETSENCRYPT_ACCOUNT_EMAIL
# Then rebuild (Let's Encrypt is handled automatically during bootstrap)
# Verify cert after rebuild:
echo | openssl s_client -connect forum.yourdomain.com:443 2>/dev/null | \
  openssl x509 -noout -subject -dates
# Expected: subject=CN=forum.yourdomain.com, notAfter=~90 days from now
```

### 5.3 Option C: Self-Signed Certificate (Fallback)

If neither Tailscale cert nor Let's Encrypt is viable, generate a self-signed cert. Users will see a browser warning on first visit; for a closed community this is acceptable.

```bash
# Generate self-signed cert
sudo mkdir -p /var/discourse/shared/standalone/ssl
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
  -keyout /var/discourse/shared/standalone/ssl/discourse.key \
  -out /var/discourse/shared/standalone/ssl/discourse.crt \
  -subj "/CN=100.120.18.84/O=Systems Resilience/C=US" \
  -addext "subjectAltName=IP:100.120.18.84"

# Verify cert
openssl x509 -in /var/discourse/shared/standalone/ssl/discourse.crt -noout -text | grep -E "(Subject|Not After|IP)"
```

### 5.4 TLS Verification

```bash
# Test HTTPS with curl (use -k if self-signed to bypass validation)
curl -vk https://100.120.18.84/about.json 2>&1 | grep -E "(SSL|TLS|cipher|expire|HTTP/)"
# Expected: SSL connection established, HTTP/2 200 or HTTP/1.1 200

# For Tailscale cert (should be valid):
curl -v https://raspby1.tail1234.ts.net/about.json 2>&1 | grep -E "(SSL|TLS|HTTP/)"
# Expected: no SSL warning, HTTP 200
```

---

## Phase 6: Database Initialization and Backup Configuration (12:55–13:40 UTC)

### 6.1 Database Status Verification

The bootstrap process initializes PostgreSQL automatically. Verify the database is healthy:

```bash
cd /var/discourse

# Enter the container
sudo ./launcher enter app

# Check PostgreSQL is running
pg_isready -h localhost -p 5432
# Expected: localhost:5432 - accepting connections

# Check database tables exist
psql -U discourse -h localhost discourse -c "\dt" | head -20
# Expected: list of tables (users, posts, topics, categories, etc.)

# Check table count (fresh install should have 80+ tables)
psql -U discourse -h localhost discourse -c "SELECT count(*) FROM information_schema.tables WHERE table_schema='public';"
# Expected: count >= 80

exit
```

### 6.2 Configure Automated Daily Backups

```bash
sudo ./launcher enter app
rails c

# Configure backup settings
SiteSetting.backup_frequency = 1                # Daily backups
SiteSetting.maximum_backups = 14                # Keep 14 days (2 weeks)
SiteSetting.backup_with_uploads = true          # Include uploaded files (Phase 5.1 PDFs)
SiteSetting.enable_backups = true               # Enable backup system

puts "Backup config: freq=#{SiteSetting.backup_frequency}d, keep=#{SiteSetting.maximum_backups}, uploads=#{SiteSetting.backup_with_uploads}"
exit
```

**Verify backup directory:**

```bash
ls -la /var/discourse/shared/standalone/backups/default/
# Expected: directory exists (may be empty on fresh install — first backup runs at midnight)
```

### 6.3 External Backup Script

Backups stored only on the Pi5 are not disaster-recovery backups. Set up an external copy job.

```bash
cat > /opt/discourse-backup.sh << 'BACKUP_SCRIPT_EOF'
#!/bin/bash
# External backup for Phase 5.1 Discourse deployment
# Run daily at 02:00 UTC (after Discourse's midnight backup)
set -euo pipefail

DISCOURSE_BACKUP_DIR="/var/discourse/shared/standalone/backups/default"
EXTERNAL_BACKUP_DIR="/home/awank/backups/discourse"
DATE=$(date -u +%Y-%m-%d)
LOG="/var/log/discourse-backup.log"

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Starting backup copy..." >> "$LOG"

mkdir -p "$EXTERNAL_BACKUP_DIR/$DATE"

# Find today's backup (Discourse names them with timestamp)
latest=$(ls -t "$DISCOURSE_BACKUP_DIR"/*.gz 2>/dev/null | head -1)
if [[ -z "$latest" ]]; then
    echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] WARNING: No backup found in $DISCOURSE_BACKUP_DIR" >> "$LOG"
    exit 1
fi

# Copy backup and config
cp -v "$latest" "$EXTERNAL_BACKUP_DIR/$DATE/" >> "$LOG" 2>&1
cp -v /var/discourse/containers/app.yml "$EXTERNAL_BACKUP_DIR/$DATE/app.yml.bak" >> "$LOG" 2>&1

# Prune old backups (keep 30 days)
find "$EXTERNAL_BACKUP_DIR" -maxdepth 1 -type d -mtime +30 -exec rm -rf {} \; 2>/dev/null || true

backup_size=$(du -sh "$EXTERNAL_BACKUP_DIR/$DATE" | cut -f1)
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Backup complete: $EXTERNAL_BACKUP_DIR/$DATE ($backup_size)" >> "$LOG"
BACKUP_SCRIPT_EOF

chmod +x /opt/discourse-backup.sh
mkdir -p /home/awank/backups/discourse

# Schedule: run at 02:00 UTC daily
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/discourse-backup.sh") | crontab -

# Verify cron entry
crontab -l | grep discourse-backup
```

### 6.4 Run Initial Manual Backup

```bash
# Trigger a backup immediately via rails console (don't wait for midnight)
sudo ./launcher enter app
rails c

BackupRestore::Backuper.new(User.find_by(admin: true).id, {}).run
# This runs in background; takes 2-5 minutes on Pi5
# Monitor in a second terminal: sudo ./launcher logs app --tail 50
exit
```

Wait 3–5 minutes, then verify:

```bash
ls -lah /var/discourse/shared/standalone/backups/default/
# Expected: at least one .gz file, size > 100KB
```

### 6.5 SMTP Email Verification

Discourse requires outbound email to function. New user accounts, password resets, and notification emails all go through SMTP.

```bash
sudo ./launcher enter app
rails c

# Send a test email
Jobs.enqueue(:test_email, to_address: "REPLACE_WITH_YOUR_EMAIL")
puts "Test email queued — check your inbox in 2-3 minutes"
exit
```

Check your inbox. If the test email does not arrive within 5 minutes:

```bash
sudo ./launcher enter app
rails c

# Check SMTP config
puts "SMTP host: #{SiteSetting.smtp_address}"
puts "SMTP port: #{SiteSetting.smtp_port}"
puts "SMTP user: #{SiteSetting.smtp_user_name}"
puts "SMTP TLS: #{SiteSetting.smtp_enable_start_tls}"

# Check for email delivery errors
EmailLog.last(5).each { |e| puts "#{e.created_at} #{e.to_address} #{e.smtp_transaction_response}" }
exit
```

**If SMTP fails and you cannot fix it before the June 8 deadline:**
Discourse will still function for content publication. Email notifications for new topics won't work, but the content will be readable. Log this as a known issue and resolve post-publication.

---

## Phase 7: User Provisioning (13:40–14:25 UTC)

### 7.1 Create Admin Account

After bootstrap, you must complete the admin setup via the web interface OR via rails console.

**Method A — Web setup wizard:**

1. Open a browser to `https://100.120.18.84` (or your configured hostname)
2. Discourse will show the setup wizard
3. Enter admin email and create password
4. Complete the wizard (site name, categories, etc.)

**Method B — Rails console (if web wizard is unavailable):**

```bash
sudo ./launcher enter app
rails c

# Check if admin account already exists from DISCOURSE_DEVELOPER_EMAILS
admin = User.find_by(email: "REPLACE_WITH_ADMIN_EMAIL")
if admin
    puts "Admin exists: #{admin.username} (id=#{admin.id})"
else
    # Create admin
    admin = User.new(
        email: "REPLACE_WITH_ADMIN_EMAIL",
        username: "admin",
        name: "Admin",
        password: "REPLACE_WITH_STRONG_PASSWORD"
    )
    admin.active = true
    admin.approved = true
    admin.save!
    admin.grant_admin!
    puts "Admin created: #{admin.username} (id=#{admin.id})"
end

# Verify admin status
puts "Admin: #{admin.admin?}, Moderator: #{admin.moderator?}"
exit
```

### 7.2 Create Moderator Accounts

```bash
sudo ./launcher enter app
rails c

# Create moderator role for community moderators
# Moderators can edit/delete posts, manage flags, but cannot change site settings
[
  { username: "moderator1", email: "mod1@example.com", name: "Moderator One" },
  # Add additional moderators as needed
].each do |attrs|
    u = User.new(
        username: attrs[:username],
        email: attrs[:email],
        name: attrs[:name],
        password: SecureRandom.hex(12)   # temp password — they'll reset via email
    )
    u.active = true
    u.approved = true
    u.save!
    u.grant_moderation!
    puts "Moderator created: #{u.username} (temp password will be sent via email)"
end

exit
```

### 7.3 Author Role Group

For Phase 5.1, authors are community members with elevated trust. Create a group.

```bash
sudo ./launcher enter app
rails c

# Create author group
group = Group.new(
    name: "phase5_authors",
    full_name: "Phase 5 Research Authors",
    bio_raw: "Authors and contributors to Phase 5 research documents",
    mentionable_level: 1,           # anyone can mention @phase5_authors
    messageable_level: 3,           # members can message each other
    visibility_level: 0,            # public — anyone can see the group
    members_visibility_level: 0     # public member list
)
group.save!
puts "Group created: #{group.name} (id=#{group.id})"

# Set group trust level: members get Trust Level 2 automatically
group.update!(grant_trust_level: 2)
puts "Group grants TL2 to members"

exit
```

### 7.4 Trust Level Configuration

```bash
sudo ./launcher enter app
rails c

# Tune trust levels for a community of ~50-200 trusted users
# Lower thresholds (default values are for large public forums)

SiteSetting.tl1_requires_read_posts = 5          # default: 30
SiteSetting.tl1_requires_topics_entered = 2       # default: 5
SiteSetting.tl1_requires_time_spent_mins = 5      # default: 60

SiteSetting.tl2_requires_days_visited = 3         # default: 15
SiteSetting.tl2_requires_read_posts = 15          # default: 100
SiteSetting.tl2_requires_topics_entered = 5       # default: 20

SiteSetting.tl3_requires_days_visited = 10        # default: 50
SiteSetting.tl3_requires_posts_read = 75          # default: 500

# New user posting limits (loosen for trusted community)
SiteSetting.newuser_max_replies_per_topic = 50    # default: 3
SiteSetting.newuser_max_links = 20                # default: 2

puts "Trust level thresholds configured for small trusted community"
exit
```

### 7.5 Phase 7 Verification Checklist

- [ ] Admin account exists and can log in via browser
- [ ] Admin panel accessible at `/admin`
- [ ] At least one moderator account created
- [ ] `phase5_authors` group created
- [ ] Trust level thresholds saved (verify via Admin → Settings → Trust Levels)
- [ ] User count in Admin → Users shows admin + any test accounts

---

## Phase 8: Community Configuration (14:25–15:10 UTC)

### 8.1 Category Structure

Phase 5.1 requires a dedicated publication category. Create the full category structure via rails console.

```bash
sudo ./launcher enter app
rails c

admin_user = User.find_by(admin: true)

categories = [
    {
        name: "Announcements",
        color: "F7941D",
        description: "Official project announcements",
        position: 0,
        readonly_for_everyone: false
    },
    {
        name: "Phase 5 — Published Research",
        color: "3AB54A",
        description: "Phase 5 Wave 1+2 research documents (61,611 words, 336 citations). Read-only for community. Authors post here.",
        position: 1,
        readonly_for_everyone: true     # Public read, author-only post
    },
    {
        name: "Discussion",
        color: "0088CC",
        description: "Community discussion of published research and implementation",
        position: 2,
        readonly_for_everyone: false
    },
    {
        name: "Project Coordination",
        color: "808281",
        description: "Wave 2 recruitment and coordination (TL2+ required to post)",
        position: 3,
        readonly_for_everyone: false
    },
    {
        name: "Meta",
        color: "E45735",
        description: "Forum feedback and governance",
        position: 4,
        readonly_for_everyone: false
    }
]

categories.each do |attrs|
    cat = Category.new(
        name: attrs[:name],
        color: attrs[:color],
        description: attrs[:description],
        position: attrs[:position],
        user: admin_user
    )
    cat.save!
    puts "Created category: #{cat.name} (id=#{cat.id})"
end

puts "\nAll categories created. Verify at /categories"
exit
```

### 8.2 Set Category Permissions

```bash
sudo ./launcher enter app
rails c

# Phase 5 Published Research: authors post, everyone reads
phase5_cat = Category.find_by(name: "Phase 5 — Published Research")
authors_group = Group.find_by(name: "phase5_authors")
admin_group = Group.find_by(name: "admins")

# everyone: can read only (3)
# phase5_authors: can create and reply (1)
# admins: full access (1)
phase5_cat.set_permissions({
    everyone: :readonly,
    "phase5_authors" => :full,
    "staff" => :full
})
phase5_cat.save!
puts "Phase 5 category permissions set: public=read, authors=full"

# Project Coordination: TL2+ can post
coord_cat = Category.find_by(name: "Project Coordination")
coord_cat.set_permissions({
    everyone: :readonly,
    trust_level_2: :full,
    "staff" => :full
})
coord_cat.save!
puts "Project Coordination: TL2+ can post"

# Announcements: staff only post
ann_cat = Category.find_by(name: "Announcements")
ann_cat.set_permissions({
    everyone: :readonly,
    "staff" => :full
})
ann_cat.save!
puts "Announcements: staff-only post"

exit
```

### 8.3 Content Moderation Settings

```bash
sudo ./launcher enter app
rails c

# Moderation settings for a curated research community
SiteSetting.allow_anonymous_posting = false
SiteSetting.must_approve_users = false         # open signup, but monitor
SiteSetting.approve_post_count = 0             # no post-approval queue
SiteSetting.invite_only = false                # anyone can register
SiteSetting.login_required = false             # public read (Phase 5 content is public)

# Spam protection
SiteSetting.newuser_spam_host_threshold = 5
SiteSetting.min_post_interval = 5             # 5 seconds between posts
SiteSetting.rate_limit_create_topic = 5       # 5 topics/minute max (anti-spam)
SiteSetting.rate_limit_create_post = 10       # 10 posts/minute max

# Flagging — community self-governance
SiteSetting.min_trust_to_flag_posts = 1       # TL1 can flag
SiteSetting.flags_required_to_hide_post = 5   # 5 flags auto-hide

puts "Content moderation settings configured"
exit
```

### 8.4 Site Settings

```bash
sudo ./launcher enter app
rails c

SiteSetting.title = "Systems Resilience Community"
SiteSetting.site_description = "Community platform for Phase 5 resilience research — 61,611 words, 336 citations"
SiteSetting.contact_email = "REPLACE_WITH_ADMIN_EMAIL"
SiteSetting.notification_email = "noreply@REPLACE_WITH_YOUR_DOMAIN"

# Allow markdown features
SiteSetting.enable_markdown_tables = true
SiteSetting.enable_markdown_linkify = true

# Search
SiteSetting.min_search_term_length = 3

puts "Site settings saved"
exit
```

---

## Phase 9: Publication Category Preparation (15:10–15:40 UTC)

### 9.1 Create Publication Index Topic

```bash
sudo ./launcher enter app
rails c

admin_user = User.find_by(admin: true)
phase5_cat = Category.find_by(name: "Phase 5 — Published Research")

# Create landing index topic (pinned)
index_topic = TopicCreator.create(
    admin_user,
    Guardian.new(admin_user),
    title: "Phase 5 Wave 1+2 — Research Index and Access Guide",
    raw: <<~MARKDOWN,
    # Systems Resilience Research — Phase 5 Wave 1+2

    This category contains 61,611 words of research across five domains,
    produced June 2026. All content is open and freely available.

    ## Published Documents

    | # | Title | Domain | Words | Citations |
    |---|-------|--------|-------|-----------|
    | 01 | Distributed Microgrids | Energy Infrastructure | ~4,600 | 50+ |
    | 02 | Community Implementation Playbook | Governance | ~8,847 | 42 |
    | 03 | Conflict Resolution Framework | Governance | ~8,587 | 28 |
    | 04 | Psychological Support Guide | Community Health | ~9,153 | 36 |
    | 05 | Veterinary Care in Crisis | Food Systems | ~10,654 | 39 |
    | 06 | Integrated Corpus (complete reference) | All | ~16,234 | 195+ |

    ## How to Access

    Click any topic in this category to read the full document.
    PDF downloads are attached to each topic.

    ## Clinical Advisories

    Documents 04 and 05 contain clinical and professional protocols.
    All procedures should be adapted to local professional standards.

    Published: June 9, 2026
    MARKDOWN
    category: phase5_cat.id,
    tags: ["phase-5", "index", "reference"]
)

if index_topic
    # Pin globally
    index_topic.update!(pinned_globally: true, pinned_at: Time.now)
    puts "Index topic created and pinned: id=#{index_topic.id}"
else
    puts "ERROR: Topic creation failed"
end

exit
```

### 9.2 Verify Discourse API Key Exists

The publication automation script (used June 9) requires an API key.

```bash
sudo ./launcher enter app
rails c

# Check if an API key exists
existing_key = ApiKey.first
if existing_key
    puts "API key exists: #{existing_key.key[0..8]}... (id=#{existing_key.id})"
else
    # Create one
    key = ApiKey.create!(
        key: SecureRandom.hex(32),
        description: "Phase 5.1 publication automation",
        user: User.find_by(admin: true)
    )
    puts "API key created: #{key.key}"
    puts "IMPORTANT: Save this key securely — it cannot be retrieved later"
end

exit
```

Save the API key to a secure location:

```bash
# Store API key in a local file (not in git)
echo "DISCOURSE_API_KEY=<your-key>" > /home/awank/.discourse-api-credentials
chmod 600 /home/awank/.discourse-api-credentials
```

---

## Phase 10: End-to-End Verification and Load Test (15:40–16:25 UTC)

### 10.1 API Health Checks

```bash
# Load API key from credentials file
source /home/awank/.discourse-api-credentials

DISCOURSE_URL="https://100.120.18.84"  # or your hostname

# Forum metadata
curl -sk "$DISCOURSE_URL/about.json" | python3 -m json.tool | head -20
# Expected: JSON with title, description, stats

# Categories
curl -sk "$DISCOURSE_URL/categories.json" | \
    python3 -c "
import sys, json
cats = json.load(sys.stdin)['category_list']['categories']
for c in cats:
    print(f'  {c[\"id\"]}: {c[\"name\"]}')
"
# Expected: list of 5 categories

# Test authenticated API
curl -sk -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    "$DISCOURSE_URL/admin/dashboard.json" | \
    python3 -c "import sys,json; d=json.load(sys.stdin); print('Sidekiq queued jobs:', d.get('sidekiq_queued_jobs', 'N/A'))"
# Expected: Sidekiq queued jobs: 0 (or very low number)
```

### 10.2 Concurrent User Load Test

Simulate 20 concurrent read requests to verify Pi5 handles Phase 5.1 traffic:

```bash
# Install hey (HTTP load testing tool)
# ARM64 binary:
curl -L https://hey-release.s3.us-east-2.amazonaws.com/hey_linux_arm64 -o /usr/local/bin/hey
chmod +x /usr/local/bin/hey

# Run 200 requests, 20 concurrent, to the main categories page
hey -n 200 -c 20 -disable-redirects "https://100.120.18.84/categories" 2>&1
# Expected results:
#   Average response time: < 2 seconds
#   99th percentile: < 5 seconds
#   Error rate: 0%

# If hey is not available, use curl loop:
for i in $(seq 1 20); do
    curl -sk -o /dev/null -w "%{time_total}s\n" "https://100.120.18.84/about.json" &
done
wait
# Expected: all times < 2 seconds
```

### 10.3 Content Upload Dry Run

Test the Discourse API upload workflow with a small test topic:

```bash
source /home/awank/.discourse-api-credentials

DISCOURSE_URL="https://100.120.18.84"

# Create test topic via API
response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"[TEST] Phase 5.1 Pre-Publication Verification $(date +%Y%m%d%H%M)\",
        \"raw\": \"This is a test post to verify API upload works correctly before June 9 publication.\n\n## Test Section\n\nIf you see this post, the API is working.\",
        \"category\": $(curl -sk \"$DISCOURSE_URL/categories.json\" | python3 -c \"import sys,json; cats=json.load(sys.stdin)['category_list']['categories']; print([c['id'] for c in cats if 'Meta' in c['name']][0])\")
    }")

topic_id=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('topic_id', 'ERROR'))")
echo "Test topic created: id=$topic_id"
echo "URL: $DISCOURSE_URL/t/$topic_id"

# Verify it appears in the forum
curl -sk "$DISCOURSE_URL/t/$topic_id.json" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('Title:', d.get('title'))
print('Posts:', d.get('posts_count'))
"

# Clean up test topic
curl -s -X DELETE "$DISCOURSE_URL/t/$topic_id.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system"
echo "Test topic deleted"
```

### 10.4 Phase 10 Verification Checklist

- [ ] `/about.json` returns valid JSON
- [ ] All 5 categories visible in `/categories.json`
- [ ] Admin dashboard accessible via API
- [ ] Sidekiq queue depth is 0 or near 0
- [ ] Load test: average response time < 2s under 20 concurrent users
- [ ] Test topic created via API and deleted successfully
- [ ] No errors in Discourse logs after load test

---

## Phase 11: Backup Verification and Disaster Recovery Setup (16:25–16:55 UTC)

### 11.1 Verify Backup System

```bash
# Confirm backup directory exists and is writable
ls -lah /var/discourse/shared/standalone/backups/default/
# If empty: trigger manual backup (see Phase 6.4)

# Verify external backup script works
sudo /opt/discourse-backup.sh
# Expected: Backup complete: /home/awank/backups/discourse/YYYY-MM-DD

ls -lah /home/awank/backups/discourse/
```

### 11.2 Restore Procedure Test (Dry Run)

```bash
# List available backups
ls -lah /var/discourse/shared/standalone/backups/default/

# Identify the backup file name (format: discourse-YYYY-MM-DD-HHMMSS.tar.gz)
latest_backup=$(ls -t /var/discourse/shared/standalone/backups/default/*.gz | head -1)
echo "Latest backup: $latest_backup"
echo "Backup size: $(du -sh $latest_backup | cut -f1)"

# Verify backup is readable
file "$latest_backup"
# Expected: gzip compressed data (not: ERROR or empty)

# Test extraction (don't actually restore — just verify archive integrity)
tar -tzf "$latest_backup" | head -10
# Expected: list of files inside the backup archive
```

### 11.3 Monitoring Health Check Setup

```bash
cat > /opt/discourse-healthcheck.sh << 'HEALTH_EOF'
#!/bin/bash
# Discourse health check — run every 5 minutes
set -euo pipefail

DISCOURSE_URL="https://100.120.18.84"
LOG="/var/log/discourse-health.log"
TIMESTAMP=$(date -u '+%Y-%m-%dT%H:%M:%SZ')
failures=()

# HTTP health check
http_code=$(curl -sk -o /dev/null -w "%{http_code}" --max-time 15 "$DISCOURSE_URL/about.json" 2>/dev/null || echo "000")
if [[ "$http_code" != "200" ]]; then
    failures+=("HTTP check failed: status=$http_code (expected 200)")
fi

# Container status
container_status=$(cd /var/discourse && sudo ./launcher status app 2>&1 | head -1)
if ! echo "$container_status" | grep -q "up"; then
    failures+=("Container not running: $container_status")
fi

# Disk space
disk_used=$(df -h /var/discourse/shared | tail -1 | awk '{print $5}' | tr -d '%')
if [[ "$disk_used" -gt 85 ]]; then
    failures+=("Disk usage HIGH: ${disk_used}% (threshold: 85%)")
fi

# Report
if [[ "${#failures[@]}" -eq 0 ]]; then
    echo "[$TIMESTAMP] OK — HTTP=$http_code disk=${disk_used}%" >> "$LOG"
else
    echo "[$TIMESTAMP] ALERT: ${failures[*]}" >> "$LOG"
    echo "ALERT at $TIMESTAMP: ${failures[*]}" | wall 2>/dev/null || true
fi
HEALTH_EOF

chmod +x /opt/discourse-healthcheck.sh

# Install cron: run every 5 minutes
(crontab -l 2>/dev/null; echo "*/5 * * * * /opt/discourse-healthcheck.sh") | crontab -

# Run once manually to verify
/opt/discourse-healthcheck.sh
cat /var/log/discourse-health.log | tail -3
```

---

## Phase 12: Final Verification — June 8 18:00 UTC Gate

This is the deployment complete gate. All of the following must be confirmed before signing off.

### 12.1 Infrastructure Verification

```bash
# Full system status report
echo "=== DISCOURSE DEPLOYMENT STATUS $(date -u '+%Y-%m-%dT%H:%M:%SZ') ===" 

echo -n "Container status: "
cd /var/discourse && sudo ./launcher status app 2>&1 | head -1

echo -n "HTTP health: "
curl -sk -o /dev/null -w "HTTP %{http_code}" --max-time 10 "https://100.120.18.84/about.json"
echo ""

echo -n "Disk available: "
df -h /var/discourse/shared | tail -1 | awk '{print $4}'

echo -n "RAM available: "
free -h | awk '/Mem:/{print $7}'

echo -n "Backup present: "
ls /var/discourse/shared/standalone/backups/default/*.gz 2>/dev/null | wc -l | xargs echo "backup files"

echo -n "API key: "
cd /var/discourse && sudo ./launcher enter app 2>/dev/null <<'EOF'
rails runner "puts ApiKey.any? ? 'CONFIGURED' : 'MISSING'"
EOF

echo -n "Categories: "
curl -sk "https://100.120.18.84/categories.json" | python3 -c "
import sys, json
d = json.load(sys.stdin)
cats = d['category_list']['categories']
print(f'{len(cats)} categories')
"

echo -n "Admin user: "
cd /var/discourse && sudo ./launcher enter app 2>/dev/null <<'EOF'
rails runner "u=User.find_by(admin: true); puts u ? \"#{u.username} (admin)\" : 'MISSING'"
EOF
```

### 12.2 June 8 Deployment Sign-Off Checklist

- [ ] Container status: "app: up"
- [ ] HTTPS returns HTTP 200 for `/about.json`
- [ ] Disk: 10+ GB available
- [ ] RAM: 3+ GB available (Discourse uses ~1.5–2 GB)
- [ ] At least 1 backup file present
- [ ] API key configured and stored securely
- [ ] All 5 categories created
- [ ] Admin user account functional
- [ ] `phase5_authors` group created
- [ ] SMTP: test email received (or documented as known issue)
- [ ] Health check cron installed and producing "OK" logs
- [ ] External backup script installed and verified
- [ ] `/home/awank/.discourse-api-credentials` exists with API key
- [ ] Publication index topic created and pinned

**Deployment Status**: If all items above are checked, Discourse is production-ready for June 9 13:00 UTC publication.

---

## Appendix A: Quick Reference Commands

```bash
# Start Discourse
cd /var/discourse && sudo ./launcher start app

# Stop Discourse
cd /var/discourse && sudo ./launcher stop app

# Restart Discourse
cd /var/discourse && sudo ./launcher restart app

# View live logs
cd /var/discourse && sudo ./launcher logs app --tail 100

# Enter container shell
cd /var/discourse && sudo ./launcher enter app

# Enter Rails console (inside container)
rails c

# Check status
cd /var/discourse && sudo ./launcher status app

# Rebuild (after app.yml changes)
cd /var/discourse && sudo ./launcher rebuild app

# Trigger manual backup (inside container)
rails runner "BackupRestore::Backuper.new(User.find_by(admin: true).id, {}).run"
```

## Appendix B: Pi5-Specific Notes

1. **Thermal throttling**: Bootstrap and rebuild operations will push CPU temperature to 87-88C on Pi5. This is within operational limits but slows compile times. Bootstrap takes 15–25 min vs 5–10 min on x86 VPS.

2. **ARM64 compatibility**: The official Discourse Docker image is built for x86-64. On ARM64, the launcher bootstraps from source (compiles Ruby and assets). This is slower but produces a working ARM64 build.

3. **RAM allocation**: With 8GB RAM, leave 2GB free for the OS. Set `UNICORN_WORKERS: 2` not 3. Discourse + PostgreSQL + Redis will use approximately 1.5–2GB at idle, 2.5–3GB under moderate load.

4. **SD card vs SSD**: If the Pi5 is running on an SD card, I/O will be a bottleneck during bootstrap and database writes. SSD over USB3 is strongly preferred. Monitor I/O: `iostat -x 2 5`.

5. **Tailscale interface binding**: The `expose:` section in `app.yml` uses `100.120.18.84:80:80`. If Tailscale IP changes (after tailscale re-registration), update `app.yml` and rebuild.
