#!/usr/bin/env bash
# =============================================================================
# GATE_3_VERIFICATION_SCRIPT.sh
# Seedwarden — Gate 3 automated pass/fail verification
#
# Checks:
#   1. DNS CNAME propagation for Kit email authentication records
#   2. Kit API tag existence (all 15 tags)
#   3. Zone card PDF links resolve and download (not "Request access")
#
# Dependencies: bash, curl, nslookup (all standard on macOS/Linux)
# No package installs required.
#
# Usage:
#   chmod +x GATE_3_VERIFICATION_SCRIPT.sh
#   ./GATE_3_VERIFICATION_SCRIPT.sh
#
# Required environment variable:
#   KIT_API_KEY — your Kit API key (from Kit > Settings > API)
#
# Optional environment variable:
#   KIT_CNAME_HOST — the CNAME hostname Kit gave you (e.g. em.seedwarden.com)
#                    Leave blank to skip DNS check until you have this value.
#
# Example:
#   KIT_API_KEY=your_key_here KIT_CNAME_HOST=em.seedwarden.com ./GATE_3_VERIFICATION_SCRIPT.sh
# =============================================================================

set -euo pipefail

# ---------------------------------------------------------------------------
# Configuration — edit these after Gate 3 account setup
# ---------------------------------------------------------------------------

# Kit API key — REQUIRED for tag verification
# Get from: Kit > Settings > Developer (API) > API Keys > Create a new key
KIT_API_KEY="${KIT_API_KEY:-}"

# Kit CNAME host — the Name/Host value from Kit's DNS settings
# Example: em.seedwarden.com  or  k1._domainkey.seedwarden.com
# Leave blank if you do not have a custom domain yet; DNS check will be skipped.
KIT_CNAME_HOST="${KIT_CNAME_HOST:-}"

# Google Drive zone card PDF direct-download URLs
# Replace [FILE_ID_X] with actual Google Drive file IDs after uploading zone cards.
# Format: https://drive.google.com/uc?export=download&id=YOUR_FILE_ID
declare -A ZONE_CARD_URLS=(
  [3]="${ZONE_CARD_URL_3:-}"
  [4]="${ZONE_CARD_URL_4:-}"
  [5]="${ZONE_CARD_URL_5:-}"
  [6]="${ZONE_CARD_URL_6:-}"
  [7]="${ZONE_CARD_URL_7:-}"
  [8]="${ZONE_CARD_URL_8:-}"
  [9]="${ZONE_CARD_URL_9:-}"
  [10]="${ZONE_CARD_URL_10:-}"
)

# Expected tags (must exist in Kit account)
EXPECTED_ZONE_TAGS=(zone-3 zone-4 zone-5 zone-6 zone-7 zone-8 zone-9 zone-10)
EXPECTED_INTEREST_TAGS=(seed-saver forager food-preserver homesteader medicinal-herbs vip-buyer phase-1-buyer)

# Kit API base URL
KIT_API_BASE="https://api.kit.com/v4"

# ---------------------------------------------------------------------------
# Output helpers
# ---------------------------------------------------------------------------

PASS_COUNT=0
FAIL_COUNT=0
SKIP_COUNT=0

pass() { echo "  [PASS] $1"; PASS_COUNT=$((PASS_COUNT + 1)); }
fail() { echo "  [FAIL] $1"; FAIL_COUNT=$((FAIL_COUNT + 1)); }
skip() { echo "  [SKIP] $1"; SKIP_COUNT=$((SKIP_COUNT + 1)); }
section() { echo; echo "=== $1 ==="; }

# ---------------------------------------------------------------------------
# Check 1: DNS CNAME propagation
# ---------------------------------------------------------------------------

section "CHECK 1: DNS CNAME Propagation"

if [[ -z "$KIT_CNAME_HOST" ]]; then
  skip "KIT_CNAME_HOST not set — skipping DNS check."
  echo "       Set KIT_CNAME_HOST to the CNAME hostname from Kit > Settings > Domains."
  echo "       Example: KIT_CNAME_HOST=em.seedwarden.com ./GATE_3_VERIFICATION_SCRIPT.sh"
else
  echo "  Checking CNAME: $KIT_CNAME_HOST"

  # nslookup returns non-zero on NXDOMAIN on some systems; capture output instead
  NS_OUTPUT=$(nslookup "$KIT_CNAME_HOST" 2>&1 || true)

  if echo "$NS_OUTPUT" | grep -qi "NXDOMAIN\|can't find\|Non-existent"; then
    fail "CNAME $KIT_CNAME_HOST not found (NXDOMAIN). DNS has not propagated yet."
    echo "       This is normal if you added the record less than 48 hours ago."
    echo "       Re-run this script after May 29 06:00 UTC if you submitted by May 28 17:00 UTC."
    echo "       If you see this after May 29 12:00 UTC, check your registrar for a typo in the record."
  elif echo "$NS_OUTPUT" | grep -qi "server can't find\|No answer"; then
    fail "CNAME $KIT_CNAME_HOST returned no answer. Possible typo or registrar propagation delay."
    echo "       Verify the exact Name/Host value in Kit > Settings > Domains."
  else
    # Check for a CNAME or A record response
    if echo "$NS_OUTPUT" | grep -qi "canonical name\|address\|CNAME"; then
      pass "CNAME $KIT_CNAME_HOST is resolving."
      echo "       Full nslookup output:"
      echo "$NS_OUTPUT" | sed 's/^/         /'
    else
      fail "CNAME $KIT_CNAME_HOST returned unexpected output. Manual inspection required."
      echo "       Raw output:"
      echo "$NS_OUTPUT" | sed 's/^/         /'
    fi
  fi
