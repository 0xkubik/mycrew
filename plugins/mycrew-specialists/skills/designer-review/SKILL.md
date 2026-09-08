---
name: designer-review
description: "Use when the human explicitly asks the designer to look at a build that already runs and judge the design that came out of it — never on the designer's, lead's or coder's own initiative, since it opens their real screen. Looks with the eye, names where the design came out bad, hands back concrete fixes, and edits nothing."
argument-hint: "<the built screen or flow to look at>"
---

# designer-review — look at what came out, name what is bad

Runs standalone, only when the human asks for it by name. The screen is already built and running; this
pass opens it, uses it, and judges the design a person actually meets. It is not a check against the kit
and not a read of the code. Nothing is edited.

## How to look

- **Open the real thing and use it.** Browser or screenshot, at a real width, with the content that is
  actually there — not the sample data and not `kit.html`.
- **Look before you reason.** First impression first: where did the eye go, and was that the right place.
- **Judge the result, not the intent.** A screen that follows the kit exactly and still reads badly is
  still bad, and saying so is the whole point of this pass.

## What bad is

- **No hierarchy** — nothing is clearly first, or everything shouts at once.
- **Not readable** — contrast too low, text too small, lines too long, density crushing.
- **Broken rhythm** — arbitrary spacing, nothing aligned, gaps that differ for no reason.
- **Templated** — identical rounded cards under one shadow, ALL-CAPS eyebrows, an arrow after every
  link, decoration that says nothing about the content.
- **No answer to an action** — pressed, and nothing visibly happened; nothing shows that it is loading.
- **A dead end** — empty with nowhere to go, an error with no way out.
- **Lying about state** — a placeholder that reads as data, a disabled control that reads as live.
- **Out of reach** — targets too small to hit, no visible focus when moving by keyboard.
- **Falls apart at the edges** — narrow screen, long text, empty list, overfull list.
- **Wrong words** — system language, a button and its result named differently, an error that
  apologises instead of saying what to do.
- **Noise** — motion for its own sake, decoration doing no work, one accessory too many.

## Report

- **One line per finding**: what is bad, which of the above it is, and the concrete fix.
- **Ranked by what a person meets first.** A broken hierarchy outranks a two-pixel gap.
- **One honest line on what is good**, so the list is not read as a verdict on everything.
- **Edit nothing.** The coder applies what is accepted; a gap in the kit itself goes back through
  `designer-kit` as its own piece of work.
