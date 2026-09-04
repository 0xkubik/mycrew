---
name: designer-design
description: "Use when the designer is about to draw or refine a piece of the UI kit. Grounds and self-checks kit work — tokens and one component at a time, never a whole page."
argument-hint: "<the kit piece being designed>"
---

# designer-design — how the kit gets its shape

Adapted from frontend-design for kit work: no hero, no page composition, no whole-screen story —
only tokens and one component's anatomy at a time. Read before the first line of markup or CSS.

## Ground the choice

- **Let the product's subject drive the palette and voice.** A toy brand and a fintech dashboard
  should never share a kit — industry, audience, and material are where distinct choices come from.
- **Type carries personality.** One or two clearly distinct families, a real type scale, deliberate
  weight and line length (<80 chars). Drop the generated-page tells: one accented word in a headline,
  ALL-CAPS labels, an eyebrow label added just to look structured.
- **Structure encodes meaning, not decoration.** A divider, a number, a label says something about
  the content — number only when the content is actually a sequence.

## Motion, CSS only

- **Animate rarely, only in answer to a person's action** — opening, expanding, confirming. A
  fade-slide-up on every card or a hover transition on everything is the generic default, not a choice.
- **No JS framework in the kit** — transitions and keyframes only, never Framer Motion, Lottie, or
  GSAP; the coder has nowhere to wire them.

## Calibrate against the tells

Warm cream + serif + terracotta accent; near-black + one neon accent; broadsheet hairlines at zero
radius; the SaaS-card look — identical rounded cards under one shadow; template chrome — tracked
ALL-CAPS eyebrows, middle-dot meta strings, em-dash labels, near-black standing in for black, a
monospace face on small data, a trailing "→" on every link. None are wrong alone — they're wrong when
they're the default instead of a choice made for this brief.

## Tokens before layout

- **First pass is the token system, not a page.** Color (4-6 named hex), type roles, principles — the
  unit is a component's anatomy and states (hover, focus, active, disabled, empty, error), not a screen.
- **Watch CSS specificity.** A type selector and an element selector (`.section`, `.cta`) can cancel
  each other out, most often in the space between components.
- **Spend boldness once.** One memorable move, everything else quiet. Hit the floor without
  announcing it — responsive, visible keyboard focus, reduced motion respected, contrast that holds.
  Screenshot your own work as you go; it catches what reading the CSS won't.

## Copy is a kit component too

- **Write error and empty states in the interface's voice** — what happened, what to do next, never
  apologetic, never vague.
- **One name for one action, everywhere.** A button that says "Publish" produces a toast that says
  "Published" — the vocabulary is how someone learns the product.
