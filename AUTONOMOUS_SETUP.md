# Autonomous Setup Tracker

> Track what's done and what's still needed for the full autonomous Pi orchestrator setup.
> Last updated: 2026-04-10

---

## Phase 1 — Workspace Scaffolding (Done on dev machine)

- [x] `.claude/settings.json` — permissions model with deny rules for main/master
- [x] `PROJECTS.md` — project registry template
- [x] `WORKLOG.md` — append-only session log
- [x] `CHECKIN.md` — check-in briefing template
- [x] `BLOCKED.md` — blocked items tracker
- [x] `INBOX.md` — mobile task drop-in file
- [x] `.claude/orchestrator-prompt.md` — headless session instructions
- [x] `.claude/agents/orchestrator.md` — orchestrator agent profile
- [x] `.claude/agents/resistance-research.md` — research agent
- [x] `.claude/agents/stockbot.md` — stockbot agent
- [x] `.claude/agents/seedwarden.md` — seedwarden agent
- [x] `.claude/agents/open-source-rideshare.md` — rideshare agent
- [x] `.claude/agents/general-research.md` — general research agent
- [x] `.claude/commands/checkin.md` — /checkin slash command
- [x] `.claude/commands/standup.md` — /standup slash command
- [x] `.claude/commands/switch-project.md` — /switch-project slash command
- [x] `.claude/commands/unblock.md` — /unblock slash command
- [x] `scripts/pi-setup.sh` — Pi setup script
- [x] `scripts/start-orchestrator.sh` — orchestrator startup loop

---

## Phase 2 — User Inputs Needed

- [x] resistance-research goal ✓
- [x] stockbot goal ✓
- [x] open-source-rideshare goal ✓
- [x] seedwarden goal ✓
- [ ] **containerized-agents goal** — what is this project?
- [ ] **workout goal** — fitness tracker, planner, something else?
- (resume has a reasonable stub, only gets touched on request)

---

## Phase 3 — Pi Hardware Setup

- [x] Pi IP confirmed: 10.0.0.46, username: awank
- [x] Discord webhook URL obtained (stored in ~/.claude_env on Pi only — not tracked in git)
- [ ] **SSH key setup** — `ssh-copy-id awank@10.0.0.46` (eliminates password prompts)
- [ ] **Sync workspace to Pi** — `ssh awank@10.0.0.46 "mkdir -p ~/dev/SuperClaude_Framework" && rsync -avz /home/awank/dev/SuperClaude_Framework/ awank@10.0.0.46:~/dev/SuperClaude_Framework/`
- [ ] **Run pi-setup.sh on Pi** — `ssh awank@10.0.0.46 "bash ~/dev/SuperClaude_Framework/scripts/pi-setup.sh"`
- [ ] **Fill in ~/.claude_env on Pi** — ANTHROPIC_API_KEY + DISCORD_WEBHOOK_URL (already have URL)
- [ ] **Authenticate Claude Code on Pi** — `ssh awank@10.0.0.46` then `cd ~/dev/SuperClaude_Framework && claude`

---

## Phase 4 — Discord Setup

- [ ] **Create Discord webhook** — in any Discord channel: Settings → Integrations → Webhooks → New Webhook → Copy URL
- [ ] **Add to ~/.claude_env on Pi** — `DISCORD_WEBHOOK_URL="https://discord.com/api/webhooks/..."`
- [ ] **Test notification** — `curl -H "Content-Type: application/json" -d '{"content":"test"}' $DISCORD_WEBHOOK_URL`
- [ ] **(Optional) Set up Obsidian sync** — if you want INBOX.md accessible from phone via Obsidian

---

## Phase 5 — First Run

- [ ] **Test orchestrator manually**: `bash scripts/start-orchestrator.sh` (Ctrl+C to stop)
- [ ] **Verify WORKLOG.md gets updated**
- [ ] **Verify Discord notification fires**
- [ ] **Enable systemd service**: `systemctl --user start claude-orchestrator.service`
- [ ] **Verify it survives reboot**: `sudo reboot` → wait → `systemctl --user status claude-orchestrator.service`

---

## Architecture Decisions (Recorded)

| Decision | Choice | Reason |
|----------|--------|--------|
| Infrastructure | Raspberry Pi 5 8GB | Always-on, low power, no extra cost |
| Notification | Discord webhook (outbound) | Already have Discord, simple curl integration |
| Inbound commands | INBOX.md + Obsidian sync | Async, no bot needed, works from phone |
| Permission mode | --dangerously-skip-permissions | Full autonomy; safety via deny rules + agent instructions |
| Push policy | Feature branches only; main requires approval | User wants to check functionality before releases |
| Private projects | Local commits only, no GitHub push | All except open-source-rideshare |
| Session persistence | tmux + systemd restart | Survives crashes and reboots |
| Session loop | Headless -p with 5min pause between runs | Clean state each run, reads from files |
| Check-in cadence | Daily, sometimes twice | User available daily |