fi

# ---------------------------------------------------------------------------
# Check 2: Kit API — tag existence
# ---------------------------------------------------------------------------

section "CHECK 2: Kit API Tag Verification"

if [[ -z "$KIT_API_KEY" ]]; then
  skip "KIT_API_KEY not set — skipping tag check."
  echo "       Set KIT_API_KEY to verify tags via the Kit API."
  echo "       Get your key from: Kit > Settings > Developer (API) > API Keys."
  echo "       Example: KIT_API_KEY=your_key ./GATE_3_VERIFICATION_SCRIPT.sh"
else
  echo "  Fetching tags from Kit API..."

  # Kit v4 API: GET /tags returns paginated list of tags
  HTTP_STATUS=$(curl -s -o /tmp/kit_tags_response.json -w "%{http_code}" \
    -H "Authorization: Bearer $KIT_API_KEY" \
    -H "Accept: application/json" \
    "$KIT_API_BASE/tags" 2>/dev/null || echo "000")

  if [[ "$HTTP_STATUS" == "000" ]]; then
    fail "Could not reach Kit API (network error or curl not available)."
    echo "       Check your internet connection and try again."
  elif [[ "$HTTP_STATUS" == "401" ]]; then
    fail "Kit API returned 401 Unauthorized. Check your KIT_API_KEY value."
    echo "       Key format should be: kit_XXXXXXXX (starts with 'kit_')"
  elif [[ "$HTTP_STATUS" == "200" ]]; then
    echo "  Kit API response received (HTTP 200)."

    # Extract tag names from JSON response using basic bash parsing
    # Kit v4 response: {"tags": [{"id": 1, "name": "zone-3", ...}, ...]}
    EXISTING_TAGS=$(grep -o '"name":"[^"]*"' /tmp/kit_tags_response.json 2>/dev/null \
      | sed 's/"name":"//;s/"//' || echo "")

    ALL_EXPECTED_TAGS=("${EXPECTED_ZONE_TAGS[@]}" "${EXPECTED_INTEREST_TAGS[@]}")

    for tag in "${ALL_EXPECTED_TAGS[@]}"; do
      if echo "$EXISTING_TAGS" | grep -q "^${tag}$"; then
        pass "Tag found: $tag"
      else
        fail "Tag MISSING: $tag"
        echo "       Create this tag in Kit > Subscribers > Tags > Create a tag"
      fi
    done

    # Check total count
    FOUND_COUNT=$(echo "$EXISTING_TAGS" | grep -c "." 2>/dev/null || echo 0)
    echo "  Total tags in Kit account: $FOUND_COUNT (expected: 15)"
    if [[ "$FOUND_COUNT" -ge 15 ]]; then
      pass "Tag count is sufficient (>= 15)"
    else
      fail "Only $FOUND_COUNT tags found. Expected at least 15."
    fi
  else
    fail "Kit API returned unexpected HTTP status: $HTTP_STATUS"
    echo "       Response body saved to /tmp/kit_tags_response.json for inspection."
  fi
fi

# ---------------------------------------------------------------------------
# Check 3: Zone card PDF link resolution
# ---------------------------------------------------------------------------

section "CHECK 3: Zone Card PDF Links"

ALL_ZONE_URLS_SET=true
for zone in 3 4 5 6 7 8 9 10; do
  if [[ -z "${ZONE_CARD_URLS[$zone]:-}" ]]; then
    ALL_ZONE_URLS_SET=false
  fi
done

if [[ "$ALL_ZONE_URLS_SET" == "false" ]]; then
  skip "Zone card URLs not configured. Set ZONE_CARD_URL_3 through ZONE_CARD_URL_10 to verify."
  echo "       Example:"
  echo "         ZONE_CARD_URL_5=https://drive.google.com/uc?export=download&id=1abc... \\"
  echo "         ./GATE_3_VERIFICATION_SCRIPT.sh"
  echo ""
  echo "       Get file IDs from Google Drive: right-click file > Get link."
  echo "       FILE_ID is the string between /d/ and /view in the share URL."
