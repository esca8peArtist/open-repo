---
title: "Phase 5.1 Publication Rollback Procedure"
project: systems-resilience
phase: "5.1"
platform: "Discourse"
status: PRODUCTION-READY — activate only when rollback trigger conditions are met
created: 2026-06-10
publication_window: "2026-06-09 13:00–15:00 UTC"
rollback_activation: "Manual — see Rollback Trigger Conditions"
cross_references:
  - DISCOURSE_DEPLOYMENT_RUNBOOK.md
  - PHASE_5_1_PUBLICATION_OPERATIONAL_PROCEDURES.md
  - PHASE_5_1_CONTENT_READINESS.md
---

# Phase 5.1 Publication Rollback Procedure
## Failure Recovery — June 9, 2026 Publication Window

**This document is activated only when a rollback trigger condition is met (see Section 1). If in doubt, consult the decision tree before invoking a rollback — most issues do not require full rollback.**

**Key constraint**: Content source files in `/tmp/phase5-pub/` are the authoritative recovery source. They are verified as intact as of June 7, 2026 (PHASE_5_1_CONTENT_READINESS.md). Loss of content is not a concern — only platform availability is.

---

## Section 1: Rollback Trigger Conditions

A rollback is triggered when **any** of the following conditions occur during the June 9 13:00–15:00 UTC publication window:

| # | Condition | Threshold | Response |
|---|-----------|-----------|----------|
| R1 | Platform completely unreachable | HTTP non-200 for > 10 consecutive minutes after restart | Rollback to Nextcloud OR reschedule |
| R2 | Database corruption | PostgreSQL fails to start or returns data errors | Full rollback and restore from backup |
| R3 | All uploaded content inaccessible | Users cannot read any published topics | Diagnose; rollback if not resolved in 30 min |
| R4 | Security incident | Unauthorized modification of published content | Immediate rollback, platform audit |
| R5 | Network outage | Pi5 unreachable from Tailscale for > 20 minutes | Escalate; cannot remediate remotely |

**NOT rollback triggers** (these are partial failures — fix and continue):
- One topic fails to upload (re-upload that topic)
- Search indexing slow (non-blocking — content is still readable)
- PDF attachment fails (content is readable without PDF; attach later)
- Slow response times under 10 seconds (Pi5 under load — wait for Sidekiq to finish)
- YAML frontmatter visible in one topic (delete and re-upload that topic)

---

## Section 2: Downtime Impact Assessment

| Rollback Duration | Users Affected | Content Accessible | Recovery Path |
|------------------|-----------------|--------------------|---------------|
| < 30 minutes | Minor — publication delayed, not cancelled | No (during rollback) | Same-day republication by 16:00 UTC |
| 30–60 minutes | Moderate — 2-hour delay possible | No (during rollback) | Same-day republication by 17:00 UTC |
| 60–180 minutes | Significant — same-day publication at risk | No (during rollback) | Evening republication or June 10 shift |
| > 3 hours | June 9 deadline missed | No | Reschedule to June 10 08:00 UTC |

**Audience context**: Expected audience is 50–200 users from the author coalition and mailing list. These users are known; a delay notification via email is sufficient. There is no general public announcement that creates urgency beyond the commitment to author coalition members.

**Wave 2 impact**: Publication delay of < 24 hours does not affect Wave 2 recruitment timeline (starts June 14). A 48-hour delay (to June 11) creates minor scheduling tension but is manageable.

---

## Scenario A: Database Corruption

### Detection

```bash
# Signs of database corruption:
# 1. Discourse returns 500 errors on all requests
curl -sk -o /dev/null -w "%{http_code}" "https://100.120.18.84/about.json"
# Returns 500 or 503 (not 200)

# 2. PostgreSQL startup errors in logs
cd /var/discourse
sudo ./launcher logs app --tail 50 | grep -iE "postgres|pg|database|corrupt|error"
# Look for: FATAL, PANIC, relation "xxx" does not exist, corrupted page

# 3. Rails console fails
sudo ./launcher enter app
rails c
# Returns: PG::ConnectionBad: could not connect to server, or similar
```

**Immediate Action (first 5 minutes):**

