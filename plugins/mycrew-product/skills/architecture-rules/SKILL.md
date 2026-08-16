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
