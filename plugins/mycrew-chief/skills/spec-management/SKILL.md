---
name: spec-management
description: "Use for the product's specs — detailed feature and contract descriptions in docs/specs/ at the product root, where a feature's one-liner is not enough. The chief owns them; workers build to them. Placeholder: the rules are not written yet."
argument-hint: "<the spec to shape or grow>"
---

# spec-management — the specs, as living documents

Not written yet. Specs live in `docs/specs/` **at the product root** — detailed descriptions (a
feature's mechanics, a contract, a data schema) where a `features.md` one-liner is not enough. One
set for the whole product; sub-projects keep no specs of their own.

**You own them — a worker never writes one.** A worker building in a repo reads the specs it was
pointed at. When the work shows a spec is wrong or missing, the worker says so in its report and you
write it here first, then re-dispatch.

The rules for shaping them come later.
