---
title: "Nextcloud + Matrix Deployment Technical Specification"
project: systems-resilience
platform: "Nextcloud 29 + Matrix Synapse + Element Web"
created: 2026-06-14
purpose: "Technical specification for June 14-15 platform decision. Covers resource requirements, Docker compose configuration, known Pi5 constraints, backup procedures, and troubleshooting."
decision_context: "User is choosing between Nextcloud+Matrix (this doc) and Discourse (DISCOURSE_DEPLOYMENT_TECHNICAL_SPEC.md). See PLATFORM_DECISION_MATRIX_WITH_RUNBOOKS.md for side-by-side comparison."
---

# Nextcloud + Matrix Deployment Technical Specification
## Raspberry Pi 5 (8GB RAM, ARM64) — June 14, 2026

---

## 1. Infrastructure Requirements

### Hardware Requirements

| Resource | Minimum | Recommended | Pi5 (ours) | Status |
|----------|---------|-------------|------------|--------|
| RAM | 16 GB | 32 GB | 8 GB | MARGINAL |
| CPU cores | 4 | 8 | 4 (ARM Cortex-A76) | ADEQUATE |
| Free storage | 100 GB | 300 GB | ~189 GB | ADEQUATE |
| Network | 100 Mbps | 1 Gbps | Tailscale/home | ADEQUATE |

**RAM Assessment (CRITICAL)**: The Pi5 has 8 GB total RAM. With OS overhead (~500 MB) and Docker daemon (~200 MB), the usable headroom for containers is ~7.3 GB. The Nextcloud+Matrix stack at idle consumes:

| Container | Idle RAM | Under load (50 users) |
|-----------|---------|----------------------|
| PostgreSQL (shared) | 300–500 MB | 700 MB–1.2 GB |
| Redis | 50–100 MB | 100–200 MB |
| Nextcloud (PHP-FPM) | 400–600 MB | 900 MB–1.5 GB |
| Matrix Synapse | 300–500 MB | 600 MB–1 GB |
| Element Web | 50–100 MB | 100–150 MB |
| OnlyOffice | 400–700 MB | 800 MB–1.5 GB |
| nginx | 20–50 MB | 50–100 MB |
| **TOTAL** | **1.5–2.5 GB** | **3.2–5.6 GB** |

With 7.3 GB usable: there is a 1.7–4.1 GB margin. At 100 concurrent users this margin collapses. At 50 concurrent users it is manageable if OnlyOffice is not active simultaneously.

**Mitigation**: Disable OnlyOffice if RAM pressure is observed. Nextcloud file access (read/download) still works without OnlyOffice; only collaborative editing is affected.

### ARM64 Compatibility

Docker images with confirmed ARM64 (`linux/arm64`) support as of 2026:
- `nextcloud:29-fpm-alpine` — official ARM64 image (confirmed)
- `postgres:16-alpine` — official ARM64 image (confirmed)
- `redis:7-alpine` — official ARM64 image (confirmed)
- `matrixdotorg/synapse:latest` — official ARM64 image (confirmed)
- `vectorim/element-web:latest` — official ARM64 image (confirmed)
- `onlyoffice/documentserver` — **x86-64 only** (no ARM64 support)

**OnlyOffice is not deployable on Pi5 ARM64.** Collaborative real-time editing is not available on this hardware. Authors can still upload documents and share files; they cannot co-edit documents simultaneously in-browser.

**Alternative for collaborative editing**: Use Nextcloud's built-in Markdown editor (Markdown text editing, no Word-format support) or have authors use desktop clients (Nextcloud Desktop app) for local edits + sync.

---

## 2. Docker Compose Configuration

### 2.1 Service Topology

Seven services are required. OnlyOffice is omitted on Pi5 ARM64.

```
nginx (443/80, TLS termination)
  ├─ nextcloud:9000 (PHP-FPM, FastCGI)
  ├─ synapse:8008 (Matrix homeserver)
  └─ element:80 (static web client)

nextcloud → postgres:5432
nextcloud → redis:6379
synapse → postgres:5432
synapse → redis:6379
```

### 2.2 docker-compose.yml Template

Save to `/opt/nextcloud-matrix/docker-compose.yml`. Fill in all `REPLACE_*` values before starting.

