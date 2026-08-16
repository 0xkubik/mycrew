---
name: refactor
kind: intent
description: "Use when working code needs reshaping toward the project's own code-writing rules with its behavior held exactly as it is — gated both sides, so what the code does is provably unchanged. Triggers: \"refactor this\", \"clean up\", \"tidy the structure\"."
argument-hint: "[what to refactor — omit for the last change]"
---

# refactor — enforce the rules, preserve the behavior

You take working code and reshape it to obey **the code-writing rules the project holds** — **without
changing what it does**. You APPLY every change yourself. A gate proves the code works before you start; a gate proves
the logic is unchanged before you finish.

**Invariants — non-negotiable:**
- **Behavior-preserving.** A refactor never changes *what* the code does. Behavior changes only as a
  deliberate bug-fix or a product decision — never a side effect of cleanup.
- **Bounded to the change.** Your remit is what you were handed, plus structural work *this* change
  genuinely warrants. Not "improve the whole repo." No gold-plating.
- **Apply, don't report.** You make every fix yourself; a findings list handed up is a failure.
- **3 strikes on one problem → `mycrew-tools:slap`, then pick the fresh approach yourself.**

---

## Gate — the code must already work

You reshape **working** code only. Confirm it runs before you touch it — build / boot / existing tests
green / a smoke check. Evidence, not assumption.

- **It works** → proceed.
- **It's broken** (won't build, tests red, doesn't run) → **not a refactor job.** A refactor has
  nothing to preserve yet — route it to `review` or `do`.
- **Nothing to reshape** — you walk the change against the project's rules and cannot name a single
  violation → say so in **one line** and skip. Laying a safety net to change nothing is pure cost.

---

## Map the codebase

See where the code sits before you touch it — you reshape well, and spot reuse, only once you can
place it. Mechanical, so **dispatch it to a subagent on the `haiku` model** and work from its map:

- **List the files with line counts** — `git ls-files | xargs wc -l`. The counts point straight at
  the blobs to split.
- **Study the code** — **codegraph** if indexed (else **grep**) for modules, dependencies, call
  relationships.

---

## Lay the safety net

- **Get existing tests green** (whatever's there). A red baseline is fixed *now*, before touching anything.
- **Write characterization tests on the core logic** to pin its *current* behavior. This net is what
  lets you reshape without silently moving behavior — it is the before-half of the exit gate.
- Not full coverage — just the net.

---

## Refactor to the project's rules

- **Find the rules before you reshape anything.** They are the project's own, collected the way
  `CLAUDE.md` is: where the code sits, then each folder up to the product root, and the ones installed
  for every project. Nothing is listed here — a fixed list would be a second, staler copy of them.
- **Walk the code against every rule you found and fix each violation in place.** A rule you cannot
  point at a violation of is one this code already satisfies; move on rather than inventing work.
- **Use `/simplify` and the `code-simplifier` agent as your eyes** for clarity, dead code, naming and
  nesting.
- **Structural moves are fine when this change warrants them** — split or move a function, move a file
  — with the reason rooted in the work, never in "tidy the repo".
- **The net stays green after every step.** That green is your running proof the behavior didn't move.

---

## Gate — before vs after: the logic is unchanged

Before you close, prove the reshape was behavior-preserving:

- **The net is green** — every characterization test still passes on the new shape.
- **Compare before ↔ after** — walk the change and confirm the *logic* is identical: same inputs →
  same outputs, same side effects, same order of external calls. Only *how* it's written moved.
- **Any divergence** = you changed behavior, not just structure. **Revert that step and redo it
  behavior-preserving** — a refactor that alters what the code does is a failed refactor, not a bug-fix.