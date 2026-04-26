---
name: General Collaboration Feedback
description: Corrections and preferences about how to approach work with Anya
type: feedback
---

## File transfers: default to rsync, not scp/cp

Always suggest `rsync` for file transfer tasks instead of `scp` or `cp`. The user uses rsync as the standard tool across this environment.

**Why:** User explicitly corrected this — rsync is the established default in this workspace.

**How to apply:** Any time a file copy/transfer is needed (Pi ↔ Jetson, Pi ↔ laptop, local copies), lead with rsync. Only fall back to scp/cp if rsync isn't available or the context makes it inappropriate.
