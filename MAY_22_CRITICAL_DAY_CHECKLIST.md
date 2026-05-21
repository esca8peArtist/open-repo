# May 22 Critical Day Checklist (2026-05-21 22:34 UTC)

**CRITICAL DEADLINE**: May 22 13:30 UTC (14h 56m remaining as of 22:34 UTC)

---

## OPTION A: SSH Authorization (Preferred, No Manual Action Required)
If you have access to Jetson with YOUR credentials, authorize the orchestrator's public key one time:

```bash
# From Jetson (via your own SSH access):
ssh ubuntu@100.120.18.84
# (authenticate with your password/key)
# Then on Jetson:
echo "$(cat ~/.ssh/id_ed25519.pub)" >> ~/.ssh/authorized_keys
# Verify orchestrator can now connect:
exit
ssh -i /home/awank/.ssh/id_ed25519 ubuntu@100.120.18.84 'echo OK'
```

**Outcome**: Orchestrator gains persistent SSH access. May 22 checkpoint executes automatically. All future Jetson fixes can be pushed autonomously.

**Estimated time**: 5 minutes

---

## OPTION B: Manual Config Fix (If No Jetson Access)
If you don't have Jetson access, you can fix the Lever B config directly:

```bash
# From your machine (via SSH access):
ssh ubuntu@100.120.18.84  # (use your credentials)
nano /opt/stockbot/config/active-sessions-2session.json
```

**Find and edit both session blocks** (search for "AAPL_h10" or "AAPL_h11"):

```json
{
  "stacker_name": "AAPL_h10_lgbm_ho",
  "threshold_multiplier": 0.4,
  "confidence_floor": 0.45,
  "strategy_params": {
    "hmm_regime_masking": true,        // ← ADD THIS LINE if missing
    "hmm_observe_mode": false,
    "hmm_min_fit_bars": 60,
    "hmm_suppress_buy_in_bear": true
  }
}
```

**Do this for BOTH sessions** (lgbm_ho and ridge_wf).

```bash
# Save (Ctrl+X, Y, Enter)
# Restart trading engine:
docker restart stockbot
# Verify health endpoint:
curl http://localhost:8000/api/health
# Should return: {"status":"ok","sessions":2}
```

**Estimated time**: 5 minutes

---

## WHAT HAPPENS ON MAY 22 (Regardless of SSH Fix)

**13:30 UTC**: Market opens. Checkpoint will execute as scheduled with ONE of two outcomes:

### If SSH is Fixed Before 13:30 UTC
- Orchestrator connects, updates config automatically if needed
- May 19 STILL_MISS_B2 + Lever B config = we now test Lever B's HMM regime masking
- Checkpoint executes with correct config
- **OUTCOME**: Clear Go/No-Go signal for Lever B viability

### If SSH is NOT Fixed Before 13:30 UTC
- Checkpoint executes with current (May 19) configuration
- Result is likely another STILL_MISS_B2 (same as May 19, since config unchanged)
- **No failure — just repetition of May 19 state**
- May 23 decision becomes: "Lever A is stable, Lever B fix can wait until post-checkpoint"

---

## MAY 23 DECISION WINDOW

Regardless of May 22 outcome:

1. **Read May 22 checkpoint result**
2. **Consult `MAY_22_CHECKPOINT_DECISION_ROADMAP.md`** (all decision paths documented)
3. **Pick next action**:
   - PASS → multi-ticker scaling, Gate 2 design
   - NEAR-MISS → keep current config, watch May 14 for SELL signal completion
   - FAR-MISS → evaluate Lever C options
   - SYSTEM FAILURE → investigate and adjust

---

## MINIMUM VIABLE ACTION (REQUIRED BY 13:30 UTC)

**Pick ONE:**

- [ ] **Option A**: SSH authorize orchestrator key (5 min, persistent solution)
- [ ] **Option B**: Manually SSH fix and restart Docker (5 min, one-time fix)
- [ ] **Option C**: Take no action (checkpoint runs as-is, likely repeats May 19)

**All three are viable**. Option A is cleanest for future runs. Option B works today. Option C is safe (no change = no new failures).

---

## AFTER MAY 22

1. Checkpoint result lands in logs (auto-parsed)
2. Orchestrator makes decision available by ~15:00 UTC (post-market-close analysis)
3. `MAY_22_CHECKPOINT_DECISION_ROADMAP.md` provides all next-step options
4. No other projects are blocked on this outcome

---

**Contact**: Orchestrator will NOT reach out. Checkpoint executes regardless. You decide next steps at leisure on May 23.

**Questions**: All decision logic is in `MAY_22_CHECKPOINT_DECISION_ROADMAP.md` (Session 1447).
