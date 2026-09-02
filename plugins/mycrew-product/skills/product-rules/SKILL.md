---
name: product-rules
kind: rule
description: "Use whenever an idea the human affirmed must be written into the product plane — the one rule set for writing it down, whatever conversation it came out of. Draws the cut between a feature and the detail that belongs to it, then routes each through the backlog CLI: a milestone (the index — a name per unit of work and nothing else), a doc (what that feature actually is, when it has something to say). The routing and the rules each holds, hardcoded here; the shapes to fill in sit in templates.md beside it. Rules only: what an entry must be, never how one is gathered or by whom."
user-invocable: false
---

# product-rules — what the product plane holds, and where each thing goes

The `backlog/` at the product root holds **what the product is**, pulled toward by the code in every
sub-project: the **milestone list** names each unit of work, and a **doc** says what one is once it
has more to say than its name. Sub-projects keep no plane of their own, and the North Star lives in the
root `CLAUDE.md`. Everything here is written through the `backlog` CLI — milestone, doc, task,
decision — never by hand; the lone exception is a decision's body, which has no CLI and no structured
markers, written by `/propose-idea`.

## When a thing gets written

- **Affirmed → filed, in that turn.** Whatever session or command settled it: never batched at the end,
  never left for the next run. An affirmed idea nobody wrote down did not happen.
- **Only what they affirmed, in their intent.** Never your reconstruction, never a thought they were
  still turning over.
- **Anything nobody has to obey or act on goes nowhere.** A conversation is not a transcript to minute.

## Feature or detail — the cut everything rests on

- **A feature is one thing the product gives a person; the list of them is flat.** Whatever varies it,
  completes it, states it or makes it work is its **detail** — in that feature's doc, never a milestone
  of its own.
- **Four shapes are always detail.** A **variant** (another way to the same thing), a **part** (a piece
  of something already given), a **state** (before or after something happened), a **mechanic** (how).
- **Hunt the parent before opening a milestone.** Name which entry this would vary, complete, state or
  serve; found → it goes in that entry's doc. A new milestone is what is left when the hunt comes back
  empty.
- **Two tests settle it.** What does the person end up holding — two entries leaving them the same thing
  are one feature. Would they still ask for it while the parent works perfectly — no → it is detail.
- **Never merge to shorten the list.** Two things asked for separately stay two entries however close
  they sit; the list is short because the product is named well, not because entries were swept together.

## Every entry, and the list it sits in

- **The milestone list is the index.** A milestone is one unit of work the product tracks — a feature,
  or a cross-cutting job the plane owns ("Ops hardening", "Split the repo"). `backlog milestone add
  "<Name>"`; the list is `backlog milestone list`.
- **A name of ≤5 words and nothing else.** No gloss, clause, parenthesis or link — `Realtime Sync`,
  `Offline Vault`. What will not fit is **two milestones**.
- **The id is backlog's own `m-N`.** It is assigned in order, never reused, never renumbered — a
  removed milestone is archived, not a freed number. Everything else names the milestone by that id.
- **One home, named by id everywhere else.** Detail touching several features is written in the one doc
  it belongs to. The same thing said twice is two truths, and one starts rotting immediately.
- **The milestone list is not a task board.** A capability cut into build steps belongs in tasks, not
  milestones; breaking a feature into work is the chief's job at dispatch.
- **Accumulate, fold, never abandon.** Built work stays in the list and its completion rollup shows it
  done; a milestone that turns out to be detail is removed and its content folds into its parent's doc.
  A permanent id never justifies a wrong entry.

## The feature's own doc

- **A doc is opened when the feature has something to say** — behaviour nobody would guess, a bound, an
  edge, a promise, anything the human settled. Never one that only restates the milestone name.
- **`backlog doc create "<Name>" -t specification -p features`**, named as its milestone is named; body
  written and replaced whole with `backlog doc update <id> --content`. That shared name and
  `backlog doc list` are the join between milestone and doc; a task under the milestone links the doc
  with `--doc`.
- **This is where the feature is said.** How it works, what it promises, its states, its edges, what it
  must never do. A reader who knows nothing comes out of it knowing the feature.
- **Opening, facts, then parts.** A short opening saying what the feature is, the bullets saying what
  is true about it, a section for each part carrying a body of its own — the shape is `templates.md`.
  Never a wall of prose, and never bullets a reader meets before knowing what the feature is.
- **Their words, not your prose.** You record and order what the human said; nothing they didn't affirm
  goes in.
- **It binds.** The chief decomposes against it and a specialist builds to it; a specialist never writes to it.
- **Work someone must do leaves for the board.** The doc holds the picture, never orders hidden in prose.
- **Contradiction is named, never swallowed.** What it says conflicts with the milestone it sits under →
  say so and have it settled; the plane never carries two truths.
- **A couple of screens is the ceiling.** Past it this was two features — cut at the second thing the
  product gives a person, never at a convenient heading.