```yaml
# /opt/nextcloud-matrix/docker-compose.yml
# Nextcloud + Matrix deployment — Raspberry Pi 5 (ARM64)
# Generated 2026-06-14 for systems-resilience Phase 5 deployment

networks:
  backend:
    driver: bridge

volumes:
  postgres_data:
  redis_data:
  nextcloud_data:
  nextcloud_config:
  nginx_certs:
  synapse_data:
  element_config:

services:

  # ─── Database (shared by Nextcloud and Matrix/Synapse) ───────────────────────
  postgres:
    image: postgres:16-alpine
    restart: unless-stopped
    networks:
      - backend
    environment:
      POSTGRES_USER: REPLACE_POSTGRES_USER
      POSTGRES_PASSWORD: REPLACE_POSTGRES_PASSWORD
      POSTGRES_MULTIPLE_DATABASES: "nextcloud,synapse"
    volumes:
      - postgres_data:/var/lib/postgresql/data
      # Script to create multiple databases on first init:
      - ./init-multiple-databases.sh:/docker-entrypoint-initdb.d/init.sh:ro
    # Pi5-tuned PostgreSQL memory settings
    command: >
      postgres
        -c shared_buffers=256MB
        -c effective_cache_size=512MB
        -c work_mem=32MB
        -c maintenance_work_mem=64MB
        -c max_connections=100
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U REPLACE_POSTGRES_USER -d nextcloud"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 60s
    # Bind to backend network only — never expose to host directly
    # ports intentionally omitted

  # ─── Redis (shared cache) ─────────────────────────────────────────────────────
  redis:
    image: redis:7-alpine
    restart: unless-stopped
    networks:
      - backend
    command: redis-server --maxmemory 256mb --maxmemory-policy allkeys-lru
    volumes:
      - redis_data:/data
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 30s
      timeout: 10s
      retries: 5

  # ─── Nextcloud (PHP-FPM) ─────────────────────────────────────────────────────
  nextcloud:
    image: nextcloud:29-fpm-alpine
    restart: unless-stopped
    networks:
      - backend
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_DB: nextcloud
      POSTGRES_USER: REPLACE_POSTGRES_USER
      POSTGRES_PASSWORD: REPLACE_POSTGRES_PASSWORD
      REDIS_HOST: redis
      NEXTCLOUD_ADMIN_USER: REPLACE_NEXTCLOUD_ADMIN_USER
      NEXTCLOUD_ADMIN_PASSWORD: REPLACE_NEXTCLOUD_ADMIN_PASSWORD
      NEXTCLOUD_TRUSTED_DOMAINS: "REPLACE_NEXTCLOUD_HOSTNAME"
      SMTP_HOST: REPLACE_SMTP_HOST
      SMTP_SECURE: tls
      SMTP_PORT: 587
      SMTP_AUTHTYPE: LOGIN
      SMTP_NAME: REPLACE_SMTP_USER
      SMTP_PASSWORD: REPLACE_SMTP_PASSWORD
      MAIL_FROM_ADDRESS: noreply
      MAIL_DOMAIN: REPLACE_YOUR_DOMAIN
      # Performance: PHP-FPM process count for Pi5 (4-core ARM)
      PHP_UPLOAD_LIMIT: 512M
      PHP_MEMORY_LIMIT: 512M
    volumes:
      - nextcloud_data:/var/www/html/data
      - nextcloud_config:/var/www/html/config
      # html volume shared with nginx for static assets:
      - nextcloud_html:/var/www/html
    # FPM does not serve HTTP — no ports exposed to host
    # nginx handles HTTP; it reads from the shared html volume
    healthcheck:
      test: ["CMD-SHELL", "php-fpm -t && echo OK"]
      interval: 60s
      timeout: 30s
      retries: 3
      start_period: 120s
    deploy:
      resources:
        limits:
          memory: 1.5G

  # ─── Matrix Synapse Homeserver ────────────────────────────────────────────────
  synapse:
    image: matrixdotorg/synapse:latest
    restart: unless-stopped
    networks:
      - backend
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      SYNAPSE_SERVER_NAME: REPLACE_MATRIX_HOSTNAME
      SYNAPSE_REPORT_STATS: "no"
    volumes:
      - synapse_data:/data
      - ./synapse/homeserver.yaml:/data/homeserver.yaml:ro
    # Synapse HTTP API on port 8008 (internal only)
    healthcheck:
      test: ["CMD-SHELL", "curl -sf http://localhost:8008/_matrix/client/versions || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 5
      start_period: 90s
    deploy:
      resources:
        limits:
          memory: 1G

  # ─── Element Web (Matrix client) ──────────────────────────────────────────────
  element:
    image: vectorim/element-web:latest
    restart: unless-stopped
    networks:
      - backend
    volumes:
      - element_config:/app/config:ro
      - ./element/config.json:/app/config/config.json:ro
    healthcheck:
      test: ["CMD-SHELL", "wget -qO- http://localhost:80/ | grep -q 'Element' || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 256M

  # ─── nginx Reverse Proxy ─────────────────────────────────────────────────────
  nginx:
    image: nginx:alpine
    restart: unless-stopped
    networks:
      - backend
    depends_on:
      - nextcloud
      - synapse
      - element
    ports:
      # CRITICAL: bind to Tailscale IP only — NEVER 0.0.0.0
      - "100.120.18.84:80:80"
      - "100.120.18.84:443:443"
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - nginx_certs:/etc/nginx/certs
      # Share Nextcloud HTML for static asset serving:
      - nextcloud_html:/var/www/html:ro
    healthcheck:
      test: ["CMD-SHELL", "curl -sf http://localhost/nginx-health || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          memory: 128M

volumes:
  # Add the shared html volume (declared here in addition to named volumes above)
  nextcloud_html:
```

