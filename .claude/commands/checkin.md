# /checkin

Prepare a check-in briefing for the user. Read all state files and produce a concise, scannable summary that gets the user up to speed in under 5 minutes.

## Steps

1. Read `PROJECTS.md` for current priorities and status
2. Read the last 50 lines of `WORKLOG.md` for recent activity
3. Read `BLOCKED.md` for active blocks
4. Read `INBOX.md` for any unprocessed items
5. Read the current "Since Last Check-in" section of `CHECKIN.md`

## Output Format

Produce a briefing in this format:

```
## Check-in Briefing — [date]

### What happened
- [project]: [specific thing accomplished]
- [project]: [specific thing accomplished]

### In progress
- [project]: [what's being worked on]

### Needs your input
- [ ] [specific question or decision needed]
- [ ] [PR/push ready for approval — link or description]

### Blocked (waiting on you)
- [project]: [what's blocked and what you need to provide]

### Suggested focus for next session
1. [highest value thing user could do]
2. [second priority]

### Unprocessed inbox items
- [any items in INBOX.md that haven't been actioned]
```

Then update `CHECKIN.md` with this briefing.
