---
description: "Run the endless setup interview at the product root — cyclically draw the whole product out of the human and file each affirmed piece where it lives: features (docs/features/), architecture (docs/architecture/model.c4), specs (docs/specs/). One product plane, shared by every sub-project. Never contributes its own ideas; stops only when the user stops."
argument-hint: "[a starting thread — or nothing to open the whole setup]"
---

# /setup — pull the product out, file it where it lives

You run an **endless interview** that draws the product out of the user and files every affirmed
piece in its home. Run at the **product root** — the folder holding the sub-project repos. There is
one product plane and every sub-project builds to it; nothing here is filed per repo.

First **load the rule sets** — `mycrew-product:feature-management`, `mycrew-chief:architecture-management`
(with `mycrew-tools:likec4` for syntax), and `mycrew-chief:spec-management` — their rules govern what
you write; this command only runs the loop. Context comes from the user's words — you don't scan the
code for answers.

Then run the loop:

1. **Open the ground.** Read what exists — `docs/features/features.md` (+ `notes.md`),
   `docs/architecture/model.c4`, `docs/specs/`, and the product `CLAUDE.md`. What's captured tells you
   what not to re-ask. Missing files → seed them from the skills' templates.
2. **Ask** — one question, a fresh angle, via `AskUserQuestion`. Range across both planes — the
   product (who it's for, the job, the pain, what's missing, what they'd never build) and the system
   (the sub-projects and how they connect, top-down from the highest scale). Options seeded from
   *their* words; the free `Other` field is the real target.
3. **Dig or pivot.** Deeper on a live thread; a new angle when one is spent. Keep pulling out what
   they haven't said yet.
4. **File on affirmation.** When something they affirm emerges, route it by its nature — one
   utterance may land in several homes:
   - a capability, what the product must do → a `- [ ]` line in `features.md`
     (feature-management rules: ≤200 chars, accumulate, never delete)
   - structure, what talks to what at run time → the `model.c4` tree
     (architecture-management rules: confirm the shape back before you draw)
   - detail too big for a one-liner — mechanics, a contract, a schema → a spec in `docs/specs/`
     (spec-management rules)
   - a loose "don't forget" → `notes.md`
5. **Loop immediately.** Pose the next question in the same breath — no pause, no closing summary.

**Extract, never contribute** — their vision, never yours; never invent a feature, a node, or a spec
they didn't affirm. This is the ground-laying half of the product layer and it stays strictly
extractive: **proposing what the product should do next is not this command's job** — that's
`mycrew-product:propose-idea`. Never break the
conversation and never wrap up — the loop ends only when the user stops it. Adapt the shape to the
request: a broad "set up the product" ranges wide; a narrow starting thread digs that vein first,
then widens.
