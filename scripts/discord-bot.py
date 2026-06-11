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
from discord.ext import tasks

WORKSPACE = Path(
    os.environ.get("CLAUDE_WORKSPACE", Path.home() / "dev/SuperClaude_Framework")
)
INBOX = WORKSPACE / "INBOX.md"
WORKLOG = WORKSPACE / "WORKLOG.md"
CHECKIN = WORKSPACE / "CHECKIN.md"
BLOCKED = WORKSPACE / "BLOCKED.md"
PROJECTS = WORKSPACE / "PROJECTS.md"
NOTIFY_QUEUE = WORKSPACE / "NOTIFY_QUEUE.md"
SCRIPTS = WORKSPACE / "scripts"

# Add scripts dir to path so we can import usage-check functions
sys.path.insert(0, str(SCRIPTS))

TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "")
CHANNEL_ID = int(os.environ.get("DISCORD_CHANNEL_ID", "0"))
OWNER_ID = int(os.environ.get("DISCORD_OWNER_ID", "0"))
MOM_USER_ID = int(os.environ.get("DISCORD_MOM_USER_ID", "0"))
_whisper_model = None


def get_whisper_model():
    global _whisper_model
    if _whisper_model is None:
        from faster_whisper import WhisperModel
        _whisper_model = WhisperModel("base", device="cpu", compute_type="int8")
    return _whisper_model

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
    """Read from a section header to the next --- separator or next ## heading."""
    try:
        content = path.read_text()
        if section not in content:
            return read_tail(path, lines)
        start = content.index(section)
        chunk = content[start:]
        # Stop at next --- separator or next sibling ## heading (whichever comes first)
        candidates = [chunk.find("\n---", 10), chunk.find("\n## ", len(section))]
        stops = [c for c in candidates if c > 0]
        end = min(stops) if stops else -1
        result = chunk[:end].strip() if end > 0 else chunk.strip()
        return result or "(empty section)"
    except FileNotFoundError:
        return f"(file not found: {path.name})"


