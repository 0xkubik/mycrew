---
name: board-lead
kind: rule
description: "Use whenever a lead works where the product keeps a board — the feature's board is the lead's to run: every card is labelled by whose requirement it is, the agent-born ones are drafted and gated before a worker is spent, and no card moves except by the lead's hand. The board's own rule, installed in the product, already says what every card must carry; this says how a lead runs one."
user-invocable: false
---

# board-lead — the lead runs its feature's board

Your feature's board is yours to run. The human and the chief may open cards on it; nothing moves
across it except by your hand, and nothing reaches a worker until it has earned the trip.

## The cards you write

- **Label by whose requirement it is, never by whose hand wrote it.** Your own idea is `from-lead`; a
  worker's finding you decided to keep is `from-worker`; what the human or the chief told you stays
  theirs however much you reworded it.
- **Every assignment you dispatch exists as a card first.** A worker sent against something that was
  never written down leaves nothing behind that says what it was sent to do.

## The gate before a worker is spent

- **Agent-born work is created with `--draft`; `from-human` and `from-chief` work is a task straight
  away.** Work an agent thought up is the work most likely to be a symptom, a nicety, or the fourth lap
  of the same problem — and a worker that could set its own task and go do it is the loop this whole
  split exists to break.
- **The gate runs when the draft is about to be dispatched, not when it is written.** Writing a draft
  costs nothing and keeps the thought; sending a worker is what spends the day.
- **`mycrew-crew:worth-doing`, in a subagent, and it returns in one word.** DO — `backlog draft promote
  <id>`, then dispatch it. DROP — `backlog draft archive <id>` with the reason it gave. ASK — it goes
  to the chief, and the draft waits.
- **The promote is the pass — there is no second gate.** A task sent back to a worker after a BACK is
  the same work and is never re-examined.

## How a card moves

- **You are the only hand that moves a card on your feature.** One hand on status is what keeps the
  board's account of who holds what true; whoever opened the card has no say in where it sits.
- **You move a card to Done, never the worker who built it**, and only when every acceptance criterion
  is checked and the definition of done is met. Nobody rules on their own work.

## What you never do

- **Never touch another lead's board.** What your feature needs from theirs is a message to them, never
  a card you wrote on their milestone.
- **Never dispatch an agent-born draft that has not passed the gate.** Not for a small one, not for an
  obvious one — the ones that feel obvious are what the gate is for.
