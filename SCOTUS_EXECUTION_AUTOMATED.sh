#!/bin/bash
# SCOTUS Domain 50 Rapid-Response Execution Script
# Usage: bash SCOTUS_EXECUTION_AUTOMATED.sh <decision_outcome> <gist_url>
# decision_outcome: "FOR" or "REMAND" or "AGAINST"
# gist_url: GitHub Gist URL (e.g., https://gist.github.com/esca8peArtist/abc123def456)

set -e

DECISION=${1:-}
GIST_URL=${2:-}
TIMESTAMP=$(date -u "+%Y-%m-%d %H:%M:%S UTC")
RESPONSE_LOG="/home/awank/dev/SuperClaude_Framework/projects/resistance-research/SCOTUS_DECISION_LOG.md"

if [ -z "$DECISION" ] || [ -z "$GIST_URL" ]; then
    echo "❌ USAGE: bash SCOTUS_EXECUTION_AUTOMATED.sh <FOR|REMAND|AGAINST> <gist_url>"
    echo "Example: bash SCOTUS_EXECUTION_AUTOMATED.sh FOR https://gist.github.com/esca8peArtist/abc123def456"
    exit 1
fi

echo "🟢 SCOTUS RAPID-RESPONSE EXECUTION"
echo "========================================"
echo "Decision: $DECISION"
echo "Gist URL: $GIST_URL"
echo "Time: $TIMESTAMP"
echo ""

# Validate decision
if [[ "$DECISION" != "FOR" && "$DECISION" != "AGAINST" && "$DECISION" != "REMAND" ]]; then
    echo "❌ Invalid decision. Must be FOR, AGAINST, or REMAND."
    exit 1
fi

# Fill Gist URL in templates
echo "📝 Step 1: Filling Gist URL in templates..."
cd /home/awank/dev/SuperClaude_Framework/projects/resistance-research

# Count unfilled placeholders
UNFILLED=$(grep -r "INSERT GIST URL" . | wc -l)
echo "   Found $UNFILLED unfilled placeholders"

if [ $UNFILLED -gt 0 ]; then
    # Replace all placeholders with the actual Gist URL
    find . -name "*.md" -exec sed -i "s|\[INSERT GIST URL HERE\]|$GIST_URL|g" {} \;
    echo "   ✅ Filled all placeholders"
else
    echo "   ✅ All placeholders already filled"
fi

# Log decision outcome
echo ""
echo "📋 Step 2: Logging decision outcome..."
cat >> "$RESPONSE_LOG" << EOL

## Little v. Hecox Decision — $TIMESTAMP

**Decision Outcome**: $DECISION
**Gist URL**: $GIST_URL
**Execution Time**: $TIMESTAMP

EOL
echo "   ✅ Decision logged"

# Execute sends if favorable
if [[ "$DECISION" == "FOR" || "$DECISION" == "REMAND" ]]; then
    echo ""
    echo "✉️ Step 3: Preparing Tier 1 sends..."
    echo "   Templates filled and ready in SCOTUS_TRIGGER_5MIN_ACTION_GUIDE.md"
    echo "   Next: Copy-paste templates to Lambda Legal, AT4E, NCTE emails"
    echo "   See SCOTUS_DECISION_RAPID_RESPONSE_FLOWCHART.md for template details"

    echo ""
    echo "🚀 RAPID-RESPONSE READY"
    echo "   Templates: SCOTUS_TRIGGER_5MIN_ACTION_GUIDE.md (Templates A/B/C or D)"
    echo "   Contact list: SCOTUS_TRIGGER_5MIN_ACTION_GUIDE.md (Tier 1)"
    echo "   Follow-up guide: SCOTUS_TRIGGER_1HOUR_ACTION_GUIDE.md (Tier 2, 5-60 min window)"
else
    echo ""
    echo "ℹ️  Decision unfavorable — no immediate activation"
    echo "   Proceed with scheduled August 1 Domain 50 distribution"
fi

echo ""
echo "✅ EXECUTION COMPLETE"
echo "   Gist URL filled in all templates"
echo "   Decision outcome logged"
git add -A
git commit -m "chore(orchestrator): SCOTUS decision execution — $DECISION outcome + Gist URL filled"

