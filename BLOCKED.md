# Blocked Items

> Items the orchestrator cannot proceed on without user input.
> The orchestrator checks this at the start of each session.
> When you've unblocked something, add a note in the "Resolution" field — the orchestrator will pick it up and clear the entry.

---

## Format

```
### [Project] — [Short description of block]
**Date blocked**: YYYY-MM-DD
**Context**: What was being attempted and why it's blocked
**What I need**: Specific question or decision needed from user
**Resolution**: [Leave blank — user fills this in]
```

---

## Active Blocks

### stockbot — Python 3.12 required but not available on Pi
**Date blocked**: 2026-04-12
**Context**: The stockbot venv was created with Python 3.12 packages. The key dependency `pandas-ta` v0.4.71b0 uses Python 3.12-only syntax (nested f-string quotes) and cannot run on Python 3.11 (which is what the Pi has). Attempted to recreate the venv with 3.11 but pandas-ta fails with a SyntaxError at import time. The old venv has been restored.
**What I need**: Either (a) install Python 3.12 on the Pi (not in apt repos — would need to build from source or use pyenv/deadsnakes), or (b) decide to downgrade pandas-ta to 0.3.x (which has been removed from PyPI — would need a cached wheel or GitHub install, and GitHub isn't accessible from Pi without auth). Or (c) replace pandas-ta with an alternative TA library like `ta` or `ta-lib`.
**Resolution**: Resolved 2026-04-12 — Option C chosen. pandas-ta replaced with `ta` library across technical_indicators.py and dashboard_api.py. requirements.txt updated. Venv needs manual rebuild by user (see CHECKIN.md). Orchestrator can proceed once venv is rebuilt.

### All projects — Git identity not configured on Pi
**Date blocked**: 2026-04-12
**Context**: Attempted to commit open-source-rideshare chat feature (68 new tests, all files staged). Git requires `user.name` and `user.email` to be set. The orchestrator cannot modify git config per working rules.
**What I need**: Run `git config --global user.email "your@email.com"` and `git config --global user.name "Your Name"` on the Pi. After that, staged changes can be committed.
**Resolution**: Resolved 2026-04-12 — git identity confirmed as name=thorn, email=thorn@local. Orchestrator can proceed with commits.

---

### open-source-rideshare — GitHub push blocked: no HTTPS credentials or SSH key
**Date blocked**: 2026-04-12
**Context**: feature/background-checks-firebase-push is committed and ready to push (1,809 tests passing, 101 new tests from Checkr + Firebase features). `git push` fails with "could not read Username" — Pi has no HTTPS credential helper configured and no SSH key for GitHub (only `authorized_keys` present, no `id_rsa`/`id_ed25519`).
**What I need**: One of: (a) `git config --global credential.helper store` + `git push` once entering GitHub username/PAT, (b) generate SSH key on Pi and add public key to GitHub account, or (c) set remote URL to SSH: `git remote set-url origin git@github.com:SuperClaude-Org/SuperClaude_Framework.git` and add SSH key to GitHub.
**Resolution**:

---

## Resolved (Archive)

<!-- Move resolved blocks here with resolution date -->
