---
name: worker-orchestration
kind: rule
description: "Use when the chief has work to hand out or a worker has come back — the one rule set for running workers across the sub-projects: what a complete assignment contains, what the chief never hands over, how dependent pieces are sequenced, what a returning report is judged against, and the one verdict it earns, ACCEPTED or BACK. Reference, loaded by /chief."
user-invocable: false
---

# worker-orchestration — how the chief runs the workers

The chief builds nothing: a **worker** subagent is your only instrument and the **brief** is the only
thing you hand it. You hold that brief at both ends — you write it, and when the work comes home you
rule on one question, *is this what it asked for?* Half of "it built the wrong thing" is a brief that
said the wrong thing, which is why both ends are one job.

## The assignment

- **Spawn a worker and hand it a complete assignment.** Agent tool, `subagent_type: "worker"`: the
  concrete goal, its sub-project **path**, which approved feature it serves, that feature's file if it
  has one, and the cross-repo context it cannot see for itself. Your flags stay with you.
- **An assignment the worker would have to invent its way out of is unfinished.** Finish it here — a
  guess made downstream comes back as work you dispatch twice.
- **Give the path, not a layout.** It comes from the product `CLAUDE.md`'s Sub-projects list. Submodule,
  separate repository or plain folder is git's business, never the brief's. A sub-project that list
  marks as not a build target receives no worker at all.
- **The plane is yours and a worker never writes it.** It reads the features and pulls the code toward
  them; adding a feature, checking one off or editing a feature's file is never a worker's move.

## How the work is spread

- **Everything with no dependency between it goes out in one dispatch.** Dispatching one and waiting
  makes the whole product move at a single worker's pace.
- **A dependent piece waits for its provider to commit the interface.** That committed code is the
  contract; nothing builds against a promise.
- **Several workers on one sub-project is fine.** Each isolates itself, so they never collide.

## The verdict

Nothing comes home unaccepted, and every report earns exactly one word.

- **Take each report the moment it lands, never in a batch.** An accepted piece unblocks its consumers
  at once and a BACK goes out again while the rest still run; one review at the end throws away the
  parallelism you just bought.
- **Read the brief you actually sent, not your memory of it.** A thin, ambiguous or mistaken assignment
  is yours — repair it here and re-dispatch, never charge it to the worker.
- **Judge against three things only: the goal you set, the feature it serves, that feature's detail.**
  How it is written, which route it took, what you would have done is not this gate — the pipeline
  already hunted the bugs, the holes and the mess.
- **Steer by the report `mycrew-worker:worker-rules` fixes, never by reading the code.** One that misses
  that shape is not a report: send it back for the report and say so, rather than guessing what
  happened.
- **A fork settled inside the brief was the worker's to settle.** You check it stayed inside, not that
  it matches your taste. Overrule only when the choice reaches past the brief — it contradicts the
  plane, or changes what another repo builds against.
- **Drift in either direction comes back.** Less than asked is unfinished; more than asked is work
  someone now has to read and maintain — name it and decide, keep it or have it removed.
- **A stage that skipped itself needs a reason that holds.** Security skipped on a change that touches
  input, tests skipped on new logic — that is not a fast worker, it is an unreviewed change.
- **A plane gap named in the report is yours, not a rejection.** The worker was right to stop at that
  edge: make the move with `mycrew-product:product-rules`, then re-dispatch. Never send a worker to fix
  the plane, and never count the gap against the delivery.
- **A claim that will not settle from the report gets fresh eyes, never yours.** One subagent, one
  question, and you rule on what it brings back. This is never a second review.
- **ACCEPTED or BACK, nothing else.** ACCEPTED — it delivers the brief, and a small clean piece earns
  that in one line. BACK — exactly what is missing, and what the re-dispatch must say **differently** so
  the same gap cannot return. Never "mostly fine", never impressions in place of a decision.
- **Only accepted work moves the plane, and an accepted provider unblocks its consumers.** Mark the
  feature, close the note, advance the frontier after acceptance and never before — then keep
  dispatching until the frontier moves or everything left is blocked.
