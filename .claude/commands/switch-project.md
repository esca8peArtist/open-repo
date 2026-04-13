# /switch-project

Gracefully suspend current work and switch to a different project. Ensures work is logged and committed before switching.

## Steps

1. Log current progress to `WORKLOG.md` — what was done, what's the state, what the next step is
2. Check if there are uncommitted changes in the current project directory
   - If yes: `git add -A && git commit -m "wip: checkpoint before project switch"` in the project directory
3. Update the "Current focus" field in `PROJECTS.md` for the project being suspended
4. If switching due to a block: write the block to `BLOCKED.md` first
5. Identify the next highest-priority unblocked project from `PROJECTS.md`
6. Log the switch in `WORKLOG.md`: "Switching from [old] to [new] — reason: [block/priority/complete]"
7. Load the relevant agent profile from `.claude/agents/` and begin work on the new project

## Arguments

Optionally accepts a project name: `/switch-project stockbot`
If no argument, picks the next highest priority unblocked project automatically.
