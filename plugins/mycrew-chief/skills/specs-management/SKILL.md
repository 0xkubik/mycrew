---
name: specs-management
description: "Use whenever the product plane is written to or changed — the one rule set behind its three files at the product root: features.md (what the product must do), notes.md (work no feature covers), decisions.md (what was settled and why). Holds the routing that says which of the three a thing belongs in, the rules each obeys, and the templates each file is. Rules only: what an entry must be, never how one is gathered or by whom."
user-invocable: false
---

# specs-management — the product plane's three files

The plane is what the product must be, written down at the **product root** and pulled toward by the
code in every sub-project. It is three files, no more, each with its own permanent id space:

| File | Holds | Ids |
| --- | --- | --- |
| `docs/features.md` | what the product must do | `F001` |
| `docs/notes.md` | work to do that no feature covers | `N001` |
| `docs/decisions.md` | what was settled, and why | `D001` |

Sub-projects keep no plane of their own — never a second list, and never one inside a sub-project's
repo. The North Star lives in the root `CLAUDE.md`, and the system's shape in
`docs/architecture/model.c4` by `mycrew-chief:architecture-management` — not here.

## Routing — which of the three
- **A capability the product must have** → a feature.
- **Detail that capability's one line can't carry** — a contract, a bound, a state, an edge case → a
  point *under that feature*, never a file of its own.
- **A choice that is closed, with a reason** — a rule, a constraint, a stack, a way of existing that
  belongs to no single feature and will still bind in a year → a decision.
- **Work someone has to do** — a fix, a rework, something still to be thought through → a note.
- **Anything nobody has to obey or act on** → nowhere. A conversation is not a transcript to be minuted.

## Features — `docs/features.md`
- **The heading is the feature, in ≤200 chars.** `## [ ] F001 — <feature>`: one crisp line in the
  user's intent, not your embellishment, with `[ ]` not built yet and `[x]` built.
- **Beneath it, only what the line can't carry.** Short `-` points, one thought each: a constraint to
  hold to, a wish about how it's implemented, a contract, a shape, a limit, a state, an edge case,
  what counts as done. Never a restatement of the heading, never how the code is organized (that's
  the repo's), never the system's shape, never why a choice was made (that's a decision).
- **Keep it thin — at most ten points, one line each.** A feature needing more is two features. A
  paragraph under a heading is a feature written wrong.
- **Accumulate or edit, never delete.** The list is declarative — the product's desired state. A built
  feature is marked `[x]`, never removed; the list only grows.

## Notes — `docs/notes.md`
- **One line, one note.** `- [ ] N001 — <what to do or what breaks, and where>`.
- **Only work someone has to do.** A conclusion nobody has to act on is not a note, and neither is a
  question parked for later.
- **Notes are scratch.** A settled note either graduates into a feature or is cleaned out; unlike a
  feature, a done note does not stay.

## Decisions — `docs/decisions.md`
- **The heading is the decision itself.** One line naming what was chosen and — where there was a real
  alternative — what it was chosen over: `## D004 — The job queue is a Postgres table, not Redis`. A
  heading that names a topic instead of a choice is a decision not yet made.
- **Beneath it, only the reasoning and its ceiling.** Short `-` points: why this won, what it was
  weighed against and what that would have cost, the known limit where it stops working, what would
  overturn it. A paragraph under a heading is a decision written wrong.
- **Name the feature only when the decision serves one.** Its heading then ends `(F004)`. Most
  decisions serve the whole product and name none.
- **Superseded, never deleted.** A decision that no longer holds stays, its heading marked
  `— superseded by D0NN`, and the choice replacing it is a new entry with a new id.

## All three
- **Ids are permanent.** `F`, `N` or `D` and a zero-padded three-digit number, running in order from
  the highest that letter has already taken. **Never reused and never renumbered** once given —
  everything else points at an entry by its id.
- **Strictly the template shape.** Each file *is* the `example.features.md`, `example.notes.md` or
  `example.decisions.md` template shipped beside this skill — nothing else.
- **English.** Headings, prose, identifiers — all English.
