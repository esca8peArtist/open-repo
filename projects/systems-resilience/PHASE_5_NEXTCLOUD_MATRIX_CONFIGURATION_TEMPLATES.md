---
title: "Phase 5 Nextcloud + Matrix — Configuration Templates"
project: systems-resilience
phase: 5
status: PRODUCTION-READY — apply during deployment Stage 8 (after containers healthy)
applies_after: PHASE_5_DEPLOYMENT_SCRIPTS_NEXTCLOUD_MATRIX.md
created: 2026-06-04
version: 1.0
cross_references:
  - NEXTCLOUD_MATRIX_DEPLOYMENT_PLAYBOOK.md
  - PHASE_5_DEPLOYMENT_SCRIPTS_NEXTCLOUD_MATRIX.md
  - PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md
---

# Phase 5 Configuration Templates — Nextcloud + Matrix
## Author Coordination Setup for Wave 1 (18 Authors, 5 Domains)

This document provides copy-paste-ready configuration for the author coordination layer: CalDAV/CardDAV shared calendars, Matrix room hierarchy, permissions per domain, and federation notes. Apply these after the base stack is healthy.

---

## Part 1: Nextcloud CalDAV/CardDAV Setup

### 1.1 Shared Editorial Calendar

Create a shared calendar visible to all Wave 1 authors for milestone tracking. Run on raspby1 after deployment:

```bash
# Create shared editorial calendar as admin
# Using Nextcloud occ CLI
docker exec -u www-data community-nextcloud php occ \
  dav:create-calendar admin editorial-calendar "Phase 5 Editorial Calendar"

# Share the calendar with the "authors" group (created in Part 2)
# This is done via Nextcloud web UI:
# 1. Open https://100.70.184.84/apps/calendar
# 2. Click the three-dot menu next to "Phase 5 Editorial Calendar"
# 3. Click "Share" → type "authors" (group name) → click Share
# 4. Set permission: "Can edit" (so authors can add draft completion events)
```

**Calendar events to pre-populate** (add these via the Nextcloud Calendar UI or CalDAV client after setup):

| Date | Event | Description |
|------|-------|-------------|
| June 5 | Wave 1 Go-Live | Platform live, onboarding emails sent |
| June 8 | First Draft Check-In | Author draft status review in #coordination |
| June 15 09:00 UTC | Go/No-Go Decision Point | 15+ acceptances required to proceed |
| June 20 | Roster Finalized | Final author list locked |
| June 30 | Wave 1 Drafts Due | All Wave 1 articles submitted |
| July 15 | Peer Review Complete | Author cross-reviews finished |
| July 31 | Wave 1 Publication | Articles published to corpus |

### 1.2 CalDAV Sync URL for Authors

Authors add the shared calendar to their own calendar app:

```
CalDAV Server: https://100.70.184.84/remote.php/dav/
Calendar URL:  https://100.70.184.84/remote.php/dav/calendars/admin/editorial-calendar/
Username:      [their Nextcloud username]
Password:      [their Nextcloud password]
```

**Client-specific instructions**:

- **macOS Calendar**: File → New Calendar Subscription → paste CalDAV URL → enter credentials
- **Google Calendar** (no native CalDAV): Use a third-party app (e.g., CalDAV-Sync for Android, BusyCal for Mac)
- **Thunderbird**: Calendar → New Calendar → CalDAV → paste URL
- **iOS**: Settings → Calendar → Accounts → Add Account → Other → Add CalDAV Account

### 1.3 Shared Author Contact List (CardDAV)

Create a shared address book for author contact info and Matrix IDs:

```bash
# Create shared address book
docker exec -u www-data community-nextcloud php occ \
  dav:create-addressbook admin wave1-authors "Wave 1 Authors"
```

Via Nextcloud UI (Settings → Contacts → New address book), then share with the "authors" group (read-only access for all authors, read-write for admin).

**Pre-populate with author vCard entries** (example format):

```vcf
BEGIN:VCARD
VERSION:3.0
FN:Jane Smith
N:Smith;Jane;;;
EMAIL;TYPE=INTERNET:smith@example.com
X-MATRIX-ID:@author_smith:resilience-hub.local
ORG:Cooperative Institute / University
NOTE:Domain 1 - Governance and Decision-Making
END:VCARD
```

