---
title: "Phase 5.1 Publication Operational Procedures"
project: systems-resilience
phase: "5.1"
platform: "Discourse (primary) / Nextcloud (fallback)"
status: PRODUCTION-READY — execute June 9 12:30–15:00 UTC
created: 2026-06-10
publication_window: "2026-06-09 13:00–15:00 UTC"
pre_publication_window: "2026-06-09 12:30–13:00 UTC"
content_bundle: "/tmp/phase5-pub/ — 61,611 words, 336+ citations, 12 files verified"
cross_references:
  - DISCOURSE_DEPLOYMENT_RUNBOOK.md
  - PHASE_5_1_PUBLICATION_ROLLBACK_PROCEDURE.md
  - PHASE_5_1_CONTENT_READINESS.md
---

# Phase 5.1 Publication Operational Procedures
## June 9, 2026 — 12:30–15:00 UTC Execution Window

**Hard deadline**: All content live and verified by 15:00 UTC June 9.

**Operator**: One person can execute this solo. Two-person team (publisher + monitor) is preferred for the 13:00–15:00 UTC window.

**Platform**: These procedures are written for Discourse as primary. Section 7 covers Nextcloud fallback if Discourse is unavailable at execution time.

---

## Pre-Publication Checklist (June 9, 12:30–13:00 UTC)

Complete this section before starting any uploads. If any check fails, diagnose and resolve before 13:00 UTC. If a check cannot be resolved in time, invoke the appropriate contingency.

### Check A: Content Bundle Integrity

```bash
# Verify all 12 files are present and checksums match
cd /tmp/phase5-pub

# File presence
ls -lah *.md pdf/*.pdf
# Expected: 6 .md files + 6 .pdf files, total ~12 files

# File sizes (quick sanity check)
du -sh /tmp/phase5-pub/
# Expected: ~2.1 MB total

# Checksum verification (compare against manifest from June 7 audit)
md5sum -c MANIFEST.txt 2>/dev/null || (
    echo "MANIFEST.txt not found — running fresh checksum check"
    md5sum *.md pdf/*.pdf
)
# Expected: all checksums match (no "FAILED" output)
```

**If a checksum fails**: Do NOT publish. Identify which file is corrupted, restore from the project repository in `/home/awank/dev/SuperClaude_Framework/projects/systems-resilience/phase-5/`, regenerate the PDF if needed, and re-verify. This should take 5–10 minutes maximum.

**Decision**: If content bundle cannot be verified intact by 12:55 UTC, invoke the 30-minute delay procedure (push publication start to 13:30 UTC) and notify any waiting authors.

### Check B: Platform Availability

```bash
# Confirm Discourse is running
curl -sk -o /dev/null -w "HTTP %{http_code}\n" https://100.120.18.84/about.json
# Expected: HTTP 200

# If using a named hostname:
curl -sk -o /dev/null -w "HTTP %{http_code}\n" https://YOUR_DISCOURSE_HOSTNAME/about.json

# Confirm admin login works (test in browser)
# Navigate to: https://100.120.18.84
# Click Login → enter admin credentials
# Expected: admin dashboard icon visible in top-right
```

**Decision tree — platform availability**:

- HTTP 200 + admin login works → proceed
- HTTP 200 + admin login fails → reset admin password via rails console (10 min max), then proceed
- HTTP 503 / connection refused → Discourse is down; invoke restart procedure (see below), allow 10 min recovery
- Discourse cannot recover in 10 min → invoke Nextcloud fallback (Section 7)

```bash
# Discourse restart (if needed):
cd /var/discourse
sudo ./launcher status app
sudo ./launcher restart app
# Wait 2 minutes, then recheck HTTP
```

### Check C: API Credentials

```bash
# Verify API credentials are accessible
source /home/awank/.discourse-api-credentials
echo "API key prefix: ${DISCOURSE_API_KEY:0:8}..."
# Expected: 8-char hex prefix

# Test API access
curl -sk -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    "https://100.120.18.84/admin/dashboard.json" | \
    python3 -c "import sys,json; d=json.load(sys.stdin); print('API: OK, queued_jobs=', d.get('sidekiq_queued_jobs', '?'))"
# Expected: API: OK, queued_jobs= 0
```

**If API credentials missing**: Log into Discourse admin, go to Admin → API → New API Key, create a global key, save to `/home/awank/.discourse-api-credentials`.

### Check D: YAML Frontmatter Strip Verification

Discourse does not auto-strip YAML frontmatter. You must strip it before pasting content into topic bodies, or it will display as raw YAML at the top of each post.

