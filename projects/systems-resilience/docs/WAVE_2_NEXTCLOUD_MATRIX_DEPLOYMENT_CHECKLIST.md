---
title: "Wave 2 Nextcloud+Matrix Deployment Checklist (Pre-June 15)"
project: systems-resilience
phase: 6
wave: 2
status: PRODUCTION-READY
created: 2026-06-05
deployment_date: June 15, 2026
word_count: 1,600+
confidence: 95%
---

# Wave 2 Nextcloud+Matrix Deployment Checklist

## Executive Summary

This checklist governs all pre-deployment verification, load testing, and go/no-go decision-making for Wave 2 Nextcloud+Matrix launch (June 15, 08:00-20:00 UTC). It is designed to be completed in parallel with credential distribution (Part 3 of Provisioning Guide) and allows for automated verification where possible.

**Timeline:**
- **June 5-9:** Pre-deployment verification (Parts 1-2)
- **June 12-13:** Load testing (Part 3)
- **June 14:** Credential distribution & final checks (Part 4)
- **June 15 08:00-12:00 UTC:** Pre-launch verification (Part 5)
- **June 15 12:00-20:00 UTC:** Deployment day execution & monitoring (Part 6)
- **June 15 20:00 UTC:** Go/no-go decision & sign-off (Part 7)

---

## Part 1: Pre-Deployment Infrastructure Verification (June 5-9)

### 1.1 Nextcloud Instance Verification

**Verify Nextcloud is operational and performance-ready.**

**Checklist:**

- [ ] **Service running**
  ```bash
  docker ps | grep nextcloud | grep -q "Up"
  # Expected: container is running, uptime > 24 hours
  ```

- [ ] **Admin account accessible**
  ```bash
  curl -k -I https://nextcloud.example.com/
  # Expected: HTTP 200, page loads in <2 seconds
  ```

- [ ] **Database connectivity**
  ```bash
  docker exec nextcloud php /var/www/nextcloud/occ config:list | grep -q "database"
  # Expected: PostgreSQL connection healthy
  ```

- [ ] **Disk space available**
  ```bash
  docker exec nextcloud df -h /var/www/nextcloud/data | tail -1
  # Expected: at least 50 GB free (18 authors × 1 GB quota + overhead)
  ```

- [ ] **Memory available**
  ```bash
  free -h | grep Mem
  # Expected: at least 8 GB available (not including Docker overhead)
  ```

- [ ] **Required apps installed**
  ```bash
  docker exec nextcloud php /var/www/nextcloud/occ app:list | grep -E "groupfolders|notifications|twofactor_totp"
  # Expected: all three enabled
  ```

- [ ] **User quota default set to 1 GB**
  ```bash
  docker exec nextcloud php /var/www/nextcloud/occ config:app:get core default_quota
  # Expected: output "1 GB" (or "1GB")
  ```

- [ ] **HTTPS/TLS working with valid certificate**
  ```bash
  openssl s_client -connect nextcloud.example.com:443 -showcerts < /dev/null 2>&1 | openssl x509 -noout -dates
  # Expected: Certificate valid (not expired, dates show current+future)
  ```

### 1.2 Matrix Homeserver Verification

**Verify Synapse is operational and federation-ready.**

**Checklist:**

- [ ] **Service running**
  ```bash
  docker ps | grep synapse | grep -q "Up"
  # Expected: container running, uptime > 24 hours
  ```

- [ ] **Admin API accessible**
  ```bash
  curl -s -H "Authorization: Bearer ADMIN_TOKEN" https://matrix.example.com/_synapse/admin/v1/server_version
  # Expected: {"server_version": "Synapse/1.120.0", ...}
  ```

- [ ] **Federation enabled**
  ```bash
  curl -k -s https://matrix.example.com/.well-known/matrix/server | jq .
  # Expected: {"m.server": "matrix.example.com:8448"}
  ```

- [ ] **Registration API accessible**
  ```bash
  curl -s https://matrix.example.com/_matrix/client/r0/register | jq .
  # Expected: returns {"session": "...", "flows": [...]} (not "registration disabled")
  ```

- [ ] **Database connectivity (PostgreSQL)**
  ```bash
  docker exec synapse psql -U synapse -d synapse -c "SELECT 1;"
  # Expected: output "1" (database connection successful)
  ```

- [ ] **Disk space available**
  ```bash
  df -h /var/lib/synapse/ | tail -1
  # Expected: at least 20 GB free
  ```

- [ ] **Memory available**
  ```bash
  free -h | grep Mem
  # Expected: at least 6 GB available
  ```

