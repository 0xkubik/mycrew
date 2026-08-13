---
name: product-view
description: "Use whenever the product view is written to or changed — the one rule set behind docs/product/: features.md (what the product must do, one line each and nothing beneath), features/F00N-<slug>.md (the full picture of a feature whose line can't carry it, in the human's own words), notes.md (work no feature covers), decisions.md (what was settled about the product and why). Holds the line against the technical view in docs/design/, the routing that says where a thing goes, the rules each file obeys, and the templates each file is. Rules only: what an entry must be, never how one is gathered or by whom."
user-invocable: false
---

# product-view — what the product is

`docs/product/` holds **what the product is** — written down at the product root and pulled toward by
the code in every sub-project. Three files, no more, each with its own permanent id space:

| File | Holds | Ids |
| --- | --- | --- |
| `docs/product/features.md` | what the product must do — one line each, nothing more | `F001` |
| `docs/product/features/F00N-<slug>.md` | the full picture of one feature, when its line can't carry it | its feature's |
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
- **Detail that capability's one line can't carry** — mechanics, a contract, a bound, a state, an
  edge case → **that feature's own file**, never nested under its line in the list.
- **A closed choice about the product, with a reason** — a rule, a constraint, a way of existing that
  belongs to no single feature and will still bind in a year → a decision.
- **A closed choice about the machinery** — a language, a store, a library, a thing deliberately not
  used → **out of here**, into `docs/design/decisions.md`.
- **Work someone has to do** — a fix, a rework, something still to be thought through → a note.
- **Anything nobody has to obey or act on** → nowhere. A conversation is not a transcript to be minuted.

## Features — `docs/product/features.md`
- **A feature is what you'd name telling someone what the product does.** Someone can do something,
  or the product offers something. How that capability *behaves* — its states, limits, rules, the
  smaller actions inside it — is **detail**, and detail belongs in that feature's file, never in a
  line of its own.
- **Two tests, both quick.** Would you mention it when *telling* someone what the product does, or
  only while *explaining* something you already mentioned? And does it exist at all without another
  feature? Named only in the explanation **and** dead without its parent → it is that parent's
  detail. **No parent at all → it is a feature, however small.**
- **The list is not a backlog.** Cutting a capability into the steps it takes to build turns the
  plane into a task board and kills the one thing it is for — being read at a glance. Breaking a
  feature into work is the chief's job at dispatch, not this file's.
- **One line, one feature, and nothing beneath it.** `- [ ] F001 — <feature>`: one crisp line of ≤200
  chars in the user's intent, not your embellishment, with `[ ]` not built yet and `[x]` built. A
  point, a sub-bullet or a paragraph under a line is exactly what this shape exists to stop — the
  list stays one screen you can read at a glance, however big the product gets.
- **More than the line holds → the feature's own file.** Never a longer line and never a nested
  point: open `docs/product/features/F00N-<slug>.md` and end the line with ` → features/F00N-<slug>.md`
  so a reader knows it exists. One file per feature, never one file covering two.
- **Accumulate or edit, never delete.** The list is declarative — the product's desired state. A built
  feature is marked `[x]`, never removed; the list only grows.

## A feature's detail — `docs/product/features/F00N-<slug>.md`
- **Only when the line genuinely can't carry it.** Most features never earn a file. One is opened
  because there is a real picture to hold — mechanics, states, edge cases, what it must never do —
  not to have somewhere to write.
- **Their words, not your prose.** You record and order what the human said; you never rewrite it
  into your own register, and nothing they didn't affirm goes in.
- **It binds.** The chief decomposes against it, a worker builds to it, and a worker never writes to
  it. A file nobody has to obey is a file nobody should have written.
- **One feature per file, and only that feature.** Detail that belongs to a second capability is a
  second feature with its own line.
- **What binds wider leaves.** A rule holding beyond this feature → `decisions.md`; a technical
  choice → `docs/design/decisions.md`; work someone must do → `notes.md`; the system's shape →
  `model.c4`. The file holds the picture, never orders hidden in prose.
- **Contradiction is named, never swallowed.** What it says conflicts with the feature's line, a
  decision, or the shape → say so plainly and have it settled; never keep two truths in the plane.
- **A couple of screens is the ceiling.** Past it, this is two features, or half of it belongs in one
  of the files above.

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

## All of them
- **An entry is capped: a feature is one line of ≤200 chars, a note or a decision ≤300 — heading and
  points together.** Ids, boxes and bullet marks don't count. What will not fit is **two entries**,
  never one written longer: a feature too big to state in a line is two features, a decision carrying
  two choices is two decisions. Detail is not what the cap forbids — it has its own file; sprawl in
  the list is. An entry over the cap is not detailed, it is unfinished thinking.
- **Ids are permanent.** `F`, `N` or `P` and a zero-padded three-digit number, running in order from
  the highest that letter has already taken. **Never reused and never renumbered** once given —
  everything else points at an entry by its id. A gap in the numbering is a retired entry, never a
  free number.
- **A plane file carries its entries and nothing else.** No header block, no note explaining what
  the file is for, no restatement of these rules inside it. That is written **here**, once — copied
  into every file it becomes pages of duplicated prose nobody reads and everybody has to scroll
  past. Check what you are about to write against these rules *before* writing it: an entry that
  doesn't answer what the file holds belongs in another file.
- **Strictly the template shape.** Each file is the `example.features.md`, `example.feature.md`,
  `example.notes.md` or `example.decisions.md` shape shipped beside this skill — a title and its
  entries, nothing else.
- **Reference data goes to `docs/product/appendix/`.** A catalogue that would swamp a feature file —
  a list of categories, a table of values, anything that keeps growing — stands there as its own
  file, and the feature points at it. It is data the plane refers to, not a plane file: no ids, no
  entries, no rules of its own.
- **English.** Headings, prose, identifiers — all English.
