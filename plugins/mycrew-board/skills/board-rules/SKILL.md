---
name: board-rules
kind: rule
description: "Use whenever work is put on the board or moved across it — the one rule set for tasks: what every task must carry, who may create one and who must approve it, what each column means and who moves a card into it. Rules only: never how the work itself is done."
user-invocable: false
---

# board-rules — what a task carries and how it moves

The plane says what the product must be; the board says what is being done about it **right now**. A
card is the only place work exists — anything being built without one is work nobody agreed to, and
anything on the board that nobody is building is a lie about the state of the product.

The board is `backlog.md` in the product root. Its CLI owns the files.

## What every task carries

- **Never edit a task file by hand — every change goes through `backlog`.** Sections are delimited by
  markers the CLI writes and reads; a hand-edited file loses its relationships and its history, and
  nothing warns you.
- **An origin label, always: `human-asked` or `agent-proposed`.** This is the one fact that decides
  whether the task is questioned, and it can only be recorded when the task is written, never
  reconstructed later.
- **A milestone naming the feature it serves.** Features come from the plane; a task belonging to none
  is work aimed at nothing, and that is exactly the kind that swallows a week.
- **Acceptance criteria that someone other than the executor can check.** Vague enough to argue about
  is vague enough to never finish.
- **A definition of done wherever the work can sprawl.** Edge cases, states, polish — the boundary is
  set before the work starts, or the work sets its own and never stops.

## Who creates, who approves

- **A task the human asked for goes straight to the board and is never questioned.** They said it; that
  settles why.
- **A task an agent thought of opens as `agent-proposed` and waits for approval.** Nothing agent-born
  is worked before someone allows it, however obvious it looks from inside the work that spawned it.
- **The cheap check first: which feature on the plane does this advance?** None → it does not go on the
  board; take it to the human. Unclear → `agent-warden:why-do-it` decides. Clear → approve it and move on.
- **Only the chief approves an agent-proposed task.** They own the plane and are the only one who can
  say the work belongs to it.
- **Widening your own brief is a new task, not more of the current one.** A nearby bug, a better
  structure, a state nobody asked for — it opens a card with your name on the origin and you carry on
  with what you were given.

## How a card moves

- **In Progress means a live session is holding it right now.** A card in progress with nobody working
  it is the board's worst lie: the work looks owned and is not.
- **Done requires every acceptance criterion checked and the definition of done met.** Not "it works",
  not "close enough" — the boxes were written so that finishing is a fact rather than a feeling.
- **Nobody moves a card they do not hold.** The exception is the chief, who may pull anything back and
  say why.
- **A blocked card says what blocks it, and the blocker is a card too.** Blocked-and-silent is
  indistinguishable from abandoned.

## What the board is not

- **The board is not the plane.** What the product must be lives in `docs/product/`; the board holds
  only what is being done about it. A feature is never invented on the board.
- **The board is not a report.** Nothing is written on a card for someone to read later — a card
  describes work that exists, and closed work is closed, not narrated.