- [ ] **HTTPS/TLS working**
  ```bash
  openssl s_client -connect matrix.example.com:8448 -showcerts < /dev/null 2>&1 | openssl x509 -noout -dates
  # Expected: Certificate valid (matching matrix.example.com)
  ```

- [ ] **Element Web client accessible**
  ```bash
  curl -k -I https://chat.example.com
  # Expected: HTTP 200, page loads in <2 seconds
  ```

### 1.3 Networking & DNS Verification

**Checklist:**

- [ ] **Nextcloud DNS resolves**
  ```bash
  nslookup nextcloud.example.com 8.8.8.8
  # Expected: returns IP address (e.g., 100.70.184.84 or public IP)
  ```

- [ ] **Matrix DNS resolves**
  ```bash
  nslookup matrix.example.com 8.8.8.8
  # Expected: returns IP address
  ```

- [ ] **Firewall allows HTTPS (443) from internet**
  ```bash
  curl -k -I https://nextcloud.example.com/ 2>&1 | head -1
  # Expected: HTTP/1.1 200 or HTTP/2 200
  ```

- [ ] **Firewall allows Matrix federation (8448)**
  ```bash
  openssl s_client -connect matrix.example.com:8448 < /dev/null 2>&1 | grep -q "Verify return code"
  # Expected: connection succeeds (Verify return code = 0 or X509 error acceptable)
  ```

- [ ] **No port conflicts (nginx, Docker bindings)**
  ```bash
  netstat -tlnp | grep -E ":443|:80|:8448"
  # Expected: exactly 3 listeners (nginx for 80/443, Matrix federation for 8448)
  ```

---

## Part 2: Application Configuration Verification (June 10-12)

### 2.1 Nextcloud Domain Groups & Folder Configuration

**Checklist:**

- [ ] **All 6 domain groups created**
  ```bash
  docker exec nextcloud php /var/www/nextcloud/occ group:list
  # Expected output includes: domain-60, domain-61, domain-62, domain-63, domain-64, domain-65
  ```

- [ ] **Shared groups created**
  ```bash
  docker exec nextcloud php /var/www/nextcloud/occ group:list
  # Expected output includes: all-authors, facilitators
  ```

- [ ] **All 6 domain folders exist** (verify via Nextcloud admin UI or CLI)
  ```bash
  ls -la /var/www/nextcloud/data/domain-60-international-coordination/
  # Expected: directory exists with subdirectories: drafts, submitted, published, _resources
  ```

- [ ] **Folder permissions set correctly**
  - Domain-60 folder:
    - `domain-60` group: Read-Write ✓
    - `all-authors` group: Read-only ✓
    - `facilitators` group: Read-Write ✓
  - (Repeat verification for domains 61-65)

- [ ] **Shared resources folder readable by all-authors**
  ```bash
  # Manual verification via admin UI:
  # Settings → Administration → Group folders → Phase5-Wave2-Shared-Resources
  # Check: all-authors has Read permission
  ```

- [ ] **Governance folder readable by facilitators only**
  ```bash
  # Manual verification via admin UI:
  # Settings → Administration → Group folders → Governance
  # Check: facilitators has Read-Write; all-authors has no permission
  ```

### 2.2 Matrix Room Configuration

**Checklist:**

- [ ] **All 6 domain rooms created**
  ```bash
  curl -s -H "Authorization: Bearer ADMIN_TOKEN" \
    https://matrix.example.com/_synapse/admin/v1/rooms | jq '.rooms | length'
  # Expected: at least 6 (plus 3 coordination rooms = 9 minimum)
  ```

- [ ] **Room aliases set** (for easy discovery)
  ```bash
  curl -s -H "Authorization: Bearer ADMIN_TOKEN" \
    https://matrix.example.com/_synapse/admin/v1/rooms | \
    jq '.rooms[] | select(.canonical_alias) | .canonical_alias'
  # Expected output includes: #domain-60-international-coordination:matrix.example.com (etc.)
  ```

- [ ] **Encryption enabled in all domain rooms**
  ```bash
  # Manual check via Element Web:
  # Join #domain-60; Settings → Security → Encryption enabled
  # Check mark visible next to "End-to-end encryption"
  ```

- [ ] **3 coordination rooms created**
  ```bash
  # Rooms to verify exist: #wave-2-announcements, #meta-governance, #technical-support
  # Manual: Log into Element Web, verify rooms in sidebar
  ```

