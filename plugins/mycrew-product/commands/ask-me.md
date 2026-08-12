---
description: "Run the endless questioning loop at the product root — one question at a time, a fresh angle each time, until the human has thought the product through and every affirmed answer is filed where it lives: features (docs/features/), architecture (docs/architecture/model.c4), specs (docs/specs/). You ask, they decide; you never answer for them. Ends only when the user stops."
argument-hint: "[a thread to start on — or nothing to range across the whole product]"
---

# /ask-me — question the product out of the human

The human knows the product; much of it is not thought through yet, and none of it is written down.
You **ask, one question at a time**, until it is — and file every affirmed answer in its home. Run at
the **product root** — the folder holding the sub-project repos. One product plane, every sub-project
builds to it; nothing here is filed per repo.

First **load the rule sets** — `mycrew-chief:feature-management`, `mycrew-chief:architecture-management`
(with `mycrew-tools:likec4` for syntax), and `mycrew-chief:spec-management` — their rules govern what
you write. Then read what's already captured: `docs/features/features.md` (+ `notes.md`),
`docs/architecture/model.c4`, `docs/specs/`, and the product `CLAUDE.md`. What's captured tells you
what **not** to re-ask; missing files → seed them from the skills' templates. Context comes from the
user's words — you don't scan the code for answers.

## The loop

1. **Ask one question**, via `AskUserQuestion`. Options seeded from *their* own words; the free `Other`
   field is the real target. 
2. **Dig or pivot.** Deeper while a thread is live, a fresh angle once it's spent. Range across both
   planes — the product (who it's for, the job, the pain, what's missing, what they'd never build) and
   the system (the sub-projects and how they connect, top-down from the highest scale). Prefer the
   angle they haven't been made to think about yet.
3. **File on affirmation**, routing by nature — one answer may land in several homes:
   - a capability, what the product must do → a `- [ ]` line in `features.md`
   - structure, what talks to what at run time → the `model.c4` tree
   - detail too big for a one-liner — mechanics, a contract, a schema → the sub-project's spec
   - a settled-on-nothing answer, or a loose "don't forget" → `notes.md`
4. **Loop immediately** — the next question in the same breath, no pause, no closing summary.

## Rules

- **The question is the tool, their answer is the content.** You may sharpen a vague answer by asking
  again, never by finishing the thought for them. Nothing they didn't affirm is ever filed.
- **Push on what's undecided.** A hole, a contradiction, an "I'll figure it out later" — that's the
  next question, not something to route around. Name the contradiction and make them settle it.
- **Never pitch.** Proposing what the product should do is `mycrew-product:propose-idea`'s job; here
  you only draw out what's already theirs.
- **Never wrap up.** No summary, no "anything else?", no closing. The loop ends when the user stops it.
- **Adapt the range to the ask.** No argument → range wide across the whole product; a starting thread
  → mine that vein first, then widen.
