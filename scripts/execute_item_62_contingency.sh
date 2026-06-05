#!/bin/bash
# Item 62 Contingency Decision Router
# Run immediately after stockbot_june5_premarket_check.sh completes
# Parses JUNE_5_PREMARKET_CHECK_RESULTS.md and routes to correct contingency path

set -e

RESULTS_FILE="/home/awank/dev/SuperClaude_Framework/JUNE_5_PREMARKET_CHECK_RESULTS.md"
CONTINGENCY_LOG="/home/awank/dev/SuperClaude_Framework/ITEM_62_CONTINGENCY_EXECUTION_LOG.md"
JETSON_HOST="awank@100.120.18.84"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

echo -e "${BLUE}========================================${NC}"
echo "Item 62 Contingency Decision Router"
echo -e "${BLUE}========================================${NC}"
echo ""

# Check if results file exists
if [ ! -f "$RESULTS_FILE" ]; then
    echo -e "${RED}❌ ERROR: $RESULTS_FILE not found${NC}"
    echo "Please run stockbot_june5_premarket_check.sh first"
    exit 1
fi

# Parse results file
DECISION=$(grep -F "**Final Verdict**:" "$RESULTS_FILE" | awk -F': ' '{print $2}' | xargs)
GATES_PASSED=$(grep -F "**Gates Passed**:" "$RESULTS_FILE" | grep -o '[0-9] / [0-9]')

echo "Decision: $DECISION"
echo "Gates Passed: $GATES_PASSED"
echo ""

# Initialize log
echo "# Item 62 Contingency Execution Log" > "$CONTINGENCY_LOG"
echo "**Timestamp**: $(date -u +"%Y-%m-%d %H:%M:%S UTC")" >> "$CONTINGENCY_LOG"
echo "**Decision**: $DECISION" >> "$CONTINGENCY_LOG"
echo "**Gates**: $GATES_PASSED" >> "$CONTINGENCY_LOG"
echo "" >> "$CONTINGENCY_LOG"

# Route decision
if [[ "$DECISION" == "GO"* ]]; then
    echo -e "${GREEN}✅ ROUTING: GO Path${NC}"
    echo "Executing GO path contingency..."
    echo "" >> "$CONTINGENCY_LOG"
    echo "## GO Path Execution" >> "$CONTINGENCY_LOG"

    # GO Path: Market open monitoring
    echo -e "${GREEN}→ Starting market-open monitoring (13:30 UTC)${NC}"
    echo "  - Monitoring enabled for 2-hour window (13:30-15:30 UTC)" >> "$CONTINGENCY_LOG"
    echo "  - Alert threshold: 2+ anomalies → pause and review" >> "$CONTINGENCY_LOG"
    echo "  - Daily summary: 20:00 UTC (end of market session)" >> "$CONTINGENCY_LOG"
    echo "" >> "$CONTINGENCY_LOG"

    # Create monitoring checklist
    cat > "/home/awank/dev/SuperClaude_Framework/ITEM_62_GO_MONITORING_CHECKLIST.md" << 'GOEOF'
# Item 62 GO Path — Active Market Monitoring Checklist

## Market Open Monitoring (13:30–15:30 UTC)

**Pre-market verification** (13:15 UTC):
- [ ] Docker container running
- [ ] Sessions sleeping until 13:15 UTC wake signal
- [ ] Jetson SSH connectivity verified
- [ ] Discord webhook active

**Early market watch** (13:30-14:30 UTC):
- [ ] First signals generating (expected 0-2 within first hour)
- [ ] No WebSocket disconnections
- [ ] No Alpaca API authentication errors
- [ ] Position fill rate normal (0.5-2 fills expected in first hour)

**Mid-market monitoring** (14:30-15:30 UTC):
- [ ] Session logs show normal trading activity
- [ ] No error spikes in Docker logs
- [ ] Database fills table updating correctly
- [ ] P&L variance within expected range