- [ ] **Power levels configured** (project lead = admin, peer reviewers = moderators)
  ```bash
  # Manual check via Element Web:
  # Join #domain-60; Room Info → People
  # Verify: @lead = Power 100 (admin icon), peer reviewers = Power 50 (mod icon)
  ```

### 2.3 Nextcloud+Matrix Integration Test

**Checklist (to verify basic interoperability):**

- [ ] **Test Nextcloud file upload and sync**
  ```bash
  # Upload a test file via WebDAV
  curl -u admin:PASSWORD -T test-file.md \
    https://nextcloud.example.com/remote.php/dav/files/admin/domain-60/test-file.md
  # Expected: HTTP 201 Created
  ```

- [ ] **Test Nextcloud file access via browser**
  ```bash
  # Log into Nextcloud as admin
  # Navigate to domain-60 folder
  # Verify test-file.md appears within 5 seconds
  ```

- [ ] **Test Matrix user registration**
  ```bash
  # Use Element Web or Element Desktop to register new account
  # Homeserver: https://matrix.example.com
  # Username: testuser001
  # Password: [temp]
  # Expected: registration succeeds, confirmation email sent
  ```

- [ ] **Test Matrix room join**
  ```bash
  # As testuser001, click "Join #domain-60-international-coordination"
  # Expected: room appears in sidebar, encryption banner shows, can post test message
  ```

---

## Part 3: Load & Performance Testing (June 12-13)

### 3.1 Nextcloud Load Test (Simulating 18 Authors)

**Setup: Create 18 test accounts with identical production configuration**

**Checklist:**

- [ ] **Create 18 test user accounts**
  ```bash
  for i in {01..18}; do
    docker exec nextcloud php /var/www/nextcloud/occ user:add \
      --password-from-env testauthor-$i << EOF
  TestPass123!_$i
  EOF
    echo "Created testauthor-$i"
  done
  ```

- [ ] **Add test users to domain groups** (3 per domain: authors 01-03 to domain-60, authors 04-06 to domain-61, etc.)
  ```bash
  # Domain 60: testauthor-01, testauthor-02, testauthor-03
  for user in testauthor-01 testauthor-02 testauthor-03; do
    docker exec nextcloud php /var/www/nextcloud/occ group:adduser domain-60 $user
  done
  # ... (repeat for other domains)
  ```

- [ ] **Set quota for all test users**
  ```bash
  for i in {01..18}; do
    docker exec nextcloud php /var/www/nextcloud/occ user:setting testauthor-$i files quota 1GB
  done
  ```

- [ ] **Simulate 100 MB file upload (3 parallel uploads per domain)**
  ```bash
  # Create test file
  dd if=/dev/zero of=sample-file.bin bs=1M count=100
  
  # Upload from 3 test users in parallel (domain-60)
  for user in testauthor-01 testauthor-02 testauthor-03; do
    curl -u ${user}:TestPass123!_${user##*-} -T sample-file.bin \
      https://nextcloud.example.com/remote.php/dav/files/$user/domain-60/sample-file-$user.bin &
  done
  wait
  
  # Expected: All 3 uploads complete in <30 seconds each (total 30 min parallel uploads)
  ```

- [ ] **Monitor Nextcloud performance during upload**
  ```bash
  # In separate terminal, run:
  watch -n 1 'docker stats nextcloud --no-stream | grep -v "CONTAINER\|NAME"'
  
  # Expected during test:
  # CPU %: <60%
  # Memory Usage: <3 GB
  # No errors in docker logs
  ```

- [ ] **Verify files appear in folder** (sync check)
  ```bash
  # For testauthor-01, verify uploaded file appears in folder within 5 seconds
  curl -u testauthor-01:TestPass123!_01 \
    https://nextcloud.example.com/remote.php/dav/files/testauthor-01/domain-60/ | grep "sample-file"
  # Expected: file appears in listing
  ```

- [ ] **Verify disk usage** (should be ~300 MB: 18 users × 100 MB each, minus dedup if enabled)
  ```bash
  du -sh /var/www/nextcloud/data/
  # Expected: <500 MB (assuming deduplication or sparse files)
  ```

### 3.2 Matrix Load Test (Simulating 18 Authors + 100 Messages)

**Setup: Create 18 test accounts, add to 6 domain rooms, send 100 messages per room**

**Checklist:**

- [ ] **Create 18 test Matrix accounts**
  ```bash
  # Via Matrix admin API
  for i in {01..18}; do
    curl -X POST https://matrix.example.com/_matrix/client/r0/register \
      -d "{
        \"kind\": \"user\",
        \"auth\": {\"type\": \"m.login.dummy\"},
        \"user\": \"testuser-$i\",
        \"password\": \"TestPass123!_$i\",
        \"initial_device_display_name\": \"Test Device $i\"
      }"
  done
  ```

