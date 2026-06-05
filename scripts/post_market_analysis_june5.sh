#!/bin/bash
# Stockbot June 5 Post-Market Analysis (20:00 UTC)
# Run at market close (20:00 UTC) to analyze trading performance
# Outputs GO/CAUTION/NO-GO for June 6 continuation

set -e

JETSON_HOST="awank@100.120.18.84"
ANALYSIS_FILE="/home/awank/dev/SuperClaude_Framework/JUNE_5_POSTMARKET_ANALYSIS.md"
TIMESTAMP=$(date -u +"%Y-%m-%d %H:%M:%S UTC")

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo "Stockbot June 5 Post-Market Analysis"
echo "Analysis time: $TIMESTAMP"
echo -e "${BLUE}========================================${NC}"
echo ""

# Initialize analysis file
cat > "$ANALYSIS_FILE" << 'EOF'
# Stockbot June 5 Post-Market Analysis

EOF

echo "Timestamp: $TIMESTAMP" >> "$ANALYSIS_FILE"
echo "" >> "$ANALYSIS_FILE"

# Step 1: Query Alpaca fills for today
echo -e "${BLUE}[1/5] Querying Alpaca fills for June 5...${NC}"
FILL_SUMMARY=$(ssh "$JETSON_HOST" <<'SSHEOF'
# Query Alpaca paper account for fills since market open (13:30 UTC)
ALPACA_KEY=$(grep "^ALPACA_API_KEY_ID=" /opt/stockbot/.env 2>/dev/null | cut -d= -f2)
FILL_COUNT=$(curl -s -H "APCA-API-KEY-ID: $ALPACA_KEY" \
    'https://paper-api.alpaca.markets/v2/orders?status=closed' 2>/dev/null | \
    grep -o '"filled_at"' | wc -l 2>/dev/null || echo "0")
echo "$FILL_COUNT"
SSHEOF
)

echo "  Fills today: $FILL_SUMMARY" >> "$ANALYSIS_FILE"
echo "  ✓ Fill count: $FILL_SUMMARY"
echo ""

# Step 2: Query database for trading metrics
echo -e "${BLUE}[2/5] Analyzing trading database...${NC}"
DB_SUMMARY=$(ssh "$JETSON_HOST" <<'SSHEOF'
sqlite3 /opt/stockbot/database/trading.db <<SQL
SELECT
  COUNT(*) as total_trades,
  COUNT(CASE WHEN action='BUY' THEN 1 END) as buys,
  COUNT(CASE WHEN action='SELL' THEN 1 END) as sells,
  ROUND(SUM(CASE WHEN action='BUY' THEN realized_pnl ELSE 0 END), 2) as realized_pnl
FROM trades
WHERE DATE(timestamp) = '2026-06-05';
SQL
SSHEOF
)

echo "Database Summary:" >> "$ANALYSIS_FILE"
echo '```' >> "$ANALYSIS_FILE"
echo "$DB_SUMMARY" >> "$ANALYSIS_FILE"
echo '```' >> "$ANALYSIS_FILE"

# Step 3: Check for errors in Docker logs
echo -e "${BLUE}[3/5] Checking for trading errors...${NC}"
ERROR_COUNT=$(ssh "$JETSON_HOST" 'docker logs stockbot --since 6h 2>/dev/null | grep -i "error\|fail\|exception" | wc -l' || echo "0")
echo "  Error count (last 6h): $ERROR_COUNT" >> "$ANALYSIS_FILE"

if [ "$ERROR_COUNT" -gt 5 ]; then
    echo -e "${YELLOW}  ⚠️  Multiple errors detected ($ERROR_COUNT). See details below.${NC}"
    ERROR_DETAIL=$(ssh "$JETSON_HOST" 'docker logs stockbot --since 6h 2>/dev/null | grep -i "error\|fail\|exception" | tail -5' || echo "No errors found")
    echo "Recent errors:" >> "$ANALYSIS_FILE"
    echo '```' >> "$ANALYSIS_FILE"
    echo "$ERROR_DETAIL" >> "$ANALYSIS_FILE"
    echo '```' >> "$ANALYSIS_FILE"
else
    echo -e "${GREEN}  ✓ Error count acceptable ($ERROR_COUNT)${NC}"
fi
echo ""

# Step 4: Signal quality score
echo -e "${BLUE}[4/5] Computing signal quality score...${NC}"