### 2.3 Supporting Files Required

**`init-multiple-databases.sh`** — creates both `nextcloud` and `synapse` databases:

```bash
#!/bin/bash
set -e
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<-EOSQL
    CREATE DATABASE synapse;
    GRANT ALL PRIVILEGES ON DATABASE synapse TO "$POSTGRES_USER";
    CREATE DATABASE nextcloud;
    GRANT ALL PRIVILEGES ON DATABASE nextcloud TO "$POSTGRES_USER";
EOSQL
```

**`synapse/homeserver.yaml`** — minimal Synapse config:

```yaml
server_name: "REPLACE_MATRIX_HOSTNAME"
pid_file: /data/homeserver.pid
listeners:
  - port: 8008
    tls: false
    type: http
    x_forwarded: true
    resources:
      - names: [client, federation]
        compress: false
database:
  name: psycopg2
  args:
    user: REPLACE_POSTGRES_USER
    password: REPLACE_POSTGRES_PASSWORD
    database: synapse
    host: postgres
    cp_min: 5
    cp_max: 10
log_config: "/data/log.config"
media_store_path: /data/media_store
report_stats: false
signing_key_path: "/data/REPLACE_MATRIX_HOSTNAME.signing.key"
trusted_key_servers:
  - server_name: "matrix.org"
registration_shared_secret: "REPLACE_REGISTRATION_SECRET"
```

**`element/config.json`** — Element Web client config:

```json
{
    "default_server_config": {
        "m.homeserver": {
            "base_url": "https://REPLACE_MATRIX_HOSTNAME",
            "server_name": "REPLACE_MATRIX_HOSTNAME"
        }
    },
    "brand": "Systems Resilience Community",
    "showLabsSettings": false,
    "default_theme": "light"
}
```

---

## 3. Configuration Steps

### Step 1: Generate Secrets

```bash
# Generate all required secrets before editing docker-compose.yml
echo "POSTGRES_PASSWORD=$(openssl rand -hex 24)"
echo "NEXTCLOUD_ADMIN_PASSWORD=$(openssl rand -hex 16)"
echo "REGISTRATION_SECRET=$(openssl rand -hex 24)"
```

Store these in a secure location (password manager). Do not commit to git.

### Step 2: Database Setup

The `init-multiple-databases.sh` script handles database creation on first `docker compose up`. If PostgreSQL volume already exists and needs reset:

```bash
docker compose down
docker volume rm nextcloud-matrix_postgres_data
docker compose up -d postgres
# Wait 30 seconds, then verify both databases exist:
docker compose exec postgres psql -U REPLACE_POSTGRES_USER -c "\l"
```

### Step 3: Generate Synapse Signing Key

```bash
docker compose run --rm synapse generate_config --server-name REPLACE_MATRIX_HOSTNAME --report-stats no
# This writes homeserver.yaml and the signing key to ./synapse/
```

### Step 4: SSL Certificate Setup

For Tailscale-only deployment (recommended — no public DNS needed):

```bash
# Get Tailscale MagicDNS hostname
tailscale_host=$(tailscale status --json | python3 -c "import sys,json; d=json.load(sys.stdin); print(d['Self']['DNSName'].rstrip('.'))")
sudo tailscale cert "$tailscale_host"
# Copy certs to nginx volume path
sudo cp /var/lib/tailscale/certs/$tailscale_host.crt /opt/nextcloud-matrix/nginx/certs/
sudo cp /var/lib/tailscale/certs/$tailscale_host.key /opt/nextcloud-matrix/nginx/certs/
```