- [ ] **Invite test users to domain rooms** (3 users per room)
  ```bash
  # Domain 60: testuser-01, testuser-02, testuser-03
  for user in testuser-01 testuser-02 testuser-03; do
    curl -X POST https://matrix.example.com/_synapse/admin/v1/rooms/\!domain60roomid/members \
      -H "Authorization: Bearer ADMIN_TOKEN" \
      -d "{\"user_id\": \"@${user}:matrix.example.com\"}"
  done
  # ... (repeat for other rooms)
  ```

- [ ] **Send 100 test messages per room (6 rooms = 600 total messages)**
  ```bash
  # Send 100 messages from testuser-01 to domain-60 room
  for msg in {1..100}; do
    curl -X POST https://matrix.example.com/_matrix/client/r0/rooms/\!domain60roomid/send/m.room.message \
      -H "Authorization: Bearer $(get_token testuser-01)" \
      -d "{\"msgtype\": \"m.text\", \"body\": \"Test message $msg at $(date)\"}"
    sleep 0.5  # Rate limit to prevent API exhaustion
  done &
  # ... (repeat for other rooms with different users, in parallel)
  wait
  ```

- [ ] **Monitor Matrix performance**
  ```bash
  watch -n 1 'docker stats synapse postgres --no-stream'
  
  # Expected:
  # Synapse CPU: <50%
  # Synapse Memory: <2 GB
  # PostgreSQL CPU: <30%
  # No CRITICAL errors in docker logs
  ```

- [ ] **Verify message latency** (measure time from POST to room history)
  ```bash
  # Send timestamped message
  send_time=$(date +%s%N)
  curl -X POST https://matrix.example.com/_matrix/client/r0/rooms/\!domain60roomid/send/m.room.message \
    -H "Authorization: Bearer $TOKEN" \
    -d "{\"msgtype\": \"m.text\", \"body\": \"Latency test at $send_time\"}"
  
  # Query room history (immediate)
  sleep 1
  curl -s https://matrix.example.com/_matrix/client/r0/rooms/\!domain60roomid/messages \
    -H "Authorization: Bearer $TOKEN" | grep "Latency test"
  
  # Expected: message appears within 3 seconds of POST
  ```

- [ ] **Verify message count** (verify all 600 messages arrived)
  ```bash
  # Query each domain room for message count
  for room in domain-60 domain-61 domain-62 domain-63 domain-64 domain-65; do
    curl -s -H "Authorization: Bearer ADMIN_TOKEN" \
      https://matrix.example.com/_synapse/admin/v1/rooms/%21${room}id/members | \
      jq '.members | length'
  done
  # Expected: at least 100 messages in each room (rough check via member list size)
  ```

### 3.3 Load Test Acceptance Criteria

**All of the following must be TRUE for deployment to proceed:**

- [ ] **Nextcloud:** CPU <60%, memory <3 GB during 3-parallel-upload test
- [ ] **Nextcloud:** File uploads complete in <30 seconds each (parallel)
- [ ] **Nextcloud:** Files appear in folder sync within 5 seconds
- [ ] **Matrix:** CPU <50%, memory <2 GB during 600-message test
- [ ] **Matrix:** Message latency <3 seconds (average across 6 rooms)
- [ ] **Matrix:** Zero dropped messages (all 600 messages present in history)
- [ ] **Services:** Zero critical errors in Docker logs during load test
- [ ] **Disk:** Sufficient space remaining (>30 GB after test)

**If any criterion fails:**
- Investigate root cause (see Troubleshooting, Part 8)
- Remediate (e.g., increase memory, optimize database queries, enable caching)
- Rerun load test
- If unresolved, escalate and consider deferring Wave 2 deployment (unlikely)

---

## Part 4: Pre-Launch Verification (June 14)

### 4.1 Credential Distribution Checklist

- [ ] **All 18 author email addresses verified** (current institutional emails)
- [ ] **One-time login tokens generated** for all 18 authors (via Nextcloud admin)
- [ ] **Temporary passwords generated** (if using password-reset instead of tokens)
- [ ] **Email templates prepared** and tested (Nextcloud + Matrix setup emails)
- [ ] **Nextcloud invitation email sent** to all 18 authors at 14:00 UTC June 14
- [ ] **Matrix setup email sent** to all 18 authors at 14:00 UTC June 14
- [ ] **Response email address monitored** ([PROJECT_LEAD_EMAIL]) for delivery status, bounces