```bash
# Step 1: Stop Discourse to prevent further writes
cd /var/discourse
sudo ./launcher stop app

# Step 2: Check PostgreSQL data directory integrity
sudo ./launcher enter app bash -c "
echo 'Checking PostgreSQL data directory...'
ls -lah /shared/postgres_data/
ls -lah /shared/postgres_data/global/pg_control 2>/dev/null && echo 'pg_control: OK' || echo 'pg_control: MISSING — severe corruption'
"

# Step 3: Identify most recent backup
ls -lth /var/discourse/shared/standalone/backups/default/
ls -lth /home/awank/backups/discourse/
# Use the most recent backup that predates the corruption
```

**Restoration:**

```bash
# Option A: Restore from Discourse built-in backup
# This is the preferred method as it handles schema migrations automatically

# Start Discourse in maintenance mode first
cd /var/discourse
sudo ./launcher start app

# Wait for Discourse to become partially available (may show errors)
sleep 30

# Restore via rails console
sudo ./launcher enter app
# Inside container:
backup_file="/shared/backups/default/REPLACE_WITH_BACKUP_FILENAME.tar.gz"
discourse restore "$backup_file"
# This will:
# 1. Drop the current database
# 2. Restore from backup
# 3. Run any pending migrations
# 4. Restart Discourse
exit
```

```bash
# Option B: If container won't start at all — restore PostgreSQL directly
# More complex; only use if Option A fails

# 1. Stop container completely
cd /var/discourse
sudo ./launcher stop app
sudo docker rm app 2>/dev/null || true

# 2. Backup corrupted data directory (don't overwrite — keep for forensics)
sudo mv /var/discourse/shared/standalone/postgres_data \
    /var/discourse/shared/standalone/postgres_data_corrupted_$(date +%Y%m%d%H%M)

# 3. Extract backup archive to restore postgres_data
latest_backup=$(ls -t /home/awank/backups/discourse/*/*.tar.gz 2>/dev/null | head -1)
if [[ -z "$latest_backup" ]]; then
    latest_backup=$(ls -t /var/discourse/shared/standalone/backups/default/*.tar.gz 2>/dev/null | head -1)
fi
echo "Restoring from: $latest_backup"

sudo mkdir -p /var/discourse/shared/standalone/postgres_data
sudo tar -xzf "$latest_backup" -C /var/discourse/shared/standalone/ --wildcards "*/db/postgres_data/*" 2>/dev/null || \
    echo "Archive does not contain raw postgres_data — must use Discourse restore command"

# 4. Re-bootstrap (this reinitializes the container with restored data)
sudo ./launcher bootstrap app

# 5. Start
sudo ./launcher start app
```

**Recovery Time Estimate**: 
- Option A (rails restore): 20–45 minutes (depends on backup size ~100MB)
- Option B (raw restore + bootstrap): 45–90 minutes (Pi5 bootstrap time)

**Communication:**

Within 5 minutes of detecting database corruption:

```
Email to author coalition:
Subject: Phase 5 publication delayed — brief technical issue

We're experiencing a brief technical issue with the publication platform.
All content is safe and intact. We expect to complete publication by [new time].
We'll send a confirmation when everything is live.
```

**Post-incident review:**

1. Determine what caused corruption: power loss during write? Docker OOM kill? SD card failure?
2. If SD card failure on Pi5: migrate to USB3 SSD immediately (see Pi5-specific notes in DISCOURSE_DEPLOYMENT_RUNBOOK.md)
3. Enable write-ahead log (WAL) archiving if not already active
4. Add UPS or graceful shutdown hook if power loss is suspected

**Prevention:**
- Run Discourse on SSD (not SD card) on Pi5
- Enable PostgreSQL WAL archiving to external storage
- Configure automatic shutdown on low power via UPS integration

---

## Scenario B: Platform Crash (Discourse Container Exits)

### Detection

```bash
# Container has stopped running
cd /var/discourse
sudo ./launcher status app
# Returns: "app: down" or "Error: no such object: app"

# Discourse not responding
curl -sk -o /dev/null -w "%{http_code}" "https://100.120.18.84/about.json"
# Returns: 000 (connection refused) or 502

# Check system journal for OOM or crash
sudo journalctl -u docker -n 50 --no-pager
# Look for: OOMKilled, segfault, SIGKILL
```

