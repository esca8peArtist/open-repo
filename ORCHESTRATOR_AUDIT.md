# Orchestrator Process Audit — 2026-05-12

**Auditor:** analyze-agent (deep-read pass over orchestrator state, prompts, scripts, and 5 latest sessions)
**Scope:** ORCHESTRATOR_STATE.md, INBOX.md, PROJECTS.md, WORKLOG.md, CHECKIN.md, BLOCKED.md, EXPLORATION_QUEUE.md, AUTONOMOUS_SETUP.md, AGENTS.md, CLAUDE.md, `.claude/orchestrator-prompt.md`, `.claude/agents/orchestrator.md`, `.claude/commands/*.md`, `scripts/start-orchestrator.sh`, `scripts/generate-orchestrator-state.sh`, `scripts/discord-bot.py`.

## Summary

The orchestrator system has a sound architecture (compact state file, headless loop, branch discipline, Discord bridge, 2-hour watchdog) but it is failing in five concrete, fixable ways:

1. **There is no "stale-detector" pass.** Nothing in the session protocol re-validates that a project's `Current focus` text is still accurate, or that a `Blocked on:` line in PROJECTS.md still matches reality. The orchestrator only edits state when it deliberately works on a project — so abandoned/superseded items sit forever.
2. **`BLOCKED.md` and `PROJECTS.md` are not cross-validated.** They drift independently, and the orchestrator treats each as authoritative without reconciling them.
3. **Block surfacing is one-shot, not persistent.** A new block sends one Discord ping at the moment it's written. After that, the only place it appears is the 2-hour watchdog summary, which is easy to miss. Nothing repeats unresolved-block surfacing per session.
4. **The "user unblocked it" path is fragile.** The orchestrator only picks up unblocks when (a) the user fills in the `Resolution:` field in BLOCKED.md *or* (b) a `Verify with` shell command happens to pass. Conversational/Discord/Inbox unblocks have no automatic capture path.
5. **The session log files have grown past usable size and PROJECTS.md is being used as a worklog.** WORKLOG.md is 2.5 MB / 32,830 lines; PROJECTS.md is 320 KB / 1,862 lines. The orchestrator never compacts these. Stale "Current focus" entries from 4–6 weeks ago are still load-bearing.

The single most important finding: **the orchestrator never asks "is this still true?" about anything it didn't just touch.** Everything else flows from that.

---

## 1. Root Causes of Staleness

### 1.1 No "is this still true?" pass on PROJECTS.md

**Evidence — `.claude/orchestrator-prompt.md` lines 14–26 (the orient step):**
The orient protocol reads `ORCHESTRATOR_STATE.md` (a derived view) and only opens raw files "if you need deeper detail for a specific task you have already chosen." So the orchestrator **never re-examines `Current focus` or `Blocked on` in PROJECTS.md unless it picks that project as today's task.** Low-priority projects (workout, off-grid-living, resume) are therefore never re-validated.

**Evidence in the wild — `PROJECTS.md` line 60 (mfg-farm):**
> `**Current focus**: Session 291: **Business plan COMPLETE** ...`

That focus text references **Session 291**. The most recent session is **937**. mfg-farm's "current focus" hasn't been refreshed in ~646 sessions. The block on test print has been outstanding since 2026-04-12 — 30 days ago — with no escalation.

**Evidence — `PROJECTS.md` line 366 (stockbot):**
> `**Current focus**: 🔴 MAY 12 CHECKPOINT PREPARATION — COMPLETE (Session 922)`
> `**Blocked on**: Engine restart (user action — before 2026-04-28 09:30 ET, CRITICAL)`

The "Blocked on" field is **stale by 14 days** — it references the April 28 engine-restart deadline. The block was actually resolved (BLOCKED.md "Resolved Archive" line 164 shows engine restarted Session 622, 2026-04-29). But because the BLOCKED.md resolution was never reflected back into PROJECTS.md, the stockbot project still claims it's blocked on something that is no longer blocked. Meanwhile its real current blockers (Jetson disk, cron PATH) live only in BLOCKED.md.

