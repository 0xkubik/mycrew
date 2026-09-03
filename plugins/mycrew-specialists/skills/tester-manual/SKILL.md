---
name: tester-manual
description: "Manual testing on the milestone's visual surface — exercised by hand/eyes against the real frontend after automated tests pass. Used only when the milestone has a visual part. Reports what works, what breaks, and routes findings."
argument-hint: "<the milestone / UI to test>"
---

# tester-manual — exercise the visual surface by hand

Run at the very end of the milestone, only when it carries a **visual part**. Automated tests have
already passed; now the real screen is opened as the human would use it and walked through. The run
ends with a clear account of what works and what does not.

## What to do

- **Open the real UI and use it as a person would.** Load the frontend, walk the flows the milestone
  built — not a checklist of code paths, but the screens and interactions a user actually meets.
- **Check the visual surface, not the code.** Layout, spacing, states, edge input, the look against the
  product's design — what a test of internal logic cannot see.
- **Fix small things in place.** A broken look, a dead interaction, a mis-wired control — fix it now and
  note it.
- **Flag what you cannot fix.** A real design disagreement, a flow that needs the plane to move → name it
  for the lead, never patch around a decision.

## Report

Plain lines back to the lead: what you exercised, what works, what you fixed, what remains open. The
milestone is done only when this pass (where it applies) is clean or its open items are named.