```bash
# Quick test: confirm files have frontmatter
head -3 /tmp/phase5-pub/01-microgrids.md
# Expected first line: ---  (YAML frontmatter start)

# Create stripped versions for upload
mkdir -p /tmp/phase5-stripped

for f in /tmp/phase5-pub/*.md; do
    basename=$(basename "$f")
    python3 -c "
import re, sys
content = open('$f').read()
# Remove YAML frontmatter (everything between opening --- and closing ---)
stripped = re.sub(r'^---\n.*?\n---\n', '', content, count=1, flags=re.DOTALL)
open('/tmp/phase5-stripped/$basename', 'w').write(stripped)
print(f'Stripped: $basename ({len(stripped)} chars)')
"
done

# Verify no frontmatter remains
for f in /tmp/phase5-stripped/*.md; do
    first_line=$(head -1 "$f")
    if [[ "$first_line" == "---" ]]; then
        echo "WARNING: $f still has frontmatter"
    else
        echo "OK: $f starts with: $first_line"
    fi
done
```

### Check E: Announcement Email Draft

```bash
# Confirm announcement email is drafted and ready to send
# Email should include:
# - Publication confirmation
# - Direct links to all 6 topics (you'll have these after upload)
# - PDF download location
# - Wave 2 recruitment start date (June 14)

# Open your email client now; pre-stage the draft with placeholder URLs
# You'll fill in the actual topic URLs during the upload phase
```

### Check F: 12:55 UTC Pre-Publication Sign-Off

At 12:55 UTC, confirm all checks before starting uploads:

- [ ] Content bundle: all 12 files present, checksums match
- [ ] Stripped copies created in `/tmp/phase5-stripped/`
- [ ] Discourse: HTTP 200, admin login verified
- [ ] API credentials: tested and working
- [ ] Announcement email: drafted and staged
- [ ] Both PDF files and markdown ready for upload
- [ ] This runbook open and accessible

**13:00 UTC**: Begin publication uploads.

---

## Content Staging (13:00 UTC)

Before uploading topics, verify the publication category exists and has the correct structure.

```bash
source /home/awank/.discourse-api-credentials
DISCOURSE_URL="https://100.120.18.84"

# Get category list and find Phase 5 category
curl -sk "$DISCOURSE_URL/categories.json" | python3 -c "
import sys, json
cats = json.load(sys.stdin)['category_list']['categories']
for c in cats:
    print(f'  id={c[\"id\"]:3} | {c[\"name\"]}')
" 

# Note the category ID for 'Phase 5 — Published Research'
# You'll need this ID for all uploads
# Expected output should include: Phase 5 — Published Research
```

**If the category does not exist** (was not created during June 8 deployment):

```bash
cd /var/discourse
sudo ./launcher enter app
rails c

admin_user = User.find_by(admin: true)
cat = Category.create!(
    name: "Phase 5 — Published Research",
    color: "3AB54A",
    description: "Phase 5 Wave 1+2 research documents",
    position: 1,
    user: admin_user
)
cat.set_permissions({ everyone: :readonly, "phase5_authors" => :full, "staff" => :full })
cat.save!
puts "Category created: id=#{cat.id}"
exit
```

---

## Publication Sequence (13:00–14:30 UTC)

### Rationale for Upload Order

Documents are published in dependency order: infrastructure first (gives context), implementation second (builds on infrastructure), supportive domains third, integrated corpus last (depends on all preceding topics being available for cross-reference).

| Order | Document | Rationale | Time |
|-------|----------|-----------|------|
| 1st | Microgrids | Infrastructure context; foundational | 13:00–13:20 |
| 2nd | Community Implementation Playbook | Governance builds on infrastructure | 13:20–13:40 |
| 3rd | Conflict Resolution Framework | Governance sub-domain | 13:40–14:00 |
| 4th | Psychological Support Guide | Community health; independent | 14:00–14:15 |
| 5th | Veterinary Care Guide | Food systems; independent | 14:15–14:30 |
| 6th | Integrated Corpus | Requires all 5 docs to be live first | 14:30–14:50 |

Each document: 15–20 minutes (copy content + set metadata + verify rendering).

### Upload Script

Use this script to create each topic via the Discourse API. This is faster and more reliable than manual copy-paste for large documents.

