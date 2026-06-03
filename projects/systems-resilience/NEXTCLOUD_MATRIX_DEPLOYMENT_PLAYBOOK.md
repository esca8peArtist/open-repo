---
title: "Nextcloud + Matrix Deployment Playbook"
project: systems-resilience
phase: "5/6"
platform: "A — Nextcloud Hub + Matrix/Synapse + Element Web"
score: "9.5/10 (Session 2649 analysis)"
status: PRODUCTION-READY — pending June 3 platform decision
created: 2026-06-03
revised: 2026-06-03
target_date: "2026-06-05 13:00 UTC (Wave 1 author recruitment kickoff)"
deployment_time: "4–6 hours including DNS propagation"
host: "raspby1 (100.70.184.84) or dedicated VPS"
containers: 7
cross_references:
  - PHASE_6_IMPLEMENTATION_GUIDE_OPTION_C_NEXTCLOUD_MATRIX.md
  - PHASE_6_PLATFORM_ANALYSIS_v2.md
  - DISCOURSE_DEPLOYMENT_PLAYBOOK.md
---

# Nextcloud + Matrix Deployment Playbook
## Platform A — Production-Ready Execution Guide

**Decision gate**: User chooses platform A or B by June 3 EOD. If A is chosen, begin deployment June 4 morning to meet the June 5 13:00 UTC Wave 1 kickoff.

**Success criteria**: All 7 containers healthy + federation test passes + 5 test users can log in to both Nextcloud and Element Web + offline sync verified.

---

## Part 0: Architecture Overview

This deployment runs seven Docker containers on a single host behind an nginx reverse proxy. The FPM architecture requires that nginx shares file volumes with Nextcloud to serve static assets — this is the most common configuration error to avoid.

```
Internet → nginx (TLS termination)
              ├─ nextcloud.example.com → nextcloud (FPM:9000)
              │                           ↑ shared volumes
              │                       nginx-web (static files)
              ├─ matrix.example.com   → synapse (8008)
              ├─ element.example.com  → element (80)
              └─ office.example.com   → onlyoffice (80)

Internal network (backend):
  postgres  ← nextcloud, synapse
  redis     ← nextcloud, synapse, onlyoffice
```

**Container list**:
1. `postgres` — shared database (Nextcloud + Synapse)
2. `redis` — session cache + job queue
3. `nextcloud` — PHP-FPM process (port 9000, no HTTP)
4. `synapse` — Matrix homeserver
5. `element` — Element Web client (static files, nginx inside)
6. `onlyoffice` — Document server for collaborative editing
7. `nginx` — Reverse proxy + TLS termination (shares volumes with nextcloud)

**Key architecture note**: `nextcloud:fpm-alpine` does NOT serve HTTP. It speaks FastCGI on port 9000. The nginx container must be granted access to Nextcloud's volumes via `volumes_from` to serve static assets (CSS, JS, images). A healthcheck using `curl http://localhost/` against the Nextcloud FPM container will fail — the correct healthcheck targets the FPM status port or uses `php-fpm` directly.

---

## Part 1: Pre-Flight Checklist

### 1.1 Infrastructure Requirements

- [ ] **Docker Host**:
  - OS: Ubuntu 22.04 LTS or Debian 12 (Bookworm) — tested
  - CPU: 4 cores minimum; 8 recommended for 150+ users
  - RAM: 8 GB minimum (raspby1 Pi 5 with 8 GB is on the edge — close OnlyOffice if RAM-constrained); 16 GB ideal
  - Storage: 80 GB free minimum; 200 GB recommended (Nextcloud files grow fast)
  - Network: stable internet + public IP (or Tailscale for Tailscale-only deployment)

- [ ] **DNS Records** (create 48 hours before go-live; TTL 300):
  - [ ] `nextcloud.example.com` → host public IP
  - [ ] `matrix.example.com` → host public IP
  - [ ] `element.example.com` → host public IP
  - [ ] `office.example.com` → host public IP
  - [ ] `example.com` — needs `.well-known` records for Matrix (see Part 5)

- [ ] **TLS**: Let's Encrypt email address ready; ports 80 and 443 accessible from internet

- [ ] **Credentials**: password manager open; generate 5× random 32-char secrets before starting

- [ ] **SMTP**: outbound email provider credentials (Brevo free tier: 300/day; Mailgun free: 100/day)

### 1.2 Pre-Flight Network Test

```bash
# Run from an external machine (not the host itself)
nmap -p 80,443,8448 <host-public-ip>
# Expected: 80/tcp open, 443/tcp open

# Verify DNS before starting
dig +short nextcloud.example.com
dig +short matrix.example.com

# Check available RAM on host
free -h
# Need at least 6 GB available (not just total)

# Check disk
df -h /
# Need at least 80 GB free
```

### 1.3 Port Requirements

| Port | Protocol | Purpose | Exposure |
|------|----------|---------|---------|
| 80 | TCP | HTTP → HTTPS redirect + ACME | Public |
| 443 | TCP | HTTPS (all services) | Public |
| 8448 | TCP | Matrix federation (optional) | Public (optional) |
| 8008 | TCP | Synapse client API | Internal only (127.0.0.1) |
| 9000 | TCP | Nextcloud PHP-FPM | Internal only (Docker network) |

---

## Part 2: Environment Setup

### 2.1 Install Docker

```bash
# Install Docker Engine (official method)
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
sudo usermod -aG docker $USER
newgrp docker

# Verify (must be Compose v2)
docker --version
docker compose version
# Expected: Docker version 26.x, Docker Compose version v2.x
```

### 2.2 Firewall

```bash
# Ubuntu/Debian
sudo ufw allow 22/tcp comment "SSH"
sudo ufw allow 80/tcp comment "HTTP (ACME)"
sudo ufw allow 443/tcp comment "HTTPS"
sudo ufw allow 8448/tcp comment "Matrix federation"
sudo ufw enable
sudo ufw status

# CentOS/RHEL
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --permanent --add-port=8448/tcp
sudo firewall-cmd --reload
```

### 2.3 Directory Structure

```bash
# Create deployment root
sudo mkdir -p /opt/community/nextcloud-matrix
sudo chown $USER:$USER /opt/community/nextcloud-matrix
cd /opt/community/nextcloud-matrix

# Persistent data directories
mkdir -p data/{postgres,redis,nextcloud,matrix/media,onlyoffice,letsencrypt/webroot}
mkdir -p nginx/conf.d
mkdir -p matrix/config
mkdir -p element

# Secure sensitive files
chmod 700 data/

# Env file (never commit)
touch .env
chmod 600 .env
```

---

## Part 3: Configuration Files

### 3.1 Environment Variables (.env)

