---
name: what-to-do
description: "Use when the next move is unclear and one must be picked — returns ONE ranked menu of moves drawn only from what the product plane already holds: an approved feature to carry, half-built work to finish, rough parts to rebuild, debt to pay down. Chooses among possible moves; it never invents a new capability."
argument-hint: "[optional focus — or nothing to survey the whole product]"
---

# what-to-do — pick the next move out of what the plane already holds

The run ends with **one ranked menu** of moves and nothing else: no code, no line added to the plane,
no capability invented that the human never approved.

## Steps

1. **Ground before you fan out.** `backlog milestone list` at the **product root**, read by the product
   layer's rule. Missing or empty → tell the human to ground the list there first. Present → the
   **frontier** (first milestone with work still open) is your steer. List every sub-project's files
   with line counts, paths from the Sub-projects list (never by scanning): `git -C <path> ls-files |
   sed "s|^|<path>/|" | xargs wc -l`. That list is shared ground handed to every lens.
2. **Fan out — four lenses in parallel.** One subagent per move on `sonnet`, each handed its mandate,
   the **North Star** if any, the approved list and the file list. ADD picks from the list; the others
   take the frontier as a steer, not a gate. Each returns candidates: ADD (unbuilt feature off the
   approved list; never one not on it), FINISH (started and never done — stubs, dead ends, partial
   flows), REBUILD (works but has a clearly better redo — must name the better way), REFACTOR (structural
   drag slowing everything else — real, never cosmetic). Each `move`, `title`, `what`, `why_now`,
   `goal_fit`, `effort`, `reversibility`, `advances` (or `off-list`); empty lane → `empty_reason`.
3. **The menu — one pass, main thread.** **Merge before you rank** — a FINISH and a REBUILD on the same
   thing are one candidate. **Score goal-fit against effort**, weighing reversibility more once the
   product is **live**; pre-production is carte blanche. **The frontier biases, it never filters** —
   advancing it boosts a candidate, off-list is never dropped for being off-list. **Nothing disappears
   quietly** — a strong candidate ranked low by production-caution or features-fit stays on the menu with
   the reason it ranked there.

## Done

- **One ranked menu** of moves, greatest first, each with its score (`goal_fit / effort /
  reversibility` and what moved the rank).
- **Nothing invented.** Every candidate comes off the approved list or existing work; no new capability
  is proposed.
