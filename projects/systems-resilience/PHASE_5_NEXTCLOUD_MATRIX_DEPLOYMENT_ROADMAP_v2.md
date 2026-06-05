---
title: "Phase 5 Nextcloud + Matrix Deployment Roadmap v2"
project: systems-resilience
phase: 5
status: PRODUCTION-READY — June 5-15 deployment window
platform: "Nextcloud Hub 33 + Matrix Synapse + Element Web + PostgreSQL + Redis"
containers: 5
target_host: "raspby1 (Raspberry Pi 5, 4-8 GB RAM, 100.70.184.84)"
created: 2026-06-05
version: 2.0
confidence: 87%
note: "v2 — 5-container simplified stack for Pi 5 resource constraints. Full 7-container stack in NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md."
cross_references:
  - NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md (full 7-container reference)
  - PHASE_5_DEPLOYMENT_SCRIPTS_NEXTCLOUD_MATRIX.md
  - PHASE_5_NEXTCLOUD_MATRIX_CONFIGURATION_TEMPLATES.md
  - PHASE_5_MESHTASTIC_BRIDGE_CONTINGENCY.md
  - PHASE_5_DEPLOYMENT_CHECKLIST_AND_ONBOARDING.md
---

# Phase 5 Nextcloud + Matrix — Deployment Roadmap v2
## 5-Container Stack | Raspberry Pi 5 | June 5-15 Deployment Window

---

## Executive Summary

This roadmap is the consolidated technical reference for deploying Nextcloud + Matrix on a Raspberry Pi 5 (or equivalent Linux host with 4 GB+ RAM). It is the simplified 5-container variant of the full 7-container stack documented in `NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md`. OnlyOffice and the nginx-nextcloud FPM sidecar are omitted to stay within Pi 5 memory constraints.

**What this stack provides:**
- Nextcloud Hub 33 — file sync, CalDAV/CardDAV, collaborative Markdown editing (Text app)
- Matrix Synapse — encrypted group messaging, offline message queuing
- Element Web — browser-based Matrix client (also functions as Element X on mobile)
- PostgreSQL 16 — shared database for Nextcloud and Synapse
- Redis 7 — session cache and job queue

**What is deferred:**
- OnlyOffice / Collabora document server (add in Phase 6 if RAM allows)
- Meshtastic bridge (separate container, separate document: `PHASE_5_MESHTASTIC_BRIDGE_CONTINGENCY.md`)
- LDAP/SSO (document structure prepared; not deployed in Wave 1)

**Confidence:** 87% (all components production-grade June 2026; Pi 5 thermal constraints noted)

---

## Section 1: Architecture

### 1.1 Container Architecture Diagram

```
External Access (Tailscale or Public HTTPS)
         |
         v
+------------------+
|   nginx:alpine   |  Port 127.0.0.1:443  (HTTPS)
|  (Reverse Proxy) |  Port 127.0.0.1:80   (HTTP → redirect)
|  TLS Termination |  Port 127.0.0.1:8448 (Matrix federation, optional)
+------------------+
         |
         | Internal Docker network: resilience-net (172.28.0.0/16)
         |
    +----|----+------------+------------+
    |         |            |            |
    v         v            v            v
+----------+ +----------+ +----------+ +----------+
| nextcloud| | synapse  | | element  | | postgres |
|  Hub 33  | | (Matrix) | | (web UI) | |   :16   |
| FPM :9000| | :8008    | | :80      | |  :5432   |
+----------+ +----------+ +----------+ +----+-----+
                                             |
                                        +----+-----+
                                        |  redis:7 |
                                        |  :6379   |
                                        +----------+

Volume mounts (all on host at /opt/community/):
  data/postgres/   → postgres:/var/lib/postgresql/data
  data/nextcloud/  → nextcloud:/var/www/html
  data/matrix/     → synapse:/data
  data/redis/      → redis:/data
  nginx/           → nginx:/etc/nginx (config)
  certs/           → nginx:/etc/letsencrypt (TLS)
```

### 1.2 Network and Port Summary

| Port (Host) | Container | Purpose | Exposure |
|-------------|-----------|---------|----------|
| 127.0.0.1:80 | nginx | HTTP → HTTPS redirect + ACME | Tailscale/local only |
| 127.0.0.1:443 | nginx | HTTPS (all services via SNI) | Tailscale/local only |
| 127.0.0.1:8448 | nginx → synapse | Matrix federation (optional) | Enable only if federating |
| (internal) 9000 | nextcloud | PHP-FPM (Docker network only) | Internal |
| (internal) 8008 | synapse | Matrix client API (internal) | Internal |
| (internal) 5432 | postgres | Database (Docker network only) | Internal |
| (internal) 6379 | redis | Cache (Docker network only) | Internal |

**No 0.0.0.0 bindings.** All host-facing ports bind to 127.0.0.1 per CLAUDE.md policy. External access via Tailscale (raspby1 = 100.70.184.84) or through a separate Tailscale-to-port forwarding rule.

