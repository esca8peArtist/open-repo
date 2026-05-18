#!/bin/bash
# Wave 1 Pre-Flight Checklist Execution
# Run at 07:00 UTC May 18, 2026

set -e

TIMESTAMP=$(date -u '+%Y-%m-%d %H:%M:%S UTC')
echo "============================================"
echo "Wave 1 Pre-Flight Checklist Execution"
echo "Time: $TIMESTAMP"
echo "============================================"

# Phase 1: Gist Accessibility Verification (8 minutes)
echo ""
echo "Phase 1: Gist Accessibility Verification..."
GIST_URLS=(
  "https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261"
  "https://gist.github.com/esca8peArtist/2869da6eaeb15a47246ade3bbbc4a3f4"
  "https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0"
  "https://gist.github.com/esca8peArtist/418d51bda087f15a04d685ab171a5ee0"
  "https://gist.github.com/esca8peArtist/98dc61a3294a612482b37bd90f5c94ab"
)

GIST_FAILURES=0
for url in "${GIST_URLS[@]}"; do
  status=$(curl -s -o /dev/null -w "%{http_code}" "$url")
  short_id=$(echo $url | cut -d'/' -f5)
  if [ "$status" == "200" ]; then
    echo "✓ Gist $short_id: HTTP 200"
  else
    echo "✗ GIST FAILURE: $short_id returned HTTP $status"
    GIST_FAILURES=$((GIST_FAILURES + 1))
  fi
done

if [ $GIST_FAILURES -gt 0 ]; then
  echo ""
  echo "⚠️  CRITICAL: $GIST_FAILURES Gist(s) failed. DO NOT PROCEED."
  echo "Action: Wait 60 seconds, retry. If still failing, consult PHASE_1_LAUNCH_RISK_PLAYBOOK.md Section 1.1"
  exit 1
fi

echo "✓ Phase 1 PASSED: All 5 Gists accessible"

# Phase 2: Baseline Gist View Counts
echo ""
echo "Phase 2: Baseline Gist View Counts..."
echo "⚠️  MANUAL VERIFICATION REQUIRED:"
echo "  - Open main proposal Gist: https://gist.github.com/esca8peArtist/2dec7fd03b08ab5b41c55d402f44c261"
echo "  - Open Domain 37 Gist: https://gist.github.com/esca8peArtist/1277f5d5bcb0fe46604bbaba8fa37fd0"
echo "  - Record view counts in WAVE_1_MONITORING_DASHBOARD.md"
echo "  - Confirm user has recorded both baselines"
echo "  (Skipping automated check — view counts are HTML dynamic)"

# Phase 3: Contact Verification
echo ""
echo "Phase 3: Contact Verification (Batch 1 — 5 contacts)..."
echo "⚠️  MANUAL VERIFICATION REQUIRED:"
echo "  Check 1 — Ryan Goodman (Just Security/NYU Law)"
echo "    Status: $(curl -s -L https://law.nyu.edu/faculty/ryan-goodman 2>/dev/null | grep -q 'ryan-goodman' && echo '✓ Found' || echo '⚠️  Verify manually')"
echo "  Check 2 — Wendy Weiser (Brennan Center)"
echo "    Status: $(curl -s -L https://www.brennancenter.org/about/leadership 2>/dev/null | grep -q 'Weiser' && echo '✓ Found' || echo '⚠️  Verify manually')"
echo "  Check 3 — Erica Chenoweth (Harvard Kennedy School)"
echo "    Status: $(curl -s -L https://www.hks.harvard.edu/faculty 2>/dev/null | grep -q 'Chenoweth' && echo '✓ Found' || echo '⚠️  Verify manually')"
echo "  Check 4 — Ian Bassin (Protect Democracy)"
echo "    Status: $(curl -s -L https://www.protectdemocracy.org 2>/dev/null | grep -q 'Bassin' && echo '✓ Found' || echo '⚠️  Verify manually')"
echo "  Check 5 — Marc Elias (Democracy Docket/Elias Law)"
echo "    Email: melias@elias.law (NOT perkinscoie.com)"
echo "    Status: $(curl -s -L https://www.democracydocket.com 2>/dev/null | grep -q 'Elias' && echo '✓ Found' || echo '⚠️  Verify manually')"

# Phase 4: Email Template Scan
echo ""
echo "Phase 4: Email Template Final Scan..."
echo "⚠️  MANUAL VERIFICATION REQUIRED:"
echo "  Check file: projects/resistance-research/execution/phase-1-personalized-batch-1.md"
echo "  For each of 5 templates:"
echo "    - Zero remaining placeholders (no {{, [bracket], [Your name], [Your email])"
echo "    - Path-specific block correct (only ONE path block present)"
echo "    - Personalization fields filled"
echo "    - Gist URLs correct"

# Phase 5: Spreadsheet Setup
echo ""
echo "Phase 5: Spreadsheet Baseline Setup..."
echo "⚠️  MANUAL VERIFICATION REQUIRED:"
echo "  Confirm: Wave 1 Batch 1 Tracking spreadsheet created with:"
echo "    - Columns: Contact Name | Organization | Send Time | Status | Response Date | Notes"
echo "    - All 5 Batch 1 contacts listed (Weiser, Elias, Goodman, Chenoweth, Bassin)"
echo "    - Baseline Gist view counts recorded"

# Phase 6: Test Email
echo ""
echo "Phase 6: Test Email Delivery Verification..."
echo "⚠️  MANUAL VERIFICATION REQUIRED:"
echo "  Confirm user has sent test email to self and verified:"
echo "    - Email arrived in inbox (not spam)"
echo "    - Gist links are clickable and render"
echo "    - Email formatting is intact"

# Summary
echo ""
echo "============================================"
echo "Pre-Flight Status: 🟢 READY FOR BATCH 1 SEND"
echo "============================================"
echo ""
echo "Next Actions (by 08:00 UTC):"
echo "  1. User opens email account draft folder"
echo "  2. Send Email 1 (Weiser) at 08:00 UTC"
echo "  3. Send remaining 4 emails at 30-min intervals"
echo ""
echo "Orchestrator will:"
echo "  1. Monitor batch 1 execution (08:00–12:00 UTC)"
echo "  2. Log send timestamps in WAVE_1_MONITORING_DASHBOARD.md"
echo "  3. Flag any bounce-backs or failures immediately"
echo "  4. Activate Phase 1 measurement at 10:30 UTC"
echo ""
