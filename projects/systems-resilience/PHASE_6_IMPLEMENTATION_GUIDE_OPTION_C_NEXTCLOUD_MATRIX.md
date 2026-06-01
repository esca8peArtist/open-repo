---
title: "Phase 6 Platform Implementation Guide — Option C: Nextcloud Hub + Matrix/Element (Autonomy Path)"
project: systems-resilience
phase: 6
option: C
score: "8.5/10"
status: READY — pending June 3 decision
created: 2026-06-02
decision_deadline: 2026-06-03
operational_target: 2026-06-05 00:00 UTC
cost_annual: "$0 on raspby1 infrastructure + optional $120 Loomio"
host_machine: "raspby1 (Raspberry Pi 5, 100.70.184.84)"
cross_references:
  - PHASE_6_PLATFORM_ANALYSIS_v2.md
  - PHASE_6_DECISION_SUPPORT_CHECKLIST.md
  - PHASE_6_COMMUNICATION_INFRASTRUCTURE_SCOPING.md
---

# Option C: Nextcloud Hub + Matrix/Element — Autonomy Path Implementation Guide

**Score**: 34/40 (8.5/10) | **Annual cost**: $0 on raspby1 | **Setup time**: 7–10 hours | **Technical requirement**: Docker Compose familiarity

---

## 1. Pre-Implementation Checklist

Option C is the highest-complexity setup. Complete this checklist in full before starting. Skipped items cause mid-installation failures that are time-consuming to diagnose.

**Host Machine (raspby1)**
- [ ] SSH access confirmed: `ssh <user>@100.70.184.84` from your local machine succeeds
- [ ] Raspberry Pi 5 OS version: `cat /etc/os-release` — should show Debian/Bookworm or Ubuntu 22.04+
- [ ] Tailscale confirmed active on raspby1: `tailscale status` shows `100.70.184.84` as the device's IP
- [ ] Available disk space: `df -h /` — need at least 20 GB free for Docker images, Nextcloud data, and Matrix event store. Nextcloud alone will grow as documents accumulate; provision or mount external storage if under 40 GB free.
- [ ] Docker installed: `docker --version` and `docker compose version`. If absent:
  ```bash
  curl -fsSL https://get.docker.com | sh
  sudo usermod -aG docker $USER
  # log out and back in
  ```
- [ ] Memory check: `free -h` — Raspberry Pi 5 ships with 4 or 8 GB RAM. Nextcloud + Synapse together will use approximately 1.5–2 GB RAM under light load. 4 GB is the minimum; 8 GB is comfortable.

**Domain / Networking**
Option C has two deployment options. Choose one:

**Option C1 — Tailscale-only (recommended for this use case)**
Community members access Nextcloud and Matrix exclusively through Tailscale VPN. No public-facing services, no domain required, no port exposure. Members install Tailscale on their devices and join the tailnet.
- [ ] Tailscale admin panel access at `login.tailscale.com` — you are the account owner
- [ ] Tailscale ACL allows raspby1 to be reachable by all community member devices (default ACL permits this)
- [ ] No public domain needed; services are accessed at `http://100.70.184.84:8080` (Nextcloud) and `http://100.70.184.84:8448` (Matrix) or via Tailscale MagicDNS hostname

**Option C2 — Public domain with Caddy reverse proxy**
Community members access services from any internet connection without Tailscale.
- [ ] Domain name registered (e.g., `hub.yourdomain.org` for Nextcloud; `matrix.yourdomain.org` for Matrix)
- [ ] Dynamic DNS configured if raspby1 has a dynamic public IP (use ddclient or Cloudflare DDNS)
- [ ] Ports 80, 443 forwarded from router to raspby1's LAN IP
- [ ] This option requires an additional Caddy or Nginx reverse proxy configuration step (documented below)

**Email**
- [ ] SMTP credentials for outbound email (Nextcloud sends notifications for file shares, calendar invites). Use Brevo (free 300/day) or Mailgun free tier.
- [ ] Nextcloud and Synapse (Matrix) can share the same SMTP credentials.

