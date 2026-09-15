---
name: tester-visual
description: "Use when the human explicitly asks for the design itself to be judged on a build that already runs — never on the tester's or lead's own initiative, since it opens their real screen. Looks with the eye, not the code, against designer-craft's tells for bad design, names what came out bad, fixes small things in place, flags the rest."
argument-hint: "<the built screen or flow to look at>"
---

# tester-visual — look at what came out, name what is bad

Runs standalone, only when the human asks for it by name — same discipline as `tester-manual`. The
screen is already built and running; this pass opens it, uses it, and judges the design a person
actually meets against `designer-craft`. It is not a check against the kit and not a read of the code.

## How to look

- **Open the real thing and use it.** Browser or screenshot, at a real width, with the content that is
  actually there — not sample data.
- **Look before you reason.** First impression first: where did the eye go, and was that the right
  place.
- **Judge the result, not the intent.** A screen that follows the kit exactly and still reads badly is
  still bad, and saying so is the whole point of this pass.

## What bad is

Read `designer-craft`'s "what bad looks like, in a finished build" section — the same list, so a
finding here means the same thing it would from the designer.

## Fixing it

- **Fix small things in place** — a spacing slip, a missing state, a wrong word — the same way you
  would on any other pass, and note it.
- **Flag what you can't** — a real design disagreement, or a gap that needs the kit itself extended —
  goes back through `designer-import` as its own piece of work, never patched around here.

## Report

- **One line per finding**: what is bad, which tell it is, and the fix — applied or flagged.
- **Ranked by what a person meets first.** A broken hierarchy outranks a two-pixel gap.
- **One honest line on what is good**, so the list doesn't read as a verdict on everything.
