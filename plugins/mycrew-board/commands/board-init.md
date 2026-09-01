---
description: "Use once per product to stand the board up — install the columns and labels this harness works by, install the rule that keeps the board honest into the product's own rules, and open a milestone for every approved feature the plane already holds. Refuses to run where a board already exists rather than overwriting one. Run at the product root."
argument-hint: "[nothing — it reads the plane]"
---

# /board-init — stand the board up over the plane that already exists

The run ends with a board whose columns and labels are the ones named below, the rule that keeps it
honest installed in the product, one milestone per approved feature, and no tasks — those are the
chief's to write.

## Refuse rather than overwrite

- **A `backlog/` directory already here → stop and say so.** Re-initialising a live board is how a
  week of state disappears. Reconciling an existing board with the plane is a different job.
- **No `docs/product/features.md` at this root → stop and send them to `/ask-me`.** A board over an
  empty plane is a to-do list, and this harness already has better places for those.
- **The `backlog` CLI missing → say how to install it and stop.** Never improvise a board out of
  hand-written markdown; the CLI owns those files.

## Stand it up

- **Initialise with the agent integration off** — `backlog init "<product>" --integration-mode none`.
  Its own instructions would install a directive over every request in this product; the rule that
  governs the board here is the one this command installs, and two rule sets pulling in different
  directions is worse than either alone.
- **Leave the columns as they come: `To Do, In Progress, Done`.** What may be dispatched is decided by
  the origin label and the gate, not by a column, and a column that duplicates a label is one more
  thing to keep in step.
- **Declare the labels** — `from-human`, `from-chief`, `from-lead`, `from-worker`, and `gated` — so
  nothing depends on whoever types them first spelling them the same way. They are the whole of what
  the board knows about where work came from.
- **Open one milestone per approved feature, named as the plane names it.** The board's whole
  connection to the product is this list; a task can only point at a feature that exists here.

## Install the rule that keeps it honest

- **Copy every rule this plugin ships into the product's `.claude/rules/`, in a `backlog/` folder of
  its own.** They ship in the plugin's `rules/`
  (`find ~/.claude/plugins -path '*mycrew-board/rules/*.md'`); rule files are discovered recursively,
  so that folder holds the board's rules together as they grow.
- **Copy them verbatim and never write one of your own.** A rule reworded on the way in is a second
  rule, and what binds the crew has to be the one they were given.
- **A rule already sitting there is left exactly as it is.** The human may have edited it, and their
  copy outranks the shipped one.

## Then stop

- **Write no tasks.** The board is empty on purpose: what gets worked next is the chief's call, made
  from the plane, and this run has no opinion about it.
- **Say what exists now** — the columns, the labels, the rule installed, the milestones opened — and
  name the one command that shows it: `backlog browser` for the board in a browser, `backlog board`
  for it in the terminal.
