# Notification Queue

> The orchestrator writes pending push notifications here as `- [ ] message`.
> The Discord bot polls this file every 30 seconds and sends any `[ ]` items
> to the Discord channel, then marks them `[x]`.
>
> **Orchestrator instructions**: Write to this file (append under Pending) whenever:
> - A new block is added to BLOCKED.md (copy the block title + what you need)
> - A sprint is complete (all items in SPRINT.md checked off)
> - A decision gate is reached that cannot proceed without user input
> - A deployment is ready for user approval
>
> Format: `- [ ] [PROJECT] message — what you need from the user`

---

## Pending

- [x] [stockbot] Pause cleared and Sprint 3 started — orchestrator resuming autonomous dev loop. First task: buy_prob flatline investigation + backtesting pipeline. Will notify when blocked or sprint complete.

---

## Sent Archive