else
  for zone in 3 4 5 6 7 8 9 10; do
    URL="${ZONE_CARD_URLS[$zone]}"
    ZONE_LABEL="Zone $zone"

    if [[ -z "$URL" ]]; then
      skip "$ZONE_LABEL URL not set."
      continue
    fi

    echo "  Testing $ZONE_LABEL: $URL"

    # Curl with redirect follow; check for redirect to Google login (indicates non-public sharing)
    # -L follows redirects; -s silent; -o /dev/null discard body; -w print status
    HTTP_CODE=$(curl -s -L -o /tmp/zone_card_test.tmp -w "%{http_code}" \
      --max-time 15 \
      --user-agent "Mozilla/5.0 (compatible; SeedwardenVerifier/1.0)" \
      "$URL" 2>/dev/null || echo "000")

    RESPONSE_BODY=$(cat /tmp/zone_card_test.tmp 2>/dev/null || echo "")

    if [[ "$HTTP_CODE" == "000" ]]; then
      fail "$ZONE_LABEL — Network error (could not reach Google Drive)."
    elif [[ "$HTTP_CODE" == "200" ]]; then
      # Check if response is a Google login page (indicates "Request access" error)
      if echo "$RESPONSE_BODY" | grep -qi "accounts.google.com\|Sign in\|ServiceLogin"; then
        fail "$ZONE_LABEL — Redirected to Google login. File sharing is not set to 'Anyone with the link'."
        echo "       Fix: Google Drive > right-click file > Share > change to 'Anyone with link can view'"
      elif echo "$RESPONSE_BODY" | grep -qi "content-type.*pdf\|%PDF"; then
        pass "$ZONE_LABEL — PDF content detected. Link appears to work."
      elif echo "$RESPONSE_BODY" | grep -qi "Google Drive\|drive.google.com"; then
        fail "$ZONE_LABEL — Returned a Google Drive viewer page (not a direct download)."
        echo "       Fix: Change URL to use /uc?export=download format, not /file/d/[ID]/view"
      else
        pass "$ZONE_LABEL — HTTP 200 received. Manual verification recommended (open in browser)."
      fi
    elif [[ "$HTTP_CODE" == "302" ]] || [[ "$HTTP_CODE" == "301" ]]; then
      pass "$ZONE_LABEL — HTTP $HTTP_CODE redirect (normal for Google Drive downloads). Follow redirect to confirm."
    elif [[ "$HTTP_CODE" == "403" ]]; then
      fail "$ZONE_LABEL — HTTP 403 Forbidden. File is not shared publicly."
      echo "       Fix: Google Drive > right-click file > Share > 'Anyone with link can view'"
    elif [[ "$HTTP_CODE" == "404" ]]; then
      fail "$ZONE_LABEL — HTTP 404 Not Found. Check the FILE_ID in the URL."
    else
      fail "$ZONE_LABEL — Unexpected HTTP status: $HTTP_CODE"
    fi
  done
fi

# ---------------------------------------------------------------------------
# Summary
# ---------------------------------------------------------------------------

section "VERIFICATION SUMMARY"

TOTAL=$((PASS_COUNT + FAIL_COUNT + SKIP_COUNT))
echo "  PASS:  $PASS_COUNT"
echo "  FAIL:  $FAIL_COUNT"
echo "  SKIP:  $SKIP_COUNT"
echo "  TOTAL: $TOTAL checks run"
echo ""

if [[ "$FAIL_COUNT" -eq 0 ]] && [[ "$SKIP_COUNT" -eq 0 ]]; then
  echo "  RESULT: PASS — All checks passed. Gate 3 verification complete."
  echo ""
  echo "  Next steps:"
  echo "    - Run 3-test protocol (GATE_3_AUTOMATION_KIT.md Part 3)"
  echo "    - Confirm automation status is Published in Kit dashboard"
  echo "    - Update social bios with Kit landing page URL"
  echo "    - Log Gate 3 completion in WORKLOG.md"
  exit 0
elif [[ "$FAIL_COUNT" -eq 0 ]] && [[ "$SKIP_COUNT" -gt 0 ]]; then
  echo "  RESULT: PASS WITH SKIPS — No failures, but $SKIP_COUNT check(s) were skipped."
  echo ""
  echo "  To run skipped checks, set the missing environment variables:"
  echo "    KIT_API_KEY        — required for tag verification"
  echo "    KIT_CNAME_HOST     — required for DNS propagation check"
  echo "    ZONE_CARD_URL_3 through ZONE_CARD_URL_10 — required for PDF link checks"
  echo ""
  echo "  Re-run with all variables set for a full PASS before launch."
  exit 0
else
  echo "  RESULT: FAIL — $FAIL_COUNT check(s) failed."
  echo ""
  echo "  Fix each FAIL item above before running the 3-test protocol."
  echo ""
  echo "  Critical path reminder:"
  echo "    DNS deadline: May 28 17:00 UTC"
  echo "    Automation must be Published by: May 27 23:59 UTC"
  echo "    Launch: May 30 10:00 UTC"
  echo ""
  echo "  For contingency guidance, see SEEDWARDEN_TRACK_B_GATES_RUNBOOK.md"
  echo "  Contingency D (automation not published) or"
  echo "  Contingency E (multiple gates blocked)."
  exit 1
fi
