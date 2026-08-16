---
description: "Use when the product's interface is in question — one surface or the whole thing — and the answer has to be reasoned rather than picked. Several directions are worked out independently, each is put to a critic whose only job is to break it against a real person using it, and one survives with the case for it and against every alternative it beat. Ends in work, never in a document. Triggers: \"propose a design\", \"how should this look\", \"what should this screen be\"."
argument-hint: "[the surface, flow or feature to design — or nothing for the whole product]"
---

# /propose-design — work a direction out, defend it, then build it

You **invent the interface and argue for it** — not a menu of options handed to the human to sort out.
One recommendation comes back, with why it won and why each alternative lost. It is worth nothing
until it is built, so the run does not end at the answer. Run at the **product root**.

## Ground first

**Load `mycrew-product:design-rules`** — it governs every choice made here, including the one that
matters most: nothing is written down. Then get real ground under the question:

- **The product as it runs** — open it and look at the surfaces that exist, the patterns they already
  use, the words they already use. This is the only design there is. Nothing built yet → the features
  are the ground.
- **What it must carry** — the North Star in the root `CLAUDE.md`, `docs/product/features.md`, and the
  feature's own file when the question belongs to one feature.
- **Whatever the human has said about how they see it** — in this session or handed in with the
  request. It binds every direction proposed; a direction that ignores it is not a direction, it is a
  different product.
- **The question, in one sentence** — what is being decided, and what "best" means *for this decision*:
  the criteria the final answer is scored against.

## How it runs — one Workflow, three phases

- **Direct.** Several agents in parallel, each working out one whole direction on its own, materially
  different from the others — a different idea of how the thing is used, not the same layout with the
  spacing changed. Each returns what a person sees and does, step by step, what it bets on, and what
  it gives up.
- **Kill.** Every direction goes to a critic that did not write it, whose only job is to **break** it:
  put a real person in front of it and find where they stall, misread it, or cannot get back. What it
  costs once the product has ten times the content. Where it fights what is already built. A critic
  that comes back approving has not done the job.
- **Settle.** One pass over everything. What every direction agreed on goes in. Where they genuinely
  disagree is the real choice — score the survivors against the framed criteria and pick **one**.
  Never a menu, and never the prettiest proposal taken as-is.

## What comes back

One recommendation, in plain human language, no jargon — they decide on the case, not the vocabulary:

- **the direction**, concretely — what is on screen, what a person does, what happens next
- **why this one** — the case against the criteria that were framed
- **why not the others** — every rejected direction named, with the specific thing that killed it
- **what it rests on** — each assumption about the person using it, and what would prove it wrong

Put the verdict itself through `AskUserQuestion`.

## Then it is built

Approved → it goes into work **in the same run**: to the chief to decompose, or straight to a worker
when it lives in one repo. Turned down or reshaped → take their reason, which binds the next attempt,
and settle again. **Nothing is left behind either way** — no summary file, no mockup, no spec. A
direction nobody built is a direction nobody decided.