**Immediate Action (first 5 minutes):**

```bash
# Step 1: Attempt restart
cd /var/discourse
sudo ./launcher start app
sleep 60   # Discourse takes up to 2 min to start

# Check if it came back
sudo ./launcher status app
curl -sk -o /dev/null -w "%{http_code}" "https://100.120.18.84/about.json"
```

**If restart succeeds (HTTP 200 within 2 minutes):**
- Check logs for error cause: `sudo ./launcher logs app --tail 100`
- Identify if it was a transient error (OOM under load) or a recurring bug
- If transient OOM: continue publication at reduced pace (fewer concurrent API calls)
- Document the crash time and cause; continue publication

**If restart fails:**

```bash
# Step 2: Full launcher destroy and rebuild
sudo ./launcher destroy app
sudo ./launcher bootstrap app   # Pi5: ~20 minutes
sudo ./launcher start app
```

**Recovery Time Estimate:**
- Restart only: 2–5 minutes
- Destroy + bootstrap: 25–35 minutes on Pi5

**If platform crash occurs during publication (some topics already uploaded):**

Topics that were already uploaded before the crash are stored in PostgreSQL and survive a container restart. After recovery:

```bash
# Verify which topics survived
curl -sk "$DISCOURSE_URL/c/phase-5-published-research.json" | python3 -c "
import sys, json
d = json.load(sys.stdin)
topics = d.get('topic_list',{}).get('topics',[])
print(f'Topics in Phase 5 category: {len(topics)}')
for t in topics:
    print(f'  [{t[\"id\"]}] {t[\"title\"][:60]}')
"
# Compare against expected 6 topics
# Re-upload only the topics that are missing
```

**Communication:**

For crash duration < 15 minutes: no communication needed (resume and complete within window).

For crash duration 15–30 minutes:

```
Email: "Brief technical interruption resolved. Publication continuing. All documents will be live by [adjusted time]."
```

---

## Scenario C: Network Outage

### Detection

```bash
# Pi5 unreachable via Tailscale
ping -c 4 100.120.18.84
# Request timeout for all 4 pings

# Tailscale status from another device
tailscale status | grep raspby1
# Expected if offline: "raspby1 100.120.18.84 ... offline"
```

**Nature of network outage matters:**

**Case 1: Tailscale reconnection issue (Pi5 still running, just not reachable)**

```bash
# If you have physical access or another path to the Pi5:
ssh awank@raspby1.local   # LAN hostname if on same network

# Restart Tailscale
sudo tailscale down && sudo tailscale up

# Or restart tailscaled service
sudo systemctl restart tailscaled
sleep 10

# Verify Tailscale came back
tailscale status
```

**Case 2: Pi5 has lost all network connectivity (ISP outage, WiFi issue)**

This cannot be remediated remotely. Actions:

1. Wait up to 20 minutes — if the outage is a brief blip, Tailscale will reconnect automatically.
2. If outage persists at 20 minutes: invoke the June 10 reschedule (see Section F).
3. Send communication immediately (from a device not on the affected network).

**Recovery Time Estimate:**
- Tailscale reconnection: 2–5 minutes (if Pi5 is up and just dropped VPN)
- ISP outage: depends on ISP; outside operator control
- Total downtime before reschedule trigger: 20 minutes

**Communication:**

```
If outage > 20 minutes:
Subject: Phase 5 publication rescheduled — network issue

We've experienced an unexpected network interruption affecting our publishing platform.
All content is safe. We are rescheduling publication to:

June 10, 2026 at 10:00 UTC

We apologize for the delay. Wave 2 recruitment is not affected.
```

---

## Scenario D: Permission Errors (Users Cannot Access Content)

### Detection

```bash
# Users report they cannot read published topics
# Or: you verify anonymously that topics are blocked

# Test unauthenticated access
curl -sk "https://100.120.18.84/t/TOPIC_ID.json" | python3 -c "
import sys,json
d=json.load(sys.stdin)
if 'errors' in d:
    print('ACCESS DENIED:', d['errors'])
else:
    print('OK:', d.get('title','?'))
"
# If access denied: category permission is set incorrectly
```

**Immediate Action (first 5 minutes):**

