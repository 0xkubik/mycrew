---
name: skillsmaker
description: "Use when writing or rewriting a SKILL.md in this repo. The house standard every skill here obeys: what a skill must say, what never goes in one, and the shape of a line — a bold sentence carrying the whole demand, optional detail behind it. Not what a skill does (its own job) but how it is written."
argument-hint: "<the skill to write or rewrite>"
---

# skillsmaker — how a skill is written here

A skill is a **standing constraint** on one kind of work, not a script for doing it. It hands over what
must hold and then trusts the work to be done. Write the one you were asked for by the rules below, and
obey them in it — a skill that breaks the house shape is rewritten, not shipped.

## Every line: a bold demand, then optional detail

- **The bold text is the whole rule, in one short sentence.** Someone reading only the bold lines knows
  everything the skill demands. `**Ids are permanent.**`, `**Never write the design down.**` — obeyable
  on its own, never a label like `**Bulletproof.**` that means nothing until the prose behind it.
- **What comes after the bold is optional.** One to three lines, and only for what the sentence cannot
  carry: the edge, the anti-pattern, the exception. Nothing to add → the bold stands alone.
- **Never stretch one idea across both.** An abstract phrase in bold with the demand unfolding behind it
  is the failure this shape exists to stop: nothing skims, and the rule reaches only whoever reads it all.
- **Sections are named by what they settle.** `What the interface must be`, `Where a thing goes` — a
  heading a reader can act on, never `Step 1`, never a word they have to decode.
- **The skill obeys its own rules, in English.** One preaching brevity in a wall of prose is wrong.

## What a skill must say

- **The invariants, first.** Open the body with what must be true when the work is done; the rest serves it.
- **What the work must come out as, not only how it is decided.** A skill that settles who decides and
  by what process, but never what the result has to be, leaves the outcome to taste.
- **Its boundary — what it covers and where it hands off.** In the body, and in the description too.
- **The exception is written in the rule, or there is none.** A rule that can be rationalized around is
  not a rule — say `never`, say `always`, and say where it stops. Left unsaid, the reader invents it.
- **The description is the only line the router reads.** Open with `Use when…`, give the boundary and
  what the skill guarantees, close with the literal phrases a human types.

## What never goes in

- **Never a numbered procedure.** `1 → 2 → 3` ossifies and goes stale; invariants hold. A skill that
  scripts the order is a checklist, not a skill.
- **Never a hardcoded particular.** No baked-in file list, no magic value, no "then run X" the skill
  cannot know — name the concept, let the invocation supply the rest. Only stable infra may be literal.
- **Never the mechanism in the description.** Step order, subagent counts, "then X" — a description that
  summarises the how becomes the shortcut taken instead of reading the skill.
- **Never what the model already knows.** No tutorial, no background, no paragraph defending a rule.
  Every line binds the work or it is cut.
- **Never a rule that already lives in a sibling.** Point at it by name. The same rule in two files is
  two truths, and one of them starts rotting immediately.
- **Never past one screen — about 70 lines.** Past that you are explaining, not ruling. Cut it, or split
  a template or an example out beside `SKILL.md` and point at it by name.

## Shape

```
skills/<name>/SKILL.md         # optional sibling beside it: a template or an example

---
name: <one word>
description: "Use when … — <boundary + what it guarantees>. Triggers: \"…\", \"…\"."
argument-hint: "<what to pass>"     # omit for a pure reference
---

# <name> — <tagline>

<2–4 lines: what this constrains, and the one job it settles.>

## <What this section settles>
- **<The demand, in one short sentence.>** <optional: the edge, the anti-pattern, the exception.>
- **<The next demand, standing alone.>**
```