```bash
#!/bin/bash
# Phase 5.1 publication upload script
# Usage: ./upload_topic.sh <doc_number> <title> <category_id> <tags>
# Run from /tmp/phase5-stripped/

source /home/awank/.discourse-api-credentials
DISCOURSE_URL="https://100.120.18.84"
PHASE5_CATEGORY_ID="REPLACE_WITH_ACTUAL_CATEGORY_ID"  # from staging check above

upload_document() {
    local doc_num="$1"
    local title="$2"
    local tags="$3"
    local filename="/tmp/phase5-stripped/$(ls /tmp/phase5-stripped/ | grep "^0${doc_num}")"

    if [[ ! -f "$filename" ]]; then
        echo "ERROR: File not found for doc $doc_num"
        return 1
    fi

    local content=$(cat "$filename")
    local word_count=$(wc -w < "$filename")
    echo "Uploading: $title ($word_count words from $filename)"

    response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
        -H "Api-Key: $DISCOURSE_API_KEY" \
        -H "Api-Username: system" \
        -H "Content-Type: application/json" \
        --data-binary @- << CURL_EOF
{
    "title": "$title",
    "raw": $(python3 -c "import json,sys; print(json.dumps(open('$filename').read()))"),
    "category": $PHASE5_CATEGORY_ID,
    "tags": $tags
}
CURL_EOF
    )

    topic_id=$(echo "$response" | python3 -c "
import sys, json
d = json.load(sys.stdin)
if 'errors' in d:
    print('ERROR:', d['errors'])
elif 'topic_id' in d:
    print('OK:', d['topic_id'])
else:
    print('UNKNOWN:', d)
" 2>&1)

    echo "$title => $topic_id"
    echo "$doc_num|$title|$topic_id|$(date -u +%H:%M)" >> /tmp/phase5-publication-log.txt
}
```

### Document 1: Distributed Microgrids (13:00–13:20 UTC)

```bash
source /home/awank/.discourse-api-credentials
DISCOURSE_URL="https://100.120.18.84"

# Get Phase 5 category ID
PHASE5_CAT_ID=$(curl -sk "$DISCOURSE_URL/categories.json" | python3 -c "
import sys,json
cats = json.load(sys.stdin)['category_list']['categories']
phase5 = [c for c in cats if 'Phase 5' in c['name']]
print(phase5[0]['id'] if phase5 else 'NOT_FOUND')
")
echo "Phase 5 category ID: $PHASE5_CAT_ID"

# Upload Document 1
content=$(cat /tmp/phase5-stripped/01-microgrids.md)
response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"01 — Distributed Microgrids as Community Resilience Infrastructure\",
        \"raw\": $(python3 -c "import json; print(json.dumps(open('/tmp/phase5-stripped/01-microgrids.md').read()))"),
        \"category\": $PHASE5_CAT_ID,
        \"tags\": [\"microgrids\", \"energy\", \"infrastructure\", \"phase-5\", \"wave-2\"]
    }")

doc1_topic_id=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('topic_id','ERROR'))")
echo "Document 1 topic ID: $doc1_topic_id"
echo "URL: $DISCOURSE_URL/t/$doc1_topic_id"
```

**Verification after Document 1** (takes 2 minutes):

```bash
# Confirm topic exists and is readable
curl -sk "$DISCOURSE_URL/t/$doc1_topic_id.json" | python3 -c "
import sys, json
d = json.load(sys.stdin)
print('Title:', d.get('title'))
print('Posts:', d.get('posts_count'))
post1 = d.get('post_stream',{}).get('posts',[{}])[0]
print('First 100 chars:', post1.get('raw','')[:100])
"
# Expected: Title matches, posts=1, content starts with document text (not '---')
```

**Decision tree — if Document 1 upload fails:**
- Error: "category not found" → verify `$PHASE5_CAT_ID` is correct, re-run category ID check
- Error: "rate limited" → wait 60 seconds, retry
- Error: "title has already been used" → topic already exists (check Discourse UI), skip to Document 2
- Error: empty response / connection refused → Discourse may be down; wait 2 min, retry once; if still failing activate rollback (PHASE_5_1_PUBLICATION_ROLLBACK_PROCEDURE.md, Scenario 2)
- Upload takes > 30 minutes for a single 65KB document → network issue; check `ping 100.120.18.84`, restart network if needed

**Record topic ID for announcement email**: `DOC1_URL=$DISCOURSE_URL/t/$doc1_topic_id`

### Document 2: Community Implementation Playbook (13:20–13:40 UTC)

```bash
response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"02 — Community Implementation Playbook — Tier 3 Coordination Framework\",
        \"raw\": $(python3 -c "import json; print(json.dumps(open('/tmp/phase5-stripped/02-playbook.md').read()))"),
        \"category\": $PHASE5_CAT_ID,
        \"tags\": [\"governance\", \"coordination\", \"implementation\", \"phase-5\", \"wave-2\"]
    }")

doc2_topic_id=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('topic_id','ERROR'))")
echo "Document 2 topic ID: $doc2_topic_id"
```

**Verification**: Open `$DISCOURSE_URL/t/$doc2_topic_id` in browser. Verify:
- [ ] Governance section visible (tables should render as formatted tables)
- [ ] No YAML frontmatter at top
- [ ] Ostrom principles table appears formatted (not raw pipe characters)

**If tables are not rendering**: Discourse requires a blank line before and after Markdown tables. If the stripped markdown has tables immediately following a heading without a blank line, the rendering may be broken. Fix:

