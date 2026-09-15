---
name: designer-import
description: "Use when the human hands over a batch of pages exported from Claude Design (or any outside design work) to fold into the product. Breaks what arrived into the smallest reusable bricks, extends the kit with them, then assembles the screens those bricks belong to. Reads designer-craft for what good and bad look like; never invents a direction of its own — the human already decided it."
argument-hint: "<the exported files, or what changed since last time>"
---

# designer-import — fold what the human already decided into the kit

Everything the product is built out of lives in `design/kit.html`: the mood, the tokens, then each
component with its markup, CSS and every state, then the screens assembled out of them. This skill is
how outside work — a batch of pages exported from Claude Design, most often — becomes part of that one
file. The human has already made the creative call; this is extraction and fit, not invention. Judge
what you produce against `designer-craft`, never against your own taste.

## First run vs. an update

- **Nothing in `design/kit.html` yet** — read everything handed over before touching the file, and
  build the tokens and the first bricks from what actually repeats across it.
- **The kit already exists** — this is an edit, not a rewrite. Work out what changed since the last
  import (a new screen, a reworked component) and touch only the sections that changed. Never redo the
  whole file because part of it did.

## Breaking it down

- **Split as far as it goes.** A button, a field, a row, a badge, a card — each is its own brick, even
  if right now only one screen uses it. A screen imported as one solid block is not imported, it is
  pasted.
- **Find the repeats.** The same card shape on three pages is one component with three uses, not three
  components. Merge on sight; a kit with near-duplicate bricks is already drifting.
- **Extend, don't append.** A brick that's a variant of one already in the kit goes into that
  component's own states and sizes, in its own section — never bolted on at the end of the file as a
  near-copy.

## Building the bricks

- Extract the tokens first — colour, type, spacing — name them by role per `designer-craft`, even if
  the export named them by hue or used raw values inline.
- Carry over every state the export shows; where it's missing one a live product needs (hover, focus,
  disabled, loading, empty, error), add it, matching the export's own language rather than inventing a
  new visual idea.
- Keep the words as the human wrote them, unless they conflict with themselves across screens — flag
  that in the report rather than silently picking one.

## Assembling the screens

Once the bricks a screen needs exist in the kit, assemble it there per `designer-craft`'s composition
rules: its job in one sentence, what dominates, behaviour over time, its edges, how it connects to its
neighbours. Add it to the Screens section of `design/kit.html`.

## Before you call it done

- **Render it and look.** Serve `design/` over HTTP (not `file://`, and not a cache that will hand you
  yesterday's kit), open it, and check it against `designer-craft`'s tells for bad design and the
  accessibility floor — both themes if the kit has more than one.
- **Prove nothing is dangling.** No class used in the kit's markup that its stylesheet does not define.
- **Commit the kit** so the work outlives the run.

## Report

Goes in your reply, never into a file. **What arrived** (what was handed over) · **Bricks** (new or
extended, and what was merged as a repeat) · **Screens** (assembled, with the arrangement in words so
the coder can build without opening the kit) · **Flagged** (anything inconsistent in what arrived, or a
gap the export didn't cover, left for the human rather than guessed).
