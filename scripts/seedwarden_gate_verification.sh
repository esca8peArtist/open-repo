#!/bin/bash
# Seedwarden Gates 1-2 Verification Script
# Purpose: Check if Gates 1-2 are complete by May 26 23:59 UTC
# Usage: bash /home/awank/dev/SuperClaude_Framework/scripts/seedwarden_gate_verification.sh

SEEDWARDEN_DIR="/home/awank/dev/SuperClaude_Framework/projects/seedwarden"
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

echo "================================"
echo "Seedwarden Gate Verification"
echo "Timestamp: $TIMESTAMP"
echo "================================"

# Check for indicators of completed gates
# Gate 1: Instagram, TikTok, Pinterest account creation
# Gate 2: Canva Brand Kit setup

# Look for gate completion markers or documentation
if [ -f "$SEEDWARDEN_DIR/GATE_1_COMPLETION_STATUS.md" ]; then
    echo "✅ Gate 1 completion status file found"
    grep -E "COMPLETE|PASSED|✅" "$SEEDWARDEN_DIR/GATE_1_COMPLETION_STATUS.md" && echo "Gate 1: APPEARS COMPLETE" || echo "Gate 1: Status unclear"
else
    echo "⏳ Gate 1: No completion status file found"
fi

if [ -f "$SEEDWARDEN_DIR/GATE_2_COMPLETION_STATUS.md" ]; then
    echo "✅ Gate 2 completion status file found"
    grep -E "COMPLETE|PASSED|✅" "$SEEDWARDEN_DIR/GATE_2_COMPLETION_STATUS.md" && echo "Gate 2: APPEARS COMPLETE" || echo "Gate 2: Status unclear"
else
    echo "⏳ Gate 2: No completion status file found"
fi

# Fallback: Check for updated PROJECTS.md with gate status
echo ""
echo "Current PROJECTS.md seedwarden status:"
grep -A 5 "Critical path" "$SEEDWARDEN_DIR"/../PROJECTS.md | head -10 || echo "Could not find status in PROJECTS.md"

echo ""
echo "================================"
echo "Verification complete at: $(date -u +"%Y-%m-%d %H:%M:%S UTC")"
echo "================================"
echo ""
echo "If gates are NOT complete by this time:"
echo "→ Activate June 6 or June 15 contingency slip"
echo "→ See MAY_30_DECISION_GATE_CONTINGENCY_PLAYBOOK.md for fallback dates"