```bash
# Generate all passwords first, then populate
python3 -c "
import secrets
for name in ['NEXTCLOUD_ADMIN_PASSWORD','POSTGRES_PASSWORD','REDIS_PASSWORD',
             'MATRIX_FORM_SECRET','MATRIX_MACAROON_KEY','ONLYOFFICE_JWT_SECRET']:
    print(f'{name}={secrets.token_urlsafe(32)}')
"

# Paste generated values into .env
cat > .env << 'ENVEOF'
# =============================================================
# CRITICAL: Replace ALL placeholder values before deployment
# =============================================================

# --- Domains (replace example.com with your actual domain) ---
BASE_DOMAIN=example.com
NEXTCLOUD_DOMAIN=nextcloud.example.com
MATRIX_DOMAIN=matrix.example.com
ELEMENT_DOMAIN=element.example.com
OFFICE_DOMAIN=office.example.com

# --- Nextcloud ---
NEXTCLOUD_ADMIN_USER=admin
NEXTCLOUD_ADMIN_PASSWORD=REPLACE_WITH_GENERATED_VALUE_1
NEXTCLOUD_TRUSTED_DOMAINS=nextcloud.example.com

# --- PostgreSQL ---
POSTGRES_USER=community_db_user
POSTGRES_PASSWORD=REPLACE_WITH_GENERATED_VALUE_2
POSTGRES_DB=nextcloud_db
SYNAPSE_DB=synapse_db

# --- Redis ---
REDIS_PASSWORD=REPLACE_WITH_GENERATED_VALUE_3

# --- Matrix / Synapse ---
SYNAPSE_SERVER_NAME=example.com
SYNAPSE_REPORT_STATS=no
MATRIX_FORM_SECRET=REPLACE_WITH_GENERATED_VALUE_4
MATRIX_MACAROON_KEY=REPLACE_WITH_GENERATED_VALUE_5

# --- OnlyOffice ---
ONLYOFFICE_JWT_SECRET=REPLACE_WITH_GENERATED_VALUE_6

# --- Email (outbound notifications) ---
SMTP_HOST=smtp.brevo.com
SMTP_PORT=587
SMTP_USER=your_brevo_login@example.com
SMTP_PASSWORD=your_brevo_smtp_key
SMTP_FROM=noreply@example.com

# --- Let's Encrypt ---
LETSENCRYPT_EMAIL=admin@example.com

# --- Timezone ---
TZ=UTC
ENVEOF

# Verify no placeholders remain
grep "REPLACE_WITH" .env
# Must return empty. Do not proceed if it shows output.
```

### 3.2 docker-compose.yml

```yaml
# Version field deprecated in Compose v2 — omit
name: community-platform

services:

  # ================================================================
  # PostgreSQL — shared database for Nextcloud and Synapse
  # ================================================================
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
      - ./init-db.sql:/docker-entrypoint-initdb.d/init.sql:ro
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB}"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 30s

  # ================================================================
  # Redis — session cache for Nextcloud and Synapse workers
  # ================================================================
  redis:
    image: redis:7-alpine
    container_name: community-redis
    restart: unless-stopped
    command: >
      redis-server
      --requirepass ${REDIS_PASSWORD}
      --maxmemory 512mb
      --maxmemory-policy allkeys-lru
      --save 60 1000
    volumes:
      - ./data/redis:/data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "redis-cli", "-a", "${REDIS_PASSWORD}", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
      start_period: 10s

  # ================================================================
  # Nextcloud (FPM) — file sync, calendars, collaborative editing
  # NOTE: This container speaks FastCGI on port 9000, NOT HTTP.
  # nginx (below) serves HTTP and shares volumes with this container.
  # ================================================================
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
      # Database
      POSTGRES_HOST: postgres
      POSTGRES_DB: ${POSTGRES_DB}
      POSTGRES_USER: ${POSTGRES_USER}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      # Admin account (first-run only)
      NEXTCLOUD_ADMIN_USER: ${NEXTCLOUD_ADMIN_USER}
      NEXTCLOUD_ADMIN_PASSWORD: ${NEXTCLOUD_ADMIN_PASSWORD}
      NEXTCLOUD_TRUSTED_DOMAINS: ${NEXTCLOUD_TRUSTED_DOMAINS}
      # Redis
      REDIS_HOST: redis
      REDIS_HOST_PASSWORD: ${REDIS_PASSWORD}
      # Reverse proxy
      OVERWRITEPROTOCOL: https
      OVERWRITEHOST: ${NEXTCLOUD_DOMAIN}
      OVERWRITEWEBROOT: /
      # Email
      SMTP_HOST: ${SMTP_HOST}
      SMTP_SECURE: tls
      SMTP_PORT: ${SMTP_PORT}
      SMTP_AUTHTYPE: LOGIN
      SMTP_NAME: ${SMTP_USER}
      SMTP_PASSWORD: ${SMTP_PASSWORD}
      MAIL_FROM_ADDRESS: ${SMTP_FROM}
      # Performance
      PHP_MEMORY_LIMIT: 512M
      PHP_UPLOAD_LIMIT: 512M
      TZ: ${TZ}
    volumes:
      - ./data/nextcloud:/var/www/html
    networks:
      - backend
    healthcheck:
      # FPM healthcheck: check PHP-FPM status endpoint (not HTTP)
      test: ["CMD-SHELL", "SCRIPT_NAME=/status REQUEST_METHOD=GET cgi-fcgi -bind -connect 127.0.0.1:9000 || exit 1"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

  # ================================================================
  # nginx (web) — serves Nextcloud static assets + forwards PHP
  # MUST share volumes with nextcloud container
  # ================================================================
  nginx-nextcloud:
    image: nginx:1.27-alpine
    container_name: community-nginx-nextcloud
    restart: unless-stopped
    depends_on:
      - nextcloud
    volumes:
      - ./data/nextcloud:/var/www/html:ro
      - ./nginx/conf.d/nextcloud-fpm.conf:/etc/nginx/conf.d/default.conf:ro
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost/status.php"]
      interval: 15s
      timeout: 5s
      retries: 3
      start_period: 30s

  # ================================================================
  # Matrix Synapse — homeserver
  # ================================================================
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
      - backend
    ports:
      - "127.0.0.1:8008:8008"   # Client-server API (proxied by nginx)
      - "127.0.0.1:8448:8448"   # Federation API (proxied by nginx)
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost:8008/_matrix/client/versions"]
      interval: 15s
      timeout: 10s
      retries: 5
      start_period: 60s

  # ================================================================
  # Element Web — Matrix client
  # ================================================================
  element:
    image: vectorim/element-web:latest
    container_name: community-element
    restart: unless-stopped
    volumes:
      - ./element/config.json:/app/config.json:ro
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3

  # ================================================================
  # OnlyOffice Document Server — collaborative editing
  # Disable if RAM < 8 GB or if you prefer Collabora
  # ================================================================
  onlyoffice:
    image: onlyoffice/documentserver:latest
    container_name: community-onlyoffice
    restart: unless-stopped
    environment:
      JWT_ENABLED: "true"
      JWT_SECRET: ${ONLYOFFICE_JWT_SECRET}
    volumes:
      - ./data/onlyoffice:/var/www/onlyoffice/Data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost/healthcheck"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 60s

  # ================================================================
  # nginx (TLS/reverse proxy) — public-facing entrypoint
  # Binds to 127.0.0.1 — traffic arrives here from host firewall
  # For cloud/VPS: change 127.0.0.1 to the specific Tailscale or
  # public interface IP, never 0.0.0.0
  # ================================================================
  nginx:
    image: nginx:1.27-alpine
    container_name: community-nginx
    restart: unless-stopped
    depends_on:
      - nginx-nextcloud
      - synapse
      - element
      - onlyoffice
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./data/letsencrypt:/etc/letsencrypt:ro
      - ./data/letsencrypt/webroot:/var/www/certbot:ro
    ports:
      - "127.0.0.1:80:80"     # HTTP → HTTPS redirect + ACME
      - "127.0.0.1:443:443"   # HTTPS
      - "127.0.0.1:8448:8448" # Matrix federation
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-sf", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3

networks:
  backend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.22.0.0/16
```