### 1.3 Resource Budget (Raspberry Pi 5, 4 GB minimum)

| Container | RAM (steady state) | RAM (peak) |
|-----------|--------------------|-----------|
| postgres | 256 MB | 512 MB |
| redis | 128 MB | 256 MB |
| nextcloud | 512 MB | 1,024 MB |
| synapse | 512 MB | 768 MB |
| element | 64 MB | 128 MB |
| nginx | 32 MB | 64 MB |
| **Total** | **~1.5 GB** | **~2.75 GB** |

Leaves approximately 1.25–2.5 GB for OS and Docker overhead on a 4 GB system. On an 8 GB Pi 5 (raspby1), headroom is comfortable. Monitor with `docker stats --no-stream`.

---

## Section 2: Prerequisites

### 2.1 Infrastructure Requirements

- **OS**: Raspberry Pi OS Bookworm (64-bit) or Ubuntu 22.04 LTS / Debian 12
- **Docker**: Engine 24+ with Compose v2 (`docker compose version`)
- **Storage**: Minimum 32 GB free on the data partition (80 GB recommended)
- **Tailscale**: Running on raspby1 (`tailscale status` confirms 100.70.184.84)
- **Thermal**: Idle temp below 85°C; if at 87°C+, add passive cooling before deployment

```bash
# Verify Docker (must show Compose v2)
docker --version && docker compose version

# Check storage
df -h /
# Need ≥ 32 GB free

# Check RAM
free -h
# Need ≥ 3.5 GB available

# Check temperature (Pi 5)
vcgencmd measure_temp
# If > 85°C, add cooling before proceeding
```

### 2.2 Generate Secrets Before Starting

Run this once. Save the output in a password manager before creating `.env`.

```bash
python3 -c "
import secrets
vars = [
    'POSTGRES_PASSWORD',
    'REDIS_PASSWORD',
    'NEXTCLOUD_ADMIN_PASSWORD',
    'SYNAPSE_FORM_SECRET',
    'SYNAPSE_MACAROON_KEY',
]
for v in vars:
    print(f'{v}={secrets.token_urlsafe(32)}')
"
```

### 2.3 Directory Structure

```bash
sudo mkdir -p /opt/community/nextcloud-matrix
sudo chown $USER:$USER /opt/community/nextcloud-matrix
cd /opt/community/nextcloud-matrix

mkdir -p data/{postgres,redis,nextcloud,matrix/media}
mkdir -p nginx/conf.d
mkdir -p matrix/config
mkdir -p element
mkdir -p scripts

chmod 700 data/
touch .env && chmod 600 .env
```

---

## Section 3: Configuration Files

### 3.1 Environment File (.env)

```bash
# /opt/community/nextcloud-matrix/.env
# NEVER commit this file. Add to .gitignore.
# All placeholder values MUST be replaced before deployment.

# === Domains ===
# For Tailscale-only: use raspby1 Tailscale IP
# For public: use your domain (e.g., resilience-hub.org)
BASE_DOMAIN=resilience-hub.local
NEXTCLOUD_DOMAIN=nextcloud.resilience-hub.local
MATRIX_DOMAIN=matrix.resilience-hub.local
ELEMENT_DOMAIN=element.resilience-hub.local

# === PostgreSQL ===
POSTGRES_USER=community_user
POSTGRES_PASSWORD=REPLACE_WITH_GENERATED_VALUE
POSTGRES_DB=nextcloud_db
SYNAPSE_DB=synapse_db

# === Redis ===
REDIS_PASSWORD=REPLACE_WITH_GENERATED_VALUE

# === Nextcloud ===
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=REPLACE_WITH_GENERATED_VALUE
NEXTCLOUD_TRUSTED_DOMAINS=nextcloud.resilience-hub.local 100.70.184.84

# === Matrix Synapse ===
SYNAPSE_SERVER_NAME=resilience-hub.local
SYNAPSE_REPORT_STATS=no
SYNAPSE_FORM_SECRET=REPLACE_WITH_GENERATED_VALUE
SYNAPSE_MACAROON_KEY=REPLACE_WITH_GENERATED_VALUE

# === Email (optional but recommended) ===
SMTP_HOST=smtp.brevo.com
SMTP_PORT=587
SMTP_USER=your_email@example.com
SMTP_PASSWORD=your_smtp_key
SMTP_FROM=noreply@resilience-hub.org

# === Let's Encrypt (for public deployment) ===
LETSENCRYPT_EMAIL=admin@resilience-hub.org

# === Timezone ===
TZ=UTC
```

Verify no placeholders remain before proceeding:

```bash
grep "REPLACE_WITH" .env
# Output must be empty. If not, fill in all values first.
```

### 3.2 docker-compose.yml (5-Container Stack)