```bash
python3 -c "
import re
content = open('/tmp/phase5-stripped/02-playbook.md').read()
# Ensure blank line before tables
fixed = re.sub(r'(\S)\n(\|)', r'\1\n\n\2', content)
open('/tmp/phase5-stripped/02-playbook-fixed.md', 'w').write(fixed)
print('Fixed table spacing')
"
# Then re-upload with the fixed file
```

### Document 3: Conflict Resolution Framework (13:40–14:00 UTC)

```bash
response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"03 — Conflict Resolution and Governance Framework\",
        \"raw\": $(python3 -c "import json; print(json.dumps(open('/tmp/phase5-stripped/03-conflict-resolution.md').read()))"),
        \"category\": $PHASE5_CAT_ID,
        \"tags\": [\"conflict-resolution\", \"mediation\", \"governance\", \"nvc\", \"phase-5\"]
    }")

doc3_topic_id=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('topic_id','ERROR'))")
echo "Document 3 topic ID: $doc3_topic_id"
```

### Document 4: Psychological Support Guide (14:00–14:15 UTC)

**This document requires a clinical advisory at the top of the topic.**

```bash
ADVISORY_TEXT="**Clinical Advisory**: This document contains Psychological First Aid (PFA) protocols based on SAMHSA and Red Cross guidelines. All clinical procedures should be adapted to local mental health professional standards and jurisdiction-specific requirements. This is not a substitute for professional mental health care.\n\n---\n\n"

DOC4_CONTENT=$(python3 -c "
import json
content = open('/tmp/phase5-stripped/04-psychological-support.md').read()
advisory = '**Clinical Advisory**: This document contains Psychological First Aid (PFA) protocols based on SAMHSA and Red Cross guidelines. All clinical procedures should be adapted to local mental health professional standards and jurisdiction-specific requirements. This is not a substitute for professional mental health care.\n\n---\n\n'
print(json.dumps(advisory + content))
")

response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"04 — Psychological Support and Trauma Recovery — Tier 2 Household Guide\",
        \"raw\": $DOC4_CONTENT,
        \"category\": $PHASE5_CAT_ID,
        \"tags\": [\"psychological-support\", \"trauma\", \"pfa\", \"mental-health\", \"phase-5\"]
    }")

doc4_topic_id=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('topic_id','ERROR'))")
echo "Document 4 topic ID: $doc4_topic_id"
```

**Critical verification for Document 4:**
- [ ] Clinical advisory appears as the FIRST content visible when opening the topic
- [ ] Advisory uses bold text and is separated from content by `---` divider
- [ ] PFA protocols section (SAMHSA) is present further in the document

### Document 5: Veterinary Care Guide (14:15–14:30 UTC)

```bash
DOC5_CONTENT=$(python3 -c "
import json
content = open('/tmp/phase5-stripped/05-veterinary-care.md').read()
advisory = '**Professional Practice Advisory**: This document contains veterinary protocols and triage procedures. Implementation requires collaboration with licensed veterinarians. Protocols should be adapted to local disease patterns, climate conditions, and professional veterinary standards. This is not a substitute for professional veterinary medicine.\n\n---\n\n'
print(json.dumps(advisory + content))
")

response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"05 — Veterinary Care in Crisis Contexts — Tier 2 Household Guide\",
        \"raw\": $DOC5_CONTENT,
        \"category\": $PHASE5_CAT_ID,
        \"tags\": [\"veterinary\", \"livestock\", \"crisis-medicine\", \"food-systems\", \"phase-5\"]
    }")

doc5_topic_id=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('topic_id','ERROR'))")
echo "Document 5 topic ID: $doc5_topic_id"
```

### Document 6: Integrated Corpus (14:30–14:50 UTC)

The integrated corpus is the largest document (16,234 words, 1285 lines). Upload last, pin to top of category.

```bash
response=$(curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"REFERENCE — Phase 5 Wave 1+2 Integrated Corpus (Complete Research Reference)\",
        \"raw\": $(python3 -c "import json; print(json.dumps(open('/tmp/phase5-stripped/06-integrated-corpus.md').read()))"),
        \"category\": $PHASE5_CAT_ID,
        \"tags\": [\"reference\", \"corpus\", \"complete\", \"phase-5\", \"wave-1\", \"wave-2\"]
    }")

doc6_topic_id=$(echo "$response" | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('topic_id','ERROR'))")
echo "Document 6 (corpus) topic ID: $doc6_topic_id"

# Pin the corpus topic to the top of the category
curl -s -X PUT "$DISCOURSE_URL/t/$doc6_topic_id/status.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d '{"status": "pinned", "enabled": "true"}'
echo "Corpus topic pinned"
```

### PDF Attachment Upload

After all topics are created, attach PDFs to each topic.

