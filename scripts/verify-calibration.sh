#!/bin/bash
# verify-calibration.sh
# Checks whether the token limits in PROJECTS.md are calibrated for the current billing week.
#
# Usage (from BLOCKED.md Verify with field — no args):
#   bash scripts/verify-calibration.sh
#   → prints OK or CALIBRATE, exits 0 if calibrated recently, 1 if stale/missing
#
# Usage (to calibrate — two args):
#   bash scripts/verify-calibration.sh <sonnet_pct> <all_pct>
#   → runs usage-check.py --calibrate and prints result

WORKSPACE="$(cd "$(dirname "$0")/.." && pwd)"

if [ "$#" -eq 2 ]; then
  python3 "$WORKSPACE/scripts/usage-check.py" --calibrate "$1" "$2"
  exit $?
fi

python3 - "$WORKSPACE/PROJECTS.md" <<'PYEOF'
import re, sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

text = Path(sys.argv[1]).read_text()
m = re.search(r'calibrated (\d{4}-\d{2}-\d{2})', text)
if not m:
    print("CALIBRATE: no calibration date found in PROJECTS.md")
    sys.exit(1)

cal_date = datetime.strptime(m.group(1), "%Y-%m-%d").date()
today = datetime.now(timezone.utc).date()
age_days = (today - cal_date).days

if age_days > 7:
    print(f"CALIBRATE: limits last calibrated {age_days} days ago ({cal_date}). "
          f"Run: bash scripts/verify-calibration.sh <sonnet_pct> <all_pct>")
    sys.exit(1)

print(f"OK: limits calibrated {age_days} days ago ({cal_date}) — within 7-day window.")
sys.exit(0)
PYEOF
