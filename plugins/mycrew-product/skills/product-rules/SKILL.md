---
name: product-rules
kind: rule
description: "Use whenever an idea the human affirmed must be written into the product plane — the one rule set for writing it down, whatever conversation it came out of. Draws the cut between a feature and the detail that belongs to it, then routes each: features.md (the index — a name per feature and nothing else), features/F00N-<slug>.md (what that feature actually is, when it has something to say), notes.md (work no feature covers, in the same index shape). The routing and the rules each file obeys, hardcoded here; the shapes to fill in sit in templates.md beside it. Rules only: what an entry must be, never how one is gathered or by whom."
user-invocable: false
---

# product-rules — what the product plane holds, and where each thing goes

`docs/product/` holds **what the product is** — written down at the product root and pulled toward by
the code in every sub-project. Two lists, each with its own permanent id space, and a file behind a
feature that has more to say than its name:

| File | Holds | Ids |
| --- | --- | --- |
| `docs/product/features.md` | the index — a name per feature and nothing else | `F001` |
| `docs/product/features/F00N-<slug>.md` | what that feature actually is, spelled out | its feature's |
| `docs/product/notes.md` | work to do that no feature covers, in the same index shape | `N001` |

Sub-projects keep no plane of their own — never a second list, and never one inside a sub-project's
repo. The North Star lives in the root `CLAUDE.md`.

## When a thing gets written
- **Affirmed → filed, in that turn.** The human settles something mid-conversation — in whatever
  session, under whatever command — and it goes in right then, never batched at the end and never
  left for the next run. An affirmed idea nobody wrote down did not happen.
- **Only what they affirmed, in their intent.** Never your reconstruction of it and never a thought
  they were still turning over. Said in passing and clearly not settled → a note, not a feature.

## Feature or detail — the cut everything else rests on
- **A feature is one thing the product gives a person.** Whatever varies it, is part of it, is a
  state of it, or makes it work is that feature's **detail**: it lives in the feature's file and
  never takes a line of its own.
- **Four shapes are always detail.** A **variant** — another way to the same thing. A **part** — a
  piece of something the product already gives. A **state** — that same thing before or after
  something happened to it. A **mechanic** — how it works. Each belongs to what it varies, completes,
  states or serves, and is written there.
- **Hunt the parent before opening a line.** Read the list and name which entry this would vary,
  complete, state or serve. One found → it goes in that entry's file. A new line is only what is left
  when that hunt comes back empty.
- **Ask what the person ends up holding.** Two entries that leave them holding the same thing are one
  feature — a post read aloud is a post read aloud, whether its author recorded it or a machine did.
- **Ask whether they would still want it.** Something they would still ask for while the parent works
  perfectly is its own feature. Something they would not is that parent's detail.
- **Never merge to shorten the list.** Two things a person asks for separately stay two entries
  however close they sit. The list is short because the product is named well, never because entries
  were swept together.
- **Two levels, never a third.** A flat list of names, and behind each the one file that says
  everything about it. A feature is never the child of another feature: anything that would be is
  that feature's detail.
- **One home, named by id everywhere else.** Detail touching several features is written in the one
  file it belongs to; the others point at it by id. The same thing said in two files is two truths,
  and one of them starts rotting immediately.

## Routing — where a thing goes
- **A thing the product gives a person** → a feature.
- **Whatever varies, completes, states or serves that thing** → that feature's file.
- **Work someone has to do** — a fix, a rework, something still to be thought through → a note.
- **Anything nobody has to obey or act on** → nowhere. A conversation is not a transcript to be minuted.

## Features — `docs/product/features.md`
- **The list is not a backlog.** Cutting a capability into the steps it takes to build turns the
  plane into a task board and kills the one thing it is for — being read at a glance. Breaking a
  feature into work is the chief's job at dispatch, not this file's.
