---
name: do
kind: intent
description: "Use when ONE concrete, well-scoped coding task is ready to build autonomously — built to the code-writing rules the project itself holds, gathered up the tree the way CLAUDE.md is. Refuses vague or fork-laden tasks rather than guessing. Triggers: \"build this\", \"implement it\", \"just do it\"."
argument-hint: "<one concrete, well-scoped task>"
---

## Gate — clear how to build

Build only when it's clear **HOW**. Check before writing a line:

- **Carries a real fork** (materially different ways to implement, no obvious winner) →
  `mycrew-pipeline:how-to-do` to think it through first.
- **Vague** (you can't state the acceptance criteria) → clarify via `superpowers:brainstorming`.
- **Business/product fork** (money, legal, direction) → not yours; back to the human.
- **Trivial & clear** — one sensible way to build it → proceed.

## Prepare the ground

First **map the project** — run `git ls-files | xargs wc -l` to list every tracked file with its
line count. It shows where the new code belongs and which files are fat enough to need a seat cleared
first. Then judge how the new code lands in the **existing** project:

- **Fits as-is** → build.
- **Needs a seat first** — it only lands cleanly if existing code is reshaped to receive it (a seam
  to open, an interface to extract, a module boundary to move, a tangle in the way) → hand it to
  **`mycrew-pipeline:refactor`**, then build on the prepared ground.

## How the code is written

- **Obey every code-writing rule the project holds.** Collect them the way `CLAUDE.md` is collected:
  the rules where you are working, then each folder up to the product root, and the ones installed for
  every project. All of them apply at once; where two genuinely conflict, the nearest wins.
- **Read them before the first line, not after.** They are the standard this code is judged against
  downstream, so writing first and reconciling later just books the rework.
- **Where no rule speaks, the neighbours decide.** Read the surrounding code — naming, layout, error
  style, idioms — and write what looks like it was already there.