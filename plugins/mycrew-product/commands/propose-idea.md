---
description: "Use when the product needs ideas it doesn't hold yet — the endless loop at the product root: one invented idea at a time, pitched with the case for it, filed into the milestone list only on their approval, and the next one in the same breath. Every idea, approved or rejected, is recorded with their own reason as a backlog decision and binds every later pitch, and it ends only when they stop. The counterpart to /braindump and /ask-me: those draw the human's vision out, this one puts an idea of its own in."
argument-hint: "[an angle to invent along — or nothing to range across the whole product]"
---

# /propose-idea — invent an idea, pitch it, keep the verdict, pitch the next

The **one place mycrew contributes a product idea of its own**. Everywhere else the product plane is
strictly extractive — `/braindump` listens and `/ask-me` questions, and neither adds to it. Here you invent:
features and improvements the plane doesn't hold yet, each put to the human with the case for it. You
**never decide** — only their approval puts a milestone in the index, and every verdict, yes or no, is
recorded as a backlog decision and binds what you pitch next. Run at the **product root**.

## The loop

1. **Pitch one idea**, and put the verdict through `AskUserQuestion` with the answer already in its
   options. What it is and why it is worth doing comes first, in plain language; the question comes
   after the case, never in place of it.
2. **File the verdict the moment it lands** — the decision and its body, approved or rejected alike —
   and let it bind what you pitch next.
3. **Widen or dig.** A fresh angle the moment a vein is spent: who the product fails today, what it
   does badly, what the North Star implies and nobody has written down. Prefer the corner nothing has
   been pitched into yet.
4. **Pitch the next one immediately** — in the same breath, no pause, no closing summary.

## Rules & concepts — non-negotiable

- **Load the rule set first** — `mycrew-product:product-rules`. It governs where an approved idea
  lands and in what shape, and it is what you obey the moment the human affirms anything at all here.
- **Ground before you invent.** Read the North Star in the root `CLAUDE.md`, `backlog milestone list`,
  every `backlog decision` — then look at what the sub-projects actually
  are. An idea that restates something already listed, already built, or already pitched is not an idea;
  find a real gap.
- **The decisions bind you.** A rejected idea is **never** re-pitched. The one exception: something
  material changed since — the product moved, the reason no longer holds — and then the pitch opens by
  naming exactly what changed. Run `backlog decision list` every run, and read the body of any decision
  that bears on the pitch, before the first pitch.
- **Serve the North Star, not novelty.** Every idea must close a real gap between what the product is
  and where it's going. Inventing to have something to say is one failure mode; declaring the well dry
  is the other, and it is the likelier one — the obvious gaps run out early, and what is left is the
  angle you have not looked from yet.
- **One idea at a time.** Pitch it, take the verdict, file it, then the next — never a menu of five.
- **Pitch in plain human language.** Say what it is and *why it's worth doing* — the gap it closes, who
  it helps, what it costs — before you ask. No jargon: the human decides on the case, not on your
  vocabulary. Put the question itself through `AskUserQuestion`.
- **The options are predicted verdicts with the reason already in them, never a bare yes and no.** Each
  reads as a position someone holds — yes because this is the gap that actually hurts, no because it
  costs more than it returns — and there may be several of each where you can see more than one way
  this lands. A naked yes beside a naked no makes the human type the thinking you were supposed to
  have done; their own words are there for what you failed to foresee, and needing them is the rare
  case rather than the shape of the run.
- **Predict the refusals as hard as the approvals.** The reason they turn an idea down is the thing you
  most need on record, and it is the one you are most tempted to leave for them to write.
- **Approval is the only door into the plane.** An approved idea is filed in their intent, in the shape
  `mycrew-product:product-rules` sets — and that skill decides whether it opens a milestone at all or is
  detail written into a feature the plane already holds (its *only what they affirmed* rule governs what
  may be filed, not what may be pitched — inventing is exactly your job). An idea that varies, completes
  or serves a feature already listed never takes a milestone of its own. Nothing reaches the plane
  unapproved — never approve on the human's behalf, whatever else the session was told.
- **Every verdict is a backlog decision, both halves, always.** `backlog decision create "<idea
  title>" -s accepted|rejected`, then its body written straight after — the three sections filled to
  the shape below. A rejection is filed exactly as carefully as an approval. An idea pitched but not
  recorded never happened.
- **The reason is the human's, however they gave it.** An option they picked is their verdict and
  their reason both — file it exactly as it stands and go to the next idea, never asking them to put
  in their own words what they have just chosen. Anything they typed themselves is recorded as they
  put it, never your reconstruction. Only a bare yes or no with nothing behind it earns a follow-up.
- **Never wrap up.** No summary, no "that's all I have", no "anything else?", no closing. You pitch
  until the human stops you, and running low on easy ideas is a reason to widen the angle rather than
  to end the run.
- **Append, never rewrite.** Decisions are permanent. An overturned verdict is a **new** `backlog
  decision`, never an edit to the old one.
- **The backlog is stood up by `/product-init`.** Not here → say so and stop.

## The decision body

`backlog decision create` writes only the title, status and date and leaves three empty sections. Fill
them straight after, with the editor — a decision has no structured markers, so this is the one file
in the plane written by hand:

```markdown
## Context

<the case as it was put: the gap it closes, who it helps, how it serves the North Star, what it costs>

## Decision

<the verdict — approved | rejected — and the human's reason, in their words>

## Consequences

<what this binds for later pitches: what is now off the table, or what an approved idea now commits the
product to>
```
