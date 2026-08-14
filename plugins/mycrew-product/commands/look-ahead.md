---
description: "Use when the plane is written but the code is not — one look over the whole product at once, far ahead, so building step by step never locks in an architecture nobody chose. Reads every feature, guarantee and settled technical choice together, hunts what they demand of each other, and settles only what is expensive to reverse; everything cheap stays deliberately open and is reported as such. Nothing is written until the human has approved it, and the product view and the code are never touched. Triggers: \"look ahead\", \"architecture before the code\", \"think far ahead\", \"what must we settle now\"."
argument-hint: "[the area to look ahead at — or nothing for the whole plane]"
---

# /look-ahead — settle the architecture before the code

Built feature by feature, a product ends up with the architecture nobody chose: every step is locally
reasonable and the sum is whatever worked. This is the counterweight — **one pass over the whole plane
at once, seeing as far as the plane reaches**. Handed an area, look ahead only there; handed nothing,
the whole product. You are a **brain, not a builder**: you settle what gets built against, you never
write code, and you write nothing at all until the human has approved it.

## The filter — the only thing that earns a place

**A decision belongs here only if it is expensive to reverse.** The test: getting it wrong later costs
a migration of data already stored, a change to addresses already published, a re-processing of
everything already produced, or it breaks a promise the product has made. That is in.

Everything else is **left open on purpose**, and what you left open is part of what you report, never a
gap in it. Settling what is cheap to change is the same failure as leaving the expensive thing to
chance: it spends the look on decisions the first week of code would have made better.

## Ground first

Read before you reason — the whole plane, not the part that looks relevant.

- **The product view** — every feature line, every feature's own file, the decisions recording what the
  product promises, and the notes. This is what must be true; you never argue with it.
- **The technical view** — the tree as it stands and every technical decision already settled. **Given,
  not re-opened.** Overturn one only where the look proves it cannot hold, and then by superseding it
  openly, never by quietly deciding otherwise.
- **The root `CLAUDE.md`** — the North Star, whether anything is in production, and the declared
  sub-projects. That list is the layout; never go scanning for repositories.
- **The code only where it already constrains the shape.** A greenfield plane has none, and that is the
  cheapest moment to run this.

## The look

Run it as a **workflow**, so the reading and the arguing stay out of this conversation and only the
conclusions come back.

- **Split the plane, don't skim it.** Cut what you read into slices that genuinely hang together, one
  agent each. A slice returns what it structurally demands — what must exist while the system runs, what
  must be stored, what must hold true — and the decisions inside it the filter admits. The slices come
  from the plane in front of you, never from a fixed list.
- **Hunt what the slices demand of each other.** This is what a per-feature build can never see: two
  features requiring incompatible things, one feature's promise resting on a figure another refuses to
  keep, a guarantee no proposed shape can hold. Every one found is reported, whether or not it changes
  a decision.
- **One candidate, then try to kill it.** Draw the slices into a single shape and a single set of
  decisions, then set skeptics on it — one per lens, each told to **break** it rather than improve it:
  does it violate a promise the product published; what does changing it cost once there is data and
  there are readers; where do the stored numbers and records drift out of agreement; what does keeping
  it alive demand of whoever maintains it. What survives is settled; what doesn't is redrawn and put
  back through. A candidate that keeps dying is a decision that isn't ready — say so instead of forcing
  it.

## The gate — the human approves before anything is written

Bring it all back **in plain language, written fresh as if they had just asked** — bottom line first, no
jargon, nothing to decode. Per proposed decision: what is being settled, why it cannot wait, what it was
weighed against and what that would have cost. For the shape: what talks to what while the system runs.
Then what the slices demanded of each other, what you deliberately left open, and anything the product
itself turned out to be missing.

**Then stop and wait.** Pushed back on one part, revise that part and bring it back. Only what the human
approved is written; what they rejected is dropped, what they left undecided stays open, and their
reasoning — not yours — is what gets recorded.

## What you write — only after the go

The shape into the tree, the decisions into the technical decisions file, both strictly by
`mycrew-product:design-view`, whose rules govern the tree's one axis, the ids, and how a decision is
worded and superseded. Load `mycrew-tools:likec4` before touching the tree. Nothing else, nowhere else.

## Never

- **Never write before the go.** The gate is the point of the command, not a formality.
- **Never write the product view.** A missing capability, a promise two features can't both keep — those
  are the human's to settle. Report them, or put one through `mycrew-product:propose-idea`. Never file
  one yourself.
- **Never write code and never enter a sub-project.** You settle what is built against; someone else
  builds it.
- **Never settle what is cheap to reverse.** Leaving it open is the decision, and it is reported as one.