```bash
# PDF files are in /tmp/phase5-pub/pdf/
# Discourse max attachment size: 4 MB (all Phase 5 PDFs are 247–295 KB — well within limit)

attach_pdf() {
    local topic_id="$1"
    local pdf_path="$2"
    local doc_label="$3"

    # Upload the file to get upload_url and short_url
    upload_response=$(curl -s -X POST "$DISCOURSE_URL/uploads.json" \
        -H "Api-Key: $DISCOURSE_API_KEY" \
        -H "Api-Username: system" \
        -F "files[]=@$pdf_path" \
        -F "type=attachment")

    short_url=$(echo "$upload_response" | python3 -c "
import sys,json
d=json.load(sys.stdin)
if isinstance(d,list): d=d[0]
print(d.get('short_url','ERROR'))
")
    filename=$(basename "$pdf_path")

    # Append PDF download link to topic's first post
    # Get post_id for the first post of the topic
    post_id=$(curl -sk "$DISCOURSE_URL/t/$topic_id.json" | python3 -c "
import sys,json
d=json.load(sys.stdin)
posts = d.get('post_stream',{}).get('posts',[])
print(posts[0]['id'] if posts else 'ERROR')
")

    # Edit the post to append PDF link
    # Get current content first
    current_raw=$(curl -sk "$DISCOURSE_URL/posts/$post_id.json" | python3 -c "
import sys,json; d=json.load(sys.stdin); print(d.get('raw',''))
")

    pdf_link="\n\n---\n\n**Download PDF**: [$filename]($short_url)"

    curl -s -X PUT "$DISCOURSE_URL/posts/$post_id.json" \
        -H "Api-Key: $DISCOURSE_API_KEY" \
        -H "Api-Username: system" \
        -H "Content-Type: application/json" \
        -d "{\"post\": {\"raw\": $(python3 -c "import json; print(json.dumps('$current_raw\n\n---\n\n**Download PDF**: [$filename]($short_url)'))") }}" > /dev/null

    echo "PDF attached: $doc_label -> topic $topic_id"
}

# Attach PDFs to each topic (run after all topics are created)
attach_pdf "$doc1_topic_id" "/tmp/phase5-pub/pdf/01-microgrids.pdf" "Microgrids"
attach_pdf "$doc2_topic_id" "/tmp/phase5-pub/pdf/02-playbook.pdf" "Playbook"
attach_pdf "$doc3_topic_id" "/tmp/phase5-pub/pdf/03-conflict-resolution.pdf" "Conflict Resolution"
attach_pdf "$doc4_topic_id" "/tmp/phase5-pub/pdf/04-psychological-support.pdf" "Psychological Support"
attach_pdf "$doc5_topic_id" "/tmp/phase5-pub/pdf/05-veterinary-care.pdf" "Veterinary Care"
attach_pdf "$doc6_topic_id" "/tmp/phase5-pub/pdf/06-integrated-corpus.pdf" "Integrated Corpus"
```

---

## Permissions and Access Control

After all topics are created, verify access controls are correct.

```bash
# Test 1: Unauthenticated read access (should work — content is public)
curl -sk "https://100.120.18.84/t/$doc1_topic_id.json" | python3 -c "
import sys,json
d=json.load(sys.stdin)
if 'errors' in d:
    print('ERROR: Public read blocked:', d['errors'])
else:
    print('OK: Public read works, title:', d.get('title'))
"

# Test 2: Unauthenticated post attempt (should fail — only authors can post)
post_test=$(curl -sk -o /dev/null -w "%{http_code}" -X POST "https://100.120.18.84/posts.json" \
    -H "Content-Type: application/json" \
    -d "{\"title\":\"test\",\"raw\":\"test\",\"category\":$PHASE5_CAT_ID}")
echo "Unauthenticated post attempt: HTTP $post_test"
# Expected: 403 (forbidden) — category is restricted to phase5_authors group

# Test 3: Admin can post (verify author role works)
admin_post_test=$(curl -sk -o /dev/null -w "%{http_code}" -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{\"title\":\"[DELETE ME] access test\",\"raw\":\"access test\",\"category\":$PHASE5_CAT_ID}")
echo "Admin post attempt: HTTP $admin_post_test"
# Expected: 200 (success)
# Clean up test topic if created
```

---

## Real-Time Monitoring During Publication

Assign one person to monitor while another uploads, OR run monitoring checks between each document upload.

### Between-Upload Status Check (run after each document)

