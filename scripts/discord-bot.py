#!/usr/bin/env python3
"""
Discord bot for two-way communication with the Claude orchestrator.
- Receives messages/commands from user in a designated channel
- Writes tasks to INBOX.md for Claude to pick up next session
- Responds to status commands with info from WORKLOG.md, CHECKIN.md, etc.

Setup:
  DISCORD_BOT_TOKEN=your-bot-token in ~/.claude_env
  DISCORD_CHANNEL_ID=your-channel-id in ~/.claude_env
  DISCORD_OWNER_ID=your-discord-user-id in ~/.claude_env
"""

import fcntl
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import discord

WORKSPACE = Path(
    os.environ.get("CLAUDE_WORKSPACE", Path.home() / "dev/SuperClaude_Framework")
)
INBOX = WORKSPACE / "INBOX.md"
WORKLOG = WORKSPACE / "WORKLOG.md"
CHECKIN = WORKSPACE / "CHECKIN.md"
BLOCKED = WORKSPACE / "BLOCKED.md"
PROJECTS = WORKSPACE / "PROJECTS.md"
SCRIPTS = WORKSPACE / "scripts"

# Add scripts dir to path so we can import usage-check functions
sys.path.insert(0, str(SCRIPTS))

TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")
CHANNEL_ID = int(os.environ.get("DISCORD_CHANNEL_ID", "0"))
OWNER_ID = int(os.environ.get("DISCORD_OWNER_ID", "0"))

MAX_DISCORD_LENGTH = 1900  # leave room for formatting


def read_tail(path: Path, lines: int = 30) -> str:
    """Read last N lines of a file."""
    try:
        content = path.read_text()
        all_lines = content.splitlines()
        return "\n".join(all_lines[-lines:]) if all_lines else "(empty)"
    except FileNotFoundError:
        return f"(file not found: {path.name})"


def read_section(path: Path, section: str, lines: int = 40) -> str:
    """Read from a section header to the next --- or end of file."""
    try:
        content = path.read_text()
        if section not in content:
            return read_tail(path, lines)
        start = content.index(section)
        chunk = content[start:]
        # Stop at next --- separator
        end = chunk.find("\n---", 10)
        result = chunk[:end].strip() if end > 0 else chunk.strip()
        return result[:MAX_DISCORD_LENGTH] or "(empty section)"
    except FileNotFoundError:
        return f"(file not found: {path.name})"