**Credentials to Have Ready**
- raspby1 SSH credentials
- Tailscale admin credentials
- SMTP credentials (host, port, user, password)
- Admin email address (for both Nextcloud and Matrix admin accounts)
- Chosen admin password (use a password manager; you will need this to recover both systems)

---

## 2. Step-by-Step Installation

### Recommended Architecture

Both services run in Docker containers managed by Docker Compose. Nextcloud uses its standard LEMP stack (Nginx + MariaDB + PHP-FPM). Matrix Synapse uses PostgreSQL. The two services share a Docker network for internal communication but maintain separate databases.

Create a working directory on raspby1:

```bash
mkdir -p /opt/community
cd /opt/community
```

---

### Part A — Nextcloud Installation (Estimated: 2–3 hours)

#### Step A1 — Docker Compose File for Nextcloud

Create `/opt/community/nextcloud/docker-compose.yml`:

```yaml
version: "3.8"

services:
  db:
    image: mariadb:10.11
    container_name: nextcloud-db
    restart: always
    command: --transaction-isolation=READ-COMMITTED --log-bin=binlog --binlog-format=ROW
    environment:
      MYSQL_ROOT_PASSWORD: CHANGE_THIS_ROOT_PW
      MYSQL_DATABASE: nextcloud
      MYSQL_USER: nextcloud
      MYSQL_PASSWORD: CHANGE_THIS_DB_PW
    volumes:
      - nextcloud-db:/var/lib/mysql

  redis:
    image: redis:7-alpine
    container_name: nextcloud-redis
    restart: always

  app:
    image: nextcloud:28-fpm-alpine
    container_name: nextcloud-app
    restart: always
    depends_on:
      - db
      - redis
    environment:
      MYSQL_HOST: db
      MYSQL_DATABASE: nextcloud
      MYSQL_USER: nextcloud
      MYSQL_PASSWORD: CHANGE_THIS_DB_PW
      NEXTCLOUD_TRUSTED_DOMAINS: "100.70.184.84 hub.yourdomain.org"
      NEXTCLOUD_ADMIN_USER: admin
      NEXTCLOUD_ADMIN_PASSWORD: CHANGE_THIS_ADMIN_PW
      REDIS_HOST: redis
      SMTP_HOST: smtp.brevo.com
      SMTP_SECURE: ssl
      SMTP_PORT: 465
      SMTP_AUTHTYPE: LOGIN
      SMTP_NAME: your-smtp-user
      SMTP_PASSWORD: your-smtp-password
      MAIL_FROM_ADDRESS: noreply
      MAIL_DOMAIN: yourdomain.org
    volumes:
      - nextcloud-data:/var/www/html

  web:
    image: nginx:alpine
    container_name: nextcloud-web
    restart: always
    ports:
      - "127.0.0.1:8080:80"
    depends_on:
      - app
    volumes:
      - nextcloud-data:/var/www/html:ro
      - ./nginx.conf:/etc/nginx/nginx.conf:ro

volumes:
  nextcloud-db:
  nextcloud-data:
```

Replace all `CHANGE_THIS_*` values and SMTP credentials with real values before running.

