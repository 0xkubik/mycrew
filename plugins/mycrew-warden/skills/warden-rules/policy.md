# The policy — what each trigger earns

One row per trigger, one column per move. A tick is a duty, not a permission: land on that row and the
move happens. A cross is a prohibition: the move is not made on that trigger, however reasonable it
feels at the time. The judgment is in choosing the row and never in choosing the cell — that is what
makes a watch predictable enough to be trusted, and what stops a hard call from quietly becoming a
silent one. A trigger with no row of its own earns a journal line and nothing else, and where more than
one row fits, every duty across all of them applies. The table is the tunable: a precedent that changes
what a trigger earns is written here as a changed cell, never carried in someone's head.

| trigger | log | stop | gate | release | human | prec |
| --- | :-: | :-: | :-: | :-: | :-: | :-: |
| a session appeared | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| human set a new goal | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| human corrected the work | ✓ | ✗ | ✗ | ✗ | ✗ | ✓ |
| human withdrew or changed the goal | ✓ | ✓ | ✗ | ✗ | ✗ | ✓ |
| human overrode a stop | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ |
| human settled an open case | ✓ | ✗ | ✗ | ✓ | ✗ | ✓ |
| dispatch inside the goal | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| dispatch beyond the goal, unasked | ✓ | ✓ | ✓ | ✗ | ✗ | ✗ |
| dispatch against a standing precedent | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| dispatch irreversible or outside the project | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ |
| a dispatched worker returned | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |
| one file edited over and over, with no end in sight | ✓ | ✓ | ✗ | ✗ | ✗ | ✗ |
| a session that dispatches took the work into its own hands | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ |
| gate returned GO | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| gate returned NO-GO | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| gate returned no verdict | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ |
| stopped session carried on anyway | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ |
| a tick overflowed its cap | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |

**log** a journal entry · **stop** a flag that halts that work · **gate** `why-do-it` in a subagent ·
**release** the message that ends the stop · **human** it goes to them · **prec** a precedent is written

A stop that cites a precedent carries its own reason and closes there — no gate, no second message.
