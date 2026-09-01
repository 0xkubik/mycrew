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
- **Right after init, bring `backlog/config.yml` to the shape below — every key the CLI ships is in it,
  active or commented, so nothing about the board is a key someone has to go find in the CLI's own
  docs.** Keep the `project_name` and `task_prefix` init already wrote; `statuses` and `labels` are the
  two keys the CLI won't take as a flag or a `config set`, set here to what this board needs — a
  `Backlog` column ahead of the CLI's own three, and the five origin/gate labels declared so nothing
  depends on whoever types them first spelling them the same way. Every other key is left at the CLI's
  own default and commented out, so it's there to uncomment rather than something to rediscover:

  ```yaml
  project_name: "<as init wrote it>"
  default_status: "To Do"
  statuses: ["Backlog", "To Do", "In Progress", "Done"]
  labels: ["from-human", "from-chief", "from-lead", "from-worker", "gated"]
  date_format: yyyy-mm-dd
  max_column_width: 20
  auto_open_browser: true
  default_port: 6420
  remote_operations: true
  auto_commit: false
  filesystem_only: false
  bypass_git_hooks: false
  check_active_branches: true
  active_branch_days: 30
  task_prefix: "<as init wrote it>"
  # hide_empty_columns: false             # hide board columns with no cards
  # types: [bug, feature, enhancement, task, chore, docs, spike]  # allowed --type values
  # default_assignee: []                  # assignees applied to new tasks created without -a
  # definition_of_done:                   # default Definition of Done items added to every new task
  #   - Tests pass
  # priorities: ["High", "Medium", "Low"] # ordered priority labels, first sorts highest
  # projects: ["web", "api"]              # allowed --project values for a monorepo backlog
  # include_datetime_in_dates: true       # add time-of-day to new dates
  # default_editor: "code --wait"         # editor opened by the 'E' key
  # zero_padded_ids: true                 # pad task/doc/decision IDs with leading zeros
  # on_status_change: "..."               # shell command run on every status change
  ```
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
