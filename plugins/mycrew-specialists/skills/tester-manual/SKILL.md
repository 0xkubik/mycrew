---
name: tester-manual
description: "Use when the human explicitly asks for a manual pass on the milestone's visual surface, after automated tests pass — never on the tester's or lead's own initiative, since it drives their real screen with computer-use. Walks the real frontend as a person would and reports what works, what breaks, and what got fixed in place."
argument-hint: "<the milestone / UI to test>"
---

# tester-manual — exercise the visual surface by hand

Runs at the very end of the milestone, only when it carries a visual part and the human has explicitly
asked for this pass. Automated tests have already passed; now the real screen is opened as the human
would use it and walked through, eyes on the result, not the code.

## What to do

- **Open the real UI and use it as a person would.** Load the frontend, walk the flows the milestone
  built — not a checklist of code paths, but the screens and interactions a user actually meets.
- **Check the visual surface, not the code.** Layout, spacing, states, edge input, the look against the
  product's design — what a test of internal logic cannot see.
- **Fix small things in place.** A broken look, a dead interaction, a mis-wired control — fix it now and
  note it.

## Never

- Start this pass on your own — it drives the human's real screen with computer-use; only they trigger
  it, never the tester's or lead's own initiative.
- Patch around a real design disagreement or a flow that needs the plane to move — flag it for the
  lead instead.

## Report

Plain lines back to the lead: what you exercised, what works, what you fixed, what remains open. The
milestone is done only when this pass (where it applies) is clean or its open items are named.
