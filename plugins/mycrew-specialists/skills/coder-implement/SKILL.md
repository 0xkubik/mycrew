---
name: coder-implement
description: "Build one concrete task end to end: decide which stages apply, settle any fork in how, fit the repo to the work, then write the code to the project's own rules."
argument-hint: "<the task to implement>"
---

# coder-implement — build one task, in the shape the project already has

The run ends with the task built and working, written the way this project writes code. Nothing else
is touched. Stages run in order; each that does not apply is skipped in stage 0.

## Step 0 — decide which stages run

Read the task and decide what it carries, then settle which stages apply. The **do** stage always
runs; **review** and **test** are separate agents — the reviewer and tester — and never part of this
run. State which stages you are running and why before step 1.

### Run the fork stage when any of these hold

- More than one materially different way to build it, no obvious winner.
- A choice between existing library and building our own / a vendored lib vs a maintained one.
- A technical decision whose cost only shows later (schema, interface, storage, concurrency model).
- Two prior approaches exist in the codebase and monotonic direction is unknown.
- The task names a concept ("just add caching") whose concrete *how* is undecided.

### Run the refactor stage when any of these hold

- A seam must be opened for the new code to land — an interface to extract, a module boundary to move.
- The intersecting code is a tangle — new code would bury itself in it.
- The new code duplicates an existing structure that should be reshaped and reused instead.
- The change violates the project's code-writing rules in the code it touches (fix before building).
- Existing tests or the build are red where the new code lands — cleared first, provably unchanged.

### Never run a stage

- **Fork** — too trivial, one obvious way: settle a one-liner with the neighbours, don't spin four
  poles.
- **Refactor** — new code fits as-is with nothing reshaped to receive it; tidying the repo is not
  refactor, it is gold-plating and never runs here.

## Step 1 — settle the fork (skip if stage 0 skipped it)

Settle the *how* into one buildable approach — never a menu, never a line of code yet. Frame the fork
in one sentence: **what is to be built** and the **decision that forks** it, plus the **criteria** for
what "best" means here. List the project files — `git ls-files | xargs wc -l` — as shared ground.

Then weigh the four poles in parallel, one per stance, each its own strongest plan under its stance:

- **Speed** — fastest to something working. Sacrifices robustness.
- **Quality** — the production version at 10× load. Sacrifices speed and simplicity.
- **Reuse** — existing libraries, proven patterns, the codebase's own way. Sacrifices fit.
- **Build own** — bespoke, fit-to-purpose. Sacrifices predictability.

Synthesize into one decision on the main thread. What the poles agree on is the **robust core** and
goes in; where they genuinely disagree are the **live axes**; score the survivors against the criteria
and decide. Say which alternatives you beat and why. If the picked direction itself looks wrong, stop
and flag to the human — do not build.

## Step 2 — fit the repo (skip if stage 0 skipped it)

Reshape the working code to receive the new work, with behavior held exactly as it is. Map the
codebase — `git ls-files | xargs wc -l`, then codegraph if indexed, else grep, for modules and
dependencies. Lay a safety net first: get existing tests green, write characterization tests on the
logic that will move. Then collect the project's own code-writing rules (where the code sits, then each
folder up to the product root) and walk the change against them, fixing each violation in place. The
net stays green after every step. Exit: net green, logic identical, no divergence.

## Step 3 — build it

Obey every code-writing rule the project holds — collected the same way: the rules where you are
working, then each folder up to the product root, then the ones installed for every project. All apply
at once; where two genuinely conflict, the nearest wins. Read them before the first line. Where no rule
speaks, the neighbours decide — naming, layout, error style, idioms — write what looks like it was
already there. Nothing is invented the task did not ask for.

## Done

- **Task built and working**, written the way the project writes code, nothing else touched.
- **Commit your work** so the reviewer can find it. Review and testing are separate agents that run
  later — the coder does not do them.
