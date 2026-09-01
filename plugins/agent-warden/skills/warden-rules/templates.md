# The shapes — what a watch keeps, under `.claude/warden/`

`journal.log` — one line per wake, appended, never edited afterwards:

    <ISO time>  <FINDING>  <card>  <SILENT|ACT>  <flags>  <happened> · <done, or why nothing was> · <came of it>

- **FINDING** is the event as it arrived: `CARD`, `UNGATED`, `NOPLAN`, `EARLYDONE`, `STALE`, `MORE` —
  and `START` or `STOP` when the watch itself is put on or put down.
- **flags** is `—` on a SILENT line, and on an ACT the duties that fired, comma-joined, each carrying
  what it produced: `ask`, `flag`, `human`, `case:C00N`. They are `policy.md`'s columns, so a line and
  the table read against each other.
- **The tail is three clauses and never leaves the line.** A clause with nothing in it is `—`.

    2026-08-27T09:12:04Z  CARD       TASK-014  SILENT  —              moved to In Progress by its lead · gated and on a feature, nothing to raise · —
    2026-08-27T09:31:47Z  UNGATED    TASK-017  ACT     ask            from-lead card in progress with no gated label · asked the lead which gate it passed · answered: gate ran, label missed
    2026-08-27T11:02:10Z  STALE      TASK-011  ACT     ask            in progress, untouched three days · asked whether a worker still holds it · the worker had died, card pulled back
    2026-08-27T14:20:33Z  EARLYDONE  TASK-009  ACT     flag,case:C003 second card closed with criteria open · flagged the card, opened the case · lead reopened it and checked them

`cases/C00N-<slug>.md` — opened the moment a question becomes a flag, closed when the card moves again
or the human settles it:

```markdown
# C001 — <the card and the rule that did not hold>

- **Card:** <id>   **Lead:** <name>
- **Opened:** <ISO timestamp>   **Closed:** <ISO timestamp | open>
- **Rule:** <one line — the rule, as the board's own rule states it>
- **Asked first:** <ISO timestamp — and what came back, or that nothing did>

## What was flagged

<one line — the same words the flag carried>

## Outcome

<what the lead did next, or what the human decided>
```
