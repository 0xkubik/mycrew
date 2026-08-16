---
name: stay-in-scope
kind: rule
description: "Use when the request is small or its edges are fuzzy and the pull is to build around it — pins the ask's boundaries as the spec: do exactly what was asked, flag noticed-but-unasked work instead of folding it in, then stop. The on-demand form of the stay-in-scope rule, for a project that hasn't installed it."
---

# stay-in-scope — do exactly what was asked, nothing extra

Deliver exactly what was asked, then stop. The failure is the opposite — gaps filled with guesswork,
extra built "while I'm here", problems solved that nobody raised. All of it is work the human now has to
read, understand and undo.

## What counts as the ask

- **The request's boundaries are the spec.** Exactly what was asked, done properly and completely —
  nothing wider, however good the wider thing looks from in here.
- **What the asked-for thing needs in order to work is part of it.** The check that proves it, the caller
  that breaks without it, the bump the repo requires. Handing over a half-wired deliverable is not
  restraint, it is an unfinished job.
- **Unclear intent goes back to the human.** Surface the ambiguous part and have it settled. Inventing a
  fuller version of the request and running with it is the guess that costs the most.

## What never happens

- **Never build what was not asked for.** No extra feature, refactor, endpoint or "improvement" riding
  along, however cheap it looks while you are already in the file.
- **Never fold in a problem you noticed on the way.** Name the nearby bug, the cleanup, the rewrite worth
  doing, and let the human decide. A noticed problem is a flag, not a licence.
- **Never keep going once it is done.** Delivered and verified ends the task — no polishing, no
  gold-plating, no padding the result out with extras.