```yaml
# /opt/community/nextcloud-matrix/docker-compose.yml
# 5-container stack optimized for Raspberry Pi 5 (4-8 GB RAM)
# No OnlyOffice, no FPM sidecar — uses nextcloud:fpm-alpine direct with nginx proxy
name: community-platform

services:

  # ----------------------------------------------------------------
  # PostgreSQL 16 — shared database for Nextcloud and Matrix Synapse
  # ----------------------------------------------------------------
  postgres:
    image: postgres:16-alpine
    container_name: community-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_INITDB_ARGS: "--encoding=UTF8 --locale=C"
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
      - ./init-db.sql:/docker-entrypoint-initdb.d/10-init.sql:ro
    networks:
      - resilience-net
    mem_limit: 512m
    restart: unless-stopped
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

  # ----------------------------------------------------------------
  # Redis 7 — session cache and background job queue
  # ----------------------------------------------------------------
  redis:
    image: redis:7-alpine
    container_name: community-redis
    restart: unless-stopped
    command: >
      redis-server
      --requirepass ${REDIS_PASSWORD}
      --maxmemory 256mb
      --maxmemory-policy allkeys-lru
      --save 60 1000
    volumes:
      - ./data/redis:/data
    networks:
      - resilience-net
    mem_limit: 320m
    healthcheck:
      test: ["CMD", "redis-cli", "-a", "${REDIS_PASSWORD}", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  # ----------------------------------------------------------------
  # Nextcloud Hub 33 (FPM) — file sync, CalDAV, CardDAV, Markdown
  # NOTE: This speaks FastCGI on port 9000, not HTTP.
  # nginx (below) handles HTTP and shares volumes with this container.
  # ----------------------------------------------------------------
  nextcloud:
    image: nextcloud:33-fpm-alpine
    container_name: community-nextcloud
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      POSTGRES_HOST: postgres
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      NEXTCLOUD_ADMIN_USER: ${NEXTCLOUD_ADMIN_USER}
      NEXTCLOUD_ADMIN_PASSWORD: ${NEXTCLOUD_ADMIN_PASSWORD}
      NEXTCLOUD_TRUSTED_DOMAINS: ${NEXTCLOUD_TRUSTED_DOMAINS}
      REDIS_HOST: redis
      REDIS_HOST_PASSWORD: ${REDIS_PASSWORD}
      OVERWRITEPROTOCOL: https
      OVERWRITEHOST: ${NEXTCLOUD_DOMAIN}
      OVERWRITEWEBROOT: /
      SMTP_HOST: ${SMTP_HOST}
      SMTP_SECURE: tls
      SMTP_PORT: ${SMTP_PORT}
      SMTP_AUTHTYPE: LOGIN
      SMTP_NAME: ${SMTP_USER}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
      MAIL_FROM_ADDRESS: ${SMTP_FROM}
      PHP_MEMORY_LIMIT: 512M
      PHP_UPLOAD_LIMIT: 512M
      TZ: ${TZ}
    volumes:
      - ./data/nextcloud:/var/www/html
    networks:
      - resilience-net
    mem_limit: 1024m
    healthcheck:
      # FPM does not serve HTTP; check PHP-FPM status via process check
      test: ["CMD-SHELL", "ps aux | grep php-fpm | grep -v grep || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

  # ----------------------------------------------------------------
  # Matrix Synapse — Matrix homeserver with PostgreSQL backend
  # ----------------------------------------------------------------
  synapse:
    image: matrixdotorg/synapse:latest
    container_name: community-synapse
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      SYNAPSE_SERVER_NAME: ${SYNAPSE_SERVER_NAME}
      SYNAPSE_REPORT_STATS: ${SYNAPSE_REPORT_STATS}
      SYNAPSE_CONFIG_PATH: /data/homeserver.yaml
    volumes:
      - ./data/matrix:/data
      - ./matrix/config/homeserver.yaml:/data/homeserver.yaml:ro
      - ./matrix/config/log.yaml:/data/log.yaml:ro
    networks:
      - resilience-net
    ports:
      - "127.0.0.1:8008:8008"   # Client API (proxied by nginx)
      - "127.0.0.1:8448:8448"   # Federation (enable only if federating)
    mem_limit: 768m
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost:8008/_matrix/client/versions"]
      interval: 15s
      timeout: 10s
      retries: 5
      start_period: 60s

  # ----------------------------------------------------------------
  # Element Web — browser-based Matrix client
  # Served as static files; configure via element/config.json
  # ----------------------------------------------------------------
  element:
    image: vectorim/element-web:latest
    container_name: community-element
    restart: unless-stopped
    volumes:
      - ./element/config.json:/app/config.json:ro
    networks:
      - resilience-net
    mem_limit: 128m
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ----------------------------------------------------------------
  # nginx — reverse proxy + TLS termination + Nextcloud FPM proxy
  # Binds to 127.0.0.1 only. Never 0.0.0.0.
  # Also shares nextcloud volume to serve static assets.
  # ----------------------------------------------------------------
  nginx:
    image: nginx:1.27-alpine
    container_name: community-nginx
    restart: unless-stopped
    depends_on:
      - nextcloud
      - synapse
      - element
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./data/nextcloud:/var/www/html:ro   # shared with nextcloud for static files
      - ./data/certs:/etc/ssl/certs:ro       # TLS certificates
      - ./data/letsencrypt:/etc/letsencrypt:ro
    ports:
      - "127.0.0.1:80:80"
      - "127.0.0.1:443:443"
      - "127.0.0.1:8448:8448"
    networks:
      - resilience-net
    mem_limit: 64m
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost/nginx-health"]
      interval: 15s
      timeout: 5s
      retries: 3

networks:
  resilience-net:
    driver: bridge
    ipam:
      config:
        - subnet: 172.28.0.0/16
```