```bash
# Check category permissions
cd /var/discourse
sudo ./launcher enter app
rails c

cat = Category.find_by(name: "Phase 5 — Published Research")
puts "Category permissions:"
cat.category_groups.each do |cg|
    group = cg.group
    level = cg.permission_type
    puts "  #{group&.name || 'everyone'}: #{level}"
end

# Permission type values:
# 1 = full (create, reply, see)
# 2 = create_post (reply only)
# 3 = readonly (see only)

# Fix: ensure everyone gets read access
cat.set_permissions({
    everyone: :readonly,      # type 3 — public read
    "phase5_authors" => :full, # type 1 — authors can post
    "staff" => :full
})
cat.save!
puts "Permissions corrected"

exit
```

**Verification after fix:**

```bash
# Test from unauthenticated curl
curl -sk "https://100.120.18.84/t/TOPIC_ID.json" | python3 -c "
import sys,json; d=json.load(sys.stdin); print('OK' if 'title' in d else 'STILL BLOCKED:', d)
"
```

**Recovery Time Estimate**: 5–10 minutes (permission fix is instant; verify immediately).

**Root cause**: This typically happens when category permissions are misconfigured during Phase 8 of deployment, or when a "must_approve_users" flag prevents anonymous read. Check `SiteSetting.login_required` — if set to `true`, all content requires login.

```bash
sudo ./launcher enter app
rails c
puts "Login required: #{SiteSetting.login_required}"
# If true: set to false for public read
SiteSetting.login_required = false
puts "Fixed: login no longer required for reading"
exit
```

**Prevention**: Always test anonymous read access during Phase 10 of deployment (June 8 verification), not just API-authenticated access.

---

## Scenario E: Citation Link 404s

### Detection

```bash
# Users report that citation links in documents return 404 or are broken
# This is most likely to occur in the Integrated Corpus (most citations)

# Quick check: count how many unique external URLs are in published documents
grep -oE 'https?://[^)>" ]+' /tmp/phase5-pub/*.md | \
    awk -F: '{print $2}' | sort -u | wc -l
# Expected: 200+ unique URLs

# Test a sample of citation URLs
grep -oE 'https?://[^)>" ]+' /tmp/phase5-pub/*.md | \
    awk -F: '{print $2}' | sort -u | head -20 | while read url; do
        status=$(curl -sk -o /dev/null -w "%{http_code}" --max-time 5 "https:$url" 2>/dev/null || echo "ERR")
        echo "$status $url"
    done
```

**Classification of citation 404s:**

| Type | Example | Severity | Action |
|------|---------|----------|--------|
| Broken external URL | Academic paper moved | Low | Not our platform's problem; document in errata |
| Internal anchor broken | `#section-5` not found | Medium | Fix anchor in post content |
| Discourse topic link broken | Topic was deleted | High | Re-create missing topic |
| API returns 404 for our topic | Category changed | High | Fix routing/permissions |

**For broken external URLs (academic, government sources):**

This is expected for some citations (link rot is normal). It does not constitute a rollback trigger. Document broken links in an errata topic:

```bash
# Create an errata/notes topic in Meta category
cd /var/discourse
sudo ./launcher enter app
rails c

meta_cat = Category.find_by(name: "Meta")
admin_user = User.find_by(admin: true)

# Collect broken external links first, then create errata post
errata_content = "## Citation Link Verification Notes\n\nSome external citation links may be unavailable due to link rot (sources moved or removed). The following links were flagged as returning 404:\n\n[list broken links here]\n\nAlternative access methods:\n- Google Scholar search by title\n- Wayback Machine archive: https://web.archive.org/\n- Library access to paywalled papers"

# Create the errata post
exit
```

**For broken internal anchors (within Discourse topics):**

Discourse renders Markdown headings as anchor links. If a heading contains special characters, the anchor may not match what the author linked.

Fix by editing the post:

```bash
curl -s -X PUT "$DISCOURSE_URL/posts/POST_ID.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d '{"post": {"raw": "CORRECTED_CONTENT_HERE"}}' > /dev/null
```

**Recovery Time Estimate**: Variable. External URL 404s are non-blocking (5 minutes to document). Internal anchor fixes: 10–20 minutes per document.

**Communication**: Citation link issues do not require stakeholder notification unless widespread (> 25% of citations broken). Log to errata topic.

