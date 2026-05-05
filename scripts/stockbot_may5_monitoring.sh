#!/bin/bash
# Stockbot May 5 2026 Market Open Monitoring Script
# Run at 11:30 UTC (2h before market open), 13:15 UTC (market open), and 20:00 UTC (market close)

set -e

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

JETSON_IP="100.120.18.84"
JETSON_USER="awank"
TIMESTAMP=$(date -u "+%Y-%m-%d %H:%M:%S UTC")

echo -e "${BLUE}=== Stockbot May 5 Monitoring ===${NC}"
echo "Timestamp: $TIMESTAMP"
echo ""

# 1. Check Jetson connectivity
echo -e "${YELLOW}1. Jetson Connectivity...${NC}"
if ssh -T "${JETSON_USER}@${JETSON_IP}" "echo ok" &>/dev/null; then
    echo -e "${GREEN}✓ SSH access verified${NC}"
else
    echo -e "${RED}✗ SSH access FAILED${NC}"
    exit 1
fi
echo ""

# 2. Check Docker container status
echo -e "${YELLOW}2. Docker Container Status...${NC}"
CONTAINER_STATUS=$(ssh "${JETSON_USER}@${JETSON_IP}" "docker inspect stockbot --format='{{.State.Status}}' 2>/dev/null || echo 'missing'")
if [ "$CONTAINER_STATUS" = "running" ]; then
    echo -e "${GREEN}✓ Container running${NC}"
    UPTIME=$(ssh "${JETSON_USER}@${JETSON_IP}" "docker stats --no-stream stockbot --format='{{.MemPerc}}' 2>/dev/null | head -1")
    echo "  Memory: $UPTIME"
else
    echo -e "${RED}✗ Container status: $CONTAINER_STATUS${NC}"
fi
echo ""

# 3. Check database connectivity
echo -e "${YELLOW}3. Database Check...${NC}"
POSITION_COUNT=$(ssh "${JETSON_USER}@${JETSON_IP}" "sqlite3 /home/awank/stockbot.db 'SELECT COUNT(*) FROM positions WHERE status=\"OPEN\";' 2>/dev/null || echo 'error'")
if [ "$POSITION_COUNT" != "error" ]; then
    echo -e "${GREEN}✓ Database connected${NC}"
    echo "  Open positions: $POSITION_COUNT"
else
    echo -e "${RED}✗ Database query failed${NC}"
fi
echo ""

# 4. Check API health
echo -e "${YELLOW}4. API Health Check...${NC}"
API_RESPONSE=$(ssh "${JETSON_USER}@${JETSON_IP}" "timeout 3 curl -s http://localhost:8000/api/ready 2>/dev/null | head -c 20 || echo 'timeout'")
if [ "$API_RESPONSE" != "timeout" ]; then
    echo -e "${GREEN}✓ API responding${NC}"
    echo "  Response: ${API_RESPONSE:0:50}..."
else
    echo -e "${YELLOW}⚠ API endpoint timeout (not critical for trading)${NC}"
fi
echo ""

# 5. Check Discord webhook
echo -e "${YELLOW}5. Discord Webhook Test...${NC}"
if [ -z "$STOCKBOT_DISCORD_WEBHOOK_URL" ]; then
    echo -e "${RED}✗ Discord webhook URL not set${NC}"
else
    WEBHOOK_STATUS=$(curl -s -o /dev/null -w "%{http_code}" -X POST "$STOCKBOT_DISCORD_WEBHOOK_URL" -H "Content-Type: application/json" -d "{\"content\":\"[May 5 Monitoring] Health check at $TIMESTAMP\"}" 2>/dev/null)
    if [ "$WEBHOOK_STATUS" = "204" ]; then
        echo -e "${GREEN}✓ Discord webhook working${NC}"
    else
        echo -e "${RED}✗ Discord webhook returned HTTP $WEBHOOK_STATUS${NC}"
    fi
fi
echo ""

# 6. Check log files
echo -e "${YELLOW}6. Recent Log Activity...${NC}"
LATEST_LOG=$(ssh "${JETSON_USER}@${JETSON_IP}" "ls -t /home/awank/logs/trading_*.log 2>/dev/null | head -1 || echo 'not-found'")
if [ "$LATEST_LOG" != "not-found" ]; then
    echo -e "${GREEN}✓ Log file: $LATEST_LOG${NC}"
    LAST_ENTRY=$(ssh "${JETSON_USER}@${JETSON_IP}" "tail -1 $LATEST_LOG 2>/dev/null")
    echo "  Last entry: ${LAST_ENTRY:0:80}..."
else
    echo -e "${RED}✗ No log files found${NC}"
fi
echo ""

echo -e "${BLUE}=== Monitoring Complete ===${NC}"
echo "Next check: 2h before market open (11:30 UTC) or at market open (13:30 UTC)"
