---
name: feature-management
description: "Use when features are being drawn out of a human and filed — the constraints any features interview obeys: the user's own features only (never your own ideas), a fresh angle each question, ≤200 chars per feature, the one product features list. Loaded by /setup; also a standalone reference."
---

# feature-management — the rules for drawing out features

**Rules — non-negotiable:**
- **≤200 chars per feature.** Compress each affirmed feature to one crisp line of **at most 200
  characters**, in the user's intent — not your embellishment.
- **One list, at the product root.** There is a single features list for the whole product —
  `docs/features/features.md` beside the root `CLAUDE.md`. Sub-projects keep no features of their own;
  the chief decomposes a product feature into per-repo assignments, not into a second list. You touch
  only this file. The North Star lives in the root `CLAUDE.md`; notes and specs are others'.
- **Accumulate or edit, never delete.** The features list is declarative — the product's desired state. A
  built feature is marked `[x]`, never removed; the list only grows.
- **Strictly the template shape.** The whole file *is* the `example.features.md` template shipped
  beside this skill — nothing else.
