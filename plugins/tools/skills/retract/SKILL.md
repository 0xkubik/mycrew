---
name: retract
description: "Use when the human declares recorded information wrong or dead ('X is not true', 'there will be no X', 'we dropped X'). Every place stating it, across docs, CLAUDE.mds and persistent memory, is removed or corrected, and each touch reported."
argument-hint: "<the claim + the action: cut entirely, or replace with the new fact>"
---

# retract — remove or correct a wrong statement across the repo

Carry out the human's ruling on a claim. How it runs depends on the ruling.

## Steps

1. **Right the claim and the action.** One call handles one claim. The action is either **cut** — the
   fact is dead, remove every trace — or **replace** — correct it with the new truth the human stated.
   Vague input ("the docs are stale") → ask what exactly is wrong and what to do before touching
   anything.
2. **Find every place it is stated.** Search by meaning, not one literal string — the fact hides under
   synonyms, translations, derived phrasing. Search the docs tree, every `CLAUDE.md` up to the product
   root, sibling doc repos, persistent memory. Stop when new searches stop finding new places.
3. **Cut or correct each place.** For a **cut**: remove the sentence, bullet or line that states it and
   nothing else; a file that exists only for that fact goes whole. For a **replace**: swap the fact for
   the human's stated truth — no invented replacement, no new ideas riding in. A matching persistent
   memory is edited the same way, and its `MEMORY.md` index line with it.

5. **Report every touch.** The file, what was removed or changed, and each dependent left alone. An edit
   missing from the report did not happen.

## Done

- **Every stated trace is gone or corrected.** New searches for the claim turn up nothing.
- **Nothing beyond the claim was touched.** Never rewrite what merely builds on the fact — a flow that
  assumes the fact exists is flagged for the human to decide, not reworked here.
