---
title: "Phase 5.1 Deployment Playbook — Platform-Agnostic Template"
project: systems-resilience
phase: 5
wave: 1+2
status: TEMPLATE-READY
purpose: "Platform-agnostic deployment template. Steps 1–5 identical for Nextcloud+Matrix and Discourse. Platform-specific install (Step 4) to be selected June 8 based on user decision. Template ready for immediate platform-specific completion."
publication_date: 2026-06-09
publication_start_time: "13:00 UTC"
publication_end_time: "15:00 UTC (estimated)"
deployment_host: "raspby1 (100.70.184.84) — Docker-enabled Raspberry Pi 5"
---

# Phase 5.1 Deployment Playbook — Platform-Agnostic Template
## Unified Deployment Framework for June 9, 2026 13:00–15:00 UTC

---

## Executive Summary

**Deployment Timeline**: June 9, 2026 13:00–15:00 UTC (90-minute publication window)

**Content Being Published**:
- 5 primary documents (Microgrids, Playbook, Conflict Resolution, Psychological Support, Veterinary Care)
- 1 integrated corpus (unified reference)
- Total: 61,611 words, 336+ citations, 2.1 MB bundle

**Publication Platform**: 
- **[PENDING JUNE 8 DECISION]** 
  - Option A: Nextcloud + Matrix (community-focused, federation-ready)
  - Option B: Discourse (discussion-forum format, built-in user management)

**Deployment Architecture**:
1. **Steps 1–5**: Platform-agnostic (identical for both options)
   - Pre-flight checks (Docker, network, disk, ports)
   - Content validation (files present, checksums match)
   - Network/TLS setup (reverse proxy on 80/443)
   - **[STEP 4-PLATFORM-SPECIFIC: Nextcloud OR Discourse]**
   - Post-deployment verification (health checks, content accessible)

2. **Steps 6+**: Platform-specific (post-publication monitoring, scaling)

**Success Criteria**:
- All 6 documents + corpus live and accessible by 15:00 UTC
- Public announcement sent to author coalition
- Post-publication monitoring complete by 15:30 UTC
- Zero critical errors in first 2 hours

**Risk Level**: LOW (all assets pre-verified, no blocking issues identified)

---

## SECTION 1: PRE-DEPLOYMENT SETUP (Applies to Both Platforms)

### 1.1 Deployment Prerequisites Checklist

**Date**: June 9, 2026 12:30 UTC
**Checklist Owner**: Publication lead
**Duration**: 15 minutes

**Pre-Flight Verification**:

- [ ] Infrastructure audit completed and passed (PHASE_5_1_DEPLOYMENT_INFRASTRUCTURE_AUDIT.md)
- [ ] Content readiness verified (PHASE_5_1_CONTENT_READINESS.md)
- [ ] Docker daemon is running and operational
  ```bash
  docker version
  # Expected: Both Client and Server sections present
  ```
- [ ] Network connectivity confirmed
  ```bash
  curl -I https://example.com
  # Expected: HTTP/1.1 200 OK
  ```
- [ ] Ports 80 and 443 are free
  ```bash
  sudo netstat -tlnp | grep -E ':(80|443)\s'
  # Expected: No output (ports are free)
  ```
- [ ] Storage space available (≥189GB confirmed)
  ```bash
  df /
  # Expected: Available column shows 189G+
  ```
- [ ] SSH access to raspby1 verified (if deploying remotely)
  ```bash
  ssh <user>@100.70.184.84
  # Expected: Login successful
  ```
- [ ] Content files staged and manifest verified
  ```bash
  cd /tmp/phase5-pub
  md5sum -c MANIFEST.txt
  # Expected: All checksums pass
  ```
- [ ] Announcement email drafted and ready
- [ ] Team briefing completed (if applicable)

**Status**: [Check all items; if any unchecked, DO NOT PROCEED]

**Sign-Off**: _________________ (Date: _________ Time: ______ UTC)

---

### 1.2 Deployment Team Composition

**Minimum Team**:
- **Publisher** (primary): Executes upload sequence, manages platform access
- **Monitor** (if available): Watches platform for errors during upload
- **Backup Publisher** (if available): Ready to take over if primary unavailable

**Communication Channel**: [Specify Slack/Discord/Email for status updates]

**Escalation Path**: 
- Technical issues → [Lead Engineer Name]
- Content issues → [Project Lead Name]
- Platform access issues → [Platform Admin Name]