# Signal quality: fills / expected fills for day
EXPECTED_FILLS=$(echo "$FILL_SUMMARY" | awk '{print int($1 / 6 * 5)}')  # Expect ~30 fills in 6.5 hours
if [ -z "$FILL_SUMMARY" ] || [ "$FILL_SUMMARY" = "0" ]; then
    SIGNAL_QUALITY=0
else
    SIGNAL_QUALITY=$(awk "BEGIN {printf \"%.1f\", ($FILL_SUMMARY / 30) * 10}")
fi

echo "Signal Quality Score: $SIGNAL_QUALITY / 10.0" >> "$ANALYSIS_FILE"

if (( $(echo "$SIGNAL_QUALITY >= 6.0" | bc -l) )); then
    SIGNAL_STATUS="EXCELLENT"
    COLOR=$GREEN
elif (( $(echo "$SIGNAL_QUALITY >= 4.0" | bc -l) )); then
    SIGNAL_STATUS="GOOD"
    COLOR=$GREEN
elif (( $(echo "$SIGNAL_QUALITY >= 2.0" | bc -l) )); then
    SIGNAL_STATUS="CAUTION"
    COLOR=$YELLOW
else
    SIGNAL_STATUS="POOR"
    COLOR=$RED
fi

echo "  ✓ Signal status: $SIGNAL_STATUS"
echo ""

# Step 5: Decision logic
echo -e "${BLUE}[5/5] Computing GO/CAUTION/NO-GO decision...${NC}"

echo "" >> "$ANALYSIS_FILE"
echo "## Decision Logic" >> "$ANALYSIS_FILE"
echo "" >> "$ANALYSIS_FILE"
echo "**Criteria**:" >> "$ANALYSIS_FILE"
echo "- Fills: $FILL_SUMMARY (expected ≥20 for GO)" >> "$ANALYSIS_FILE"
echo "- Signal Quality: $SIGNAL_QUALITY / 10.0 (expected ≥6.0 for GO)" >> "$ANALYSIS_FILE"
echo "- Errors: $ERROR_COUNT (expected <3 for GO)" >> "$ANALYSIS_FILE"
echo "" >> "$ANALYSIS_FILE"

# Determine decision
if [ "$FILL_SUMMARY" -ge 20 ] && (( $(echo "$SIGNAL_QUALITY >= 6.0" | bc -l) )) && [ "$ERROR_COUNT" -lt 3 ]; then
    DECISION="GO"
    DECISION_COLOR=$GREEN
elif [ "$FILL_SUMMARY" -ge 10 ] && (( $(echo "$SIGNAL_QUALITY >= 4.0" | bc -l) )); then
    DECISION="CAUTION (continue with monitoring)"
    DECISION_COLOR=$YELLOW
else
    DECISION="NO-GO (hold until next checkpoint)"
    DECISION_COLOR=$RED
fi

echo "**Final Decision**: $DECISION" >> "$ANALYSIS_FILE"
echo "" >> "$ANALYSIS_FILE"
echo "## Next Steps" >> "$ANALYSIS_FILE"
echo "" >> "$ANALYSIS_FILE"

if [[ "$DECISION" == "GO"* ]]; then
    echo "- ✅ Market execution normal" >> "$ANALYSIS_FILE"
    echo "- Continue trading June 6" >> "$ANALYSIS_FILE"
    echo "- Repeat daily analysis at 20:00 UTC" >> "$ANALYSIS_FILE"
elif [[ "$DECISION" == "CAUTION"* ]]; then
    echo "- ⚠️  Performance acceptable but not optimal" >> "$ANALYSIS_FILE"
    echo "- Enable enhanced monitoring (15-min checks)" >> "$ANALYSIS_FILE"
    echo "- Decision gate at June 6 15:00 UTC" >> "$ANALYSIS_FILE"
else
    echo "- ❌ Stop trading and escalate" >> "$ANALYSIS_FILE"
    echo "- Root cause analysis required" >> "$ANALYSIS_FILE"
    echo "- User decision required" >> "$ANALYSIS_FILE"
fi

echo ""
echo -e "${DECISION_COLOR}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo -e "${DECISION_COLOR}DECISION: $DECISION${NC}"
echo -e "${DECISION_COLOR}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━${NC}"
echo ""

echo "Analysis written to: $ANALYSIS_FILE"
echo "Check-in complete at $(date -u +"%H:%M:%S UTC")"
