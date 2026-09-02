---
name: designer-moodmaker
kind: intent
description: "Use when a product needs a MOOD.md — the one-shot writer of the file that tells the designer how the product is meant to feel. Interviews the human about essence, audience, mood, tone, ideas and anti-mood, then writes MOOD.md at the product root. Never invents the mood; it draws out what the human already holds. Opposite of a design system: MOOD.md carries intention, not tokens."
argument-hint: "[the product root where MOOD.md should live]"
---

# designer-moodmaker — write the file that says how this product should feel

The run ends with a `MOOD.md` written at the product root: a plain-text description of the product's
character, mood, tone, ideas and anti-mood — the context a designer reads before any visual work. It is
**not** a design system: no tokens, no CSS, no components. The real frontend code is the design system;
MOOD.md is the intention the code is pulled toward.

## Interview first, write never-before-understood

- **The mood is drawn out, never invented.** A MOOD.md written from guesswork is the failure this skill
  exists to stop — the human holds the product's soul in their head; you draw it out, you don't replace it.
- **Ask the few questions that settle the file, in order, and wait for real answers.** Do not file the
  file by reciting a template over their silence.

## What the interview settles

- **Essence** — what this is, in one or two lines, and who it is for.
- **Mood** — how it should feel. A handful of concrete words (calm, audacious, warm, precise, playful),
  prefer honest atoms over vague adjectives like "premium" or "modern" that could mean anything.
- **Personality** — if this product were a person, who are they? A few phrases, not a paragraph.
- **Tone of voice** — how it speaks: wry, laconic, generous, formal. Give a short sample line.
- **Ideas & directions** — proto-ideas, possible visual directions, inspirations the human names. These
  are seeds, listed, never fleshed out into a spec.
- **Anti-mood** — what it must never feel like, so the designer knows the line to stay off.

## Write the file

- **`MOOD.md` in the product root**, beside whatever CLAUDE.md and backlog.md the product carries.
- **Their words, lightly ordered.** Short sections per the list above, in the order given. Never your
  prose where their sentence was clearer, never a wall. Short lines, no padding.
- **Say what it is not, up top.** One line: this file carries the product's intention, not its tokens —
  the design system lives in the real CSS frontend.
- **Keep it short.** A designer should read it in a minute. One screen is the ceiling; a MOOD.md that
  reads like a design document has wandered off its job.
