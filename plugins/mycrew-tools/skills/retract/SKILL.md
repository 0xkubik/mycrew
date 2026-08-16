---
name: retract
description: "Use when the human declares recorded information wrong or dead ('X is not true', 'there will be no X', 'we dropped X') — every place that still states it, across the repo's docs, CLAUDE.mds, and persistent memory, ends up deleted or corrected, and every touched spot reported. Removes only what was named, never rewrites around it."
argument-hint: "<the wrong information — one claim, e.g. 'there will be no post versioning'>"
---

# retract — hunt wrong information down and take it out

The human says a recorded fact is no longer true. Find every place that still states it, remove or
correct exactly that, and account for each cut. You are a scalpel, not a rewrite.

## Finding every place it is stated

- **One call retracts one claim.** The argument names a single wrong fact. Handed something vague —
  "the docs are stale" — ask what exactly is wrong before touching anything.
- **Search by meaning, never by one literal string.** The fact hides under synonyms, translations and
  derived phrasing: versioning turns up as versions, as immutable, as "a new copy beside the old".
- **Every surface the project records things on gets searched.** The docs tree, every `CLAUDE.md` up to
  the product root, sibling doc repos of the product, persistent memory. Stop only when new searches
  stop finding new places.

## Cutting it out

- **Take out the sentence, bullet or line that states it and nothing else.** Correct instead of delete
  when the human gave the replacement truth ("no versioning — posts are edited in place"). A file that
  exists only for that fact goes whole.
- **A memory is cut like any other file.** The matching persistent memory is corrected or deleted the
  same way, and its `MEMORY.md` index line with it.
- **A retraction is the one thing that may delete a `features.md` line.** Entries there are otherwise
  permanent; an explicit human retraction takes the line out.
- **Every cut and every flag is reported.** The file, what was removed or changed, and each dependent
  left alone. An edit missing from the report did not happen.

## What never happens

- **Never touch what merely builds on the fact.** A flow that assumes versions exist does not state the
  retracted fact — flag it for the human to decide; reworking it is a new task, not this one.
- **Never invent the replacement.** Only what the human said goes in. No new product idea rides in on a
  correction.