---

## Part 2: Nextcloud Groups and Permissions

### 2.1 Group Structure

Create the following groups in Nextcloud (Settings → Users → Add group):

| Group | Members | Purpose |
|-------|---------|---------|
| `authors` | All 18 Wave 1 authors | Shared calendar, contact list, Wave 1 folder read/write |
| `domain-1-governance` | 3–4 authors in Domain 1 | Domain 1 folder full access |
| `domain-2-food` | 3–4 authors in Domain 2 | Domain 2 folder full access |
| `domain-3-infrastructure` | 3–4 authors in Domain 3 | Domain 3 folder full access |
| `domain-4-security` | 3–4 authors in Domain 4 | Domain 4 folder full access |
| `domain-5-scaling` | 3–4 authors in Domain 5 | Domain 5 folder full access |
| `editors` | Admin + 1–2 lead reviewers | Admin access to all author folders |
| `reviewers` | Peer reviewers | Comment-only access to all folders |

Create groups via occ:

```bash
docker exec -u www-data community-nextcloud php occ group:add authors
docker exec -u www-data community-nextcloud php occ group:add domain-1-governance
docker exec -u www-data community-nextcloud php occ group:add domain-2-food
docker exec -u www-data community-nextcloud php occ group:add domain-3-infrastructure
docker exec -u www-data community-nextcloud php occ group:add domain-4-security
docker exec -u www-data community-nextcloud php occ group:add domain-5-scaling
docker exec -u www-data community-nextcloud php occ group:add editors
docker exec -u www-data community-nextcloud php occ group:add reviewers
```

Add authors to groups after creating their accounts:

```bash
# Example: add author_smith to authors + domain-1-governance
docker exec -u www-data community-nextcloud php occ group:adduser authors author_smith
docker exec -u www-data community-nextcloud php occ group:adduser domain-1-governance author_smith
```

### 2.2 Folder Structure and Permissions

Create the Phase 5 folder hierarchy:

```bash
# Create folder structure via WebDAV (run from raspby1 after deployment)
NEXTCLOUD_URL="https://100.70.184.84"
ADMIN_PASS=$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)

# Create top-level folders
for path in \
  "Phase5_Wave1" \
  "Phase5_Wave1/Domain1_Governance" \
  "Phase5_Wave1/Domain2_Food" \
  "Phase5_Wave1/Domain3_Infrastructure" \
  "Phase5_Wave1/Domain4_Security" \
  "Phase5_Wave1/Domain5_Scaling" \
  "Phase5_Wave1/_Administration" \
  "Phase5_Wave1/_Administration/Author_Guides" \
  "Phase5_Wave1/_Administration/Editorial_Calendar" \
  "Phase5_Wave1/_Administration/Policy_Documents" \
  "Phase5_Wave1/_Reviews"; do
  curl -sk -u "admin:$ADMIN_PASS" \
    -X MKCOL \
    "$NEXTCLOUD_URL/remote.php/dav/files/admin/$path"
  echo "Created: $path"
done
```

Share folders with groups via Nextcloud sharing API:

```bash
# Share Domain 1 folder with domain-1-governance group (permission 31 = read+write+share+create+delete)
# Permission 17 = read+write (most common for authors)
# Permission 1  = read only (for reviewers)

NEXTCLOUD_URL="https://100.70.184.84"
ADMIN_PASS=$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)

# Share Wave1 top-level with all authors (read-only — they access their domain folder for writing)
curl -sk -u "admin:$ADMIN_PASS" \
  -X POST \
  "$NEXTCLOUD_URL/ocs/v2.php/apps/files_sharing/api/v1/shares?format=json" \
  -H "OCS-APIRequest: true" \
  -d "path=/Phase5_Wave1&shareType=1&shareWith=authors&permissions=1"

# Share each domain folder with the domain group (read+write = permission 17)
for domain_num in 1 2 3 4 5; do
  domain_names=("Governance" "Food" "Infrastructure" "Security" "Scaling")
  domain_name="${domain_names[$((domain_num-1))]}"
  curl -sk -u "admin:$ADMIN_PASS" \
    -X POST \
    "$NEXTCLOUD_URL/ocs/v2.php/apps/files_sharing/api/v1/shares?format=json" \
    -H "OCS-APIRequest: true" \
    -d "path=/Phase5_Wave1/Domain${domain_num}_${domain_name}&shareType=1&shareWith=domain-${domain_num}-${domain_name,,}&permissions=17"
  echo "Shared Domain $domain_num with domain-$domain_num group"
done

# Share Reviews folder with all authors (read+create = permission 5)
curl -sk -u "admin:$ADMIN_PASS" \
  -X POST \
  "$NEXTCLOUD_URL/ocs/v2.php/apps/files_sharing/api/v1/shares?format=json" \
  -H "OCS-APIRequest: true" \
  -d "path=/Phase5_Wave1/_Reviews&shareType=1&shareWith=authors&permissions=5"
```