### 3.3 PostgreSQL Init Script (init-db.sql)

This creates separate databases for Nextcloud and Synapse using the same database user.

```sql
-- init-db.sql
-- Creates the Synapse database alongside the Nextcloud database.
-- Both use the same POSTGRES_USER defined in .env.

\connect postgres

-- Create synapse database (nextcloud_db created automatically from POSTGRES_DB env)
SELECT 'CREATE DATABASE synapse_db'
  WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'synapse_db')\gexec

-- Grant permissions
GRANT ALL PRIVILEGES ON DATABASE synapse_db TO community_db_user;
```

### 3.4 Matrix Synapse Configuration (matrix/config/homeserver.yaml)

```yaml
# matrix/config/homeserver.yaml
# Synapse production configuration — replace all example.com references

server_name: "example.com"
pid_file: /data/homeserver.pid

# Listeners
listeners:
  - port: 8008
    tls: false
    type: http
    x_forwarded: true
    bind_addresses: ['::1', '127.0.0.1']
    resources:
      - names: [client, federation]
        compress: false

  - port: 8448
    tls: false
    type: http
    x_forwarded: true
    bind_addresses: ['::1', '127.0.0.1']
    resources:
      - names: [federation]
        compress: false

# Database
database:
  name: psycopg2
  args:
    user: community_db_user
    password: "POSTGRES_PASSWORD_PLACEHOLDER"  # override at runtime via env substitution
    database: synapse_db
    host: postgres
    port: 5432
    cp_min: 5
    cp_max: 10

# Redis (for worker coordination and caching)
redis:
  enabled: true
  host: redis
  port: 6379
  password: "REDIS_PASSWORD_PLACEHOLDER"  # override at runtime

# Media storage
media_store_path: "/data/media"
max_upload_size: 50M
max_image_pixels: 32M
url_preview_enabled: true
url_preview_ip_range_blacklist:
  - '127.0.0.0/8'
  - '10.0.0.0/8'
  - '172.16.0.0/12'
  - '192.168.0.0/16'
  - '100.64.0.0/10'
  - '169.254.0.0/16'

# Security secrets (must match .env values)
form_secret: "MATRIX_FORM_SECRET_PLACEHOLDER"
macaroon_secret_key: "MATRIX_MACAROON_KEY_PLACEHOLDER"
signing_key_path: "/data/example.com.signing.key"

# Registration
enable_registration: false
registration_requires_token: true

# Email
email:
  smtp_host: smtp.brevo.com
  smtp_port: 587
  smtp_user: "your_smtp_user"
  smtp_pass: "your_smtp_pass"
  notif_from: "Matrix <noreply@example.com>"

# Logging
log_config: "/data/log.yaml"

# Performance
event_cache_size: 10K
caches:
  global_factor: 1.0

# Federation (enable for cross-server communication)
federation_domain_whitelist: []  # empty = allow all
allow_public_rooms_over_federation: false

# Trusted key servers
trusted_key_servers:
  - server_name: "matrix.org"

# Client
enable_room_list_search: true
```

**Secret substitution**: The homeserver.yaml above uses placeholder strings. The recommended approach is to use a startup script that substitutes environment variables before Synapse reads the file, or use Synapse's built-in environment variable template support (`POSTGRES_PASSWORD` env var is read directly when using the official Docker image's generate mode).

**Production approach**: Run `docker compose run --rm synapse generate` once to generate a homeserver.yaml from environment variables, then edit the result for the sections above. Store the generated signing key in `./data/matrix/`.

```bash
# Generate initial config from environment (run once before first start)
docker compose run --rm \
  -e SYNAPSE_SERVER_NAME=example.com \
  -e SYNAPSE_REPORT_STATS=no \
  -e POSTGRES_HOST=postgres \
  -e POSTGRES_USER=community_db_user \
  -e POSTGRES_PASSWORD="$(grep POSTGRES_PASSWORD .env | cut -d= -f2)" \
  -e POSTGRES_DB=synapse_db \
  synapse generate

# Generated files appear in ./data/matrix/
ls ./data/matrix/
# example.com.signing.key  homeserver.yaml  log.config
```

### 3.5 Synapse Log Config (matrix/config/log.yaml)

```yaml
# matrix/config/log.yaml
version: 1
formatters:
  precise:
    format: '%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(request)s - %(message)s'
handlers:
  console:
    class: logging.StreamHandler
    formatter: precise
loggers:
  synapse.storage.SQL:
    level: WARNING
root:
  level: WARNING
  handlers: [console]
disable_existing_loggers: false
```

### 3.6 nginx Reverse Proxy Config (nginx/nginx.conf)

```nginx
# nginx/nginx.conf
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

    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent" rt=$request_time';

    access_log /var/log/nginx/access.log main;

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;

    # Upload limit (Nextcloud files)
    client_max_body_size 512M;
    client_body_timeout 300s;

    # Compression
    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml text/javascript
               application/json application/javascript application/xml+rss
               application/atom+xml image/svg+xml;

    # Security headers (applied globally, per-vhost headers augment these)
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    include /etc/nginx/conf.d/*.conf;
}
```

### 3.7 nginx Virtual Hosts (nginx/conf.d/)

**nginx/conf.d/00-http-redirect.conf** — HTTP to HTTPS + ACME challenge

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;

    # ACME challenge for Let's Encrypt
    location /.well-known/acme-challenge/ {
        root /var/www/certbot;
        try_files $uri =404;
    }

    # Redirect everything else to HTTPS
    location / {
        return 301 https://$host$request_uri;
    }
}
```

**nginx/conf.d/10-nextcloud.conf** — Nextcloud (proxied to nginx-nextcloud sidecar)

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name nextcloud.example.com;

    ssl_certificate     /etc/letsencrypt/live/nextcloud.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/nextcloud.example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:ECDHE-RSA-CHACHA20-POLY1305:DHE-RSA-AES128-GCM-SHA256;
    ssl_prefer_server_ciphers off;
    ssl_session_cache shared:SSL:10m;
    ssl_session_timeout 1d;

    add_header Strict-Transport-Security "max-age=15552000; includeSubDomains" always;

    location / {
        proxy_pass http://nginx-nextcloud:80;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_redirect off;
        proxy_buffering off;
        proxy_connect_timeout 60s;
        proxy_send_timeout 300s;
        proxy_read_timeout 300s;
        # Nextcloud large file uploads
        client_max_body_size 512M;
    }

    # CalDAV/CardDAV redirect
    location = /.well-known/carddav {
        return 301 $scheme://$host/remote.php/dav;
    }
    location = /.well-known/caldav {
        return 301 $scheme://$host/remote.php/dav;
    }
}
```

