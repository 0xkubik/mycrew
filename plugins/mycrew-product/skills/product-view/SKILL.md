---
name: product-view
description: "Use whenever the product view is written to or changed — the one rule set behind the three files in docs/product/: features.md (what the product must do), notes.md (work no feature covers), decisions.md (what was settled about the product and why). Holds the line against the technical view in docs/design/, the routing that says where a thing goes, the rules each file obeys, and the templates each file is. Rules only: what an entry must be, never how one is gathered or by whom."
user-invocable: false
---

# product-view — what the product is

`docs/product/` holds **what the product is** — written down at the product root and pulled toward by
the code in every sub-project. Three files, no more, each with its own permanent id space:

| File | Holds | Ids |
| --- | --- | --- |
| `docs/product/features.md` | what the product must do | `F001` |
| `docs/product/notes.md` | work to do that no feature covers | `N001` |
| `docs/product/decisions.md` | what was settled about the product, and why | `P001` |

**Never what it is built on.** That is the **design view** — `docs/design/` by
`mycrew-product:design-view`: the shape in `model.c4` and the technical choices in `decisions.md`.
**The line between them:** a product decision is one a person outside could notice — what the product
does, offers, forbids or charges for. A technical decision is about the machinery — the language, the
store, the protocol, the library — and nobody reading the product would ever see it.

Sub-projects keep no plane of their own — never a second list, and never one inside a sub-project's
repo. The North Star lives in the root `CLAUDE.md`.

## Routing — where a thing goes
- **A capability the product must have** → a feature.
- **Detail that capability's one line can't carry** — a contract, a bound, a state, an edge case → a
  point *under that feature*, never a file of its own.
- **A closed choice about the product, with a reason** — a rule, a constraint, a way of existing that
  belongs to no single feature and will still bind in a year → a decision.
- **A closed choice about the machinery** — a language, a store, a library, a thing deliberately not
  used → **out of here**, into `docs/design/decisions.md`.
- **Work someone has to do** — a fix, a rework, something still to be thought through → a note.
- **Anything nobody has to obey or act on** → nowhere. A conversation is not a transcript to be minuted.

## Features — `docs/product/features.md`
- **The heading is the feature, in ≤200 chars.** `## [ ] F001 — <feature>`: one crisp line in the
  user's intent, not your embellishment, with `[ ]` not built yet and `[x]` built.
- **Beneath it, only what the line can't carry.** Short `-` points, one thought each: a constraint to
  hold to, a wish about how it's implemented, a contract, a shape, a limit, a state, an edge case,
  what counts as done. Never a restatement of the heading, never how the code is organized (that's
  the repo's), never the system's shape, never why a choice was made (that's a decision).
- **A paragraph under a heading is a feature written wrong.** One thought a point, one line a point.
- **Accumulate or edit, never delete.** The list is declarative — the product's desired state. A built
  feature is marked `[x]`, never removed; the list only grows.

## Notes — `docs/product/notes.md`
- **One line, one note.** `- [ ] N001 — <what to do or what breaks, and where>`.
- **Only work someone has to do.** A conclusion nobody has to act on is not a note, and neither is a
  question parked for later.
- **Notes are scratch.** A settled note either graduates into a feature or is cleaned out; unlike a
  feature, a done note does not stay.

## Decisions — `docs/product/decisions.md`
- **The heading is the decision itself.** One line naming what was chosen and — where there was a real
  alternative — what it was chosen over: `## P004 — Reading is free and needs no account, ever`. A
  heading that names a topic instead of a choice is a decision not yet made.
- **Beneath it, only the reasoning and its ceiling.** Short `-` points: why this won, what it was
  weighed against and what that would have cost, the known limit where it stops working, what would
  overturn it. Cut the retelling first — the reasoning is the point, not the story around it. A
  paragraph under a heading is a decision written wrong.
- **The product only, never the machinery.** A stack, a store, a protocol, a library, a way of running
  it — that is a **technical** decision and belongs in `docs/design/decisions.md`. If nobody
  outside could ever notice the choice, it does not go here.
- **Name the feature only when the decision serves one.** Its heading then ends `(F004)`. Most
  decisions serve the whole product and name none.
- **Superseded, never deleted.** A decision that no longer holds stays, its heading marked
  `— superseded by P0NN`, and the choice replacing it is a new entry with a new id.

## All three
- **An entry is ≤300 chars — the heading and every point under it together.** Ids, boxes and bullet
  marks don't count; a feature's heading alone stays within its own ≤200. What will not fit is **two
  entries**, never one written longer: a feature too big to state is two features, a decision carrying
  two choices is two decisions. This is the cap that keeps the plane readable at a glance — an entry
  over it is not detailed, it is unfinished thinking.
- **Ids are permanent.** `F`, `N` or `P` and a zero-padded three-digit number, running in order from
  the highest that letter has already taken. **Never reused and never renumbered** once given —
  everything else points at an entry by its id.
- **Read the file's own header before you write to it.** Each file opens with a block saying what it
  is for, what belongs in it, what does not and where that goes instead. Check the entry you are
  about to write against it *first*: if the entry doesn't answer what the file is for, it belongs in
  another file, and writing it here is the mistake that block exists to stop.
- **Strictly the template shape, header included.** Each file *is* the `example.features.md`,
  `example.notes.md` or `example.decisions.md` template shipped beside this skill — nothing else. A
  file missing its header block is seeded from the template before anything is written to it.
- **English.** Headings, prose, identifiers — all English.