### 2.3 Permissions Reference Table

| Folder | Group | Permission | Notes |
|--------|-------|------------|-------|
| `/Phase5_Wave1/` | `authors` | Read (1) | See structure, not write |
| `/Phase5_Wave1/Domain1_Governance/` | `domain-1-governance` | Read+Write (17) | Authors edit their domain |
| `/Phase5_Wave1/Domain2_Food/` | `domain-2-food` | Read+Write (17) | |
| `/Phase5_Wave1/Domain3_Infrastructure/` | `domain-3-infrastructure` | Read+Write (17) | |
| `/Phase5_Wave1/Domain4_Security/` | `domain-4-security` | Read+Write (17) | |
| `/Phase5_Wave1/Domain5_Scaling/` | `domain-5-scaling` | Read+Write (17) | |
| `/Phase5_Wave1/_Reviews/` | `authors` | Read+Create (5) | Peer review submissions |
| `/Phase5_Wave1/_Administration/` | `editors` | Full (31) | Admin only |
| `/Phase5_Wave1/_Administration/Author_Guides/` | `authors` | Read (1) | View guides only |
| All folders | `reviewers` | Read+Comment | Comment-only via Nextcloud Text |

---

## Part 3: Matrix Room / Space Hierarchy

### 3.1 Space Structure

Create one Matrix Space as the top-level container, with child rooms for each domain.

**Space**: `Phase 5 — Resilience Corpus`

```
Phase 5 — Resilience Corpus (Space)
├── #general:resilience-hub.local           (all authors)
├── #coordination:resilience-hub.local      (editors + authors)
├── #domain-1-governance:resilience-hub.local
├── #domain-2-food:resilience-hub.local
├── #domain-3-infrastructure:resilience-hub.local
├── #domain-4-security:resilience-hub.local
├── #domain-5-scaling:resilience-hub.local
├── #peer-review:resilience-hub.local       (cross-domain review)
├── #technical:resilience-hub.local         (platform support)
└── #admin-only:resilience-hub.local        (admin, private)
```

### 3.2 Room Creation Script

```bash
# Run these commands from a machine with curl and the admin Matrix token

MATRIX_URL="https://100.70.184.84"
ADMIN_TOKEN="$(grep SYNAPSE_ADMIN_TOKEN /opt/community/nextcloud-matrix/.env.runtime | cut -d= -f2)"
DOMAIN="resilience-hub.local"

# Helper function: create a room
create_room() {
  local alias="$1"
  local name="$2"
  local topic="$3"
  local preset="${4:-private_chat}"  # private_chat or public_chat
  
  curl -s -X POST \
    -H "Authorization: Bearer $ADMIN_TOKEN" \
    -H "Content-Type: application/json" \
    "$MATRIX_URL/_matrix/client/v3/createRoom" \
    -d "{
      \"room_alias_name\": \"$alias\",
      \"name\": \"$name\",
      \"topic\": \"$topic\",
      \"preset\": \"$preset\",
      \"initial_state\": [{
        \"type\": \"m.room.history_visibility\",
        \"content\": {\"history_visibility\": \"shared\"}
      }, {
        \"type\": \"m.room.guest_access\",
        \"content\": {\"guest_access\": \"forbidden\"}
      }]
    }" | python3 -m json.tool
}

# Create all rooms
create_room "general" "General" "Welcome to Phase 5. Introductions and announcements." "restricted"
create_room "coordination" "Coordination" "Editor-author coordination. Check-ins, deadlines, blockers." "private_chat"
create_room "domain-1-governance" "Domain 1: Governance" "Governance and decision-making at community scale." "private_chat"
create_room "domain-2-food" "Domain 2: Food Systems" "Food systems, supply chains, and agricultural resilience." "private_chat"
create_room "domain-3-infrastructure" "Domain 3: Information Infrastructure" "Information infrastructure, comms, and data resilience." "private_chat"
create_room "domain-4-security" "Domain 4: Security and Defense" "Community security frameworks and conflict de-escalation." "private_chat"
create_room "domain-5-scaling" "Domain 5: Scaling Pathways" "Scaling thresholds, federation, and inter-community coordination." "private_chat"
create_room "peer-review" "Peer Review" "Cross-domain article review and feedback." "private_chat"
create_room "technical" "Technical Support" "Platform issues, account problems, upload help." "private_chat"
```

