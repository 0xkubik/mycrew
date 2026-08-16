# The two shapes — fill in the one the kind calls for

`kind: rule` — a standing constraint on how a kind of work is done:

```markdown
---
name: <one word>
kind: rule
description: "Use when … — <the boundary, and what must hold>."
argument-hint: "<what it constrains>"    # omit unless the constraint has a target
---

# <name> — <what it constrains>

<2–4 lines: the work this binds, and the one thing it settles.>

## <What this section settles>
- **<The demand, in one short sentence.>** <optional: the edge, the anti-pattern, the exception.>
- **<The next demand, standing alone.>**

## What never happens
- **<Never …>** <what breaking it looks like.>
```

`kind: intent` — one act, invoked and finished:

```markdown
---
name: <one word>
kind: intent
description: "Use when <the trigger> — <what the run ends with>. Triggers: \"…\", \"…\"."
argument-hint: "<the target>"            # [optional] when the run can take stock on its own
---

# <name> — <the act, as a verb phrase>

<2–4 lines: what this run must end with, and what it is not.>

## <What the run ends with>
- **<The end state, in one short sentence.>**

## <How it runs>
- **<The move.>** <what it takes in, what it leaves behind.>

## What never happens
- **<Never …>** <the widening, the guess, the thing left unreported.>
```
