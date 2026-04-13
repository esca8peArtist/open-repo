# Autonomous Claude Orchestrator — Architecture & Setup

**Date**: 2026-04-10
**Status**: Phase 1 complete — awaiting Pi SSH details, project goals, Discord webhook

---

## What This Is

A 24/7 autonomous Claude Code orchestrator running on a Raspberry Pi 5 (8GB). Claude works continuously across multiple projects, logs all activity, and prepares briefings for periodic check-ins. The user checks in 1-2x daily to review progress, unblock items, and redirect priorities.

---

## Architecture Overview

```
Raspberry Pi 5 (8GB, always on)
  └── systemd user service
        └── tmux session "claude-auto"
              └── scripts/start-orchestrator.sh (loop)
                    └── claude --dangerously-skip-permissions -p <orchestrator-prompt>
                          └── reads PROJECTS.md → picks task → works → logs → notifies
```

**State lives in files** (not sessions):
- `PROJECTS.md` — source of truth for priorities and goals
- `WORKLOG.md` — append-only timestamped log of all work
- `CHECKIN.md` — briefing prepared for user's next check-in
- `BLOCKED.md` — items needing user input
- `INBOX.md` — task drop-in from phone/Obsidian

**Notification**: Discord webhook (outbound only). Claude posts updates via `curl`.
**Inbound commands**: Edit `INBOX.md` from Obsidian on phone → Claude picks it up next session.

---

## Project Registry Summary

| Project | Priority | Visibility | Push policy |
|---------|----------|-----------|-------------|
| resistance-research | High | Private | Local only |
| stockbot | High | Private | Local only |
| open-source-rideshare | Medium | Public | Feature branches → GitHub |
| seedwarden | Medium | Private | Local only |
| containerized-agents | Low | Private | Local only |
| workout | Low | Private | Local only |
| resume | Low (paused) | Private | Local only |

---

## Check-in Workflow

**You arrive** → read `CHECKIN.md` (< 5 min briefing) → leave notes in "Your Notes for Orchestrator" section → done

**Orchestrator** → reads your notes at session start → processes INBOX.md → picks highest priority task → works → updates CHECKIN.md before going idle

---

## Slash Commands Added

| Command | Purpose |
|---------|---------|
| `/checkin` | Generate full check-in briefing from all state files |
| `/standup` | 3-line quick daily standup (done/doing/blocked) |
| `/switch-project` | Gracefully save state and switch to another project |
| `/unblock` | Process user's unblocking notes and resume suspended work |

---

## Files Built (Phase 1)

All in `/home/awank/dev/SuperClaude_Framework/`:

```
PROJECTS.md                          ← fill in project goals
WORKLOG.md                           ← append-only log
CHECKIN.md                           ← check-in briefing
BLOCKED.md                           ← blocked items
INBOX.md                             ← task drop-in
AUTONOMOUS_SETUP.md                  ← full pending task tracker

.claude/
├── settings.json                    ← permissions (acceptEdits + deny rules)
├── orchestrator-prompt.md           ← headless session instructions
├── agents/
│   ├── orchestrator.md
│   ├── resistance-research.md
│   ├── stockbot.md
│   ├── seedwarden.md
│   ├── open-source-rideshare.md
│   └── general-research.md
└── commands/
    ├── checkin.md
    ├── standup.md
    ├── switch-project.md
    └── unblock.md

scripts/
├── pi-setup.sh                      ← run once on Pi
└── start-orchestrator.sh            ← session loop (called by systemd)
```

---

## Pending Setup Tasks

### Blocking
- [ ] Fill in project goals in `PROJECTS.md` (required before autonomous work starts)

### Pi Setup (one-time)
- [ ] Get Pi IP: `hostname -I` on Pi
- [ ] SSH key setup: `ssh-copy-id user@<PI_IP>` from dev machine
- [ ] Run `bash scripts/pi-setup.sh` on Pi
- [ ] Fill in `~/.claude_env` on Pi (API key + Discord webhook)
- [ ] Sync workspace to Pi (git pull or rsync)
- [ ] Authenticate Claude Code on Pi: `claude` (follow login)

### Discord
- [ ] Create webhook: Discord channel → Settings → Integrations → Webhooks → New → Copy URL
- [ ] Add to `~/.claude_env` as `DISCORD_WEBHOOK_URL`
- [ ] Test: `curl -H "Content-Type: application/json" -d '{"content":"test"}' $DISCORD_WEBHOOK_URL`

### First Run
- [ ] Manual test: `bash scripts/start-orchestrator.sh`
- [ ] Enable service: `systemctl --user start claude-orchestrator.service`
- [ ] Verify reboot survival: `sudo reboot` → check status after

---

## Permission Model

- Interactive sessions: `acceptEdits` mode (file edits auto-approved, dangerous bash needs confirm)
- Orchestrator sessions: `--dangerously-skip-permissions` (full autonomy)
- Hard denies (both modes): push to main/master, force push, rm -rf /, pipe-to-bash
- Private projects: commits only, no remote push ever
- Public project (rideshare): push to feature branches freely, main requires user approval

---

## How to Check In

1. Open any Claude session and type `/checkin` — get a briefing
2. Or just read `CHECKIN.md` directly in Obsidian
3. Leave instructions in the "Your Notes" section of `CHECKIN.md`, or drop tasks into `INBOX.md`
4. Type `/unblock` if you've resolved something in `BLOCKED.md`
