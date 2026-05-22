#!/bin/bash
# Jetson Connectivity Diagnostic Script
# Run this to troubleshoot Jetson unreachability issue

JETSON_IP="100.120.18.84"
JETSON_HOSTNAME="xxsb-01"
JETSON_USER="ubuntu"
API_ENDPOINT="http://${JETSON_IP}:8000/api/health"

echo "=== Jetson Connectivity Diagnostic ==="
echo "Target: $JETSON_IP ($JETSON_HOSTNAME)"
echo "Time: $(date -u)"
echo ""

# Test 1: Local network
echo "[1/5] Local network status:"
ip route show default
echo ""

# Test 2: Tailscale connectivity
echo "[2/5] Tailscale status:"
tailscale status 2>&1 | grep -E "^$JETSON_IP|xxsb-01"
echo ""

# Test 3: Ping connectivity
echo "[3/5] Ping test (3 packets):"
timeout 5 ping -c 3 "$JETSON_IP" 2>&1 || echo "❌ Ping FAILED"
echo ""

# Test 4: SSH connectivity
echo "[4/5] SSH connectivity test:"
timeout 10 ssh -o ConnectTimeout=5 -o StrictHostKeyChecking=no "$JETSON_USER@$JETSON_IP" \
  "echo 'SSH Connection: OK'" 2>&1 || echo "❌ SSH FAILED (check credentials)"
echo ""

# Test 5: API health check
echo "[5/5] API health check ($API_ENDPOINT):"
timeout 10 curl -s "$API_ENDPOINT" 2>&1 | head -5 || echo "❌ API TIMEOUT or UNREACHABLE"
echo ""

echo "=== Summary ==="
echo "If ping fails but SSH works: Jetson firewall is blocking ICMP"
echo "If SSH fails: Key auth issue or Jetson offline"
echo "If API times out but SSH works: Docker container may be stopped"
echo ""
echo "NEXT STEPS:"
echo "1. SSH to Jetson: ssh ubuntu@$JETSON_IP"
echo "2. Check processes: ps aux | grep launch_stacker_sessions"
echo "3. Check Docker: docker ps | grep stockbot"
echo "4. Restart if needed: docker restart stockbot"
echo "5. Verify API: curl http://localhost:8000/api/health"
