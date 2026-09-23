---
description: "Set a recurring check-in that wakes the chief on a fixed interval to make sure delegated work hasn't stalled, until the human's stated goal is actually done."
argument-hint: "<interval, e.g. 30m or 2h> [the goal, if not everything currently delegated]"
---

# /watch — keep checking that delegated work is moving

Argument: an interval — `30m`, `2h`, that shape. Also take whatever goal the human states in the same
call; if none is given, the goal is everything currently delegated reaching completion.

## Steps

1. Turn the interval into a cron expression, off the round minute — a bare `:00`/`:30` fires at the same
   instant as everyone else's. `30m` → `7,37 * * * *`; `2h` → `13 */2 * * *`; scale the same way for
   other spans.
2. `CronCreate` with that schedule and a prompt that repeats the goal and says: check every lead and
   every directly-dispatched specialist still running. Stalled means no report, no progress, gone idle
   with nothing sent back. Deal with what's stalled — nudge it, reassign it, or tell the human if it's
   beyond you — before ending the turn.
3. Each firing: if the goal is now actually done, `CronDelete` this job and say so to the human. If not,
   just end the turn — the same schedule fires again on its own.

## Know before you set it

- The job lives only in this session — gone the moment the session ends, nothing survives on disk.
  This outlives idle time, not a crash or a closed session.
- A recurring job auto-expires after 7 days regardless of the goal. Past that, `/watch` again if the
  goal still isn't done.
