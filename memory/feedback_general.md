---
name: General Collaboration Feedback
description: Corrections and preferences about how to approach work with Anya
type: feedback
---

## Always check the clock before stating time or day of week

Always run `date` via Bash before making any claim about the current time, day of week, or whether the market is open. Never infer the day of week from context (e.g. "market is closed therefore it must be a weekend"). April 27, 2026 is a Monday — inferring "Sunday" from a closed market in the evening was wrong and caused a missed trading day diagnosis.

**Why:** This has happened multiple times. The system-reminder provides a date but not the day of week, and internal reasoning about calendar arithmetic is unreliable. The clock is always available and always correct.

**How to apply:** Any time a response involves the current time, market status, day of week, or time-sensitive decisions — run `date` first, use the output, do not guess.

---

## File transfers: default to rsync, not scp/cp

Always suggest `rsync` for file transfer tasks instead of `scp` or `cp`. The user uses rsync as the standard tool across this environment.

**Why:** User explicitly corrected this — rsync is the established default in this workspace.

**How to apply:** Any time a file copy/transfer is needed (Pi ↔ Jetson, Pi ↔ laptop, local copies), lead with rsync. Only fall back to scp/cp if rsync isn't available or the context makes it inappropriate.