This is the classic data-divergence failure: two files, two writers, no reconciliation step.

### 1.2 PROJECTS.md is used as a quasi-worklog

The "Current focus" field has been treated as an append-only narrative log. `stockbot` alone (lines 358–622) contains running history of Sessions 502, 519, 526–537, 552, 560, 570, 651, 656, 659, 694, 697, 714, 829, 922 — 264 lines of historical state inside a single project entry.

**Why this causes staleness:** the script `generate-orchestrator-state.sh` (line 97) truncates the focus to 300 chars with `cut -c1-300`. So whatever happens to be in the **first 300 characters** of the focus block becomes "the truth" the orchestrator sees. For mfg-farm, the first 300 chars are still "Session 291: Business plan COMPLETE" — old text that was prepended once and never moved down.

### 1.3 No "done" signal exists

There's no bullet in the session protocol that says "if a deliverable was completed last session, update the relevant project's status to reflect that and remove the now-stale focus line."

The Resolved Archive in BLOCKED.md works (it's automatically populated when Resolution is filled or Verify passes — orchestrator-prompt.md lines 21–24). **But there is no analogous mechanism for in-PROJECTS.md state.** Completed exploration items go into EXPLORATION_QUEUE.md as `✅ Item N: COMPLETE` — and they *also* never get pruned (the file has 17 items marked complete, none archived).

### 1.4 Session handoff loses nothing — it just adds

CHECKIN.md is 452 lines and has accumulated 18 separate "Session NNN" headings since 2026-05-09. The orchestrator-prompt.md instruction (line 80) says "**Archive** the previous Since Last Check-in section into History" — but in practice every session prepends a new heading and never moves the old one. Discord summary script (`start-orchestrator.sh` lines 56–85) reads only the **first** "Since Last Check-in" heading via regex and stops at the next one, so the user only ever sees the most recent. The other 17 are dead weight that the next orchestrator session has to read past.

---

## 2. Block Notification Failures

### 2.1 What the orchestrator actually does for blocks

From `.claude/orchestrator-prompt.md` lines 53–75 (Handle Blocks + Discord Notifications):

1. Write a new entry to BLOCKED.md (correct format)
2. Commit BLOCKED.md
3. Fire **one** Discord webhook: `[Claude] BLOCKED: brief description — see BLOCKED.md`

That's it. **There is no re-notification on subsequent sessions.** If the first ping is missed (phone on silent, Discord not foreground), the user finds out at the next 2-hour watchdog summary, which only lists block titles ("• stockbot — Manual DB sync...") and does not repeat *what the user is supposed to do*.

### 2.2 The 2-hour watchdog is also weak

`scripts/start-orchestrator.sh` `send_summary()` (lines 86–98):
```python
return "\n".join(f"• {t}" for t in titles[:5]) if titles else "None"
```
It pulls only `### Title` lines from Active Blocks, capped at 5, with no `What I need:` content. The user gets "Active Blocks: • mfg-farm — Test print required" and has to remember what that means or open the file. Blocks older than 5 are silently truncated (currently fine — 3 active — but a structural risk).

### 2.3 New blocks vs. lingering blocks have identical urgency in the UI

A 30-day-old block (mfg-farm test print, blocked 2026-04-12) appears in the same Active Blocks list as a 3-day-old fresh block (Jetson disk, 2026-05-09). Discord summary doesn't age-flag, doesn't bold, doesn't escalate. So the user stops paying attention to the list because it always looks the same.

### 2.4 ORCHESTRATOR_STATE.md doesn't show user actions clearly

Look at the current state file lines 56–77. The "Active Blocks" section is just dumped from `awk` over BLOCKED.md, with no transformation. The user has to read 22 lines of context/verify-commands to extract the actual TODO. Compare to CHECKIN.md, which does have a "USER INPUT NEEDED" header — but the user doesn't see CHECKIN.md unless they `!checkin` over Discord.

### 2.5 Why unblocked issues recur

There are **three** documented mechanisms for the orchestrator to detect an unblock, and they don't always agree:

- **Path 1 — `Resolution:` field filled** (orchestrator-prompt.md line 22): orchestrator reads BLOCKED.md, sees Resolution text, moves to archive.
- **Path 2 — `Verify with:` command passes** (line 23): orchestrator runs the shell command; if exit 0, writes Resolution itself, moves to archive.
- **Path 3 — User mentions it conversationally / via Discord / Inbox**: **no documented capture mechanism.** The orchestrator just won't notice.

The user is most likely to use Path 3 ("oh yeah, I restarted the engine") and least likely to use Path 1 (editing BLOCKED.md is friction). When a user "unblocks" something verbally and Path 3 fires, the block stays Active in BLOCKED.md → next session re-surfaces it → user thinks "I told you that already" → loses trust.

**Concrete example from BLOCKED.md (Resolved Archive):**

Lines 158–163 show *the same engine-restart issue* getting a "Resolution: RESOLVED..." entry, then **eight sessions later** a fresh block appearing for the same condition because nobody validated the engine was still running. The orchestrator doesn't track "I marked this resolved at session N, but I've never re-verified since" — once it's in the archive, it's out of mind. Verify-with is run at orient time only for *active* blocks, never for archived ones.

### 2.6 Path 2 (Verify with) is fragile by design

Most blocks have either `# manual — cannot auto-verify` (mfg-farm test print) or a verify command that requires SSH to the Jetson, which is itself unreliable. So Path 2 fires successfully maybe 30% of the time. The orchestrator can't auto-resolve most of what's in there.

---

## 3. Process Gaps (Rules That Exist vs. What's Actually Followed)

### 3.1 Rules in the prompt that the orchestrator does follow
- ✅ Reading ORCHESTRATOR_STATE.md first
- ✅ Working on highest-priority unblocked project (then exploration queue)
- ✅ Spawning parallel subagents for independent work
- ✅ Committing orchestration files on master at session end
- ✅ Sending one Discord ping per new block
- ✅ Pre/post-session `git checkout master`

### 3.2 Rules that exist but are silently broken
- ❌ "**Archive the previous Since Last Check-in section into History**" (orch-prompt line 80) — last 18 sessions are stacked, none archived.
- ❌ "**Clear processed items from INBOX.md and log in WORKLOG.md what was done**" (line 33) — the INBOX comment for "Path Model item processed 2026-05-12" is still inline in INBOX.md. There's no `## History` archive in INBOX.md; the cleanup script only removes comments older than 7 days.
- ❌ "**For each Active Block ... if Resolution field is blank and block has a Verify with command → run it**" (line 23) — none of the three current active blocks shows verification was attempted in recent worklogs. The cron-PATH block has a verify command but no run record.
- ❌ "**Update CHECKIN.md before each session ends**" (orchestrator.md line 19) — the *most recent* "Since Last Check-in" header in CHECKIN.md is dated 2026-05-09 (Session 937), not 2026-05-12. The orchestrator hasn't updated CHECKIN.md in 3 days even though sessions kept running (per ORCHESTRATOR_STATE.md generated 2026-05-11T23:59:59Z).

### 3.3 Rules that don't exist but should
- ❌ No rule to **prune** PROJECTS.md "Current focus" when it's older than N sessions.
- ❌ No rule to **reconcile** PROJECTS.md `Blocked on:` against BLOCKED.md `## Active Blocks` titles. When they diverge, BLOCKED.md should win.
- ❌ No rule to **re-surface** blocks older than 24 hours via Discord with the "What I need" body, not just the title.
- ❌ No rule to **detect dead projects** — workout, off-grid-living, resume haven't been touched in months but are still in priority order with `Blocked on: —`.
- ❌ No rule to **truncate WORKLOG.md** (currently 2.5 MB; the recent-log slice in ORCHESTRATOR_STATE.md is only the last 40 lines, but git operations and grep over the file are getting expensive).
- ❌ No rule for what to do with **conversational unblocks**. The user has no documented way to say "I did the test print, here's the photo" without manually editing BLOCKED.md.
- ❌ No rule that "**cybersecurity-hardening**" exists — it's priority #3 in PROJECTS.md but is **not in the orchestrator agent map** (`.claude/agents/orchestrator.md` lines 36–40 only lists resistance-research, stockbot, seedwarden, open-source-rideshare, general-research). Same for mfg-farm. So the orchestrator is delegating to `general-research` for half its priority work.

### 3.4 Configuration drift between files
- `AUTONOMOUS_SETUP.md` was last updated 2026-04-10 (line 3). It still lists "containerized-agents" as a project needing definition; that project is in PROJECTS.md but no one is sure it's real.
- `PROJECTS.md` line 7 says "Last updated by orchestrator on 2026-04-27 Session 498" — actually it has been edited since (line 38 mentions Session 937), but the metadata header is wrong.
- The `Projects.priority order` (10 items) doesn't match the `Active Projects` rendered in ORCHESTRATOR_STATE.md (only 9 — `cybersecurity-hardening` is in the priority list but its block on this state file generation is actually showing it as having no blockers, while mfg-farm shows blocked, etc.).

---

## 4. User Responsibilities

These are behaviors the user could adopt that would unblock the system without changing any code:

### 4.1 Always resolve blocks via BLOCKED.md, not chat

**Rule:** when you do something the orchestrator was waiting on, edit `BLOCKED.md` and add one line under `**Resolution**:`. Even just `Resolution: Done 2026-05-12 — engine restarted, AAPL h+10 fired.` is enough — the orchestrator's orient-step machinery will then auto-archive it on the next run.

If you tell the orchestrator over Discord "I did X" and don't touch BLOCKED.md, the block stays active forever.

### 4.2 Use INBOX.md (or `!` Discord) for new direction, not "current focus" edits

The user's `INBOX.md` has a `## New Items` section that the orchestrator processes every session. Using it is the supported channel for redirections and questions. Editing PROJECTS.md "Current focus" by hand is fine but the orchestrator may overwrite it.

### 4.3 Periodically delete stale lines from PROJECTS.md focus blocks

The orchestrator never prunes its own "Current focus" history. About once a week, the user should:
- Open PROJECTS.md
- For each project, keep the **first 1–2 paragraphs** of "Current focus"; delete everything below it that's session NNN history.
- Move historical Session-NNN content into WORKLOG.md if it's not already there (it usually is).

This is currently the only way to keep `generate-orchestrator-state.sh`'s 300-char truncation from showing 4-week-old text.

### 4.4 Confirm or kill quiescent projects

`workout`, `off-grid-living`, `resume`, `containerized-agents`, `open-source-rideshare`, `open-repo` haven't moved meaningfully in weeks. Either declare them paused (the prompt skips paused projects per orient-step rule 3) or delete from priority order. Right now they're noise.

### 4.5 If you say "do X next," put it in INBOX.md the same way

A Discord `!message` becomes an INBOX item via the bot — that does work. The path that fails is when the user says something in a Claude chat session ("when you next start, focus on stockbot Gate 2") — that's not captured anywhere persistent and the next headless orchestrator run won't see it.

---

## 5. Recommended Fixes (Prioritized)

### P0 — Fix this week (highest leverage, smallest change)

**P0.1 — Add a `validate_state.py` step to `generate-orchestrator-state.sh` that fails loudly when state files disagree.**
Specifically:
- For each project section in PROJECTS.md, check that `Blocked on:` text either says `—` / `None` or has a matching `### <project>` entry in BLOCKED.md `## Active Blocks`. If divergent, print a `STATE DRIFT` warning into ORCHESTRATOR_STATE.md so the orchestrator sees it on orient.
- Check that `Last updated by` in PROJECTS.md is within the last 7 days; warn otherwise.
- Check that the "Current focus" first paragraph references a session number within the last 14 sessions; warn otherwise as `STALE FOCUS`.

This costs ~50 lines of Python and would have caught every staleness bug in the current state file.

**P0.2 — Add a `re_notify_blocks()` step at the top of every session.**
In `start-orchestrator.sh`, before invoking Claude, walk BLOCKED.md Active Blocks and send a Discord summary ONCE PER DAY (track via a `.last-block-notify` timestamp file). Format:
```
**[Claude] Daily Blocked Reminder** (3 active blocks)
1. mfg-farm — Test print required (blocked 30 days)
   → What I need: print modrun_clip.stl + modrun_rail.stl, photograph result
2. stockbot — Manual DB sync before May 12 checkpoint (blocked 3 days)
   → What I need: ssh jetson, run sync_db_from_alpaca.py --since 2026-04-29
...
```
Currently blocks are notified once and the user has to remember.

**P0.3 — Add a `## Resolved (Recent)` section to ORCHESTRATOR_STATE.md.**
List the last 5 BLOCKED.md resolutions with date. This gives the user a "did the orchestrator notice my unblock?" feedback loop. Currently there's no signal that the orchestrator saw a resolution other than the block disappearing (and the user can't easily tell that).

