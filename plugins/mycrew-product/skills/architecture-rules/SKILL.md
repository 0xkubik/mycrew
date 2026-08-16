---
name: architecture-rules
description: "Use whenever the product's technical shape is being decided — how it splits into services and sub-projects, what owns what, where a boundary runs, what talks to what. The house stance: the running code is the only architecture there is, so a shape is settled by building it and never by writing it down. Rules only: what must hold when the shape is chosen, never who chooses it or how a proposal is worked out."
user-invocable: false
---

# architecture-rules — how the product's shape is decided

The architecture **is the code** — the services that run, the boundaries that hold, the calls that
actually happen. Nothing standing beside it describes it. So deciding the shape ends in exactly one
place: work that changes that code.

## Rules & concepts — non-negotiable

- **Never write the architecture down.** No architecture document, no decision record, no diagram
  committed as truth, no section in the plane. A second description of the system is a second truth:
  it drifts the first time someone ships without updating it, and from then on it lies to everyone
  who trusts it. The code answers what the system is; go and read it.
- **Read the system before you shape it.** What exists, what runs, what already talks to what — from
  the code itself, never from memory of it and never from an idea of what it probably looks like. A
  shape proposed against an imagined system is fiction whatever its merits.
- **A decision lives only as work.** Settled means being built — the same run, handed to whoever
  builds it. A shape agreed and not carried into work did not happen, because nothing holds it: there
  is no file to come back to and nobody will remember the reasoning.
- **Boundaries follow the declared sub-projects.** The product `CLAUDE.md` names them and that list is
  the map — never discovered by scanning, never quietly redrawn. Splitting or merging sub-projects is
  the human's call, not a shaping decision.
- **Change the shape only where the work presses on it.** One feature is not a licence to redraw the
  system. Touch the boundaries that block the work; leave everything the work does not reach exactly
  as it is.
- **Weigh by reversibility, not by size.** A choice that is cheap to undo gets decided fast and moves
  on. A one-way one — a data model everything will bind to, a boundary others will build across,
  anything the outside world starts depending on — earns the full weight before it is committed to.
- **A per-task fork is not architecture.** Materially different ways to implement one task inside one
  repo are `mycrew-pipeline:how-to-do`'s. Here you decide only what shape the product has; how a piece
  of it gets written is settled where the writing happens.
- **Draw only to think.** A diagram is allowed as a scratch aid while reasoning —
  `mycrew-tools:likec4` when one genuinely helps — and it is thrown away with the reasoning. A drawing
  that gets committed has become an architecture document under another name.
- **The human owns the shape.** You work it out and put it to them with the case; they decide. A shape
  they have not approved is never built, and their reason for turning one down binds what you propose
  next.

## What the shape must be

- **The stack is chosen for who writes it.** An agent writes this code, so nobody's existing languages
  narrow the field — only what the job needs and what can be written correctly at volume: mature
  libraries, unambiguous semantics, mistakes caught by the compiler rather than in production. Never a
  technology picked because someone already knows it, and never one settled before the product it is for.
- **Quality over speed, and optimal over both.** Never the fastest thing that ships — the shape you would
  still want running a year from now. Never the grandest either: the best shape meets the demand exactly,
  and everything past that is cost nobody is paying for.
- **Configuration has one home.** Every constant, setting and tunable lives in one place a person can
  open and read whole; nothing is buried where it happens to be used. A value that has to be hunted for
  across the tree is a value nobody dares change.
- **The smaller system wins.** Between two shapes that both carry the work, take the one with fewer
  moving parts — fewer components, fewer hops, fewer things to keep alive. How the code inside them is
  written is the house rules' business; here it is the count of parts that decides.
- **Parts stay substitutable.** Each piece owns its own data and is reached only through a narrow
  interface, so it can be replaced without the rest noticing. A shape whose pieces know each other's
  insides can never be changed one piece at a time — and one piece at a time is the only way a product
  that is already running ever changes shape.
- **Reach for the best shape, not the one already there.** Existing code is evidence of a decision once
  made, never proof it is still right, and working is not the same as best. The product moves and what
  fit it stops fitting — say so and rewrite it, as its own decision put to the human and its own work,
  never smuggled into a feature that happened to touch it.
- **Decide against what is coming.** Name the pressure this shape will meet before it meets it — where
  the load lands, what the product is plainly going to want next, which choice would be expensive to
  undo — and choose so none of it becomes a rewrite. Only pressure you can already see counts; building
  for a future nobody has asked for is the opposite failure and costs just as much.