**Admin-only room**: Create manually in Element, set join_rules to `invite`, do not share the room alias publicly.

### 3.3 Space Creation and Room Linking

```bash
# Create the Space itself
SPACE_ROOM_ID=$(curl -s -X POST \
  -H "Authorization: Bearer $ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  "$MATRIX_URL/_matrix/client/v3/createRoom" \
  -d '{
    "name": "Phase 5 — Resilience Corpus",
    "topic": "Coordination space for Phase 5 Wave 1 authors",
    "creation_content": {"type": "m.space"},
    "preset": "private_chat",
    "room_alias_name": "phase5-space"
  }' | python3 -c "import json,sys; print(json.load(sys.stdin)['room_id'])")

echo "Space room ID: $SPACE_ROOM_ID"

# Link child rooms to the Space (m.space.child event)
# Get room IDs first:
for alias in general coordination domain-1-governance domain-2-food \
             domain-3-infrastructure domain-4-security domain-5-scaling \
             peer-review technical; do
  ROOM_ID=$(curl -s \
    "$MATRIX_URL/_matrix/client/v3/directory/room/%23${alias}%3A${DOMAIN}" \
    -H "Authorization: Bearer $ADMIN_TOKEN" | \
    python3 -c "import json,sys; print(json.load(sys.stdin).get('room_id','NOT_FOUND'))")
  
  echo "Linking $alias ($ROOM_ID) to Space"
  
  # Add as child of Space
  curl -s -X PUT \
    -H "Authorization: Bearer $ADMIN_TOKEN" \
    -H "Content-Type: application/json" \
    "$MATRIX_URL/_matrix/client/v3/rooms/$SPACE_ROOM_ID/state/m.space.child/$ROOM_ID" \
    -d '{"via": ["resilience-hub.local"], "suggested": true}'
done
```

### 3.4 Room Power Levels (Permissions)

Matrix uses numerical power levels:
- 100 = Admin (can do anything)
- 50 = Moderator (can kick, ban, redact)
- 0 = Regular user (default)

Set per-room power levels for Wave 1:

```bash
# Helper: set power level for a user in a room
set_power_level() {
  local room_id="$1"
  local user_id="$2"
  local level="$3"
  
  # Get current power levels first
  CURRENT=$(curl -s \
    -H "Authorization: Bearer $ADMIN_TOKEN" \
    "$MATRIX_URL/_matrix/client/v3/rooms/$room_id/state/m.room.power_levels")
  
  # This is a simplified approach — use admin API to set specific user power level
  curl -s -X PUT \
    -H "Authorization: Bearer $ADMIN_TOKEN" \
    -H "Content-Type: application/json" \
    "$MATRIX_URL/_matrix/client/v3/rooms/$room_id/state/m.room.power_levels" \
    -d "{\"users\": {\"@admin:$DOMAIN\": 100, \"$user_id\": $level}}"
}

# Admin gets power 100 in all rooms (set during room creation — admin is owner)
# Domain leads get power 50 in their domain room

# Example: set domain lead as moderator in their domain room
# (Replace with actual room IDs and usernames from your wave1_authors.csv)
DOMAIN_1_ROOM_ID="!..."  # Get from room creation output above
set_power_level "$DOMAIN_1_ROOM_ID" "@author_smith:$DOMAIN" 50
```

**Standard Wave 1 power level policy**:

