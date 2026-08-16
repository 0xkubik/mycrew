---
name: review
kind: intent
description: "Use when a change needs hunting for edge cases and correctness bugs before it ships — eyes that didn't write the code hunt AND rule; every confirmed finding is fixed in place, never handed up as a list. Security is its own pass (secure). Triggers: \"review this\", \"find bugs\", \"edge cases\"."
argument-hint: "[what to review — omit for the last change]"
---

# review — hunt edge cases and bugs; fix them

You hunt the change across **two axes — edge cases and bugs** — have each finding **ruled on by eyes
that didn't write it**, and **fix it yourself**. Security holes are a separate pass:
`mycrew-pipeline:secure`.

**Invariants — non-negotiable:**
- **The author never rules on his own code.** You dispatch the hunt and the verdict; you do not decide
  a finding isn't real because you remember meaning it that way.
- **Verify before you fix.** A finding is a hypothesis until it is confirmed to reproduce. A fix applied
  to a non-bug is a *new* bug. Triage through `superpowers:receiving-code-review` — no performative
  agreement.
- **Apply, don't report.** You make every fix yourself. A findings list handed up is a failure.
- **Bounded to the change** — the diff you were handed, not the whole repo.

---

## Gate — does the change earn a hunt

Judge **what actually changed**, never what the task was called. Nothing that executes — documentation,
comments, copy, a value in a config file → say so in **one line** and skip. Anything that runs — logic,
control flow, data handling, error paths, a build or deploy script → never skipped, however few the
lines. Unsure → hunt: a bug that ships costs more than a wasted pass.

---

## Step 1 — Fan out the hunts (parallel subagents)

Dispatch a subagent per axis in parallel, each on the **`sonnet` model**, scoped to the
change. Each hunts hard in its lane and returns findings in the contract below.

- **EDGE** — boundaries and the unexpected: empty / null / zero / one, off-by-one, overflow &
  truncation, unusual or malformed input, ordering & concurrency, partial failure & retries, resource
  exhaustion, timezone / encoding / locale.
- **BUG** — correctness: wrong logic, mishandled or swallowed errors, state / lifecycle mistakes, race
  conditions, wrong API contract, leaks. Use **`/code-review`** as this lane's eyes.

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

Empty-lane valve: a lane with nothing real says so — **inventing a finding to fill a slot is a bug.**

## Step 2 — Verify (adversarial, and not by you)

Each finding goes to a **fresh judge** — a subagent that never wrote this code and never sees your
account of what you intended, told to **refute it**: does the trigger actually reach the defect, or
is it guarded upstream? Confirmed means reproduced — a test, a trace, or a tight argument. Then, main
thread, dedupe overlaps across lanes and rank by severity. **False positives die at the judge, not at
the author's memory of the intent.**

## Step 3 — Fix (apply, never report)

Fix each confirmed finding yourself. A bug-fix deliberately changes wrong→right behavior; where a
safety net already pins the old expectation, update it to the corrected one.

- **Behavior/product fork** — the code's *intended* behavior is genuinely ambiguous ("what *should*
  this do?"), materially different options, no clear answer → **not yours to guess.** Never a human,
  never stop: flag it to the **chief** in your closing report and keep going. Standalone, no chief →
  note it in the report and close.
- **A fix with a genuine HOW fork** — materially different ways to fix, no clear winner, costly to
  reverse → `mycrew-pipeline:how-to-do`.