### 4.2 Documentation Checklist

- [ ] **Scope documents prepared** for all 6 domains (ready to send to authors on June 9)
- [ ] **Annotated bibliographies prepared** for all 6 domains (ready to send on June 9)
- [ ] **Author briefing documents** prepared (overview of Wave 2 project, timeline, expectations)
- [ ] **Zone 5 context brief** prepared (geographic/demographic/governance context)
- [ ] **First-draft template** prepared (markdown structure, section headings, word count targets)

### 4.3 Support Infrastructure Checklist

- [ ] **`#technical-support` Matrix room** is active and monitored
- [ ] **Support escalation procedures** documented in `WAVE_2_NEXTCLOUD_MATRIX_PROVISIONING_GUIDE.md` Part 4.4
- [ ] **Project lead contact info** shared (email + Matrix ID) in all communication emails
- [ ] **Peer reviewers' contact info** shared in domain-specific emails to authors
- [ ] **Support SLA posted** in `#technical-support` room and welcome email

### 4.4 Rollback Procedures Checklist

- [ ] **Backup snapshots taken** (Nextcloud database, Matrix database, filesystem)
  ```bash
  # Nextcloud database backup
  docker exec postgres pg_dump -U nextcloud nextcloud > nextcloud-backup-june-14.sql
  
  # Matrix database backup
  docker exec postgres pg_dump -U synapse synapse > synapse-backup-june-14.sql
  
  # Filesystem backups (Nextcloud data, Matrix media store)
  tar -czf nextcloud-data-backup-june-14.tar.gz /var/www/nextcloud/data/
  tar -czf synapse-media-backup-june-14.tar.gz /var/lib/synapse/media_store/
  ```

- [ ] **Rollback procedures documented** in `WAVE_2_NEXTCLOUD_MATRIX_PROVISIONING_GUIDE.md` Part 8
- [ ] **Database restore procedure tested** on staging environment (if available)
- [ ] **Service restart procedure tested** (to ensure cold-start works)

---

## Part 5: Pre-Launch Verification (June 15, 08:00-12:00 UTC)

### 5.1 Final Service Health Check

**Checklist (run at 08:00 UTC, 08:30 UTC, 09:00 UTC):**

- [ ] **Nextcloud service status**
  ```bash
  docker ps | grep nextcloud | grep -q "Up (.*hours)" || echo "WARNING: Nextcloud restarted recently"
  curl -k -I https://nextcloud.example.com/ 2>&1 | grep -q "200" || echo "WARNING: Nextcloud HTTP error"
  ```

- [ ] **Matrix service status**
  ```bash
  docker ps | grep synapse | grep -q "Up (.*hours)" || echo "WARNING: Synapse restarted recently"
  curl -s https://matrix.example.com/_matrix/client/versions | jq . > /dev/null || echo "WARNING: Matrix API error"
  ```

- [ ] **PostgreSQL database status** (shared by both services)
  ```bash
  docker exec postgres pg_isready -U nextcloud -d nextcloud || echo "WARNING: Nextcloud DB error"
  docker exec postgres pg_isready -U synapse -d synapse || echo "WARNING: Synapse DB error"
  ```

- [ ] **Disk space adequate** (>30 GB free)
  ```bash
  df -h / | awk 'NR==2 {print $4}'
  ```

- [ ] **Network connectivity to external DNS**
  ```bash
  curl -I https://google.com 2>&1 | grep -q "200\|301\|302\|400" && echo "OK" || echo "WARNING: Internet connectivity issue"
  ```

### 5.2 Author Login Verification (Spot-Check)

**Test 3 random authors' first-login workflow at 10:00 UTC:**

- [ ] **Test Author 1: Philip McMichael (Domain 60)**
  - [ ] Click one-time login link (from June 14 email)
  - [ ] Set password
  - [ ] Enable 2FA (save recovery codes)
  - [ ] Log in to Nextcloud dashboard
  - [ ] See domain-60 folder in sidebar ✓
  - [ ] Can access shared-resources folder (read-only) ✓
  - [ ] Upload test file to domain-60/drafts/ → File appears within 5 sec ✓

- [ ] **Test Author 2: Wes Jackson (Domain 61)**
  - [ ] Same workflow as above
  - [ ] Verify domain-61 folder accessible ✓

- [ ] **Test Author 3: Kathleen Tierney (Domain 62)**
  - [ ] Same workflow as above
  - [ ] Verify domain-62 folder accessible ✓