- **The name is the whole entry.** `- [ ] F001 — <Name>`, with `[ ]` not built yet and `[x]` built.
  The name is the product's own term for the capability, the crisp one you'd print on a feature page
  — `Realtime Sync`, `Offline Vault`, `Trust Graph` — **≤5 words**, never a sentence and never a
  verb phrase. **No description of any kind**: no gloss, no clause, no parenthesis, no link. Saying
  what it is is the feature file's job, and a line that starts explaining is the list turning back
  into prose.
- **Nothing beneath a line, ever.** A point, a sub-bullet or a paragraph under an entry is exactly
  what this shape exists to stop — the list stays one screen you can read at a glance, however big
  the product gets. Everything that would go there goes in the feature's file.
- **Accumulate, fold, never abandon.** The list is declarative — the product's desired state. A built
  feature is marked `[x]`, never removed. A line that turns out to be detail is folded into its
  parent's file and its id retired, the gap standing as the record. What is never done is leaving a
  wrong line up because its id is permanent.

## The feature itself — `docs/product/features/F00N-<slug>.md`
- **A file is opened when the feature has something to say.** Behaviour nobody would guess, a bound,
  an edge, a promise, anything the human settled about it — that earns a file. A capability its own
  name already explains whole opens none, and its line stands alone until there is something to put
  there. Never a file that only restates the name above it.
- **This is where the feature is said.** The list only names it; here you write what it concretely
  is — how it works, what it promises, its states, its edges, what it must never do. A reader who
  knows nothing should come out of this file knowing the feature.
- **No template — write to the feature.** There is no shape to fill in, no headings to match, no
  sections to leave empty. Every feature is a different thing and its file is however it needs to
  read: prose, a list, a table, a walk through one path. Only the title is fixed.
- **Their words, not your prose.** You record and order what the human said; you never rewrite it
  into your own register, and nothing they didn't affirm goes in.
- **It binds.** The chief decomposes against it, a worker builds to it, and a worker never writes to
  it. A file nobody has to obey is a file nobody should have written.
- **One feature per file, and only that feature.** Detail that belongs to a second capability is
  written in that capability's file, never a second time here.
- **What binds wider leaves.** Work someone must do → `notes.md`. The file holds the picture, never
  orders hidden in prose.
- **Contradiction is named, never swallowed.** What it says conflicts with the feature's line → say so
  plainly and have it settled; never keep two truths in the plane.
- **A couple of screens is the ceiling.** Past it, this was two features all along — cut it at the
  second thing the product gives a person, never at a convenient heading.

## Notes — `docs/product/notes.md`
- **The same shape as a feature.** `- [ ] N001 — <Name>` — a ≤5-word name for the thing to do, and
  nothing after it. One list shape across the plane, so either file reads at a glance. Unlike a
  feature, a note opens no file: what won't fit in its name is a note nobody has thought through yet.
- **Only work someone has to do.** A conclusion nobody has to act on is not a note, and neither is a
  question parked for later.
- **Notes are scratch.** A settled note either graduates into a feature or is cleaned out; unlike a
  feature, a done note does not stay.

## All of them
- **Every entry is a name of ≤5 words and nothing else, feature and note alike.** Ids, boxes and
  bullet marks don't count. What will not fit is **two entries**, never one written longer: a
  capability too big to name is two capabilities. Detail is not what the cap forbids — a feature has
  its own file for it; sprawl in the list is. An entry over the cap is not detailed, it is
  unfinished thinking.
- **Ids are permanent.** `F` or `N` and a zero-padded three-digit number, running in order from
  the highest that letter has already taken. **Never reused and never renumbered** once given —
  everything else points at an entry by its id. A gap in the numbering is a retired entry, never a
  free number.
- **A plane file carries its entries and nothing else.** No header block, no note explaining what
  the file is for, no restatement of these rules inside it. That is written **here**, once — copied
  into every file it becomes pages of duplicated prose nobody reads and everybody has to scroll
  past. Check what you are about to write against these rules *before* writing it: an entry that
  doesn't answer what the file holds belongs in another file.
- **Strictly the shapes in `templates.md`, beside this file.** Both list files are the one shape
  written there — a title and its entries, nothing else. A feature's own file has no template at all.
