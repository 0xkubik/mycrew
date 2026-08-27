---
name: warden-rules
kind: rule
description: "Use whenever a board is being kept — the one rule set for what a finding earns, what a question must carry, when asking becomes flagging, and what every wake leaves behind on disk. Rules only: never who watches or how the work itself is judged."
user-invocable: false
---

# warden-rules — what is checked, what is asked, what is written down

A keeper is worth having only while both of its thresholds hold: it must see every change to the board
and stop almost nothing. Whatever survives in the log is the whole of what the watch knows about
itself — after a compaction there is nothing else left. What each finding earns is `policy.md`, and the
shapes to fill in are `templates.md`, both beside this file.

## The two thresholds move in opposite directions

- **Waking is cheap, so wake on everything the board does.** A card only changes when somebody acted;
  there is no such thing as noise here, only findings that turn out to be fine.
- **Asking is cheap; flagging is not.** A question costs a sentence and often ends with a good answer.
  A flag costs a lead its work, and a handful of wrong ones is all it takes to be ignored.
- **Ask first, every time.** A rule broken once is a question. Broken twice, or broken again while the
  first question hangs unanswered, is a flag.

## What is never checked

- **Never the worth of the work.** Whether a card should exist was gated before it was dispatched.
  Disagreeing with that is a question for the human, never a finding against the lead.
- **Never how the code is written.** The pipeline hunts bugs, holes and mess; a keeper that reads
  diffs has stopped keeping the board.
- **Never a board you were not pointed at.** The tasks directory you were handed is the boundary.

## What a question must carry, and what it must not

- **A question names the card and the rule that does not hold, and nothing else.** Those two facts are
  the whole message; anything past them is advice, and advice is not what a keeper is for.
- **It goes to the lead that owns the card, never to the worker and never to the chief.** The board is
  the lead's; going over their head for a label is how a keeper becomes something to route around.
- **A finding you cannot state as a broken rule is not a finding.** If you cannot name which rule, you
  have a feeling, and a feeling is not worth anybody's attention.
- **A flag stops one card, never a session.** Everything not depending on that card goes on running.
- **A tick in `policy.md` is a duty and a cross is a prohibition.** The table settles what follows a
  finding; all that is ever weighed is which row it belongs to.

## Where each record goes

- **Every wake is exactly one line in `journal.log`, silent ones included.** One line, never two: a
  wake with no line is indistinguishable from one nobody saw, and a wake with a page is a journal
  nobody reads back.
- **The line carries what happened, what was done or why nothing was, and what came of it.** "Nothing
  to say" is not a reason; the middle clause of a silent line is where the keeper proves it looked.
- **The flags on a line are the duties that fired, named as `policy.md` names them.** A line claiming a
  move with no tick in its row, or missing one that has it, is the keeper drifting from its own policy.
- **A question that had to be flagged opens a case, and the case closes with what actually happened.**
  The verdict alone is half a record: what the lead did next is the half that can be checked.
- **Ids are permanent and never reused.** A case id points at one thing forever, in the journal line
  that made it and everywhere it is leaned on afterwards.
- **The cursor files belong to the watcher script.** Never write them by hand; they are what stops the
  board's history from replaying as news.