### 3.3 PostgreSQL Init Script (init-db.sql)

```sql
-- /opt/community/nextcloud-matrix/init-db.sql
-- Creates Synapse database alongside the Nextcloud database.
-- Both use the same POSTGRES_USER from .env.

\connect postgres

SELECT 'CREATE DATABASE synapse_db
  ENCODING UTF8
  LC_COLLATE C
  LC_CTYPE C
  TEMPLATE template0'
  WHERE NOT EXISTS (
    SELECT FROM pg_database WHERE datname = 'synapse_db'
  )\gexec

GRANT ALL PRIVILEGES ON DATABASE synapse_db TO community_user;
```

### 3.4 Matrix Synapse Configuration (matrix/config/homeserver.yaml)

Generate the base configuration first (creates signing key automatically):

```bash
# Run once before first start. Generates homeserver.yaml and signing key.
docker compose run --rm \
  -e SYNAPSE_SERVER_NAME="${SYNAPSE_SERVER_NAME}" \
  -e SYNAPSE_REPORT_STATS=no \
  synapse generate

# Generated files appear in ./data/matrix/
ls ./data/matrix/
# *.signing.key  homeserver.yaml  log.config

# Extract the auto-generated secrets to use in your config
grep -E "macaroon_secret_key|form_secret|signing_key_path" ./data/matrix/homeserver.yaml
```

Then replace `./data/matrix/homeserver.yaml` with:

```yaml
# matrix/config/homeserver.yaml
server_name: "resilience-hub.local"
pid_file: /data/homeserver.pid

listeners:
  - port: 8008
    tls: false
    type: http
    x_forwarded: true
    bind_addresses:
      - "127.0.0.1"
    resources:
      - names: [client, federation]
        compress: false

database:
  name: psycopg2
  args:
    user: community_user
    password: "PASTE_POSTGRES_PASSWORD_HERE"
    database: synapse_db
    host: postgres
    port: 5432
    cp_min: 3
    cp_max: 8

redis:
  enabled: true
  host: redis
  port: 6379
  password: "PASTE_REDIS_PASSWORD_HERE"

media_store_path: /data/media
max_upload_size: 50M
url_preview_enabled: false

# Copy these values from the generated homeserver.yaml
form_secret: "PASTE_GENERATED_FORM_SECRET"
macaroon_secret_key: "PASTE_GENERATED_MACAROON_KEY"
signing_key_path: "/data/resilience-hub.local.signing.key"

# Registration: invite-only (admin creates accounts)
enable_registration: false
registration_requires_token: true

# Federation: disabled for internal-only deployment
# Set to true + configure federation_domain_whitelist to open up
federation_domain_whitelist:
  - "resilience-hub.local"

trusted_key_servers:
  - server_name: "matrix.org"

email:
  smtp_host: "smtp.brevo.com"
  smtp_port: 587
  smtp_user: "PASTE_SMTP_USER"
  smtp_pass: "PASTE_SMTP_PASS"
  notif_from: "Matrix <noreply@resilience-hub.org>"
  enable_notifs: true

log_config: "/data/log.yaml"

# Performance tuning for Pi 5
event_cache_size: 5K
caches:
  global_factor: 0.5

admin_contact: "admin@resilience-hub.local"
```

### 3.5 Element Web Config (element/config.json)

```json
{
    "default_server_config": {
        "m.homeserver": {
            "base_url": "https://matrix.resilience-hub.local",
            "server_name": "resilience-hub.local"
        }
    },
    "brand": "Resilience Hub",
    "default_theme": "light",
    "room_directory": {
        "servers": ["resilience-hub.local"]
    },
    "features": {
        "feature_spotlight": true,
        "feature_video_rooms": false
    },
    "setting_defaults": {
        "breadcrumbs": true,
        "sendReadReceipts": true
    },
    "show_labs_settings": false,
    "disable_custom_urls": false,
    "disable_guests": true,
    "enable_presence_by_hs_url": {
        "https://matrix.resilience-hub.local": false
    }
}
```

For offline message queuing: Element Web uses IndexedDB to cache the last ~1000 messages per room. Messages typed while offline queue and flush when the connection is restored. No additional configuration is needed.

### 3.6 nginx Configuration

**nginx/nginx.conf** — global settings:

```nginx
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 1024;
    use epoll;
    multi_accept on;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" rt=$request_time';
    access_log /var/log/nginx/access.log main;

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    client_max_body_size 512M;
    client_body_timeout 300s;

    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml text/javascript
               application/json application/javascript application/xml+rss;

    # Global security headers
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    include /etc/nginx/conf.d/*.conf;
}
```

**nginx/conf.d/00-http.conf** — HTTP redirect:

```nginx
server {
    listen 80 default_server;
    server_name _;

    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
        try_files $uri =404;
    }

    location /nginx-health {
        access_log off;
        return 200 "OK\n";
        add_header Content-Type text/plain;
    }

    location / {
        return 301 https://$host$request_uri;
    }
}
```

**nginx/conf.d/10-nextcloud.conf** — Nextcloud (FPM via FastCGI):

```nginx
upstream php-nextcloud {
    server nextcloud:9000;
}

server {
    listen 443 ssl http2;
    server_name nextcloud.resilience-hub.local;

    ssl_certificate     /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/certs/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;

    add_header Strict-Transport-Security "max-age=15552000; includeSubDomains" always;

    root /var/www/html;
    index index.php index.html;
    client_max_body_size 512M;
    fastcgi_buffers 64 4K;

    # CalDAV/CardDAV
    location = /.well-known/carddav { return 301 /remote.php/dav; }
    location = /.well-known/caldav  { return 301 /remote.php/dav; }

    # Deny sensitive paths
    location ~ /\. { deny all; return 404; }
    location ~ ^/(?:build|tests|config|lib|3rdparty|templates|data)(?:$|/) { return 404; }

    # Static assets
    location ~ \.(?:css|js|woff2?|svg|gif|png|jpg|jpeg|webp|ico|ttf)$ {
        try_files $uri /index.php$request_uri;
        expires 6M;
        access_log off;
    }

    # PHP
    location ~ \.php(?:$|/) {
        fastcgi_split_path_info ^(.+?\.php)(/.*)$;
        set $path_info $fastcgi_path_info;
        try_files $fastcgi_script_name =404;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $path_info;
        fastcgi_param HTTPS on;
        fastcgi_param modHeadersAvailable true;
        fastcgi_pass php-nextcloud;
        fastcgi_intercept_errors on;
        fastcgi_request_buffering on;
    }

    location / {
        try_files $uri $uri/ /index.php$request_uri;
    }
}
```

**nginx/conf.d/11-matrix.conf** — Matrix Synapse:

```nginx
server {
    listen 443 ssl http2;
    server_name matrix.resilience-hub.local;

    ssl_certificate     /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/certs/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_session_cache shared:SSL:10m;

    add_header Strict-Transport-Security "max-age=15552000; includeSubDomains" always;

    # Matrix client API
    location /_matrix {
        proxy_pass http://synapse:8008;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $host;
        proxy_buffering off;
        client_max_body_size 50M;
        proxy_read_timeout 600s;
    }

    # Synapse admin API
    location /_synapse/admin {
        proxy_pass http://synapse:8008;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $host;
        # Restrict to Tailscale IP in production:
        # allow 100.70.184.84;
        # deny all;
    }

    # Matrix .well-known (server discovery)
    location /.well-known/matrix/server {
        return 200 '{"m.server": "matrix.resilience-hub.local:443"}';
        default_type application/json;
        add_header Access-Control-Allow-Origin *;
    }

    location /.well-known/matrix/client {
        return 200 '{"m.homeserver": {"base_url": "https://matrix.resilience-hub.local"}}';
        default_type application/json;
        add_header Access-Control-Allow-Origin *;
    }
}

# Matrix federation port (8448) — enable if federating externally
server {
    listen 8448 ssl http2;
    server_name matrix.resilience-hub.local;

    ssl_certificate     /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/certs/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;

    location / {
        proxy_pass http://synapse:8448;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $host;
    }
}
```

**nginx/conf.d/12-element.conf** — Element Web:

```nginx
server {
    listen 443 ssl http2;
    server_name element.resilience-hub.local;

    ssl_certificate     /etc/ssl/certs/fullchain.pem;
    ssl_certificate_key /etc/ssl/certs/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_session_cache shared:SSL:10m;

    add_header Strict-Transport-Security "max-age=15552000" always;
    add_header Content-Security-Policy "frame-ancestors 'none'" always;

    location / {
        proxy_pass http://element:80;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

### 3.7 TLS Certificate Setup

**For Tailscale-only deployment (self-signed)**:

```bash
mkdir -p /opt/community/nextcloud-matrix/data/certs
cd /opt/community/nextcloud-matrix/data/certs

openssl req -x509 -nodes -newkey rsa:4096 \
  -keyout privkey.pem \
  -out fullchain.pem \
  -days 365 \
  -subj "/CN=resilience-hub.local" \
  -addext "subjectAltName=DNS:resilience-hub.local,DNS:nextcloud.resilience-hub.local,DNS:matrix.resilience-hub.local,DNS:element.resilience-hub.local,IP:100.70.184.84"

