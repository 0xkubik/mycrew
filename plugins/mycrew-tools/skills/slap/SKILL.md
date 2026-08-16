---
name: slap
kind: intent
description: "Use when a fix has stopped working and more of the same is being tried — three failed attempts, the same error returning, the debugging going in circles. Forces a hard reset: the failed approach is abandoned and the run ends with two or three fundamentally different ones for the human to pick, and no code written. Not a debugging method (that's systematic-debugging) but the circuit breaker for one that failed. Triggers: \"slap\", \"you're going in circles\", \"stop, rethink this\"."
argument-hint: "[optional context about the bug]"
---

# slap — drop the failed approach and come back with different ones

You have been slapped. The fix you keep pushing has failed often enough that more of it is waste, and
the way out is not another variation of it. This run ends with that approach abandoned and real
alternatives on the table for the human. It changes no code.

## What the run ends with

- **Two or three fundamentally different approaches, each with its cost.** Different means it fails for
  a different reason than the last one did. A variation of what already failed is not an alternative.
- **Nothing in the repository touched.** A slap produces a proposal; the human picks, and building the
  pick is the next task, not this one.

## How it runs, in this order

- **Check that something actually failed.** No approach has been tried yet → say so and work the problem
  normally. There is nothing to reset, and a slap on an untried problem just burns a turn.
- **State the problem in one sentence.** What you are trying to achieve, and what happens instead.
- **List what you already tried, and why each attempt failed.** Honestly. The attempt written up as
  "almost worked" is the one that gets quietly tried again.
- **Question the assumption underneath all of them.** Right file, right layer, right service? Root cause
  or a symptom pointing elsewhere? Fighting the framework instead of using it? A version or config
  mismatch you have been reading past?
- **Look outward before proposing anything.** How this project already solves the same problem, what the
  tool's own documentation says rather than a forum answer about it, whether something already exists
  that does this.
- **Put the alternatives to the human and stop.** The case for each, what it costs, which one you would
  take — then wait for the pick.

## What never happens

- **Never continue the approach that just failed.** One more patch, one more workaround, "let me try one
  more thing" with the parameters changed — that is the exact move this exists to stop.
- **Never offer alternatives that die the same way.** Two options resting on the same broken assumption
  are one option, and the run has produced nothing.
- **Never widen it into a redesign.** A slap resets the approach to one problem. Rewriting the module
  around it is a different task, and nobody asked for it.