```bash
check_discourse_health() {
    echo "=== HEALTH CHECK $(date -u '+%H:%M UTC') ==="

    # Response time
    response_time=$(curl -sk -o /dev/null -w "%{time_total}" "https://100.120.18.84/about.json")
    echo "Response time: ${response_time}s"
    if (( $(echo "$response_time > 5.0" | bc -l) )); then
        echo "WARNING: Response time > 5s — Discourse may be under load"
    fi

    # Container resource usage
    docker stats --no-stream --format "{{.Name}}: CPU={{.CPUPerc}} MEM={{.MemUsage}}" app 2>/dev/null || \
        cd /var/discourse && sudo ./launcher enter app bash -c "free -h | awk '/Mem:/{print \"RAM: used=\"\$3\"/\"\$2}'"

    # Sidekiq queue depth (background jobs)
    queue_depth=$(curl -sk \
        -H "Api-Key: $DISCOURSE_API_KEY" \
        -H "Api-Username: system" \
        "https://100.120.18.84/admin/dashboard.json" | \
        python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('sidekiq_queued_jobs','?'))" 2>/dev/null || echo "?")
    echo "Sidekiq queue: $queue_depth"
    if [[ "$queue_depth" -gt 100 ]] 2>/dev/null; then
        echo "WARNING: Sidekiq queue > 100 — background jobs may be backed up"
    fi

    echo "==="
}

# Run between each document upload
```

### Uptime and Access Confirmation

```bash
# Verify all published topics are accessible from external perspective
# (test from a different machine if possible, or use curl from Pi5 without API auth)

for topic_id in $doc1_topic_id $doc2_topic_id $doc3_topic_id $doc4_topic_id $doc5_topic_id $doc6_topic_id; do
    status=$(curl -sk -o /dev/null -w "%{http_code}" "https://100.120.18.84/t/$topic_id.json")
    echo "Topic $topic_id: HTTP $status"
done
# Expected: all return HTTP 200
```

### Decision Tree — Monitoring Issues

**If response time consistently > 5 seconds:**
1. Check Pi5 CPU: `top` — is Discourse consuming > 200% CPU?
2. If yes: Sidekiq is running background jobs (indexing, emails). Wait 5 minutes; it will normalize.
3. If CPU is low but response is slow: check `/var/log/discourse-health.log` for database issues.
4. If response time > 10 seconds for 3 consecutive checks: pause uploads, diagnose. Allow 15 minutes. If unresolved, push remaining uploads to 15:30 UTC and notify authors of 30-min delay.

**If users report they cannot access content by 14:00 UTC:**
1. Verify from your own browser (anonymous window): can you read the topics?
2. If yes: user-side issue (VPN, browser, DNS). Not a platform problem.
3. If no: escalate to rollback assessment (PHASE_5_1_PUBLICATION_ROLLBACK_PROCEDURE.md).

**If a topic renders incorrectly (raw markdown visible, tables broken):**
1. Identify which topic has rendering issues.
2. Delete the topic via API: `curl -s -X DELETE "$DISCOURSE_URL/t/$topic_id.json" -H "Api-Key: $DISCOURSE_API_KEY" -H "Api-Username: system"`
3. Fix the content (add blank lines around tables, ensure headings have blank lines below them).
4. Re-upload using the same procedure.
5. Time budget: 20 minutes per re-upload. If more than 2 documents need re-upload, this pushes the deadline past 15:00 UTC — invoke the delay notification procedure.

---

## Post-Publication Verification (14:50–15:00 UTC)

After all 6 documents and PDFs are uploaded, run the full verification suite.

```bash
echo "=== POST-PUBLICATION VERIFICATION $(date -u '+%Y-%m-%dT%H:%M:%SZ') ===" | tee /tmp/publication-verification.log

# Verify all topic IDs are set
for varname in doc1_topic_id doc2_topic_id doc3_topic_id doc4_topic_id doc5_topic_id doc6_topic_id; do
    val="${!varname:-MISSING}"
    echo "$varname: $val" | tee -a /tmp/publication-verification.log
    if [[ "$val" == "MISSING" || "$val" == "ERROR" ]]; then
        echo "CRITICAL: $varname not set — this document was not published"
    fi
done

echo "" | tee -a /tmp/publication-verification.log
echo "Topic accessibility:" | tee -a /tmp/publication-verification.log

for topic_id in $doc1_topic_id $doc2_topic_id $doc3_topic_id $doc4_topic_id $doc5_topic_id $doc6_topic_id; do
    if [[ -z "$topic_id" || "$topic_id" == "ERROR" || "$topic_id" == "MISSING" ]]; then
        echo "  SKIP (no topic ID)" | tee -a /tmp/publication-verification.log
        continue
    fi

    result=$(curl -sk "$DISCOURSE_URL/t/$topic_id.json" | python3 -c "
import sys,json
d=json.load(sys.stdin)
if 'errors' in d:
    print(f'  FAIL topic={$topic_id}: {d[\"errors\"]}')
else:
    title = d.get('title','?')[:50]
    posts = d.get('posts_count',0)
    views = d.get('views',0)
    # Check first post for YAML frontmatter leak
    first_post = d.get('post_stream',{}).get('posts',[{}])[0]
    raw = first_post.get('raw','')
    frontmatter_leak = raw.startswith('---')
    status = 'FRONTMATTER_LEAK' if frontmatter_leak else 'OK'
    print(f'  {status} topic=$topic_id posts={posts} views={views} title={title[:40]}')
" 2>&1)
    echo "$result" | tee -a /tmp/publication-verification.log
done

echo "" | tee -a /tmp/publication-verification.log
echo "Category listing:" | tee -a /tmp/publication-verification.log
curl -sk "$DISCOURSE_URL/c/phase-5-published-research.json" 2>/dev/null | python3 -c "
import sys,json
d=json.load(sys.stdin)
topics = d.get('topic_list',{}).get('topics',[])
print(f'  Topics in Phase 5 category: {len(topics)}')
for t in topics[:10]:
    print(f'  - [{t[\"id\"]}] {t[\"title\"][:60]}')
" 2>/dev/null || echo "  (Category listing via slug — check manually if this fails)" | tee -a /tmp/publication-verification.log

echo "" | tee -a /tmp/publication-verification.log
echo "Search verification:" | tee -a /tmp/publication-verification.log
# Note: search index may take 5-10 min to update after publication
for term in "microgrids" "Ostrom" "veterinary" "psychological"; do
    count=$(curl -sk "$DISCOURSE_URL/search.json?q=$term" | python3 -c "
import sys,json
d=json.load(sys.stdin)
print(len(d.get('topics',[])))
" 2>/dev/null || echo "?")
    echo "  Search '$term': $count results" | tee -a /tmp/publication-verification.log
done

echo "" | tee -a /tmp/publication-verification.log
echo "Verification complete. Review log at /tmp/publication-verification.log"
```