def resolve_block(project: str, note: str) -> str:
    """Write a Resolution line to the first matching active block in BLOCKED.md.
    Returns a status message."""
    import fcntl
    lock_path = BLOCKED.with_suffix(".lock")
    timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    try:
        with open(lock_path, "w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            text = BLOCKED.read_text()
            # Find Active Blocks section
            active_m = re.search(r'## Active Blocks\n(.*?)(?=\n## |\Z)', text, re.DOTALL)
            if not active_m:
                return "⚠️ Could not find Active Blocks section in BLOCKED.md"
            # Find a block matching the project name (case-insensitive prefix match)
            pattern = re.compile(
                r'(### ' + re.escape(project) + r'[^\n]*\n(?:(?!\n###).)*?)'
                r'(\*\*Resolution\*\*:\s*)(\n)',
                re.DOTALL | re.IGNORECASE
            )
            match = pattern.search(active_m.group(0))
            if not match:
                # Try looser match — project name anywhere in the header
                pattern2 = re.compile(
                    r'(### [^\n]*' + re.escape(project) + r'[^\n]*\n(?:(?!\n###).)*?)'
                    r'(\*\*Resolution\*\*:\s*)(\n)',
                    re.DOTALL | re.IGNORECASE
                )
                match = pattern2.search(active_m.group(0))
            if not match:
                titles = re.findall(r'### (.+)', active_m.group(0))
                available = ", ".join(titles) if titles else "none"
                return f"⚠️ No unresolved block found matching '{project}'. Active blocks: {available}"
            resolution_line = f"**Resolution**: {note} (resolved via !resolve {timestamp})\n"
            new_text = text[:active_m.start() + match.start(2)] + resolution_line + text[active_m.start() + match.end(2) + 1:]
            tmp = BLOCKED.with_suffix(".tmp")
            tmp.write_text(new_text)
            os.replace(tmp, BLOCKED)
            block_title = re.search(r'### (.+)', match.group(1))
            title = block_title.group(1) if block_title else project
            return f"✅ Resolution written for: **{title}**\nNote: {note}\nThe orchestrator will archive this block at the next session."
    except Exception as e:
        return f"⚠️ Error writing to BLOCKED.md: {e}"


def add_to_inbox(message: str) -> None:
    """Append a task to INBOX.md under New Items, using a lock file to prevent
    race conditions with concurrent orchestrator writes."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    entry = f"- [{timestamp}] {message}\n"
    lock_path = INBOX.with_suffix(".lock")
    try:
        with open(lock_path, "w") as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            try:
                content = INBOX.read_text()
            except FileNotFoundError:
                content = "# Inbox\n\n## New Items\n"
            if "## New Items\n" in content:
                content = content.replace("## New Items\n", f"## New Items\n{entry}", 1)
            else:
                content += f"\n{entry}"
            INBOX.write_text(content)
            print(f"[{timestamp}] INBOX written: {message[:80]}")
    except Exception as e:
        print(f"[{timestamp}] ERROR writing to INBOX: {e}")


def chunk_message(text: str, max_len: int = MAX_DISCORD_LENGTH) -> list[str]:
    """Split long text into Discord-safe chunks."""
    if len(text) <= max_len:
        return [text]
    chunks = []
    while text:
        chunks.append(text[:max_len])
        text = text[max_len:]
    return chunks


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print(f"[{datetime.now()}] Bot online as {client.user}")
    channel = client.get_channel(CHANNEL_ID)
    if channel:
        await channel.send(
            "**[Claude]** Bot online — orchestrator is running. Type `!help` for commands."
        )


@client.event
async def on_message(message: discord.Message):
    # Ignore messages from the bot itself
    if message.author == client.user:
        return

    # Only respond in the designated channel
    if message.channel.id != CHANNEL_ID:
        return

    # Only respond to the owner
    if OWNER_ID and message.author.id != OWNER_ID:
        return

    content = message.content.strip()

    # ── Commands ──────────────────────────────────────────────────────────────

    if content.lower() == "!help":
        help_text = (
            "**Claude Orchestrator Commands**\n\n"
            "**Read state**\n"
            "`!status` — last 20 lines of WORKLOG.md\n"
            "`!checkin` — current check-in briefing (CHECKIN.md)\n"
            "`!blocked` — items waiting on your input (BLOCKED.md)\n"
            "`!inbox` — current unprocessed items in INBOX.md\n"
            "`!projects` — active project list (PROJECTS.md)\n"
            "`!log N` — last N lines of WORKLOG.md (default 20)\n"
            "`!usage` — current weekly Claude usage vs budget\n\n"
            "**Write state**\n"
            "`!resolve <project> <note>` — mark a block resolved in BLOCKED.md\n"
            "    Example: `!resolve stockbot cron PATH fix deployed`\n"
            "`!pause [reason]` — pause autonomous project work\n"
            "`!resume` — resume autonomous work (clears pause/override)\n\n"
            "**Inbox**\n"
            "Any non-command message → added to INBOX.md as a task for Claude"
        )
        await message.channel.send(help_text)

    elif content.lower() == "!status":
        text = read_tail(WORKLOG, 20)
        for chunk in chunk_message(f"**WORKLOG (last 20 lines)**\n```\n{text}\n```"):
            await message.channel.send(chunk)

    elif content.lower().startswith("!log"):
        parts = content.split()
        n = int(parts[1]) if len(parts) > 1 and parts[1].isdigit() else 20
        text = read_tail(WORKLOG, n)
        for chunk in chunk_message(f"**WORKLOG (last {n} lines)**\n```\n{text}\n```"):
            await message.channel.send(chunk)

    elif content.lower() == "!checkin":
        text = read_section(CHECKIN, "## Since Last Check-in")
        for chunk in chunk_message(f"**CHECKIN**\n{text}"):
            await message.channel.send(chunk)

    elif content.lower() == "!blocked":
        text = read_section(BLOCKED, "## Active Blocks")
        for chunk in chunk_message(f"**BLOCKED**\n{text}"):
            await message.channel.send(chunk)

    elif content.lower() == "!inbox":
        text = read_section(INBOX, "## New Items")
        for chunk in chunk_message(f"**INBOX (unprocessed)**\n{text}"):
            await message.channel.send(chunk)

    elif content.lower() == "!projects":
        text = read_tail(PROJECTS, 50)
        for chunk in chunk_message(f"**PROJECTS**\n```\n{text}\n```"):
            await message.channel.send(chunk)

    elif content.lower().startswith("!resolve"):
        parts = content.split(None, 2)
        if len(parts) < 3:
            await message.channel.send(
                "Usage: `!resolve <project> <resolution note>`\n"
                "Example: `!resolve stockbot cron PATH fix deployed`"
            )
        else:
            project_name = parts[1]
            resolution_note = parts[2]
            result = resolve_block(project_name, resolution_note)
            await message.channel.send(result)

    elif content.lower() == "!usage":
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "usage_check", SCRIPTS / "usage-check.py"
            )
            uc = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(uc)
            r = uc.build_report()
            u = r["usage"]
            b = r["budgets"]
            s = r["status"]
            pause_state = uc.read_pause_state()
            flag = "🔴" if s["over_weekly_budget"] else ("🟡" if s["warn_weekly_budget"] else "🟢")
            pause_note = ""
            if pause_state.get("paused"):
                if pause_state.get("override"):
                    pause_note = "\n⚠️ **Override active** — orchestrator resuming despite pause"
                else:
                    pause_note = "\n⏸️ **Orchestrator paused** — reply `!resume` to continue"
            lines = [
                f"{flag} **Claude Usage — {r['current_week']}**",
                f"```",
                f"This week : {u['this_week']}/{b['weekly']} sessions ({s['week_pct']}%)",
                f"Today     : {u['today']}/{b['daily']} sessions ({s['day_pct']}%)",
                f"Rolling 7d: {u['rolling_7d']} sessions",
                f"All-time  : {u['total_all_time']} sessions",
                f"```",
                f"**Recommendation**: {r['recommendation']}",
            ]
            if pause_note:
                lines.append(pause_note)
            lines.append("\nVerify actual usage: claude.ai → Settings → Usage & billing")
            for chunk in chunk_message("\n".join(lines)):
                await message.channel.send(chunk)
        except Exception as e:
            await message.channel.send(f"⚠️ Error reading usage: {e}")

    elif content.lower().startswith("!pause"):
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "usage_check", SCRIPTS / "usage-check.py"
            )
            uc = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(uc)
            parts = content.split(None, 1)
            reason = parts[1].strip() if len(parts) > 1 else "Manually paused by user via Discord"
            uc.write_pause_state(paused=True, reason=reason, override=False)
            add_to_inbox(f"!pause received via Discord: {reason}")
            await message.channel.send(
                f"⏸️ **Orchestrator paused.**\nReason: {reason}\n"
                "All autonomous project work will halt at the next session check-in.\n"
                "Reply `!resume` when ready to continue."
            )
        except Exception as e:
            await message.channel.send(f"⚠️ Error writing pause state: {e}")

    elif content.lower() == "!resume":
        try:
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                "usage_check", SCRIPTS / "usage-check.py"
            )
            uc = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(uc)
            state = uc.read_pause_state()
            was_paused = state.get("paused", False)
            uc.write_pause_state(paused=False, override=False)
            add_to_inbox("!resume received via Discord — orchestrator cleared to continue")
            if was_paused:
                await message.channel.send(
                    "▶️ **Orchestrator resumed.**\n"
                    "Autonomous project work will continue at the next session.\n"
                    "Check claude.ai → Settings → Usage & billing for remaining capacity."
                )
            else:
                await message.channel.send(
                    "▶️ Orchestrator was not paused — no change needed.\n"
                    "Added resume note to INBOX.md."
                )
        except Exception as e:
            await message.channel.send(f"⚠️ Error clearing pause state: {e}")

    else:
        # Any non-command message becomes a task in INBOX.md
        add_to_inbox(content)
        await message.reply(
            f"Added to inbox: *{content[:100]}*\nClaude will pick it up next session."
        )


if __name__ == "__main__":
    if not TOKEN:
        print("ERROR: DISCORD_BOT_TOKEN not set in ~/.claude_env")
        exit(1)
    if not CHANNEL_ID:
        print("ERROR: DISCORD_CHANNEL_ID not set in ~/.claude_env")
        exit(1)
    client.run(TOKEN)
