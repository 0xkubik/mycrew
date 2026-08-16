---
name: rulesmaker
description: "Use when writing or rewriting a rule file in .claude/rules/. The house standard every rule here obeys: what a rule must say, what never goes in one, and the shape of a line — a bold sentence carrying the whole demand, optional detail behind it. Not what a rule demands (its own job) but how it is written."
argument-hint: "<the rule to write or rewrite>"
---

# rulesmaker — how a rule is written here

A rule is an **always-on constraint** on how work is done: loaded with every task, obeyed without being
invoked. Not a skill, which is summoned for one job, and not a procedure, which runs in order. Write the
one you were asked for by the rules below, and obey them in it — a rule that breaks the house shape is
rewritten, not shipped.

## Every line: a bold demand, then optional detail

- **The bold text is the whole demand, in one short sentence.** Someone reading only the bold lines knows
  everything the rule asks of them. `**Finish and stop.**`, `**Follow the repo's established workflow.**`
  — obeyable on its own, never a label like `**Scope.**` that means nothing until the prose behind it.
- **What comes after the bold is optional.** One to three lines, and only for what the sentence cannot
  carry: the violation, the edge, the exception. Nothing to add → the bold stands alone.
- **Four to six bullets, and no more.** A rule is re-read in every context it loads into; past six
  demands it is a manual, and nobody re-reads a manual.
- **The rule obeys itself, in English.** One demanding brevity is never three paragraphs.

## What a rule must say

- **The title is the whole rule.** `# <Verb-first demand> — <the sharp clarifier>`, and everything under
  it is elaboration. The filename is its kebab-case echo: `write-less-code.md`.
- **Open with the failure it prevents.** Two to four lines on what concretely goes wrong without this
  rule. A cost the reader can feel is a rule that gets kept — motivate first, demand second.
- **Show the violation, not only the virtue.** `i += 1  # increment i`, a `try/catch` that swallows, a
  branch handling the one value that broke. Concrete anti-patterns close the loopholes praise leaves open.
- **The exception is written in the rule, or there is none.** Close with the bullet naming where the rule
  legitimately stops: the documented workaround, the convention that overrides it, the floor it never
  crosses. Left unstated, the reader invents it.

## What never goes in

- **Never two concerns in one file.** If the title needs an "and", it is two rules — split them. A vague
  banner over unrelated demands is a rule nobody obeys.
- **Never a procedure — say what must be true.** A rule holds across every task at once, so it can never
  assume a stage or a next step. No `1 → 2 → 3`, no workflow, no "then run X"; that is a skill's job.
- **Never a path, a library or a command.** A rule installs into any repo: name the concept — the
  project's logger, the repo's established workflow, the pattern already there — never one project's
  specifics.
- **Never frontmatter.** A rule is always loaded: there is nothing to route and nothing to invoke.
- **Never past one screen — about 30 lines.** A rule sits in every context and pays its cost every turn;
  make it worth the tokens. Wrapped near 100 columns.

## Shape

```
.claude/rules/<verb-first-name>.md

# <Imperative demand> — <clarifier>

<2–4 lines: the failure this prevents, concretely.>

- **<The demand, in one short sentence.>** <optional: the violation, the edge, the exception.>
- **<The next demand, standing alone.>**
- **<Where the rule legitimately stops.>** <the exception, or the floor it never crosses.>
```
