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

### mfg-farm — Test print required before launch prep continues
**Date blocked**: 2026-04-12
**Context**: Business plan, CadQuery designs (modrun_rail.py, modrun_clip.py), market research, and listing copy are all complete. Orchestrator cannot proceed with launch prep until a physical test print confirms the designs are printable.
**What I need**: Run a test print of the CadQuery rail and clip designs and confirm they printed correctly.
**Verify with**: `# manual — cannot auto-verify`
**Resolution**:

---

## Resolved Archive

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
