---
name: pipeline-rules
kind: rule
description: "Use whenever a pipeline stage runs — how-to-do, do, refactor, review, secure, test. The stance every stage obeys on top of its own: judge yourself at the door and skip in one honest line, stay inside the change you were handed, fix what you find rather than report it, never rule on your own work, and hand back one line saying what ran or why it skipped. Only what is true of every stage; each stage's own bar, subject and method live in that stage."
user-invocable: false
---

# pipeline-rules — what holds for every stage of the pipeline

A stage is one pass over one change, run inside somebody else's piece of work. These hold for every
one of them. Whatever is true of only one stage is written in that stage and never here.

## What every stage does

- **Judge yourself at the door, and skip in one honest line.** Weigh what actually changed, never what
  the task was called. Each stage carries its own bar; unsure whether the change clears it → run it,
  because a problem that ships costs more than a wasted pass.
- **Stay inside the change you were handed.** The diff, not the repository. Work this change genuinely
  warrants is inside it; everything else you notice is a flag, not a licence.
- **Fix what you find, yourself.** A list of findings handed up is a failed stage — you are here to
  leave the code better, not to describe what is wrong with it.
- **Hand back one line about yourself.** What ran, or what skipped and the reason it gave. The worker's
  report is built out of those lines and the chief checks every skip against them; a stage that says
  nothing cannot be shown to have happened.

## What every stage refuses

- **Never act on a finding you have not confirmed.** It is a hypothesis until it reproduces — a test, a
  trace, a tight argument. A fix applied to a non-finding is a new defect.
- **Never rule on your own work.** Where a stage produces a verdict, the hunt and the ruling go to eyes
  that did not write this code and never hear your account of what you meant by it. Your own eyes knew
  the intent and will forgive it.
- **Never invent a finding to fill a slot.** An empty lane says so, and says why it is genuinely clean.
  Noise trains everyone to stop reading the output, which costs more than the empty lane ever did.
- **Never guess at what you cannot settle.** Materially different ways to do it with no clear winner →
  `mycrew-pipeline:how-to-do`. Genuine ambiguity about what the behaviour *should* be → flag it and
  keep going; that one is never yours to decide, and never a reason to stop.
