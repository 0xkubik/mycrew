---
name: feature-management
description: "Use whenever the product's feature list or its working notes are written to or changed — the rules both obey: one features file and one notes file at the product root, permanent F000 and N000 ids, a feature headed by one ≤200-char line in the user's own intent and carrying beneath it only the short points that line can't hold, accumulate and mark built but never delete. Rules only: what an entry must be, never how one is gathered or by whom."
user-invocable: false
---

# feature-management — the rules the product's feature list obeys

**Features — `docs/features.md`**
- **One list, at the product root.** There is a single features file for the whole product —
  `docs/features.md` beside the root `CLAUDE.md`. Sub-projects keep no features of their own; the
  chief decomposes a product feature into per-repo assignments, not into a second list. The North
  Star lives in the root `CLAUDE.md`; what is settled but is no capability lives in `docs/decisions.md`,
  by `mycrew-chief:decision-management`.
- **Every feature carries a permanent id.** Each entry heads with `F` and a zero-padded three-digit
  number — `## [ ] F000 — <feature>`. Ids run in order from the highest already taken, and are
  **never reused and never renumbered** once given: everything else points at features by id.
- **The heading is the feature, in ≤200 chars.** One crisp line in the user's intent — not your
  embellishment — with `[ ]` not built yet and `[x]` built (the id and the box don't count).
- **Beneath it, only what the line can't carry.** Short `-` points, one thought each: a constraint to
  hold to, a wish about how it's implemented, a piece of data the line has no room for — a contract, a
  shape, a limit, a state, an edge case, what counts as done. Never a restatement of the heading,
  never how the code is organized (that's the repo's), never the system's shape (that's `model.c4`),
  never why a choice was made (that's `docs/decisions.md`).
- **Keep it thin — at most ten points, one line each.** A feature needing more is two features. A
  paragraph under a heading is a feature written wrong.
- **Accumulate or edit, never delete.** The features list is declarative — the product's desired
  state. A built feature is marked `[x]`, never removed; the list only grows.
- **Strictly the template shape.** The whole file *is* the `example.features.md` template shipped
  beside this skill — nothing else.

**Notes — `docs/notes.md`**
- **Notes hold work still to be done.** Fixes, tweaks, reworks and raw ideas still to be thought
  through go to `docs/notes.md` beside the features, by the `example.notes.md` template — never onto
  the features list. A conclusion nobody has to act on is not a note.
- **One line, one note, one id.** `- [ ] N000 — <what to do or what breaks, and where>`. The `N`-id is
  how a note is pointed at, and it is never reused.
- **Notes are scratch.** A settled note either graduates into a feature or is cleaned out; unlike a
  feature, a done note does not stay.

**Both**
- **English.** Headings, prose, identifiers — all English.