### Step 5: SMTP Integration

SMTP credentials go into the `nextcloud` service `environment` block. Required fields:
- `SMTP_HOST` — your SMTP server (e.g., `smtp.brevo.com` for Brevo free tier)
- `SMTP_PORT` — 587 (STARTTLS)
- `SMTP_USER` / `SMTP_PASSWORD` — your SMTP credentials
- `MAIL_FROM_ADDRESS` + `MAIL_DOMAIN` — combined to form the From address

Free SMTP options: Brevo (300 emails/day free), Mailgun (100/day free trial), Gmail SMTP (500/day with app password).

### Step 6: Start Stack

```bash
cd /opt/nextcloud-matrix
docker compose up -d
# Watch for all services healthy:
watch docker compose ps
# All services should show "healthy" within 3–5 minutes
# Nextcloud has a 120-second start_period due to PHP initialization
```

### Step 7: Nextcloud Post-Startup Configuration

```bash
# Set CalDAV and CardDAV URLs (fixes default URL issues)
docker compose exec nextcloud php occ config:system:set overwriteprotocol --value=https
docker compose exec nextcloud php occ config:system:set trusted_proxies --value='["nginx"]'
docker compose exec nextcloud php occ config:system:set default_phone_region --value=US

# Enable Redis session caching
docker compose exec nextcloud php occ config:system:set redis --value='{"host":"redis","port":6379}' --type=json

# Verify installation
docker compose exec nextcloud php occ status
```

---

## 4. Backup and Restore Procedures

### 4.1 Daily Backup Script

```bash
cat > /opt/discourse-backup.sh << 'EOF'
#!/bin/bash
# Nextcloud+Matrix daily backup
set -euo pipefail

BACKUP_DIR="/home/awank/backups/nextcloud-matrix"
DATE=$(date -u +%Y-%m-%d)
LOG="/var/log/nextcloud-backup.log"
COMPOSE_DIR="/opt/nextcloud-matrix"

echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Starting backup..." >> "$LOG"

mkdir -p "$BACKUP_DIR/$DATE"

# 1. PostgreSQL dump (both databases)
docker compose -f "$COMPOSE_DIR/docker-compose.yml" exec -T postgres \
    pg_dumpall -U REPLACE_POSTGRES_USER | gzip > "$BACKUP_DIR/$DATE/postgres-all.sql.gz"

# 2. Nextcloud config
docker run --rm -v nextcloud-matrix_nextcloud_config:/data alpine \
    tar czf - /data > "$BACKUP_DIR/$DATE/nextcloud-config.tar.gz"

# 3. Synapse signing key and config
docker run --rm -v nextcloud-matrix_synapse_data:/data alpine \
    tar czf - /data > "$BACKUP_DIR/$DATE/synapse-data.tar.gz"

# Prune backups older than 14 days
find "$BACKUP_DIR" -maxdepth 1 -type d -mtime +14 -exec rm -rf {} \; 2>/dev/null || true

backup_size=$(du -sh "$BACKUP_DIR/$DATE" | cut -f1)
echo "[$(date -u '+%Y-%m-%dT%H:%M:%SZ')] Backup complete: $backup_size" >> "$LOG"
EOF

chmod +x /opt/discourse-backup.sh
# Schedule at 02:00 UTC daily
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/discourse-backup.sh") | crontab -
```

Note: Nextcloud file data itself (the `/var/www/html/data` volume) is not backed up by this script because it will grow very large. For Phase 5.1, documents are small; add file backup with `rsync` if user-uploaded file volume grows beyond 1 GB.

### 4.2 Restore Procedure

```bash
# 1. Stop stack (keep database service running)
cd /opt/nextcloud-matrix
docker compose stop nextcloud synapse element nginx

# 2. Drop and re-create databases
docker compose exec postgres psql -U REPLACE_POSTGRES_USER -c "DROP DATABASE nextcloud;"
docker compose exec postgres psql -U REPLACE_POSTGRES_USER -c "DROP DATABASE synapse;"
docker compose exec postgres psql -U REPLACE_POSTGRES_USER -c "CREATE DATABASE nextcloud;"
docker compose exec postgres psql -U REPLACE_POSTGRES_USER -c "CREATE DATABASE synapse;"

# 3. Restore PostgreSQL dump
gunzip -c /home/awank/backups/nextcloud-matrix/YYYY-MM-DD/postgres-all.sql.gz | \
    docker compose exec -T postgres psql -U REPLACE_POSTGRES_USER

# 4. Restore Nextcloud config
docker run --rm -v nextcloud-matrix_nextcloud_config:/data -v \
    /home/awank/backups/nextcloud-matrix/YYYY-MM-DD:/backup alpine \
    tar xzf /backup/nextcloud-config.tar.gz -C /

# 5. Restart stack
docker compose start nextcloud synapse element nginx
```