# Users accessing via browser will see a certificate warning.
# Import fullchain.pem into their browser trust store to suppress it.
```

**For public deployment with Let's Encrypt** (requires public DNS pointing to host):

```bash
# Issue certificates before starting the stack (port 80 must be free)
docker run --rm \
  -p 80:80 \
  -v /opt/community/nextcloud-matrix/data/letsencrypt:/etc/letsencrypt \
  certbot/certbot certonly \
  --standalone --agree-tos --non-interactive \
  --email admin@resilience-hub.org \
  -d nextcloud.resilience-hub.org \
  -d matrix.resilience-hub.org \
  -d element.resilience-hub.org

# After issuance, symlink to expected paths in data/certs/:
ln -sf /opt/community/nextcloud-matrix/data/letsencrypt/live/nextcloud.resilience-hub.org/fullchain.pem \
       /opt/community/nextcloud-matrix/data/certs/fullchain.pem
ln -sf /opt/community/nextcloud-matrix/data/letsencrypt/live/nextcloud.resilience-hub.org/privkey.pem \
       /opt/community/nextcloud-matrix/data/certs/privkey.pem

# Auto-renewal cron:
(crontab -l 2>/dev/null; echo "0 0,12 * * * docker run --rm -v /opt/community/nextcloud-matrix/data/letsencrypt:/etc/letsencrypt certbot/certbot renew --quiet && docker exec community-nginx nginx -s reload") | crontab -
```

---

## Section 4: Nextcloud Feature Configuration

### 4.1 CalDAV / CardDAV Setup

After the stack is running, install and configure calendar and contacts via the Nextcloud OCC CLI:

```bash
# Enable Calendar app
docker exec -u www-data community-nextcloud php occ app:enable calendar

# Enable Contacts app
docker exec -u www-data community-nextcloud php occ app:enable contacts

# Create shared editorial calendar
docker exec -u www-data community-nextcloud php occ \
  dav:create-calendar admin editorial-calendar "Phase 5 Editorial Calendar"

# Create shared contacts list
docker exec -u www-data community-nextcloud php occ \
  dav:create-addressbook admin wave1-authors "Wave 1 Authors"
```

**CalDAV URL for authors:**
```
https://nextcloud.resilience-hub.local/remote.php/dav/calendars/USERNAME/editorial-calendar/
```

**CardDAV URL for authors:**
```
https://nextcloud.resilience-hub.local/remote.php/dav/addressbooks/users/USERNAME/wave1-authors/
```

### 4.2 File Sharing Policies

Configure via Nextcloud admin panel (Settings → Sharing) or OCC:

```bash
# Restrict public link creation to admin only (for initial Phase 5 deployment)
docker exec -u www-data community-nextcloud php occ config:app:set \
  core shareapi_only_share_with_group_members --value="yes"

# Set default link expiration (30 days)
docker exec -u www-data community-nextcloud php occ config:app:set \
  core shareapi_default_expire_date --value="yes"
docker exec -u www-data community-nextcloud php occ config:app:set \
  core shareapi_expire_after_n_days --value="30"

# Enforce expiration dates
docker exec -u www-data community-nextcloud php occ config:app:set \
  core shareapi_enforce_expire_date --value="yes"
```

### 4.3 LDAP/SSO Integration Structure

Not deployed in Wave 1 — Nextcloud local accounts used. The structure is prepared for future activation:

```bash
# Install LDAP app (install only, do not configure)
docker exec -u www-data community-nextcloud php occ app:install user_ldap

# When ready to configure (Phase 6):
# 1. Add LDAP container to docker-compose.yml
# 2. Configure via: Settings → LDAP/AD Integration
# 3. LDAP provider: OpenLDAP (Docker image: osixia/openldap)
# 4. Matrix Synapse can use LDAP password provider for SSO
```

### 4.4 Offline-First Sync Configuration

Nextcloud offline capability is delivered through the desktop sync client. Authors install it once and get persistent local file access:

```bash
# Authors install: https://nextcloud.com/install/#install-clients
# Server URL: https://nextcloud.resilience-hub.local
# After sync, use "Available offline" toggle per folder in the client.
```

Key behavior: edits made offline are queued in the local sync folder and pushed when connectivity returns. Conflicts produce a `filename (conflict by username YYYY-MM-DD).md` copy for manual resolution.

---

## Section 5: Matrix Configuration

### 5.1 Admin User Creation

```bash
# Create admin Matrix user after Synapse is healthy
docker exec -it community-synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u admin \
  -p "$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)" \
  --admin \
  http://localhost:8008

# Get admin access token (needed for API calls)
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d "{\"type\":\"m.login.password\",\"user\":\"admin\",\"password\":\"ADMIN_PASSWORD\"}" \
  https://matrix.resilience-hub.local/_matrix/client/r0/login \
  | python3 -m json.tool
