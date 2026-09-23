---
name: how-to-do
description: "Think through how to build something before a task is written — weigh speed, quality, reuse, and build-own as four independent angles, then settle one buildable approach, never a menu. Three depths: med reasons alone, high sends each angle to its own subagent, max has the four argue before you decide."
argument-hint: "<what needs an approach> --depth med|high|max"
---

# how-to-do — settle the how before a task is written

Turns a fork — more than one workable way to build something, no obvious winner — into one buildable
approach. Never a menu, never a line of code. Runs at the depth the caller names.

## Step 1 — frame the fork

State in one sentence what is to be built and the decision that forks it, plus the criteria for what
"best" means here. List the project files as shared ground — `git ls-files | xargs wc -l` — before any
angle gets argued.

## Step 2 — run the four angles, at the chosen depth

Four angles, always the same four, each its own strongest plan under its own stance:

- **Speed** — fastest to something working. Sacrifices robustness.
- **Quality** — the production version under real load. Sacrifices speed and simplicity.
- **Reuse** — existing libraries, proven patterns, the codebase's own way. Sacrifices fit.
- **Build own** — bespoke, fit-to-purpose. Sacrifices predictability.

**`med` (default)** — no subagents. Reason through all four angles yourself, one after another, on the main
thread. 

**`high`** — spawn four subagents in parallel, one per angle, each arguing only its own stance with no
knowledge of the others. Read their four plans back; you alone weigh them, on the main thread.

**`max`** — spawn the same four subagents in parallel for round one. Once all four plans are in, send
each subagent the other three plans and have it argue against them and restate its own position in
light of their counters — parallel again, all four at once. Weigh the four second-round opinions, not
the first round.

## Step 3 — synthesize one decision

On the main thread only — never delegate this part. What the angles agree on is the **robust core** and
goes in; where they genuinely disagree are the **live axes**. Score the survivors against the criteria
from step 1 and decide. Name which alternatives you beat and why.

If the direction that wins still looks wrong, stop and flag it to the human — do not write the task on
a decision you don't trust.

## Done

- **One buildable approach**, framed against the criteria, with the alternatives it beat named.
- **Never a line of code** — this settles the how; the task you write hands a coder a settled approach,
  not a fork to resolve itself.
