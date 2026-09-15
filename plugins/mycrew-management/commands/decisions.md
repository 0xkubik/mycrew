---
description: "Walk the human through business questions the chief has filed as decisions, one at a time — short context, then the fork, via AskUserQuestion."
---

# /decisions — work through what piled up

Loop, oldest first, until none are left. Per decision: two or three plain sentences of context, no
more, then the actual fork via `AskUserQuestion` with the real options — never a leading or padded
question. Record the human's answer against that decision and close it (`backlog decision --help` for
the exact syntax if it isn't `edit`), then move to the next.
