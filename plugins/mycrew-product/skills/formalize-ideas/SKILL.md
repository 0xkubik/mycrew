---
name: formalize-ideas
description: "Use whenever an idea the human affirmed must be written into the product plane — the one rule set for formalizing it, whatever conversation it came out of. Where a thing goes: features.md (the index — a name per feature and nothing else), features/F00N-<slug>.md (what that feature actually is, spelled out in the human's own words, to no template), notes.md (work no feature covers, in the same index shape). The routing, the rules each file obeys, and the two templates, hardcoded here. Rules only: what an entry must be, never how one is gathered or by whom."
user-invocable: false
---

# formalize-ideas — how an affirmed idea is written down

`docs/product/` holds **what the product is** — written down at the product root and pulled toward by
the code in every sub-project. Two files, no more, each with its own permanent id space:

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

## Routing — where a thing goes
- **A capability the product must have** → a feature.
- **What that capability actually is** — mechanics, a contract, a bound, a state, an edge case →
  **that feature's own file**, never nested under its line in the list.
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
- **The name is the whole entry.** `- [ ] F001 — <Name>`, with `[ ]` not built yet and `[x]` built.
  The name is the product's own term for the capability, the crisp one you'd print on a feature page
  — `Realtime Sync`, `Offline Vault`, `Trust Graph` — **≤5 words**, never a sentence and never a
  verb phrase. **No description of any kind**: no gloss, no clause, no parenthesis, no link. Saying
  what it is is the feature file's job, and a line that starts explaining is the list turning back
  into prose.
- **What it actually is lives in its file, always.** Every feature opens
  `docs/product/features/F00N-<slug>.md` the moment its line does — the line is an index entry, and
  an index entry nobody can look up is useless. The path falls out of the id, so the line never
  carries a link to it. One file per feature, never one file covering two.
- **Nothing beneath a line, ever.** A point, a sub-bullet or a paragraph under an entry is exactly
  what this shape exists to stop — the list stays one screen you can read at a glance, however big
  the product gets. Everything that would go there goes in the feature's file.
- **Accumulate or edit, never delete.** The list is declarative — the product's desired state. A built
  feature is marked `[x]`, never removed; the list only grows.

## The feature itself — `docs/product/features/F00N-<slug>.md`
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
- **One feature per file, and only that feature.** Detail that belongs to a second capability is a
  second feature with its own line.
- **What binds wider leaves.** Work someone must do → `notes.md`. The file holds the picture, never
  orders hidden in prose.
- **Contradiction is named, never swallowed.** What it says conflicts with the feature's line → say so
  plainly and have it settled; never keep two truths in the plane.
- **A couple of screens is the ceiling.** Past it, this is two features, or half of it belongs in one
  of the files above.

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
- **Strictly the template below.** Both list files are the one shape written here — a title and its
  entries, nothing else. A feature's own file has no template at all.

## The template — one shape, both lists

`docs/product/features.md`:

```markdown
# Features — <product name>

- [ ] F001 — <Name>
- [x] F002 — <Name>
```

`docs/product/notes.md` — the same shape, its own id space:

```markdown
# Notes — <product name>

- [ ] N001 — <Name>
```

`docs/product/features/F00N-<slug>.md` — **no template**. One fixed title, then whatever the feature
needs to be understood:

```markdown
# F001 — <Name>

<what this feature concretely is, in their words, however it needs to read>
```
