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

### open-repo — GitHub push blocked: esca8peArtist key lacks SuperClaude-Org write access
**Date blocked**: 2026-04-26
**Context**: Feature branch `feature/wave4-phase2-federation-service` is fully ready (5+ commits, 194 tests passing, 0 failures). All code work complete and verified. Push attempt failed: SSH key authenticates as esca8peArtist, but that account lacks write permission to SuperClaude-Org/SuperClaude_Framework repository.
**What I need**: Either (1) add esca8peArtist to SuperClaude-Org organization with push access, OR (2) configure an SSH key for an account that already has write access to SuperClaude-Org.
**Verify with**: `cd /home/awank/dev/SuperClaude_Framework && git push origin feature/wave4-phase2-federation-service && echo "Push succeeded"`
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

### stockbot — Test contamination + missing position recovery
**Date blocked**: 2026-04-27
**Context**: At 2026-04-26 22:15:27 UTC, pytest test suite ran concurrently with live engine. Test code injected mock objects (bad_callback, test halt messages) into engine's shutdown handler. Engine failed to load open positions from database (error: "'Mock' object is not iterable"). Open BUY position (36 AAPL @ $271.04, placed 17:06 UTC) exists only in trades table, not positions table. Engine continued running with orphaned position.
**Resolution**: RESOLVED 2026-04-27 — Investigated root cause: test contamination @ 22:15:27 (pytest + live engine concurrent, Mock objects in shutdown handler). Actions taken: (1) Created missing position record (ID=1, AAPL 36@271.04) in positions table to match open BUY trade. (2) Fixed position_manager.py logging bug (AttributeError on mode.value when mode is string instead of enum). (3) Verified engine loads position cleanly without Mock errors. Engine ready for Monday 2026-04-28 market open. Next: Monitor SELL signal execution Monday at 14:30 UTC. Long-term: Add pytest database isolation (separate test DB, prevent concurrent engine+pytest runs).

---

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
