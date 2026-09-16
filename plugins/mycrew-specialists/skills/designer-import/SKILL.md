---
name: designer-import
description: "Use when the human hands over a batch of pages exported from Claude Design (or any outside design work) to fold into the product. Breaks what arrived into the smallest reusable bricks and writes the spec the coder builds the real kit from. Reads designer-craft for what good and bad look like; never invents a direction of its own — the human already decided it."
argument-hint: "<the exported files, or what changed since last time>"
---

# designer-import — fold what the human already decided into the spec

The product's design truth lives in `design/spec.md` — the mood, the tokens, then each component broken
down into its bricks, its variants, its states, then how the screens arrange them — plus the original
pages saved in `design/reference/` for whoever builds against the spec to check fidelity later. This
skill is how outside work — a batch of pages exported from Claude Design, most often — becomes that spec.
The human has already made the creative call; this is extraction and description, not invention. Judge
what you write against `designer-craft`, never against your own taste. The spec is not the kit —
`coder-kit` builds the real thing from it.

## First run vs an update

- **Nothing in `design/spec.md` yet** — read everything handed over before writing a line, and build the
  tokens and the first bricks from what actually repeats across it.
- **The spec already exists** — this is an edit, not a rewrite. Work out what changed since the last
  import (a new screen, a reworked component) and touch only the sections that changed. Never redo the
  whole file because part of it did.

## Breaking it down

- **Split as far as it goes.** A button, a field, a row, a badge, a card — each is its own brick, even
  if right now only one screen uses it. A screen described as one solid block is not imported, it is
  pasted.
- **Find the repeats.** The same card shape on three pages is one component with three uses, not three
  components. Merge on sight; a spec with near-duplicate bricks is already drifting.
- **Extend, don't append.** A brick that's a variant of one already in the spec goes into that
  component's own states and sizes, in its own section — never bolted on at the end of the file as a
  near-copy.

## Writing the spec

- **Tokens by role, not by hue.** Colour, type, spacing — name them by job per `designer-craft`, even if
  the export named them by hue or used raw values inline. Value plus role is enough; there is no CSS to
  write here.
- **Every state the export shows, plus every state a live product needs and it doesn't** — hover, focus,
  disabled, loading, empty, error — describe each precisely enough that whoever builds it doesn't have to
  guess. Match the export's own visual language rather than inventing a new idea.
- **Keep the words as the human wrote them**, unless they conflict with themselves across screens — flag
  that in the report rather than silently picking one.
- **Save the originals.** Whatever pages or screenshots arrived go into `design/reference/`, named so
  it's obvious which brick or screen each backs.

## Describing the screens

Once the bricks a screen needs are in the spec, describe its arrangement per `designer-craft`'s
composition rules: its job in one sentence, what dominates, behaviour over time, its edges, how it
connects to its neighbours. Add it to the Screens section of `design/spec.md` — words, not markup;
`coder-kit` is what turns this into something that renders.

## Before you call it done

- **Check it against `designer-craft`'s tells for bad design and the accessibility floor** — using the
  original pages, since there is nothing of yours yet to render.
- **Commit the spec** so the work outlives the run.

## Report

Goes in your reply, never into a file, and doubles as the brief for whoever runs `coder-kit` next.
**What arrived** (what was handed over) · **Bricks** (new or extended, and what was merged as a repeat) ·
**Screens** (described, with the arrangement in words so the coder can build without opening the spec) ·
**Flagged** (anything inconsistent in what arrived, or a gap the export didn't cover, left for the human
rather than guessed).
