# The policy — what each trigger earns

One row per trigger, one column per move the watch can make. A tick means the move is open on that
trigger; a cross means it is not. Nothing else is open: a trigger that is not a row gets a journal line
and nothing more, and a move with no tick in its row is never made, however reasonable it feels at the
time. The table is the tunable — a precedent that changes what a trigger earns is written here as a
changed cell, not carried in someone's head.

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
| gate returned GO | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| gate returned NO-GO | ✓ | ✗ | ✗ | ✓ | ✗ | ✗ |
| gate returned no verdict | ✓ | ✗ | ✗ | ✗ | ✓ | ✗ |
| stopped session carried on anyway | ✓ | ✓ | ✗ | ✗ | ✓ | ✗ |
| a tick overflowed its cap | ✓ | ✗ | ✗ | ✗ | ✗ | ✗ |

**log** a journal entry · **stop** a flag that halts that work · **gate** `why-do-it` in a subagent ·
**release** the message that ends the stop · **human** it goes to them · **prec** a precedent is written

A stop that cites a precedent carries its own reason and closes there — no gate, no second message.
