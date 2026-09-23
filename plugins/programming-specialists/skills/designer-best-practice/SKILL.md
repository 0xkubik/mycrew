---
name: designer-best-practice
description: "What good design actually is — palette, tokens, component completeness, wording, the accessibility floor, composition — and the clearest tells of bad design, in a spec or a real running kit."
---

# designer-best-practice — what good design is, and what bad design is

The craft floor every design decision in this project is judged against. Knowledge, not a process —
nothing here is a step to run.

## Ground the choice

- Let the product's subject drive palette and voice — a toy brand and a fintech dashboard never match.
- Read the product's own mood or brand notes if they exist; say so when what arrived fights them.
- One or two clearly distinct type families, a real scale, deliberate weight.
- Line length stays under 80 characters.
- Icons from one set only — mismatched stroke width and grid read as loud as mismatched type.

## Tokens carry roles, not colours

- Name a token by its job, never its hue — `accent`, never `orange`.
- A kit named by hue can never grow a second theme.
- Keep it to 4–6 base values plus one accent; a palette that needs a legend is too big.
- Spacing, radius, and weight are scales too — an invented number breaks the rhythm.

## A component is its states

- Not done until every state exists: rest, hover, focus, active, disabled, loading, empty, error.
- Keyboard focus is a state, not a default to strip — visible on every control.
- Build against hostile content: a long name, a wrapped label, an empty list, three hundred rows.
- Changing a component's contract means sweeping every place in the kit that uses it, same run.
- A half-swept kit is worse than the one you started with — two versions on screen, both look deliberate.

## What you cannot draw yourself

- An asset somebody has to draw is a real slot, not a gap — a brief beside it counts as delivered work.
- Size a drawn asset with one variable so a single file serves every place it appears.
- Say plainly a slot is a placeholder, or it ships and reads as final.
- For motion the base tools can't reach, write what moves, what triggers it, how long, where it ends.
- Say what stands in its place for someone who asked for less motion.

## Words belong to the component

- One name for one action, everywhere — a button that says "Publish" produces "Published".
- An error says what happened and what to do next — never apologetic, never vague.
- An empty state is an invitation to act, not a shrug.
- Name things the way the user says them, not the way the system is built.

## The floor, never traded away

- Contrast holds: 4.5:1 for text, 3:1 for interface edges.
- Targets are big enough to hit; text survives 200% zoom.
- Motion respects the reduced-motion setting.
- Every control carries a name a screen reader can read.
- Verify the floor before calling anything done — one pair under it and it isn't handed over.

## Bad practice — the tells

- Motion as decoration — a fade-slide-up on every card; animate only in answer to an action.
- The generated look — identical rounded cards, tracked ALL-CAPS eyebrows, a spaced em dash everywhere.
- Decoration that says nothing — a divider separating nothing, an eyebrow added just to look structured.
- Boldness spread thin — one memorable move beats five quiet ones; take an accessory off.
- Lifted wholesale — a reference is fuel for your own work, never a thing to transplant directly.

## Assembling a screen

- Say the screen's job in one sentence; a job that won't fit in one is two screens.
- Pick the one thing that dominates — everything else supports it or goes.
- Settle behaviour over time: loading, empty, failure, and the moment right after an action.
- Take it to its edges: narrow width, long text, zero items, three hundred items, a slow network.
- Connect it to what already exists — where someone arrives from, where they can go, how they get back.
- Consistency with the kit's existing screens beats a better idea for this one screen alone.

## What bad looks like, in a finished build

- No hierarchy — nothing is clearly first, or everything shouts at once.
- Not readable — contrast too low, text too small, lines too long, density crushing.
- Broken rhythm — arbitrary spacing, nothing aligned, gaps that differ for no reason.
- Templated — identical cards, ALL-CAPS eyebrows, an arrow after every link.
- No answer to an action — pressed, and nothing visibly happened.
- Layout jumps — an untouched element moves when something nearby loads, expands, or opens.
- A dead end — empty with nowhere to go, an error with no way out.
- Lying about state — a placeholder that reads as data, a disabled control that reads as live.
- Out of reach — targets too small to hit, no visible focus when moving by keyboard.
- Falls apart at the edges — narrow screen, long text, empty list, overfull list.
- Wrong words — system language, a button and its result named differently.
- Noise — motion for its own sake, one accessory too many.
