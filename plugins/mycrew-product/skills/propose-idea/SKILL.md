---
name: propose-idea
description: "Use when the product needs an idea it doesn't hold yet — invent a candidate feature or improvement, pitch it to the human with the case for it, and file it into features.md only on their approval. Every idea, approved or rejected, is logged with their own reason in docs/product/ideas/ and binds every later pitch. The counterpart to /braindump and /ask-me: those draw the human's vision out, this one puts an idea of its own in."
argument-hint: "[an angle to invent along — or nothing to range across the whole product]"
---

# propose-idea — invent a feature, pitch it, keep the verdict

The **one place mycrew contributes a product idea of its own**. Everywhere else the product plane is
strictly extractive — `/braindump` listens and `/ask-me` questions, and neither adds to it. Here you invent:
features and improvements the plane doesn't hold yet, each put to the human with the case for it. You
**never decide** — only their approval puts a line in `features.md`, and every verdict, yes or no, is
written down and binds what you pitch next. Run at the **product root**.

## Rules & concepts — non-negotiable

- **Ground before you invent.** Read the North Star in the root `CLAUDE.md`, `docs/product/features.md`,
  the architecture and the decisions, the whole ideas ledger — then look at what the sub-projects actually
  are. An idea that restates something already listed, already built, or already pitched is not an idea;
  find a real gap.
- **The ledger binds you.** A rejected idea is **never** re-pitched. The one exception: something
  material changed since — the product moved, the reason no longer holds — and then the pitch opens by
  naming exactly what changed. Read `docs/product/ideas/ideas.md` every run, before the first pitch.
- **Serve the North Star, not novelty.** Every idea must close a real gap between what the product is
  and where it's going. Inventing to have something to say is the failure mode — a run that honestly
  finds nothing left worth pitching says so and stops.
- **One idea at a time.** Pitch it, take the verdict, file it, then the next — never a menu of five.
- **Pitch in plain human language.** Say what it is and *why it's worth doing* — the gap it closes, who
  it helps, what it costs — before you ask. No jargon: the human decides on the case, not on your
  vocabulary. Put the question itself through `AskUserQuestion`.
- **Approval is the only door into the feature list.** An approved idea becomes one `- [ ]` line of
  **≤200 chars** in `docs/product/features.md`, in their intent, in the shape
  `mycrew-product:product-view` sets (that skill's *extract, never contribute* stance governs the
  interview, not you — pitching is exactly your job). Nothing else ever reaches that file — never
  approve on the human's behalf, whatever else the session was told.
- **Every verdict, both halves, always.** A verdict lands in **two** places: one line in
  `docs/product/ideas/ideas.md` and a full dossier at `docs/product/ideas/history/<slug>.md`. A
  rejection is filed exactly as carefully as an approval. An idea pitched but not logged never happened.
- **The reason is the human's, in their words.** Record why they said yes or no as *they* put it, never
  your reconstruction of it. Answered with no reason → ask for the reason before you file.
- **Append, never rewrite.** Ledger lines and dossiers are permanent. An overturned verdict is a **new**
  verdict block and a **new** ledger line — never an edit to the old one.
- **Strictly the template shapes.** `ideas.md` is the `example.ideas.md` shipped beside this skill; each
  history file is `example.idea.md`. Missing folder or files → seed them from the templates.