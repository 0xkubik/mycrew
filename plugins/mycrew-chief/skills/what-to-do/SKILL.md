---
name: what-to-do
description: "Use when the next move is unclear and one must be picked — returns ONE ranked menu of moves drawn only from what the product plane already holds: an approved feature to carry, half-built work to finish, rough parts to rebuild, debt to pay down. Chooses among possible moves; it never invents a new capability. Triggers: \"what next\", \"what should we do\", \"where do we go from here\"."
argument-hint: "[optional focus — or nothing to survey the whole product]"
---

## Gate — ground before you fan out

- **The features** — `docs/features.md` at the **product root**, the one approved list, each entry
  carrying its own detail. **Missing or empty → route to `/ask-me`** first (it grounds the feature
  list). Present → read the **frontier** (first unchecked `[ ]`) as the steer.
- **The design** — `docs/architecture/model.c4` and `docs/decisions.md`, also at the product root:
  what the system is shaped like and what has already been settled and why.
- **The file list** — every sub-project's tracked files with line counts. Take the paths from the
  Sub-projects list, never by scanning, and run per path:
  `git -C <path> ls-files | sed "s|^|<path>/|" | xargs wc -l`. Shared ground handed to every lens.
  Then fan out.

## Step 1 — Fan out (four subagents, parallel)

Dispatch four subagents in parallel, one per move, each on the **`sonnet` model**. Give each: its
**move mandate**, the **North Star** (if any), the **approved feature list** (ADD picks from it; the
others take the frontier as *orienting steer, not a gate*), the **design**, and the **file list**.
Each explores the sub-projects **in its own lane** and returns candidates in the contract below.

- **ADD** — an **unbuilt feature from the approved list**, ready to be carried now. _"Which unchecked
  `[ ]` is the right one to start, and why this one before the others?"_ You choose and argue among
  what the product plane already holds; **you never invent a capability that isn't on the list** —
  inventing is the product layer's job, not yours. Nothing unbuilt left → say so, that's a real empty
  lane, not a prompt to make something up.
- **FINISH** — half-built things to carry to done. _"What did we start and not finish?"_ Stubs,
  dead-ends, partial flows, dangling TODOs.
- **REBUILD** — working things with a clearly better redo. _"What works but we now know how to do
  properly?"_ Must name the better way, not just "it's ugly."
- **REFACTOR** — structural debt slowing everything else. _"Where is the mess expensive?"_ Real
  drag only, not cosmetic nits.

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
  advances:      <frontier feature it advances | "off-list">   # only if a features file exists
} ]
empty_reason:  <if candidates == [] : why this lane has nothing real here>
```

## Step 2 — Aggregate → the menu

One pass, main thread. Collect all candidates, then **dedupe/merge** overlaps (a FINISH and a
REBUILD on the same thing collapse to one) → **score** on goal-fit × effort, weighing reversibility
more if the product is **live** (pre-production → carte blanche) → **rank** into one ordered menu.
Features-fit is a bias: advancing the frontier boosts, **off-list is never dropped.** Drop nothing
silently — if a strong candidate ranks low from production-caution or features-fit, keep it and say why.

```
rank:      <n>
move:      ADD | FINISH | REBUILD | REFACTOR
title:     <direction>
what:      <1–2 sentences>
why_now:   <gap it closes toward the North Star>
score:     goal_fit / effort / reversibility  (+ any adjustment that moved the rank)
```
