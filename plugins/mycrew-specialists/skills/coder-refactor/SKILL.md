---
name: coder-refactor
kind: intent
description: "Reshape working code toward the project's own code-writing rules with its behavior held exactly as it is — gated both sides, so what the code does is provably unchanged."
---

# coder-refactor — enforce the rules, preserve the behavior

The run ends with the same behavior in a better shape, proven twice over: a green net, and a
before-against-after walk that finds no divergence. Nothing outside the change moves.

- **Behavior-preserving.** A refactor never changes *what* the code does. Behavior changes only as a
  deliberate bug-fix or a product decision — never a side effect of cleanup.
- **Structural work this change warrants is inside it; tidying the repo is not.** No gold-plating.

## Start — the code must already work

You reshape **working** code only: build / boot / existing tests green / a smoke check. Evidence, not
assumption.

- **It works** → proceed.
- **It's broken** (won't build, tests red, doesn't run) → **not a refactor job**: there is nothing to
  preserve yet. Route it to review or do.
- **Nothing to reshape** — you walk the change against the project's rules and cannot name a single
  violation → skip. Laying a safety net to change nothing is pure cost.

## Map the codebase

Mechanical, so dispatch it to a subagent and work from the map it brings back:

- **List the files with line counts** — `git ls-files | xargs wc -l`. The counts point straight at the
  blobs to split.
- **Study the code** — **codegraph** if indexed, else **grep**, for modules, dependencies and call
  relationships.

## Lay the safety net

- **Get existing tests green first.** A red baseline is fixed now, before anything is touched.
- **Write characterization tests on the core logic** to pin its *current* behavior. This net is what
  lets you reshape without silently moving behavior — it is the before-half of the exit gate.
- **Just the net, never full coverage.**

## Refactor to the project's rules

- **Find the rules before you reshape anything.** They are the project's own, collected the way
  `CLAUDE.md` is: where the code sits, then each folder up to the product root, and the ones installed
  for every project. Nothing is listed here — a fixed list would be a second, staler copy of them.
- **Walk the code against every rule you found and fix each violation in place.** A rule you cannot
  point at a violation of is one this code already satisfies; move on rather than inventing work.
- **Use the `code-simplifier` agent as your eyes** for clarity, dead code, naming and nesting.
- **Structural moves are fine when this change warrants them** — split or move a function, move a file
  — with the reason rooted in the work, never in "tidy the repo".
- **The net stays green after every step.** That green is your running proof the behavior didn't move.

## Exit gate — before against after

- **The net is green** — every characterization test still passes on the new shape.
- **The logic is identical** — same inputs → same outputs, same side effects, same order of external
  calls. Only *how* it is written moved.
- **Any divergence means you changed behavior, not structure.** Revert that step and redo it
  behavior-preserving: a refactor that alters what the code does is a failed refactor, not a bug-fix.
