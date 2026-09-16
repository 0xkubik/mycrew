---
name: coder-kit
description: "Use when a design spec from the designer (or a design handed straight to you) needs to become the product's real UI kit — actual components in the project's stack, with a Storybook story for every variant and state, desktop and mobile. This is the kit now; there is no separate file to keep in sync with it."
argument-hint: "<the spec to build from, or what changed since last time>"
---

# coder-kit — build the kit as real code

The kit lives in the product's own components now — nothing separate to redraw when they change,
because there is nothing separate. Storybook is how it gets browsed: every component, every state, both
viewports. This skill is how a design spec — most often the designer's `design/spec.md` — becomes that.

## Get the spec first

Handed a design straight from the human with nothing written up yet — spawn
`mycrew-specialists:designer` on it first (its `designer-import`), wait for the report, then build from
that. Never skip the designer's pass to save a step: breaking a design into bricks and judging it
against the craft floor is its job, not yours.

## First run vs an update

- **No Storybook in the project yet** — set it up with whatever the project's own frontend stack already
  uses (its framework, its build tool). Never introduce a second component framework to host it.
- **Storybook already wired** — this is an edit, not a rewrite. Work out which components the spec
  changed or added, touch only those.

## Building the components

- **One component, one file, the project's own way.** Match the neighbours: naming, folder, styling
  approach, prop conventions — nothing invented the spec didn't ask for. Run this alongside
  `coder-implement`'s own discipline — settle a real fork (styling approach, a library choice) in its
  step 1, open a seam first if one's needed, same as any other task.
- **Every state the spec lists gets built**, not just rest: hover, focus, disabled, loading, empty,
  error — whatever it carries over from `designer-craft`'s floor.
- **A repeat in the spec is a prop, not a copy.** Two variants of the same brick are one component with
  a variant prop, never two components.
- **Tokens wire in, never hardcode.** Colour, spacing, type scale from the spec become the project's own
  token mechanism — CSS variables, a Tailwind config, a theme object, whatever it already has — not
  literals sprinkled through the component.

## Building the stories

- **One story file per component, one story per state.** Desktop and mobile viewport for each, using
  Storybook's own viewport controls — never a hand-rolled iframe or a pair of screenshots.
- **Hostile content in the stories, not just the happy path.** A long label, an empty list, three hundred
  rows — whatever the spec called out as an edge.
- **No component without a story.** A kit member nobody can browse in isolation isn't in the kit yet.

## Before you call it done

- **Run Storybook and look.** Every story renders, no console error, no dangling class or missing token.
- **Commit your work** — components and stories together, so the reviewer can find both.

## Report

Same shape as `coder-implement`'s: what you built, the forks you settled, tools used, what you left
outside.