**P0.4 — Force the orchestrator to update `CHECKIN.md` every session, not just every check-in.**
Add to the post-session commit step: `if [ ! -n "$(git diff --staged CHECKIN.md)" ]; then echo WARNING NO CHECKIN UPDATE; fi`. Right now sessions silently skip the checkin-update step.

### P1 — Fix this month

**P1.1 — Move the "Current focus" history out of PROJECTS.md.**
Define the rule: PROJECTS.md `Current focus` is **the next 1–2 things** (≤500 chars). Anything else lives in WORKLOG.md. Add a script to one-shot-migrate the existing PROJECTS.md back to that shape — for the 6 projects with bloated focus blocks, this will reclaim ~280 KB.

**P1.2 — Add a `/resolve <project> <note>` Discord command to the bot.**
Today's `discord-bot.py` accepts `!pause`, `!resume`, `!status`, etc. but has no way to mark a block resolved. Add `!resolve <project>` that finds the matching block in BLOCKED.md, fills in `**Resolution**: <note>` and `**Date resolved**: <today>`, lets the next orient-step move it to archive automatically. This solves the "user said it on Discord" failure mode.

**P1.3 — Add the missing project agents to `.claude/agents/orchestrator.md`.**
`cybersecurity-hardening` and `mfg-farm` are priority #3 and #4 — they need their own agent profiles, or the orchestrator agent map needs to be updated to delegate them to `general-research` explicitly.