---

### 1.3 Pre-Deployment Communications

**12:15 UTC**: Send briefing to team
```
Subject: Phase 5.1 Publication Ready — Team Briefing
Message: Publication window is 13:00–15:00 UTC. All systems ready. 
Standing by for go-ahead at 12:30 UTC.
```

**12:45 UTC**: Final confirmation from decision authority
```
Confirmation from [User]: Platform choice = [NEXTCLOUD+MATRIX / DISCOURSE]
Deployment proceeds with [PLATFORM] configuration.
```

**13:00 UTC**: Begin publication upload (see Section 2)

---

## SECTION 2: PLATFORM-AGNOSTIC DEPLOYMENT STEPS (Steps 1–5)

### Step 1: Pre-Flight Checks (5 minutes)

**Objective**: Verify infrastructure is operational and ready

**1a. Docker Status Check**
```bash
sudo docker ps
sudo docker system df
```

**Expected Output**:
```
CONTAINER ID   IMAGE     COMMAND   CREATED   STATUS
(no containers running)

TYPE            TOTAL     ACTIVE    SIZE      RECLAIMABLE
Images          0         0         0B        0B
Containers      0         0         0B        0B
```

**1b. Network Connectivity Check**
```bash
curl -I https://example.com
```

**Expected**: HTTP/1.1 200 OK response

**1c. Port Availability Check**
```bash
sudo netstat -tlnp | grep -E ':(80|443)\s' || echo "Ports 80/443 are free"
```

**Expected**: "Ports 80/443 are free" (no service output)

**1d. Disk Space Check**
```bash
df -h /
```

