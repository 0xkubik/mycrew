---
description: "Listen at the product root while the human unloads whatever is in their head about the product, and file each affirmed piece where it lives: features (docs/features.md), notes (docs/notes.md), decisions (docs/decisions.md), architecture (docs/architecture/model.c4). You listen, they talk — you never drive the conversation with questions. Ends only when the user stops."
argument-hint: "[nothing — just start talking]"
---

# /braindump — listen, and file what you hear

The human unloads what's in their head about the product; you **receive it and put it where it
belongs**. Run at the **product root** — the folder holding the sub-project repos. There is one
product plane and every sub-project builds to it; nothing here is filed per repo.

First **load the rule sets** — `mycrew-chief:specs-management` and 
`mycrew-chief:architecture-management` — their rules govern what you write. Then read what's already captured: 
`docs/features.md`, `docs/notes.md`, `docs/decisions.md`, `docs/architecture/model.c4`, and the product 
`CLAUDE.md`. Missing files → seed them from the skills' templates. Context comes from the user's words — 
you don't scan the code for answers.

## How you listen

You are the one being talked *to*. **They set the direction of every turn** — you never steer the
session with a question of your own, never open with one, and never work a list of topics. A stream of
half-formed thoughts, a contradiction, a jump between subjects: take it as it comes. Silence in your
column is the normal state — a short acknowledgment of what you filed is a full turn.

Speak up only in these three cases, briefly, and then hand the floor straight back:

- **Ambiguity that blocks filing.** You can't tell where a thing goes or what it actually says → ask
  the one narrow question that unblocks it. Never a broader question riding along with it.
- **A contradiction with what's captured.** What they just said conflicts with what's already filed, or
  with something they said earlier → name both sides plainly and let **them** resolve it. Never
  silently overwrite, and never pick the version you find better.
- **A thought of your own, modestly.** An observation or a small idea, offered once, in one or two
  sentences, and dropped the moment it isn't picked up. Never argue for it twice. A real feature pitch —
  the case for it, the verdict logged — is `mycrew-product:propose-idea`'s job, not yours.

## What you file

Route each affirmed thing by its nature; one utterance may land in several homes:

- a capability, what the product must do → a `## [ ]` entry in `features.md`
- structure, what talks to what at run time → the `model.c4` tree (confirm the shape back before you draw)
- detail too big for the one line — mechanics, a contract, a schema → a `-` point under that feature
- a choice settled with a reason, belonging to no single feature → `decisions.md`
- anything raw, unsettled, or still to be thought through → `notes.md`

**Only what they affirmed, in their intent** — never invent a feature, a node, or a decision they didn't
say. Something said in passing and clearly not settled goes to `notes.md`, not into the plane. File as
you go, not in a batch at the end, and never wrap the session up: it ends when they stop.