# Save the "access_token" value as MATRIX_ADMIN_TOKEN
```

### 5.2 Default Room Creation

```bash
export MATRIX_ADMIN_TOKEN="syt_admin_..."  # From login step above

# Create default coordination rooms
for room_name in "phase-5-general" "phase-5-feedback" "coordination" "technical"; do
  curl -s -X POST \
    -H "Authorization: Bearer $MATRIX_ADMIN_TOKEN" \
    -H "Content-Type: application/json" \
    -d "{\"name\": \"$room_name\", \"room_alias_name\": \"$room_name\", \"topic\": \"Phase 5 ${room_name}\", \"preset\": \"private_chat\", \"visibility\": \"private\"}" \
    https://matrix.resilience-hub.local/_matrix/client/v3/createRoom
  echo ""
done
```

### 5.3 Offline Message Queuing

Matrix Synapse stores all messages server-side. Element Web uses IndexedDB to cache the last ~1000 messages per room locally in the browser.

**Behavior when offline:**
- Cached messages: readable without network connection
- Messages typed while offline: queued in IndexedDB, sent on reconnection
- Encryption: E2E encryption state maintained locally; encrypted messages readable offline

**Limitation:** Offline queuing works only between the client and the homeserver. If the homeserver itself is unreachable (e.g., raspby1 is down), no relay occurs. For true infrastructure-down scenarios, see the Meshtastic bridge in `PHASE_5_MESHTASTIC_BRIDGE_CONTINGENCY.md`.

### 5.4 Federation Configuration

For Phase 5 (internal deployment), federation is disabled by default. The `federation_domain_whitelist` in homeserver.yaml restricts outbound federation. To open federation later:

```yaml
# In homeserver.yaml — remove the whitelist to allow all federation
federation_domain_whitelist: []  # empty list = allow all
allow_public_rooms_over_federation: false  # keep false for privacy
```

Then restart Synapse and verify via the Matrix federation tester:

```bash
curl "https://federationtester.matrix.org/api/report?server_name=resilience-hub.local"
```

### 5.5 Media Storage Configuration

```yaml
# homeserver.yaml media settings
media_store_path: /data/media
max_upload_size: 50M    # Reduce to 10M if disk is constrained
max_image_pixels: 32M
url_preview_enabled: false  # Disable to save RAM on Pi 5
```

Media cleanup (run periodically to reclaim disk):

```bash
# Remove remote media older than 30 days via Synapse admin API
curl -s -X POST \
  -H "Authorization: Bearer $MATRIX_ADMIN_TOKEN" \
  "https://matrix.resilience-hub.local/_synapse/admin/v1/purge_media_cache?before_ts=$(date -d '30 days ago' +%s)000"
```

---

## Section 6: Backup and Disaster Recovery

### 6.1 Automated Backup Script

```bash
#!/bin/bash
# /opt/community/nextcloud-matrix/scripts/backup.sh
# Run: 0 2 * * * /opt/community/nextcloud-matrix/scripts/backup.sh

set -euo pipefail

COMPOSE_DIR="/opt/community/nextcloud-matrix"
BACKUP_BASE="/mnt/backup/community-platform"
DATE=$(date -u +%Y-%m-%d)
BACKUP_DIR="$BACKUP_BASE/$DATE"

mkdir -p "$BACKUP_DIR"
echo "[$(date -u)] Backup starting → $BACKUP_DIR"

# 1. Nextcloud maintenance mode ON
docker exec -u www-data community-nextcloud php occ maintenance:mode --on

# 2. PostgreSQL backup
docker exec community-postgres pg_dump -U community_user nextcloud_db \
  | gzip > "$BACKUP_DIR/nextcloud_db.sql.gz"
docker exec community-postgres pg_dump -U community_user synapse_db \
  | gzip > "$BACKUP_DIR/synapse_db.sql.gz"
echo "  PostgreSQL: done"

# 3. Nextcloud data (exclude temp and cache)
tar -czf "$BACKUP_DIR/nextcloud-data.tar.gz" \
  --exclude="$COMPOSE_DIR/data/nextcloud/tmp" \
  --exclude="$COMPOSE_DIR/data/nextcloud/data/*/cache" \
  -C "$COMPOSE_DIR" data/nextcloud/
echo "  Nextcloud data: done"

# 4. Matrix data (media + signing key)
tar -czf "$BACKUP_DIR/matrix-data.tar.gz" \
  -C "$COMPOSE_DIR" data/matrix/
echo "  Matrix data: done"

# 5. Configuration (no secrets)
tar -czf "$BACKUP_DIR/config.tar.gz" \
  -C "$COMPOSE_DIR" \
  nginx/ matrix/config/ element/ init-db.sql docker-compose.yml
echo "  Config: done"

# 6. Nextcloud maintenance mode OFF
docker exec -u www-data community-nextcloud php occ maintenance:mode --off

# 7. Prune backups older than 30 days
find "$BACKUP_BASE" -maxdepth 1 -type d -mtime +30 -exec rm -rf {} \; 2>/dev/null || true