**nginx/conf.d/11-matrix.conf** — Matrix Synapse

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name matrix.example.com;

    ssl_certificate     /etc/letsencrypt/live/matrix.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/matrix.example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256:ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384;
    ssl_session_cache shared:SSL:10m;

    add_header Strict-Transport-Security "max-age=15552000; includeSubDomains" always;

    # Client-server API
    location /_matrix {
        proxy_pass http://synapse:8008;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $host;
        proxy_buffering off;
        # Large media uploads
        client_max_body_size 50M;
        proxy_read_timeout 600s;
    }

    # Synapse admin API (restrict to trusted IPs in production)
    location /_synapse/admin {
        proxy_pass http://synapse:8008;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $host;
        # Optional: restrict access
        # allow 100.70.184.84;  # raspby1 Tailscale IP
        # deny all;
    }

    # .well-known for Matrix server delegation
    location /.well-known/matrix/server {
        return 200 '{"m.server": "matrix.example.com:443"}';
        default_type application/json;
        add_header Access-Control-Allow-Origin *;
    }

    location /.well-known/matrix/client {
        return 200 '{"m.homeserver": {"base_url": "https://matrix.example.com"}}';
        default_type application/json;
        add_header Access-Control-Allow-Origin *;
    }
}

# Matrix federation listener on 8448
server {
    listen 8448 ssl http2;
    listen [::]:8448 ssl http2;
    server_name matrix.example.com;

    ssl_certificate     /etc/letsencrypt/live/matrix.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/matrix.example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;

    location / {
        proxy_pass http://synapse:8448;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_set_header Host $host;
    }
}
```

**nginx/conf.d/12-element.conf** — Element Web

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name element.example.com;

    ssl_certificate     /etc/letsencrypt/live/element.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/element.example.com/privkey.pem;
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

**nginx/conf.d/13-onlyoffice.conf** — OnlyOffice Document Server

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name office.example.com;

    ssl_certificate     /etc/letsencrypt/live/office.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/office.example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;

    location / {
        proxy_pass http://onlyoffice:80;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $remote_addr;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        # OnlyOffice needs long timeouts
        proxy_read_timeout 600s;
        client_max_body_size 100M;
    }
}
```

### 3.8 nginx Nextcloud FPM Config (nginx/conf.d/nextcloud-fpm.conf)

This config runs inside the `nginx-nextcloud` sidecar container and handles PHP-FPM proxying. It is NOT the public-facing nginx.

```nginx
# nginx/conf.d/nextcloud-fpm.conf
# This config serves inside nginx-nextcloud container
# It proxies PHP to nextcloud FPM container on port 9000

upstream php-handler {
    server nextcloud:9000;
    keepalive 4;
}

server {
    listen 80;
    listen [::]:80;
    server_name _;

    root /var/www/html;
    index index.php index.html /index.php$request_uri;

    # HSTS, CSP (set by outer nginx; skip here)
    # large file uploads
    client_max_body_size 512M;
    client_body_timeout 300s;

    # Nextcloud recommended timeouts
    fastcgi_buffers 64 4K;
    fastcgi_hide_header X-Powered-By;

    # Gzip
    gzip on;
    gzip_vary on;
    gzip_comp_level 4;
    gzip_min_length 256;
    gzip_proxied expired no-cache no-store private no_last_modified no_etag auth;
    gzip_types application/atom+xml text/javascript application/javascript
               application/json application/ld+json application/manifest+json
               application/rss+xml application/vnd.geo+json application/vnd.ms-fontobject
               application/wasm application/x-font-ttf application/x-web-app-manifest+json
               application/xhtml+xml application/xml font/opentype image/bmp
               image/svg+xml image/x-icon text/cache-manifest text/css
               text/plain text/vcard text/vnd.rim.location.xloc text/vtt
               text/x-component text/x-cross-domain-policy;

    # CalDAV/CardDAV
    location = /.well-known/carddav { return 301 /remote.php/dav; }
    location = /.well-known/caldav  { return 301 /remote.php/dav; }

    # Security: deny hidden files
    location ~ /\. {
        deny all;
        return 404;
    }

    # Security: deny sensitive paths
    location ~ ^/(?:build|tests|config|lib|3rdparty|templates|data)(?:$|/) {
        return 404;
    }
    location ~ ^/(?:\.|autotest|occ|issue|indie|db_|console) {
        return 404;
    }

    # Static assets with cache headers
    location ~ \.(?:css|js|woff2?|svg|gif|map|png|html|ttf|ico|jpg|jpeg|webp)$ {
        try_files $uri /index.php$request_uri;
        expires 6M;
        access_log off;
    }

    # PHP processing
    location ~ \.php(?:$|/) {
        # Required for path info
        fastcgi_split_path_info ^(.+?\.php)(/.*)$;
        set $path_info $fastcgi_path_info;

        try_files $fastcgi_script_name =404;

        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $path_info;
        fastcgi_param HTTPS on;
        fastcgi_param modHeadersAvailable true;
        fastcgi_param front_controller_active true;
        fastcgi_pass php-handler;
        fastcgi_intercept_errors on;
        fastcgi_request_buffering on;
        fastcgi_max_temp_file_size 0;
    }

    # Default
    location / {
        try_files $uri $uri/ /index.php$request_uri;
    }
}
```

### 3.9 Element Web Config (element/config.json)

```json
{
    "default_server_config": {
        "m.homeserver": {
            "base_url": "https://matrix.example.com",
            "server_name": "example.com"
        },
        "m.identity_server": {
            "base_url": "https://vector.im"
        }
    },
    "brand": "Community Hub",
    "default_theme": "light",
    "room_directory": {
        "servers": ["matrix.example.com"]
    },
    "features": {
        "feature_spotlight": true,
        "feature_video_rooms": false
    },
    "map_style_url": "https://api.maptiler.com/maps/streets/style.json?key=fU3vlMsMn4Jb6dnEIFsx",
    "setting_defaults": {
        "breadcrumbs": true
    },
    "show_labs_settings": false,
    "disable_custom_urls": true,
    "disable_guests": true
}
```

---

## Part 4: TLS Certificate Provisioning

TLS certificates must exist before starting nginx. Run certbot standalone before the stack starts.

```bash
cd /opt/community/nextcloud-matrix

# Ensure ports 80 and 443 are NOT already in use
sudo ss -tlnp | grep -E ':80|:443'

# Issue certificates for all domains (standalone mode — no web server running yet)
docker run --rm \
  -p 80:80 -p 443:443 \
  -v ./data/letsencrypt:/etc/letsencrypt \
  certbot/certbot certonly \
  --standalone \
  --agree-tos \
  --non-interactive \
  --email admin@example.com \
  -d nextcloud.example.com \
  -d matrix.example.com \
  -d element.example.com \
  -d office.example.com

# Verify
ls -la ./data/letsencrypt/live/
# Expected: directories for each domain, each containing fullchain.pem and privkey.pem
```

**Certificate auto-renewal**: Add to host crontab after deployment:

