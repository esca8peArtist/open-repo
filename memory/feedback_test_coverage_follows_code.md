---
name: feedback-test-coverage-follows-code
description: Tests must cover the code that actually runs, not archived predecessors. Every task that writes or changes code must include tests that verify the design intent.
metadata:
  type: feedback
---

For every task where code is written or changed, tests must be written or updated to verify the functionality according to design intent. This is non-negotiable.

**Why:** The 2026-06-24 stockbot incident lost a full trading day validation window. The monitoring system (`health_poller.py` + `run_monitor.py`) had three production bugs that went undetected because:
1. Tests followed the archived predecessor (`monitoring_alert_script.py`) instead of the live code.
2. A wrong env var name (`DISCORD_WEBHOOK_URL` vs `STOCKBOT_DISCORD_WEBHOOK_URL`) silenced Discord for all events — never caught because the test suite only covered `src/notifications/discord.py`, not the monitor's own Discord sender.
3. `engine=unknown` during market hours was treated as transient and never escalated — no test existed to catch this gap.

**How to apply:**

1. **Tests follow code, not files.** When code is refactored or moved, migrate tests immediately. Tests that import from an old path don't prove the new code is correct — they prove the old code is correct, which is worthless. Never leave a test file pointing at `scripts/archive/`.

2. **Every cron-invoked script must have unit tests.** Operational scripts that run unattended (cron, systemd) have the highest risk and the least visibility. If it runs automatically, it must be tested. Add it to `tests/unit/test_<module_name>/`.

3. **Test design intent, not implementation.** Tests must exercise the *behaviour the system was built to produce* — e.g. "Discord fires when engine is unknown during market hours for 2+ polls" — not just "the function runs without exceptions."

4. **Env var names used by operational scripts must be pinned in `test_env_contract.py`.** Any mismatch between what a script reads and what `.env` defines is a silent, total failure. Add banned aliases to `BANNED_ENV_VAR_NAMES` the moment a wrong name is found or corrected.

5. **When refactoring moves code: delete or explicitly migrate tests before closing the task.** A test that passes against dead code is worse than no test — it creates false confidence. The task is not done until coverage follows the live module.

**Related:** [[project-stockbot-lever-b-critical-deadline]], [[feedback-verify-code-immediately]]
