---
name: spec-management
description: "Use whenever a spec is written to or changed — the rules every spec obeys: one file for the whole product at docs/specs/spec.md, one `##` section per feature keyed by its id from features.md, and only the detail a feature's one line can't carry. The chief owns them, workers only read. Rules only: what a spec must be, never how one is gathered or by whom."
user-invocable: false
---

# spec-management — the specs, as living documents

A spec carries what a feature's one line can't — mechanics, a contract, a schema, the edge cases.
Specs live in `docs/specs/spec.md` **at the product root**, one file for the whole product;
sub-projects keep no specs of their own.

**You own them — a worker never writes one.** A worker reads the specs it was pointed at; when the work
shows one is wrong or missing, it says so in its report and you write it here, then re-dispatch.

## Rules & concepts — non-negotiable
- **One file, at the product root.** Everything the product must be built to lives in the single
  `docs/specs/spec.md`, beside the root `CLAUDE.md`. Never a second spec file, never one per
  sub-project, and never a spec inside a sub-project's own repo.
- **One `##` per feature, keyed by its id.** Every section heads with the feature's id and line from
  `docs/features/features.md` — `## F004 - <feature>`. No section without a feature behind it: detail
  that serves no feature belongs in `docs/features/notes.md`, not here.
- **A feature spanning repos is still one section.** Its section carries the whole feature, whichever
  repos build it — never split by sub-project. A point names a repo only where that is what the point
  is about.
- **Short points, never prose.** Under a heading there are only `-` bullets, one thought each: a
  constraint to hold to, a wish about how it's implemented, a piece of data the feature's line can't
  carry — a contract, a shape, a limit, a state, an edge case, what counts as done. A paragraph under a
  heading is a spec written wrong.
- **Only what the one line can't carry.** Never a restatement of the feature, never how the code is
  organized (that's the repo's), never the system's shape (that's `model.c4`).
- **Strictly the template shape.** The whole file *is* the `example.spec.md` template shipped beside
  this skill — nothing else.
- **English.** Headings, prose, identifiers — all English.