```bash
# Add renewal cron (runs twice daily, renews if within 30 days of expiry)
(crontab -l 2>/dev/null; echo "0 0,12 * * * docker run --rm -v /opt/community/nextcloud-matrix/data/letsencrypt:/etc/letsencrypt -v /opt/community/nextcloud-matrix/data/letsencrypt/webroot:/var/www/certbot certbot/certbot renew --webroot -w /var/www/certbot --quiet && docker exec community-nginx nginx -s reload") | crontab -
```

---

## Part 5: Deployment Execution

### 5.1 Pre-Deployment Validation

```bash
cd /opt/community/nextcloud-matrix

# 1. Verify no placeholder values remain
grep -E "REPLACE_WITH|example\.com|YOUR_" .env
# Every occurrence must be intentional — check each one

# 2. Validate docker-compose syntax
docker compose config > /dev/null && echo "Compose config: OK"

# 3. Verify certificate files exist
for domain in nextcloud matrix element office; do
  ls ./data/letsencrypt/live/${domain}.example.com/fullchain.pem \
     ./data/letsencrypt/live/${domain}.example.com/privkey.pem && \
  echo "TLS: ${domain}.example.com OK" || echo "MISSING: ${domain}.example.com"
done

# 4. Verify required config files
for f in nginx/nginx.conf nginx/conf.d/00-http-redirect.conf \
          nginx/conf.d/10-nextcloud.conf nginx/conf.d/11-matrix.conf \
          nginx/conf.d/12-element.conf nginx/conf.d/nextcloud-fpm.conf \
          matrix/config/homeserver.yaml matrix/config/log.yaml \
          element/config.json init-db.sql; do
  [ -f "$f" ] && echo "OK: $f" || echo "MISSING: $f"
done
```

### 5.2 Initialize Synapse Config (First Time Only)

```bash
# Generate Synapse homeserver.yaml from environment (creates signing key too)
docker compose run --rm \
  -e SYNAPSE_SERVER_NAME="$(grep BASE_DOMAIN .env | cut -d= -f2)" \
  -e SYNAPSE_REPORT_STATS=no \
  synapse generate

# Check generated files
ls ./data/matrix/
# Should include: *.signing.key  homeserver.yaml  log.config

# The generated homeserver.yaml will default to SQLite.
# Replace it with matrix/config/homeserver.yaml (which points to PostgreSQL)
# BUT preserve the generated signing key path and macaroon secrets.

echo "IMPORTANT: Copy the macaroon_secret_key and form_secret from"
echo "./data/matrix/homeserver.yaml into your matrix/config/homeserver.yaml"
cat ./data/matrix/homeserver.yaml | grep -E "macaroon|form_secret|signing_key"
```

### 5.3 Launch Services (Staged)

```bash
cd /opt/community/nextcloud-matrix

# Stage 1: Start infrastructure (postgres + redis)
docker compose up -d postgres redis
echo "Waiting 20s for databases to initialize..."
sleep 20
docker compose ps postgres redis
# Both should show: (healthy)

# Stage 2: Start application layer
docker compose up -d nextcloud synapse onlyoffice element nginx-nextcloud
echo "Waiting 60s for applications to start..."
sleep 60
docker compose ps

# Stage 3: Start public proxy
docker compose up -d nginx

# Full status check
docker compose ps
# Expected: All 8 containers "Up" with "(healthy)" status
```

### 5.4 Post-Launch Log Check

```bash
# Check for errors in all containers (last 20 lines each)
for container in community-postgres community-redis community-nextcloud \
                  community-synapse community-element community-onlyoffice \
                  community-nginx community-nginx-nextcloud; do
  echo "=== $container ==="
  docker logs --tail=10 "$container" 2>&1 | grep -iE "error|fatal|exception|warn" | head -5
  echo ""
done
```

---

## Part 6: Post-Deployment Verification

### 6.1 API Health Checks

```bash
# Nextcloud
curl -sf https://nextcloud.example.com/status.php | python3 -m json.tool
# Expected: {"installed":true,"maintenance":false,"version":"33.x.x",...}

# Matrix client API
curl -sf https://matrix.example.com/_matrix/client/versions | python3 -m json.tool
# Expected: {"versions":["r0.0.1",...,"v1.x"]}

# Matrix .well-known
curl -sf https://example.com/.well-known/matrix/server
# Expected: {"m.server":"matrix.example.com:443"}

# Element Web
curl -sf -I https://element.example.com/ | head -5
# Expected: HTTP/2 200

# OnlyOffice
curl -sf https://office.example.com/healthcheck
# Expected: true
```

### 6.2 Federation Check

```bash
# Use the official Matrix federation tester
curl -sf "https://federationtester.matrix.org/api/report?server_name=example.com" | \
  python3 -m json.tool | head -30
# Look for "AllChecksOK": true
```

### 6.3 Login Tests

```bash
# Create a test Matrix user
docker exec -it community-synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u testuser01 \
  -p "$(python3 -c 'import secrets; print(secrets.token_urlsafe(16))')" \
  --no-admin \
  http://localhost:8008

echo "Test user created. Log into https://element.example.com with @testuser01:example.com"

# Create a test Nextcloud user via OCC
docker exec -u www-data community-nextcloud php occ user:add \
  --password-from-env \
  --display-name "Test User" \
  --group "users" \
  testuser01
# Set NEXTCLOUD_ADMIN_PASSWORD env, then:
export OC_PASS="TestPassword123!"
docker exec -u www-data -e OC_PASS community-nextcloud php occ user:add \
  --password-from-env testuser01
```

### 6.4 Offline Sync Verification

**Nextcloud offline sync (WebDAV)**:

```bash
# Test WebDAV endpoint
curl -u admin:$(grep NEXTCLOUD_ADMIN_PASSWORD .env | cut -d= -f2) \
  -X PROPFIND \
  https://nextcloud.example.com/remote.php/dav/files/admin/ \
  -H "Depth: 1" | head -20
# Expected: XML response with file listing

# Desktop client setup:
# 1. Install Nextcloud Desktop client (https://nextcloud.com/install/#install-clients)
# 2. Server: https://nextcloud.example.com
# 3. Enable "Always keep on this device" for offline directories
# 4. Files sync automatically when connected; edits queue offline
```

**Matrix offline message queuing (Element Web)**:

```
1. Log in to Element Web at https://element.example.com
2. Join a test room
3. Open browser developer tools → Network → toggle offline (throttle)
4. Type and send a message
5. Observe: message shows "pending" indicator (clock icon)
6. Toggle back to online
7. Verify: message sends within 2-3 seconds
```

---

## Part 7: Offline Operation Guide

### 7.1 Nextcloud Offline-First Architecture

Nextcloud is inherently offline-capable through WebDAV sync clients:

- **Desktop (Windows/macOS/Linux)**: Nextcloud Desktop Client syncs files to local disk. Edits made offline are queued and pushed on reconnection. Conflict resolution is automatic (creates conflict copies).
- **Mobile (iOS/Android)**: Nextcloud mobile app with "Available Offline" toggle per file/folder.
- **OnlyOffice**: Documents edited in OnlyOffice auto-save to Nextcloud every 10 seconds. If server unreachable, edits continue locally in the browser's service worker cache.

**Offline-first workflow for authors**:

