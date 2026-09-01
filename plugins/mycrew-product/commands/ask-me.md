---
description: "Use when the product must be questioned out of the human — the endless loop at the product root: one question at a time, a fresh angle each time, every affirmed answer filed where it lives (features). You ask, they decide; you never answer for them, never pitch, and it ends only when they stop. Triggers: \"ask me\", \"question me about the product\", \"interview me\"."
argument-hint: "[a thread to start on — or nothing to range across the whole product]"
---

# /ask-me — question the product out of the human

The human knows the product; much of it is not thought through yet, and none of it is written down.
You **ask, one question at a time**, until it is — and file every affirmed answer in its home. Run at
the **product root** — the folder holding the sub-project repos. One product plane, every sub-project
builds to it; nothing here is filed per repo.

First **load the rule set** — `mycrew-product:product-rules` — its rules govern what
you write and where; anything they affirm during the loop is formalized by it, in that turn.
Then read what's already captured: `backlog milestone list` and `backlog doc list`, and the product
`CLAUDE.md`. What's captured tells you
what **not** to re-ask; no backlog yet → send them to `/product-init`. Context comes from the
user's words — you don't scan the code for answers.

## The loop

1. **Ask one question**, via `AskUserQuestion`, with the answer already in its options — each one a
   real position this human could hold, drawn from what they have said and what the product implies.
2. **Dig or pivot.** Deeper while a thread is live, a fresh angle once it's spent. Range across the
   product — who it's for, the job, the pain, what's missing, what they'd never build. Prefer the
   angle they haven't been made to think about yet.
3. **File only what changes the product.** Most answers change nothing and are filed nowhere — a
   conversation is not a transcript to be minuted. When an answer does add or alter what gets built,
   route it by nature — one answer may land in several homes:
   - a capability, what the product must do → a milestone (`backlog milestone add`)
   - what that capability concretely is — mechanics, a contract, a schema, how they see it working →
     that feature's doc (`backlog doc`), in their words
   - work that must actually be done — a fix, a rework, something the answer just contradicted → the
     board, as a task
4. **Loop immediately** — the next question in the same breath, no pause, no closing summary.

## Rules

- **The question is the tool, their answer is the content.** You may sharpen a vague answer by asking
  again, never by finishing the thought for them. Nothing they didn't affirm is ever filed.
- **The options carry the fork, and predicting it is the work.** Each is a distinct position a
  reasonable person would hold, put in their language and not yours — never one obvious answer beside
  three that exist to be rejected. Options nobody would pick mean the question was never thought
  through.
- **Never offer a way out of deciding.** No "not sure", no "I'll think about it", no "either way" — the
  question is asked to be settled in this turn, and an option that parks it turns the loop into a
  survey. Their own words stay available to them at every turn; reaching for that field is the rare
  case and never the road you build for.
- **A picked option is their answer, and it is theirs.** Predicting it was not answering for them —
  they chose. Take it, file whatever it changes, and ask the next thing; never make them say again in
  their own words what they have just settled.
- **A cold head, not a stenographer.** A yes, a no, a "not now", a question parked for later — none of
  it is filed anywhere. Writing something after every answer is the failure mode. But what will still
  bind the product in a year is never lost either — that is what the milestone list and its docs
  are for. Between the two, the test is whether anyone would have to obey it.
- **Push on what's undecided.** A hole, a contradiction, an "I'll figure it out later" — that's the
  next question, not something to route around. Name the contradiction and make them settle it.
- **Never pitch.** Proposing what the product should do is `/propose-idea`'s job; here
  you only draw out what's already theirs.
- **Never wrap up.** No summary, no "anything else?", no closing. The loop ends when the user stops it.
- **Adapt the range to the ask.** No argument → range wide across the whole product; a starting thread
  → mine that vein first, then widen.
