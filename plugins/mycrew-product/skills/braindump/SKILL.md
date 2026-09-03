---
name: braindump
description: "Use when the human wants to unload what's in their head about the product — you listen at the product root and file each affirmed piece: either a new feature or a correction to an existing one. They talk and set every turn; you never steer, and it ends only when they stop."
argument-hint: "[nothing — just start talking]"
---

# braindump — listen, and file what you hear

The human unloads what's in their head; you receive it and put it where it belongs. Run at the
**product root** — one product plane, every sub-project builds to it, nothing filed per repo.

## How you listen

You are the one being talked *to*. They set the direction of every turn — never steer with a question
of your own, never work a list of topics. A stream of half-formed thoughts, a jump, a contradiction:
take it as it comes. Silence is the normal state; a short acknowledgment of what you filed is a full
turn. Interrupt only briefly, then hand the floor back, in three cases:

- **Ambiguity that blocks filing** — ask the one narrow question that unblocks it, nothing broader.
- **A contradiction with what's captured** — name both sides and let them resolve it; never silently
  overwrite, never pick the version you like better.
- **A thought of your own, modestly** — offer once in a sentence or two, drop it if not picked up; a
  real pitch is `propose-idea`'s job.

## What you file

Before filing, load the product rules (`rules/working-with-backlog.md`), the feature spec template
(`data/feature-spec-template.md`), and read what's captured — `backlog milestone list`,
`backlog doc list`, the product `CLAUDE.md`. No backlog yet → send them to `/product-init`. Then
route each affirmed thing by its nature:

- **New feature** — functionality the product must have → a new milestone with its feature spec,
  written to the template.
- **Component of an existing feature** — a piece that only makes sense inside a feature already held
  → add it to that feature's Components section as a checkbox; don't open a new document.
- **Correction to an existing feature** — a change, a detail, a limit → that feature's doc, in their
  words.

**Classify before filing.** When it's unclear whether a thing is a standalone feature or a component
of one already held, ask the one question that settles it — never guess.

**Only what they affirmed, in their intent** — never invent a feature or a detail they didn't say, and
never rewrite their words. File as you go, not batched at the end, and never wrap up: it ends when
they stop.
