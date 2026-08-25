---
name: oversight-rules
kind: rule
description: "Use whenever a session is being watched — the one rule set for what earns a look, what earns a stop, and what every verdict leaves behind on disk. Fixes the two thresholds that keep a watch useful, what a flag must carry, and which file each kind of record belongs in. Rules only: never who watches or how a verdict is reached."
---

# oversight-rules — what is watched, what is stopped, what is written down

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
- **A move with no tick in `policy.md` is not available on that trigger.** The table is what the watch
  may do, not a summary of what it usually does.
- **An unanswerable flag is not a flag.** If you cannot say which goal is being missed, you have a
  feeling, and a feeling is not worth a human's attention.

## Where each record goes

- **Every trigger leaves one entry in the journal — silent verdicts included.** A trigger with no entry
  is indistinguishable from a trigger nobody saw, which is the one thing that must never be ambiguous.
- **A silent verdict still says why it was silent.** "Nothing to say" is not a reason and rots into
  nothing the moment it needs to be trusted.
- **A flag that goes to a gate opens a case file, and the case closes with what actually happened.** The
  verdict alone is half a record: what the session did next is the half that can be checked.
- **A precedent is the human's decision in the human's words.** Your paraphrase is what rots first, and
  it is the file every later verdict leans on.
- **Ids are permanent and never reused.** A case id points at one case forever, in the journal and in
  the precedent that came out of it.
- **The cursor files belong to the watcher script.** Never write them by hand; they are what stops
  history from replaying as news.
