---
name: rulesmaker
description: "Use when writing or rewriting a rule file in rules/. Groups related rules into domain files, each rule compressed to a2-3 sentence bullet."
argument-hint: "<the rule to write or rewrite>"
---

# rulesmaker — write rules as dry bullets grouped by domain

Writes rule files under `rules/`, one per domain. A rule is an always-on constraint: loaded with every
task, obeyed without being invoked. Each rule is one bullet — compressed, factual, no padding. Finished
when the rule file matches the format below.

## Format

- **File name** `working-with-<domain>.md`, or `working-in-<domain>.md` for environments.
- **Bold part** is the demand itself, one short phrase — not a label, the thing to obey.
- **Sentences** run what it demands, how it behaves, where it stops. Third sentence only when there is
  a legitimate exception.
- **No more than eight bullets per file.** Past eight → the domain is too broad, split it.

## What never goes in

- **No procedures** — `1 → 2 → 3` is a skill, not a rule; rules hold across every task at once.
- **No hardcoded values** — name the concept, not one project's specifics.
- **No frontmatter args** — rules are always loaded, nothing to route.
- **No one concern per bullet** — a bullet needing "and" is two rules, split it.
- **No motivation** — "this is important because..." is noise.

## Where it stops

- **Stops at the written rule file.** No further work: no explaining why, no adding context, no
  polishing. Replace the bullet in place and move on.