**P1.4 — Compress WORKLOG.md.**
2.5 MB / 32,830 lines is unsustainable. Add a quarterly archival rotation: `WORKLOG.md` keeps last 60 days; older content moves to `worklog/archive/2026-Q1.md`. Adjust the recent-log tail in the state file generator accordingly.

**P1.5 — Add an `!unblock <id>` mirror of the `/unblock` slash command.**
The `/unblock` slash command (`.claude/commands/unblock.md`) is interactive-Claude-only. Make a Discord-bot equivalent so the user can do it from phone.

### P2 — Structural improvements

**P2.1 — Replace the dual "PROJECTS.md + BLOCKED.md" model with a single source of truth.**
Both files describe project state. The current architecture asks the orchestrator to keep them in sync manually. A small SQLite table (`project_state.db` with columns: project, status, current_focus, blocked_on_id, last_touched) would eliminate the divergence bug entirely. Markdown files become rendered views of the DB, generated each session. This is a multi-week refactor but ends the staleness problem permanently.

**P2.2 — Track block age + escalation.**
Add a `block_age_threshold_days` field. When a block exceeds it (e.g. 14 days), promote its Discord re-notify to `@here` or DM. Right now a 30-day-old block looks identical to a 3-hour-old block.

**P2.3 — Make the orchestrator review every project once per week even if not selected.**
Add to the orient step: "If any project's `last_touched` field is older than 7 days, spend 5 minutes re-reading its Goal and Current focus and asking 'is this still accurate?' Update if not."

