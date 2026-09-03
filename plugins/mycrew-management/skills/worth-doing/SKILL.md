---
name: worth-doing
description: "Lightweight gate run as a subagent before work from a lead or specialist is dispatched — reconsiders the proposal, then rules in one word: DO, DROP or ASK. Judges need, never how to build. Minutes, not a study."
argument-hint: "<the task to rule on>"
---

# worth-doing — is this work really worth doing?

Runs as its own subagent in front of work proposed by a lead or specialist. Reconsider the proposal
instead of taking it as given, then hand back **one word and one line**: DO, DROP or ASK. Nothing is
written to the board or the plane, no code. Speed is the point — this gate stands before every
agent-born task, and a slow one gets skipped and then protects nothing.

## Steps

1. **Reconsider the ask, then restate it.** Strip the solution off the proposal — most arrive as a
   solution in disguise ("add a cache", "rebuild the dashboard"). Drill what the ask is *for* — the goal
   behind it, the pain it eases — until it bottoms out on something that stands alone. That floor is
   the real task. If rethinking changes the proposal, say so in a line before ruling (correct, never
   design the replacement — building it is the coder's job).
2. **Read what it touches.** The task, the feature it names, what has already been done toward that
   feature. Nothing else — not the repo at large, not nearby improvements. A task naming no feature is
   already answered: DROP.
3. **Ask two questions, each answerable in a sentence.** What does the product gain if this ships? And
   is this treating a cause or covering a symptom? A task born of a fix that didn't hold, an error that
   came back wearing another name, or a case the last change missed is a symptom — doing this one buys
   another round of the same. A second visit to the same code within one feature is the loudest signal
   to look first.
4. **Weigh it, then rule.** With the real task named, weigh at least one other route to it — a smaller
   change, something already there, doing nothing. Then the verdict:
   - **DO** — it treats a cause and earns its place. One line on what the product gains.
   - **DROP** — it does not. One line why: no feature gains, the gain is smaller than the work, or it
     patches over something to be fixed properly.
   - **ASK** — you cannot settle it here. The work is large, the cause unclear, or it argues with the
     plane. Goes up with the question in a line; deeper argument is the chief's, never this gate's.

## Done

- **One word and one line**, back to whoever called the gate. Cheap when it is cheap: small, reversible
  work whose bad outcome costs an hour to undo is **DO** in one line — a gate that taxes every move is
  a gate that stops being called.
- **Uncertain is DROP, not DO.** Dropping a good task costs a re-raise; passing a bad one costs a week
  nobody planned.
