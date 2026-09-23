---
name: what-to-do
description: "Use when the next move is unclear and one must be picked — returns ONE ranked menu of moves drawn only from what the product plane already holds: an approved feature to carry, half-built work to finish, rough parts to rebuild, debt to pay down. Chooses among possible moves; it never invents a new capability. Three depths: med reasons alone, high sends each lens to its own subagent, max has the four argue before you decide."
argument-hint: "[optional focus — or nothing to survey the whole product] --depth med|high|max"
---

# what-to-do — pick the next move out of what the plane already holds

The run ends with **one ranked menu** of moves and nothing else: no code, no line added to the plane,
no capability invented that the human never approved.

## Step 1 — ground before you fan out

`backlog milestone list` at the **product root**, read by the product layer's rule. Missing or empty →
tell the human to ground the list there first. Present → the **frontier** (first milestone with work
still open) is your steer. List every sub-project's files with line counts, paths from the Sub-projects
list (never by scanning): `git -C <path> ls-files | sed "s|^|<path>/|" | xargs wc -l`. That list is
shared ground handed to every lens.

## Step 2 — run the four lenses, at the chosen depth

Four lenses, always the same four, each its own strongest candidates under its own stance:

- **ADD** — an unbuilt feature off the approved list; never one not on it.
- **FINISH** — started and never done: stubs, dead ends, partial flows.
- **REBUILD** — works but has a clearly better redo — must name the better way.
- **REFACTOR** — structural drag slowing everything else — real, never cosmetic.

ADD picks from the approved list only; the other three take the frontier as a steer, not a gate. Each
candidate carries `move`, `title`, `what`, `where` (the file or path that shows it — FINISH, REBUILD
and REFACTOR only; ADD has nothing built yet), `why_now`, `goal_fit`, `effort`, `reversibility`,
`advances` (or `off-list`); empty lane → `empty_reason`.

**`med` (default)** — no subagents. Reason through all four lenses yourself, one after another, on the
main thread.

**`high`** — spawn four subagents in parallel on `sonnet`, one per lens, each handed its mandate, the
**North Star** if any, the approved list and the file list, arguing only its own lane with no
knowledge of the others. Read their four candidate sets back; you alone weigh them, on the main thread.

**`max`** — spawn the same four subagents in parallel for round one. Once all four sets are in, send
each subagent the other three sets and have it argue against them and restate its own candidates in
light of their counters — parallel again, all four at once. Weigh the four second-round sets, not the
first round.

## Step 3 — the menu, one pass on the main thread

**Merge before you rank** — a FINISH and a REBUILD on the same thing are one candidate. **Score
goal-fit against effort**, weighing reversibility more once the product is **live**; pre-production is
carte blanche. **The frontier biases, it never filters** — advancing it boosts a candidate, off-list is
never dropped for being off-list. **Nothing disappears quietly** — a strong candidate ranked low by
production-caution or features-fit stays on the menu with the reason it ranked there.

## Done

- **One ranked menu** of moves, greatest first, each with its score (`goal_fit / effort /
  reversibility` and what moved the rank) and its anchor where it has one — a claim about existing code
  the human cannot check without redoing the scan is not a candidate.
- **Nothing invented.** Every candidate comes off the approved list or existing work; no new capability
  is proposed.
