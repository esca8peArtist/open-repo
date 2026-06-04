---
title: "Nextcloud + Matrix Deployment Playbook — Phase 5 Production Guide"
project: systems-resilience
phase: "5 — Wave 1 Author Recruitment & Collaboration Platform"
platform: "Nextcloud 29 + Matrix Synapse + Element Web + OnlyOffice"
status: PRODUCTION-READY
created: 2026-06-04
target_date: 2026-06-05T13:00Z
deployment_window: "4-6 hours (June 4 06:00 UTC – June 5 11:00 UTC)"
resource_requirement: "16GB RAM, 4-8 CPU cores, 100GB+ storage"
success_criteria: "Platform online + HTTPS + user accounts active + offline editing tested + team collaboration verified by June 5 13:00 UTC"
---

# Nextcloud + Matrix Deployment Playbook
## Complete Production Guide for Phase 5 Wave 1 Author Collaboration Platform

**Decision Context**: User selects Platform A (Nextcloud+Matrix) by June 4 EOD. If selected, deployment begins June 4 06:00 UTC to meet June 5 13:00 UTC Wave 1 author recruitment kickoff.

**Critical Success Factor**: Authors must be able to (1) access the platform, (2) download documents for offline editing, (3) collaborate via real-time chat, and (4) see published Wave 1+2 documents **by June 5 13:00 UTC**. This playbook is designed to be deployable in 4-6 hours if executed sequentially.

---

## Part 0: Architecture Overview

### Service Stack

```
┌─────────────────────────────────────────────────────────────────┐
│ Authors (Browser + Desktop Clients)                             │
│ - Web browsers (Firefox, Chrome)                                │
│ - Nextcloud Desktop Client (optional, for offline sync)         │
│ - Element Desktop/Mobile (optional, for chat on mobile)         │
└────────────────────────┬────────────────────────────────────────┘
                         │
         ┌───────────────┴────────────────┬──────────────────┐
         │                                │                  │
    ┌────▼──────────┐  ┌────────────────▼─┐  ┌────────────┐
    │  nginx        │  │                  │  │            │
    │  (TLS,proxy)  │  │  docker-compose  │  │  Optional: │
    └────┬──────────┘  │                  │  │  Certbot   │
         │             └────────────────┬─┘  │  (auto-SSL)│
         │                              │     └────────────┘
         ├──────────────────┬───────────┤
         │                  │           │
    ┌────▼─────────┐  ┌────▼───────┐  ┌┴─────────────┐
    │  Nextcloud   │  │   Matrix   │  │   Element    │
    │  (php-fpm)   │  │  Synapse   │  │   Web (CDN)  │
    │              │  │  Homeserver│  │              │
    │  ├─ Files    │  │            │  │ - Web client │
    │  ├─ OnlyOffice├──────────────┤  │ - Chat UI    │
    │  ├─ Calendar │  │ Federation │  │              │
    │  ├─ Contacts │  │ to matrix. │  └──────────────┘
    │  └─ Auth     │  │ org, etc   │
    └────┬─────────┘  └────┬───────┘
         │                 │
    ┌────────────────┬─────▼──────────┐
    │   PostgreSQL   │   Redis Cache  │
    │   (shared DB)  │   (shared)     │
    │                │                │
    │ ├─ Nextcloud   │ ├─ Sessions    │
    │ ├─ Matrix      │ ├─ Rate-limit  │
    │ └─ Metadata    │ └─ Temp storage│
    └────────────────┴────────────────┘
```

### Data Flow for Offline Authoring

```
Author Computer (Online)
  │
  ├─→ Nextcloud WebDAV client
  │   ├─ Download document for offline edit
  │   ├─ Cache to local filesystem
  │   └─ On reconnect: sync changes back
  │
  ├─→ Browser (OnlyOffice)
  │   ├─ Local storage (auto-save draft)
  │   ├─ When online: push to server
  │   └─ Conflict resolution: author wins
  │
  └─→ Element Web
      ├─ Message queue (IndexedDB)
      ├─ When online: deliver messages
      └─ End-to-end encryption (E2E room)

Author Computer (Offline)
  │
  ├─→ Nextcloud Desktop Client
  │   ├─ Sync pause (queued)
  │   ├─ Edit offline files
  │   └─ Changes stored locally
  │
  ├─→ OnlyOffice Cache
  │   ├─ Read from .docx/.xlsx offline
  │   ├─ Edit in browser
  │   └─ Local storage holds draft
  │
  └─→ Element (Desktop)
      ├─ Message queue (local DB)
      └─ Edit draft messages (not sent yet)

Reconnection Event
  │
  ├─→ Nextcloud: batched sync
  ├─→ OnlyOffice: push draft + merge
  └─→ Element: send queued messages
```

### Resource Model for 150 Active Users

| Service | RAM | CPU | Purpose |
|---------|-----|-----|---------|
| PostgreSQL 15 | 2.0 GB | 2 cores | Nextcloud + Matrix metadata, user accounts, file indices |
| Redis 7 | 1.5 GB | 1 core | Session cache, rate limiting, real-time subscriptions |
| Nextcloud 29 FPM | 2.0 GB | 2 cores | File management, WebDAV, calendar/contacts, metadata |
| OnlyOffice | 2.0 GB | 2 cores | Document editing (locks, formatting, collaboration) |
| Matrix Synapse | 2.5 GB | 2 cores | Homeserver, federation, end-to-end encryption |
| Element Web | <512 MB | shared | Static CDN, runs in user browsers |
| nginx reverse proxy | 512 MB | 1 core | TLS termination, request routing, compression |
| **Total Recommended** | **13-14 GB** | **4-6 cores** | Conservative allocation with 30% headroom |

**Scaling Notes**:
- 150-300 users: 16 GB RAM, 4-6 cores comfortable
- 300-500 users: 24 GB RAM, 8 cores + separate PostgreSQL host
- 500+ users: Consider architecture split (Matrix on separate host)

---

## Part 1: Pre-Deployment Checklist

### 1.1 Infrastructure Requirements

**Hardware** (must meet ALL):
- [ ] **Host Machine**: Ubuntu 22.04 LTS or 24.04 (strongly recommended)
- [ ] **RAM**: Minimum 14 GB (8 GB for services + 6 GB OS/buffer); 16+ GB recommended
- [ ] **CPU**: 4 cores minimum; 6-8 cores recommended for sub-2s response times
- [ ] **Storage**: 100 GB minimum (OS + database + file cache); 200 GB recommended
- [ ] **Network**: Static public IP address (not dynamic DHCP)
- [ ] **Uptime**: Host available 24/7 or configured with auto-restart on crash

**Network Requirements** (must meet ALL):
- [ ] **DNS Domain**: Registered, owns `*.yourdomain.com` (e.g., `collab.example.com`)
- [ ] **DNS TTL**: Set to 300 seconds (5 minutes) before go-live
- [ ] **Firewall**: Inbound allowed on ports 80 (HTTP), 443 (HTTPS)
- [ ] **Outbound**: Can reach `letsencrypt.org` (for TLS), `matrix.org` (for federation)
- [ ] **No restrictions**: No corporate firewall blocking WebDAV or XMPP protocols
- [ ] **Reverse DNS**: Helpful but not required (improves mail deliverability)

**Software Prerequisites** (install before starting deployment):
- [ ] Docker (v20.10+): `docker --version` should return `Docker version 20.10+`
- [ ] Docker Compose (v2.0+): `docker compose version` (note: `compose` not `compose-cli`)
- [ ] curl: `curl --version` works
- [ ] openssl: `openssl version` works (for certificate generation)

**Pre-Flight Checks** (run 30 minutes before deployment start):

