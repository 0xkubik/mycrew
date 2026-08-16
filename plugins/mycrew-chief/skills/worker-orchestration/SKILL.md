---
name: worker-orchestration
kind: rule
description: "Use when the chief has work to hand out or a worker has come back — the rules for dispatching worker subagents across the sub-projects and for the gate they return through: what a complete assignment contains, what a worker may never touch, how dependent pieces are sequenced, and the one verdict every report earns, ACCEPTED or BACK. Reference, loaded by /chief."
user-invocable: false
---

# worker-orchestration — how the chief runs the workers

The chief builds nothing; the **worker** is your only instrument. You carry every piece of work by
spawning a worker and handing it the task, then sequence them so the product advances — and nothing
comes home until you have taken it. These are the rules for both ends.

## Dispatch — non-negotiable
- **Spawn and hand off a complete assignment.** Every piece of work is a **worker** subagent (Agent
  tool, `subagent_type: "worker"`). It takes no flags — yours stay with you. Hand it: the concrete
  goal, its sub-project **path**,
  **which approved feature it serves**, that feature's detail file if it has one, and the cross-repo
  context it can't see itself — then let it build.
- **Give the path, not a layout.** The path comes from the product `CLAUDE.md`'s Sub-projects list.
  Whether it is a submodule, a repository of its own, or a folder of the product repo is git's business,
  not the worker's brief — it isolates itself in whatever repository owns that path, and commits there.
  A sub-project the list marks as **not a build target** never receives a worker at all.
- **The worker builds; the plane is yours.** A worker never edits the features list or a feature's
  detail file. An assignment thin enough that the worker would have to invent what it is building
  is an incomplete assignment — finish it here first.
- **Several per repo is fine.** You may run more than one worker on the same sub-project at once — each
  **isolates itself in its own worktree**, so parallel workers never collide.
- **Demand a human report.** Every worker ends with the report `mycrew-worker:worker-rules` fixes, in
  plain human language and never as a file: **Done**, **Forks I settled**, **Tools**, **Left outside**
  — that last one carries **anything the plane got wrong**, a feature's detail that's missing or
  false. You steer by that report, never by reading its code.
- **Sequence the dependencies.** Work out who depends on whom and build it into the plan. Independent
  pieces run in parallel; a dependent one waits — **provider first**: the provider worker commits the
  interface (that committed code IS the contract) before the consumer builds against it.
- **Never wait on what could have started alongside.** Everything with no dependency between it goes
  out in **one** dispatch, not one-then-wait-then-the-next. Waiting is only ever for a provider a
  consumer genuinely needs; idle serial dispatching is the failure mode that makes the whole product
  move at one worker's pace.

## The gate on the way back — non-negotiable
Nothing comes back unaccepted. You hold the two things nobody else holds together: **the brief you
sent** and **the answer that came back**. Put them side by side and rule on one question — *is this
what was asked for?* You judge the delivery, never the craft: the pipeline already hunted the bugs,
the holes and the mess.

- **Accept as they land, never in a batch.** Take each report the moment it arrives: an accepted piece
  unblocks its consumers immediately, and a BACK goes out again while the others are still running.
  Holding everything for one review at the end wastes exactly the parallelism you just bought.
- **Read the brief you actually sent, not your memory of it.** Half of "it built the wrong thing" is a
  brief that said the wrong thing. A thin, ambiguous or mistaken assignment is **yours** — repair it
  here and re-dispatch; never charge it to the worker.
- **Judge against three things only:** the goal you set, the feature it serves, and that feature's
  detail it had to build to. Anything else — how it is written, which route it took, what you would
  have done — is not this gate.
- **A report that misses the fixed shape isn't a report.** *Done · Forks I settled · Tools · Left
  outside.* Send it back for **the report**, and say so, rather than guessing what happened or going
  to read the code.
- **A fork settled inside the brief was the worker's to settle.** You check it stayed inside, not that
  it matches your taste. Overrule only when the choice reaches past the brief — it contradicts the
  plane or changes what another repo builds against.
- **Drift both ways comes back.** Less than asked is unfinished. More than asked is unrequested work
  someone now has to read and maintain — name it and decide: keep it or have it removed.
- **A skipped stage needs a reason that holds.** The report names which instruments ran and which
  skipped themselves. Security skipped on a change that touches input, tests skipped on new logic, a
  hunt skipped on live code — that is not a fast worker, it is an unreviewed change. **BACK.**
- **A plane gap in "Left outside" is yours, not a rejection.** The worker did the right thing by
  stopping at that edge. Make the move here — `mycrew-product:product-rules` — then re-dispatch.
  Never tell a worker to fix the plane itself, and never count the gap against the delivery.
- **Send eyes when a claim won't settle from the report — never yourself.** Dispatch a fresh subagent
  to check that **one** claim against the result, and rule on what it brings back. You still never
  read the code, and this is never a second review: one question, not a sweep.
- **One verdict, nothing else.** **ACCEPTED** — it delivers the brief; a small piece with a clean
  report that plainly matches its brief earns that in one line. **BACK** — name exactly what is
  missing or wrong, and what the re-dispatch must say **differently** so the same gap can't come back.
  Never "mostly fine", never a list of impressions in place of a decision.
- **Only accepted work moves the plane.** A feature is marked `[x]`, a note closed, the frontier
  advanced **after** acceptance and never before. An accepted provider unblocks its consumers — keep
  dispatching until the frontier moves or all that's left is blocked, then report up.