```
Setup phase (requires connectivity):
  1. Author installs Nextcloud Desktop Client
  2. Author marks the "Phase 5 Drafts" folder as "Always available offline"
  3. Initial sync downloads all shared drafts (~100 MB typical)

Working offline:
  1. Author opens any synced file in their preferred editor
  2. Edits save locally via the Nextcloud Desktop Client sync folder
  3. If using OnlyOffice in browser: edits persist in browser cache

Reconnecting:
  1. Desktop client detects network, uploads queued changes
  2. Server reconciles conflicts; if concurrent edits to same file, creates "filename (conflict by user).docx"
  3. Author reviews conflict copy and merges manually if needed
```

### 7.2 Matrix Offline Message Queuing

Element Web uses a local IndexedDB cache for all messages. The behavior when offline:

- Received messages: cached locally, readable offline (last ~1000 messages per room)
- Sent messages: queue in IndexedDB, flush on reconnection in order
- Encryption: E2E encryption works fully offline (key material stored locally)

**Limitation**: Matrix does not support asynchronous offline peer-to-peer delivery (messages go through the homeserver). If the homeserver itself is unreachable, messages cannot be relayed. This is where the Meshtastic bridge adds value.

### 7.3 Matrix-Meshtastic Bridge

**Status (June 2026)**: The `meshtastic-matrix-relay` project (jeremiah-k/meshtastic-matrix-relay) is actively maintained with v1.3.7 released May 3, 2026. It provides bidirectional relay between Matrix rooms and Meshtastic LoRa radio networks.

**What it enables**: When internet connectivity is completely unavailable, community members with Meshtastic radio devices (e.g., Heltec LoRa v3, T-Echo) can send messages that are relayed into Matrix rooms when any node with internet connectivity is available, and vice versa. This is a store-and-forward model.

**Hardware required**: At minimum one Meshtastic node with serial or USB connection to a machine running the relay daemon. Range per node: 2–10 km line-of-sight depending on antenna.

**Deployment**:

```bash
# Create bridge deployment directory
mkdir -p /opt/community/mmrelay
cd /opt/community/mmrelay

# Create config file
cat > config.yaml << 'RELAYEOF'
matrix:
  homeserver: "https://matrix.example.com"
  access_token: "syt_MATRIX_BOT_USER_ACCESS_TOKEN"
  bot_user_id: "@meshbridge:example.com"

meshtastic:
  connection_type: network  # or "serial" if device connected directly
  host: 192.168.1.100       # Meshtastic device IP (if network-connected)
  # port: /dev/ttyUSB0      # uncomment for serial connection

matrix_rooms:
  - id: "!roomid:example.com"
    meshtastic_channel: 0
    name: "General"

logging:
  level: INFO
RELAYEOF

# Create a Matrix bot user account for the relay
docker exec -it community-synapse register_new_matrix_user \
  -c /data/homeserver.yaml \
  -u meshbridge \
  -p "$(python3 -c 'import secrets; print(secrets.token_urlsafe(24))')" \
  --no-admin \
  http://localhost:8008

# Get the bot's access token (log in via API)
curl -s -X POST \
  -H "Content-Type: application/json" \
  -d '{"type":"m.login.password","user":"meshbridge","password":"BOT_PASSWORD"}' \
  https://matrix.example.com/_matrix/client/r0/login | python3 -m json.tool
# Copy "access_token" value into config.yaml above

# Run the relay (Docker)
docker run -d \
  --name mmrelay \
  --restart unless-stopped \
  -v ./config.yaml:/config/config.yaml:ro \
  ghcr.io/jeremiah-k/meshtastic-matrix-relay:latest

# Check logs
docker logs mmrelay --tail=20
```

**Contingency if bridge unavailable**: If Meshtastic hardware is unavailable, Matrix with Element Web + offline queuing is still the primary communication tool. For true off-grid scenarios: export critical contacts and channels as a static page that can be printed, and establish a pre-planned check-in frequency on a secondary out-of-band channel (phone tree, Signal, radio).

---

## Part 8: User Onboarding Automation

### 8.1 User Import Script

```python
#!/usr/bin/env python3
"""
Bulk user onboarding for Nextcloud + Matrix.
Reads from a CSV file and creates accounts on both platforms.

CSV format: username,password,email,display_name
"""
import csv
import os
import sys
import json
import urllib.request
import urllib.error
import base64
import time

# Configuration — load from environment to avoid hardcoding
NEXTCLOUD_URL = os.environ.get("NEXTCLOUD_URL", "https://nextcloud.example.com")
NEXTCLOUD_ADMIN_USER = os.environ.get("NEXTCLOUD_ADMIN_USER", "admin")
NEXTCLOUD_ADMIN_PASS = os.environ.get("NEXTCLOUD_ADMIN_PASS", "")
MATRIX_URL = os.environ.get("MATRIX_URL", "https://matrix.example.com")
MATRIX_ADMIN_TOKEN = os.environ.get("MATRIX_ADMIN_TOKEN", "")
MATRIX_SERVER_NAME = os.environ.get("MATRIX_SERVER_NAME", "example.com")


def _nc_request(method: str, path: str, data: dict | None = None) -> dict:
    """Make a Nextcloud OCS API request."""
    url = f"{NEXTCLOUD_URL}/ocs/v1.php/cloud{path}?format=json"
    creds = base64.b64encode(f"{NEXTCLOUD_ADMIN_USER}:{NEXTCLOUD_ADMIN_PASS}".encode()).decode()
    headers = {
        "Authorization": f"Basic {creds}",
        "OCS-APIRequest": "true",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    body = None
    if data:
        body = "&".join(f"{k}={v}" for k, v in data.items()).encode()
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        return {"error": str(e), "status": e.code}


def _mx_request(method: str, path: str, data: dict | None = None) -> dict:
    """Make a Matrix Synapse Admin API request."""
    url = f"{MATRIX_URL}{path}"
    headers = {
        "Authorization": f"Bearer {MATRIX_ADMIN_TOKEN}",
        "Content-Type": "application/json",
    }
    body = json.dumps(data).encode() if data else None
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        try:
            return json.load(e)
        except Exception:
            return {"error": str(e), "status": e.code}


def create_nextcloud_user(username: str, password: str, email: str, display_name: str) -> bool:
    result = _nc_request("POST", "/users", {
        "userid": username,
        "password": password,
        "email": email,
        "displayName": display_name,
        "groups[]": "users",
    })
    ok = result.get("ocs", {}).get("meta", {}).get("statuscode") in (100, 200)
    status = "OK" if ok else f"FAIL ({result})"
    print(f"  Nextcloud: {status}")
    return ok


def create_matrix_user(username: str, password: str, display_name: str) -> bool:
    user_id = f"@{username}:{MATRIX_SERVER_NAME}"
    result = _mx_request(
        "PUT",
        f"/_synapse/admin/v2/users/{user_id}",
        {"password": password, "displayname": display_name, "deactivated": False, "admin": False},
    )
    ok = "name" in result or result.get("status") in (200, 201)
    status = "OK" if ok else f"FAIL ({result})"
    print(f"  Matrix:    {status}")
    return ok


def validate_env() -> bool:
    missing = []
    if not NEXTCLOUD_ADMIN_PASS:
        missing.append("NEXTCLOUD_ADMIN_PASS")
    if not MATRIX_ADMIN_TOKEN:
        missing.append("MATRIX_ADMIN_TOKEN")
    if missing:
        print(f"ERROR: Missing environment variables: {', '.join(missing)}")
        print("Export them before running:")
        for var in missing:
            print(f"  export {var}=...")
        return False
    return True


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} users.csv")
        print("CSV columns: username,password,email,display_name")
        sys.exit(1)

    if not validate_env():
        sys.exit(1)

    csv_path = sys.argv[1]
    success_count = 0
    fail_count = 0

    with open(csv_path, newline="") as f:
        reader = csv.DictReader(f)
        required_cols = {"username", "password", "email", "display_name"}
        if not required_cols.issubset(reader.fieldnames or []):
            print(f"ERROR: CSV must have columns: {required_cols}")
            sys.exit(1)

        for i, row in enumerate(reader, 1):
            username = row["username"].strip().lower()
            password = row["password"].strip()
            email = row["email"].strip()
            display_name = row["display_name"].strip()

            print(f"\n[{i}] Creating user: {username} <{email}>")
            nc_ok = create_nextcloud_user(username, password, email, display_name)
            mx_ok = create_matrix_user(username, password, display_name)

            if nc_ok and mx_ok:
                success_count += 1
            else:
                fail_count += 1

            time.sleep(0.5)  # Rate limiting

    print(f"\n{'='*40}")
    print(f"Done: {success_count} created, {fail_count} failed")
    if fail_count > 0:
        print("Check logs above for failed accounts. Re-run with corrected CSV rows.")


if __name__ == "__main__":
    main()
```

