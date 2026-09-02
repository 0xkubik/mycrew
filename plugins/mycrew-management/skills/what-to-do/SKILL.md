---
name: what-to-do
kind: intent
description: "Use when the next move is unclear and one must be picked — returns ONE ranked menu of moves drawn only from what the product plane already holds: an approved feature to carry, half-built work to finish, rough parts to rebuild, debt to pay down. Chooses among possible moves; it never invents a new capability. Triggers: \"what next\", \"what should we do\", \"where do we go from here\"."
argument-hint: "[optional focus — or nothing to survey the whole product]"
---

# what-to-do — pick the next move out of what the plane already holds

The run ends with **one ranked menu** of moves and nothing else: no code written, no line added to the
plane, no capability invented that the human never approved.

## Gate — ground before you fan out

- **The approved list is the ground.** `backlog milestone list` at the **product root**, read by
  `mycrew-product:product-rules`. Missing or empty → tell the human to run `/ask-me` there first; it
  grounds the list. Present → the **frontier**, the first milestone with work still open, is your steer.
- **Every sub-project's files, with line counts.** Take the paths from the Sub-projects list, never by
  scanning, and run per path: `git -C <path> ls-files | sed "s|^|<path>/|" | xargs wc -l`. That list is
  shared ground handed to every lens.

## The fan-out — four lenses, in parallel

One subagent per move, each on the **`sonnet` model**, handed its mandate, the **North Star** if there
is one, the approved list and the file list. ADD picks from the list; the others take the frontier as a
steer, not a gate. Each explores its own lane and returns candidates in the contract below.

- **ADD takes an unbuilt feature off the approved list and argues why this one before the others.**
  Never a capability that isn't on the list — inventing is the product layer's job, not yours. Nothing
  unbuilt left is a real empty lane, not a prompt to make something up.
- **FINISH takes what was started and never carried to done.** Stubs, dead ends, partial flows,
  dangling TODOs.
- **REBUILD takes something that works and has a clearly better redo.** It must name the better way,
  not just call the current one ugly.
- **REFACTOR takes structural debt that is slowing everything else.** Real drag, never cosmetic nits.

**Each lens returns** (0–N candidates):

```
move:          ADD | FINISH | REBUILD | REFACTOR
candidates:    [ {
  title:         <short name>
  what:          <1–2 sentences: the concrete move>
  why_now:       <how it closes the gap to the North Star>
  goal_fit:      high | med | low
  effort:        S | M | L
  reversibility: easy | hard
  advances:      <frontier feature it advances | "off-list">   # only if the milestone list is non-empty
} ]
empty_reason:  <if candidates == [] : why this lane has nothing real here>
```

## The menu — one pass, main thread

- **Merge before you rank.** A FINISH and a REBUILD on the same thing are one candidate, not two.
- **Score on goal-fit against effort**, weighing reversibility more once the product is **live**;
  pre-production is carte blanche.
- **The frontier biases, it never filters.** Advancing it boosts a candidate; off-list is never dropped
  for being off-list.
- **Nothing disappears quietly.** A strong candidate ranked low by production-caution or features-fit
  stays on the menu with the reason it ranked there.

```
rank:      <n>
move:      ADD | FINISH | REBUILD | REFACTOR
title:     <direction>
what:      <1–2 sentences>
why_now:   <gap it closes toward the North Star>
score:     goal_fit / effort / reversibility  (+ any adjustment that moved the rank)
```
