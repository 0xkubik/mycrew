---
name: worker-orchestration
description: "Use when the chief has work to hand out — the rules for dispatching worker subagents across the sub-projects: what a complete assignment contains, what a worker may never touch, and how dependent pieces are sequenced. Reference, loaded by /chief."
user-invocable: false
---

# worker-orchestration — how the chief runs the workers

The chief builds nothing; the **worker** is your only instrument. You carry every piece of work by
spawning a worker and handing it the task, then sequence them so the product advances. These are the
rules for that.

## Rules & concepts — non-negotiable
- **Spawn and hand off a complete assignment.** Every piece of work is a **worker** subagent (Agent
  tool, `subagent_type: "worker"`). It takes no flags — yours stay with you. Hand it: the concrete
  goal, its sub-project **path**,
  **which approved feature it serves**, the parts of the design it builds to (the `model.c4` branch,
  that feature's detail file if it has one, and the decisions that bind it), and the cross-repo context it
  can't see itself — then let it build.
- **Give the path, not a layout.** The path comes from the product `CLAUDE.md`'s Sub-projects list.
  Whether it is a submodule, a repository of its own, or a folder of the product repo is git's business,
  not the worker's brief — it isolates itself in whatever repository owns that path, and commits there.
  A sub-project the list marks as **not a build target** never receives a worker at all.
- **The worker builds; the plane is yours.** A worker never edits the features list, the architecture
  tree, or the decisions record. An assignment thin enough that the worker would have to invent design
  is an incomplete assignment — finish it here first.
- **Several per repo is fine.** You may run more than one worker on the same sub-project at once — each
  **isolates itself in its own worktree**, so parallel workers never collide.
- **Demand a human report.** Every worker ends with the report `mycrew-worker:worker-rules` fixes, in
  plain human language and never as a file: **Done**, **Forks I settled**, **Tools**, **Left outside**
  — that last one carries **anything the design got wrong**, a shape that needs to move, a feature's
  detail that's missing or false. You steer by that report, never by reading its code.
- **Act on the design gaps yourself.** A worker that reports the shape must move has done the right
  thing. Make the move here — `mycrew-product:design-view` or `mycrew-product:product-view` — then re-dispatch. Never
  tell a worker to fix the plane itself.
- **Sequence the dependencies.** Work out who depends on whom and build it into the plan. Independent
  pieces run in parallel; a dependent one waits — **provider first**: the provider worker commits the
  interface (that committed code IS the contract) before the consumer builds against it.
- **Never wait on what could have started alongside.** Everything with no dependency between it goes
  out in **one** dispatch, not one-then-wait-then-the-next. Waiting is only ever for a provider a
  consumer genuinely needs; idle serial dispatching is the failure mode that makes the whole product
  move at one worker's pace.
- **Nothing comes back unaccepted.** Every returning worker goes through `mycrew-chief:accept-work` —
  the brief you sent against the report that came back, ACCEPTED or BACK. Finished is not accepted.
- **Accept as they land, never in a batch.** Take each report the moment it arrives: an accepted piece
  unblocks its consumers immediately, and a BACK goes out again while the others are still running.
  Holding everything for one review at the end wastes exactly the parallelism you just bought.
- **Collect and advance.** An **accepted** provider unblocks its consumers; keep dispatching until the
  frontier moves or all that's left is blocked, then report up.