def parse_active_blocks() -> list[dict]:
    """Parse BLOCKED.md active blocks into compact dicts {title, project, what_i_need}."""
    try:
        content = BLOCKED.read_text()
        active_m = re.search(r'## Active Blocks\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
        if not active_m:
            return []
        blocks = []
        for block_text in re.split(r'\n(?=### )', active_m.group(1)):
            if not block_text.strip():
                continue
            title_m = re.match(r'### (.+)', block_text)
            if not title_m:
                continue
            title = title_m.group(1).strip()
            project = re.split(r'\s*[—–]\s*', title, 1)[0].strip()
            res_m = re.search(r'\*\*Resolution\*\*:\s*(.+)', block_text)
            resolution = res_m.group(1).strip() if res_m else ''
            if resolution and resolution != '[leave blank]':
                continue  # already resolved, skip
            need_m = re.search(r'\*\*What I need\*\*:\s*(.*?)(?=\n\*\*|\Z)', block_text, re.DOTALL)
            what_i_need = need_m.group(1).strip() if need_m else '(see full detail below)'
            if len(what_i_need) > 200:
                what_i_need = what_i_need[:197] + '...'
            blocks.append({'title': title, 'project': project, 'what_i_need': what_i_need})
        return blocks
    except FileNotFoundError:
        return []


def _update_blocked_field(filepath: Path, field_re: str, project: str, new_value: str) -> str | None:
    """Find **Blocked[...]**: in project's section and replace its value.
    Returns the old blocked text if found and changed, else None."""
    lines = filepath.read_text().splitlines(keepends=True)
    in_project = False
    result_lines = []
    old_value = None
    for line in lines:
        if re.match(r'^### ', line):
            in_project = bool(re.match(r'^### ' + re.escape(project) + r'\b', line, re.IGNORECASE))
        if in_project and re.match(field_re, line):
            m = re.match(r'(' + field_re + r'\s*)(.*)', line.rstrip('\n'))
            if m:
                old_value = m.group(2).strip()
                line = m.group(1) + new_value + '\n'
                in_project = False  # only update first match per project
        result_lines.append(line)
    if old_value is not None:
        tmp = filepath.with_suffix('.tmp')
        tmp.write_text(''.join(result_lines))
        os.replace(tmp, filepath)
    return old_value


def _prepend_focus_resolution(filepath: Path, project: str, marker: str) -> bool:
    """Prepend a resolution marker to **Current focus**: (PROJECTS.md) or
    **Focus**: (ORCHESTRATOR_STATE.md) for the given project section.
    Returns True if the field was found and updated."""
    lines = filepath.read_text().splitlines(keepends=True)
    in_project = False
    result_lines = []
    updated = False
    # Match both field names used across the two files
    focus_re = re.compile(r'^(\*\*(?:Current focus|Focus)\*\*:\s*)(.*)', re.DOTALL)
    for line in lines:
        if re.match(r'^### ', line):
            in_project = bool(re.match(r'^### ' + re.escape(project) + r'\b', line, re.IGNORECASE))
        if in_project and not updated:
            m = focus_re.match(line.rstrip('\n'))
            if m:
                prefix, rest = m.group(1), m.group(2)
                # Don't double-stamp if already resolved
                if not rest.startswith('[RESOLVED') and not rest.startswith('[PATH DECIDED'):
                    line = f"{prefix}{marker} {rest}\n"
                    updated = True
                    in_project = False
        result_lines.append(line)
    if updated:
        tmp = filepath.with_suffix('.tmp')
        tmp.write_text(''.join(result_lines))
        os.replace(tmp, filepath)
    return updated


def resolve_project_block(project: str, note: str, timestamp: str) -> str:
    """Update **Blocked on** + **Current focus** in PROJECTS.md and the
    matching fields in ORCHESTRATOR_STATE.md so the resolution survives
    into the next orchestrator session without being overwritten."""
    cleared = f"— resolved {timestamp}: {note}"
    focus_marker = f"[RESOLVED {timestamp}: {note}]"
    updated = []

    try:
        old = _update_blocked_field(PROJECTS, r'\*\*Blocked on\*\*:', project, cleared)
        if old is not None:
            updated.append(f"PROJECTS.md (**Blocked on**: was: _{old}_)")
    except Exception as e:
        return f"⚠️ Error updating PROJECTS.md: {e}"

    # Also stamp **Current focus** so the resolution survives orchestrator rewrites
    try:
        if _prepend_focus_resolution(PROJECTS, project, focus_marker):
            updated.append("PROJECTS.md (**Current focus**: resolution marker prepended)")
    except Exception:
        pass

    state_file = WORKSPACE / "ORCHESTRATOR_STATE.md"
    try:
        old2 = _update_blocked_field(state_file, r'\*\*Blocked\*\*:', project, cleared)
        if old2 is not None:
            updated.append("ORCHESTRATOR_STATE.md (**Blocked** updated)")
    except Exception:
        pass

    # Also update **Focus** in ORCHESTRATOR_STATE.md — this is what the orchestrator reads
    try:
        if _prepend_focus_resolution(state_file, project, focus_marker):
            updated.append("ORCHESTRATOR_STATE.md (**Focus**: resolution marker prepended)")
    except Exception:
        pass  # state file is auto-generated; PROJECTS.md updates are what matter

    if not updated:
        return (
            f"⚠️ No **Blocked on** field found for **{project}** in PROJECTS.md.\n"
            f"Check the project name matches exactly (e.g. `mfg-farm`, `resistance-research`, `seedwarden`)."
        )

    return (
        f"✅ Block cleared for **{project}**\n"
        + "\n".join(f"• {u}" for u in updated)
        + f"\nNote: _{note}_"
    )


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
                # No formal BLOCKED.md entry — update PROJECTS.md and
                # ORCHESTRATOR_STATE.md directly so the change is immediate.
                result = resolve_project_block(project, note, timestamp)
                add_to_inbox(f"[UNBLOCKED] {project}: {note}")
                return result
            resolution_line = f"**Resolution**: {note} (resolved via !resolve {timestamp})\n"
            new_text = text[:active_m.start() + match.start(2)] + resolution_line + text[active_m.start() + match.end(2) + 1:]
            tmp = BLOCKED.with_suffix(".tmp")
            tmp.write_text(new_text)
            os.replace(tmp, BLOCKED)
            block_title = re.search(r'### (.+)', match.group(1))
            title = block_title.group(1) if block_title else project
            add_to_inbox(f"[UNBLOCKED] {project}: {note}")
            return f"✅ Resolution written for: **{title}**\nNote: {note}\nThe orchestrator will archive this block at the next session."
    except Exception as e:
        return f"⚠️ Error writing to BLOCKED.md: {e}"


def read_project_blocks() -> list[tuple[str, str]]:
    """Parse ORCHESTRATOR_STATE.md for project-level Blocked fields."""
    state_file = WORKSPACE / "ORCHESTRATOR_STATE.md"
    try:
        content = state_file.read_text()
        results = []
        current_project = None
        for line in content.splitlines():
            m = re.match(r'^### (.+)', line)
            if m:
                current_project = m.group(1).strip()
            elif current_project and re.match(r'^\*\*Blocked\*\*:', line):
                blocked_text = line.split('**Blocked**:', 1)[1].strip()
                if blocked_text and not re.match(r'^(—|None|none|-)', blocked_text):
                    results.append((current_project, blocked_text))
        return results
    except FileNotFoundError:
        return []


def _extract_project_section(project: str) -> list[str]:
    """Return the raw lines of a project's section from PROJECTS.md."""
    try:
        lines = PROJECTS.read_text().splitlines()
    except FileNotFoundError:
        return []
    for strict in (True, False):
        in_project = False
        section = []
        for line in lines:
            if re.match(r'^### ', line):
                if in_project:
                    break
                pattern = (r'^### ' + re.escape(project) + r'\b') if strict else re.escape(project)
                if re.search(pattern, line, re.IGNORECASE):
                    in_project = True
            if in_project:
                section.append(line)
        if section:
            return section
    return []


def read_project_detail(project: str) -> str:
    """Return a decision-focused brief for a blocked project."""
    section = _extract_project_section(project)
    if not section:
        return f"No project found matching '{project}' in PROJECTS.md."

    # Extract key fields by scanning lines
    fields: dict[str, str] = {}
    options: list[str] = []

    for line in section:
        # Named fields
        for field in ("Blocked on", "Status", "Current focus"):
            m = re.match(r'\*\*' + re.escape(field) + r'\*\*:\s*(.*)', line)
            if m:
                fields[field] = m.group(1).strip()

        # Option/path/track bullet lines — must start the label with Path/Option/Track
        if re.match(r'\s*[-•]\s*\*\*(Path|Option|Track)\s', line, re.IGNORECASE):
            cleaned = re.sub(r'\*\*', '', line).strip().lstrip('-• ').rstrip('.')
            if len(cleaned) > 120:
                cleaned = cleaned[:117] + '...'
            options.append(cleaned)

    # Build the brief
    out = []

    blocked = fields.get("Blocked on", "").strip()
    if not blocked or re.match(r'^(—|None|none|-)', blocked):
        out.append("✅ No active block recorded for this project.")
    else:
        out.append(f"🔴 BLOCKED: {blocked}")

    # Status (short) — strip markdown and session references
    status = fields.get("Status", "")
    if status:
        status = re.sub(r'\*\*', '', status)
        status = re.sub(r'\(Sessions?[^)]+\)', '', status).strip().rstrip(',')
        if len(status) > 150:
            status = status[:147] + '...'
        out.append(f"Status: {status}")

    # Current focus — strip "Session NNN:" prefix, extract deadline if present
    focus = fields.get("Current focus", "")
    if focus:
        focus = re.sub(r'^Session \d+:\s*', '', focus).strip()
        # Surface any deadline
        deadline_m = re.search(r'(deadline|due|hearing|launch|checkpoint)[^.–—]*?((?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\w*\s+\d+|\d{4}-\d{2}-\d{2})', focus, re.IGNORECASE)
        if deadline_m:
            out.append(f"⏰ Deadline: {deadline_m.group(0).strip()}")
        # Show trimmed focus (cut at 200 chars)
        focus_short = focus if len(focus) <= 200 else focus[:197] + '...'
        out.append(f"Context: {focus_short}")

    if options:
        out.append("\nOptions:")
        for opt in options:
            out.append(f"  • {opt}")
    elif blocked and not re.match(r'^(—|None|none|-)', blocked):
        out.append("\n(No explicit options listed — check project dir for decision docs.)")

    return '\n'.join(out)


def normalize_voice_command(text: str) -> str:
    """Map spoken phrases to bot command syntax before dispatch."""
    # "exclamation blocked" / "exclamation mark blocked" / "bang blocked" → "!blocked"
    text = re.sub(r'(?i)^(exclamation\s*(mark|point)?|bang)\s+', '!', text.strip())
    return text


async def transcribe_voice(attachment: discord.Attachment) -> str:
    """Download a Discord voice note and transcribe it via local faster-whisper."""
    import asyncio
    import tempfile

    audio_bytes = await attachment.read()
    suffix = ".ogg"
    name = attachment.filename.lower()
    if name.endswith(".mp3"):
        suffix = ".mp3"
    elif name.endswith(".wav"):
        suffix = ".wav"
    elif name.endswith(".m4a"):
        suffix = ".m4a"

    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as f:
        f.write(audio_bytes)
        tmp_path = f.name
    try:
        def _transcribe():
            model = get_whisper_model()
            segments, _ = model.transcribe(tmp_path)
            return " ".join(s.text for s in segments).strip()

        return await asyncio.get_event_loop().run_in_executor(None, _transcribe)
    finally:
        os.unlink(tmp_path)


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


@tasks.loop(seconds=30)
async def poll_notify_queue():
    """Send any pending [ ] items from NOTIFY_QUEUE.md to the Discord channel."""
    if not NOTIFY_QUEUE.exists():
        return
    try:
        content = NOTIFY_QUEUE.read_text()
        lines = content.splitlines()
        pending = [(i, line) for i, line in enumerate(lines) if re.match(r'^- \[ \] ', line)]
        if not pending:
            return
        channel = client.get_channel(CHANNEL_ID)
        if not channel:
            return
        new_lines = lines.copy()
        for i, line in pending:
            msg = line[6:].strip()  # strip "- [ ] "
            await channel.send(f"🔔 **Orchestrator**: {msg}")
            new_lines[i] = "- [x] " + msg
        tmp = NOTIFY_QUEUE.with_suffix(".tmp")
        tmp.write_text("\n".join(new_lines) + "\n")
        os.replace(tmp, NOTIFY_QUEUE)
    except Exception as e:
        print(f"[notify_queue] Error: {e}")


@poll_notify_queue.before_loop
async def before_poll_notify_queue():
    await client.wait_until_ready()


@client.event
async def on_ready():
    print(f"[{datetime.now()}] Bot online as {client.user}")
    poll_notify_queue.start()
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

    # Route mom's messages directly to mom-projects inbox, no commands
    if MOM_USER_ID and message.author.id == MOM_USER_ID:
        content = message.content.strip()
        if content:
            add_to_inbox(f"[mom-projects] {content}")
            await message.reply("Got it — I'll pass that along.")
        return

    # Only respond to the owner for all other commands
    if OWNER_ID and message.author.id != OWNER_ID:
        return

    content = message.content.strip()

    # ── Voice message transcription ───────────────────────────────────────────
    if not content and message.attachments:
        for att in message.attachments:
            if att.content_type and att.content_type.startswith("audio/"):
                try:
                    content = normalize_voice_command(await transcribe_voice(att))
                    await message.channel.send(f"🎙️ *{content[:150]}*")
                except Exception as e:
                    await message.channel.send(f"⚠️ Transcription failed: {e}")
                    return
                break

    if not content:
        return

    # ── Commands ──────────────────────────────────────────────────────────────

    if content.lower() == "!help":
        help_text = (
            "**Claude Orchestrator Commands**\n\n"
            "**Read state**\n"
            "`!status` — last 20 lines of WORKLOG.md\n"
            "`!checkin` — current check-in briefing (CHECKIN.md)\n"
            "`!blocked` — all blocks: formal BLOCKED.md entries + project-level user actions\n"
            "`!block <project>` — full detail for one project (focus, blocked reason, notes)\n"
            "    Example: `!block mfg-farm`\n"
            "`!inbox` — current unprocessed items in INBOX.md\n"
            "`!projects` — active project list (PROJECTS.md)\n"
            "`!log N` — last N lines of WORKLOG.md (default 20)\n"
            "`!usage` — current weekly Claude usage vs budget\n\n"
            "**Write state**\n"
            "`!resolve <project> <note>` — mark a block resolved in BLOCKED.md\n"
            "    Format: `!resolve <project-name> <what you did>`\n"
            "    Example: `!resolve stockbot cron PATH fix deployed to Jetson`\n"
            "    Example: `!resolve mfg-farm test print done, snap arm holds at 0.4mm gap`\n"
            "    Example: `!resolve seedwarden tag corrections applied, Etsy account verified`\n"
            "⚠️ **IMPORTANT**: If you do something the orchestrator was waiting on, you MUST\n"
            "   use `!resolve`. Saying it in chat or a Claude session will NOT clear the block —\n"
            "   only `!resolve` (or editing BLOCKED.md directly) persists across sessions.\n\n"
            "`!pause [reason]` — pause autonomous project work\n"
            "    Example: `!pause going offline for 3 days`\n"
            "`!resume` — resume autonomous work (clears pause)\n\n"
            "**Send tasks or decisions to the orchestrator**\n"
            "Any non-command message → added to INBOX.md, picked up next session\n"
            "    Example: `focus on stockbot Gate 2 next session`\n"
            "    Example: `resistance-research: switch to distribution path A+37`\n"
            "    Example: `seedwarden launch approved for May 30`\n"
            "⚠️ **IMPORTANT**: Claude chat sessions are NOT captured by the orchestrator.\n"
            "   Only messages sent here in Discord are written to INBOX.md and acted on."
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
        blocks = parse_active_blocks()
        project_blocks = read_project_blocks()

        lines = []
        if blocks:
            lines.append(f"**BLOCKED ({len(blocks)} item{'s' if len(blocks) != 1 else ''})**\n")
            for i, b in enumerate(blocks, 1):
                lines.append(f"**{i}. {b['title']}**")
                lines.append(f"Needs: {b['what_i_need']}")
                lines.append(f"→ `!resolve {b['project']} <what you did>`\n")
            lines.append("_Use `!block <project>` for full context on any item._")
        else:
            lines.append("**BLOCKED** — No active blocks ✅")

        if project_blocks:
            lines.append("\n**Project-level actions needed** (ORCHESTRATOR_STATE.md):")
            for proj, block in project_blocks:
                block_short = block[:150] + '...' if len(block) > 150 else block
                lines.append(f"• **{proj}**: {block_short}")
            lines.append("_Use `!resolve <project> <what you did>` to clear._")

        for chunk in chunk_message("\n".join(lines)):
            await message.channel.send(chunk)

    elif content.lower().startswith("!block "):
        project_name = content[7:].strip()
        text = read_project_detail(project_name)
        for chunk in chunk_message(f"**{project_name} — full detail**\n```\n{text}\n```"):
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

    elif content.startswith("!"):
        # Unrecognised command — don't pollute INBOX
        await message.reply(
            f"Unknown command: `{content.split()[0]}`\nType `!help` for available commands."
        )

    else:
        # Plain text message → task in INBOX.md
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
