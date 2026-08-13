---
name: decision-management
description: "Use whenever a settled choice is recorded or changed — the rules every decision obeys: one file for the whole product at docs/decisions.md, a permanent D000 id, the decision itself as the heading, and beneath it only why it won and what would overturn it. Superseded, never deleted. The chief owns it, workers only read. Rules only: what a decision must be, never how one is reached or by whom."
user-invocable: false
---

# decision-management — what was settled, and why

A decision records a choice that is closed — a rule, a constraint, a mechanism, a way the product is
to exist, something deliberately not done — together with the reasoning that closed it. It belongs to
no single feature, so no feature's points can hold it, and it is permanent, so notes must not. Written
down, it stops being re-argued every few weeks, and a later reader can tell a decision from an accident.

Decisions live in `docs/decisions.md` **at the product root**, one file for the whole product.

**You own it — a worker never writes one.** A worker reads the decisions that bind its work; when the
work shows one is wrong or missing, it says so in its report and you write it here, then re-dispatch.

## Rules & concepts — non-negotiable
- **One file, at the product root.** Every settled choice for the whole product lives in
  `docs/decisions.md`, beside the root `CLAUDE.md`. Never a second decisions file, never one per
  sub-project, and never one inside a sub-project's own repo.
- **Every decision carries a permanent id.** Each section heads with `D` and a zero-padded
  three-digit number. Ids run in order from the highest already taken, and are **never reused and
  never renumbered** once given.
- **The heading is the decision itself, and it is dated.** One line naming what was chosen and — where
  there was a real alternative — what it was chosen over, closing with the day it was settled:
  `## D004 — The job queue is a Postgres table, not Redis · 2026-08-13`. A heading that names a topic
  instead of a choice is a decision not yet made.
- **Beneath it, only the reasoning and its ceiling.** Short `-` points, one thought each: why this
  won, what it was weighed against and what that would have cost, the known limit where it stops
  working, what would overturn it. A paragraph under a heading is a decision written wrong.
- **Never the other planes' content.** Not what the product does (that's `docs/features.md`), not how
  a feature must behave (that's the points under that feature), not the system's shape (that's
  `model.c4`), not how the code is organized (that's the repo's).
- **Name the feature only when the decision is about one.** A decision serving a single feature ends
  its heading with that feature's id — `(F004)`. Most decisions serve the whole product and name none.
- **Superseded, never deleted.** A decision that no longer holds stays, its heading marked
  `— superseded by D0NN`, and the choice that replaced it is a **new** entry with a new id. The record
  of a wrong turn is worth more than a clean file.
- **Strictly the template shape.** The whole file *is* the `example.decisions.md` template shipped
  beside this skill — nothing else.
- **English.** Headings, prose, identifiers — all English.
