---
name: accept-work
description: "Use when a worker comes back and its work must be taken or sent back — the chief's acceptance gate. Reads the assignment as it was issued against the report that came back and rules on one thing: did this deliver what was asked. Returns ONE verdict, ACCEPTED or BACK with exactly what is missing and what the re-dispatch must say differently. Only accepted work moves the plane. Triggers: \"accept this\", \"is this done\", \"did the worker do what I asked\"."
argument-hint: "<the assignment you issued + the report that came back>"
---

# accept-work — take it, or send it back

A worker has finished and reported. You hold the two things nobody else holds together: **the brief
you sent** and **the answer that came back**. Put them side by side and rule on one question — *is
this what was asked for?* You judge the delivery, never the craft: the pipeline already hunted the
bugs, the holes and the mess.

## Rules & concepts — non-negotiable

- **Read the brief you actually sent, not your memory of it.** Half of "it built the wrong thing" is a
  brief that said the wrong thing. A thin, ambiguous or mistaken assignment is **yours** — repair it
  here and re-dispatch; never charge it to the worker.
- **Judge against three things only:** the goal you set, the feature it serves, and the parts of the
  design it had to build to. Anything else — how it is written, which route it took, what you would
  have done — is not this gate.
- **The report is your evidence, and it has a fixed shape.** *Done · Forks I settled · Tools · Left
  outside.* A report that doesn't answer those isn't a report — send it back for **the report**, and
  say so, rather than guessing what happened or going to read the code.
- **A fork settled inside the brief was the worker's to settle.** You check it stayed inside, not that
  it matches your taste. Overrule only when the choice reaches past the brief — it contradicts a
  decision, moves the design, or changes what another repo builds against.
- **Drift both ways comes back.** Less than asked is unfinished. More than asked is unrequested work
  someone now has to read and maintain — name it and decide: keep it or have it removed.
- **A design gap in "Left outside" is yours, not a rejection.** The worker did the right thing by
  stopping at that edge. Move the plane, then re-dispatch — the gap never counts against the delivery.
- **When a claim that matters can't be settled from the report, send eyes — not yourself.** Dispatch a
  fresh subagent to check that **one** claim against the result, and rule on what it brings back. You
  still never read the code, and this is never a second review: one question, not a sweep.
- **One verdict, nothing else.** **ACCEPTED** — it delivers the brief; say it in a line and move on.
  **BACK** — name exactly what is missing or wrong, and what the re-dispatch must say **differently**
  so the same gap can't come back. Never "mostly fine", never a list of impressions in place of a
  decision.
- **Only accepted work moves the plane.** A feature is marked `[x]`, a note closed, the frontier
  advanced **after** acceptance and never before. Work that was never accepted is not done, however
  green the report reads.
- **Cheap when it should be cheap.** A small piece with a clean report that plainly matches the brief
  → **ACCEPTED** in one line. A gate that taxes every delivery is a gate that stops being used.