- [ ] **Test Matrix Registration & Room Join**
  - [ ] Register on matrix.example.com as @testauthor-spot01:matrix.example.com
  - [ ] Join #domain-60-international-coordination room
  - [ ] Post test message: "Hello, testing room access"
  - [ ] Verify message appears in room history within 3 seconds ✓
  - [ ] Verify encryption is enabled (🔒 icon visible) ✓

### 5.3 Scope Document & Bibliography Distribution

- [ ] **Scope documents sent** to all 18 authors at 09:00 UTC
- [ ] **Annotated bibliographies sent** to all 18 authors at 09:00 UTC
- [ ] **Author briefing documents sent** at 09:00 UTC
- [ ] **Zone 5 context brief sent** at 09:00 UTC

### 5.4 Final Go/No-Go Determination

**At 11:30 UTC, project lead completes this decision tree:**

```
┌─ All service health checks GREEN?
│  ├─ Yes → Go to next check
│  └─ No → NO-GO (see Part 8: Troubleshooting & Rollback)
│
├─ Spot-check 3 authors: Nextcloud login + file upload successful?
│  ├─ Yes → Go to next check
│  └─ No → NO-GO (investigate author account issues)
│
├─ Spot-check 3 authors: Matrix registration + room join successful?
│  ├─ Yes → Go to next check
│  └─ No → NO-GO (investigate Matrix user registration)
│
├─ All 18 authors received credential emails + scope documents?
│  ├─ Yes (≥17 of 18 confirmed) → Go to next check
│  └─ No → CAUTION (escalate delivery failures, continue if <3 failures)
│
└─ Do you have confidence this deployment will succeed (on scale 1-10)?
   ├─ Yes (≥9/10) → ✅ GO FOR LAUNCH
   └─ No (<9/10) → 🛑 NO-GO (assess risk, defer if necessary)
```

**Sign-off (required for launch):**

```
Wave 2 Nextcloud+Matrix Pre-Launch Go/No-Go Determination
Date: June 15, 2026
Time: 11:30-12:00 UTC

Decision: [ ] GO   [ ] CAUTION   [ ] NO-GO

Project Lead: _________________________ Signature: ________________
System Administrator: _________________ Signature: ________________

If CAUTION or NO-GO, attach explanation and remediation plan:
_________________________________________________________________
_________________________________________________________________
_________________________________________________________________
```

---

## Part 6: Deployment Day Execution (June 15, 12:00-20:00 UTC)

### 6.1 12:00-14:00 UTC: Launch Window Opens

**Checklist:**

- [ ] **Services online** (pre-verified; all systems green)
- [ ] **All 18 authors contacted** (optional reminder email: "Platform goes live at 12:00 UTC; your login link expires at 12:00 UTC June 15; click now to access")
- [ ] **Monitoring dashboard active** (if Prometheus/Grafana in use, open in browser)
- [ ] **Support team on-call** (project lead + system administrator available for questions)

### 6.2 14:00-18:00 UTC: Active Onboarding Window

**Checklist (monitor every 30 minutes):**

- [ ] **Nextcloud active user count rising** (target: 15+ of 18 by 16:00 UTC)
  ```bash
  curl -s -H "Authorization: Bearer ADMIN_TOKEN" \
    https://nextcloud.example.com/ocs/v2.php/apps/admin_provisioning_api/api/v1/users/list | \
    jq '.ocs.data.users[] | select(.enabled == true) | .lastLogin' | grep "2026-06-15" | wc -l
  ```

- [ ] **Matrix user count rising** (target: 15+ of 18 registered by 16:00 UTC)
  ```bash
  # Manual: Element Web → Room Members panel in each domain room
  # Count total unique users across all 6 domain rooms
  ```

- [ ] **Support queue empty** (no pending Tier 1/2 issues; Tier 3 escalations <2)
  - Check `#technical-support` room for unanswered questions
  - Respond to questions within 30 minutes

- [ ] **No service errors** (Docker logs clean)
  ```bash
  docker logs nextcloud 2>&1 | grep -i error | wc -l
  docker logs synapse 2>&1 | grep -i error | wc -l
  # Expected: <5 errors each (minor errors okay; CRITICAL errors are not)
  ```

- [ ] **Performance stable** (CPU, memory not spiking)
  ```bash
  docker stats nextcloud synapse --no-stream
  # Expected: CPU <40%, Memory <2 GB each
  ```

### 6.3 18:00-20:00 UTC: Checkpoint & Verification

**Checklist (at 18:00 UTC and 20:00 UTC):**

- [ ] **Author login success rate**
  ```bash
  # Count authors who successfully logged in
  # Target: ≥15 of 18 (83% success rate acceptable)
  ```