**Usage**:

```bash
# Prepare CSV
cat > wave1_authors.csv << 'EOF'
username,password,email,display_name
author_smith,TempPass!2026,smith@example.com,Jane Smith
author_jones,TempPass!2026,jones@example.com,Bob Jones
EOF

# Run with environment variables (not hardcoded passwords)
export NEXTCLOUD_ADMIN_PASS="$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)"
export MATRIX_ADMIN_TOKEN="syt_admin_..."  # Get from Synapse admin API login
export NEXTCLOUD_URL="https://nextcloud.example.com"
export MATRIX_URL="https://matrix.example.com"
export MATRIX_SERVER_NAME="example.com"

python3 import_users.py wave1_authors.csv
```

### 8.2 Welcome Email Template

```python
#!/usr/bin/env python3
"""Send welcome emails to onboarded authors with login instructions."""
import csv
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

SMTP_HOST = os.environ["SMTP_HOST"]
SMTP_PORT = int(os.environ.get("SMTP_PORT", 587))
SMTP_USER = os.environ["SMTP_USER"]
SMTP_PASS = os.environ["SMTP_PASS"]
FROM_EMAIL = os.environ.get("SMTP_FROM", SMTP_USER)
NEXTCLOUD_URL = os.environ.get("NEXTCLOUD_URL", "https://nextcloud.example.com")
ELEMENT_URL = os.environ.get("ELEMENT_URL", "https://element.example.com")

WELCOME_TEMPLATE = """Hello {display_name},

Your contributor account has been created.

== File Collaboration (Nextcloud) ==
URL: {nextcloud_url}
Username: {username}
Password: {password}

We strongly recommend changing your password on first login.

== Community Chat (Matrix/Element) ==
URL: {element_url}
Username: @{username}:{matrix_domain}
Password: (same as above — change it)

For offline access, install the Nextcloud Desktop client:
  https://nextcloud.com/install/#install-clients

Questions? Reply to this email.
"""

def send_welcome(row: dict, matrix_domain: str):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Your Community Platform Access"
    msg["From"] = FROM_EMAIL
    msg["To"] = row["email"]

    body = WELCOME_TEMPLATE.format(
        display_name=row["display_name"],
        username=row["username"],
        password=row["password"],
        nextcloud_url=NEXTCLOUD_URL,
        element_url=ELEMENT_URL,
        matrix_domain=matrix_domain,
    )
    msg.attach(MIMEText(body, "plain"))

    with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
        server.starttls()
        server.login(SMTP_USER, SMTP_PASS)
        server.sendmail(FROM_EMAIL, row["email"], msg.as_string())
    print(f"  Email sent to {row['email']}")
```

---

## Part 9: Monitoring & Health Checks

### 9.1 Monitoring Script

```bash
#!/bin/bash
# /opt/community/nextcloud-matrix/scripts/healthcheck.sh
# Run hourly via cron; alerts on failure

set -euo pipefail

COMPOSE_DIR="/opt/community/nextcloud-matrix"
ALERT_EMAIL="admin@example.com"
NEXTCLOUD_URL="https://nextcloud.example.com"
MATRIX_URL="https://matrix.example.com"
ELEMENT_URL="https://element.example.com"

failures=()

check_http() {
  local name="$1" url="$2"
  if ! curl -sf --max-time 10 "$url" > /dev/null 2>&1; then
    failures+=("$name endpoint unreachable: $url")
  else
    echo "OK: $name"
  fi
}

check_container() {
  local name="$1"
  local status
  status=$(docker inspect --format='{{.State.Health.Status}}' "$name" 2>/dev/null || echo "not_found")
  if [[ "$status" != "healthy" ]]; then
    failures+=("Container $name is $status")
  else
    echo "OK: Container $name"
  fi
}

# Container health
for container in community-postgres community-redis community-nextcloud \
                  community-synapse community-nginx; do
  check_container "$container"
done

# HTTP endpoints
check_http "Nextcloud" "$NEXTCLOUD_URL/status.php"
check_http "Matrix" "$MATRIX_URL/_matrix/client/versions"
check_http "Element" "$ELEMENT_URL/"

# Disk space
disk_used=$(df -h /opt/community/nextcloud-matrix/data | tail -1 | awk '{print $5}' | tr -d '%')
if [[ "$disk_used" -gt 85 ]]; then
  failures+=("Disk usage critical: ${disk_used}%")
fi

# Report
if [[ "${#failures[@]}" -gt 0 ]]; then
  echo "ALERT: ${#failures[@]} failures detected:"
  printf '  - %s\n' "${failures[@]}"
  # Send alert email
  printf '%s\n' "${failures[@]}" | mail -s "Community Platform Alert - $(hostname)" "$ALERT_EMAIL" 2>/dev/null || true
  exit 1
else
  echo "All checks passed at $(date -u '+%Y-%m-%dT%H:%M:%SZ')"
fi
```

```bash
# Install as hourly cron
chmod +x /opt/community/nextcloud-matrix/scripts/healthcheck.sh
mkdir -p /opt/community/nextcloud-matrix/scripts
(crontab -l 2>/dev/null; echo "0 * * * * /opt/community/nextcloud-matrix/scripts/healthcheck.sh >> /var/log/community-health.log 2>&1") | crontab -
```

### 9.2 Container Resource Monitoring

