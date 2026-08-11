---
name: spec-management
description: "Use when a feature's one-liner is not enough and the detail belongs in docs/specs/ at the product root — the chief owns the specs, workers only read them. The shaping rules are not written yet; this holds the ownership boundary only."
user-invocable: false
---

# spec-management — the specs, as living documents

Not written yet. Specs live in `docs/specs/` **at the product root** — detailed descriptions (a
feature's mechanics, a contract, a data schema) where a `features.md` one-liner is not enough. One
set for the whole product; sub-projects keep no specs of their own.

**You own them — a worker never writes one.** A worker building in a repo reads the specs it was
pointed at. When the work shows a spec is wrong or missing, the worker says so in its report and you
write it here first, then re-dispatch.

The rules for shaping them come later.
