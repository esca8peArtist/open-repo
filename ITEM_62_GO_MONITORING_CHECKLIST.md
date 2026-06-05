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