**Prevention**: Pre-validate external URLs before publication using the check script above. For large citation lists, Wayback Machine has a bulk-save API that can snapshot all sources.

---

## Scenario F: Hard Deadline Miss — June 10 Reschedule Procedure

If publication cannot complete by 19:00 UTC on June 9 for any reason, execute this reschedule.

### Reschedule Activation Criteria

Activate June 10 reschedule if:
- Platform cannot be restored within 3 hours of failure detection
- Network outage persists > 20 minutes with no resolution path
- Content corruption is discovered that requires regenerating source files

### Reschedule Procedure

**Step 1: Stop current publication attempt**

```bash
# If mid-upload: record which topics have been uploaded
curl -sk "$DISCOURSE_URL/c/phase-5-published-research.json" 2>/dev/null | python3 -c "
import sys, json
d = json.load(sys.stdin)
topics = d.get('topic_list',{}).get('topics',[])
print(f'Topics uploaded before reschedule: {len(topics)}')
for t in topics:
    print(f'  [{t[\"id\"]}] {t[\"title\"][:60]}')
" 2>/dev/null || echo "Platform unavailable — cannot enumerate uploaded topics"
```

**Step 2: Send reschedule notification**

```
Email subject: Phase 5 publication rescheduled to June 10

Dear coalition members,

We have encountered a technical issue that prevents us from completing
Phase 5 publication today. All content is safe and unaffected.

New publication schedule:
June 10, 2026 at 10:00 UTC

We will send a confirmation when publication is complete.

This delay does not affect Wave 2 recruitment (June 14) or any downstream
commitments.

We apologize for the inconvenience.
```

**Step 3: Diagnose and resolve the blocking issue**

Document the root cause in this file (add to the relevant scenario above).

**Step 4: June 10 execution**

Same procedure as June 9 operational document. For Discourse: run from the pre-publication checklist (Section 1 of PHASE_5_1_PUBLICATION_OPERATIONAL_PROCEDURES.md). The platform should already be deployed and working; only the content upload needs to execute.

---

## Rollback Decision Tree — Quick Reference

```
Publication issue detected
        |
        v
Is Discourse responding? (curl returns HTTP code)
        |
   YES  |  NO
        |   \
        |    --> Is Pi5 reachable at all? (ping 100.120.18.84)
        |             |
        |        YES  |  NO
        |             |   \
        |             |    --> Network outage (Scenario C)
        |             |       Wait 20 min; if unresolved → reschedule June 10
        |             v
        |        Discourse down but Pi5 up
        |        --> Attempt restart: ./launcher start app
        |        --> Wait 2 min; recheck
        |        --> If still down: destroy + bootstrap (25 min)
        |        --> If bootstrap fails: database corruption (Scenario A)
        |
        v
What error is Discourse returning?
        |
   500  |  403      |  200
   /503 |  (denied) |  (but users can't see content)
        |           |       |
        v           v       v
Database    Permission    Content
corruption  error         rendering
(Scenario A)(Scenario D)  or access
            Fix perms     issue
            (5-10 min)    Check login_required
                          (Scenario D)
        |
   If 500 for all requests:
        v
Check PostgreSQL logs
        |
   DB OK?  |  DB ERROR
           |
           v
      Database corruption
      (Scenario A)
      Restore from backup
      (20-45 min)
```

---

## Pre-Rollback Preservation Steps

Before executing any destructive recovery (destroy + bootstrap, or database restore), always preserve current state:

```bash
# 1. Copy app.yml (may have been modified since June 8)
cp /var/discourse/containers/app.yml /home/awank/backups/app.yml.pre-rollback-$(date +%Y%m%d%H%M)

# 2. Note which topics have been published (for re-upload after recovery)
curl -sk "$DISCOURSE_URL/c/phase-5-published-research.json" 2>/dev/null | python3 -c "
import sys,json
d=json.load(sys.stdin)
topics=d.get('topic_list',{}).get('topics',[])
[print(f'{t[\"id\"]}|{t[\"title\"]}') for t in topics]
" > /home/awank/backups/topics-pre-rollback-$(date +%Y%m%d%H%M).txt 2>/dev/null

# 3. Copy current backup to safe location
latest_backup=$(ls -t /var/discourse/shared/standalone/backups/default/*.gz 2>/dev/null | head -1)
[[ -n "$latest_backup" ]] && cp "$latest_backup" /home/awank/backups/

echo "State preserved before rollback"
ls /home/awank/backups/ | tail -5
```