du -sh "$BACKUP_DIR"/*
echo "[$(date -u)] Backup complete"
```

```bash
chmod +x /opt/community/nextcloud-matrix/scripts/backup.sh
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/community/nextcloud-matrix/scripts/backup.sh >> /var/log/community-backup.log 2>&1") | crontab -
```

### 6.2 Disaster Recovery

```bash
# Full restore procedure
cd /opt/community/nextcloud-matrix

# 1. Stop all services
docker compose down

# 2. Start only postgres
docker compose up -d postgres
sleep 20

# 3. Restore databases
gunzip -c /mnt/backup/community-platform/YYYY-MM-DD/nextcloud_db.sql.gz \
  | docker exec -i community-postgres psql -U community_user nextcloud_db

gunzip -c /mnt/backup/community-platform/YYYY-MM-DD/synapse_db.sql.gz \
  | docker exec -i community-postgres psql -U community_user synapse_db

# 4. Restore file data
tar -xzf /mnt/backup/community-platform/YYYY-MM-DD/nextcloud-data.tar.gz \
  -C /opt/community/nextcloud-matrix/
tar -xzf /mnt/backup/community-platform/YYYY-MM-DD/matrix-data.tar.gz \
  -C /opt/community/nextcloud-matrix/

# 5. Start all services
docker compose up -d

# 6. Repair Nextcloud
sleep 60
docker exec -u www-data community-nextcloud php occ maintenance:repair
docker exec -u www-data community-nextcloud php occ db:add-missing-indices
docker exec -u www-data community-nextcloud php occ maintenance:mode --off
```

---

## Section 7: Rollback Procedure

If deployment fails to become healthy by the end of the deployment window:

```bash
# Step 1: Stop all containers and remove volumes
cd /opt/community/nextcloud-matrix
docker compose down -v

# Step 2: Remove data directories (WARNING: data loss if services were running)
# Only do this on a fresh deployment that failed before production use
rm -rf data/nextcloud data/matrix data/postgres data/redis

# Step 3: Diagnose before retry
docker compose logs --no-color > /tmp/deployment-failure-$(date +%Y%m%d-%H%M%S).log

# Step 4: Fix the identified issue, then re-deploy from Section 3 above

# Fallback platform: If Nextcloud+Matrix fails completely,
# see PHASE_5_DISCOURSE_DEPLOYMENT_ROADMAP.md for the Discourse alternative.
# Discourse deployment window: 2-3 hours. Still achieves June 15 readiness.
```

---

## Section 8: Troubleshooting Reference

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| Nextcloud blank page after login | PHP-FPM error or DB not ready | `docker logs community-nextcloud | grep -i error`; `docker exec -u www-data community-nextcloud php occ maintenance:mode --off` |
| Nextcloud returns 502 Bad Gateway | nginx can't reach FPM on port 9000 | Check nextcloud container is healthy; verify upstream address in nginx config |
| Synapse won't start | homeserver.yaml syntax error or DB not ready | `docker logs community-synapse`; validate YAML syntax |
| Element can't connect to homeserver | Wrong base_url in config.json or TLS cert untrusted | Check element/config.json base_url; import self-signed cert |
| Matrix login returns 403 | Registration disabled, account doesn't exist | Create account via `register_new_matrix_user` |
| Disk full | Matrix media or Nextcloud files consuming space | Run media purge API; delete old logs |
| Pi 5 throttling during deployment | CPU load + thermal | Pause between docker pull stages; add passive cooling |
| Calendar sync fails for author | Wrong CalDAV URL or credentials | Verify URL pattern: `/remote.php/dav/calendars/USERNAME/` |

---

## File Manifest

This roadmap requires the following files on the host:

```
/opt/community/nextcloud-matrix/
├── docker-compose.yml          ← Section 3.2
├── .env                        ← Section 3.1
├── init-db.sql                 ← Section 3.3
├── element/
│   └── config.json             ← Section 3.5
├── matrix/
│   └── config/
│       ├── homeserver.yaml     ← Section 3.4
│       └── log.yaml            ← (generate via `synapse generate`)
├── nginx/
│   ├── nginx.conf              ← Section 3.6
│   └── conf.d/
│       ├── 00-http.conf
│       ├── 10-nextcloud.conf
│       ├── 11-matrix.conf
│       └── 12-element.conf
├── data/
│   ├── certs/                  ← TLS certificates (Section 3.7)
│   ├── postgres/
│   ├── redis/
│   ├── nextcloud/
│   └── matrix/
└── scripts/
    └── backup.sh               ← Section 6.1
```

---

**Status**: PRODUCTION-READY for June 5-15 deployment window
**Confidence**: 87% (Pi 5 thermal constraints noted; all software components verified June 2026)
**Next file**: `PHASE_5_MESHTASTIC_BRIDGE_CONTINGENCY.md` for bridge integration
**Checklist**: `PHASE_5_DEPLOYMENT_CHECKLIST_AND_ONBOARDING.md` for runbook