### Orchestrator-side vs. user-side

| Fix | Side |
|-----|------|
| P0.1 state-drift validator | Orchestrator |
| P0.2 daily block re-notify | Orchestrator |
| P0.3 Resolved Recent section | Orchestrator |
| P0.4 force CHECKIN update | Orchestrator |
| P1.1 prune PROJECTS focus | Both (script + user discipline) |
| P1.2 `!resolve` Discord cmd | Orchestrator |
| P1.3 add missing agents | Orchestrator |
| P1.4 compress WORKLOG | Orchestrator |
| P1.5 `!unblock` Discord cmd | Orchestrator |
| P2.1 SQLite source of truth | Orchestrator |
| P2.2 block-age escalation | Orchestrator |
| P2.3 weekly project review | Orchestrator |
| **User: always resolve via BLOCKED.md** | **User** |
| **User: use INBOX, not chat, for redirects** | **User** |
| **User: prune Current focus weekly** | **User** (until P1.1) |
| **User: kill or pause quiescent projects** | **User** |

Most of the leverage is on the orchestrator side. The user's main responsibility is **always commit unblocks to a file** (BLOCKED.md or via the new `!resolve` command), never just speak them.

---

## What's Working Well

- **Branch discipline** is enforced structurally (`git checkout master` pre/post session in `start-orchestrator.sh`). This is solid.
- **Usage budget gating** (usage-check.py + USAGE_PAUSE flag + `secs_until_reset()`) is well thought out — the orchestrator can't burn the weekly budget unattended.
- **The compact `ORCHESTRATOR_STATE.md` pattern** (one read instead of five) is the right architecture; it just needs a state-drift validator added.
- **The 90-min session timeout + watchdog** prevents hung sessions from blocking the loop.
- **The Discord bot's INBOX-write path** (with file locking) is correct and race-safe.
- **The exploration queue + parallel subagent execution** generates real value during user-blocked windows — not idle.
- **The Resolved Archive in BLOCKED.md** is a good pattern (auto-archival on Resolution-fill) — it just needs an analog for PROJECTS.md.

