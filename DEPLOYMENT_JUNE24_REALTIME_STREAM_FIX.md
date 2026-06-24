# June 24 Real-Time Stream Timeout Fix — Post-Market Deployment

## Summary

**Root Cause**: `asyncio.wait_for(stream._run_forever(), timeout=300)` killed working connections every 5 minutes, triggering circuit-breaker after 3 consecutive failures during 13:30–13:50 UTC validation window.

**Fix**: Removed the 300-second timeout wrapper. Let `_run_forever()` run indefinitely with exception handler safeguards.

**Status**: ✅ Committed (d4b675ba), tested (72/72 tests pass)

**Deployment Window**: 20:30–21:00 UTC (post-market, after trading halts at 20:00 UTC)

---

## Deployment Checklist

### Pre-Deployment (20:00 UTC)
- [ ] Trading halted cleanly at market close (20:00 UTC)
- [ ] Jetson accessible via SSH (test: `ssh awank@100.120.18.84 "echo OK"`)
- [ ] Current Docker container still running (`docker ps | grep stockbot`)
- [ ] Code synced from local master (commit d4b675ba present)

### Deployment Steps (20:30 UTC)

**Step 1: Sync Code to Jetson**
```bash
cd /home/awank/dev/SuperClaude_Framework/projects/stockbot
bash scripts/deploy-to-jetson.sh
```

**Step 2: Verify Code Sync**
```bash
ssh awank@100.120.18.84 "grep -A 2 'await self.stream._run_forever' /opt/stockbot/src/data/realtime_stream.py"
```
Expected: Should show `await self.stream._run_forever()` WITHOUT `asyncio.wait_for(...)` wrapper.

**Step 3: Restart Container**
```bash
ssh awank@100.120.18.84 "docker restart stockbot"
```

**Step 4: Verify Container Health (30s)**
```bash
ssh awank@100.120.18.84 "docker logs stockbot --tail=20 2>&1 | grep -E 'started|stream|connection'"
```
Expected: Should show `started data stream` and `starting data websocket connection` logs.

**Step 5: Verify API Endpoint (60s)**
```bash
ssh awank@100.120.18.84 "curl -s http://100.120.18.84:8000/api/health | jq ."
```
Expected: `{"status":"ok","sessions":5}`

### Post-Deployment Verification

**June 25 Pre-Market (13:15 UTC)**
- Phase 0 gates: Docker health, sessions initialized, clock verification
- Phase 1 gates: Market open detection, signal cycle begins

**June 25 Market Open (13:30 UTC)**
- Stream should NOT timeout
- All 5 sessions should generate signals
- No circuit-breaker alerts expected

---

## Rollback Plan

If stream still times out after fix:
1. **Revert to previous image**: `docker stop stockbot && docker run [with old image]`
2. **Option B**: Implement activity-based timeout (only timeout if NO ticks for 10 minutes)
3. **Option C**: Switch to historical bar polling (lose tick granularity, gain resilience)

Time to rollback: <5 minutes (container restart)

---

## Timeline

- **14:30 UTC (Session 4187)**: Root cause identified, fix committed, tests passed
- **20:00 UTC**: Market close
- **20:30 UTC**: Begin deployment
- **20:50 UTC**: Deployment complete, health verified
- **June 25 13:15 UTC**: Begin Phase 0 pre-market gates
- **June 25 13:30 UTC**: Market open, validation window begins

---

## Success Criteria

✅ **Deployment Success**:
- Code synced to Jetson without errors
- Docker container restarts cleanly
- API health endpoint returns 200 OK
- No timeout-related logs in first 60s after restart

✅ **Validation Success** (June 25 13:30 UTC):
- All 5 sessions detect market open
- Stream runs > 1 minute without timeout
- Signals generated (buy_prob > 0 for at least one session)
- Zero circuit-breaker alerts

---

## Notes

- The fix removes the timeout entirely. This is safe because:
  - `_run_forever()` is designed to run indefinitely
  - WebSocket exceptions are caught and handled in the stream's internal loop
  - Only explicit `stop()` calls or clean stream exits (e.g., outside market hours) will stop the stream
  - This matches the intended design of `_run_forever()` — a self-managing coroutine that runs "forever"

- If we need a safeguard timeout in the future, should be activity-based (no ticks for 10+ minutes) rather than hard time-based.
