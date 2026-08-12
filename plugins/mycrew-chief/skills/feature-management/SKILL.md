---
name: feature-management
description: "Use whenever the product's feature list is written to or changed — the rules every entry obeys: one list at the product root, a permanent three-digit id the specs point at, ≤200 chars in the user's own intent, accumulate and mark built but never delete, strictly the shipped template shape, and the notes file beside it for what isn't a feature yet. Rules only: what an entry must be, never how one is gathered or by whom."
---

# feature-management — the rules the product's feature list obeys

**Rules**
- **Every feature carries a permanent id.** Each line opens with a zero-padded three-digit id —
  `- [ ] 000 - <feature>`. Ids run in order from the highest already taken, are **never reused and never
  renumbered** once given: the specs point at features by id.
- **≤200 chars per feature.** Compress each affirmed feature to one crisp line of **at most 200
  characters** (the id doesn't count), in the user's intent — not your embellishment.
- **One list, at the product root.** There is a single features list for the whole product —
  `docs/features/features.md` beside the root `CLAUDE.md`. Sub-projects keep no features of their own;
  the chief decomposes a product feature into per-repo assignments, not into a second list. You touch
  only this file. The North Star lives in the root `CLAUDE.md`; specs are others'.
- **Accumulate or edit, never delete.** The features list is declarative — the product's desired state. A
  built feature is marked `[x]`, never removed; the list only grows.
- **Strictly the template shape.** The whole file *is* the `example.features.md` template shipped
  beside this skill — nothing else.
- **Notes hold what isn't a feature yet.** Fixes, tweaks, reworks and raw ideas still to be thought
  through go to `docs/features/notes.md`, by the `example.notes.md` template — never onto the features
  list. Notes are scratch: one thought a line, and a settled one either graduates into a feature or is
  cleaned out.