---

## 5. Known Limitations on Pi5 (8GB RAM)

1. **OnlyOffice unavailable**: The OnlyOffice document server has no ARM64 image. Collaborative in-browser document editing is not possible on Pi5. Authors must use download-edit-upload workflow or use the Nextcloud markdown editor.

2. **Memory pressure at 50+ concurrent users**: At 50–100 active users simultaneously editing files, RAM usage can reach 5–6 GB. Linux OOM killer may terminate the largest consumer (usually Synapse or Nextcloud PHP-FPM). Monitor with `free -h` and set `memory: 1G` limits per service to prevent cascade OOM.

3. **Startup time**: First-time database initialization takes 3–5 minutes. Cold start after reboot takes 2–3 minutes before all services are healthy.

4. **Disk growth**: Nextcloud's `/var/www/html/data` volume grows with every uploaded file, version, and thumbnail. With 50 active authors each storing 100 MB, that is 5 GB. The Pi5 has 189 GB free — this is not an imminent problem, but monitor with `docker system df`.

5. **ARM64 image availability**: Not all Nextcloud plugins have ARM64 builds. Calendar, Contacts, and Talk plugins are ARM64-compatible; some third-party apps may not be.

6. **Database RAM contention**: PostgreSQL is shared between Nextcloud and Synapse. Under concurrent load from both applications, the `shared_buffers=256MB` setting may be insufficient. If PostgreSQL is slow, increase to `384MB` and restart.

---

## 6. Troubleshooting

### Container won't start

```bash
docker compose logs --tail=50 [service-name]
# Most common causes:
# - postgres not ready: healthcheck protects against this; wait 60s
# - bad YAML in docker-compose.yml: docker compose config (validates)
# - volume permissions: docker compose exec nextcloud chown -R www-data:www-data /var/www/html
```

### Nextcloud 503 or blank page

```bash
# Nextcloud uses PHP-FPM; nginx must pass requests via FastCGI
# Confirm nginx can reach nextcloud:9000
docker compose exec nginx curl -sf http://nextcloud:9000/ping || echo "FPM not reachable"
# If FPM not reachable: check nextcloud container is healthy
docker compose ps nextcloud
```

### Matrix federation errors

```bash
# Check Synapse logs
docker compose logs synapse --tail=50 | grep -E "(ERROR|WARN)"
# Test federation endpoint
curl -sf https://REPLACE_MATRIX_HOSTNAME/_matrix/federation/v1/version | python3 -m json.tool
```

### OOM (out-of-memory) kill

```bash
# Check dmesg for OOM events
dmesg | grep -i "oom\|kill" | tail -20
# If OOM killed a service, restart it:
docker compose restart [service]
# Long-term fix: lower memory limits on OnlyOffice (not deployed) or Synapse
```

### SSL certificate errors in browser

```bash
# Verify cert is valid
openssl s_client -connect REPLACE_NEXTCLOUD_HOSTNAME:443 2>/dev/null | openssl x509 -noout -dates
# If self-signed: users must accept browser warning once
# If Tailscale cert: verify tailscale cert is not expired
sudo tailscale cert [hostname]
```

---

## Deployment Time Estimate: 4–6 hours

| Phase | Duration |
|-------|---------|
| DNS + secrets setup | 30 min |
| Write config files (compose, nginx.conf, homeserver.yaml) | 60 min |
| First `docker compose up` + image pulls | 30 min (network speed dependent) |
| Database initialization + Nextcloud setup wizard | 45 min |
| Synapse signing key generation + verification | 30 min |
| SSL setup | 30 min |
| User creation + permission verification | 30 min |
| Smoke tests + troubleshooting buffer | 60 min |
| **Total** | **5.25 hours typical** |

**Cross-references**: `NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md` (comprehensive), `DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md`, `docker-compose-nextcloud-matrix.yml` (existing template)
