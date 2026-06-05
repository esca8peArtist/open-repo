#!/bin/bash
# Stockbot June 5 Pre-Market Checklist
# Run at 13:00 UTC (before 13:15 UTC)
# Decision: GO / CAUTION / NO-GO for market open at 13:30 UTC

set -e

RESULTS_FILE="/home/awank/dev/SuperClaude_Framework/JUNE_5_PREMARKET_CHECK_RESULTS.md"
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")
GATE_COUNT=0
GATE_PASS=0

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo "==============================================="
echo "Stockbot June 5 Pre-Market Checklist"
echo "Start time: $TIMESTAMP"
echo "==============================================="
echo ""

# Initialize results file
cat > "$RESULTS_FILE" << 'EOF'
# Stockbot June 5 Pre-Market Check Results
EOF

# Gate 1: Container Health
echo "GATE 1: Container Health"
GATE_COUNT=$((GATE_COUNT + 1))
GATE_1_RESULT=$(ssh awank@100.120.18.84 'docker ps --filter name=stockbot' 2>/dev/null | grep stockbot | awk '{print $5}' || echo "FAIL")
if echo "$GATE_1_RESULT" | grep -q "Up"; then
    echo -e "${GREEN}✅ PASS${NC} — Container is running"
    GATE_PASS=$((GATE_PASS + 1))
    GATE_1_STATUS="PASS"
else
    echo -e "${RED}❌ FAIL${NC} — Container not healthy"
    GATE_1_STATUS="FAIL"
fi
echo "  Status: $GATE_1_RESULT"
echo ""

# Gate 2: Session Status (count session logs in last hour)
echo "GATE 2: Active Sessions"
GATE_COUNT=$((GATE_COUNT + 1))
SESSION_COUNT=$(ssh awank@100.120.18.84 'docker logs stockbot --since 1h 2>/dev/null' | grep -c "Session.*001" || echo "0")
# Expect at least 4 log entries (2 sessions × ~2 cycles/hr)
if [ "$SESSION_COUNT" -ge 4 ]; then
    echo -e "${GREEN}✅ PASS${NC} — Sessions active"
    GATE_PASS=$((GATE_PASS + 1))
    GATE_2_STATUS="PASS"
else
    echo -e "${YELLOW}⚠️  CAUTION${NC} — Low session activity ($SESSION_COUNT cycles in last hour)"
    GATE_2_STATUS="CAUTION"
fi
echo "  Session cycles: $SESSION_COUNT (expected ≥4)"
echo ""

# Gate 3: WebSocket Stability (check for connection errors in last 30 min)
echo "GATE 3: WebSocket Stability"
GATE_COUNT=$((GATE_COUNT + 1))
WS_ERRORS=$(ssh awank@100.120.18.84 'docker logs stockbot --since 30m 2>/dev/null' | grep -c "connection limit exceeded\|WebSocket.*error" || echo "0")
if [ "$WS_ERRORS" -eq 0 ]; then
    echo -e "${GREEN}✅ PASS${NC} — No WebSocket errors"
    GATE_PASS=$((GATE_PASS + 1))
    GATE_3_STATUS="PASS"
else
    echo -e "${YELLOW}⚠️  CAUTION${NC} — WebSocket errors detected"
    GATE_3_STATUS="CAUTION"
fi
echo "  Errors in last 30 min: $WS_ERRORS"
echo ""

# Gate 4: Alpaca API Connectivity
echo "GATE 4: Alpaca API Health"
GATE_COUNT=$((GATE_COUNT + 1))
API_RESPONSE=$(ssh awank@100.120.18.84 'ALPACA_KEY=$(grep "^ALPACA_API_KEY_ID=" /opt/stockbot/.env 2>/dev/null | cut -d= -f2); curl -s -H "APCA-API-KEY-ID: $ALPACA_KEY" https://paper-api.alpaca.markets/v2/account 2>/dev/null | grep -q "equity" && echo "OK" || echo "FAIL"' || echo "FAIL")
if [ "$API_RESPONSE" = "OK" ]; then
    echo -e "${GREEN}✅ PASS${NC} — Alpaca API responsive"
    GATE_PASS=$((GATE_PASS + 1))
    GATE_4_STATUS="PASS"
else
    echo -e "${RED}❌ FAIL${NC} — Alpaca API unreachable or invalid credentials"
    GATE_4_STATUS="FAIL"
fi
echo "  API Status: $API_RESPONSE"
echo ""

# Decision Logic
echo "==============================================="
echo "DECISION LOGIC"
echo "==============================================="
echo "Gates Passed: $GATE_PASS / $GATE_COUNT"
echo ""

DECISION=""
if [ "$GATE_1_STATUS" = "PASS" ] && [ "$GATE_4_STATUS" = "PASS" ] && ([ "$GATE_2_STATUS" = "PASS" ] || [ "$GATE_3_STATUS" = "CAUTION" ]); then
    if [ "$GATE_PASS" -eq 4 ]; then
        DECISION="GO"
        COLOR=$GREEN
    elif [ "$GATE_PASS" -ge 3 ]; then
        DECISION="GO (with monitoring)"
        COLOR=$GREEN
    else
        DECISION="HOLD"
        COLOR=$YELLOW
    fi
elif [ "$GATE_PASS" -le 2 ]; then
    DECISION="NO-GO (Escalate)"
    COLOR=$RED
else
    DECISION="CAUTION"
    COLOR=$YELLOW
fi

echo -e "${COLOR}DECISION: $DECISION${NC}"
echo ""

# Write results to file
cat >> "$RESULTS_FILE" << EOF

**Timestamp**: $TIMESTAMP
**Gates Passed**: $GATE_PASS / $GATE_COUNT

## Gate Results

| Gate | Status | Detail |
|------|--------|--------|
| 1: Container Health | $GATE_1_STATUS | $GATE_1_RESULT |
| 2: Session Status | $GATE_2_STATUS | $SESSION_COUNT cycles in last hour |
| 3: WebSocket Stability | $GATE_3_STATUS | $WS_ERRORS errors in last 30 min |
| 4: Alpaca API | $GATE_4_STATUS | $API_RESPONSE |

## Decision

**Final Verdict**: $DECISION

## Next Actions

- Decision time: 13:00 UTC
- Market open: 13:30 UTC
- If GO/GO-CAUTION: Resume normal trading execution at 13:30 UTC
- If NO-GO: Escalate to BLOCKED.md + notify user
EOF

echo "Results written to: $RESULTS_FILE"
echo ""
echo "Check-in complete at $(date -u +"%H:%M:%S UTC")"