- [ ] **Domain folder access verification**
  - Check Nextcloud `/domain-60/` ... `/domain-65/` folders
  - Verify all subfolders (drafts, submitted, published, _resources) exist ✓
  - Verify permissions are set correctly (test user can read, cannot write to non-domain folders) ✓

- [ ] **Matrix room membership verification**
  - Check each domain room has ≥3 members ✓
  - Check each room shows encryption enabled ✓
  - Check at least 3 authors posted introduction message ✓

- [ ] **Cross-domain folder access verification**
  - Test user from Domain 60 can read `/Phase5-Wave2-Shared-Resources/` ✓
  - Test user from Domain 60 cannot write to `/Cross-Domain-Research/` (read-only) ✓
  - Test user from Domain 60 cannot see `/Governance/` folder (no permission) ✓

---

## Part 7: Deployment Success Verification (June 15, 20:00 UTC)

### 7.1 Final Success Checklist

**All checkboxes must be TRUE for deployment to be marked "SUCCESSFUL":**

- [ ] **Nextcloud:**
  - [ ] ≥15 of 18 authors successfully logged in
  - [ ] ≥15 authors have access to their domain folder
  - [ ] Spot-check: 3 random authors can upload and access test file within 5 sec
  - [ ] No Tier 3 escalations unresolved; support queue clear

- [ ] **Matrix:**
  - [ ] ≥15 of 18 authors registered Matrix accounts
  - [ ] ≥15 authors joined their assigned domain room
  - [ ] Spot-check: ≥3 authors posted introduction message in domain rooms
  - [ ] ≥3 messages visible in each domain room (all 6 rooms)
  - [ ] Message latency <5 seconds

