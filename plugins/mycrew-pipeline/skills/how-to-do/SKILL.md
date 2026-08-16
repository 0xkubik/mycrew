---
name: how-to-do
kind: intent
description: "Use when a task carries a real fork — a technical or implementation decision with materially different options and no obvious winner — or when picked directions need working out into something buildable. Returns ONE buildable approach, never a menu. The rigorous replacement for open-ended brainstorming. Triggers: \"how should we build this\", \"which approach\", \"weigh the options\"."
argument-hint: "<the fork or question to work through>"
---

**Load and follow `mycrew-pipeline:pipeline-rules` first — what follows holds on top of it.**

## Gate — this is an implementation fork

how-to-do works out **HOW to build something in code**. Confirm that before spending four poles:

- **Product direction** (what to build or where to go, not how) → `/what-to-do` or `/ask-me`.
- **Trivial & clear how** (one obvious way to implement) → straight to `mycrew-pipeline:do`.
- **A real implementation or architecture fork** — materially different ways to build it, no obvious
  winner → continue.

## The four poles

Two **orthogonal** axes, Speed⟷Quality and Reuse⟷BuildOwn. Keep each pole on its own: Speed argues
*less now*, not *reuse*; Reuse argues *proven and existing*, not *minimal*.

- **Speed** — fastest path to something working. Sacrifices robustness and completeness.
- **Quality** — the version you'd run in prod at 10× load. Sacrifices speed and present simplicity.
- **Reuse** — existing libraries and code, proven patterns, the codebase's own way. Sacrifices fit.
- **Build own** — bespoke, fit-to-purpose. Sacrifices predictability and speed.

## Step 1 — Frame the idea to build

State in one sentence **what is to be built** and the **decision that forks** it. Then the **criteria** —
what "best" means *for this decision* ("lowest time-to-first-working" vs "lowest 12-month maintenance"),
derived from the task, because Step 4 scores against exactly these. Also **list the project's files with
line counts** — `git ls-files | xargs wc -l` — as shared ground handed to every pole.

## Step 2 — Fan out (four partisan subagents, parallel)

One per pole, each on the **`sonnet` model**, handed the framed decision, its pole mandate and the file
list. **Each runs internally before answering:** strongest plan under its locked stance → self-attack
(where does *this* plan break?) → repair → emit:

```
pole/conviction: Speed | Quality | Reuse | BuildOwn — high | medium | low
                 # low = "this axis doesn't bite here" — say so, don't fake it
approach:        <concrete plan sketch under this stance>
core_bet:        <what it optimizes / the central wager>
sacrifices:      <what it deliberately gives up>
weakest_point:   <where it's most vulnerable — honest; synthesis reuses it>
cost:            <rough effort / complexity>
```

## Step 3 — Cross-evaluate the opposite

Four subagents again, each handed **its own proposal plus its axis-opposite's** (Speed⟷Quality,
Reuse⟷BuildOwn). Partisanship drops here — this is where the debate happens, opposite against
opposite — and each returns its **real** read:

```
pole/opposite: <your pole> against <the opposing pole>
steelman:      <the opposite's strongest point, put fairly — not a strawman>
concede:       [ where the opposite is genuinely right for THIS task ]
hold:          [ where your stance still wins — grounded reason, not partisan reflex ]
real_position: <your honest verdict now that you've weighed the opposite>
```

## Step 4 — Synthesize

One neutral pass, main thread, on your stronger model, over **all** outputs. Do **not** pick the nicest
proposal, **construct** the decision: what the poles agree on is the **robust core** and goes in; where
they genuinely disagree are the **live axes**, the real choices; score the survivors against the Step-1
criteria, weighting out any axis where conviction was uniformly low; then decide and say what it beat.

```
decision:            <the chosen *how* + a thin plan sketch: what won and why, never a build checklist>
robust_core:         [ <points that held across poles> ]
beaten_alternatives: [ { alternative, why_not } ]
assumptions:         [ { claim, confidence, kill_signal } ]  # kill_signal = FALSIFIABLE trip-condition
                     # ("the library buffers instead of streams"), never a vibe ("if it gets too big")
framing:             ok | reframe(<the *how* was mis-framed — redo Step 1>)
                     | flag_to_human(<the picked direction itself looks wrong — stop, do NOT build>)
```
