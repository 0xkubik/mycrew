# The shapes — the three files a watch keeps, under `.claude/warden/`

`journal.md` — one entry per trigger, appended, newest at the bottom:

```markdown
## <ISO timestamp> · <session, as the human would name it> · <HUMAN | DISPATCH | NEW>

- **Saw:** <what the event was, one line>
- **Judged:** <silent | flag | escalate> — <what it was weighed against, one line>
- **Did:** <nothing | the flag, in the words it was sent | opened C00N>
```

`cases/C00N-<slug>.md` — opened the moment a flag goes to a gate, closed when the work resumes or dies:

```markdown
# C001 — <the work that was stopped>

- **Session:** <name>
- **Opened:** <ISO timestamp>   **Closed:** <ISO timestamp | open>
- **Goal it was given:** <one line>
- **What diverged:** <one line — the same words the flag carried>

## Verdict

<GO | NO-GO | unsettled — what the human must decide>

<the reason the gate gave, in its own words>

## Outcome

<what the session was told, and what it actually did next>
```

`precedents.md` — one line per decision the human made, appended, and binding on every later verdict:

```markdown
- **<short name>** — <the situation, one clause> → <what they decided>. Their words: "<quoted>". (C00N)
```

A precedent that cannot quote the human is not a precedent — leave it out and ask them again.
