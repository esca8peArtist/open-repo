#!/usr/bin/env bash
# gate1_auto_check.sh
# ===================
# One-shot Gate 1 checkpoint runner for May 14, 2026.
# Scheduled via cron at 14:30 UTC (1 hour after h+10 AAPL exit at 13:30 UTC).
#
# What it does:
#   1. Syncs today's Alpaca fills into stockbot.db (catches the AAPL SELL)
#   2. Runs the Gate 1 scenario assignment (A/B/C) from gate1_dashboard.sh
#   3. Checks Alpaca directly for AAPL position status
#   4. Writes a compact result to INBOX.md for the orchestrator/Discord bot
#
# Cron entry (Pi, UTC):
#   30 14 14 5 * bash /home/awank/dev/SuperClaude_Framework/scripts/gate1_auto_check.sh >> /tmp/gate1_auto.log 2>&1

set -euo pipefail

WORKSPACE="${CLAUDE_WORKSPACE:-${HOME}/dev/SuperClaude_Framework}"
PROJECT="${WORKSPACE}/projects/stockbot"
INBOX="${WORKSPACE}/INBOX.md"
LOG_DIR="${PROJECT}/logs"
TMPDIR_LOCAL="$(mktemp -d)"
trap 'rm -rf "${TMPDIR_LOCAL}"' EXIT

mkdir -p "${LOG_DIR}"

timestamp() { date -u '+%Y-%m-%d %H:%M UTC'; }
log() { echo "[$(timestamp)] $*"; }

log "=== gate1_auto_check.sh starting ==="

# Load credentials: .claude_env first, then project .env (project wins on conflicts)
for envfile in "${HOME}/.claude_env" "${PROJECT}/.env"; do
    if [[ -f "${envfile}" ]]; then
        set -a
        # shellcheck disable=SC1090
        source <(grep -v '^\s*#' "${envfile}" | grep -v '^\s*$')
        set +a
    fi
done

# ── Step 1: Sync today's fills ─────────────────────────────────────────────
TODAY=$(date -u '+%Y-%m-%d')
log "Running DB sync for ${TODAY}..."

SYNC_LOG="${LOG_DIR}/gate1_sync_${TODAY}.log"
set +e
cd "${PROJECT}"
uv run python scripts/sync_db_from_alpaca.py \
    --db "${PROJECT}/stockbot.db" \
    --since "${TODAY}" \
    > "${SYNC_LOG}" 2>&1
SYNC_EXIT=$?
set -e

if [[ ${SYNC_EXIT} -eq 0 ]]; then
    log "Sync OK — $(grep 'Trades:' "${SYNC_LOG}" | tail -1)"
else
    log "Sync FAILED (exit ${SYNC_EXIT}) — checkpoint will still run using existing DB data"
fi

# ── Step 2: Run Gate 1 dashboard, capture output ───────────────────────────
log "Running Gate 1 dashboard..."
DASHBOARD_LOG="${LOG_DIR}/gate1_dashboard_${TODAY}.log"

set +e
cd "${PROJECT}"
bash scripts/gate1_dashboard.sh > "${DASHBOARD_LOG}" 2>&1
SCENARIO_EXIT=$?
set -e

case ${SCENARIO_EXIT} in
    0) SCENARIO="A" ; VERDICT="PASS" ; VERDICT_ICON="✅" ;;
    1) SCENARIO="B" ; VERDICT="NEAR-MISS" ; VERDICT_ICON="⚠️" ;;
    2) SCENARIO="C" ; VERDICT="FAR-MISS" ; VERDICT_ICON="❌" ;;
    *) SCENARIO="?" ; VERDICT="ERROR" ; VERDICT_ICON="⚠️" ;;
esac

log "Gate 1 result: Scenario ${SCENARIO} — ${VERDICT_ICON} ${VERDICT}"

# ── Step 3: Check Alpaca AAPL position directly ────────────────────────────
log "Checking Alpaca AAPL position..."

