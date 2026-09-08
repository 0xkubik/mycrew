---
name: designer-kit
description: "Use when the designer is making or extending the product's bricks — tokens, a component, its states. Best and worst practice for the craft; the kit comes back extended, one component at a time, never a whole screen."
argument-hint: "<the kit piece being made>"
---

# designer-kit — the bricks, made well

Everything the product is built out of lives in `design/kit.html`: the mood, the tokens, then each
component with its markup, CSS and every state. Its shape is fixed by `data/designer/kit-template.html` —
start the kit from that skeleton on first use, and afterwards extend the section a piece belongs to
instead of appending to the end. This skill is the craft floor for that file — what good looks like and
what bad looks like. Screens are assembled elsewhere, with `designer-compose`.

## Ground the choice

- **The product's subject drives palette and voice.** A toy brand and a fintech dashboard never share a
  kit — industry, audience and material are where distinct choices come from. Read the mood section of
  the product's `CLAUDE.md` if it has one and design to it; when the brief fights it, say so outright.
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

You have no illustrator and no motion tool, and you never will. Two kinds of thing therefore leave the
kit as **a slot with a brief** rather than as a finished drawing — and a slot with a brief is delivered
work, not a gap.

- **An asset somebody has to draw.** An emblem, a medal, a mascot, an illustration, a mark, an icon no
  set carries. Build the placeholder as a real slot: one variable owns its size so a single file will
  serve every place it appears, and the component's own prose says what arrives, what it replaces and
  what falls away when it does. Say plainly, in the kit, that it *is* a placeholder — otherwise the
  coder ships it. Never draw a permanent approximation in CSS and leave it looking finished.
- **A motion the base tools do not reach.** A transition, a hover, a press, a thing that slides or
  settles — write it in CSS and it belongs in the kit, working. Anything past that — a drawn loop, a
  character, a sequence somebody has to animate — is described in words beside the component it belongs
  to: what moves, what sets it off, how long it takes, where it ends, and what stands in its place for a
  reader who has asked for less motion.

Reach for both rather than around them. A kit with no assets and no motion in it is a wireframe, and
nobody asked for a wireframe. Describing one costs a paragraph; leaving it out costs the product its
character.

## Words belong to the component

- **One name for one action, everywhere.** A button that says "Publish" produces "Published".
- **Errors say what happened and what to do next** — never apologetic, never vague. An empty state is
  an invitation to act, not a shrug.
- **Name things the way the user says them**, not the way the system is built.

## The floor, never traded away

- Contrast holds — 4.5:1 for text, 3:1 for interface edges. Targets big enough to hit. Text survives
  200% zoom. Motion respects the reduced-motion setting. Every control carries a name a screen reader
  can read.
- **The palette carries its own check, and it is runnable.** Copy `data/designer/contrast.mjs` in beside
  the kit on first use, list in it every pair the kit actually puts on screen, and run it after touching
  a colour — it measures every theme in one pass. A kit is not handed over while one pair sits under its
  floor. Without this, "both themes are correct" is a thing you believe rather than a thing you know.

## Bad practice — the tells

- **Motion as decoration.** A fade-slide-up on every card, a hover transition on everything. Animate
  only in answer to a person's action. No JS motion library — the kit has nowhere to wire one.
- **The generated look.** Identical rounded cards under one grey shadow; tracked ALL-CAPS eyebrows; meta
  joined by middle dots; a spaced em dash in every label; near-black standing in for black; a monospace
  face on small data; "→" after every link. Warm cream with a serif and a terracotta accent; near-black
  with one neon; broadsheet hairlines at zero radius. None is wrong when chosen — all are wrong as a
  default.
- **Decoration that says nothing.** Numbering content that is not a sequence, a divider separating
  nothing, an eyebrow added to look structured.
- **Boldness spread thin.** One memorable move, everything else quiet. Look at the finished thing and
  take one accessory off.
- **Lifted wholesale.** A reference is fuel for something of your own, never a thing to transplant.

## Before you call it done

- **Render it and look.** Open `design/kit.html`, screenshot it, name what is weak out loud, fix it.
  Reading your own CSS is not looking, and a first pass is not an answer.
  - **Serve it, do not open the file.** The browser refuses `file://`, and a plain static server hands
    you a cached stylesheet — you will screenshot yesterday's kit and believe it. Serve the design
    folder over HTTP with `Cache-Control: no-store`.
  - **Look at every theme, forced.** Set `[data-theme]` yourself rather than leaving it to the system: a
    browser that darkens pages on its own will show you a dark screenshot of your light theme and tell
    you nothing at all.
  - **Prove nothing is dangling.** No class used in the kit's markup that its stylesheet does not
    define. It is one pass over one file and it catches every brick you renamed and half-swept.