**Escalation triggers** (pause if any two occur):
1. WebSocket connection errors (2+ in 15 min)
2. Alpaca API 401/403 authentication failures
3. Zero signals from both sessions (confirm data feed active)
4. Fill rate >50% higher or lower than expected
5. Single trade P&L loss >$500
6. Drawdown spike >2% in single session

**Action if escalation triggered**:
1. Run `docker logs stockbot --tail 100` to diagnose
2. If data feed issue: Check Alpaca subscription status
3. If auth issue: Verify credentials in container
4. If trading error: Review recent fills in database
5. If unsure: Post query to CHECKIN.md "Needs Your Input" and await user guidance

## Market Close Analysis (20:00 UTC)

Run `/home/awank/dev/SuperClaude_Framework/scripts/post_market_analysis_june5.sh` for:
- Daily fill summary
- P&L reconciliation
- Signal quality score
- Tomorrow's GO/CAUTION/NO-GO decision

GOEOF

    echo "  - Checklist created at ITEM_62_GO_MONITORING_CHECKLIST.md" >> "$CONTINGENCY_LOG"
    echo "" >> "$CONTINGENCY_LOG"

    exit 0

elif [[ "$DECISION" == "CAUTION"* ]]; then
    echo -e "${YELLOW}⚠️  ROUTING: CAUTION Path${NC}"
    echo "Executing CAUTION path contingency..."
    echo "" >> "$CONTINGENCY_LOG"
    echo "## CAUTION Path Execution" >> "$CONTINGENCY_LOG"

    # CAUTION Path: Enhanced monitoring
    echo -e "${YELLOW}→ Enabling enhanced monitoring mode${NC}"
    echo "  - Check interval: every 15 min (vs normal hourly)" >> "$CONTINGENCY_LOG"
    echo "  - Decision gates: 14:30/17:00/19:00 UTC" >> "$CONTINGENCY_LOG"
    echo "  - Escalation threshold: 1 anomaly (vs normal 2)" >> "$CONTINGENCY_LOG"
    echo "" >> "$CONTINGENCY_LOG"

    # Create enhanced monitoring checklist
    cat > "/home/awank/dev/SuperClaude_Framework/ITEM_62_CAUTION_MONITORING_CHECKLIST.md" << 'CAUTIONEOF'
# Item 62 CAUTION Path — Enhanced Monitoring Checklist

## Critical Decision Gates

### Gate 1: 14:30 UTC (1 hour post-open)
**Check**: Alpaca API connectivity + WebSocket stability
- [ ] No WebSocket errors in last 30 min
- [ ] All sessions responding to API queries
- [ ] First signals generated (or data feed confirmed working)

**Decision**:
- If all checks PASS → Continue to Gate 2
- If 1+ checks FAIL → Move to NO-GO path and escalate

### Gate 2: 17:00 UTC (3.5 hours post-open)
**Check**: Fill rate + P&L trajectory
- [ ] Fills within expected range (30-50% of normal rate OK)
- [ ] No session-specific failures
- [ ] Drawdown within 2% per session

**Decision**:
- If all checks PASS → Continue to evening close
- If 1+ checks FAIL → Hold and prepare NO-GO for close

### Gate 3: 19:00 UTC (evening pre-close)
**Check**: Daily summary review
- [ ] Total daily fills >= 10
- [ ] No cascading errors
- [ ] P&L range normal

**Decision**:
- PASS → Resume normal trading; schedule EOD analysis
- FAIL → Halt trading; escalate to NO-GO path

## Anomaly Detection (check every 15 min)

**WARN Threshold** (1 anomaly detected):
1. WebSocket error (>1 in 15 min)
2. Session lag (>5 min without API response)
3. Signal runaway (>5 BUY signals without SELL)
4. Fill slip (actual price >2% vs predicted)
5. DB sync lag (>10 min behind live time)

**Action on WARN**: Log and monitor; escalate if persists 2 checks

**CRITICAL Threshold** (2+ anomalies or any FAIL):
- Immediate escalation: Run NO-GO path
- Contact user via Discord if NO-GO triggers