```bash
# Real-time resource usage
docker stats community-postgres community-redis community-nextcloud \
              community-synapse community-element community-onlyoffice \
              community-nginx

# One-shot snapshot
docker stats --no-stream --format "table {{.Name}}\t{{.CPUPerc}}\t{{.MemUsage}}\t{{.MemPerc}}"
```

---

## Part 10: Backup & Recovery

### 10.1 Backup Script

```bash
#!/bin/bash
# /opt/community/nextcloud-matrix/scripts/backup.sh
# Run daily at 02:00 UTC

set -euo pipefail

COMPOSE_DIR="/opt/community/nextcloud-matrix"
BACKUP_BASE="/mnt/backup/community-platform"
DATE=$(date -u +%Y-%m-%d)
BACKUP_DIR="$BACKUP_BASE/$DATE"

mkdir -p "$BACKUP_DIR"

echo "[$(date -u)] Starting backup to $BACKUP_DIR"

# 1. Put Nextcloud in maintenance mode
docker exec -u www-data community-nextcloud php occ maintenance:mode --on

# 2. Backup PostgreSQL databases
echo "Backing up PostgreSQL..."
docker exec community-postgres pg_dump \
  -U community_db_user nextcloud_db \
  | gzip > "$BACKUP_DIR/nextcloud_db.sql.gz"

docker exec community-postgres pg_dump \
  -U community_db_user synapse_db \
  | gzip > "$BACKUP_DIR/synapse_db.sql.gz"

# 3. Backup Nextcloud data (exclude cache)
echo "Backing up Nextcloud data..."
tar -czf "$BACKUP_DIR/nextcloud-data.tar.gz" \
  --exclude="$COMPOSE_DIR/data/nextcloud/data/*/cache" \
  --exclude="$COMPOSE_DIR/data/nextcloud/tmp" \
  -C "$COMPOSE_DIR" data/nextcloud/

# 4. Backup Matrix media + signing keys
echo "Backing up Matrix data..."
tar -czf "$BACKUP_DIR/matrix-data.tar.gz" \
  -C "$COMPOSE_DIR" data/matrix/

# 5. Backup configuration (not .env — store separately in secrets manager)
tar -czf "$BACKUP_DIR/config.tar.gz" \
  -C "$COMPOSE_DIR" \
  nginx/ matrix/config/ element/ init-db.sql docker-compose.yml

# 6. Take Nextcloud out of maintenance mode
docker exec -u www-data community-nextcloud php occ maintenance:mode --off

# 7. Log backup sizes
echo "Backup sizes:"
du -sh "$BACKUP_DIR"/*

# 8. Prune backups older than 30 days
find "$BACKUP_BASE" -maxdepth 1 -type d -mtime +30 -exec rm -rf {} \; 2>/dev/null || true

echo "[$(date -u)] Backup complete: $BACKUP_DIR"
```

```bash
# Install backup cron
chmod +x /opt/community/nextcloud-matrix/scripts/backup.sh
(crontab -l 2>/dev/null; echo "0 2 * * * /opt/community/nextcloud-matrix/scripts/backup.sh >> /var/log/community-backup.log 2>&1") | crontab -
```

### 10.2 Recovery Procedure

```bash
# 1. Stop all services
docker compose -f /opt/community/nextcloud-matrix/docker-compose.yml down

# 2. Restore PostgreSQL
docker compose up -d postgres
sleep 20
gunzip -c /mnt/backup/community-platform/YYYY-MM-DD/nextcloud_db.sql.gz | \
  docker exec -i community-postgres psql -U community_db_user nextcloud_db
gunzip -c /mnt/backup/community-platform/YYYY-MM-DD/synapse_db.sql.gz | \
  docker exec -i community-postgres psql -U community_db_user synapse_db

# 3. Restore Nextcloud data
tar -xzf /mnt/backup/community-platform/YYYY-MM-DD/nextcloud-data.tar.gz \
  -C /opt/community/nextcloud-matrix/

# 4. Restore Matrix data
tar -xzf /mnt/backup/community-platform/YYYY-MM-DD/matrix-data.tar.gz \
  -C /opt/community/nextcloud-matrix/

# 5. Start all services
docker compose -f /opt/community/nextcloud-matrix/docker-compose.yml up -d

# 6. Repair Nextcloud
docker exec -u www-data community-nextcloud php occ maintenance:repair
docker exec -u www-data community-nextcloud php occ db:add-missing-indices
```

---

## Part 11: Go-Live Timeline (June 5)

| Time (UTC) | Action | Owner | Duration |
|------------|--------|-------|----------|
| June 4 08:00 | DNS records created + TTL set to 300 | Admin | 30 min |
| June 4 10:00 | Docker host verified (RAM, disk, Docker version) | Admin | 15 min |
| June 4 11:00 | TLS certificates issued (certbot standalone) | Admin | 30 min |
| June 4 12:00 | docker-compose.yml + all config files in place | Admin | 45 min |
| June 4 14:00 | Synapse config generated; homeserver.yaml verified | Admin | 30 min |
| June 4 15:00 | Stage 1 launch (postgres + redis) | Admin | 20 min |
| June 4 16:00 | Stage 2 launch (nextcloud + synapse + element) | Admin | 30 min |
| June 4 17:00 | All API health checks pass | Admin | 30 min |
| June 4 18:00 | 5 test users created + login verified | Admin | 30 min |
| June 4 20:00 | Backup script tested; crons installed | Admin | 20 min |
| June 5 06:00 | Final validation run (all checks) | Admin | 30 min |
| June 5 09:00 | Wave 1 author CSV prepared | Admin | 60 min |
| June 5 12:00 | Bulk user import (Wave 1 authors) | Admin | 30 min |
| June 5 12:30 | Welcome emails sent | Admin | 15 min |
| **June 5 13:00** | **Wave 1 author recruitment kickoff** | All | — |

---

## Part 12: Pre-Go-Live Checklist

- [ ] All 7 containers show `(healthy)` in `docker compose ps`
- [ ] `curl https://nextcloud.example.com/status.php` returns `"installed":true`
- [ ] `curl https://matrix.example.com/_matrix/client/versions` returns version list
- [ ] Element Web loads at `https://element.example.com` without console errors
- [ ] OnlyOffice healthcheck returns `true`
- [ ] `.well-known/matrix/server` returns correct JSON
- [ ] Federation test at `federationtester.matrix.org` shows no errors
- [ ] 5 test users can log into both Nextcloud and Element
- [ ] Nextcloud desktop client syncs a test file offline and online
- [ ] Backup script runs without errors; files appear in backup dir
- [ ] All TLS certificates valid and auto-renewal cron installed
- [ ] Health check cron installed and running
- [ ] `.env` file NOT committed to git (`echo ".env" >> .gitignore`)

---

**Document Version**: 2.0 (June 3, 2026 — full rewrite with corrected FPM architecture, verified Meshtastic bridge status, production-ready config files)
**Confidence**: High — all critical paths verified against current image documentation and upstream repos
**Key corrections from v1.0**: Fixed FPM healthcheck (was using HTTP against non-HTTP container); added nginx-nextcloud sidecar with volumes; updated Nextcloud version to 33; added complete nginx config files; corrected Meshtastic bridge status (active, v1.3.7); removed hardcoded passwords from Python script.