### Post-Publication Verification Checklist

- [ ] All 6 topic IDs are set (not MISSING or ERROR)
- [ ] All 6 topics return HTTP 200 when accessed without authentication
- [ ] No topic shows FRONTMATTER_LEAK (YAML `---` at start of content)
- [ ] Category listing shows 6+ topics in Phase 5 category (includes pinned index topic from June 8)
- [ ] Search for "microgrids" returns at least 1 result
- [ ] Search for "veterinary" returns at least 1 result
- [ ] Integrated corpus topic is pinned (appears at top of category)
- [ ] Documents 04 and 05 show clinical advisory at top of first post
- [ ] PDF download links are attached to each topic
- [ ] All topics have appropriate tags applied

**If all checks pass**: Publication is successful. Proceed to notification sequence.

**If any topic shows FRONTMATTER_LEAK**: Delete and re-upload that topic immediately. This is a content presentation issue, not a platform issue, and is fixable in < 20 minutes.

**If search returns 0 results for all terms**: Discourse search index updates asynchronously. Wait 10 minutes and recheck. Search indexing is a non-blocking issue — content is readable even if search takes longer.

---

## Notification Sequence (15:00–15:15 UTC)

### Step 1: Record All Publication URLs

```bash
# Print final URL summary for announcement email
echo "=== PUBLICATION URL SUMMARY ==="
echo "Discourse base URL: $DISCOURSE_URL"
echo ""
echo "Published topics:"
echo "  01. Microgrids:          $DISCOURSE_URL/t/$doc1_topic_id"
echo "  02. Playbook:            $DISCOURSE_URL/t/$doc2_topic_id"
echo "  03. Conflict Resolution: $DISCOURSE_URL/t/$doc3_topic_id"
echo "  04. Psychological:       $DISCOURSE_URL/t/$doc4_topic_id"
echo "  05. Veterinary Care:     $DISCOURSE_URL/t/$doc5_topic_id"
echo "  06. Integrated Corpus:   $DISCOURSE_URL/t/$doc6_topic_id"
echo ""
echo "Category (all documents): $DISCOURSE_URL/c/phase-5-published-research"
```

### Step 2: Send Author Coalition Email

Fill in the URLs from Step 1 into the announcement email draft and send.

Subject: `Phase 5 Wave 1+2 Published — Community Resilience Framework Live`

Body template (fill in `[TOPIC_URL_*]` with actual URLs):

```
Phase 5 Wave 1+2 research is now published and publicly accessible.

DOCUMENTS LIVE:

1. Distributed Microgrids as Community Resilience Infrastructure
   [TOPIC_URL_1]

2. Community Implementation Playbook — Tier 3 Coordination Framework
   [TOPIC_URL_2]

3. Conflict Resolution and Governance Framework
   [TOPIC_URL_3]

4. Psychological Support and Trauma Recovery
   [TOPIC_URL_4]
   (Clinical advisory: SAMHSA-based PFA protocols — adapt to local standards)

5. Veterinary Care in Crisis Contexts
   [TOPIC_URL_5]
   (Professional advisory: adapt to local veterinary standards)

6. Integrated Corpus — Complete Reference
   [TOPIC_URL_6]

All content is open and freely available. PDF downloads are attached to each topic.

NEXT STEPS:

Wave 2 author recruitment begins June 14, 2026.

If you are interested in contributing to Phase 6 expansion domains, please reply with:
- Your area of expertise
- Hours per week available July–September 2026
- Any prior writing or research experience

Questions: [contact email]
```

