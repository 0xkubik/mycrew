---
name: feature-management
description: "The feature-management rules — the constraints any features interview obeys: draw the user's own features out (never your own ideas), a fresh angle each question, ≤200 chars per feature, the one product features list only. Loaded by the /setup command; also invocable on its own as a reference."
argument-hint: "(reference — the rules /setup follows for features)"
---

# feature-management — the rules for drawing out features

**Rules — non-negotiable:**
- **Extract, never contribute.** You draw out *their* vision and record only what they affirm — you
  are not a source of product ideas.
- **Never your ideas.** Never propose a feature, a direction, or your own product vision. The **only**
  exception: the user explicitly asks what you'd suggest. Even question options are seeded from *their*
  words, never from a vision of your own.
- **A fresh angle every question.** Come at the product from a new side each time — who it's for, the
  job they hire it for, the pain, the moment of use, the edge user, what "great" looks like, what's
  missing, what they'd never build — adapting to what they just said. Never re-ask an angle.
- **≤200 chars per feature.** Compress each affirmed feature to one crisp line of **at most 200
  characters**, in the user's intent — not your embellishment.
- **One list, at the product root.** There is a single features list for the whole product —
  `docs/features/features.md` beside the root `CLAUDE.md`. Sub-projects keep no features of their own;
  the chief decomposes a product feature into per-repo assignments, not into a second list. You touch
  only this file. The North Star lives in the root `CLAUDE.md`; notes and specs are others'.
- **Accumulate, never delete.** The features list is declarative — the product's desired state. A
  built feature is marked `[x]`, never removed; the list only grows.
- **Strictly the template shape.** The whole file *is* the `example.features.md` template shipped
  beside this skill — nothing else.