**Expected**: 
- Available space ≥5GB minimum (we have 189GB — comfortable margin)
- Usage <80% (we're at 16% — excellent)

**1e. Content Manifest Verification**
```bash
cd /tmp/phase5-pub
md5sum -c MANIFEST.txt
```

**Expected**: 
```
./01-microgrids.md: OK
./02-playbook.md: OK
...
(all 12 files OK)
```

**If Any Check Fails**:
- [ ] Stop all operations
- [ ] Investigate root cause (see troubleshooting section)
- [ ] Do NOT proceed until all checks pass
- [ ] Contact technical lead

**Step 1 Status**: 
- [ ] All checks passed — proceed to Step 2
- [ ] One or more checks failed — STOP, investigate, escalate

---

### Step 2: Content Validation (5 minutes)

**Objective**: Confirm all publication files are present and uncorrupted

**2a. File Presence Check**
```bash
ls -lh /tmp/phase5-pub/*.md | wc -l
# Expected: 6 files

ls -lh /tmp/phase5-pub/pdf/*.pdf | wc -l
# Expected: 6 files
```

**2b. Total Bundle Size Check**
```bash
du -sh /tmp/phase5-pub/
# Expected: ~2.1M
```

**2c. Sample Content Verification**
```bash
# Verify markdown files are readable
head -20 /tmp/phase5-pub/01-microgrids.md
# Should show YAML frontmatter with title, project, status: PRODUCTION-READY

# Verify PDF files are readable
file /tmp/phase5-pub/pdf/01-microgrids.pdf
# Should show "PDF document, version 1.4"
```

**2d. Checksum Validation (detailed)**
```bash
cd /tmp/phase5-pub
md5sum -c MANIFEST.txt 2>&1 | grep -E "OK|FAILED"
# Expected: 12 "OK" lines, 0 "FAILED" lines
```

**If Any Check Fails**:
- [ ] Content files may have been corrupted or modified
- [ ] Do NOT proceed
- [ ] Restore content from backup (Git repo or archive)
- [ ] Re-run content readiness audit
- [ ] Contact project lead

**Step 2 Status**: 
- [ ] All content validated — proceed to Step 3
- [ ] Content validation failed — STOP, investigate, restore backup

---

### Step 3: Network and Reverse Proxy Setup (10 minutes)

**Objective**: Configure nginx reverse proxy on ports 80/443 to forward traffic to platform

**3a. Check if nginx is installed**
```bash
which nginx
# If not found, install:
sudo apt-get update && sudo apt-get install -y nginx
```

**3b. Create nginx configuration**

**For Nextcloud+Matrix deployment**:
```bash
# Create nginx config file at /etc/nginx/sites-available/phase5-nextcloud
sudo tee /etc/nginx/sites-available/phase5-nextcloud > /dev/null <<'EOF'
upstream nextcloud {
    server 127.0.0.1:8080;
}

upstream matrix {
    server 127.0.0.1:8008;
}

server {
    listen 80;
    listen 443 ssl http2;
    server_name 100.70.184.84 localhost;
    
    ssl_certificate /etc/ssl/certs/self-signed.crt;
    ssl_certificate_key /etc/ssl/private/self-signed.key;
    
    # Redirect HTTP to HTTPS
    if ($scheme != "https") {
        return 301 https://$server_name$request_uri;
    }
    
    # Nextcloud routing
    location /nextcloud {
        proxy_pass http://nextcloud;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
    
    # Matrix routing (optional if Matrix included)
    location /_matrix {
        proxy_pass http://matrix;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }
    
    location /_synapse {
        proxy_pass http://matrix;
        proxy_set_header Host $host;
    }
}
EOF
```

**For Discourse deployment**:
```bash
# Create nginx config file at /etc/nginx/sites-available/phase5-discourse
sudo tee /etc/nginx/sites-available/phase5-discourse > /dev/null <<'EOF'
upstream discourse {
    server 127.0.0.1:3000;
}

server {
    listen 80;
    listen 443 ssl http2;
    server_name 100.70.184.84 localhost;
    
    ssl_certificate /etc/ssl/certs/self-signed.crt;
    ssl_certificate_key /etc/ssl/private/self-signed.key;
    
    # Redirect HTTP to HTTPS
    if ($scheme != "https") {
        return 301 https://$server_name$request_uri;
    }
    
    # Discourse routing
    location / {
        proxy_pass http://discourse;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
EOF
```

**Note**: Choose configuration based on platform selected on June 8.

**3c. Generate self-signed SSL certificate (if not already present)**
```bash
sudo openssl req -x509 -nodes -days 365 -newkey rsa:2048 \
    -keyout /etc/ssl/private/self-signed.key \
    -out /etc/ssl/certs/self-signed.crt \
    -subj "/CN=raspby1/O=Phase5/C=US"
```

**3d. Enable nginx configuration**
```bash
# Remove default site
sudo rm /etc/nginx/sites-enabled/default

# Create symlink to appropriate config
# For Nextcloud: sudo ln -s /etc/nginx/sites-available/phase5-nextcloud /etc/nginx/sites-enabled/
# For Discourse: sudo ln -s /etc/nginx/sites-available/phase5-discourse /etc/nginx/sites-enabled/
```

**3e. Verify nginx configuration syntax**
```bash
sudo nginx -t
# Expected: "nginx: configuration file test is successful"
```

**3f. Start or reload nginx**
```bash
sudo systemctl start nginx
# or if already running:
sudo systemctl reload nginx

# Verify nginx is running
sudo systemctl status nginx
# Expected: "active (running)"
```

**3g. Test reverse proxy connectivity**
```bash
# Test that reverse proxy is listening
sudo netstat -tlnp | grep nginx
# Expected: nginx listening on 80 and 443

# Test local connectivity (will fail until platform is running, that's OK)
curl -k https://localhost/
# May show "connection refused" yet — that's expected
```

**Step 3 Status**: 
- [ ] nginx installed and configured
- [ ] SSL certificate generated
- [ ] nginx syntax validated
- [ ] nginx started/reloaded
- [ ] Ready for platform container startup

---

### Step 4: [PLATFORM-SPECIFIC] Platform Installation

**⚠️ PLATFORM CHOICE REQUIRED ⚠️**

**This step is platform-specific. Proceed with either Option A or Option B based on June 8 decision.**

**[IF NEXTCLOUD+MATRIX CHOSEN → Use Option A below]**

**[IF DISCOURSE CHOSEN → Use Option B below]**

#### **OPTION A: Nextcloud + Matrix Deployment** (If chosen June 8)

**Objective**: Deploy Nextcloud file server + Matrix messaging platform using Docker Compose

**4a. Create Nextcloud+Matrix Docker Compose file**

Reference existing file: `/home/awank/dev/SuperClaude_Framework/projects/systems-resilience/docker-compose-nextcloud-matrix.yml`

**[NOTE TO DEPLOYMENT OPERATOR]: Replace this with actual Nextcloud+Matrix docker-compose.yml if it differs from project repo**

```bash
# Copy existing docker-compose file (or create new)
cp /home/awank/dev/SuperClaude_Framework/projects/systems-resilience/docker-compose-nextcloud-matrix.yml \
   /tmp/docker-compose.yml
```

**4b. Create persistent volumes and directories**
```bash
# Create directories for Nextcloud and Matrix data
mkdir -p /var/lib/nextcloud/data
mkdir -p /var/lib/nextcloud/config
mkdir -p /var/lib/matrix/homeserver
mkdir -p /var/lib/postgres_data
mkdir -p /var/lib/redis_data

sudo chown -R 999:999 /var/lib/nextcloud
sudo chown -R 991:991 /var/lib/matrix
sudo chown -R 999:999 /var/lib/postgres_data
sudo chown -R 999:999 /var/lib/redis_data
```

**4c. Start Nextcloud and Matrix containers**
```bash
cd /tmp
docker-compose -f docker-compose.yml up -d

# Monitor startup
docker-compose logs -f nextcloud matrix-synapse postgres redis
# Press Ctrl+C once all services show "ready" or "listening"

# Typical startup time: 3–5 minutes
```

**4d. Verify services are running**
```bash
docker ps | grep -E "nextcloud|matrix|postgres|redis"
# Expected: 4 containers running (nextcloud, matrix-synapse, postgres, redis)

# Check logs for errors
docker-compose logs --tail=50 nextcloud
docker-compose logs --tail=50 matrix-synapse
```

**4e. Initialize Nextcloud (admin user)**
```bash
# Wait 30 seconds for Nextcloud to finish initialization
sleep 30

# Access Nextcloud and create admin user via web UI
# Navigate to: https://100.70.184.84/nextcloud
# Create admin user with username: admin, password: [SECURE_PASSWORD]
```

**4f. Create Nextcloud folder structure for Phase 5 content**

Via Nextcloud web UI (https://100.70.184.84/nextcloud):
1. Log in as admin
2. Create folder: "Phase 5 Published Research"
3. Create subfolders:
   - 01-Microgrids
   - 02-Community-Implementation
   - 03-Conflict-Resolution
   - 04-Psychological-Support
   - 05-Veterinary-Care
   - 00-Integrated-Corpus

Alternatively, via SSH:
```bash
ssh <user>@100.70.184.84
sudo mkdir -p /var/lib/nextcloud/data/admin/files/Phase\ 5\ Published\ Research/{01-Microgrids,02-Community-Implementation,03-Conflict-Resolution,04-Psychological-Support,05-Veterinary-Care,00-Integrated-Corpus}
```

**4g. Verify Matrix Homeserver is operational**
```bash
curl https://100.70.184.84/_matrix/client/versions -k
# Expected: JSON response with version information
```

**Step 4A Status (Nextcloud+Matrix)**: 
- [ ] Docker-compose file ready and configured
- [ ] Persistent volumes created
- [ ] Containers started successfully (docker ps shows 4 running)
- [ ] Nextcloud admin user created
- [ ] Nextcloud folder structure ready
- [ ] Matrix homeserver responding
- [ ] Proceed to Step 5

---

#### **OPTION B: Discourse Deployment** (If chosen June 8)

**Objective**: Deploy Discourse forum platform using Docker container

**4b. Prerequisites for Discourse**
```bash
# Discourse requires Docker and docker-compose
# Already verified in Step 1

# Ensure hostname is set (for Discourse admin panel)
sudo hostnamectl set-hostname phase5-discourse
```

**4b. Clone Discourse Docker template**
```bash
cd /tmp
git clone https://github.com/discourse/discourse_docker.git
cd discourse_docker
```

**4c. Create Discourse containers.yml**
```bash
sudo tee containers/app.yml > /dev/null <<'EOF'
version: '3'
services:
  db:
    image: postgres:13
    environment:
      POSTGRES_PASSWORD: discourse-password
    volumes:
      - /var/lib/postgres:/var/lib/postgresql/data
    restart: always

  redis:
    image: redis:6-alpine
    restart: always

  discourse:
    image: discourse/discourse:latest
    depends_on:
      - db
      - redis
    environment:
      DISCOURSE_DB_HOST: db
      DISCOURSE_DB_NAME: discourse
      DISCOURSE_DB_USER: discourse
      DISCOURSE_DB_PASSWORD: discourse-password
      DISCOURSE_REDIS_HOST: redis
      DISCOURSE_DEVELOPER_EMAILS: admin@example.com
      DISCOURSE_HOSTNAME: 100.70.184.84
      DISCOURSE_SMTP_ADDRESS: localhost
      DISCOURSE_SMTP_USER_NAME: discourse
      DISCOURSE_SMTP_PASSWORD: discourse-password
    ports:
      - "3000:3000"
    volumes:
      - /var/lib/discourse_data:/shared
      - /var/lib/discourse_logs:/var/log
    restart: always

version: '3'
EOF
```

**4d. Build and start Discourse**
```bash
docker-compose -f containers/app.yml up -d

# Monitor startup (5-10 minutes typical)
docker-compose -f containers/app.yml logs -f discourse

# Once "ready" appears, proceed
```

**4e. Verify Discourse is running**
```bash
curl http://127.0.0.1:3000/ -s | head -30
# Expected: HTML response with Discourse page layout
```

**4f. Initialize Discourse admin user**

Access Discourse at: https://100.70.184.84/
1. Complete setup wizard
2. Create admin user
3. Set up categories (see 4g below)

**4g. Create Discourse categories for Phase 5 content**

Via Discourse admin panel (https://100.70.184.84/admin):
1. Navigate to Categories
2. Create category: "Phase 5 — Published Research"
3. Add subcategories:
   - Distributed Microgrids
   - Community Implementation
   - Conflict Resolution & Governance
   - Psychological Support & Trauma Recovery
   - Veterinary Care in Crisis Contexts
   - Integrated Corpus & Reference

**Step 4B Status (Discourse)**: 
- [ ] Discourse containers started successfully
- [ ] Discourse admin panel accessible
- [ ] Admin user created
- [ ] Categories created for Phase 5 content
- [ ] Discourse responding on port 3000
- [ ] Proceed to Step 5

---

### Step 5: Post-Deployment Verification (5 minutes)

**Objective**: Verify platform is accessible and ready for content upload

**5a. Verify nginx reverse proxy is forwarding traffic**
```bash
# Check nginx is running
sudo systemctl status nginx | grep "active (running)"
# Expected: "active (running)"

# Check reverse proxy is listening
sudo netstat -tlnp | grep nginx | grep "80\|443"
# Expected: nginx listening on both 80 and 443
```

**5b. Test platform accessibility**

**For Nextcloud+Matrix**:
```bash
curl -k https://127.0.0.1/nextcloud 2>&1 | head -20
# Expected: HTML response starting with "<!DOCTYPE" or redirect to login

curl -k https://127.0.0.1/_matrix/client/versions 2>&1 | grep -q "versions"
# Expected: JSON response with Matrix versions
```

**For Discourse**:
```bash
curl -k https://127.0.0.1/ 2>&1 | head -20
# Expected: HTML response with Discourse layout
```

**5c. Health check API calls**

**For Nextcloud+Matrix**:
```bash
# Check Nextcloud status API
curl -k https://127.0.0.1/nextcloud/status.php
# Expected: JSON response with installed: true

# Check Matrix homeserver /info
curl -k https://127.0.0.1/_matrix/federation/v1/version
# Expected: JSON response with server version
```

**For Discourse**:
```bash
# Check Discourse health
curl -k https://127.0.0.1/admin/dashboard.json
# Expected: JSON response with dashboard data
```

**5d. Verify ports are correctly bound**
```bash
sudo netstat -tlnp | grep LISTEN
# Expected: nginx on 80/443, Docker container ports (8080, 8008 for Nextcloud; 3000 for Discourse)
```

**5e. Verify CPU and Memory usage is normal**
```bash
docker stats --no-stream
# Expected: Reasonable CPU (<20%) and memory (<50%) usage
# If excessive, containers may still be initializing; wait 1-2 minutes and retry
```

**If Step 5 checks fail**:
- [ ] Check Docker logs: `docker-compose logs --tail=50 <service>`
- [ ] Verify network connectivity: `curl -v https://127.0.0.1`
- [ ] Check nginx configuration: `sudo nginx -t`
- [ ] Restart services: `docker-compose restart && sudo systemctl restart nginx`
- [ ] Contact technical lead if issues persist

**Step 5 Status**: 
- [ ] nginx reverse proxy running
- [ ] Platform accessible via HTTPS on localhost
- [ ] Health checks pass
- [ ] Docker containers in stable state
- [ ] **READY FOR CONTENT UPLOAD** — Proceed to Section 3

---

## SECTION 3: CONTENT UPLOAD EXECUTION (June 9 13:00–14:30 UTC)

### Overview

**Publication Order**: Documents uploaded sequentially to ensure readers encounter content in logical order:
1. Microgrids (foundational infrastructure)
2. Playbook (implementation framework)
3. Conflict Resolution (governance)
4. Psychological Support (trauma/mental health)
5. Veterinary Care (livestock management)
6. Integrated Corpus (unified reference)

**Each document upload cycle**: 
- Upload markdown file
- Upload corresponding PDF file
- Verify both are accessible and render correctly
- Check file size and metadata match source

**Estimated Time Per Document**: 5–7 minutes
- 1–2 minutes: Navigate to upload location
- 1–2 minutes: Upload both files
- 2–3 minutes: Verify accessibility and content integrity

**Total Upload Time**: ~35–40 minutes for all 6 documents

---

### Document 1: Distributed Microgrids (13:00–13:10 UTC)

**Source Files**:
- Markdown: `/tmp/phase5-pub/01-microgrids.md` (65 KB)
- PDF: `/tmp/phase5-pub/pdf/01-microgrids.pdf` (247 KB)

#### For Nextcloud+Matrix:

1. Navigate to Nextcloud web UI: https://100.70.184.84/nextcloud
2. Log in as admin
3. Navigate to folder: "Phase 5 Published Research/01-Microgrids/"
4. Drag-drop both files into folder (or upload individually)
5. Wait for both uploads to complete (progress bar shows 100%)
6. Verify files appear in folder listing
7. Click markdown file to preview; verify content is visible
8. Click PDF file to preview (Nextcloud may show PDF preview or offer download)

#### For Discourse:

1. Log in to Discourse admin panel
2. Navigate to "Phase 5 — Published Research" category
3. Click "New Topic"
4. Title: "Distributed Microgrids as Community Resilience Infrastructure"
5. Copy markdown file content into post body (or upload as attachment)
6. Attach PDF file (via "Upload" button in post editor)
7. Set category: "Distributed Microgrids"
8. Click "Create Topic"
9. Verify post appears in category and content is readable
10. Verify PDF download link works

**Status Check**:
- [ ] Markdown file uploaded and accessible
- [ ] PDF file uploaded and accessible
- [ ] Content renders without errors
- [ ] File sizes match source (65 KB markdown, 247 KB PDF)

**Expected Duration**: 5–7 minutes

---

### Document 2: Community Implementation Playbook (13:10–13:20 UTC)

**Source Files**:
- Markdown: `/tmp/phase5-pub/02-playbook.md` (65 KB)
- PDF: `/tmp/phase5-pub/pdf/02-playbook.pdf` (270 KB)

[Same upload procedure as Document 1, but for folder "02-Community-Implementation/"]

**Status Check**:
- [ ] Markdown file uploaded and accessible
- [ ] PDF file uploaded and accessible
- [ ] Content renders without errors
- [ ] File sizes match source (65 KB markdown, 270 KB PDF)

**Expected Duration**: 5–7 minutes

---

### Document 3: Conflict Resolution Framework (13:20–13:30 UTC)

**Source Files**:
- Markdown: `/tmp/phase5-pub/03-conflict-resolution.md` (59 KB)
- PDF: `/tmp/phase5-pub/pdf/03-conflict-resolution.pdf` (258 KB)

[Same upload procedure, folder "03-Conflict-Resolution/"]

**Status Check**:
- [ ] Markdown file uploaded and accessible
- [ ] PDF file uploaded and accessible
- [ ] Content renders without errors
- [ ] File sizes match source (59 KB markdown, 258 KB PDF)

**Expected Duration**: 5–7 minutes

---

### Document 4: Psychological Support & Trauma Recovery (13:30–13:40 UTC)

**Source Files**:
- Markdown: `/tmp/phase5-pub/04-psychological-support.md` (66 KB)
- PDF: `/tmp/phase5-pub/pdf/04-psychological-support.pdf` (267 KB)

[Same upload procedure, folder "04-Psychological-Support/"]

**Status Check**:
- [ ] Markdown file uploaded and accessible
- [ ] PDF file uploaded and accessible
- [ ] Content renders without errors
- [ ] File sizes match source (66 KB markdown, 267 KB PDF)

**Expected Duration**: 5–7 minutes

---

### Document 5: Veterinary Care in Crisis Contexts (13:40–13:50 UTC)

**Source Files**:
- Markdown: `/tmp/phase5-pub/05-veterinary-care.md` (77 KB)
- PDF: `/tmp/phase5-pub/pdf/05-veterinary-care.pdf` (286 KB)

[Same upload procedure, folder "05-Veterinary-Care/"]

**Status Check**:
- [ ] Markdown file uploaded and accessible
- [ ] PDF file uploaded and accessible
- [ ] Content renders without errors
- [ ] File sizes match source (77 KB markdown, 286 KB PDF)

**Expected Duration**: 5–7 minutes

---

### Document 6: Integrated Corpus & Reference (13:50–14:00 UTC)

**Source Files**:
- Markdown: `/tmp/phase5-pub/06-integrated-corpus.md` (114 KB)
- PDF: `/tmp/phase5-pub/pdf/06-integrated-corpus.pdf` (295 KB)

[Same upload procedure, folder "00-Integrated-Corpus/"]

**Status Check**:
- [ ] Markdown file uploaded and accessible
- [ ] PDF file uploaded and accessible
- [ ] Content renders without errors
- [ ] File sizes match source (114 KB markdown, 295 KB PDF)

**Expected Duration**: 5–7 minutes

---

### Upload Status Summary (14:00 UTC)

**Checkpoint**: All content uploaded. Before proceeding to notifications, verify:

```bash
# For Nextcloud: Via web UI, check all folders contain both markdown and PDF files
# For Discourse: Via admin panel, verify all 6 topics are created and published

# All checkboxes below should be marked:
- [ ] Document 1 uploaded (microgrids)
- [ ] Document 2 uploaded (playbook)
- [ ] Document 3 uploaded (conflict resolution)
- [ ] Document 4 uploaded (psychological support)
- [ ] Document 5 uploaded (veterinary care)
- [ ] Document 6 uploaded (integrated corpus)
- [ ] All files accessible via public URL (or logged-in user access)
- [ ] No missing files
- [ ] No corrupted uploads
- [ ] All content renders correctly
```

**If All Uploads Successful**: Proceed to Section 4 (Notifications)
**If Any Upload Failed**: Investigate, retry failed upload, verify integrity before proceeding

---

## SECTION 4: POST-PUBLICATION NOTIFICATIONS & MONITORING

### 4.1 Announcement to Author Coalition (14:00–14:15 UTC)

**Send email notification**:
```
To: [Author Coalition Distribution List]
Subject: Phase 5 Wave 1+2 Published — Community Resilience Framework Ready

Dear Phase 5 Authors,

The Phase 5 Wave 1+2 publication is now live and accessible to the public.

PUBLICATION DETAILS:
- Total Content: 61,611 words across 5 documents + integrated corpus
- Citation Base: 336+ references and cross-citations
- Access URL: https://100.70.184.84/nextcloud (Nextcloud+Matrix)
                OR https://100.70.184.84/ (Discourse)
- Publication Date: June 9, 2026 13:00 UTC

DOCUMENTS NOW AVAILABLE:
1. Distributed Microgrids as Community Resilience Infrastructure
2. Community Implementation Playbook — Tier 3 Coordination Framework
3. Conflict Resolution and Governance Framework — Tier 2 Deep Dive
4. Psychological Support and Trauma Recovery — Tier 2 Household Guide
5. Veterinary Care in Crisis Contexts — Tier 2 Household Guide
6. Integrated Corpus & Reference (all 5 documents unified)

Your contributions to this comprehensive community resilience framework are now available to communities worldwide.

Best regards,
[Project Lead Name]
```

**Status**: 
- [ ] Email sent successfully
- [ ] Author coalition has been notified
- [ ] Author feedback channel is open

---

### 4.2 Public Announcement (Optional, based on project scope)

**If public distribution is planned**:

1. Post announcement to project website/social media
2. Send press release to relevant communities
3. Notify related projects/initiatives
4. Update project status in README/documentation

---

### 4.3 Real-Time Monitoring (14:15–15:30 UTC)

**First 2-Hour Monitoring Window**: Monitor platform for errors, access issues, or performance degradation

**Monitoring Checklist**:

```bash
# Monitor Docker container health every 5 minutes
watch -n 300 'docker stats --no-stream'

# Check platform accessibility
watch -n 300 'curl -k https://127.0.0.1/ -w "HTTP Status: %{http_code}\n"'

# Monitor system logs for errors
tail -f /var/log/nginx/error.log &
tail -f /var/log/syslog | grep -i "error\|fail" &
```

**Expected Baseline** (after 30 minutes of publication):
- CPU usage: 10–20% (normal)
- Memory usage: 40–50% (normal)
- HTTP 200 responses: 100% success
- Nginx error log: No new errors related to Phase 5 content
- System logs: No critical errors

**If Issues Detected**:
1. Check application logs: `docker-compose logs --tail=100 <service>`
2. Verify disk space: `df -h`
3. Check network: `ping 8.8.8.8`, `curl https://example.com`
4. Restart affected service: `docker-compose restart <service>`
5. If unresolved, escalate to technical lead

**Monitoring Duration**: 2 hours minimum (14:00–16:00 UTC)
**Escalation Threshold**: Any error rate >5% or sustained CPU >80%

---

## SECTION 5: POST-DEPLOYMENT SIGN-OFF

### 5.1 Deployment Completion Checklist

**Date**: June 9, 2026
**Estimated Completion**: 15:00 UTC

- [ ] All pre-flight checks passed (Section 1)
- [ ] Content validation successful (Section 2)
- [ ] Reverse proxy configured and operational (Step 3)
- [ ] Platform installed successfully (Step 4)
- [ ] Post-deployment verification passed (Step 5)
- [ ] All 6 documents uploaded successfully
- [ ] Content accessible via platform
- [ ] Author coalition notified
- [ ] First 2-hour monitoring window completed
- [ ] No critical issues detected

**Deployment Status**: 
- [ ] ✅ **SUCCESSFUL** — Publication ready for continued operation
- [ ] ⚠️ **PARTIAL** — Some issues detected, monitoring continues
- [ ] ❌ **FAILED** — Critical errors, rollback initiated

---

### 5.2 Deployment Metrics

**Execution Timeline** (actual vs. planned):

| Phase | Planned | Actual | Status |
|-------|---------|--------|--------|
| Pre-flight checks | 5 min | ___ min | _____ |
| Content validation | 5 min | ___ min | _____ |
| Reverse proxy setup | 10 min | ___ min | _____ |
| Platform install | 15 min | ___ min | _____ |
| Post-deployment verification | 5 min | ___ min | _____ |
| Content upload (6 docs) | 40 min | ___ min | _____ |
| Notifications & monitoring | 30 min | ___ min | _____ |
| **TOTAL** | **110 min** | **___ min** | _____ |

**Performance Notes**:
- [ ] Deployment completed ahead of schedule (optional celebration!)
- [ ] Deployment completed on schedule
- [ ] Deployment took longer than expected; document reasons

---

### 5.3 Issue Log (if any problems encountered)

| Issue | Time | Impact | Resolution | Status |
|-------|------|--------|-----------|--------|
| [Example: Port conflict] | 13:15 | Medium | [Resolved by ...] | ✅ Resolved |
| | | | | |
| | | | | |

---

### 5.4 Post-Deployment Operations

**Ongoing Responsibilities**:
1. Monitor platform health (daily checks)
2. Monitor access logs for unusual activity
3. Maintain backup of published content
4. Monitor author feedback and community responses
5. Plan Phase 6 deployment (if scheduled)

**Escalation Contacts**:
- Technical Lead: [Name] ([Email])
- Project Lead: [Name] ([Email])
- Infrastructure Admin: [Name] ([Email])

---

## APPENDIX: Troubleshooting

### Docker Issues

**Problem**: Docker daemon not responding
```bash
# Restart Docker daemon
sudo systemctl restart docker
docker ps  # Test connectivity
```

**Problem**: Image pull timeout
```bash
# Check internet connection
curl https://example.com

# Increase Docker timeout (in /etc/docker/daemon.json)
# Add: "max-concurrent-downloads": 2
sudo systemctl restart docker
```

### Nginx Issues

**Problem**: nginx won't start
```bash
# Check configuration
sudo nginx -t

# Check port already in use
sudo netstat -tlnp | grep -E ':80|:443'

# Try manual start with verbose output
sudo nginx -g 'daemon off;'
```

### Platform-Specific Issues

**For Nextcloud**: See DEPLOYMENT_PLAYBOOK_NEXTCLOUD_MATRIX.md (platform-specific version)

**For Discourse**: See DEPLOYMENT_PLAYBOOK_DISCOURSE.md (platform-specific version)

---

**Document Version**: 1.0 (Template)
**Last Updated**: June 7, 2026
**Status**: Ready for platform-specific completion on June 8
**Valid Until**: June 9, 2026 15:00 UTC (deployment completion)