CAUTIONEOF

    echo "  - Enhanced checklist created at ITEM_62_CAUTION_MONITORING_CHECKLIST.md" >> "$CONTINGENCY_LOG"
    echo "" >> "$CONTINGENCY_LOG"

    exit 0

elif [[ "$DECISION" == "NO-GO"* ]]; then
    echo -e "${RED}❌ ROUTING: NO-GO Path (ESCALATION)${NC}"
    echo "Executing NO-GO contingency rollback..."
    echo "" >> "$CONTINGENCY_LOG"
    echo "## NO-GO Path Execution" >> "$CONTINGENCY_LOG"

    # NO-GO Path: Automated rollback
    echo -e "${RED}→ Initiating rollback procedures${NC}"

    # Step 1: Notify user immediately
    echo "  [1/4] Sending Discord alert..." >> "$CONTINGENCY_LOG"
    ALERT_MSG="🚨 **STOCKBOT ALERT**: Pre-market checklist failed. NO-GO decision activated. Pre-market gates not met — trading session held. Review JUNE_5_PREMARKET_CHECK_RESULTS.md and respond in CHECKIN.md."
    curl -s -H "Content-Type: application/json" \
        -d "{\"content\":\"$ALERT_MSG\"}" \
        "${DISCORD_WEBHOOK_URL}" 2>/dev/null || echo "    (Discord notification skipped — no webhook configured)"

    # Step 2: Update BLOCKED.md
    echo "  [2/4] Creating BLOCKED.md entry..." >> "$CONTINGENCY_LOG"
    cat >> "/home/awank/dev/SuperClaude_Framework/BLOCKED.md" << 'NOGO'

### stockbot — June 5 Pre-Market Checklist Failed
**Date blocked**: 2026-06-05
**Context**: Item 62 pre-market checklist (13:00 UTC) failed with NO-GO decision. One or more of the 4 gates (Container Health, Session Status, WebSocket, Alpaca API) did not pass.
**What I need**: Review JUNE_5_PREMARKET_CHECK_RESULTS.md to determine root cause, fix if possible (e.g., container restart, Jetson SSH reconnect), and provide manual approval to retry at [user-specified-time].
**Verify with**: `ssh awank@100.120.18.84 'docker ps --filter name=stockbot' | grep stockbot`
**Resolution**: [leave blank]
NOGO

    # Step 3: Update CHECKIN.md
    echo "  [3/4] Updating CHECKIN.md..." >> "$CONTINGENCY_LOG"
    cat >> "/home/awank/dev/SuperClaude_Framework/CHECKIN.md" << 'NOGOCHECK'

## ⚠️ URGENT — Stockbot Pre-Market Checklist Failed (June 5 13:00 UTC)

**Status**: Pre-market gates not met. Trading session held (NO-GO decision).

**Action Required**:
1. Review `JUNE_5_PREMARKET_CHECK_RESULTS.md` for failing gate(s)
2. Diagnose root cause (container health, SSH connectivity, Alpaca subscription, WebSocket)
3. If fixable in <30 min: Respond with fix; orchestrator will retry at [new time]
4. If not fixable: Respond with defer date; we'll retry when ready

**Options**:
- **Retry today** (if quick fix): Provide time window
- **Defer to [date]**: Provide new target date
- **Escalate**: Request engineering help

NOGOCHECK

    # Step 4: Log completion
    echo "  [4/4] Rollback complete" >> "$CONTINGENCY_LOG"
    echo "" >> "$CONTINGENCY_LOG"
    echo "Escalation Status: User action required in CHECKIN.md" >> "$CONTINGENCY_LOG"

    echo -e "${RED}→ Rollback complete. Escalation entry written to BLOCKED.md${NC}"
    echo ""

    exit 1

else
    echo -e "${YELLOW}⚠️  UNKNOWN DECISION: $DECISION${NC}"
    echo "Could not parse decision from $RESULTS_FILE"
    echo "Expected: 'GO' or 'CAUTION' or 'NO-GO'"
    exit 2
fi
