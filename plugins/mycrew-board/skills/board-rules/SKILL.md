---
name: board-rules
kind: rule
description: "Use whenever work is put on the board or moved across it — the one rule set for tasks: who owns the board, what every task carries, whose requirement it records, and which tasks must be gated before anyone is sent to build them. Rules only: never how the work itself is done."
user-invocable: false
---

# board-rules — the lead's board, and what a card must say

The plane says what the product must be; the board says what is being done about it **right now**.
The board is `backlog.md` at the product root, its CLI owns the files, and **the lead owns the board**.

## Whose board it is

- **Only a lead creates, edits or moves a card, and only on its own feature.** One writer per feature
  is what keeps the board true; a board four kinds of author can touch describes nothing after a day.
- **The chief never touches the board.** It hands a lead what its feature must become, in words, and
  the lead turns that into cards. A chief writing cards is a chief holding a feature, and that seat
  belongs to somebody else.
- **A worker never touches the board.** What it found and did not do comes back in its report; the lead
  decides whether that becomes a card at all.
- **Never edit a task file by hand — every change goes through `backlog`.** Sections are delimited by
  markers the CLI writes and reads; a hand-edited file loses its relationships and its history, and
  nothing warns you.

## What every card carries

- **An origin label naming whose requirement it is, not whose hand wrote it.** The lead writes them
  all; the label says where the work came from — `from-human`, `from-chief`, `from-lead`,
  `from-worker`. Recorded when the card opens or never recoverable.
- **A chief's instruction is the human's.** The chief speaks for them, so `from-chief` is never gated
  and never argued with — that question was settled before it reached the board.
- **A milestone naming the feature it serves.** A card belonging to no feature is work aimed at
  nothing, and that is the kind that swallows a week.
- **Acceptance criteria someone other than the executor can check.** Vague enough to argue about is
  vague enough to never finish.
- **A definition of done wherever the work can sprawl.** Edge cases, states, polish — the boundary is
  set before the work starts, or the work sets its own and never stops.

## What must be gated before anyone builds it

- **`from-lead` and `from-worker` cards are gated; `from-human` and `from-chief` are not.** Work an
  agent thought up is the work most likely to be a symptom, a nicety, or the fourth lap of the same
  problem.
- **The gate runs when the card is about to be dispatched, not when it is written.** Writing a card
  costs nothing and keeps the thought; sending a worker is what spends the day.
- **`mycrew-crew:worth-doing`, in a subagent, and it returns in one word.** DO — dispatch it. DROP —
  close the card with the reason it gave. ASK — it goes to the chief, and the card waits.
- **A gated card is labelled `gated` once it passes.** A card re-dispatched after a BACK is the same
  work and is never gated twice.
- **A worker's finding that belongs to the card it came from is not a new card.** Same problem, same
  scope, still unfinished — the work goes on. Anything else opens a card marked `from-worker` and waits
  its turn like the rest.

## How a card moves

- **In Progress means a live worker holds it right now.** A card in progress with nobody working it is
  the board's worst lie: the work looks owned and is not.
- **The lead moves a card to Done, never the worker who built it**, and only when every acceptance
  criterion is checked and the definition of done is met. Nobody rules on their own work.
- **A blocked card says what blocks it, and the blocker is a card too.** Blocked-and-silent is
  indistinguishable from abandoned.

## What the board is not

- **The board is not the plane.** What the product must be lives in `docs/product/`; the board holds
  only what is being done about it. A feature is never invented on the board.
- **The board is not a report.** Nothing is written on a card for someone to read later — a card
  describes work that exists, and closed work is closed, not narrated.
