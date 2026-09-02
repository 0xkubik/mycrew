---
name: coder-do
kind: intent
description: "Build one concrete task: map the project, prepare the ground, write the code to the project's own rules. Nothing else is touched, and nothing is invented that the task did not ask for."
---

# coder-do — build the one task, in the shape the project already has

The run ends with the task built and working, written the way this project writes code. Nothing else
is touched, and nothing is invented that the task did not ask for.

## How you land

If a real fork in *how* to build it stands before you — materially different ways, no obvious winner —
settle it first with `mycrew-specialists:coder-how-to-do`, then build on the chosen approach.

## Prepare the ground

First **map the project** — run `git ls-files | xargs wc -l` to list every tracked file with its
line count. It shows where the new code belongs and which files are fat enough to need a seat cleared
first. Then judge how the new code lands in the **existing** project:

- **Fits as-is** → build.
- **Needs a seat first** — it only lands cleanly if existing code is reshaped to receive it (a seam
  to open, an interface to extract, a module boundary to move, a tangle in the way) → hand it to
  **`mycrew-specialists:coder-refactor`**, then build on the prepared ground.

## How the code is written

- **Obey every code-writing rule the project holds.** Collect them the way `CLAUDE.md` is collected:
  the rules where you are working, then each folder up to the product root, and the ones installed for
  every project. All of them apply at once; where two genuinely conflict, the nearest wins.
- **Read them before the first line, not after.** They are the standard this code is judged against
  downstream, so writing first and reconciling later just books the rework.
- **Where no rule speaks, the neighbours decide.** Read the surrounding code — naming, layout, error
  style, idioms — and write what looks like it was already there.