Create a minimal `nginx.conf` in the same directory (Nextcloud provides an official example at `https://github.com/nextcloud/docker/blob/master/.examples/dockerfiles/full/apache/Dockerfile` — the nginx variant is linked from the same repo's README).

#### Step A2 — Launch Nextcloud

```bash
cd /opt/community/nextcloud
docker compose up -d
# Wait 2–3 minutes for first-run initialization
docker compose logs -f app  # watch until "Nextcloud was successfully installed"
```

#### Step A3 — Initial Nextcloud Configuration

Access Nextcloud at `http://100.70.184.84:8080` (Tailscale) or your public domain. Log in as admin.

**Enable required apps** (Apps menu → search and enable each):
- "Nextcloud Office" (collaborative document editing via Collabora CODE — bundled, just activate)
- "Calendar" (CalDAV-based; enable for community scheduling)
- "Talk" (built-in video conferencing — replaces Zoom for community calls)
- "External user authentication" (optional, for future SSO)

**Create community structure:**
```
Settings → Users → Add Group → "community-builders"
Create user accounts for each of the 8–12 initial members:
  Settings → Users → New User
  Username: firstname.lastname
  Email: their email address
  Groups: community-builders
```

**Create shared folder structure:**
```
Files → + New Folder → "Phase 5 Documents"
Files → + New Folder → "Phase 6 Working Documents"
Files → + New Folder → "Community Resources"
```
Share each folder with the "community-builders" group (right-click → Share → search "community-builders").

Upload Phase 5 Wave 1 and Wave 2 documents into "Phase 5 Documents". Enable collaborative editing by opening any DOCX file — Nextcloud Office opens in-browser with real-time collaboration.

---

### Part B — Matrix Synapse Installation (Estimated: 2–3 hours)

#### Step B1 — Generate Synapse Configuration

```bash
mkdir -p /opt/community/matrix
cd /opt/community/matrix

# Generate the initial homeserver configuration
docker run -it --rm \
  -v /opt/community/matrix/data:/data \
  -e SYNAPSE_SERVER_NAME=100.70.184.84 \
  -e SYNAPSE_REPORT_STATS=no \
  matrixdotorg/synapse:latest generate
```

This creates `/opt/community/matrix/data/homeserver.yaml`. Edit it:

```yaml
# In homeserver.yaml — key settings to verify/change:

server_name: "100.70.184.84"   # or your domain if using Option C2
public_baseurl: "http://100.70.184.84:8448"

# Enable registration (you will disable this after provisioning initial accounts)
enable_registration: true
enable_registration_without_verification: true

# Email (for password reset)
email:
  smtp_host: smtp.brevo.com
  smtp_port: 465
  smtp_user: your-smtp-user
  smtp_pass: your-smtp-password
  notif_from: "%(app)s <noreply@yourdomain.org>"

# Disable federation initially (tighten security; re-enable if community decides to federate)
federation_domain_whitelist: []
```

#### Step B2 — Docker Compose File for Synapse

Create `/opt/community/matrix/docker-compose.yml`:

```yaml
version: "3.8"

services:
  synapse:
    image: matrixdotorg/synapse:latest
    container_name: matrix-synapse
    restart: always
    ports:
      - "127.0.0.1:8448:8008"
    volumes:
      - /opt/community/matrix/data:/data
    environment:
      SYNAPSE_CONFIG_PATH: /data/homeserver.yaml

  element:
    image: vectorim/element-web:latest
    container_name: matrix-element
    restart: always
    ports:
      - "127.0.0.1:8081:80"
    volumes:
      - ./element-config.json:/app/config.json:ro
```

#### Step B3 — Element Client Configuration

Create `/opt/community/matrix/element-config.json`:

```json
{
    "default_server_config": {
        "m.homeserver": {
            "base_url": "http://100.70.184.84:8448",
            "server_name": "100.70.184.84"
        }
    },
    "brand": "Systems Resilience Community",
    "disable_custom_urls": true,
    "disable_guests": true,
    "default_theme": "dark"
}
```

#### Step B4 — Launch Matrix and Create Initial Rooms

```bash
cd /opt/community/matrix
docker compose up -d
# Wait ~60 seconds for Synapse to initialize
docker compose logs synapse  # watch for "Synapse is now up and running"
```

Create admin account and initial community rooms:

```bash
# Create admin account (run inside the Synapse container)
docker exec -it matrix-synapse register_new_matrix_user \
  -u admin -p CHANGE_THIS_ADMIN_PW -a \
  http://localhost:8008

# Create community builder accounts for each member
docker exec -it matrix-synapse register_new_matrix_user \
  -u firstname.lastname -p TEMP_PASSWORD_CHANGE_ON_FIRST_LOGIN \
  http://localhost:8008
```

Open Element at `http://100.70.184.84:8081` in a browser, log in as admin, and create rooms:
- "#general:100.70.184.84" — open discussion (set to invite-only)
- "#announcements:100.70.184.84" — admin-post-only (set moderator permissions)
- "#knowledge-base:100.70.184.84" — links and references
- "#events:100.70.184.84" — event coordination

Create a Space (Matrix equivalent of a community hub) and add all rooms to it. Invite community builder accounts to the Space.

#### Step B5 — Disable Open Registration

After provisioning all initial accounts, disable registration to prevent unauthorized signups:

In `homeserver.yaml`:
```yaml
enable_registration: false
```

Then restart: `docker compose restart synapse`

---

### Part C — Optional: Caddy Reverse Proxy for Public Access (Option C2 only)

If using a public domain, add Caddy as a reverse proxy:

```bash
# /opt/community/caddy/Caddyfile
hub.yourdomain.org {
    reverse_proxy 127.0.0.1:8080
}

matrix.yourdomain.org {
    reverse_proxy 127.0.0.1:8448
}

element.yourdomain.org {
    reverse_proxy 127.0.0.1:8081
}
```

Caddy handles Let's Encrypt certificates automatically. Add Caddy to the Docker Compose setup or run it natively via `apt install caddy`. Do not expose services directly without TLS.

---

## 3. Integration With Existing Systems

**Tailscale (already in use)**
For Tailscale-only deployment (Option C1), no additional configuration is needed. Community members install Tailscale on their devices and join the tailnet using an invite link generated at `login.tailscale.com`. Once connected, they access:
- Nextcloud: `http://100.70.184.84:8080`
- Element (Matrix client): `http://100.70.184.84:8081`

Enable Tailscale MagicDNS in the admin panel for friendlier addresses (e.g., `http://raspby1:8080`).

**GitHub Pages Integration**
- Nextcloud: generate a "Share link" for any file or folder (Files → right-click → Share → Create public link). Embed or link this from GitHub Pages pages. The link remains stable even if file contents update.
- Matrix widget: Element supports embedding web content via room widgets. Add the GitHub Pages URL as a widget in the `#knowledge-base` room so members can view publications without leaving Element.

**Email**
Both Nextcloud and Synapse use the same SMTP credentials configured above. Test Nextcloud email: Settings → Basic Settings → Email server → "Send test email."

**Shared Login (Single Sign-On)**
Full SSO between Nextcloud and Matrix requires LDAP or an external identity provider (Keycloak). This is not required for launch. For Phase 6, maintain two separate credential sets (one for Nextcloud, one for Matrix) and provision them together during member onboarding. If SSO is desired post-launch, Nextcloud's LDAP app and Synapse's LDAP auth provider (`matrix-synapse-ldap3`) can be configured in approximately 4 additional hours.

**GitHub Actions Integration**
Matrix supports an incoming webhook via the `matrix-appservice-webhooks` bridge. This allows automated notifications (e.g., "New document published on GitHub Pages") to post into the #announcements room. Install after primary setup if desired:

```bash
# Add to matrix docker-compose.yml as an additional service
# See: https://github.com/turt2live/matrix-appservice-webhooks
```

**Loomio Governance Supplement**
Synapse supports outbound notifications via Matrix hooks. Post Loomio decision links directly into the #events or #general room. Configure Loomio to send Matrix notifications: Loomio Settings → Integrations → Matrix → enter the webhook URL for the #announcements room.

---

## 4. Timeline and Effort Estimate

| Date | Action | Time Required | Prerequisite |
|---|---|---|---|
| June 3 (decision day) | raspby1 SSH confirmed; disk space verified | 15 min | Decision made |
| June 3 | Nextcloud Docker Compose file written and customized | 30 min | Docker installed |
| June 3 | Nextcloud launched; initial admin configuration | 90 min | Compose file complete |
| June 3–4 | Phase 5 documents uploaded; shared folder structure created | 60 min | Nextcloud running |
| June 4 | Synapse config generated; docker-compose written | 45 min | Nextcloud stable |
| June 4 | Synapse + Element launched; admin account created | 60 min | Synapse config ready |
| June 4 | Matrix rooms and Space created; member accounts provisioned | 60 min | Synapse running |
| June 4 | Registration disabled; Tailscale access tested from second device | 30 min | All accounts provisioned |
| June 5 (target) | Invite links shared with 8–12 community builders; onboarding doc posted | 30 min | Full stack operational |

**Critical path**: The Nextcloud data volume grows over time and cannot easily be relocated. Confirm disk capacity before starting. If raspby1 has less than 40 GB free, attach external USB storage and mount it before creating the Docker volume.

**Total active effort**: approximately 7–9 hours across June 3–5. The work is sequential (Matrix setup depends on Nextcloud being stable first) so parallel effort does not shorten the calendar timeline.

---

## 5. Post-Launch Validation

**Nextcloud**
- [ ] Log in as admin at `http://100.70.184.84:8080`; Files app shows shared folder structure
- [ ] Log in as a test community member; confirm shared folders are visible and documents are readable
- [ ] Open a DOCX file in Nextcloud Office; confirm the collaborative editor loads
- [ ] Calendar app: create a test event for June 15; confirm it syncs to a CalDAV client (Apple Calendar, Thunderbird)
- [ ] Talk app: start a video call between admin and test account; confirm audio and video work

**Matrix**
- [ ] Log in to Element at `http://100.70.184.84:8081` as admin; confirm all rooms are visible
- [ ] Log in with test member account; confirm invitation to Space and all rooms has arrived
- [ ] Send a test message in #general; confirm admin and test account both receive it
- [ ] Test offline read: disconnect test device from network; open Element; confirm previously loaded messages are readable

**Tailscale Access**
- [ ] From a device that is on the tailnet but not on the local network (e.g., a phone on cellular), access `http://100.70.184.84:8080` and `http://100.70.184.84:8081`. Both should load without any VPN configuration beyond Tailscale.

**Email**
- [ ] Nextcloud password reset email: Settings → Users → select test user → send password reset. Confirm email arrives.

**Success criteria**: A new community builder can receive a Tailscale invite, join the tailnet, access both Nextcloud and Element, read Phase 5 documents offline in Element, and co-edit a document in Nextcloud — all within 45 minutes of initial onboarding.

---

## 6. Rollback and Migration Path

Option C's data is entirely self-owned and stored on raspby1. There is no vendor lock-in.

**Nextcloud data export**
All files are stored in the Docker volume at `/var/lib/docker/volumes/nextcloud_nextcloud-data`. Copy the volume directory for a full backup:

```bash
docker compose stop
tar -czf /backup/nextcloud-data-$(date +%Y%m%d).tar.gz \
  /var/lib/docker/volumes/nextcloud_nextcloud-data
docker compose start
```

**Matrix data export**
Matrix event history is stored in Synapse's data directory (`/opt/community/matrix/data`). Export individual rooms via the Synapse admin API:

```bash
curl -X GET "http://localhost:8448/_synapse/admin/v1/rooms" \
  -H "Authorization: Bearer ADMIN_ACCESS_TOKEN"
```

**Migration to Option A (Discourse)**
Files go to Discourse's file upload system or are posted as wiki posts. Matrix history has no Discourse import path — content is summarized and posted as a new topic per room. Estimated 3–5 hours.

**Migration to Option B (Mighty Networks)**
Files re-uploaded to Knowledge Base space. Estimated 2 hours. Matrix history not migrated.

**Stopping the service**
```bash
docker compose -f /opt/community/nextcloud/docker-compose.yml stop
docker compose -f /opt/community/matrix/docker-compose.yml stop
```

Services stop immediately. Data remains on disk until volumes are manually removed. raspby1 is not affected beyond reclaimed RAM and CPU. The Tailscale tailnet and existing configuration are unaffected.

**Minimum viable rollback time**: 10 minutes to stop services; 2–5 hours to rebuild content on an alternative platform. No sunk cost beyond the time spent on setup.

---

## Appendix: Ongoing Maintenance Reference

**Nextcloud updates**
```bash
cd /opt/community/nextcloud
docker compose pull && docker compose up -d
```

**Synapse updates**
```bash
cd /opt/community/matrix
docker compose pull && docker compose up -d
```

**Backup schedule (recommended)**
Run the Nextcloud backup command above via cron weekly. Store backups on a separate drive or remote location. The Synapse data directory should be included in the same backup script. Both services can be stopped briefly for consistent backups without community impact (low-traffic volunteer community; 5-minute maintenance windows are negligible).

**Adding new members after launch**
Nextcloud: Settings → Users → New User → assign to community-builders group → share onboarding document.
Matrix: `docker exec -it matrix-synapse register_new_matrix_user -u username http://localhost:8008`, then invite to the community Space from Element.
Tailscale: Admin panel → Invite user (if not already on the tailnet).