cat > "${TMPDIR_LOCAL}/alpaca_check.py" << 'EOF'
import os, sys
try:
    from alpaca.trading.client import TradingClient
    paper = os.environ.get("ALPACA_PAPER", "true").lower() != "false"
    client = TradingClient(os.environ["ALPACA_API_KEY"], os.environ["ALPACA_SECRET_KEY"], paper=paper)
    try:
        pos = client.get_open_position("AAPL")
        qty = float(pos.qty)
        upl = float(pos.unrealized_pl)
        print(f"OPEN qty={qty:.0f} upl=${upl:+.2f}")
    except Exception:
        print("CLOSED")
except Exception as e:
    print(f"ERROR: {e}")
EOF

ALPACA_RESULT=$(cd "${PROJECT}" && uv run python3 "${TMPDIR_LOCAL}/alpaca_check.py" 2>/dev/null || echo "ERROR")
log "Alpaca AAPL: ${ALPACA_RESULT}"

# ── Step 4: Pull key metrics from DB ──────────────────────────────────────
cat > "${TMPDIR_LOCAL}/db_check.py" << 'EOF'
import sqlite3, os, sys
db = os.path.join(os.getcwd(), "stockbot.db")
conn = sqlite3.connect(db)
cur = conn.cursor()
cur.execute("""
  SELECT
    COALESCE(SUM(CASE WHEN action='SELL' AND ticker='AAPL' THEN 1 ELSE 0 END), 0) as aapl_sells,
    COALESCE(SUM(CASE WHEN action='SELL' AND realized_pnl IS NOT NULL THEN 1 ELSE 0 END), 0) as confirmed_trips,
    COALESCE(SUM(CASE WHEN ticker='AAPL' AND action='SELL' AND realized_pnl IS NOT NULL
                      THEN realized_pnl ELSE 0 END), 0) as aapl_pnl
  FROM trades WHERE mode='PAPER' AND date(timestamp) >= '2026-05-05'
""")
r = cur.fetchone()
conn.close()
print(f"aapl_sells={r[0]} trips={r[1]} pnl=${r[2]:.2f}")
EOF

DB_METRICS=$(cd "${PROJECT}" && uv run python3 "${TMPDIR_LOCAL}/db_check.py" 2>/dev/null || echo "db_error")
log "DB metrics: ${DB_METRICS}"

# ── Step 5: Write to INBOX.md ─────────────────────────────────────────────
TS=$(date '+%Y-%m-%d %H:%M')
INBOX_MSG="${VERDICT_ICON} GATE 1 CHECKPOINT ${TS}: Scenario ${SCENARIO} ${VERDICT} | AAPL=${ALPACA_RESULT} | ${DB_METRICS}"

log "Writing to INBOX.md..."

cat > "${TMPDIR_LOCAL}/write_inbox.py" << 'EOF'
import sys, fcntl
inbox_path = sys.argv[1]
entry = sys.argv[2]
lock_path = inbox_path + ".lock"
with open(lock_path, "w") as lock:
    fcntl.flock(lock, fcntl.LOCK_EX)
    try:
        content = open(inbox_path).read()
    except FileNotFoundError:
        content = "# Inbox\n\n## New Items\n"
    ts = entry.split("]")[0].lstrip("- [")
    full_entry = f"- [{ts}] {entry.split('] ', 1)[1]}\n"
    if "## New Items\n" in content:
        content = content.replace("## New Items\n", f"## New Items\n{full_entry}", 1)
    else:
        content += f"\n{full_entry}"
    with open(inbox_path, "w") as f:
        f.write(content)
print(f"INBOX: written entry starting with: {full_entry[:80]}")
EOF

uv run python3 "${TMPDIR_LOCAL}/write_inbox.py" "${INBOX}" "[${TS}] ${INBOX_MSG}" 2>/dev/null \
    || echo "WARNING: could not write to INBOX.md"

log "INBOX updated: ${INBOX_MSG}"
log "=== gate1_auto_check.sh done ==="
