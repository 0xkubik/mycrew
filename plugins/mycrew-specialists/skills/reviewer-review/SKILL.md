---
name: coder-review
kind: intent
description: "Hunt edge cases and correctness bugs across the change — eyes that didn't write the code hunt AND rule; every confirmed finding is fixed in place, never handed up as a list. Security is a separate pass (coder-secure)."
---

# coder-review — hunt edge cases and bugs; fix them

You hunt the change across **two axes — edge cases and bugs**, have each finding ruled on by eyes that
didn't write it, and fix it yourself. The run ends with every confirmed finding fixed in place and
nothing left as a note for somebody else.

## What earns a hunt

Nothing that executes — documentation, comments, copy, a value in a config file → skip. Anything that
runs — logic, control flow, data handling, error paths, a build or deploy script → never skipped,
however few the lines.

## The hunt — one subagent per axis, in parallel

Dispatch a subagent per axis, scoped to the change. Each hunts hard in its own lane and returns
findings in the contract below.

- **EDGE** — boundaries and the unexpected: empty / null / zero / one, off-by-one, overflow &
  truncation, unusual or malformed input, ordering & concurrency, partial failure & retries, resource
  exhaustion, timezone / encoding / locale.
- **BUG** — correctness: wrong logic, mishandled or swallowed errors, state / lifecycle mistakes, race
  conditions, wrong API contract, leaks.

**Each hunter returns** (0–N findings):

```
axis:      EDGE | BUG
findings:  [ {
  title:    <short name>
  where:    <file:line / function>
  what:     <the defect: input/state → wrong outcome>
  severity: high | med | low
  trigger:  <concrete input/condition that hits it>
  fix:      <the correction>
} ]
empty_reason: <if findings == [] : why this lane is clean here>
```

## The verdict

Each finding goes to a **fresh judge** told to **refute it**: does the trigger actually reach the
defect, or is it guarded upstream? Confirmed means reproduced — a test, a trace, or a tight argument.
Then, main thread, dedupe overlaps across the lanes and rank by severity.

## Fix what survived

Fix each confirmed finding yourself. A bug-fix deliberately changes wrong→right behavior; where a
safety net already pins the old expectation, update it to the corrected one.

- **A behavior fork stops nothing.** The code's *intended* behavior genuinely ambiguous → flag it to
  the chief in your closing report and carry on with the rest. Standalone, no chief → note it in
  the report and close.
