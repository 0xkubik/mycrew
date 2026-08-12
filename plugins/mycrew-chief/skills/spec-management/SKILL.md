---
name: spec-management
description: "Use whenever a spec is written to or changed — the rules every spec obeys: one file per sub-project at docs/specs/<sub-project>/spec.md, one `##` section per feature keyed by its id from features.md, and only the detail a feature's one line can't carry. The chief owns them, workers only read. Rules only: what a spec must be, never how one is gathered or by whom."
user-invocable: false
---

# spec-management — the specs, as living documents

A spec carries what a feature's one line can't — mechanics, a contract, a schema, the edge cases.
Specs live in `docs/specs/` **at the product root**, one set for the whole product; sub-projects keep
no specs of their own.

**You own them — a worker never writes one.** A worker reads the specs it was pointed at; when the work
shows one is wrong or missing, it says so in its report and you write it here, then re-dispatch.

## Rules & concepts — non-negotiable
- **One file per sub-project.** Everything a sub-project must be built to lives in
  `docs/specs/<sub-project>/spec.md`, the folder named for that sub-project exactly as the root
  `CLAUDE.md`'s Sub-projects list names it. Never a second spec file for the same sub-project, and never
  a spec inside the sub-project's own repo.
- **One `##` per feature, keyed by its id.** Every section heads with the feature's id and line from
  `docs/features/features.md` — `## F004 - <feature>`. No section without a feature behind it: detail
  that serves no feature belongs in `docs/features/notes.md`, not here.
- **A feature spanning repos gets a section in each.** The same id appears in every sub-project's
  `spec.md` that carries part of it, each section describing **only that repo's part** — never the whole
  feature restated in several files.
- **Short points, never prose.** Under a heading there are only `-` bullets, one thought each: a
  constraint to hold to, a wish about how it's implemented, a piece of data the feature's line can't
  carry — a contract, a shape, a limit, a state, an edge case, what counts as done. A paragraph under a
  heading is a spec written wrong.
- **Only what the one line can't carry.** Never a restatement of the feature, never how the code is
  organized (that's the repo's), never the system's shape (that's `model.c4`).
- **Strictly the template shape.** A spec file *is* the `example.spec.md` template shipped beside this
  skill — nothing else.
- **English.** Headings, prose, identifiers — all English.
