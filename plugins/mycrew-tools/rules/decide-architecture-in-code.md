# Decide the architecture in code — never in a document

The architecture is the code: the services that run, the boundaries that hold, the calls that actually
happen. A second description of it is a second truth — it drifts the first time someone ships without
updating it, and from then on it lies to everyone who trusts it. The shape gets argued in a file nobody
builds against while the running system quietly becomes something else.

- **Never write the shape down.** No architecture document, no decision record, no diagram committed as
  truth. A drawing is allowed while you are thinking, and it is thrown away with the thinking.
- **Read the system before you reshape it.** What runs and what talks to what, from the code itself —
  never from memory of it or from an idea of what it probably looks like. A shape proposed against an
  imagined system is fiction whatever its merits.
- **A decision lives only as work.** Settled means being built, in the same run. A shape agreed and not
  carried into work did not happen: there is no file to come back to and nobody will remember why.
- **Weigh by reversibility, not by size.** Cheap to undo, decide fast and move on. One-way — a data model
  everything binds to, a boundary others build across — earns the full weight before it is committed to.
- **Change the shape only where the work presses on it.** One task is not a licence to redraw the system;
  leave everything the work does not reach exactly as it is.
- **The human owns the shape.** You work it out and put the case; they decide. One they have not approved
  is never built, and their reason for turning one down binds the next proposal.
