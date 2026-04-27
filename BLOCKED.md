# Blocked Items

> Items the orchestrator cannot proceed on without user input.
> The orchestrator checks this at the start of each session.
> When you've unblocked something, add a note in the "Resolution" field — the orchestrator will pick it up, move the entry to Resolved Archive, and commit.

---

## Format

```
### [Project] — [Short description of block]
**Date blocked**: YYYY-MM-DD
**Context**: What was being attempted and why it's blocked
**What I need**: Specific question or action needed from user
**Verify with**: Shell command to confirm resolved (e.g. `ssh -T git@github.com`)
                 For physical/manual actions write: `# manual — cannot auto-verify`
**Resolution**: [leave blank — user or orchestrator fills this in]
```

When the block is resolved (Resolution written OR Verify command passes):
- Write the resolution
- Move the entire block to **Resolved Archive** below
- Commit BLOCKED.md on master immediately

---

## Active Blocks

### stockbot — Trading engine shutdown, orphaned position risk
**Date blocked**: 2026-04-27
**Context**: Paper trading Day 3 monitoring detected that the trading engine shut down unexpectedly at 2026-04-26 22:15 UTC (reason: UNKNOWN). Engine is currently offline. An open BUY position (36 AAPL @ $271.04, placed 2026-04-26 17:06 UTC) exists in the trades table but is NOT persisted in the positions table. If the engine restarts cold, it will not recognize the open position, creating risk of a duplicate BUY stacking on top without first executing a SELL. This must be resolved before Monday 2026-04-28 market open (09:30 ET / 14:30 UTC) or the first live market session will fail to generate a SELL signal.
**What I need**: (1) Investigate why the engine shut down at 22:15 UTC on 2026-04-26 (check live_trading_20260426.log for any error context beyond "GRACEFUL SHUTDOWN REQUESTED"). (2) Ensure the engine restarts cleanly and detects the open position correctly. (3) Confirm no duplicate BUY would be placed if a new signal arrives before the SELL executes.
**Verify with**: `grep -c "SELL" /home/awank/dev/SuperClaude_Framework/projects/stockbot/logs/paper_trading_daily.jsonl` — verify at least one SELL completion after Monday market open to confirm the engine restarted and correctly managed the open position.
**Resolution**:

---

### mfg-farm — Test print required before launch prep continues
**Date blocked**: 2026-04-12
**Context**: Business plan, CadQuery designs (modrun_rail.py, modrun_clip.py), market research, and listing copy are all complete. Orchestrator cannot proceed with launch prep until a physical test print confirms the designs are printable.
**What I need**: Run a test print of the CadQuery rail and clip designs and confirm they printed correctly.
**Verify with**: `# manual — cannot auto-verify`
**Resolution**:

---

## Resolved Archive

### open-repo — GitHub push blocked: esca8peArtist key lacks SuperClaude-Org write access
**Date blocked**: 2026-04-26
**Context**: Feature branch `feature/wave4-phase2-federation-service` is fully ready (5+ commits, 194 tests passing, 0 failures). Push attempt failed because origin pointed to third-party SuperClaude-Org/SuperClaude_Framework repo the user doesn't own.
**What I need**: New public repo under esca8peArtist account.
**Verify with**: `git ls-remote open-repo HEAD`
**Resolution**: Resolved 2026-04-26 — Created `esca8peArtist/open-repo` (public). Added `open-repo` remote pointing to `git@github.com:esca8peArtist/open-repo.git`. Pushed main branch and feature branch via `git subtree push --prefix=projects/open-repo`. Feature branch is live at https://github.com/esca8peArtist/open-repo/tree/feature/wave4-phase2-federation-service.

### stockbot — Python 3.12 required but not available on Pi
**Date blocked**: 2026-04-12
**Context**: The stockbot venv was created with Python 3.12 packages. `pandas-ta` v0.4.71b0 uses Python 3.12-only syntax and cannot run on Python 3.11.
**What I need**: Install Python 3.12, downgrade pandas-ta, or replace with alternative TA library.
**Verify with**: `python3 -c "import ta; print('ok')"`
**Resolution**: Resolved 2026-04-12 — Option C chosen. pandas-ta replaced with `ta` library across technical_indicators.py and dashboard_api.py. requirements.txt updated.

### All projects — Git identity not configured on Pi
**Date blocked**: 2026-04-12
**Context**: Attempted to commit open-source-rideshare chat feature. Git requires `user.name` and `user.email` to be set.
**What I need**: Run `git config --global user.email` and `git config --global user.name` on the Pi.
**Verify with**: `git config --global user.name`
**Resolution**: Resolved 2026-04-12 — git identity confirmed as name=thorn, email=thorn@local.

### open-source-rideshare — GitHub push blocked: no HTTPS credentials or SSH key
**Date blocked**: 2026-04-12
**Context**: feature/background-checks-firebase-push committed and ready to push (1,809 tests). `git push` failed with "could not read Username" — Pi appeared to have no SSH key for GitHub.
**What I need**: SSH key or HTTPS credentials for GitHub.
**Verify with**: `ssh -T git@github.com 2>&1 | grep -q "successfully authenticated" && echo ok`
**Resolution**: Resolved 2026-04-26 — id_ed25519 SSH key exists and authenticates successfully with GitHub. Remote already set to SSH URL. (Project is paused; push will happen when rideshare resumes.)
