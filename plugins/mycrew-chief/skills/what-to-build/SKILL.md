---
name: what-to-build
description: "Use when the product needs ideas it doesn't hold yet — invent candidate features and improvements, pitch each to the human with the case for it, and on their approval file it into features.md. Every idea, approved or rejected, is logged with their reason in docs/features/ideas/ and binds every later pitch. Sibling of what-to-do: that one picks among existing moves, this one invents new ones."
argument-hint: "[an angle to invent along — or nothing to range across the whole product]"
---

# what-to-build — invent the next capability, pitch it, keep the verdict

The **one place the chief has product ideas of its own**. You invent — features and improvements the
product plane doesn't hold yet — and put each to the human with the case for it. You **never decide**:
only their approval puts a line in `features.md`, and every verdict, yes or no, is written down and
binds what you pitch next. Everything you touch sits at the **product root**.

## Rules & concepts — non-negotiable

- **Ground before you invent.** Read the North Star in the root `CLAUDE.md`, `docs/features/features.md`,
  the architecture and the specs, the whole ideas ledger — then look at what the sub-projects actually
  are. An idea that restates something already listed, already built, or already pitched is not an idea;
  find a real gap.
- **The ledger binds you.** A rejected idea is **never** re-pitched. The one exception: something
  material changed since — the product moved, the reason no longer holds — and then the pitch opens by
  naming exactly what changed. Read `docs/features/ideas/ideas.md` every run, before the first pitch.
- **Serve the North Star, not novelty.** Every idea must close a real gap between what the product is
  and where it's going. Inventing to have something to say is the failure mode — a run that honestly
  finds nothing left worth pitching says so and stops.
- **One idea at a time.** Pitch it, take the verdict, file it, then the next — never a menu of five.
  (Ranking what the plane already holds is `what-to-do`; this is the other job.)
- **Pitch in plain human language.** Say what it is and *why it's worth doing* — the gap it closes, who
  it helps, what it costs — before you ask. No jargon: the human decides on the case, not on your
  vocabulary. Put the question itself through `AskUserQuestion`.
- **Approval is the only door into the feature list.** An approved idea becomes one `- [ ]` line of
  **≤200 chars** in `docs/features/features.md`, in their intent, by the
  `mycrew-product:feature-management` rules. Nothing else ever reaches that file — and `--auto` does
  not approve on the human's behalf; without their word, this skill does not run.
- **Every verdict, both halves, always.** A verdict lands in **two** places: one line in
  `docs/features/ideas/ideas.md` and a full dossier at `docs/features/ideas/history/<slug>.md`. A
  rejection is filed exactly as carefully as an approval. An idea pitched but not logged never happened.
- **The reason is the human's, in their words.** Record why they said yes or no as *they* put it, never
  your reconstruction of it. Answered with no reason → ask for the reason before you file.
- **Append, never rewrite.** Ledger lines and dossiers are permanent. An overturned verdict is a **new**
  verdict block and a **new** ledger line — never an edit to the old one.
- **Strictly the template shapes.** `ideas.md` is the `example.ideas.md` shipped beside this skill; each
  history file is `example.idea.md`. Missing folder or files → seed them from the templates.
- **English.** Files, titles, prose — all English, whatever language the pitch was spoken in.

## Litmus

Ask before every pitch: *would this idea survive the human asking "why now?"* — and after every
verdict: *is it in both the ledger and history, with their reason?* Either answer is no → you're not done.