| Role | Power Level | Applies to |
|------|-------------|------------|
| Admin (@admin) | 100 | All rooms |
| Domain lead (one per domain) | 50 | Their domain room |
| All Wave 1 authors | 0 (default) | All rooms they're in |
| Mjolnir bot (if deployed) | 100 | All rooms |

---

## Part 4: Author Account Assignment to Domains

### 4.1 Wave 1 Author Roster Template (18 Authors)

This table must be filled in from the PHASE_5_WAVE_1_AUTHOR_RECRUITMENT_RUNBOOK.md author list:

| # | Username | Display Name | Domain | Nextcloud Group | Matrix Rooms |
|---|----------|-------------|--------|----------------|--------------|
| 1 | author_01 | [Name] | Domain 1: Governance | authors, domain-1-governance | #general, #domain-1-governance, #peer-review, #coordination |
| 2 | author_02 | [Name] | Domain 1: Governance | authors, domain-1-governance | #general, #domain-1-governance, #peer-review, #coordination |
| 3 | author_03 | [Name] | Domain 1: Governance | authors, domain-1-governance | #general, #domain-1-governance, #peer-review, #coordination |
| 4 | author_04 | [Name] | Domain 1: Governance | authors, domain-1-governance | #general, #domain-1-governance, #peer-review, #coordination |
| 5 | author_05 | [Name] | Domain 2: Food | authors, domain-2-food | #general, #domain-2-food, #peer-review, #coordination |
| 6 | author_06 | [Name] | Domain 2: Food | authors, domain-2-food | ... |
| 7 | author_07 | [Name] | Domain 2: Food | authors, domain-2-food | ... |
| 8 | author_08 | [Name] | Domain 3: Infrastructure | authors, domain-3-infrastructure | ... |
| 9 | author_09 | [Name] | Domain 3: Infrastructure | authors, domain-3-infrastructure | ... |
| 10 | author_10 | [Name] | Domain 3: Infrastructure | authors, domain-3-infrastructure | ... |
| 11 | author_11 | [Name] | Domain 4: Security | authors, domain-4-security | ... |
| 12 | author_12 | [Name] | Domain 4: Security | authors, domain-4-security | ... |
| 13 | author_13 | [Name] | Domain 4: Security | authors, domain-4-security | ... |
| 14 | author_14 | [Name] | Domain 5: Scaling | authors, domain-5-scaling | ... |
| 15 | author_15 | [Name] | Domain 5: Scaling | authors, domain-5-scaling | ... |
| 16 | author_16 | [Name] | Domain 5: Scaling | authors, domain-5-scaling | ... |
| 17 | author_17 | [Name] | Cross-domain | authors | All domain rooms |
| 18 | author_18 | [Name] | Cross-domain | authors | All domain rooms |

### 4.2 Batch Group and Room Assignment Script

After creating accounts via the bulk import script, assign to groups and rooms:

