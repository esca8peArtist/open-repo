# Discourse Deployment Playbook
## Phase 5 Platform B — Community Forum Setup Guide

**Status**: Phase 5 Wave 1 platform deployment (author recruitment June 5 13:00 UTC)  
**Target Environment**: Production (100-150 person community)  
**Estimated Deployment Time**: 2-3 hours  
**Success Criteria**: Discourse online + GitHub Pages integration + trust levels configured + test users created

---

## Executive Summary

**Platform B** provides a traditional forum experience with modern community governance features. Authors can:
- Create discussion threads organized by category
- Use trust-level-based self-governance (users earn moderation powers)
- Export discussions to GitHub Pages for permanent documentation
- Integrate with GitHub for SSO and contributor recognition

**Key Advantage**: Lightweight, fast deployments with built-in governance. No separate chat service required (unlike Platform A's Nextcloud + Matrix).

**Why This Configuration**:
- **Discourse**: Battle-tested forum software with excellent community moderation
- **PostgreSQL + Redis**: Standard backing services
- **GitHub Integration**: SSO login, contributor badges, automatic exports
- **Trust Levels 1-4**: Community-driven governance without staff overhead

**Trade-offs vs Platform A**:
- ✗ No offline document editing (forum posts only)
- ✓ Faster deployment (2h vs 4h)
- ✓ Simpler operations (fewer containers)
- ✓ Lower resource requirements

---

## Part 1: Pre-Flight Checklist

### Infrastructure Requirements

- [ ] **Docker Host**:
  - OS: Ubuntu 22.04 LTS or CentOS 8+
  - CPU: 2 cores minimum (4 cores for 150+ users)
  - RAM: 8 GB minimum (16 GB recommended)
  - Storage: 100 GB SSD
  - Network: Public IP address + reliable internet

- [ ] **Domains**:
  - [ ] `forum.example.com` → Docker host IP
  - [ ] `github.example.com` (optional, for OAuth redirect)
  - [ ] DNS TTL: 300 (5 minutes)

- [ ] **TLS Certificates**:
  - [ ] Email for Let's Encrypt ready
  - [ ] Ports 80 (HTTP) and 443 (HTTPS) open

- [ ] **GitHub Integration**:
  - [ ] GitHub organization created
  - [ ] GitHub OAuth app registered (see Section 3.3)
  - [ ] GitHub Personal Access Token generated (for exports)

- [ ] **Email Delivery**:
  - [ ] SMTP server configured (SendGrid, AWS SES, or own)
  - [ ] Test email address ready

- [ ] **Backups**:
  - [ ] S3 bucket or external storage ready
  - [ ] Daily backup schedule planned

---

## Part 2: Docker Environment Setup

### 2.1 Installation

```bash
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group
sudo usermod -aG docker $USER
newgrp docker

# Verify
docker --version && docker compose --version
```

### 2.2 Firewall

```bash
# Ubuntu/Debian
sudo ufw allow 22/tcp
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp
sudo ufw enable

# CentOS/RHEL
sudo firewall-cmd --permanent --add-service=http
sudo firewall-cmd --permanent --add-service=https
sudo firewall-cmd --reload
```

### 2.3 Directory Structure

```bash
mkdir -p /home/docker-deploy/discourse
cd /home/docker-deploy/discourse

mkdir -p data/{postgres,redis,uploads,backups}
mkdir -p nginx/{conf.d,ssl}

sudo chown -R $USER:$USER /home/docker-deploy/discourse
chmod 700 data/

# Create .env
touch .env
chmod 600 .env
```

---

## Part 3: Configuration Files

### 3.1 Environment Variables (.env)

```bash
cat > .env << 'EOF'
# === Discourse Configuration ===
DISCOURSE_HOSTNAME=forum.example.com
DISCOURSE_DEVELOPER_EMAILS=admin@example.com
DISCOURSE_REDIS_HOST=redis
DISCOURSE_DB_HOST=postgres
DISCOURSE_DB_NAME=discourse
DISCOURSE_DB_USERNAME=discourse_user
DISCOURSE_DB_PASSWORD=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE

# === GitHub OAuth ===
GITHUB_CLIENT_ID=YOUR_GITHUB_CLIENT_ID
GITHUB_CLIENT_SECRET=YOUR_GITHUB_CLIENT_SECRET
GITHUB_ORGANIZATION=your-org  # For automatic invites

# === Email (SMTP) ===
DISCOURSE_SMTP_ADDRESS=smtp.sendgrid.net
DISCOURSE_SMTP_PORT=587
DISCOURSE_SMTP_USERNAME=apikey
DISCOURSE_SMTP_PASSWORD=SG.YOUR_SENDGRID_API_KEY
DISCOURSE_SMTP_ENABLE_START_TLS=true
DISCOURSE_NOTIFICATION_EMAIL=noreply@example.com

# === Redis ===
REDIS_PASSWORD=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE

# === PostgreSQL ===
POSTGRES_PASSWORD=GENERATE_RANDOM_32_CHAR_PASSWORD_HERE

# === Let's Encrypt ===
LETSENCRYPT_EMAIL=letsencrypt@example.com
ACME_CA_URI=https://acme-v02.api.letsencrypt.org/directory

# === General ===
TIMEZONE=UTC
RAILS_ENV=production
DISCOURSE_SMTP_AUTHENTICATION=login
EOF

# Generate secure passwords
python3 -c "import secrets; print(secrets.token_urlsafe(24))"
```

### 3.2 docker-compose.yml

```yaml
version: '3.9'

services:
  postgres:
    image: postgres:16-alpine
    container_name: discourse-postgres
    restart: unless-stopped
    environment:
      POSTGRES_USER: discourse_user
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
      POSTGRES_DB: discourse
      POSTGRES_INITDB_ARGS: "--encoding=UTF8"
    volumes:
      - ./data/postgres:/var/lib/postgresql/data
    networks:
      - backend
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U discourse_user"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 2G

  redis:
    image: redis:7-alpine
    container_name: discourse-redis
    restart: unless-stopped
    command: redis-server --requirepass ${REDIS_PASSWORD} --maxmemory 2gb --maxmemory-policy allkeys-lru
    volumes:
      - ./data/redis:/data
    networks:
      - backend
    healthcheck:
      test: ["CMD", "redis-cli", "--raw", "incr", "ping"]
      interval: 10s
      timeout: 5s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 2G

  discourse:
    image: discourse/discourse:latest
    container_name: discourse-app
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      DISCOURSE_HOSTNAME: ${DISCOURSE_HOSTNAME}
      DISCOURSE_DEVELOPER_EMAILS: ${DISCOURSE_DEVELOPER_EMAILS}
      DISCOURSE_REDIS_HOST: redis
      DISCOURSE_REDIS_PASSWORD: ${REDIS_PASSWORD}
      DISCOURSE_DB_HOST: postgres
      DISCOURSE_DB_NAME: ${DISCOURSE_DB_NAME}
      DISCOURSE_DB_USERNAME: ${DISCOURSE_DB_USERNAME}
      DISCOURSE_DB_PASSWORD: ${DISCOURSE_DB_PASSWORD}
      DISCOURSE_SMTP_ADDRESS: ${DISCOURSE_SMTP_ADDRESS}
      DISCOURSE_SMTP_PORT: ${DISCOURSE_SMTP_PORT}
      DISCOURSE_SMTP_USERNAME: ${DISCOURSE_SMTP_USERNAME}
      DISCOURSE_SMTP_PASSWORD: ${DISCOURSE_SMTP_PASSWORD}
      DISCOURSE_SMTP_ENABLE_START_TLS: ${DISCOURSE_SMTP_ENABLE_START_TLS}
      DISCOURSE_NOTIFICATION_EMAIL: ${DISCOURSE_NOTIFICATION_EMAIL}
      DISCOURSE_SMTP_AUTHENTICATION: ${DISCOURSE_SMTP_AUTHENTICATION}
      RAILS_ENV: production
      UNICORN_WORKERS: 4
      UNICORN_TIMEOUT: 30
      LANG: en_US.UTF-8
    volumes:
      - ./data/uploads:/var/www/discourse/public/uploads
      - ./data/backups:/var/www/discourse/public/backups
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:3000/"]
      interval: 30s
      timeout: 10s
      retries: 5
    deploy:
      resources:
        limits:
          cpus: '2'
          memory: 4G
    ports:
      - "127.0.0.1:3000:3000"

  sidekiq:
    image: discourse/discourse:latest
    container_name: discourse-sidekiq
    restart: unless-stopped
    depends_on:
      postgres:
        condition: service_healthy
      redis:
        condition: service_healthy
    environment:
      DISCOURSE_REDIS_HOST: redis
      DISCOURSE_REDIS_PASSWORD: ${REDIS_PASSWORD}
      DISCOURSE_DB_HOST: postgres
      DISCOURSE_DB_NAME: ${DISCOURSE_DB_NAME}
      DISCOURSE_DB_USERNAME: ${DISCOURSE_DB_USERNAME}
      DISCOURSE_DB_PASSWORD: ${DISCOURSE_DB_PASSWORD}
      RAILS_ENV: production
      LANG: en_US.UTF-8
    volumes:
      - ./data/uploads:/var/www/discourse/public/uploads
      - ./data/backups:/var/www/discourse/public/backups
    networks:
      - backend
    command: bundle exec sidekiq -e production -c 4 -r /var/www/discourse
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 2G

  nginx:
    image: nginx:latest-alpine
    container_name: discourse-nginx
    restart: unless-stopped
    depends_on:
      - discourse
    volumes:
      - ./nginx/nginx.conf:/etc/nginx/nginx.conf:ro
      - ./nginx/conf.d:/etc/nginx/conf.d:ro
      - ./data/letsencrypt:/etc/letsencrypt
    ports:
      - "127.0.0.1:80:80"
      - "127.0.0.1:443:443"
    networks:
      - backend
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost/"]
      interval: 30s
      timeout: 10s
      retries: 3
    deploy:
      resources:
        limits:
          cpus: '1'
          memory: 1G

  certbot:
    image: certbot/certbot:latest
    container_name: discourse-certbot
    restart: unless-stopped
    volumes:
      - ./data/letsencrypt:/etc/letsencrypt
    entrypoint: /bin/sh -c 'trap exit TERM; while :; do certbot renew --webroot -w /etc/letsencrypt/webroot --quiet; sleep 12h & wait $${!}; done'
    networks:
      - backend

networks:
  backend:
    driver: bridge
    ipam:
      config:
        - subnet: 172.23.0.0/16

volumes:
  postgres_data:
    driver: local
  redis_data:
    driver: local
```

### 3.3 nginx Configuration (nginx/nginx.conf)

```nginx
user nginx;
worker_processes auto;
error_log /var/log/nginx/error.log warn;
pid /var/run/nginx.pid;

events {
    worker_connections 1024;
}

http {
    include /etc/nginx/mime.types;
    default_type application/octet-stream;

    log_format main '$remote_addr - $remote_user [$time_local] "$request" '
                    '$status $body_bytes_sent "$http_referer" '
                    '"$http_user_agent"';

    access_log /var/log/nginx/access.log main;

    sendfile on;
    tcp_nopush on;
    tcp_nodelay on;
    keepalive_timeout 65;
    types_hash_max_size 2048;
    client_max_body_size 50M;

    gzip on;
    gzip_vary on;
    gzip_proxied any;
    gzip_comp_level 6;
    gzip_types text/plain text/css text/xml text/javascript 
               application/json application/javascript application/xml+rss;

    add_header X-Frame-Options "SAMEORIGIN" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-XSS-Protection "1; mode=block" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    include /etc/nginx/conf.d/*.conf;
}
```

### 3.4 nginx Virtual Host (nginx/conf.d/discourse.conf)

```nginx
server {
    listen 80 default_server;
    listen [::]:80 default_server;
    server_name _;
    
    location /.well-known/acme-challenge/ {
        root /etc/letsencrypt/webroot;
    }
    
    location / {
        return 301 https://$host$request_uri;
    }
}

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name forum.example.com;

    ssl_certificate /etc/letsencrypt/live/forum.example.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/forum.example.com/privkey.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers HIGH:!aNULL:!MD5;
    ssl_prefer_server_ciphers on;

    location / {
        proxy_pass http://discourse:3000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_buffering off;
        proxy_request_buffering off;
    }

    client_max_body_size 50M;
}
```

---

## Part 4: Deployment Execution

### 4.1 Pre-Deployment Checks

```bash
cd /home/docker-deploy/discourse

# Verify configuration
grep "GENERATE_RANDOM" .env  # Should return empty

# Test docker-compose syntax
docker compose config > /dev/null

# Verify directories
ls -la data/
```

### 4.2 Generate TLS Certificates

```bash
docker run -it --rm -p 80:80 -p 443:443 \
  -v ./data/letsencrypt:/etc/letsencrypt \
  certbot/certbot certonly \
  --standalone \
  --agree-tos \
  --email letsencrypt@example.com \
  -d forum.example.com

# Verify
ls -la ./data/letsencrypt/live/
```

### 4.3 Launch Services

```bash
docker compose up -d
sleep 30
docker compose ps
docker compose logs -f --tail=50
```

### 4.4 Initialize Database & Create Admin

```bash
docker compose exec discourse rake db:migrate
docker compose exec discourse rake admin:create
# Follow prompts for admin email and password
```

### 4.5 Configure GitHub OAuth

1. Go to GitHub Settings → Developer settings → OAuth Apps
2. Create new OAuth app with:
   - Homepage URL: https://forum.example.com
   - Authorization callback: https://forum.example.com/auth/github/callback
3. Copy Client ID and Secret

```bash
docker compose exec discourse bash
cd /var/www/discourse
bundle exec rails c

SiteSetting.github_client_id = "YOUR_CLIENT_ID"
SiteSetting.github_client_secret = "YOUR_CLIENT_SECRET"
SiteSetting.github_enabled = true
SiteSetting.github_auto_create_accounts = true

exit
```

---

## Part 5: GitHub Pages Integration

Export Discourse topics to Jekyll markdown via Python script:

```python
#!/usr/bin/env python3
import requests
import json
import os
from datetime import datetime
import yaml

DISCOURSE_URL = "https://forum.example.com"
DISCOURSE_API_KEY = "YOUR_DISCOURSE_API_KEY"

class DiscourseExporter:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key
        self.headers = {
            'Api-Key': api_key,
            'Api-Username': 'system'
        }
    
    def get_categories(self):
        url = f"{self.base_url}/categories.json"
        response = requests.get(url, headers=self.headers)
        return response.json()['category_list']['categories']
    
    def get_topics(self, category_id, limit=100):
        url = f"{self.base_url}/c/{category_id}.json?limit={limit}"
        response = requests.get(url, headers=self.headers)
        return response.json()['topic_list']['topics']
    
    def get_topic_details(self, topic_id):
        url = f"{self.base_url}/t/{topic_id}.json"
        response = requests.get(url, headers=self.headers)
        return response.json()
    
    def export_topic_to_markdown(self, topic):
        details = self.get_topic_details(topic['id'])
        
        frontmatter = {
            'title': topic['title'],
            'date': topic['created_at'],
            'category': topic['category_name'],
            'author': topic['creator_name'],
            'discourse_url': f"{self.base_url}/t/{topic['slug']}/{topic['id']}",
            'tags': topic.get('tags', [])
        }
        
        posts_markdown = []
        for post in details['post_stream']['posts']:
            posts_markdown.append(f"### {post['username']} ({post['created_at']})\n\n{post['cooked']}\n\n---\n")
        
        content = f"""---
{yaml.dump(frontmatter)}---

# {topic['title']}

**Category**: {topic['category_name']}  
**Original**: [{topic['slug']}]({self.base_url}/t/{topic['slug']}/{topic['id']})

## Discussion

{''.join(posts_markdown)}

[View on Discourse]({self.base_url}/t/{topic['slug']}/{topic['id']})
"""
        return content
    
    def export_all_topics(self, output_dir="_posts"):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        categories = self.get_categories()
        
        for category in categories:
            print(f"Exporting category: {category['name']}")
            topics = self.get_topics(category['id'])
            
            for topic in topics:
                try:
                    markdown = self.export_topic_to_markdown(topic)
                    filename = f"{topic['created_at'][:10]}-{topic['slug'][:50]}.md"
                    filepath = os.path.join(output_dir, filename)
                    
                    with open(filepath, 'w') as f:
                        f.write(markdown)
                    
                    print(f"  ✓ {filename}")
                except Exception as e:
                    print(f"  ✗ Error exporting {topic['id']}: {e}")

def main():
    exporter = DiscourseExporter(DISCOURSE_URL, DISCOURSE_API_KEY)
    exporter.export_all_topics()
    print("\nExport complete.")

if __name__ == '__main__':
    main()
```

---

## Part 6: Trust Levels & Self-Governance

Configure via Admin → Trust Levels:

- **TL 0** (New Users): View topics, create 3 posts/day
- **TL 1** (Basic): Auto after 1 day + 10 posts, reply + upload
- **TL 2** (Members): Auto after 15 days + 50 posts, create topics + moderate
- **TL 3** (Regulars): Auto after 50 days + 200 posts, approve flagged content
- **TL 4** (Leaders): Manual only, full moderation + category management

Enable auto-promotion in Admin → Settings → Trust Levels.

---

## Part 7: REST API Automation

### User Import (Ruby)

```ruby
#!/usr/bin/env ruby
require 'net/http'
require 'json'
require 'csv'

DISCOURSE_URL = "https://forum.example.com"
API_KEY = ENV['DISCOURSE_API_KEY']

class DiscourseAPI
  def initialize(url, api_key)
    @url = url
    @api_key = api_key
  end
  
  def create_user(email, username, name, password)
    uri = URI("#{@url}/users.json")
    http = Net::HTTP.new(uri.host, uri.port)
    http.use_ssl = true
    
    request = Net::HTTP::Post.new(uri)
    request['Api-Key'] = @api_key
    request['Api-Username'] = 'system'
    request['Content-Type'] = 'application/json'
    request.body = {
      email: email,
      username: username,
      name: name,
      password: password,
      active: true
    }.to_json
    
    response = http.request(request)
    
    if response.code == '200'
      puts "✓ User created: #{username}"
      return JSON.parse(response.body)['user']['id']
    else
      puts "✗ User creation failed: #{username}"
      return nil
    end
  end
end

CSV.foreach(ARGV[0], headers: true) do |row|
  api = DiscourseAPI.new(DISCOURSE_URL, API_KEY)
  api.create_user(row['email'], row['username'], row['name'], row['password'])
end
```

---

## Part 8: Post-Deployment Verification

```bash
# Test Discourse API
curl -s https://forum.example.com/about.json | jq .

# Verify email (Admin → Email → Send Test Email)

# Verify GitHub OAuth works (Login button should appear)
```

---

## Part 9: Backup & Recovery

```bash
#!/bin/bash
# Daily backup script

BACKUP_DIR="/mnt/backup/discourse-$(date +%Y-%m-%d)"
mkdir -p "$BACKUP_DIR"

# Create Discourse backup
docker compose exec discourse rake 'backup:create[skip_uploads]'

# Copy backups
cp -v /home/docker-deploy/discourse/data/backups/* "$BACKUP_DIR/"

# Clean old backups (30 days)
find /mnt/backup -type f -mtime +30 -delete

echo "✓ Backup complete: $BACKUP_DIR"
```

---

## Part 10: Success Criteria & Go-Live

**Pre-Go-Live**:
- [ ] Discourse login works
- [ ] 5+ categories created
- [ ] GitHub OAuth configured
- [ ] Email notifications working
- [ ] 10+ test users created
- [ ] Backup script runs

**Go-Live Timeline**:
- June 5, 06:00 UTC: Final validation (15 min)
- June 5, 12:00 UTC: Publish forum URL
- June 5, 13:00 UTC: Author recruitment begins

---

## Part 11: Platform Comparison Summary

| Feature | Platform A (Nextcloud+Matrix) | Platform B (Discourse) |
|---------|-------------------------------|----------------------|
| **Setup Time** | 4-6 hours | 2-3 hours |
| **Document Editing** | Offline-first | Web-only |
| **Chat** | Matrix (encrypted) | Thread-based |
| **File Sync** | WebDAV | Attachments |
| **Self-Governance** | Manual rooms | Auto trust levels |
| **RAM Required** | 16 GB | 8 GB |
| **Scalability** | 100-200 users | 500+ users |
| **Go-Live Confidence** | 9.5/10 | 8.0/10 |

---

**Document Version**: 1.0 (June 3, 2026)  
**Status**: Ready for Production Deployment

