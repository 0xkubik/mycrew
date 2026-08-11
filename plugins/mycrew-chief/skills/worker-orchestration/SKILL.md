---
name: worker-orchestration
description: "Use when the chief dispatches workers — spawn a worker subagent per task, run several on one repo (each self-isolates in its own worktree), require a plain-human report from each, and sequence who depends on whom provider-first."
argument-hint: "(reference — the rules for orchestrating workers)"
user-invocable: false
---

# worker-orchestration — how the chief runs the workers

The chief builds nothing; the **worker** is your only instrument. You carry every piece of work by
spawning a worker and handing it the task, then sequence them so the product advances. These are the
rules for that.

## Rules & concepts — non-negotiable
- **Spawn and hand off a complete assignment.** Every piece of work is a **worker** subagent (Agent
  tool, `subagent_type: "worker"`, `--auto`). Hand it: the concrete goal, its sub-project **path**,
  **which approved feature it serves**, the parts of the design it builds to (the `model.c4` branch and
  the specs), and the cross-repo context it can't see itself — then let it build.
- **Give the path, not a layout.** The path comes from the product `CLAUDE.md`'s Sub-projects list.
  Whether it is a submodule, a repository of its own, or a folder of the product repo is git's business,
  not the worker's brief — it isolates itself in whatever repository owns that path, and commits there.
  A sub-project the list marks as **not a build target** never receives a worker at all.
- **The worker builds; the plane is yours.** A worker never edits the features list, the architecture
  tree, or a spec. An assignment thin enough that the worker would have to invent design is an
  incomplete assignment — finish it here first.
- **Several per repo is fine.** You may run more than one worker on the same sub-project at once — each
  **isolates itself in its own worktree**, so parallel workers never collide.
- **Demand a human report.** Require each worker to report back **in plain human language**: what it did, 
  what problems it hit, what forks it resolved, and **anything the design got wrong** — a shape that
  needs to move, a spec that's missing or false. You steer by that report, never by reading its code.
- **Act on the design gaps yourself.** A worker that reports the shape must move has done the right
  thing. Make the move here — `architecture-management` or `spec-management` — then re-dispatch. Never
  tell a worker to fix the plane itself.
- **Sequence the dependencies.** Work out who depends on whom and build it into the plan. Independent
  pieces run in parallel; a dependent one waits — **provider first**: the provider worker commits the
  interface (that committed code IS the contract) before the consumer builds against it.
- **Collect and advance.** A finished provider unblocks its consumers; keep dispatching until the
  frontier moves or all that's left is blocked, then report up.
