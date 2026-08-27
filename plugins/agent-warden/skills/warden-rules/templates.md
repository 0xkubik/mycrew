# The shapes — what a watch keeps, under `.claude/warden/`

`journal.log` — one line per wakeup, appended, never edited afterwards:

    <ISO time>  <TRIGGER>  <session>  <SKIP|ACT>  <flags>  <happened> · <done, or why nothing was> · <came of it>

- **TRIGGER** is the event as it arrived: `HUMAN`, `DISPATCH`, `RETURN`, `NEW`, `CHURN`, `HANDSON`, `MORE` — and
  `START` or `STOP` when the watch itself is put on or put down.
- **flags** is `—` on a SKIP, and on an ACT the duties that fired, comma-joined, each carrying what it
  produced: `stop`, `gate`, `release`, `human`, `case:C00N`, `prec:P00N`. They are `policy.md`'s columns,
  so a line and the table read against each other.
- **The tail is three clauses and never leaves the line.** A clause with nothing in it is `—`.

    2026-08-26T07:21:05Z  HUMAN     227d5c6d  SKIP  —                    design called primitive, mockups still stand · the human redirecting their own session, not drift · goal unchanged
    2026-08-26T09:47:19Z  HUMAN     227d5c6d  ACT   prec:P006            the column rejected twice for one reason · wrote the precedent, named the pattern to them · element stays assigned
    2026-08-26T09:49:45Z  DISPATCH  227d5c6d  ACT   stop,gate,case:C002  a worker sent past the assigned element · stopped that work, put it to the gate · NO-GO, the work was dropped
    2026-08-26T10:36:29Z  RETURN    227d5c6d  SKIP  —                    "dense labelless column" came back · a return earns no verdict · —

`precedents.md` — one line per decision, a thesis carried in the human's own vocabulary:

```markdown
- **P001** · 2026-08-26 · 227d5c6d · the mockups are the standard — what is wrong is the implementation
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