---

## Top Findings (one-paragraph each)

**Finding 1 — PROJECTS.md and BLOCKED.md drift independently.** The orchestrator updates each in isolation. Stockbot's PROJECTS.md `Blocked on:` still says "Engine restart before 2026-04-28" — a block resolved 14 days ago — while its real current blockers (cron PATH, Jetson disk) only live in BLOCKED.md. There is no reconciliation step. Add one to `generate-orchestrator-state.sh`.

**Finding 2 — Blocks are notified once and never re-surfaced.** A new block fires one Discord message per the orchestrator-prompt rule. After that, blocks only appear inside the 2-hour watchdog summary as bare titles. A 30-day-old block (mfg-farm test print) looks identical to a 3-hour-old block in every UI. Add a daily Discord re-notification with the "What I need" body and an age tag.

**Finding 3 — User unblocks via chat are silently lost.** Three documented unblock paths exist: Resolution-field, Verify-command-passes, and "user said so." The third path has no machinery. When the user says "I did X" in chat, the block stays Active in BLOCKED.md and re-surfaces next session. Add `!resolve <project>` to the Discord bot.

**Finding 4 — "Current focus" in PROJECTS.md has become an append-only narrative log.** mfg-farm's focus still references Session 291 (now 646 sessions stale). The state generator truncates focus to 300 chars, so the orchestrator's view of "what's happening now" can be stale by weeks. Either prune manually weekly or move the field to a strict ≤500 char rule with all history pushed to WORKLOG.

**Finding 5 — CHECKIN.md was last updated 3 sessions ago.** The orchestrator-prompt requires every-session CHECKIN updates and explicit archival of prior `Since Last Check-in` headings, but neither is being enforced. Eighteen session headings have stacked since 2026-05-09 with no archival. Add a post-session check that fails loudly if CHECKIN.md wasn't modified.

