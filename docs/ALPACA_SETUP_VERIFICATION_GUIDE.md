# Alpaca Account Setup Verification Guide

**Purpose**: Ensure your Alpaca paper trading account is correctly configured to support the stockbot live trading engine restart (critical before 2026-04-28 14:30 UTC market open).

**Status Context**: Session 596 identified insufficient day-trading buying power error (code 40310000). This guide walks through verification and recovery.

---

## Quick Verification (5 minutes)

### Step 1: Log Into Alpaca Dashboard
1. Visit: https://app.alpaca.markets/
2. Sign in with your account credentials
3. Select **"Paper Trading"** tab (NOT live trading)

### Step 2: Verify Account Type
**Location**: Dashboard main page or Account Settings

**What to look for**:
- **Account Type**: Must be **"CASH"** (not "MARGIN")
  - CASH accounts: $25,000 default, no day-trading buying power restrictions, no margin requirements
  - MARGIN accounts: Have margin multiplier (2x-4x), have day-trading buying power limits, require $25K minimum to avoid pattern day trader restrictions
  
**If it shows "MARGIN"**:
- Click **Account** → **Settings** → **Account Type**
- Switch to **"CASH"** (if available)
- This change usually takes 1-2 business days to process
- Alternative: Contact Alpaca support (support@alpaca.markets) for immediate account type verification

### Step 3: Verify Account Balance
**Location**: Dashboard → Buying Power / Account Balance section

**What to look for**:
- **Buying Power**: Should show $25,000+ (Alpaca default for new paper accounts)
- **Account Value**: Should show $25,000+ or your configured starting balance
- **Cash**: Should show non-zero amount available for trading

**If Buying Power is $0**:
- This is the root cause of error 40310000
- Paper accounts don't have "insufficient funds" in the traditional sense — this usually means:
  1. Account not yet initialized (try logging out and back in)
  2. Account type is MARGIN with day-trading restrictions
  3. Account has been disabled/flagged

**Recovery Steps**:
1. Log out completely (close browser tab with Alpaca)
2. Wait 2-3 minutes
3. Log back in and check Buying Power again
4. If still $0, contact Alpaca support: support@alpaca.markets
   - Provide: Account email, account type (CASH), screenshot of Buying Power
   - Note: "Paper trading account showing zero buying power; should have $25,000 default"

### Step 4: Check API Credentials
**Location**: Settings → API Keys

**What to look for**:
- **Paper Trading Keys**: Separate keys from Live Trading keys
- Status: **ACTIVE** (not revoked/disabled)
- Key format: Should be 20-character alphanumeric strings

**If API keys are missing or disabled**:
- Regenerate new keys: Settings → API Keys → "Create New Key"
- Select **"Paper Trading"** scope
- Copy key + secret key
- Update `.env` file in projects/stockbot/ with new keys:
  ```
  ALPACA_API_KEY=<new_key>
  ALPACA_API_SECRET=<new_secret>
  ALPACA_BASE_URL=https://paper-trading.alpaca.markets
  ```
- Restart engine after updating .env

---

## Detailed Troubleshooting

### Issue 1: Account Type is MARGIN
**Symptoms**:
- Buying Power shows different value than Account Balance
- Day-trading restrictions apply (need $25K+ minimum)
- Frequent "insufficient day trading buying power" errors

**Solution**:
```
1. Alpaca Dashboard → Account → Settings
2. Find "Account Type" dropdown
3. Change from "MARGIN" to "CASH"
4. Confirm (may require email verification)
5. Wait 1-2 business days for change to process
6. Log out/in to refresh
7. Verify Buying Power is now $25,000+
```

**Why this matters for stockbot**:
- CASH accounts: Can trade up to full buying power immediately
- MARGIN accounts with day-trading restrictions: Limited to 4x leverage (intraday), but with buying power limits that change daily based on previous day settlements
- stockbot needs immediate execution without restriction, so CASH is required

### Issue 2: Buying Power is $0

**Diagnosis Steps**:

1. **Check Account Status**:
   - Settings → Account → Status should show "ACTIVE"
   - If shows "PENDING", account not yet initialized

2. **Check Account Value**:
   - Dashboard should show Account Value = $25,000 (or your configured amount)
   - If shows $0, account may be disabled

3. **Try Account Reset** (non-destructive):
   - Log out completely
   - Clear browser cache for app.alpaca.markets
   - Close all browser windows with Alpaca
   - Wait 2 minutes
   - Log back in
   - Check Buying Power again

4. **Contact Alpaca Support**:
   ```
   To: support@alpaca.markets
   Subject: Paper Trading Account - Zero Buying Power
   
   Message:
   Account: <your@email.com>
   Account Type: CASH
   Issue: Buying Power shows $0 but should be $25,000 (paper trading default)
   
   - Last successful trade: 2026-04-27 15:12 UTC
   - Current status: Account Value shows correct, Buying Power shows $0
   - Action needed: Please reset buying power to $25,000 or investigate restrictions
   ```
   
   Expected response time: 1-4 hours (Alpaca has responsive support)

### Issue 3: API Keys Not Working

**Verification**:
```bash
# In projects/stockbot/ directory
python3 << 'EOF'
import os
from alpaca.trading.client import TradingClient

api_key = os.getenv('ALPACA_API_KEY')
api_secret = os.getenv('ALPACA_API_SECRET')
client = TradingClient(api_key=api_key, secret_key=api_secret, paper=True)

try:
    account = client.get_account()
    print(f"✓ API Connection OK")
    print(f"  Account Status: {account.status}")
    print(f"  Buying Power: ${account.buying_power}")
except Exception as e:
    print(f"✗ API Connection Failed: {e}")
EOF
```

**If authentication fails**:
1. Verify .env file has correct keys (no extra spaces/newlines)
2. Generate new API keys in Alpaca Dashboard
3. Update .env and restart engine

---

## Pre-Engine-Restart Checklist

Before running `stockbot/scripts/run_live_trading.py`, verify:

- [ ] Alpaca Dashboard accessible (can log in)
- [ ] Account Type = **CASH**
- [ ] Buying Power = $25,000+ 
- [ ] API Keys are ACTIVE
- [ ] `.env` file has correct ALPACA_API_KEY and ALPACA_API_SECRET
- [ ] `ALPACA_BASE_URL=https://paper-trading.alpaca.markets` (NOT the live trading URL)

---

## Engine Restart Command

Once verified, restart the engine:

```bash
cd /home/awank/dev/SuperClaude_Framework/projects/stockbot

# Activate venv (if not already)
source .venv/bin/activate

# Run the engine
python scripts/run_live_trading.py

# Monitor logs in separate terminal
tail -f logs/live_trading_$(date +%Y%m%d).log | grep -i "fill\|order\|execution\|error"
```

**Success indicator**: Within 5 minutes of engine start, you should see a FILL or PENDING order in the logs. If you see "insufficient day trading buying power" error again, the Alpaca account still has configuration issues — stop engine and re-run verification steps above.

---

## Emergency Contacts

- **Alpaca Support**: support@alpaca.markets (response ~1-4 hours)
- **Alpaca Status Page**: https://status.alpaca.markets/ (check if service is down)
- **Alpaca Community Forum**: https://community.alpaca.markets/

---

## Related Documentation

- `projects/stockbot/RESEARCH_NOTES_ITEM8.md` — Regulatory requirements for multi-asset trading
- `projects/stockbot/signal-threshold-analysis.md` — Current trading signal configuration
- `.env.example` — Environment variable template