```bash
# Check Ubuntu version
lsb_release -a
# Expected: Ubuntu 22.04 LTS (or 24.04)

# Check available RAM (need at least 14 GB free)
free -h
# Look for "Avail" row in Mem line
# Expected: Avail should show 14+ GB

# Check CPU count
nproc
# Expected: 4 or more

# Check disk free space
df -h /
# Expected: At least 100 GB available in root partition

# Verify Docker is running
docker ps
# Expected: returns without error (may show empty container list)

# Verify Docker Compose version
docker compose version
# Expected: Docker Compose version 2.0+

# Check if ports 80/443 are available
sudo ss -tlnp | grep -E ':80|:443'
# Expected: nothing listed (ports free) OR only nginx (if running old deployment)

# Test internet connectivity (needed for Let's Encrypt + federation)
curl -I https://matrix.org
# Expected: HTTP/2 200 or similar

# Test DNS resolution of your domain
nslookup yourdomain.com
# Expected: returns your server's public IP address
```

### 1.2 Information Required Before Deployment

Gather these values **before** starting; you'll need them in configuration files:

| Item | Example | Purpose |
|------|---------|---------|
| **Public Domain Name** | `collab.example.com` | nginx host, TLS certificates, Matrix federation |
| **Server Public IP** | `203.0.113.42` | DNS A record, firewall rules |
| **Timezone** | `UTC` or `America/New_York` | Log timestamps, calendar display |
| **Admin Email** | `admin@example.com` | Let's Encrypt notifications, admin account |
| **SMTP Server** (optional) | `smtp.mailer.com` | Email notifications (password reset, invites) |
| **SMTP Port** (if email) | `587` or `465` | TLS port for outbound mail |
| **SMTP Username** (if email) | `noreply@example.com` | Authenticated sender |
| **SMTP Password** (if email) | [secure] | Encryption key for mail |
| **Initial Admin Password** | [secure, 16+ chars] | Nextcloud admin login |
| **Matrix Server Name** | `example.com` | Matrix federation identity (must match domain) |
| **Meshtastic Bridge IP** (optional) | `192.168.1.100` | If integrating LoRa messaging bridge |

### 1.3 Port and Firewall Checklist

| Port | Protocol | Used By | Firewall Rule | Notes |
|------|----------|---------|---------------|-------|
| 22 | SSH | Host admin | Allow from admin IP only | Management access |
| 80 | HTTP | nginx → Let's Encrypt | Allow from anywhere | ACME challenge, redirects to 443 |
| 443 | HTTPS | nginx ← clients | Allow from anywhere | Main platform access |
| 5432 | PostgreSQL | Docker internal | Deny (internal only) | Docker network bridge, no external access |
| 6379 | Redis | Docker internal | Deny (internal only) | Docker network bridge, no external access |
| 8008 | Matrix HTTP | Docker internal | Deny (internal only) | Synapse to nginx only |
| 8448 | Matrix HTTPS | Federation | Deny if on public IP; use 443 redirect | Federation uses 443 (via SRV records) |

