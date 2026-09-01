---
name: board-rules
kind: rule
description: "Use whenever the board is read or written — the one rule set for the board itself: that the CLI owns the files, which columns exist, what every card must carry, and where the board's authority stops. Rules only: what each role may do to a card is a skill of its own beside this one."
user-invocable: false
---

# board-rules — the board itself, and what a card must say

The plane says what the product must be; the board says what is being done about it **right now**. It
is `backlog.md` at the product root, and it carries work that exists — never a plan, never a report,
never a second copy of the plane. What each role may do to a card is `mycrew-board:board-chief`,
`board-lead` and `board-worker`, beside this file.

## How the files are touched

- **Never edit a task file by hand — every change goes through the `backlog` CLI.** Sections are
  delimited by markers the CLI writes and reads; a hand-edited file loses its relationships and its
  history, and nothing warns you.
- **Read with `--plain`.** The board's own views are drawn for a human at a terminal; an agent reading
  them is reading a picture of the truth instead of the truth.
- **The cards live in the repository and travel with the work.** They are committed like anything else
  and never sent to `.gitignore`; a board that exists only on one machine is not a board.

## The columns

- **Three columns and no more: `To Do`, `In Progress`, `Done`.** What may be dispatched is settled by
  a card's origin label and the gate it earns, never by which column it sits in; a column that
  duplicates a label is one more thing to keep in step.
- **`In Progress` means a live worker holds it right now.** A card in progress with nobody working it
  is the board's worst lie: the work looks owned and is not.
- **A blocked card says what blocks it, and the blocker is a card too.** Blocked-and-silent is
  indistinguishable from abandoned.

## What every card carries

- **An origin label naming whose requirement it is, not whose hand wrote it.** `from-human`,
  `from-chief`, `from-lead`, `from-worker` — recorded when the card opens or never recoverable. What
  each one earns is the role skills' business, and the whole reason the label exists.
- **A milestone naming the feature it serves.** A card belonging to no feature is work aimed at
  nothing, and that is the kind that swallows a week.
- **Acceptance criteria someone other than the executor can check.** Vague enough to argue about is
  vague enough to never finish.
- **A definition of done wherever the work can sprawl.** Edge cases, states, polish — the boundary is
  set before the work starts, or the work sets its own and never stops.

## What the board is not

- **The board is not the plane.** What the product must be lives in `docs/product/`; the board holds
  only what is being done about it. A feature is never invented on the board.
- **The board is not a report.** Nothing is written on a card for someone to read later — a card
  describes work that exists, and closed work is closed, not narrated.
