---
description: "Walk the human through business questions the chief has filed as decisions — grouped or solo depending on what each one actually needs, via AskUserQuestion."
---

# /decisions — work through what piled up

Oldest first, until none are left. Judge each decision's weight before asking — this isn't strictly one
at a time:

- **Simple or related ones batch together** — one `AskUserQuestion` call, up to four at once: a line of
  context each, then its fork. Decisions that share context batch too, even if neither is simple alone —
  that's what makes saying the shared part once worth it.
- **Real depth gets its own call, alone** — a decision that needs real explaining, or whose answer might
  change depending on how another lands, isn't batched: two or three plain sentences of context, no
  more, then the fork.

Never pad a question and never lead it — the real options, plainly, either way. Record each answer
against its own decision and close it (`backlog decision --help` for the exact syntax if it isn't
`edit`), then move to what's left.