**UFW Configuration** (if using Ubuntu's firewall):

```bash
sudo ufw allow 22/tcp from 203.0.113.1   # Restrict SSH to admin IP
sudo ufw allow 80/tcp                    # HTTP (Let's Encrypt)
sudo ufw allow 443/tcp                   # HTTPS
sudo ufw enable
```

---

## Part 2: Pre-Deployment Setup (1-2 Hours)

### 2.1 Create Deployment Directory Structure

```bash
# Create isolated directory for this deployment
sudo mkdir -p /opt/systems-resilience-collab
sudo chown -R $(whoami):$(whoami) /opt/systems-resilience-collab
cd /opt/systems-resilience-collab

# Create subdirectories for configuration, data, and logs
mkdir -p {config,data,backups,logs,scripts}

# Create symlinks for easier reference
ln -s /opt/systems-resilience-collab ~/collab-deployment

echo "Deployment directory ready at /opt/systems-resilience-collab"
tree -L 2 /opt/systems-resilience-collab  # If tree is installed
```

### 2.2 DNS Configuration

**Before TLS setup**: DNS must point to your server. Configure A record 30+ minutes before Let's Encrypt challenge.

**Step 1: Update DNS A Record**

At your domain registrar (GoDaddy, Namecheap, Route53, etc.):

```
Record Type: A
Host: collab.example.com
Points To: 203.0.113.42  (your public IP)
TTL: 300 (5 minutes)
```

**Step 2: Verify DNS Resolution**

```bash
# Test from your local machine
nslookup collab.example.com
# Should return your public IP address

# Test from server itself
dig collab.example.com
# Should return your public IP address

# Wait for propagation (may take 1-5 minutes with TTL 300)
# If DNS isn't resolving after 5 min, troubleshoot registrar
```

**Step 3: Create DNS SRV Record (for Matrix Federation)**

Matrix homeservers use SRV records to discover federation endpoints. Add this optional record:

```
Record Type: SRV
Service: _matrix-fed._tcp
Domain: _matrix-fed._tcp.example.com
Priority: 10
Weight: 0
Port: 443
Target: collab.example.com

OR (simpler, relies on A record):
Record Type: SRV
Service: _matrix-fed._tcp
Target: collab.example.com:443
```

**Verification**:

```bash
# Test SRV record (optional but recommended for federation)
dig SRV _matrix-fed._tcp.example.com
# Should return priority/weight/port/target

# If not present, federation still works (falls back to A record)
```

### 2.3 Environment Configuration

Create `.env` file with all configuration. This file is referenced by docker-compose.yml.

```bash
cat > /opt/systems-resilience-collab/.env << 'ENVEOF'
###############################################################################
# Nextcloud + Matrix Deployment — Environment Variables
# Phase 5 systems-resilience Project
# Created: 2026-06-04
###############################################################################

# ─────────────────────────────────────────────────────────────────────────────
# 1. DEPLOYMENT ENVIRONMENT
# ─────────────────────────────────────────────────────────────────────────────

# Public domain name (CRITICAL: must match DNS A record + TLS certificate)
DOMAIN_NAME=collab.example.com

# Server timezone (affects log timestamps, calendar display)
TZ=UTC

# Deployment environment (dev/staging/production)
ENVIRONMENT=production

# ─────────────────────────────────────────────────────────────────────────────
# 2. DOCKER NETWORK & VOLUMES
# ─────────────────────────────────────────────────────────────────────────────

# Internal Docker network (subnet for container communication)
DOCKER_NETWORK=nextcloud-matrix-net
DOCKER_SUBNET=172.20.0.0/16

# Volume mount paths (change if using different storage)
NEXTCLOUD_DATA_PATH=/opt/systems-resilience-collab/data/nextcloud
MATRIX_DATA_PATH=/opt/systems-resilience-collab/data/matrix
POSTGRES_DATA_PATH=/opt/systems-resilience-collab/data/postgres
REDIS_DATA_PATH=/opt/systems-resilience-collab/data/redis

# ─────────────────────────────────────────────────────────────────────────────
# 3. DATABASE (PostgreSQL Shared by Nextcloud + Matrix)
# ─────────────────────────────────────────────────────────────────────────────

# PostgreSQL root password (CRITICAL: 32+ random chars, stored securely)
# Generate: openssl rand -base64 32
POSTGRES_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_A

# PostgreSQL user credentials (for Nextcloud)
POSTGRES_USER=nextcloud
POSTGRES_NEXTCLOUD_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_B

# PostgreSQL user credentials (for Matrix Synapse)
POSTGRES_USER_MATRIX=synapse
POSTGRES_MATRIX_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_C

# PostgreSQL database names
POSTGRES_DB=nextcloud
POSTGRES_DB_MATRIX=synapse

# PostgreSQL version (v15 recommended for both Nextcloud + Matrix)
POSTGRES_VERSION=15-alpine

# ─────────────────────────────────────────────────────────────────────────────
# 4. REDIS CACHE (Shared Session + Rate Limiting)
# ─────────────────────────────────────────────────────────────────────────────

# Redis password (CRITICAL: 32+ random chars)
REDIS_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_D

# Redis memory limit
REDIS_MAXMEMORY=1536mb

# Redis version
REDIS_VERSION=7-alpine

# ─────────────────────────────────────────────────────────────────────────────
# 5. NEXTCLOUD CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

# Nextcloud admin credentials (for first login after deployment)
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_E

# Nextcloud version
NEXTCLOUD_VERSION=29-fpm-alpine

# NextCloud Trusted Domains (IP addresses/domains that can access Nextcloud)
# Set to your domain name and localhost
NEXTCLOUD_TRUSTED_DOMAINS="collab.example.com localhost 127.0.0.1"

# OnlyOffice integration (document editing in browser)
ONLYOFFICE_SECRET=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_F
ONLYOFFICE_JWT_SECRET=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_G

# Nextcloud SMTP (email notifications, password reset)
# Leave empty to disable email, or configure below
SMTP_HOST=smtp.mailer.com
SMTP_PORT=587
SMTP_AUTH=login
SMTP_USER=noreply@example.com
SMTP_PASSWORD=REPLACE_WITH_SMTP_PASSWORD
SMTP_FROM_ADDRESS=noreply
SMTP_FROM_NAME="Systems Resilience Collab"

# ─────────────────────────────────────────────────────────────────────────────
# 6. MATRIX SYNAPSE CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

# Matrix Server Name (CRITICAL: must match domain)
# Used for user IDs (@user:example.com), federation identity
MATRIX_SERVER_NAME=example.com

# Matrix Synapse version
MATRIX_SYNAPSE_VERSION=v1.124

# Synapse signing key (CRITICAL: 64 random hex chars, unique per server)
# Generate: openssl rand -hex 32
MATRIX_SIGNING_KEY=REPLACE_WITH_64_HEX_CHAR_SIGNING_KEY

# Synapse database connection (matches PostgreSQL config above)
SYNAPSE_DB_USER=synapse
SYNAPSE_DB_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_C
SYNAPSE_DB_NAME=synapse

# Synapse Redis cache (for rate limiting, sessions)
SYNAPSE_REDIS_PASSWORD=REPLACE_WITH_RANDOM_32_CHAR_PASSWORD_D

# Allow user registration (true = users can self-register; false = admin only)
SYNAPSE_ENABLE_REGISTRATION=true

# Registration token (if enable_registration=true, this token required for signup)
# Leave empty to allow free registration, or set token value
SYNAPSE_REGISTRATION_TOKEN=REPLACE_WITH_REGISTRATION_TOKEN_OR_LEAVE_EMPTY

# Server IP for Matrix client access (usually same as public IP)
# Used by Element Web to discover homeserver
MATRIX_CLIENT_API_URL=https://collab.example.com
MATRIX_FEDERATION_URL=https://collab.example.com:8448

# ─────────────────────────────────────────────────────────────────────────────
# 7. ELEMENT WEB CONFIGURATION
# ─────────────────────────────────────────────────────────────────────────────

# Element Web version
ELEMENT_VERSION=latest

# Homeserver URL (where Element connects to Matrix)
ELEMENT_HOMESERVER_URL=https://collab.example.com
ELEMENT_HOMESERVER_NAME=example.com

# Identity server (optional, for user lookups)
# Usually points to matrix.org's identity service, or leave empty
ELEMENT_IDENTITY_SERVER=https://vector.im

# ─────────────────────────────────────────────────────────────────────────────
# 8. NGINX REVERSE PROXY & TLS
# ─────────────────────────────────────────────────────────────────────────────

# TLS certificate method: "letsencrypt" or "self-signed"
# Use "letsencrypt" for production (requires valid domain + internet)
# Use "self-signed" for testing/internal-only (browsers show warnings)
TLS_METHOD=letsencrypt

# If using Let's Encrypt: admin email for certificate notifications
LETSENCRYPT_EMAIL=admin@example.com

# If using self-signed: certificate validity days
SELF_SIGNED_DAYS=365

# nginx worker processes (usually = CPU cores)
NGINX_WORKER_PROCESSES=4

# nginx worker connections per process
NGINX_WORKER_CONNECTIONS=2048

# ─────────────────────────────────────────────────────────────────────────────
# 9. BACKUPS & DISASTER RECOVERY
# ─────────────────────────────────────────────────────────────────────────────

# Backup location (local path or remote S3)
BACKUP_PATH=/opt/systems-resilience-collab/backups

# Backup frequency (daily, weekly, monthly)
BACKUP_FREQUENCY=daily

# Backup retention (days to keep backups)
BACKUP_RETENTION_DAYS=30

# ─────────────────────────────────────────────────────────────────────────────
# 10. OPTIONAL: MESHTASTIC LORALORA BRIDGE
# ─────────────────────────────────────────────────────────────────────────────

# Enable Meshtastic bridge (true/false)
MESHTASTIC_ENABLED=false

# Meshtastic device IP address (if enabled)
MESHTASTIC_DEVICE_IP=192.168.1.100

# Meshtastic bridge port
MESHTASTIC_BRIDGE_PORT=4403

# ─────────────────────────────────────────────────────────────────────────────
# 11. MONITORING & LOGGING
# ─────────────────────────────────────────────────────────────────────────────

# Log level (debug, info, warning, error)
LOG_LEVEL=info

# Docker log driver (json-file, syslog, awslogs, etc)
LOG_DRIVER=json-file

# Docker log maximum size per file
LOG_MAX_SIZE=10m

# Docker log maximum files to retain
LOG_MAX_FILE=5

###############################################################################
# END ENVIRONMENT CONFIGURATION
###############################################################################
ENVEOF

# Verify file created
ls -l /opt/systems-resilience-collab/.env
echo "✓ Environment configuration created"
```

### 2.4 Generate Secure Passwords

Replace all `REPLACE_WITH_*` values with random, strong passwords:

```bash
# Generate 8 strong passwords (32 chars each)
for i in {1..8}; do
  echo "Password $i: $(openssl rand -base64 32 | tr -d '\n=')"
done

# OR use Python
python3 << 'PYEOF'
import secrets
for i in range(8):
    pwd = secrets.token_urlsafe(32)
    print(f"Password {i+1}: {pwd}")
PYEOF

# Edit .env with these passwords
nano /opt/systems-resilience-collab/.env
# Replace each REPLACE_WITH_* with corresponding password
# Keep file secure (600 permissions)
chmod 600 /opt/systems-resilience-collab/.env
```

### 2.5 Create Log & Data Directories

```bash
# Create all data/log directories
mkdir -p /opt/systems-resilience-collab/data/{nextcloud,matrix,postgres,redis}
mkdir -p /opt/systems-resilience-collab/logs

# Set permissions (Docker containers run as user 33/www-data)
sudo chown -R 33:33 /opt/systems-resilience-collab/data/nextcloud
sudo chown -R 101:101 /opt/systems-resilience-collab/data/matrix
sudo chown -R 999:999 /opt/systems-resilience-collab/data/postgres
sudo chown -R 999:999 /opt/systems-resilience-collab/data/redis

# Verify
ls -lR /opt/systems-resilience-collab/data/
```

---

## Part 3: Docker Compose Configuration

Create the docker-compose.yml file that defines all 5 services:

```bash
cat > /opt/systems-resilience-collab/docker-compose.yml << 'YMLEOF'
version: '3.9'

###############################################################################
# Nextcloud + Matrix Deployment — Docker Compose Configuration
# Phase 5 systems-resilience Project
# Services: PostgreSQL, Redis, Nextcloud, Matrix Synapse, Element Web, nginx
###############################################################################

networks:
  nextcloud-matrix-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.20.0.0/16

volumes:
  postgres_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ${POSTGRES_DATA_PATH}
  
  redis_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ${REDIS_DATA_PATH}
  
  nextcloud_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ${NEXTCLOUD_DATA_PATH}
  
  matrix_data:
    driver: local
    driver_opts:
      type: none
      o: bind
      device: ${MATRIX_DATA_PATH}

services:

  # ───────────────────────────────────────────────────────────────────────────
  # PostgreSQL Database (shared by Nextcloud + Matrix)
  # ───────────────────────────────────────────────────────────────────────────
  postgres:
    image: postgres:${POSTGRES_VERSION}
    container_name: nextcloud-matrix-postgres
    networks:
      nextcloud-matrix-net:
        ipv4_address: 172.20.0.2
    environment:
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_INITDB_ARGS: "-c shared_buffers=256MB -c max_connections=400"
      TZ: ${TZ}
    volumes:
      - postgres_data:/var/lib/postgresql/data
      - ./scripts/postgres-init.sql:/docker-entrypoint-initdb.d/01-init.sql:ro
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 10s
      timeout: 5s
      retries: 5
    logging:
      driver: ${LOG_DRIVER}
      options:
        max-size: ${LOG_MAX_SIZE}
        max-file: ${LOG_MAX_FILE}
    # Resource limits (prevent runaway)
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G

  # ───────────────────────────────────────────────────────────────────────────
  # Redis Cache & Session Store
  # ───────────────────────────────────────────────────────────────────────────
  redis:
    image: redis:${REDIS_VERSION}
    container_name: nextcloud-matrix-redis
    command: redis-server --requirepass ${REDIS_PASSWORD} --maxmemory ${REDIS_MAXMEMORY} --maxmemory-policy allkeys-lru
    networks:
      nextcloud-matrix-net:
        ipv4_address: 172.20.0.3
    volumes:
      - redis_data:/data
    restart: always
    healthcheck:
      test: ["CMD", "redis-cli", "--raw", "incr", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    logging:
      driver: ${LOG_DRIVER}
      options:
        max-size: ${LOG_MAX_SIZE}
        max-file: ${LOG_MAX_FILE}
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1.5G
        reservations:
          cpus: '0.5'
          memory: 512M

  # ───────────────────────────────────────────────────────────────────────────
  # Nextcloud (File Collaboration, Calendar, Contacts, WebDAV)
  # ───────────────────────────────────────────────────────────────────────────
  nextcloud:
    image: nextcloud:${NEXTCLOUD_VERSION}
    container_name: nextcloud-matrix-app
    networks:
      nextcloud-matrix-net:
        ipv4_address: 172.20.0.4
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_NEXTCLOUD_PASSWORD}
      REDIS_HOST: redis
      REDIS_HOST_PASSWORD: ${REDIS_PASSWORD}
      NEXTCLOUD_ADMIN_USER: ${NEXTCLOUD_ADMIN_USER}
      NEXTCLOUD_ADMIN_PASSWORD: ${NEXTCLOUD_ADMIN_PASSWORD}
      NEXTCLOUD_TRUSTED_DOMAINS: ${NEXTCLOUD_TRUSTED_DOMAINS}
      SMTP_HOST: ${SMTP_HOST}
      SMTP_PORT: ${SMTP_PORT}
      SMTP_SECURE: ssl
      SMTP_AUTHTYPE: ${SMTP_AUTH}
      SMTP_NAME: ${SMTP_USER}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
      MAIL_FROM_ADDRESS: ${SMTP_FROM_ADDRESS}
      MAIL_DOMAIN: ${DOMAIN_NAME}
      TZ: ${TZ}
      OVERWRITE_PROTOCOL: https
      OVERWRITE_HOST: ${DOMAIN_NAME}
    volumes:
      - nextcloud_data:/var/www/html
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost/status.php || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: ${LOG_DRIVER}
      options:
        max-size: ${LOG_MAX_SIZE}
        max-file: ${LOG_MAX_FILE}
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G

  # ───────────────────────────────────────────────────────────────────────────
  # OnlyOffice Document Server (Office document editing in browser)
  # ───────────────────────────────────────────────────────────────────────────
  onlyoffice:
    image: onlyoffice/documentserver:latest
    container_name: nextcloud-matrix-onlyoffice
    networks:
      nextcloud-matrix-net:
        ipv4_address: 172.20.0.5
    environment:
      ALLOW_PRIVATE_IP_ADDRESS: 'true'
      JWT_ENABLED: 'true'
      JWT_SECRET: ${ONLYOFFICE_JWT_SECRET}
      TZ: ${TZ}
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "curl -f http://localhost/healthcheck || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: ${LOG_DRIVER}
      options:
        max-size: ${LOG_MAX_SIZE}
        max-file: ${LOG_MAX_FILE}
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2G
        reservations:
          cpus: '1'
          memory: 1G

  # ───────────────────────────────────────────────────────────────────────────
  # Matrix Synapse Homeserver (Real-time messaging, encryption, federation)
  # ───────────────────────────────────────────────────────────────────────────
  synapse:
    image: matrixdotorg/synapse:${MATRIX_SYNAPSE_VERSION}
    container_name: nextcloud-matrix-synapse
    networks:
      nextcloud-matrix-net:
        ipv4_address: 172.20.0.6
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    volumes:
      - matrix_data:/data
      - ./config/synapse.yaml:/data/homeserver.yaml:ro
      - ./config/synapse-logging.yaml:/data/logging.yaml:ro
    environment:
      SYNAPSE_SERVER_NAME: ${MATRIX_SERVER_NAME}
      SYNAPSE_REPORT_STATS: "yes"
      TZ: ${TZ}
      POSTGRES_ENABLED: "true"
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "curl -fSs http://localhost:8008/_synapse/admin/v1/server_version || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: ${LOG_DRIVER}
      options:
        max-size: ${LOG_MAX_SIZE}
        max-file: ${LOG_MAX_FILE}
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 2.5G
        reservations:
          cpus: '1'
          memory: 1.5G

  # ───────────────────────────────────────────────────────────────────────────
  # Element Web Client (Chat interface, runs in browsers)
  # ───────────────────────────────────────────────────────────────────────────
  element:
    image: vectorim/element-web:${ELEMENT_VERSION}
    container_name: nextcloud-matrix-element
    networks:
      nextcloud-matrix-net:
        ipv4_address: 172.20.0.7
    volumes:
      - ./config/element-config.json:/app/config.json:ro
    restart: always
    healthcheck:
      test: ["CMD", "wget", "--quiet", "--tries=1", "--spider", "http://localhost"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: ${LOG_DRIVER}
      options:
        max-size: ${LOG_MAX_SIZE}
        max-file: ${LOG_MAX_FILE}
    deploy:
      resources:
        limits:
          cpus: '0.5'
          memory: 512M
        reservations:
          cpus: '0.25'
          memory: 256M

  # ───────────────────────────────────────────────────────────────────────────
  # nginx Reverse Proxy & TLS Termination
  # ───────────────────────────────────────────────────────────────────────────
  nginx:
    image: nginx:alpine
    container_name: nextcloud-matrix-nginx
    networks:
      nextcloud-matrix-net:
        ipv4_address: 172.20.0.10
    depends_on:
      - nextcloud
      - synapse
      - element
    ports:
      - "80:80"
      - "443:443"
      - "8448:8448"
    volumes:
      - ./config/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./config/default.conf:/etc/nginx/conf.d/default.conf:ro
      - ./certs:/etc/nginx/certs:ro
      - ./letsencrypt:/etc/letsencrypt:rw
      - ${NEXTCLOUD_DATA_PATH}:/nextcloud-data:ro
    environment:
      DOMAIN_NAME: ${DOMAIN_NAME}
      TZ: ${TZ}
    restart: always
    healthcheck:
      test: ["CMD-SHELL", "curl -fSs http://localhost/health || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
    logging:
      driver: ${LOG_DRIVER}
      options:
        max-size: ${LOG_MAX_SIZE}
        max-file: ${LOG_MAX_FILE}
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 512M
        reservations:
          cpus: '0.5'
          memory: 256M

###############################################################################
# END DOCKER COMPOSE
###############################################################################
YMLEOF

# Verify file created
ls -lh /opt/systems-resilience-collab/docker-compose.yml
echo "✓ Docker Compose configuration created"
```

---

## Part 4: Configuration Files (nginx, Synapse, Element)

### 4.1 PostgreSQL Initialization Script

```bash
mkdir -p /opt/systems-resilience-collab/scripts

cat > /opt/systems-resilience-collab/scripts/postgres-init.sql << 'SQLEOF'
-- PostgreSQL initialization script
-- Creates databases and users for Nextcloud + Matrix
-- Executed once at postgres startup

-- Create Nextcloud database
CREATE DATABASE nextcloud
  ENCODING 'UTF8'
  LC_COLLATE 'C'
  LC_CTYPE 'C'
  TEMPLATE template0;

-- Create Nextcloud user
CREATE USER nextcloud WITH PASSWORD 'PLACEHOLDER_NEXTCLOUD_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE nextcloud TO nextcloud;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO nextcloud;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO nextcloud;

-- Create Matrix database
CREATE DATABASE synapse
  ENCODING 'UTF8'
  LC_COLLATE 'C'
  LC_CTYPE 'C'
  TEMPLATE template0;

-- Create Matrix user
CREATE USER synapse WITH PASSWORD 'PLACEHOLDER_MATRIX_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE synapse TO synapse;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON TABLES TO synapse;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT ALL ON SEQUENCES TO synapse;

-- Create admin role for backups
CREATE ROLE backup_user WITH PASSWORD 'PLACEHOLDER_BACKUP_PASSWORD' NOCREATEDB NOCREATEROLE;
GRANT CONNECT ON DATABASE nextcloud TO backup_user;
GRANT CONNECT ON DATABASE synapse TO backup_user;
ALTER DEFAULT PRIVILEGES IN SCHEMA public GRANT SELECT ON TABLES TO backup_user;

-- Enable required extensions
\c nextcloud
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

\c synapse
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- Verify
\l
\du

SQLEOF

chmod 600 /opt/systems-resilience-collab/scripts/postgres-init.sql
echo "✓ PostgreSQL init script created"
```

### 4.2 nginx Configuration

```bash
mkdir -p /opt/systems-resilience-collab/config

cat > /opt/systems-resilience-collab/config/nginx.conf << 'CONFEOF'
# nginx configuration for Nextcloud + Matrix + Element Web
# Handles TLS termination, request routing, compression, caching

user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 2048;
    use epoll;
    multi_accept on;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    # Logging format
    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" "$http_x_forwarded_for"';

    access_log /var/log/nginx/access.log main;

    # Performance
    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    client_max_body_size 20G;  # Allow large file uploads
    proxy_buffering off;       # Disable buffering for real-time Matrix

    # Gzip compression
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml text/javascript application/json application/javascript application/xml+rss application/rss+xml application/atom+xml image/svg+xml;
    gzip_disable "msie6";

    # Rate limiting (prevent abuse)
    limit_req_zone $binary_remote_addr zone=login:10m rate=5r/s;
    limit_req_zone $binary_remote_addr zone=api:10m rate=20r/s;
    limit_req_zone $binary_remote_addr zone=matrix:10m rate=10r/s;

    # Upstream backend services
    upstream nextcloud_backend {
        least_conn;
        server nextcloud:9000 max_fails=3 fail_timeout=30s;
    }

    upstream synapse_backend {
        least_conn;
        server synapse:8008 max_fails=3 fail_timeout=30s;
    }

    upstream element_backend {
        server element:80 max_fails=3 fail_timeout=30s;
    }

    upstream onlyoffice_backend {
        server onlyoffice:80 max_fails=3 fail_timeout=30s;
    }

    # HTTP redirect to HTTPS
    server {
        listen 80 default_server;
        listen [::]:80 default_server;
        server_name _;

        location /.well-known/acme-challenge/ {
            root /var/www/certbot;
        }

        location / {
            return 301 https://$host$request_uri;
        }
    }

    # HTTPS main server block
    server {
        listen 443 ssl http2 default_server;
        listen [::]:443 ssl http2 default_server;
        server_name DOMAIN_NAME;

        # TLS certificates
        ssl_certificate /etc/nginx/certs/cert.pem;
        ssl_certificate_key /etc/nginx/certs/key.pem;
        ssl_trusted_certificate /etc/nginx/certs/chain.pem;

        # TLS security
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;
        ssl_prefer_server_ciphers on;
        ssl_session_cache shared:SSL:10m;
        ssl_session_timeout 10m;
        ssl_stapling on;
        ssl_stapling_verify on;

        # Security headers
        add_header Strict-Transport-Security "max-age=31536000; includeSubDomains; preload" always;
        add_header X-Content-Type-Options "nosniff" always;
        add_header X-Frame-Options "SAMEORIGIN" always;
        add_header X-XSS-Protection "1; mode=block" always;
        add_header Referrer-Policy "strict-origin-when-cross-origin" always;

        # Root location: delegate to Nextcloud
        location / {
            proxy_pass http://nextcloud_backend;
            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            proxy_set_header X-Forwarded-Host $host;
        }

        # Nextcloud WebDAV (file sync protocol)
        location /.well-known/dav {
            return 301 $scheme://$host/remote.php/dav;
        }

        # Matrix homeserver (/_matrix is the API)
        location /_matrix {
            limit_req zone=matrix burst=20 nodelay;
            proxy_pass http://synapse_backend;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection $connection_upgrade;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
            # Matrix-specific timeouts (long-polling)
            proxy_connect_timeout 600s;
            proxy_send_timeout 600s;
            proxy_read_timeout 600s;
            send_timeout 600s;
        }

        # Matrix federation (/_matrix-fed)
        location /_matrix-fed {
            limit_req zone=matrix burst=20 nodelay;
            proxy_pass http://synapse_backend:8008;
            proxy_http_version 1.1;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Element Web UI
        location /element {
            proxy_pass http://element_backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # OnlyOffice document server
        location /onlyoffice {
            proxy_pass http://onlyoffice_backend;
            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection $connection_upgrade;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }

        # Health check endpoint
        location /health {
            access_log off;
            return 200 "OK\n";
            add_header Content-Type text/plain;
        }
    }

    # Matrix federation port 8448 (for server-to-server)
    server {
        listen 8448 ssl http2;
        listen [::]:8448 ssl http2;
        server_name DOMAIN_NAME;

        ssl_certificate /etc/nginx/certs/cert.pem;
        ssl_certificate_key /etc/nginx/certs/key.pem;
        ssl_protocols TLSv1.2 TLSv1.3;
        ssl_ciphers HIGH:!aNULL:!MD5;

        location / {
            proxy_pass http://synapse_backend;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Proto $scheme;
        }
    }

    # WebSocket support for Matrix/Element (long-polling)
    map $http_upgrade $connection_upgrade {
        default upgrade;
        '' close;
    }
}
CONFEOF

echo "✓ nginx configuration created"
```

### 4.3 Matrix Synapse Configuration

This is generated during first startup, but we'll create a template for reference:

```bash
cat > /opt/systems-resilience-collab/config/synapse.yaml << 'SYNAPSEEOF'
# Matrix Synapse homeserver configuration
# Generated for systems-resilience Phase 5 project
# Reference: https://matrix-org.github.io/synapse/latest/usage/configuration/config_documentation.html

server_name: "MATRIX_SERVER_NAME"
pid_file: /data/homeserver.pid

listeners:
  - port: 8008
    type: http
    tls: false
    resources:
      - names: [client, federation]
        compress: true

database:
  name: psycopg2
  args:
    user: synapse
    password: "SYNAPSE_DB_PASSWORD"
    database: synapse
    host: postgres
    port: 5432
    cp_min: 5
    cp_max: 10

redis:
  enabled: true
  host: redis
  port: 6379
  password: "SYNAPSE_REDIS_PASSWORD"

log_config: "/data/logging.yaml"

media_store_path: "/data/media_store"

registration_requires_token: false

enable_registration: true

# Admin users
admin_users:
  - "@admin:MATRIX_SERVER_NAME"

# Trusted key servers (federation)
trusted_key_servers:
  - server_name: "matrix.org"

# Room name length limits
room_invite_state_types:
  - m.room.join_rules
  - m.room.avatar
  - m.room.canonical_alias
  - m.room.guest_access
  - m.room.history_visibility
  - m.room.name
  - m.room.topic
  - m.room.encryption

# TURN server (optional, for NAT traversal in video calls)
turn_uris: []
turn_shared_secret: "TURN_SECRET"
turn_user_lifetime: 86400000
turn_allow_guests: true

# Federation
federation_domain_whitelist: []  # Empty = allow all

# Email notifications
email:
  enabled: false

# Rate limiting
rc_message:
  per_second: 0.17
  burst_count: 3.33

rc_registration:
  per_second: 0.17
  burst_count: 3

rc_login:
  per_second: 0.17
  burst_count: 3

# Metrics/Prometheus
metrics_port: 8090

# Max request body size (20GB for media)
max_upload_size: 20G

# Thumbnails
thumbnail_sizes:
  - width: 32
    height: 32
    method: crop
  - width: 96
    height: 96
    method: crop
  - width: 320
    height: 240
    method: scale
  - width: 640
    height: 480
    method: scale
  - width: 1024
    height: 768
    method: scale

SYNAPSEEOF

echo "✓ Matrix Synapse config template created"
```

### 4.4 Element Web Configuration

```bash
cat > /opt/systems-resilience-collab/config/element-config.json << 'ELEMENTEOF'
{
  "default_server_config": {
    "m.homeserver": {
      "base_url": "https://DOMAIN_NAME",
      "server_name": "MATRIX_SERVER_NAME"
    },
    "m.identity_server": {
      "base_url": "https://vector.im"
    }
  },
  "brand": "Element",
  "integrations_ui_url": "https://scalar.vector.im/",
  "integrations_rest_url": "https://scalar.vector.im/api/v1/scalar",
  "show_labs_settings": true,
  "features": {
    "feature_cross_signing": "enable",
    "feature_event_indexing": "enable"
  },
  "bug_report_endpoint_url": "https://riot.im/bugreports/submit",
  "roomDirectory": {
    "servers": ["matrix.org"]
  },
  "security": {
    "privacy_notice": null
  },
  "registration": {
    "audience": "https://DOMAIN_NAME",
    "brand": "Systems Resilience Collab"
  },
  "permalinkPrefix": "https://app.element.io"
}
ELEMENTEOF

echo "✓ Element Web config created"
```

---

## Part 5: TLS Certificate Setup (Let's Encrypt or Self-Signed)

### 5.1 Let's Encrypt (Recommended for Production)

```bash
# Create certificate directory
mkdir -p /opt/systems-resilience-collab/certs
chmod 700 /opt/systems-resilience-collab/certs

# Install Certbot (if not already installed)
sudo apt-get update && sudo apt-get install -y certbot python3-certbot-dns-route53
# OR for other DNS providers:
# sudo apt-get install -y certbot python3-certbot-dns-cloudflare

# Generate certificate using manual DNS challenge
# (This requires updating DNS TXT records)
sudo certbot certonly \
  --manual \
  --preferred-challenges=dns \
  --email admin@example.com \
  --no-eff-email \
  --agree-tos \
  -d collab.example.com \
  -d *.collab.example.com

# When prompted, add the DNS TXT record shown by certbot
# Wait for DNS propagation, then continue

# Copy certificates to docker directory
sudo cp /etc/letsencrypt/live/collab.example.com/fullchain.pem \
   /opt/systems-resilience-collab/certs/cert.pem
sudo cp /etc/letsencrypt/live/collab.example.com/privkey.pem \
   /opt/systems-resilience-collab/certs/key.pem
sudo cp /etc/letsencrypt/live/collab.example.com/chain.pem \
   /opt/systems-resilience-collab/certs/chain.pem

# Set permissions
sudo chown $(whoami):$(whoami) /opt/systems-resilience-collab/certs/*
chmod 600 /opt/systems-resilience-collab/certs/*

# Auto-renewal (runs daily)
sudo systemctl enable certbot.timer
sudo systemctl start certbot.timer
```

### 5.2 Self-Signed Certificate (Testing Only)

```bash
# Generate 365-day self-signed certificate
openssl req -x509 -newkey rsa:4096 -keyout /opt/systems-resilience-collab/certs/key.pem \
  -out /opt/systems-resilience-collab/certs/cert.pem -days 365 -nodes \
  -subj "/C=US/ST=State/L=City/O=Systems Resilience/CN=collab.example.com"

# Copy for nginx compatibility
cp /opt/systems-resilience-collab/certs/cert.pem /opt/systems-resilience-collab/certs/chain.pem

chmod 600 /opt/systems-resilience-collab/certs/*

echo "⚠️  Self-signed certificate created (browsers will show warnings)"
```

---

## Part 6: Docker Deployment (30 minutes)

### 6.1 Start All Services

```bash
cd /opt/systems-resilience-collab

# Source environment
source .env

# Verify .env is loaded
echo "Domain: $DOMAIN_NAME"
echo "Timezone: $TZ"

# Start all containers in background
docker compose up -d

# Wait for services to initialize (2-3 minutes)
echo "Waiting for services to initialize..."
sleep 30

# Check status
docker compose ps
# Expected: all services showing "healthy" or "running"

# View startup logs
docker compose logs --tail=50

# Check for errors
docker compose logs postgres  | tail -20
docker compose logs redis     | tail -20
docker compose logs nextcloud | tail -20
docker compose logs synapse   | tail -20
docker compose logs element   | tail -20
docker compose logs nginx     | tail -20
```

### 6.2 Health Verification

```bash
# Wait for all services to be healthy (may take 3-5 minutes)
echo "Checking service health..."
for i in {1..30}; do
  docker compose ps | grep -E "healthy|running"
  if [ $? -eq 0 ]; then
    echo "✓ All services initialized"
    break
  fi
  echo "  Waiting... ($i/30)"
  sleep 10
done

# Test each service endpoint
echo "Testing service endpoints..."

# Test nginx (should return 200)
curl -k https://localhost/health
# Expected: "OK"

# Test Nextcloud
curl -k https://localhost/status.php
# Expected: JSON with "installed":true

# Test Matrix
curl https://localhost/_matrix/client/versions
# Expected: JSON with "versions": [...]

# Test Element (should return HTML)
curl -k https://localhost/ | head -10

# View full service logs
docker compose logs --follow
```

---

## Part 7: Post-Deployment Configuration (1-2 Hours)

### 7.1 Nextcloud Setup

Access Nextcloud web interface:

```bash
# Open browser to:
# https://collab.example.com

# You should see login page
# Use credentials from .env:
# Username: (value of NEXTCLOUD_ADMIN_USER)
# Password: (value of NEXTCLOUD_ADMIN_PASSWORD)

# After login, you'll see setup wizard
```

**Nextcloud Configuration Steps**:

1. **Data Directory**: Accept default `/var/www/html/data`
2. **Database**: Select "PostgreSQL"
   - Host: `postgres`
   - Port: `5432`
   - Database: `nextcloud`
   - User: (from .env POSTGRES_USER)
   - Password: (from .env POSTGRES_NEXTCLOUD_PASSWORD)
3. **Admin Account**: Already set during environment config
4. **Install Apps** (via Settings → Apps → search):
   - OnlyOffice (document editing)
   - Deck (task management)
   - Calendar
   - Contacts
   - Tasks

### 7.2 Matrix Synapse Setup

```bash
# Register admin user (interactive)
docker compose exec synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u admin \
  -p (your-admin-password) \
  -a yes https://collab.example.com

# Verify admin user created
docker compose exec synapse sqlite3 /data/homeserver.db \
  "SELECT name FROM users WHERE admin=1;"

# Create test room (optional)
docker compose exec synapse curl -X POST \
  -H 'Content-Type: application/json' \
  -d '{"room_alias_name":"test"}' \
  'http://localhost:8008/_matrix/client/r0/createRoom?access_token=YOUR_TOKEN'
```

### 7.3 Element Web Setup

Access Element:

```bash
# Open browser to:
# https://collab.example.com

# Select "Create an account"
# Or "Sign in" with existing Matrix account

# After first login, Element asks for:
# - Display name
# - Avatar (optional)
# - Recovery method (backup phrase or security key)

# Recommended: enable encryption & backup
# Settings → Security & Privacy → Backup & Recovery
```

### 7.4 User & Group Management

**Create Local User Accounts** (admin login required):

```bash
# Via web GUI:
# Settings → Users → "New User"

# Or via command line:
docker compose exec synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u alice \
  -p alice-password \
  --no-admin https://collab.example.com
```

**Create Rooms for Teams**:

In Element Web:
1. Click "+" (Create Room)
2. Set room name: "Wave 1 Authors" or similar
3. Set visibility: "Private"
4. Add members: invite by username @user:collab.example.com
5. Enable encryption: Settings → Security → "Enable encryption" (toggle)

**Setup Nextcloud Groups** (for collaborative folders):

```bash
# Via Nextcloud web GUI:
# Settings → Administration → User Management → Groups → "Create new group"

# Or via command line:
docker compose exec nextcloud sudo -u www-data php occ group:create wave1-authors
docker compose exec nextcloud sudo -u www-data php occ group:adduser wave1-authors alice
```

---

## Part 8: Offline Sync Configuration

### 8.1 Nextcloud Desktop Client (Author's Machine)

**Installation** (on author's laptop):

```bash
# Ubuntu/Debian
sudo apt-get install nextcloud-client

# macOS
brew install nextcloud-client

# Windows
# Download from https://nextcloud.com/install/#install-clients
```

**Configuration**:

1. Launch Nextcloud Desktop Client
2. Enter server: `https://collab.example.com`
3. Login with Nextcloud credentials
4. Select folders to sync (or "Sync all")
5. Set local sync path: `~/Nextcloud` (or custom location)
6. Enable "Offline Support" (Settings → Sync)

**Testing Offline Sync**:

```bash
# On author's computer:
# 1. Go online, open document in Nextcloud Desktop
# 2. Document is cached to ~/Nextcloud/folder/doc.docx
# 3. Disconnect network (airplane mode, unplug ethernet)
# 4. Open local copy in OnlyOffice (via desktop client)
# 5. Make edits offline
# 6. Reconnect network
# 7. Client automatically syncs changes back to server
```

### 8.2 Browser Offline Mode

**OnlyOffice Offline Support**:

1. Open document in Nextcloud web UI
2. Click "Edit" → "OnlyOffice Editor"
3. Browser caches document in local storage (IndexedDB)
4. If network drops, cached version remains accessible
5. Edits are queued locally
6. When reconnected, changes push to server

---

## Part 9: Backup & Disaster Recovery

### 9.1 Automated Daily Backups

```bash
mkdir -p /opt/systems-resilience-collab/scripts/backup

cat > /opt/systems-resilience-collab/scripts/backup/backup-daily.sh << 'BACKUPEOF'
#!/bin/bash
# Daily backup script for Nextcloud + Matrix deployment

set -e

BACKUP_DIR="/opt/systems-resilience-collab/backups"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_${TIMESTAMP}"

mkdir -p "$BACKUP_DIR/$BACKUP_NAME"

echo "[$(date)] Starting daily backup..."

# 1. Backup Nextcloud files
echo "[$(date)] Backing up Nextcloud files..."
docker compose exec -T nextcloud tar czf - /var/www/html/data \
  > "$BACKUP_DIR/$BACKUP_NAME/nextcloud-files.tar.gz"

# 2. Backup Matrix media
echo "[$(date)] Backing up Matrix media..."
tar czf "$BACKUP_DIR/$BACKUP_NAME/matrix-media.tar.gz" \
  /opt/systems-resilience-collab/data/matrix/media_store

# 3. Backup PostgreSQL database (both nextcloud + synapse)
echo "[$(date)] Backing up PostgreSQL database..."
docker compose exec -T postgres pg_dump -U postgres \
  | gzip > "$BACKUP_DIR/$BACKUP_NAME/postgres-backup.sql.gz"

# 4. Backup nginx config
echo "[$(date)] Backing up nginx config..."
tar czf "$BACKUP_DIR/$BACKUP_NAME/nginx-config.tar.gz" \
  /opt/systems-resilience-collab/config

# 5. Remove old backups (keep 30 days)
echo "[$(date)] Cleaning up old backups..."
find "$BACKUP_DIR" -type d -name "backup_*" -mtime +30 -exec rm -rf {} + 2>/dev/null || true

# 6. Verify backup
BACKUP_SIZE=$(du -sh "$BACKUP_DIR/$BACKUP_NAME" | cut -f1)
echo "[$(date)] Backup complete. Size: $BACKUP_SIZE"

# 7. Log backup
echo "[$(date)] Backup: $BACKUP_NAME (Size: $BACKUP_SIZE)" \
  >> "$BACKUP_DIR/backup.log"

BACKUPEOF

chmod +x /opt/systems-resilience-collab/scripts/backup/backup-daily.sh
```

**Schedule Daily Backup with Cron**:

```bash
# Edit crontab
crontab -e

# Add this line (runs daily at 02:00 UTC)
0 2 * * * /opt/systems-resilience-collab/scripts/backup/backup-daily.sh

# Verify
crontab -l
```

### 9.2 Disaster Recovery Procedure

**Restore from Backup**:

```bash
# Step 1: Stop services
cd /opt/systems-resilience-collab
docker compose down

# Step 2: Restore PostgreSQL database
docker compose up -d postgres
docker compose exec -T postgres psql -U postgres \
  < /opt/systems-resilience-collab/backups/backup_YYYYMMDD_HHMMSS/postgres-backup.sql.gz

# Step 3: Restore Nextcloud files
docker compose up -d nextcloud
docker compose exec -T nextcloud tar xzf - \
  < /opt/systems-resilience-collab/backups/backup_YYYYMMDD_HHMMSS/nextcloud-files.tar.gz

# Step 4: Restore Matrix media
tar xzf /opt/systems-resilience-collab/backups/backup_YYYYMMDD_HHMMSS/matrix-media.tar.gz \
  -C /opt/systems-resilience-collab/data/

# Step 5: Restart all services
docker compose up -d

# Step 6: Verify restore
docker compose logs --tail=50
curl -k https://localhost/status.php
```

---

## Part 10: Monitoring & Troubleshooting

### 10.1 Health Checks & Logs

```bash
# View all service logs in real-time
docker compose logs -f

# View specific service logs
docker compose logs postgres    # Database
docker compose logs synapse     # Matrix
docker compose logs nextcloud   # Files
docker compose logs nginx       # Reverse proxy

# View last 50 lines of logs
docker compose logs --tail=50

# Follow logs with timestamps
docker compose logs -f --timestamps

# Save logs to file for analysis
docker compose logs > /opt/systems-resilience-collab/logs/debug-full.log
```

### 10.2 Service Status Commands

```bash
# Check all service status
docker compose ps

# Restart specific service
docker compose restart nextcloud

# Restart all services
docker compose restart

# Force rebuild (if config changed)
docker compose up -d --force-recreate

# View resource usage
docker stats

# Check network connectivity between services
docker compose exec nextcloud ping postgres
docker compose exec synapse ping redis
```

### 10.3 Common Issues & Solutions

**Issue: "connection refused" when accessing nginx**

```bash
# Check if nginx is running
docker compose ps nginx

# Check nginx error log
docker compose logs nginx | grep -i error

# Verify port 443 is accessible
sudo netstat -tlnp | grep 443

# Test nginx health
curl -k https://localhost/health

# If nginx fails, check certificate paths
ls -lh /opt/systems-resilience-collab/certs/
```

**Issue: Nextcloud showing "Error: Connect to database failed"**

```bash
# Check PostgreSQL status
docker compose ps postgres

# Verify PostgreSQL is accepting connections
docker compose exec postgres psql -U postgres -c "SELECT 1;"

# Check if Nextcloud can reach PostgreSQL
docker compose exec nextcloud nc -zv postgres 5432

# Verify .env passwords match docker-compose.yml
grep POSTGRES_PASSWORD /opt/systems-resilience-collab/.env
grep POSTGRES_NEXTCLOUD_PASSWORD /opt/systems-resilience-collab/.env

# Rebuild Nextcloud container if needed
docker compose up -d --force-recreate nextcloud
```

**Issue: Matrix federation not working (other servers can't reach yours)**

```bash
# Test Matrix client API
curl https://collab.example.com/_matrix/client/versions

# Test federation endpoint
curl https://collab.example.com:8448/_matrix/federation/v1/version

# Check DNS SRV record (optional but helpful)
dig SRV _matrix-fed._tcp.example.com

# Verify port 8448 is accessible from internet
sudo nmap -p 8448 your-public-ip  # from external machine

# Check firewall rules
sudo ufw status
sudo ufw allow 8448/tcp
```

**Issue: OnlyOffice documents won't open or edit**

```bash
# Check OnlyOffice service
docker compose ps onlyoffice
docker compose logs onlyoffice | tail -20

# Verify JWT secret is configured in Nextcloud
docker compose exec nextcloud sudo -u www-data php occ config:get onlyoffice

# Restart OnlyOffice
docker compose restart onlyoffice

# Test OnlyOffice health endpoint
curl http://localhost:8443/healthcheck || \
  docker compose exec onlyoffice curl http://localhost/healthcheck
```

---

## Part 11: Operational Runbooks

### 11.1 Daily Operations Checklist

```bash
# Run daily (automated via cron or manual)
echo "=== Daily Nextcloud + Matrix Operational Check ==="

# 1. Service health
docker compose ps | grep -E "healthy|running"

# 2. Disk space (alert if <20% free)
df -h /opt/systems-resilience-collab | tail -1

# 3. Check logs for errors (last 100 lines)
docker compose logs --tail=100 | grep -i -E "error|critical|fail" | wc -l

# 4. Test web access
curl -k https://collab.example.com/health

# 5. Backup verification (backup from previous night)
ls -lh /opt/systems-resilience-collab/backups/ | tail -2
```

### 11.2 Weekly Maintenance

```bash
# Run weekly (e.g., Sunday 01:00 UTC)

# 1. Update Docker images (optional, test in staging first)
docker compose pull

# 2. Restart services gracefully
docker compose restart

# 3. Run database optimization
docker compose exec -T postgres vacuumdb -U postgres -d nextcloud
docker compose exec -T postgres vacuumdb -U postgres -d synapse

# 4. Review logs for warnings
docker compose logs --since=7d | grep -i "warn" | head -20

# 5. Test disaster recovery (restore from backup to temp location)
# See Part 9.2 for restore procedure
```

### 11.3 Monthly Maintenance

```bash
# Run monthly (e.g., first Sunday of month, 00:00 UTC)

# 1. Full backup audit
ls /opt/systems-resilience-collab/backups/ | wc -l
du -sh /opt/systems-resilience-collab/backups/

# 2. Certificate renewal check (if using Let's Encrypt)
sudo certbot renew --dry-run

# 3. Clean old logs (keep 90 days)
find /opt/systems-resilience-collab/logs -name "*.log" -mtime +90 -delete

# 4. Update system packages
sudo apt-get update && sudo apt-get upgrade -y

# 5. Reboot server (if kernel updates were applied)
sudo reboot
```

---

## Part 12: Security Hardening

### 12.1 Network Security

```bash
# Firewall configuration (UFW)
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 203.0.113.1 to any port 22  # SSH from admin IP only
sudo ufw allow 80/tcp                           # HTTP
sudo ufw allow 443/tcp                          # HTTPS
sudo ufw allow 8448/tcp                         # Matrix federation
sudo ufw enable

# Fail2ban (prevent brute force attacks)
sudo apt-get install fail2ban
sudo systemctl enable fail2ban
sudo systemctl start fail2ban

# Rate limiting (via nginx config, already set)
# See Part 4.2 for rate limiting rules
```

### 12.2 Container Security

```bash
# Run security scan on Docker images
docker scan nextcloud:29-fpm-alpine
docker scan matrixdotorg/synapse:latest
docker scan postgres:15-alpine

# Update docker-compose to use specific versions (not :latest)
# and regularly pull updates:
docker compose pull
docker compose up -d
```

### 12.3 Database Security

```bash
# PostgreSQL password rotation (monthly)
docker compose exec postgres psql -U postgres -c \
  "ALTER USER nextcloud WITH PASSWORD 'NEW_PASSWORD';"

# Backup database encryption (encrypt to disk)
gpg --encrypt /opt/systems-resilience-collab/backups/backup_*/postgres-backup.sql.gz

# Restrict database backups to read-only user
# (already configured in postgres-init.sql)
```

---

## Part 13: Timeline & Success Criteria

### Deployment Timeline

| Phase | Task | Estimated Time | Success Criteria |
|-------|------|-----------------|------------------|
| 1 | Pre-flight checklist + DNS config | 30 min | DNS resolves, ports accessible |
| 2 | Environment setup + SSL certs | 1-1.5 hrs | Certificates generated, .env populated |
| 3 | Docker deployment | 30 min | All services showing "healthy" in docker ps |
| 4 | Post-deployment config | 1-2 hrs | Nextcloud login works, Matrix user created |
| 5 | Testing + user creation | 30 min | 5+ test users created, offline sync tested |
| **TOTAL** | | **4-6 hours** | **Platform ready for authors by June 5 13:00 UTC** |

### Success Verification Checklist

- [ ] Platform accessible at https://collab.example.com with valid TLS certificate
- [ ] Nextcloud admin login works (from .env credentials)
- [ ] Matrix admin user created and can login via Element
- [ ] 5+ test author accounts created (local or LDAP)
- [ ] Offline document editing tested (Nextcloud Desktop sync + OnlyOffice browser cache)
- [ ] Real-time chat tested (Element Web, send/receive messages)
- [ ] Room creation and permissions tested
- [ ] File upload/download tested (20MB+ file)
- [ ] End-to-end encryption verified (E2E room flag visible in Element)
- [ ] Backup script runs without errors
- [ ] All services restart cleanly after `docker compose restart`

---

## Final Notes

### When to Troubleshoot vs. Re-deploy

- **Troubleshoot if**: specific service unhealthy but others working, cert expired, configuration typo
- **Re-deploy if**: multiple services consistently failing, data corruption suspected, major version upgrade

### Scaling to 300+ Users

For Phase 6 expansion to 300+ users:

1. Increase PostgreSQL to 4GB RAM
2. Move PostgreSQL to separate host (optional but recommended)
3. Split Matrix Synapse to separate container with dedicated Redis
4. Monitor CPU usage; may need to increase cores

### Community Governance & Room Setup

After deployment, create initial room structure for Phase 5 authors:

```
💬 General Announcements (public)
💬 Wave 1 Authors Discussion (private, invite-only)
📁 Wave 1 Documents (shared folder, offline-sync enabled)
📁 Research Resources (reference materials)
📁 Backups & Recovery (operational docs)
```

This structure supports the author recruitment and collaborative editing workflows described in PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md.

---

**Document Status**: PRODUCTION-READY  
**Last Updated**: 2026-06-04  
**For support**: See troubleshooting in Part 10, or refer to official docs at nextcloud.com, matrix.org
