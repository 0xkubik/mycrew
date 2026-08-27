---
description: "Use once per product to stand the board up — install the columns and labels this harness works by, and open a milestone for every approved feature the plane already holds. Refuses to run where a board already exists rather than overwriting one. Run at the product root."
argument-hint: "[nothing — it reads the plane]"
---

# /board-init — stand the board up over the plane that already exists

The run ends with a board whose columns and labels match `mycrew-board:board-rules`, one milestone per
approved feature, and no tasks — those are the chief's to write. **Load `board-rules` first**; it
governs everything created here.

## Refuse rather than overwrite

- **A `backlog/` directory already here → stop and say so.** Re-initialising a live board is how a
  week of state disappears. Reconciling an existing board with the plane is a different job.
- **No `docs/product/features.md` at this root → stop and send them to `/ask-me`.** A board over an
  empty plane is a to-do list, and this harness already has better places for those.
- **The `backlog` CLI missing → say how to install it and stop.** Never improvise a board out of
  hand-written markdown; the CLI owns those files.

## Stand it up

- **Initialise with the agent integration off** — `backlog init "<product>" --integration-mode none`.
  Its own instructions would install a directive over every request in this product; the rules that
  govern the board here are `board-rules`, and two rule sets pulling in different directions is worse
  than either alone.
- **Leave the columns as they come: `To Do, In Progress, Done`.** What may be dispatched is decided by
  the origin label and the gate, not by a column, and a column that duplicates a label is one more
  thing to keep in step.
- **Declare the labels** — `from-human`, `from-chief`, `from-lead`, `from-worker`, and `gated` — so
  nothing depends on whoever types them first spelling them the same way. They are the whole of what
  the board knows about where work came from.
- **Open one milestone per approved feature, named as the plane names it.** The board's whole
  connection to the product is this list; a task can only point at a feature that exists here.

## Then stop

- **Write no tasks.** The board is empty on purpose: what gets worked next is the chief's call, made
  from the plane, and this run has no opinion about it.
- **Say what exists now** — the columns, the labels, the milestones opened — and name the one command
  that shows it: `backlog browser` for the board in a browser, `backlog board` for it in the terminal.
