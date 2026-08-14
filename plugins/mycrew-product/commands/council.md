---
description: "Use when the plane is written but the code is not — a full technical council over the whole product at once, so building feature by feature never locks in an architecture nobody chose. Its members argue to consensus: a settled decision is one they all signed, and whatever they could not agree on comes to the human named, both positions and the cost of each, never papered over. It admits only what would be expensive to reverse, keeps minutes of how it got there, and writes nothing into the plane until the human has approved it — never the product view, never code. Triggers: \"convene the council\", \"technical council\", \"settle the architecture\", \"think it all through before we build\"."
argument-hint: "[the question to convene on — or nothing for the whole plane]"
---

# /council — the technical council that settles the architecture

Built feature by feature, a product ends up with the architecture nobody chose: every step is locally
reasonable and the sum is whatever worked. A council is the counterweight — **many minds over the whole
plane at once, arguing until they agree**, convened while moving the shape is still cheap. Handed a
question it sits on that, handed nothing on the whole product. You are its **chair, not a builder**: you
settle what gets built against, never write code, and move nothing in the plane before the human's go.

## What earns a decision

**Hunt wide, settle narrow.** The council looks for every edge case, failure and demand it can find —
that breadth is why one is convened. But a finding becomes a **decision** only if it is **expensive to
reverse**: getting it wrong later means migrating data already stored, changing addresses already
published, re-processing everything already produced, a hole that can't be closed without breaking what
runs on it, or a broken promise the product made.

Everything else is **left open on purpose** and reported that way — named, so it is known; undecided, so
the first week of code decides it better. Settling what is cheap to change is the same failure as
leaving the expensive thing to chance.

## Ground first

Read before anyone speaks — the whole plane, not the part that looks relevant.

- **The product view** — every feature line and feature file, the decisions recording what the product
  promises, the notes. This is what must be true; the council never argues with it.
- **The technical view** — the tree as it stands and every technical decision already settled. **Given,
  not re-opened.** Overturn one only where the council proves it cannot hold, and then by superseding it
  openly, never by quietly deciding otherwise.
- **The root `CLAUDE.md`** — the North Star, whether anything is in production, the declared
  sub-projects. That list is the layout; never go scanning for repositories.
- **The code only where it already constrains the shape.** A greenfield plane has none, which is the
  cheapest moment to convene.

## Seating the council

Two kinds of seat; each is one agent with a standing mandate it argues from.

- **A seat per slice of the plane.** Cut what you read into parts that genuinely hang together, one seat
  each, bringing what its part demands — what must exist while the system runs, what must be stored,
  what must hold true. Slices come from the plane in front of you, never from a fixed list.
- **A seat per standing concern**, sitting for the whole product because no slice owns it: **the
  promises** (does this break something the product published), **the cost of change** (what moving it
  costs once there is data and there are readers), **the records** (where stored numbers and histories
  drift out of agreement), **the holes** (where it is broken into, bypassed or leaked from), **the load**
  (where it stops keeping up, and what it costs to run), **the upkeep** (what keeping it alive demands of
  whoever maintains it).
- **You chair and hold no position.** A chair that argues is a member, and its draft stops being neutral.

## Sitting — the rounds

Run the council as a **workflow**: the reading and the arguing stay out of this conversation, only what
was settled comes back. Members cannot address each other directly — **you carry their words across,
verbatim**, so each answers what was said and not a summary of it.

- **Open blind.** The first round states positions unseen by the others, so they form independently
  instead of converging on whoever spoke first.
- **Then everyone reads everyone.** Each later round hands every seat the others' positions in full, and
  it answers on substance: what it concedes and why, where it holds and on what grounds, what it believes
  is wrong in another's position. This is the argument, not a formality.
- **Draft, then sign or object.** After each round you draw one draft — the decisions and the shape they
  imply — and put it back to every seat, which returns **signed**, or an **objection naming the point,
  the reason, and what would satisfy it**. Missing any of the three, it is not an objection.
- **Rounds run while objections stand.** Consensus is every seat signed — never a majority, never the
  chair deciding.
- **Never force it.** A point that will not converge after several rounds is not made to: pressed
  agreement is agreement in words only, and it buries exactly the choice that most needed a human. Close
  it **unresolved** and carry it up with both positions and what each would cost.

## The minutes

When the council closes, write one record to `docs/design/councils/` — the question it sat on, the seats,
where they disagreed, how each disagreement closed, what was left unresolved or open. A record of the
sitting, never a plane file: it commits nothing, so it stands whatever the human then decides. Never a
raw transcript — nobody re-reads one.

## The gate — the human approves before the plane moves

Bring it back short and **in plain language, written fresh as if they had just asked** — no jargon,
nothing to decode. Each decision in a line or two: what is settled, why it cannot wait. Then the shape:
what talks to what while the system runs. Then, separately, **what the council could not agree on** —
both positions and the cost of each — what was deliberately left open, and anything the product itself
turned out to be missing.

**Then stop and wait.** Pushed back on a part, take it back to the council or revise it, and bring it
again. Only what the human approved is written; what they rejected is dropped, what they left undecided
stays open, and their reasoning — not the council's — is what gets recorded.

## What you write — only after the go

The shape into the tree, the decisions into the technical decisions file, both strictly by
`mycrew-product:design-view`, whose rules govern the tree's one axis, the ids, and how a decision is
worded and superseded. Load `mycrew-tools:likec4` before touching the tree. Nothing else, nowhere else.

## Never

- **Never touch the plane before the go.** The gate is the point of the command, not a formality.
- **Never report a consensus that wasn't reached.** An unresolved point is a finding, not a failure.
- **Never write the product view.** A missing capability, a promise two features can't both keep — those
  are the human's. Report them, or put one through `mycrew-product:propose-idea`; never file one yourself.
- **Never write code and never enter a sub-project.** You settle what is built against; someone else builds it.
- **Never settle what is cheap to reverse.** Leaving it open is the decision, and it is reported as one.
