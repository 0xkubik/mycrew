---
name: designer-compose
description: "Use when the designer has to settle how a screen is put together — what it is built from, in what order, how it behaves over time, and how it connects to its neighbours. The assembled screen lands in kit.html and the arrangement comes back in the report; no application code is ever written."
argument-hint: "<the screen or flow to compose>"
---

# designer-compose — assemble the bricks into a screen

Takes the screens a piece of work needs and settles how each is put together out of the kit's own
components. The result lands twice: as an assembled screen in `design/kit.html`, and in words in the
report the coder builds from. Nothing here touches the application's code.

## Steps

1. **Say the screen's job in one sentence.** Who arrives, what they came to do, what they leave with.
   A screen whose job will not fit in one sentence is two screens.
2. **Pick the one thing that dominates.** Everything else supports it or goes. If two things compete
   for first place, neither is first and the screen has no hierarchy.
3. **Assemble from the kit.** List the components the screen is built from, in the order they read.
   Anything missing gets made first with `designer-kit` — never improvised inline.
4. **Lay out the arrangement.** Grouping, order, where the eye lands and where it goes next, what is
   reachable without scrolling, what the spacing rhythm separates from what.
5. **Settle behaviour over time.** What the screen shows while it loads, when it holds nothing, when it
   fails, and what a person sees the moment after they act. Each of these is designed here, never left
   for the coder to invent.
6. **Take it to its edges.** Narrow width, long text, zero items, three hundred items, a slow network.
   Say what collapses, what wraps, what holds.
7. **Connect it to what already exists.** Where a person arrives from, where they can go, how they get
   back, what stays on screen across the flow so the product reads as one place. Consistency with the
   screens already in the kit beats a better idea for this screen alone.
8. **Write it into the kit, then report it.** Add the assembled screen to the Screens section of
   `design/kit.html`, in the shape `data/designer/kit-template.html` lays out, so the next run inherits
   it instead of deciding again.

## Done

- **The screen exists in `design/kit.html`** as a real assembled block, not a description of one.
- **The report carries the arrangement in words** — job, what dominates, components in order, behaviour
  at loading, empty and error, what happens at the edges, and its neighbours. Enough for the coder to
  build without guessing, and without a line of application code from you.
