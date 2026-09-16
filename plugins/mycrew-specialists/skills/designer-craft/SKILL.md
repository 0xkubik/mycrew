---
name: designer-craft
description: "The shared reference for what good design actually is — palette, type, tokens, component completeness, wording, the accessibility floor, composition, and the tells of bad design, both in the spec and in the real kit it becomes. Not a process to run on its own: designer-import builds against it while writing the spec, coder-kit builds against it while turning that spec into real components, tester-visual judges a shipped build against it."
---

# designer-craft — what good design is, and what bad design is

The craft floor every other design work in this project builds against or is judged against. This is
knowledge, not a process — nothing here is a step to run. `designer-import` reads it while writing the
spec; `coder-kit` reads it while turning that spec into the real kit; `tester-visual` reads it while
judging a shipped build.

## Ground the choice

- **The product's subject drives palette and voice.** A toy brand and a fintech dashboard never share a
  kit — industry, audience and material are where distinct choices come from. Read the mood section of
  the product's `CLAUDE.md` if it has one and design to it; when what arrived fights it, say so outright.
- **Type carries the personality.** One or two clearly distinct families, a real scale, deliberate
  weight, line length under 80 characters.
- **Icons from one set.** Lucide, Phosphor, Heroicons, Radix, Tabler — pick one and stay in it.
  Mismatched stroke width and grid read as loudly as mismatched type.

## Tokens carry roles, not colours

- **Name a token by its job, never by its hue.** Surface, ink, muted, accent, border, danger —
  `--accent`, never `--orange`. A kit named by hue can never grow a second theme.
- **4–6 base values and one accent.** Everything else derives. A palette that needs a legend is too big.
- **Spacing, radius and weight are scales too.** A component that invents its own number breaks the
  rhythm of every component beside it.

## A component is its states

- **Not done until it has all of them.** Rest, hover, focus, active, disabled, loading, empty, error.
  A component handed over with only rest hands the coder a guess.
- **Keyboard focus is a state, not a browser default to delete.** It must be visible on every control.
- **Build it against hostile content.** A long name, a wrapped label, an empty list, three hundred rows.
  Anything that only holds on the sample data is not built.
- **Change its contract and you sweep the whole kit.** Rename a class, restructure a component's markup,
  swap the device it is drawn with — then update every place in the kit that uses it, in the same run.
  The kit is one file, so this is cheap; a half-swept kit is worse than the one you started with,
  because now two versions of the same brick are both on screen and both look deliberate.

## What you cannot draw yourself

Two kinds of thing never get a finished drawing — a slot with a brief instead, and a slot with a brief
is delivered work, not a gap.

- **An asset somebody has to draw.** An emblem, a medal, a mascot, an illustration, a mark, an icon no
  set carries. A real slot: one variable owns its size so a single file will serve every place it
  appears, and prose beside it says what arrives, what it replaces and what falls away when it does.
  Say plainly that it *is* a placeholder — otherwise it ships as final.
- **A motion the base tools do not reach.** A transition, a hover, a press, a thing that slides or
  settles — write it in CSS and it belongs in the kit, working. Anything past that — a drawn loop, a
  character, a sequence somebody has to animate — is described in words beside the component it belongs
  to: what moves, what sets it off, how long it takes, where it ends, and what stands in its place for a
  reader who has asked for less motion.

## Words belong to the component

- **One name for one action, everywhere.** A button that says "Publish" produces "Published".
- **Errors say what happened and what to do next** — never apologetic, never vague. An empty state is
  an invitation to act, not a shrug.
- **Name things the way the user says them**, not the way the system is built.

## The floor, never traded away

Contrast holds — 4.5:1 for text, 3:1 for interface edges. Targets big enough to hit. Text survives 200%
zoom. Motion respects the reduced-motion setting. Every control carries a name a screen reader can read.
A kit is not handed over while one pair sits under its floor — verify it, in whatever way is at hand,
before calling anything done.

## Bad practice — the tells

- **Motion as decoration.** A fade-slide-up on every card, a hover transition on everything. Animate
  only in answer to a person's action.
- **The generated look.** Identical rounded cards under one grey shadow; tracked ALL-CAPS eyebrows; meta
  joined by middle dots; a spaced em dash in every label; near-black standing in for black; a monospace
  face on small data; "→" after every link. None is wrong when chosen — all are wrong as a default.
- **Decoration that says nothing.** Numbering content that is not a sequence, a divider separating
  nothing, an eyebrow added to look structured.
- **Boldness spread thin.** One memorable move, everything else quiet. Look at the finished thing and
  take one accessory off.
- **Lifted wholesale.** A reference is fuel for something of your own, never a thing to transplant.

## Assembling a screen

- **Say the screen's job in one sentence.** Who arrives, what they came to do, what they leave with.
  A screen whose job will not fit in one sentence is two screens.
- **Pick the one thing that dominates.** Everything else supports it or goes. If two things compete for
  first place, neither is first and the screen has no hierarchy.
- **Settle behaviour over time.** What the screen shows while it loads, when it holds nothing, when it
  fails, and what a person sees the moment after they act. Never left for the coder to invent.
- **Take it to its edges.** Narrow width, long text, zero items, three hundred items, a slow network.
  Say what collapses, what wraps, what holds.
- **Connect it to what already exists.** Where a person arrives from, where they can go, how they get
  back, what stays on screen across the flow. Consistency with the screens already in the kit beats a
  better idea for this screen alone.

## What bad looks like, in a finished build

- **No hierarchy** — nothing is clearly first, or everything shouts at once.
- **Not readable** — contrast too low, text too small, lines too long, density crushing.
- **Broken rhythm** — arbitrary spacing, nothing aligned, gaps that differ for no reason.
- **Templated** — identical rounded cards under one shadow, ALL-CAPS eyebrows, an arrow after every
  link, decoration that says nothing about the content.
- **No answer to an action** — pressed, and nothing visibly happened; nothing shows that it is loading.
- **Layout jumps** — interacting with one element moves others that were not touched: content reflows
  under a tooltip, a list shifts when one row expands, neighbours jump when something loads in.
  Untouched elements hold their place.
- **A dead end** — empty with nowhere to go, an error with no way out.
- **Lying about state** — a placeholder that reads as data, a disabled control that reads as live.
- **Out of reach** — targets too small to hit, no visible focus when moving by keyboard.
- **Falls apart at the edges** — narrow screen, long text, empty list, overfull list.
- **Wrong words** — system language, a button and its result named differently, an error that
  apologises instead of saying what to do.
- **Noise** — motion for its own sake, decoration doing no work, one accessory too many.
