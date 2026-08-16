---
description: "Use when the product's technical shape is in question — for one feature or across the whole product — and the answer has to be reasoned rather than picked. Several shapes are worked out independently, each is put to a critic whose only job is to break it, and one survives with the case for it and against every alternative it beat. Ends in work, never in a document. Triggers: \"propose an architecture\", \"how should this be structured\", \"what shape should this take\"."
argument-hint: "[the feature or question to shape — or nothing for the whole product]"
---

# /propose-architecture — work the shape out, defend it, then build it

You **invent the technical shape and argue for it** — not a menu of options handed to the human to
sort out. One recommendation comes back, with why it won and why each alternative lost. It is worth
nothing until it is built, so the run does not end at the answer. Run at the **product root**.

## Ground first

**Load `mycrew-product:architecture-rules`** — it governs every choice made here, including the one
that matters most: nothing is written down. Then get real ground under the question:

- **The system as it is** — the sub-projects the product `CLAUDE.md` names, and what their code
  actually does today. Read it. This is the only architecture there is.
- **What it must carry** — the North Star in the root `CLAUDE.md`, `docs/product/features.md`, and the
  feature's own file when the question belongs to one feature.
- **The question, in one sentence** — what is being decided, and what "best" means *for this decision*:
  the criteria the final answer is scored against. Skip these and the comparison is taste wearing a
  suit.

## How it runs — one Workflow, three phases

- **Shape.** Several agents in parallel, each working out one whole shape on its own, from an angle
  that genuinely diverges from the others — angles chosen for *this* question, never a fixed set, and
  never the same shape three times with the parts moved. Each returns its shape concretely, the bet it
  makes, what it deliberately gives up, and where it is weakest.
- **Kill.** Every shape goes to a critic that did not write it, whose only job is to **break** it:
  where it fails, what it costs six months from now, which assumption it quietly rests on, what it
  makes impossible later. A critic that comes back approving has not done the job.
- **Settle.** One pass over everything. What every shape agreed on goes in. Where they genuinely
  disagree is the real choice — score the survivors against the framed criteria and pick **one**.
  Never a menu, and never the nicest-sounding proposal taken as-is.

## What comes back

One recommendation, in plain human language, no jargon — they decide on the case, not the vocabulary:

- **the shape**, concretely — what exists, what owns what, where the boundaries run
- **why this one** — the case against the criteria that were framed
- **why not the others** — every rejected shape named, with the specific thing that killed it
- **what it rests on** — each assumption with a falsifiable signal that would prove it wrong

Put the verdict itself through `AskUserQuestion`.

## Then it is built

Approved → it goes into work **in the same run**: to the chief to decompose across the sub-projects,
or straight to a worker when it lives in one. Turned down or reshaped → take their reason, which binds
the next attempt, and settle again. **Nothing is left behind either way** — no summary file, no
decision record, no committed diagram. A shape nobody built is a shape nobody decided.
