# /unblock

Process a user's unblocking input and resume suspended work.

## Usage

Run this after you've added resolution notes to `BLOCKED.md` or `CHECKIN.md`.

## Steps

1. Read all active entries in `BLOCKED.md`
2. For each entry with a non-empty "Resolution" field:
   - Acknowledge what the user provided
   - Apply the resolution (answer the question, use the provided context, make the decision)
   - Move the resolved block to the "Resolved" archive section in `BLOCKED.md`
   - Log in `WORKLOG.md`: "[project] unblocked — [resolution summary]"
3. If the unblocked project is higher priority than what's currently active, offer to switch to it
4. Update "Current focus" in `PROJECTS.md` for the newly unblocked project
5. Ask: "Ready to resume [project name]?"
