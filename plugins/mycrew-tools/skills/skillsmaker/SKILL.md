---
name: skillsmaker
kind: rule
description: "Use when writing or rewriting a SKILL.md in this repo. The house standard every skill here obeys: the two kinds a skill can be — a rule that constrains how work is done, an intent that is the work — what each must say, what never goes in either, and the shape of a line. Not what a skill does (its own job) but how it is written."
argument-hint: "<the skill to write or rewrite>"
---

# skillsmaker — how a skill is written here

A skill is one of two things, and `kind:` in its frontmatter says which. A **rule** constrains how a kind
of work is done: loaded beside the work, obeyed throughout, never finished. An **intent** is the work:
invoked to be carried out, and it ends somewhere. Settle the kind before writing a line — everything below
follows from it. The skill you write obeys these rules too, in English.

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

## Both kinds

- **The body opens with whatever everything else serves.** A rule's invariants, an intent's end state.
- **The exception is written in the rule, or there is none.** A rule that can be rationalized around is
  not a rule — say `never`, say `always`, and say where it stops. Left unsaid, the reader invents it.
- **The description is the only line the router reads.** Open with `Use when…`, then the boundary and what
  the skill guarantees. Never the mechanism: a description that summarises the how becomes the shortcut
  taken instead of reading the skill.
- **Never a hardcoded particular.** No baked-in file list, no magic value, no "then run X" the skill
  cannot know — name the concept, let the invocation supply the rest. Only stable infra may be literal.
- **Never what the model already knows.** No tutorial, no background, no paragraph defending a rule.
  Every line binds the work or it is cut.
- **Never a rule that already lives in a sibling.** Point at it by name. The same rule in two files is
  two truths, and one of them starts rotting immediately.
- **Never past one screen — about 70 lines.** Cut it, or split an example out beside `SKILL.md`. The two
  shapes to fill in are `shape.md`, beside this file.

## kind: rule — a standing constraint on how work is done

- **Say what must be true, never what happens next.** A rule is loaded while other work runs, so it can
  never assume a stage. `1 → 2 → 3` belongs to an intent; here it ossifies and goes stale.
- **Say what the work must come out as, not only how it is decided.** A rule that settles the process but
  never the result leaves the outcome to taste.
- **A rule never finishes and never reports.** There is no run to end and nothing to hand back — it binds
  for as long as the work it constrains lasts.
- **`argument-hint` only if the constraint has a target.** Most rules take nothing.

## kind: intent — one act, carried out and finished

- **Open with what the run must end with.** Define done before anything else, or the model settles it
  alone and settles it early.
- **Order the moves when the order is the point.** An intent owns its whole run, so a sequence is honest
  here — the one place in this repo it is. Order that carries nothing is still cut.
- **Say what it may touch and what it may not.** Name the target; everything outside it is out. An intent
  that widens on its own does more damage than one that does nothing.
- **Say what comes back to the human.** The report, the handoff, the thing that now exists. A run nobody
  hears the end of did not happen.
- **`argument-hint` names the target.** `<required>` when the run is meaningless without one, `[optional]`
  when it can take stock on its own.