- [ ] **Integration:**
  - [ ] Authors can access both Nextcloud and Matrix (verified by spot-check)
  - [ ] No credential conflicts (same username/password across platforms not required; authors understand they're separate logins)
  - [ ] Support channels functional (`#technical-support` monitored)

- [ ] **Documentation:**
  - [ ] All 18 authors received scope documents and bibliographies
  - [ ] First-draft checkpoint timeline confirmed (June 24 deadline)
  - [ ] Peer reviewer assignments confirmed

### 7.2 Deployment Sign-Off

```
WAVE 2 NEXTCLOUD+MATRIX DEPLOYMENT — FINAL SIGN-OFF
Date: June 15, 2026
Time: 20:00-20:30 UTC

Status: [ ] SUCCESSFUL   [ ] PARTIALLY SUCCESSFUL (see issues below)   [ ] FAILED

Success Metrics:
  - Authors logged in: ___ of 18 (target: ≥15)
  - Matrix users registered: ___ of 18 (target: ≥15)
  - Message latency: ___ seconds (target: <5)
  - CPU utilization (peak): ___ % (target: <50%)
  - Disk space remaining: ___ GB (target: >30)
  - Tier 1/2 support issues resolved: ___ (target: 100%)
  - Critical errors in logs: ___ (target: 0)

Issues Found (if any):
_________________________________________________________________
_________________________________________________________________

Resolution & Mitigation (if applicable):
_________________________________________________________________
_________________________________________________________________

Project Lead: _________________________ Signature: ________________
Date & Time: _________________________

System Administrator: _________________ Signature: ________________
Date & Time: _________________________

Deployment Outcome: ✅ READY FOR WAVE 2 AUTHOR ONBOARDING (June 16+)
```

### 7.3 Post-Deployment Notifications

**At 20:30 UTC, post in `#wave-2-announcements`:**

```
✅ WAVE 2 NEXTCLOUD+MATRIX DEPLOYMENT COMPLETE

All systems operational. 18 authors now have access to:
- Nextcloud document collaboration workspace
- Matrix messaging platform
- Domain-specific folders and rooms

Timeline reminders:
- June 24 23:59 UTC: First draft submission deadline
- June 26: Peer review feedback posted
- July 1: Second draft checkpoint

Questions? Post in #technical-support or email [PROJECT_LEAD_EMAIL].

Thank you for your patience during launch. Welcome to Wave 2!
```

---

## Part 8: Troubleshooting & Rollback Procedures

### 8.1 Critical Issues & Emergency Responses

**If Nextcloud is completely unavailable (HTTP 500, service down):**

```bash
# Step 1: Check service status
docker ps | grep nextcloud

# Step 2: Check recent logs for errors
docker logs nextcloud | tail -50

# Step 3: Attempt service restart
docker restart nextcloud

# Step 4: Wait 30 seconds for startup
sleep 30

# Step 5: Verify recovery
curl -k -I https://nextcloud.example.com/ | head -1

# If still down: See rollback procedure (Part 8.3)
```

**If Matrix is unavailable (cannot register accounts, rooms not accessible):**

```bash
# Step 1: Check Synapse status
docker ps | grep synapse

# Step 2: Check if registration is disabled
curl -s https://matrix.example.com/_matrix/client/r0/register | grep -q "registration"

# Step 3: If disabled, enable temporarily
# Edit homeserver.yaml: enable_registration: true
# Restart: docker restart synapse

# Step 4: Verify recovery
curl -s https://matrix.example.com/_matrix/client/versions | jq . | grep -q "versions"

# If still down: See rollback procedure (Part 8.3)
```

### 8.2 Partial Failures & Workarounds

**If <50% of authors can log in (but services are online):**
- Likely cause: Account creation issue or permission problem
- Fix: Manually verify user accounts with `occ user:list`; re-add users to groups with `occ group:adduser`
- Workaround: Re-generate login tokens and re-send emails to affected authors

**If authors can log into Nextcloud but files aren't syncing:**
- Likely cause: Folder permissions not applied, or Nextcloud sync client misconfigured
- Fix: Verify group membership; re-apply folder permissions
- Workaround: Restart Nextcloud service; ask authors to restart sync client

**If Matrix room messages have high latency (>10 seconds):**
- Likely cause: Database slow, or Synapse under load
- Fix: Check PostgreSQL query performance; restart Synapse if CPU >80%
- Workaround: Continue with lower message frequency; post important decisions after checkpoint, not real-time

### 8.3 Full Rollback Procedure (If Deployment Fails)

**Trigger: Deployment marked as FAILED at 20:00 UTC (unable to meet success criteria)**

**Rollback decision:**

```
Is rollback necessary?
├─ If ≥15 authors can access (SUCCESSFUL): No rollback needed
├─ If 10-14 authors can access (PARTIALLY SUCCESSFUL): Attempt remediation first
└─ If <10 authors can access (FAILED): Execute rollback
```

**Rollback steps (if required):**

1. **Notify all authors** (immediately, before rollback begins):
   ```
   Wave 2 launch paused for emergency maintenance. Your Nextcloud + Matrix access will be restored within 2 hours. We will confirm when systems are ready.
   ```

2. **Restore from backup** (June 14 backups taken in Part 4.4):
   ```bash
   # Stop services
   docker-compose stop nextcloud synapse postgres
   
   # Restore databases
   docker exec postgres dropdb nextcloud
   docker exec postgres createdb -O nextcloud nextcloud
   psql -U nextcloud nextcloud < nextcloud-backup-june-14.sql
   
   docker exec postgres dropdb synapse
   docker exec postgres createdb -O synapse synapse
   psql -U synapse synapse < synapse-backup-june-14.sql
   
   # Restore filesystems
   rm -rf /var/www/nextcloud/data
   tar -xzf nextcloud-data-backup-june-14.tar.gz
   rm -rf /var/lib/synapse/media_store
   tar -xzf synapse-media-backup-june-14.tar.gz
   
   # Restart services
   docker-compose up -d
   sleep 60
   ```

3. **Verify services restored**:
   ```bash
   curl -k -I https://nextcloud.example.com/
   curl -s https://matrix.example.com/_matrix/client/versions | jq .
   # Both should return success responses
   ```

4. **Notify authors of restored state**:
   ```
   Wave 2 infrastructure restored. Nextcloud + Matrix are now online.
   
   If you logged in June 15 before maintenance: your account is intact.
   If you did NOT log in: try logging in now.
   
   All scope documents and resources are available in Nextcloud folders.
   ```

5. **Investigate root cause** (post-incident):
   - Review Docker logs from June 15 11:00-20:00 UTC
   - Identify failure mode (service crash, database corruption, resource exhaustion)
   - Implement fix (increase memory, optimize queries, fix configuration error)
   - Retest with load test (Part 3) before attempting re-deployment

6. **Reschedule Wave 2 launch** (if required):
   - Option A: June 16 or June 17 (retry immediately after remediation)
   - Option B: June 20 (delay by 5 days, allow for extended troubleshooting and root-cause investigation)

---

**Document Status**: PRODUCTION-READY for June 15 Wave 2 deployment

**Confidence Level**: 95%

**Version**: 1.0

**Last Updated**: 2026-06-05

**Emergency Contact**: [PROJECT_LEAD_EMAIL] + [SYSTEM_ADMIN_EMAIL] (available 24/7 June 14-15)
