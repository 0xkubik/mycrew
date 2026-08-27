---
name: warden-rules
kind: rule
description: "Use whenever a session is being watched — the one rule set for what earns a look, what earns a stop, and what every verdict leaves behind on disk. Fixes the two thresholds that keep a watch useful, what a flag must carry, and which file each kind of record belongs in. Rules only: never who watches or how a verdict is reached."
---

# warden-rules — what is watched, what is stopped, what is written down

A watch is worth having only while both of its thresholds hold: it must see nearly everything and stop
almost nothing. Whatever survives in the log is the whole of what the watch knows about itself — after a
compaction there is nothing else left. What each trigger earns is `policy.md` and the shapes to fill
in are `templates.md`, both beside this file.

## The two thresholds move in opposite directions

- **Waking is cheap, so wake wide.** An event nobody acts on costs a glance and no human attention; widen
  what wakes the watch until it is confident nothing real slips past.
- **A stop is expensive, so stop narrowly.** It spends the attention the watch exists to save, and a
  handful of false stops is all it takes for the human to start ignoring the watch or kill it.
- **The stop threshold only ever comes down, and only on a precedent.** The human ruling that something
  should have been caught is the one thing that lowers it; nothing is added on a hunch.

## What is never watched

- **Never your own session.** Your reasoning about a session is not evidence about that session.
- **Never a project you were not pointed at.** The transcript directory you were handed is the boundary.
- **Never a subagent's own traffic.** What it was dispatched to do was already judged when it was
  dispatched; judging its internals second-guesses work nobody handed you.

## What a flag must carry, and what it must not

- **A flag names the work, the goal it no longer serves, and nothing else.** Those two facts are the
  whole message; anything past them is advice, and advice is not what a flag is for.
- **A flag stops one piece of work, never a session.** Everything that does not depend on the flagged
  work goes on running while it is settled.
- **A tick in `policy.md` is a duty and a cross is a prohibition.** The table settles what follows a
  trigger; all that is ever weighed is which row the trigger belongs to.
- **An unanswerable flag is not a flag.** If you cannot say which goal is being missed, you have a
  feeling, and a feeling is not worth a human's attention.

## Where each record goes

- **Every wakeup is exactly one line in `journal.log`, skipped ones included.** One line, never two,
  never a paragraph: a wakeup with no line is indistinguishable from one nobody saw, and a wakeup with
  a page is a journal nobody reads back.
- **The line carries what happened, what was done or why nothing was, and what came of it.** "Nothing
  to say" is not a reason; the middle clause of a skip is where the watch proves it looked.
- **The flags on a line are the duties that fired, named as `policy.md` names them.** A line claiming a
  move with no tick in its row, or missing one that has it, is the watch drifting from its own policy.
- **A precedent is one line: the decision as a thesis, in the human's own vocabulary.** Their words
  compressed, never your summary of them — a paraphrase is the first thing to rot, and every later
  verdict leans on this file.
- **A flag that goes to a gate opens a case file, and the case closes with what actually happened.** The
  verdict alone is half a record: what the session did next is the half that can be checked.
- **Ids are permanent and never reused.** A case or precedent id points at one thing forever, in the
  journal line that made it and everywhere it is leaned on afterwards.
- **The cursor files belong to the watcher script.** Never write them by hand; they are what stops
  history from replaying as news.