---

## Scenario Recovery Time Summary

| Scenario | Detection | Fix Time | Total Downtime | Same-Day Publication? |
|----------|-----------|----------|----------------|----------------------|
| A: Database corruption | 2–5 min | 20–45 min | 25–50 min | Yes (if before 14:00 UTC) |
| B: Container crash (restart) | 1–2 min | 2–5 min | 5–10 min | Yes |
| B: Container crash (rebuild) | 1–2 min | 25–35 min | 30–40 min | Yes (if before 14:30 UTC) |
| C: Network outage (Tailscale) | 1–2 min | 2–5 min | 5–10 min | Yes |
| C: Network outage (ISP) | 5–10 min | Unknown | 20+ min | Maybe — trigger reschedule at 20 min |
| D: Permission error | 2–3 min | 5–10 min | 10–15 min | Yes |
| E: Citation 404s (external) | After publication | Non-blocking | 0 | N/A — not a rollback trigger |
| F: Hard deadline miss | Any time | Overnight | 14–21 hours | No — June 10 08:00 UTC |

**Expected probability of each scenario:**

| Scenario | Probability | Basis |
|----------|-------------|-------|
| A: Database corruption | < 1% | Clean deployment, no writes during publication |
| B: Container crash | 3–5% | Pi5 thermal throttling under sustained load; OOM possible |
| C: Network outage | 2–3% | Tailscale is generally stable; ISP outage is random |
| D: Permission error | 2–5% | Likely if permissions were not tested on June 8 |
| E: Citation 404s | 15–25% | Link rot is common in academic references; not a blocker |
| F: Hard deadline miss | < 2% | Multiple scenarios would have to chain for this to trigger |

**Most likely issue**: Container crash under load (OOM or Pi5 thermal event). Mitigated by: setting `UNICORN_WORKERS: 2`, monitoring health check during publication, and running the load test on June 8 to confirm Pi5 handles 20 concurrent users without OOM.

---

## Post-Incident Review Template

After any rollback or significant incident, complete this review within 24 hours.

```markdown
## Post-Incident Review — [DATE] [INCIDENT_TITLE]

**Detection time**: HH:MM UTC
**Resolution time**: HH:MM UTC
**Total downtime**: XX minutes
**Impact**: [Users affected, content unavailability, deadline impact]

**Root cause**: 
[One paragraph: what failed and why]

**Contributing factors**:
- [Factor 1]
- [Factor 2]

**Timeline**:
- HH:MM — [event]
- HH:MM — [event]

**What worked well**:
- [Recovery procedure step that was accurate and fast]

**What didn't work**:
- [Recovery step that was wrong, slow, or unclear]

**Action items**:
- [ ] [Specific fix to prevent recurrence]
- [ ] [Specific runbook update needed]

**Runbook accuracy**: [Did this procedure work as written, or did we deviate?]
```

---

## Appendix: Emergency Contacts and Communication Paths

**Communication if Pi5 is unreachable:**
- Use any device not on the Pi5's network
- Email is the fallback channel for all stakeholder notifications
- Tailscale admin console at `https://login.tailscale.com/admin/machines` shows Pi5 connectivity status

**Recovery resources:**
- Content source (unchanged): `/tmp/phase5-pub/` on Pi5, and `projects/systems-resilience/phase-5/` in git
- Deployment backup: `/home/awank/backups/discourse/` on Pi5
- `app.yml` backup: `/home/awank/backups/app.yml.pre-rollback-*`
- This runbook and operational procedures: `projects/systems-resilience/` in git (accessible even if Pi5 is down)

**If you need to run Discourse on a different machine (emergency fallback):**

Any Linux machine with 4GB+ RAM, Docker, and internet access can run Discourse in 30–60 minutes using the DISCOURSE_DEPLOYMENT_RUNBOOK.md Phase 2–5 procedure. Content from `/tmp/phase5-pub/` can be rsync'd to the new machine. The June 9 publication would complete 2–4 hours later than planned.