```bash
#!/bin/bash
# assign_authors.sh — Run after import_users.py completes

MATRIX_URL="https://100.70.184.84"
DOMAIN="resilience-hub.local"
ADMIN_TOKEN="$(grep SYNAPSE_ADMIN_TOKEN /opt/community/nextcloud-matrix/.env.runtime | cut -d= -f2)"
ADMIN_PASS="$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)"
NC_URL="https://100.70.184.84"

# Define author→domain mapping
# Format: "username:domain_number"
declare -a ASSIGNMENTS=(
  "author_01:1"
  "author_02:1"
  "author_03:1"
  "author_04:1"
  "author_05:2"
  "author_06:2"
  "author_07:2"
  "author_08:3"
  "author_09:3"
  "author_10:3"
  "author_11:4"
  "author_12:4"
  "author_13:4"
  "author_14:5"
  "author_15:5"
  "author_16:5"
  "author_17:cross"
  "author_18:cross"
)

DOMAIN_NAMES=("" "governance" "food" "infrastructure" "security" "scaling")

for assignment in "${ASSIGNMENTS[@]}"; do
  username="${assignment%%:*}"
  domain="${assignment##*:}"
  
  echo "=== Processing $username (Domain $domain) ==="
  
  # Add to 'authors' group (Nextcloud)
  docker exec -u www-data community-nextcloud php occ group:adduser authors "$username"
  
  if [[ "$domain" != "cross" ]]; then
    # Add to domain group (Nextcloud)
    group_name="domain-${domain}-${DOMAIN_NAMES[$domain]}"
    docker exec -u www-data community-nextcloud php occ group:adduser "$group_name" "$username"
    
    # Invite to domain Matrix room
    ROOM_ALIAS="domain-${domain}-${DOMAIN_NAMES[$domain]}"
    ROOM_ID=$(curl -s \
      "$MATRIX_URL/_matrix/client/v3/directory/room/%23${ROOM_ALIAS}%3A${DOMAIN}" \
      -H "Authorization: Bearer $ADMIN_TOKEN" | \
      python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('room_id',''))")
    
    if [[ -n "$ROOM_ID" ]]; then
      curl -s -X POST \
        -H "Authorization: Bearer $ADMIN_TOKEN" \
        -H "Content-Type: application/json" \
        "$MATRIX_URL/_matrix/client/v3/rooms/$ROOM_ID/invite" \
        -d "{\"user_id\": \"@${username}:${DOMAIN}\"}"
      echo "  Invited @$username to $ROOM_ALIAS"
    fi
  else
    # Cross-domain: invite to all domain rooms
    for d in 1 2 3 4 5; do
      ROOM_ALIAS="domain-${d}-${DOMAIN_NAMES[$d]}"
      ROOM_ID=$(curl -s \
        "$MATRIX_URL/_matrix/client/v3/directory/room/%23${ROOM_ALIAS}%3A${DOMAIN}" \
        -H "Authorization: Bearer $ADMIN_TOKEN" | \
        python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('room_id',''))")
      if [[ -n "$ROOM_ID" ]]; then
        curl -s -X POST \
          -H "Authorization: Bearer $ADMIN_TOKEN" \
          -H "Content-Type: application/json" \
          "$MATRIX_URL/_matrix/client/v3/rooms/$ROOM_ID/invite" \
          -d "{\"user_id\": \"@${username}:${DOMAIN}\"}"
      fi
    done
  fi
  
  # Invite all authors to: #general, #peer-review, #technical
  for room_alias in general peer-review technical; do
    ROOM_ID=$(curl -s \
      "$MATRIX_URL/_matrix/client/v3/directory/room/%23${room_alias}%3A${DOMAIN}" \
      -H "Authorization: Bearer $ADMIN_TOKEN" | \
      python3 -c "import json,sys; d=json.load(sys.stdin); print(d.get('room_id',''))")
    if [[ -n "$ROOM_ID" ]]; then
      curl -s -X POST \
        -H "Authorization: Bearer $ADMIN_TOKEN" \
        -H "Content-Type: application/json" \
        "$MATRIX_URL/_matrix/client/v3/rooms/$ROOM_ID/invite" \
        -d "{\"user_id\": \"@${username}:${DOMAIN}\"}"
    fi
  done
  
  echo "  Done: $username"
done

echo ""
echo "Assignment complete. Verify in Element or via:"
echo "  curl -H 'Authorization: Bearer \$ADMIN_TOKEN' $MATRIX_URL/_synapse/admin/v2/users"
```

---

## Part 5: Federation Configuration

### 5.1 Wave 1 (Internal Only — Tailscale)

For Phase 5 Wave 1, Matrix federation to external servers is **not required**. All 18 authors access the instance via Tailscale. The `homeserver.yaml` configuration should have:

```yaml
# matrix/config/homeserver.yaml — federation settings for Wave 1

# Disable public room directory
allow_public_rooms_over_federation: false

# Restrict federation to internal only (no outbound federation)
# Comment these out to allow full federation in a later phase
federation_domain_whitelist: []  # Empty list = allow all (but no external users can join)

# Registration: closed — invite only
enable_registration: false
registration_requires_token: true
```

**TLS for Tailscale-only**: The `bind_addresses` in `homeserver.yaml` listeners should be `['127.0.0.1']`, not `['0.0.0.0']`. Traffic arrives via the nginx reverse proxy.

### 5.2 Wave 2 Federation (Defer to June 30+)

Federation to external Matrix servers enables:
- Authors outside the Tailscale network to join without installing Tailscale
- Cross-community coordination (other resilience projects on Matrix)
- Redundancy if raspby1 is temporarily unreachable (messages delivered when it reconnects)

