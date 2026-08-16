---
name: product-rules
kind: rule
description: "Use whenever an idea the human affirmed must be written into the product plane — the one rule set for writing it down, whatever conversation it came out of. Draws the cut between a feature and the detail that belongs to it, then routes each: features.md (the index — a name per feature and nothing else), features/F00N-<slug>.md (what that feature actually is, when it has something to say), notes.md (work no feature covers, in the same index shape). The routing and the rules each file obeys, hardcoded here; the shapes to fill in sit in templates.md beside it. Rules only: what an entry must be, never how one is gathered or by whom."
user-invocable: false
---

# product-rules — what the product plane holds, and where each thing goes

`docs/product/` holds **what the product is**, written at the product root and pulled toward by the code
in every sub-project: `features.md` names each feature, `features/F00N-<slug>.md` says what one is once
it has more to say than its name, `notes.md` carries work no feature covers. Sub-projects keep no plane
of their own, and the North Star lives in the root `CLAUDE.md`.

## When a thing gets written

- **Affirmed → filed, in that turn.** Whatever session or command settled it: never batched at the end,
  never left for the next run. An affirmed idea nobody wrote down did not happen.
- **Only what they affirmed, in their intent.** Never your reconstruction, never a thought they were
  still turning over. Said in passing and clearly unsettled → a note, not a feature.
- **Anything nobody has to obey or act on goes nowhere.** A conversation is not a transcript to minute.

## Feature or detail — the cut everything rests on

- **A feature is one thing the product gives a person; the list of them is flat.** Whatever varies it,
  completes it, states it or makes it work is its **detail** — in that feature's file, never a line.
- **Four shapes are always detail.** A **variant** (another way to the same thing), a **part** (a piece
  of something already given), a **state** (before or after something happened), a **mechanic** (how).
- **Hunt the parent before opening a line.** Name which entry this would vary, complete, state or serve;
  found → it goes in that entry's file. A new line is what is left when the hunt comes back empty.
- **Two tests settle it.** What does the person end up holding — two entries leaving them the same thing
  are one feature. Would they still ask for it while the parent works perfectly — no → it is detail.
- **Never merge to shorten the list.** Two things asked for separately stay two entries however close
  they sit; the list is short because the product is named well, not because entries were swept together.

## Every entry, and the list it sits in

- **A name of ≤5 words and nothing else.** No gloss, clause, parenthesis or link, nothing beneath the
  line, never a sentence — `Realtime Sync`, `Offline Vault`. What will not fit is **two entries**.
- **Ids are permanent.** `F` or `N` plus zero-padded three digits, running on from the highest that letter
  has taken; never reused, never renumbered. A gap is a retired entry, not a free number.
- **One home, named by id everywhere else.** Detail touching several features is written in the one file
  it belongs to. The same thing said twice is two truths, and one starts rotting immediately.
- **A plane file carries its entries and nothing else** — no header block, no note explaining the file,
  no restatement of these rules. The shapes to fill in are `templates.md`, beside this file.
- **The list is not a backlog.** A capability cut into build steps turns the plane into a task board;
  breaking a feature into work is the chief's job at dispatch.
- **Accumulate, fold, never abandon.** Built is marked `[x]` and never removed; a line that turns out to
  be detail folds into its parent's file, its id retired. A permanent id never justifies a wrong line.

## The feature's own file

- **A file is opened when the feature has something to say** — behaviour nobody would guess, a bound, an
  edge, a promise, anything the human settled. Never one that only restates the name above it.
- **This is where the feature is said.** How it works, what it promises, its states, its edges, what it
  must never do. A reader who knows nothing comes out of it knowing the feature.
- **No template — write to the feature.** Prose, a list, a table, a walk through one path, whatever it
  needs. Only the title is fixed.
- **Their words, not your prose.** You record and order what the human said; nothing they didn't affirm
  goes in.
- **It binds.** The chief decomposes against it and a worker builds to it; a worker never writes to it.
- **Work someone must do leaves for `notes.md`.** The file holds the picture, never orders hidden in prose.
- **Contradiction is named, never swallowed.** What it says conflicts with the feature's line → say so
  and have it settled; the plane never carries two truths.
- **A couple of screens is the ceiling.** Past it this was two features — cut at the second thing the
  product gives a person, never at a convenient heading.

## Notes

- **Only work someone has to do.** Not a conclusion nobody acts on, not a question parked for later. A
  note opens no file: what won't fit in its name is a note nobody has thought through yet.
- **Notes are scratch.** A settled one graduates into a feature or is cleaned out; a done note does not
  stay.
