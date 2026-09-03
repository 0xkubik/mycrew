---
name: reviewer-review
description: "Run three parallel review lenses over the milestone's written code (the commits the coders made) — bugs, code cleanliness, security — with eyes that didn't write it. Then evaluate each finding, fix what is real, name what is rejected or deferred. Runs after all implementation is committed, before testing."
argument-hint: "<the milestone / commits to review>"
---

# reviewer-review — three lenses over the milestone's commits, then judge and fix

Review the code the coders wrote across the milestone — scoped to their commits — with three subagents,
one per lens, in parallel, then evaluate and fix. The run ends with every accepted finding fixed, the
rejected and deferred ones named with reasons, and a report that accounts for all three lenses.

## Step 1 — launch the three lenses

Dispatch three subagents in parallel, each scoped to the **commits the coders made for the milestone**,
each with fresh eyes that didn't write it. Each returns findings in the same contract:

- **Bugs** — correctness, edge cases, error paths, wrong logic, races, leaks.
- **Cleanliness** — structure, naming, dead code, duplication, consistency with the codebase.
- **Security** — injection, broken access, leaked secrets, unsafe defaults, dangerous dependencies.

Nothing that executes (docs, comments, copy, config values) earns a scan; but themes above are never
skipped wherever actual code runs.

**Each lens returns** (0–N findings):

```
lens:    bugs | cleanliness | security
findings: [ {
  title:    <short name>
  where:    <file:line / function>
  what:     <the defect or improvable point, concrete>
  severity: high | med | low
  fix:      <the proposed correction>
  confidence: high | med | low   # how certain this is a real problem
} ]
empty_reason: <if findings == [] : why this lens is clean here>
```

## Step 2 — judge each finding

Evaluate every finding against the actual code — confirm it is real, not a false positive; weigh its
severity against the fix's cost and risk. Classify into three buckets:

- **Fix** — the finding is real and worth fixing. Fix it in place.
- **Reject** — false positive, or the "improvement" makes the code worse or invents unasked work.
- **Defer** — real but out of scope: a behavior fork the change can't settle, a redesign this task
  doesn't warrant. Name it, leave it, don't patch around it.

Never fix what the task did not ask for under cover of a finding. A deliberate bug-fix may change
wrong→right behavior; where a safety net pins the old expectation, update it.

## Step 3 — report

Account for all three lenses in one closing report:

- Per lens: what was found (the findings, with severity).
- What was **fixed**, what was **rejected** (and why), what was **deferred** (and why).
- Commit any fixes you made. Point the caller at the tester — automated testing is the next pass
  (tester-automated), not run here.