### Step 3: Platform Announcement

```bash
# Create announcement topic in Discourse Announcements category
ann_cat_id=$(curl -sk "$DISCOURSE_URL/categories.json" | python3 -c "
import sys,json
cats=json.load(sys.stdin)['category_list']['categories']
ann=[c for c in cats if 'Announce' in c['name']]
print(ann[0]['id'] if ann else 'ERROR')
")

curl -s -X POST "$DISCOURSE_URL/posts.json" \
    -H "Api-Key: $DISCOURSE_API_KEY" \
    -H "Api-Username: system" \
    -H "Content-Type: application/json" \
    -d "{
        \"title\": \"Phase 5 Wave 1+2 Research Published — June 9, 2026\",
        \"raw\": \"## Phase 5 Publication Complete\n\nSix research documents are now live in the [Phase 5 Published Research]($DISCOURSE_URL/c/phase-5-published-research) category:\n\n1. Distributed Microgrids as Community Resilience Infrastructure\n2. Community Implementation Playbook\n3. Conflict Resolution and Governance Framework\n4. Psychological Support and Trauma Recovery\n5. Veterinary Care in Crisis Contexts\n6. Integrated Corpus (complete reference, 16,234 words)\n\nAll content is open and freely available. Wave 2 author recruitment begins June 14, 2026.\",
        \"category\": $ann_cat_id,
        \"tags\": [\"announcement\", \"phase-5\", \"publication\"]
    }" > /dev/null
echo "Announcement posted"
```

---

## Nextcloud Fallback (Section 7) — If Discourse is Unavailable

If Discourse is down and cannot recover by 13:30 UTC on June 9, switch to Nextcloud.

**Decision trigger**: Discourse returns non-200 responses for > 10 consecutive minutes after restart attempt. OR admin login cannot be restored within 10 minutes.

```bash
# Verify Nextcloud is available (should already be running if deployed)
curl -sk -o /dev/null -w "Nextcloud HTTP: %{http_code}\n" "https://100.70.184.84/nextcloud/"
# Expected: HTTP 200

# If Nextcloud is also down: escalate to June 10 rescheduling
# Document the failure, notify authors of 24-hour delay

# Nextcloud upload procedure:
# 1. SSH to raspby1 (100.70.184.84)
ssh awank@100.70.184.84

# 2. Copy files to Nextcloud data directory
sudo rsync -av /tmp/phase5-pub/ /var/lib/nextcloud/data/admin/files/Phase-5-Published-Research/
sudo chown -R www-data:www-data /var/lib/nextcloud/data/admin/files/Phase-5-Published-Research/

# 3. Trigger Nextcloud file scan
sudo docker exec nextcloud-app php occ files:scan --all

# 4. Create public share link
sudo docker exec nextcloud-app php occ share:create --type 3 --path "/Phase-5-Published-Research" --permissions 1
# type 3 = public link, permissions 1 = read only

# 5. Announce with Nextcloud URL instead of Discourse URL
```

Nextcloud publication uses the same document content, but the delivery mechanism changes from Discourse topics to Nextcloud shared folders. All verification steps (content accessibility, PDF downloads, word count) remain the same. Search functionality will be reduced (Nextcloud FTS takes longer to index).

---

## Publication Closeout (15:15 UTC)

```bash
# Record publication completion
echo "=== PUBLICATION COMPLETE $(date -u '+%Y-%m-%dT%H:%M:%SZ') ===" >> /tmp/publication-verification.log
echo "All 6 documents published" >> /tmp/publication-verification.log
echo "Announcement email sent" >> /tmp/publication-verification.log
echo "Platform: Discourse at $DISCOURSE_URL" >> /tmp/publication-verification.log

# Archive source files
mkdir -p /home/awank/backups/phase5-pub-archive-$(date +%Y%m%d)
rsync -a /tmp/phase5-pub/ /home/awank/backups/phase5-pub-archive-$(date +%Y%m%d)/
echo "Source files archived to /home/awank/backups/phase5-pub-archive-$(date +%Y%m%d)"

# Begin monitoring (first check)
/opt/discourse-healthcheck.sh
cat /var/log/discourse-health.log | tail -5
```

**Post-publication monitoring schedule:**
- 15:15 UTC: first post-publication check (run health check script)
- 15:30 UTC: verify Discourse logs show no errors
- 16:00 UTC: check topic view counts (indication of user access)
- 17:00 UTC: final check; publication window closed

**Wave 2 activation**: Once publication is confirmed complete, the Wave 2 author recruitment window opens (start June 10, full execution June 14).