To enable in a later phase:
1. Register a public domain (e.g., `matrix.resilience-hub.org`)
2. Point DNS to raspby1's public IP
3. Update `homeserver.yaml` `server_name` to the public domain
4. Remove `federation_domain_whitelist` restrictions
5. Run `federationtester.matrix.org` to verify
6. Update Element `config.json` with new `base_url`

**Note**: Changing `server_name` after initial deployment requires a full data migration. Lock in the final server name before Wave 1 if public federation is a Wave 2 requirement.

---

## Part 6: Matrix Client Configuration (Element Web)

The Element Web `config.json` (deployed at `/opt/community/nextcloud-matrix/element/config.json`) should be configured for the internal instance:

```json
{
    "default_server_config": {
        "m.homeserver": {
            "base_url": "https://100.70.184.84",
            "server_name": "resilience-hub.local"
        },
        "m.identity_server": {
            "base_url": "https://vector.im"
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
        "language": "en"
    },
    "show_labs_settings": false,
    "disable_custom_urls": true,
    "disable_guests": true,
    "analytics": {
        "disabled": true
    },
    "sso_redirect_options": {
        "immediate": false
    },
    "embedded": false,
    "welcome_user_id": "@admin:resilience-hub.local"
}
```

Key settings:
- `disable_custom_urls: true` — prevents authors from accidentally connecting to external Matrix servers
- `disable_guests: true` — guest access disabled; all users must log in
- `analytics.disabled: true` — no telemetry sent to Element/Vector
- `welcome_user_id` — admin sends a welcome DM when authors first log in

---

## Part 7: Nextcloud Text — Collaborative Document Templates

For each domain folder, create a template document to orient authors:

```bash
# Template document content (write one per domain)
cat > /tmp/domain1_template.md << 'EOF'
# Domain 1: Governance and Decision-Making
## Phase 5 Wave 1 — Article Template

**Author(s)**: [Your name]
**Draft due**: June 30, 2026
**Peer review due**: July 15, 2026
**Word count target**: 3,000–6,000 words
**License**: CC BY-SA 4.0

---

## Abstract (150–200 words)
[Brief summary of your article's argument and contribution]

---

## Introduction
[Context, problem statement, and scope]

---

## Main Body
### Section 1
### Section 2
### Section 3

---

## Practical Implications
[What should practitioners do? What communities is this relevant to?]

---

## References
[Citation list — use consistent format]

---

## Revision History
| Date | Author | Change |
|------|--------|--------|
| | | First draft |
EOF

# Upload to each domain folder via WebDAV
ADMIN_PASS=$(grep NEXTCLOUD_ADMIN_PASSWORD /opt/community/nextcloud-matrix/.env | cut -d= -f2)
curl -sk -u "admin:$ADMIN_PASS" \
  -T /tmp/domain1_template.md \
  "https://100.70.184.84/remote.php/dav/files/admin/Phase5_Wave1/Domain1_Governance/Article_Template.md"
```

---

## Configuration Summary Checklist

- [ ] Shared editorial calendar created and shared with `authors` group
- [ ] CalDAV URL documented and tested
- [ ] Wave 1 author contact list (CardDAV) created
- [ ] Groups created: `authors`, `domain-1` through `domain-5`, `editors`, `reviewers`
- [ ] Folder structure created with correct permissions
- [ ] Domain folders shared with domain groups (read+write)
- [ ] `_Administration/Author_Guides/` shared read-only with authors
- [ ] Matrix Space created: "Phase 5 — Resilience Corpus"
- [ ] All 10 rooms created and linked to Space
- [ ] Author accounts assigned to groups and rooms (assign_authors.sh run)
- [ ] Element config.json deployed with `disable_custom_urls: true`
- [ ] Article templates uploaded to each domain folder
- [ ] Federation set to internal-only for Wave 1

---

**Status**: PRODUCTION-READY — apply during deployment Stage 8 (after containers healthy, before author onboarding)  
**Time to apply**: Approximately 45–60 minutes for all configuration steps  
**Prerequisite**: All containers healthy, admin accounts created (PHASE_5_DEPLOYMENT_SCRIPTS_NEXTCLOUD_MATRIX.md Stages 6–8 complete)
